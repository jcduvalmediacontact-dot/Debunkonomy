// Video Modal - Lecteur YouTube intégré
(function() {
  'use strict';

  let modal = null;
  let playerFrame = null;

  // Créer la structure HTML de la modal
  function createModal() {
    modal = document.createElement('div');
    modal.className = 'video-modal';
    modal.innerHTML = `
      <div class="video-modal__content">
        <button class="video-modal__close" aria-label="Fermer">×</button>
        <div class="video-modal__player">
          <iframe 
            id="youtube-player" 
            src="" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
          </iframe>
        </div>
        <div class="video-modal__info">
          <h3 class="video-modal__title"></h3>
          <div class="video-modal__date"></div>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    playerFrame = document.getElementById('youtube-player');

    // Event listeners
    const closeBtn = modal.querySelector('.video-modal__close');
    closeBtn.addEventListener('click', closeModal);

    // Fermer en cliquant sur le fond
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal();
      }
    });

    // Fermer avec Échap
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // Ouvrir la modal avec une vidéo
  function openModal(youtubeId, title, date) {
    if (!modal) createModal();

    // Construire l'URL du player YouTube avec autoplay
    const embedUrl = `https://www.youtube.com/embed/${youtubeId}?autoplay=1&rel=0&modestbranding=1`;
    
    playerFrame.src = embedUrl;
    modal.querySelector('.video-modal__title').textContent = title;
    modal.querySelector('.video-modal__date').textContent = date;

    document.body.classList.add('modal-open');
    modal.classList.add('active');
  }

  // Fermer la modal
  function closeModal() {
    if (!modal) return;

    modal.classList.remove('active');
    document.body.classList.remove('modal-open');

    // Arrêter la vidéo en vidant l'iframe
    setTimeout(() => {
      if (playerFrame) playerFrame.src = '';
    }, 300);
  }

  // Intercepter les clics sur les cartes vidéo
  function attachVideoCardListeners() {
    document.addEventListener('click', (e) => {
      // Chercher si on a cliqué sur une carte vidéo ou un de ses enfants
      const videoCard = e.target.closest('.news-card--video');
      
      if (videoCard) {
        e.preventDefault();
        
        // Extraire les infos de la carte
        const title = videoCard.querySelector('.news-card__title')?.textContent || '';
        const date = videoCard.querySelector('.news-card__date')?.textContent || '';
        
        // Extraire le youtubeId du lien
        const link = videoCard.getAttribute('href');
        const youtubeIdMatch = link.match(/[?&]v=([^&]+)/);
        
        if (youtubeIdMatch && youtubeIdMatch[1]) {
          openModal(youtubeIdMatch[1], title, date);
        }
      }
    });
  }

  // Initialisation
  function init() {
    attachVideoCardListeners();
  }

  // Démarrer quand le DOM est prêt
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
