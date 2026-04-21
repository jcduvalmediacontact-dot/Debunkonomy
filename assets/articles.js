// Articles dynamic loading
// Charge et affiche automatiquement les articles depuis articles.json

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const response = await fetch('/articles.json');
    if (!response.ok) {
      console.error('Erreur de chargement du fichier articles.json');
      return;
    }
    
    const data = await response.json();
    
    // Générer les articles de l'auteur
    generateArticles(data.auteur, 'articles-auteur-grid', 'auteur');
    
    // Générer les articles invités
    generateArticles(data.invites, 'articles-invites-grid', 'invites');
    
    // Mettre à jour les compteurs
    updateCount('articles-auteur-count', data.auteur.length);
    updateCount('articles-invites-count', data.invites.length);
    
  } catch (error) {
    console.error('Erreur lors du chargement des articles:', error);
  }
});

function generateArticles(articles, containerId, type) {
  const container = document.getElementById(containerId);
  if (!container) return;
  
  // Trier par date (plus récent en premier)
  const sortedArticles = articles.sort((a, b) => new Date(b.date) - new Date(a.date));
  
  // Générer les cartes
  sortedArticles.forEach(article => {
    const card = createArticleCard(article, type);
    container.insertAdjacentHTML('beforeend', card);
  });
  
  // Ajouter la carte placeholder si nécessaire
  const placeholder = createPlaceholder(type);
  container.insertAdjacentHTML('beforeend', placeholder);
}

function createArticleCard(article, type) {
  const formattedDate = formatDate(article.date);
  const authorLine = article.author ? ` Par ${article.author}.` : '';
  
  return `
    <a href="${article.link}" class="card-entry">
      <div class="card-entry__date">${formattedDate}</div>
      <h3 class="card-entry__title">${article.title}</h3>
      <p class="card-entry__excerpt">${article.excerpt}${authorLine}</p>
      <div class="card-entry__meta">
        <span class="card-entry__tag">${article.category}</span>
        <span class="card-entry__read">~${article.readTime} de lecture</span>
      </div>
    </a>
  `;
}

function createPlaceholder(type) {
  const title = type === 'auteur' ? 'Analyses en préparation' : "D'autres contributions invitées";
  const excerpt = type === 'auteur' 
    ? 'NEMO IMS face à ses objections, lecture monétaire des limites planétaires, débats avec les écoles hétérodoxes contemporaines (MMT, post-keynésianisme, économie écologique)…'
    : "Cette section accueillera d'autres contributions de chercheurs, économistes et penseurs invités à dialoguer avec le programme Debunk'Onomy.";
  
  return `
    <div class="card-entry card-entry--placeholder">
      <div class="card-entry__date">À venir</div>
      <h3 class="card-entry__title">${title}</h3>
      <p class="card-entry__excerpt">${excerpt}</p>
      <div class="card-entry__meta">
        <span class="card-entry__tag">À paraître</span>
      </div>
    </div>
  `;
}

function formatDate(dateString) {
  const date = new Date(dateString);
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return date.toLocaleDateString('fr-FR', options);
}

function updateCount(elementId, count) {
  const element = document.getElementById(elementId);
  if (element) {
    element.textContent = count === 1 ? '1 article' : `${count} articles`;
  }
}
