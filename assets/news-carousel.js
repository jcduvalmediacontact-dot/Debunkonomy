// News Carousel
(function() {
  'use strict';

  // Formatage de la date en français
  function formatDate(dateStr) {
    const months = ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'];
    const date = new Date(dateStr);
    const day = date.getDate();
    const month = months[date.getMonth()];
    const year = date.getFullYear();
    return `${day} ${month} ${year}`;
  }

  // Traduction du type
  function getTypeLabel(type) {
    const labels = {
      'texte': 'Article',
      'video': 'Vidéo',
      'podcast': 'Podcast'
    };
    return labels[type] || type;
  }

  // Création d'une carte news
  function createNewsCard(item) {
    const card = document.createElement('a');
    card.className = `news-card news-card--${item.type}`;
    card.href = item.link;

    // Image (vignette YouTube pour vidéos, image personnalisée pour articles)
    if (item.image || item.youtubeId) {
      const img = document.createElement('img');
      img.className = 'news-card__image';
      img.alt = item.title;
      
      if (item.type === 'video' && item.youtubeId) {
        // Vignette YouTube automatique
        img.src = `https://img.youtube.com/vi/${item.youtubeId}/maxresdefault.jpg`;
        img.onerror = function() {
          // Fallback si maxresdefault n'existe pas
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

    // Icône vidéo si c'est une vidéo
    if (item.type === 'video') {
      const videoIcon = document.createElement('div');
      videoIcon.className = 'news-card__video-icon';
      videoIcon.textContent = '▶';
      content.appendChild(videoIcon);
    }

    card.appendChild(typeLabel);
    card.appendChild(content);

    return card;
  }

  // Chargement et affichage des news
  async function loadNews() {
    const container = document.getElementById('news-carousel-grid');
    
    if (!container) {
      console.warn('News carousel container not found');
      return;
    }

    // Affichage du loading
    container.innerHTML = '<div class="news-carousel__loading">Chargement des actualités...</div>';

    try {
      const response = await fetch('/news.json');
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      if (!data.news || data.news.length === 0) {
        container.innerHTML = '<div class="news-carousel__empty"><p class="news-carousel__empty-text">Aucune actualité pour le moment.</p></div>';
        return;
      }

      // Tri par date (plus récent en premier)
      const sortedNews = data.news.sort((a, b) => new Date(b.date) - new Date(a.date));

      // Affichage des 6 premières news
      const newsToDisplay = sortedNews.slice(0, 6);

      // Création des cartes
      container.innerHTML = '';
      newsToDisplay.forEach(item => {
        const card = createNewsCard(item);
        container.appendChild(card);
      });

    } catch (error) {
      console.error('Erreur lors du chargement des news:', error);
      container.innerHTML = '<div class="news-carousel__empty"><p class="news-carousel__empty-text">Erreur lors du chargement des actualités.</p></div>';
    }
  }

  // Initialisation au chargement de la page
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadNews);
  } else {
    loadNews();
  }
})();
