# 📰 Système de News — Guide d'utilisation

## 🎯 Vue d'ensemble

Le système de news permet d'afficher dynamiquement les dernières publications sur la page d'accueil (carrousel) et dans les pages d'archives dédiées (vidéos, textes, synthèses).

## 📂 Structure des fichiers

```
debunkonomy.org/
├── index.html                    # Page d'accueil (avec carrousel)
├── news.json                     # Base de données des news
├── videos.html                   # Archive de toutes les vidéos
├── textes.html                   # Archive de tous les textes
├── actus.html                    # Archive de toutes les synthèses
└── assets/
    ├── news-carousel.css         # Styles du carrousel
    └── news-carousel.js          # Script du carrousel
```

## ✏️ Comment ajouter une nouvelle news

### 1. Ouvrir le fichier `news.json`

### 2. Ajouter votre nouvelle news **en haut** de la liste

```json
{
  "news": [
    {
      "id": "news-004",                    // ID unique (incrémenter)
      "date": "2026-04-20",                // Date au format YYYY-MM-DD
      "type": "video",                     // Type: "video", "texte" ou "actu"
      "title": "Titre de ma nouvelle news",
      "excerpt": "Court résumé de 2-3 lignes...",
      "youtubeId": "dQw4w9WgXcQ",         // Pour les vidéos uniquement
      "link": "/articles/mon-article/"     // Lien vers l'article complet
    },
    // Les autres news existantes restent en dessous
  ]
}
```

### 3. Paramètres selon le type

#### 📹 **Pour une VIDÉO** :
```json
{
  "id": "news-005",
  "date": "2026-04-20",
  "type": "video",
  "title": "Ma présentation NEMO IMS",
  "excerpt": "Explication du système monétaire néguentropique...",
  "youtubeId": "ABC123XYZ",              // ID YouTube (après watch?v=)
  "link": "/videos/#news-005"
}
```

#### 📝 **Pour un TEXTE** :
```json
{
  "id": "news-006",
  "date": "2026-04-20",
  "type": "texte",
  "title": "Critique de la croissance verte",
  "excerpt": "Analyse des contradictions du capitalisme vert...",
  "link": "/articles/croissance-verte/"
}
```

#### 📊 **Pour une SYNTHÈSE** :
```json
{
  "id": "news-007",
  "date": "2026-04-20",
  "type": "actu",
  "title": "Synthèse : Rapport du GIEC 2026",
  "excerpt": "Décryptage des derniers scénarios climatiques...",
  "link": "/actus/giec-2026/"
}
```

## 🔄 Workflow quotidien

1. **Éditer** `news.json` (ajouter la nouvelle news en haut)
2. **Télécharger** le ZIP complet depuis Claude
3. **Extraire** dans votre dossier local du repo
4. **GitHub Desktop** : 
   - Voir les modifications
   - Faire un commit ("Ajout news du 20/04/2026")
   - Push vers GitHub
5. **Le site se met à jour automatiquement** 🎉

## 📌 Points importants

### ✅ À FAIRE
- Toujours ajouter les nouvelles news **en haut** de la liste
- Utiliser des IDs uniques (news-001, news-002, etc.)
- Format de date strict : `YYYY-MM-DD` (ex: 2026-04-20)
- Vérifier que les liens (`link`) sont corrects
- Pour les vidéos YouTube : copier uniquement l'ID (après `watch?v=`)

### ❌ À ÉVITER
- Ne pas modifier les anciennes news (sauf correction)
- Ne pas oublier la virgule `,` entre les news
- Ne pas supprimer les accolades `{ }` ou crochets `[ ]`
- Ne pas utiliser de guillemets simples `'` (toujours doubles `"`)

## 🎨 Apparence sur le site

### Page d'accueil
- Carrousel affichant les **5-6 dernières news** (toutes catégories)
- Navigation avec flèches ← →
- Points de pagination en bas
- Tri automatique par date (plus récent en premier)

### Pages d'archives
- **videos.html** : toutes les news de type "video"
- **textes.html** : toutes les news de type "texte"
- **actus.html** : toutes les news de type "actu"
- Tri par date décroissante

## 🐛 Dépannage

### La news n'apparaît pas
- ✅ Vérifier le format JSON (virgules, guillemets)
- ✅ Vérifier que le fichier est bien à la racine du site
- ✅ Vider le cache du navigateur (Ctrl+F5)

### Erreur de syntaxe JSON
- Utiliser un validateur JSON : https://jsonlint.com/
- Vérifier les virgules entre les éléments
- Vérifier que tous les guillemets sont doubles `"`

### La vidéo ne s'affiche pas
- Vérifier que `youtubeId` contient uniquement l'ID (pas l'URL complète)
- Exemple : ✅ `"dQw4w9WgXcQ"` ❌ `"https://www.youtube.com/watch?v=dQw4w9WgXcQ"`

## 📧 Contact

Pour toute question technique : contact@debunkonomy.org

---

**Dernière mise à jour** : 19 avril 2026
