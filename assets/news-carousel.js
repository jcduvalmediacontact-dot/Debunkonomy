// News Carousel - Version avec support tactile (swipe)
(function() {
  'use strict';

  let currentSlide = 0;
  let newsData = [];
  let cardsPerView = 3;
  
  // Variables pour le swipe tactile
  let touchStartX = 0;
  let touchEndX = 0;
  let isDragging = false;

  // Formatage de la date
  function formatDate(dateStr) {
    const months = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'];
    const date = new Date(dateStr);
    return `${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}`;
  }

  // Traduction du type
  function getTypeLabel(type) {
    const labels = { 'texte': 'Article', 'video': 'Vidéo', 'podcast': 'Podcast' };
    return labels[type] || type;
  }

  // Créer une carte
  function createNewsCard(item) {
    const card = document.createElement('a');
    card.className = `news-card news-card--${item.type}`;
    card.href = item.link;

    // Image si disponible
    if (item.image || item.youtubeId) {
      const img = document.createElement('img');
      img.className = 'news-card__image';
      img.alt = item.title;
      
      if (item.type === 'video' && item.youtubeId) {
        img.src = `https://img.youtube.com/vi/${item.youtubeId}/maxresdefault.jpg`;
        img.onerror = function() {
          this.src = `https://img.youtube.com/vi/${item.youtubeId}/hqdefault.jpg`;
        };
      } else if (item.image) {
        img.src = item.image;
      }
      
      card.appendChild(img);
    }

    const typeLabel = document.createElement('div');
    typeLabel.className = `news-card__type news-card__type--${item.type}`;
    typeLabel.textContent = getTypeLabel(item.type);

    const content = document.createElement('div');
    content.className = 'news-card__content';

    const date = document.createElement('div');
    date.className = 'news-card__date';
    date.textContent = formatDate(item.date);

    const title = document.createElement('h3');
    title.className = 'news-card__title';
    title.textContent = item.title;

    const excerpt = document.createElement('p');
    excerpt.className = 'news-card__excerpt';
    excerpt.textContent = item.excerpt;

    const cta = document.createElement('div');
    cta.className = 'news-card__cta';
    cta.textContent = item.type === 'video' ? 'Regarder' : 'Lire l\'article';

    content.appendChild(date);
    content.appendChild(title);
    content.appendChild(excerpt);
    content.appendChild(cta);

    card.appendChild(typeLabel);
    card.appendChild(content);

    return card;
  }

  // Calculer le nombre de cartes visibles
  function updateCardsPerView() {
    const width = window.innerWidth;
    if (width < 640) cardsPerView = 1;
    else if (width < 980) cardsPerView = 2;
    else cardsPerView = 3;
  }

  // Mettre à jour la position du carrousel
  function updateCarousel() {
    const track = document.querySelector('.news-carousel__track');
    const prevBtn = document.querySelector('.news-carousel__nav-btn--prev');
    const nextBtn = document.querySelector('.news-carousel__nav-btn--next');
    const dots = document.querySelectorAll('.news-carousel__dot');

    if (!track) return;

    const cardWidth = track.children[0]?.offsetWidth || 0;
    const gap = 24;
    const offset = -(currentSlide * (cardWidth + gap));
    
    track.style.transform = `translateX(${offset}px)`;
    track.style.transition = isDragging ? 'none' : 'transform 0.3s ease-out';

    // Update buttons
    if (prevBtn) prevBtn.disabled = currentSlide === 0;
    if (nextBtn) {
      const maxSlide = Math.max(0, newsData.length - cardsPerView);
      nextBtn.disabled = currentSlide >= maxSlide;
    }

    // Update dots
    dots.forEach((dot, index) => {
      dot.classList.toggle('active', index === currentSlide);
    });
  }

  // Navigation
  function navigate(direction) {
    const maxSlide = Math.max(0, newsData.length - cardsPerView);
    
    if (direction === 'next' && currentSlide < maxSlide) {
      currentSlide++;
    } else if (direction === 'prev' && currentSlide > 0) {
      currentSlide--;
    }
    
    updateCarousel();
  }

  // ===== GESTION DU SWIPE TACTILE =====
  function handleTouchStart(e) {
    touchStartX = e.changedTouches[0].screenX;
    isDragging = true;
  }

  function handleTouchMove(e) {
    if (!isDragging) return;
    touchEndX = e.changedTouches[0].screenX;
  }

  function handleTouchEnd() {
    if (!isDragging) return;
    isDragging = false;
    
    const swipeDistance = touchStartX - touchEndX;
    const minSwipeDistance = 50; // Distance minimale pour déclencher le swipe (en pixels)
    
    if (Math.abs(swipeDistance) > minSwipeDistance) {
      if (swipeDistance > 0) {
        // Swipe vers la gauche = suivant
        navigate('next');
      } else {
        // Swipe vers la droite = précédent
        navigate('prev');
      }
    } else {
      // Pas assez de distance = retour à la position actuelle
      updateCarousel();
    }
    
    touchStartX = 0;
    touchEndX = 0;
  }

  // Créer les dots
  function createDots() {
    const dotsContainer = document.querySelector('.news-carousel__dots');
    if (!dotsContainer) return;

    dotsContainer.innerHTML = '';
    const maxSlide = Math.max(0, newsData.length - cardsPerView);

    for (let i = 0; i <= maxSlide; i++) {
      const dot = document.createElement('button');
      dot.className = 'news-carousel__dot';
      dot.setAttribute('aria-label', `Aller à la diapo ${i + 1}`);
      dot.addEventListener('click', () => {
        currentSlide = i;
        updateCarousel();
      });
      dotsContainer.appendChild(dot);
    }
  }

  // Charger les news
  async function loadNews() {
    const track = document.querySelector('.news-carousel__track');
    
    if (!track) {
      console.warn('News carousel track not found');
      return;
    }

    try {
      const response = await fetch('/news.json');
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      if (!data.news || data.news.length === 0) {
        track.innerHTML = '<div class="news-carousel__loading">Aucune actualité pour le moment.</div>';
        return;
      }

      newsData = data.news.sort((a, b) => new Date(b.date) - new Date(a.date));

      // Créer les cartes
      track.innerHTML = '';
      newsData.forEach(item => {
        track.appendChild(createNewsCard(item));
      });

      // Créer la navigation
      createDots();
      updateCarousel();

      // ===== AJOUTER LES EVENT LISTENERS TACTILES =====
      track.addEventListener('touchstart', handleTouchStart, { passive: true });
      track.addEventListener('touchmove', handleTouchMove, { passive: true });
      track.addEventListener('touchend', handleTouchEnd, { passive: true });

    } catch (error) {
      console.error('Erreur lors du chargement des news:', error);
      // Conserver les cartes statiques si elles existent.
    }
  }

  // Initialisation
  function init() {
    updateCardsPerView();
    loadNews();

    // Event listeners pour les boutons
    const prevBtn = document.querySelector('.news-carousel__nav-btn--prev');
    const nextBtn = document.querySelector('.news-carousel__nav-btn--next');

    if (prevBtn) prevBtn.addEventListener('click', () => navigate('prev'));
    if (nextBtn) nextBtn.addEventListener('click', () => navigate('next'));

    // Responsive
    window.addEventListener('resize', () => {
      updateCardsPerView();
      currentSlide = 0;
      createDots();
      updateCarousel();
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') navigate('prev');
      if (e.key === 'ArrowRight') navigate('next');
    });
  }

  // Start
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
