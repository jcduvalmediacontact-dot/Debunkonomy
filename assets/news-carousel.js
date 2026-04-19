// ==================== NEWS CAROUSEL MANAGER ====================

class NewsCarousel {
  constructor() {
    this.news = [];
    this.currentIndex = 0;
    this.itemsPerView = 3;
    this.track = null;
    this.prevBtn = null;
    this.nextBtn = null;
    this.dotsContainer = null;
    
    this.init();
  }
  
  async init() {
    try {
      // Charger les news depuis le JSON
      const response = await fetch('/news.json');
      const data = await response.json();
      
      // Trier par date (plus récent en premier)
      this.news = data.news.sort((a, b) => new Date(b.date) - new Date(a.date));
      
      // Limiter aux 6 plus récentes pour le carrousel
      this.news = this.news.slice(0, 6);
      
      // Initialiser le carrousel
      this.setupCarousel();
      this.updateResponsive();
      window.addEventListener('resize', () => this.updateResponsive());
    } catch (error) {
      console.error('Erreur lors du chargement des news:', error);
    }
  }
  
  setupCarousel() {
    this.track = document.querySelector('.news-carousel__track');
    this.prevBtn = document.querySelector('.news-carousel__nav-btn--prev');
    this.nextBtn = document.querySelector('.news-carousel__nav-btn--next');
    this.dotsContainer = document.querySelector('.news-carousel__dots');
    
    if (!this.track) return;
    
    // Générer les items
    this.renderItems();
    
    // Setup navigation
    this.prevBtn?.addEventListener('click', () => this.prev());
    this.nextBtn?.addEventListener('click', () => this.next());
    
    // Setup dots
    this.renderDots();
    
    // Update initial state
    this.updateCarousel();
  }
  
  renderItems() {
    this.track.innerHTML = this.news.map(item => this.createNewsCard(item)).join('');
  }
  
  createNewsCard(item) {
    const date = this.formatDate(item.date);
    const typeLabel = this.getTypeLabel(item.type);
    
    let mediaContent = '';
    if (item.type === 'video' && item.youtubeId) {
      mediaContent = `
        <div class="news-carousel__item-video">
          <iframe 
            src="https://www.youtube.com/embed/${item.youtubeId}" 
            title="${item.title}"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
          </iframe>
        </div>
      `;
    }
    
    return `
      <a href="${item.link}" class="news-carousel__item">
        <div class="news-carousel__item-header">
          <div class="news-carousel__item-date">${date}</div>
          <span class="news-carousel__item-type news-carousel__item-type--${item.type}">${typeLabel}</span>
        </div>
        <h3 class="news-carousel__item-title">${item.title}</h3>
        <p class="news-carousel__item-excerpt">${item.excerpt}</p>
        ${mediaContent}
        <span class="news-carousel__item-link">
          ${item.type === 'video' ? 'Voir la vidéo' : 'Lire la suite'} →
        </span>
      </a>
    `;
  }
  
  renderDots() {
    if (!this.dotsContainer) return;
    
    const totalPages = Math.ceil(this.news.length / this.itemsPerView);
    this.dotsContainer.innerHTML = Array.from({ length: totalPages }, (_, i) => 
      `<button class="news-carousel__dot ${i === 0 ? 'active' : ''}" data-index="${i}"></button>`
    ).join('');
    
    // Add click handlers
    this.dotsContainer.querySelectorAll('.news-carousel__dot').forEach(dot => {
      dot.addEventListener('click', (e) => {
        const index = parseInt(e.target.dataset.index);
        this.goToPage(index);
      });
    });
  }
  
  updateCarousel() {
    if (!this.track) return;
    
    // Calculate offset
    const itemWidth = this.track.children[0]?.offsetWidth || 0;
    const gap = 24;
    const offset = -(this.currentIndex * (itemWidth + gap));
    
    this.track.style.transform = `translateX(${offset}px)`;
    
    // Update navigation buttons
    const maxIndex = Math.max(0, this.news.length - this.itemsPerView);
    if (this.prevBtn) this.prevBtn.disabled = this.currentIndex === 0;
    if (this.nextBtn) this.nextBtn.disabled = this.currentIndex >= maxIndex;
    
    // Update dots
    const currentPage = Math.floor(this.currentIndex / this.itemsPerView);
    this.dotsContainer?.querySelectorAll('.news-carousel__dot').forEach((dot, i) => {
      dot.classList.toggle('active', i === currentPage);
    });
  }
  
  prev() {
    if (this.currentIndex > 0) {
      this.currentIndex--;
      this.updateCarousel();
    }
  }
  
  next() {
    const maxIndex = Math.max(0, this.news.length - this.itemsPerView);
    if (this.currentIndex < maxIndex) {
      this.currentIndex++;
      this.updateCarousel();
    }
  }
  
  goToPage(pageIndex) {
    this.currentIndex = pageIndex * this.itemsPerView;
    this.updateCarousel();
  }
  
  updateResponsive() {
    const width = window.innerWidth;
    
    if (width <= 640) {
      this.itemsPerView = 1;
    } else if (width <= 1024) {
      this.itemsPerView = 2;
    } else {
      this.itemsPerView = 3;
    }
    
    this.currentIndex = 0;
    this.renderDots();
    this.updateCarousel();
  }
  
  formatDate(dateString) {
    const date = new Date(dateString);
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    return date.toLocaleDateString('fr-FR', options);
  }
  
  getTypeLabel(type) {
    const labels = {
      'video': 'Vidéo',
      'texte': 'Article',
      'actu': 'Synthèse'
    };
    return labels[type] || type;
  }
}

// Initialiser le carrousel au chargement de la page
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new NewsCarousel());
} else {
  new NewsCarousel();
}
