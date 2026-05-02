# 📚 GUIDE COMPLET - UNIFORMISATION DES ARTICLES

## 🎯 Objectif

Uniformiser tous les articles du site Debunk’Onomy avec :
- ✅ **Design cohérent** (inspiré de Solow)
- ✅ **Navigation complète** (menu complet du site)
- ✅ **CSS externe** (fini le CSS inline)
- ✅ **Liens corrects** dans les JSON

---

## 📦 FICHIERS CRÉÉS

### 1. **`article.css`**
CSS unifié pour tous les articles - **DÉJÀ CRÉÉ** dans `/assets/`

### 2. **`articles.json`**
Liste de tous les articles pour la page /articles/ - **DÉJÀ CRÉÉ** à la racine

### 3. **`news.json`**
Liste pour le carrousel homepage - **DÉJÀ CRÉÉ** à la racine

### 4. **`TEMPLATE-ARTICLE.html`**
Template universel pour tous les articles - **DÉJÀ CRÉÉ** à la racine

---

## 🚀 PLAN D'ACTION

### ✅ Étape 1 : Les CSS et JSON sont prêts !

**Rien à faire, déjà fait !**

---

### 📝 Étape 2 : Mettre à jour les 6 articles HTML

**Tu as 6 articles à mettre à jour :**

#### Articles auteur :
1. `/articles/auteur/cop-lobbycratie/index.html`
2. `/articles/auteur/ivan-illich-portrait/index.html`
3. `/articles/auteur/creation-monetaire-dette/index.html`
4. `/articles/auteur/limites-pib/index.html`
5. `/articles/auteur/septieme-limite-planetaire/index.html`

#### Article invité :
6. `/articles/invites/solow/index.html`

---

## 📋 PROCÉDURE POUR CHAQUE ARTICLE

### **Méthode simple : Copier-coller le contenu**

Pour chaque article :

#### 1. **Ouvre le template**
`TEMPLATE-ARTICLE.html`

#### 2. **Remplis le header**
```html
<title>TITRE — Debunk’Onomy</title>
<meta name="description" content="DESCRIPTION">

<!-- Dans l'article -->
<div class="article__meta">
  <span>Avril 2026</span>
  <div class="article__meta-sep"></div>
  <span>Catégorie</span>
</div>
<h1 class="article__title">Titre principal</h1>
<p class="article__subtitle">Sous-titre</p>
```

#### 3. **Copie le contenu du body**
- Ouvre l'ancien article
- Copie tout le contenu entre `<section class="article-content">` et `</section>`
- Colle-le dans le template à la place de `<div class="article__body">`
- Nettoie les `<div class="article-content__body">` si nécessaire

#### 4. **Remplace les classes si besoin**
```
AVANT :                        APRÈS :
.highlight-box (rouge)    →    .alert-box
.highlight-box (teal)     →    .highlight-box
```

#### 5. **Sauvegarde**
Sauvegarde le nouveau fichier dans le bon dossier avec le nom `index.html`

---

## 🎨 COMPOSANTS DISPONIBLES

### Drop cap (automatique)
Le premier paragraphe a automatiquement une grande première lettre

### Titres
```html
<h2>Titre de section</h2>
<h3>Sous-titre</h3>
```

### Citations
```html
<blockquote>Citation</blockquote>
```

### Pullquote (citation mise en avant)
```html
<div class="pullquote">
  <p class="pullquote__text">Citation importante</p>
  <p class="pullquote__attribution">Source</p>
</div>
```

### Highlight box (teal - points importants)
```html
<div class="highlight-box">
  <p>Point à retenir</p>
</div>
```

### Alert box (rouge - warnings)
```html
<div class="alert-box">
  <p>Information importante</p>
</div>
```

### Stat box (chiffres clés)
```html
<div class="stat-box">
  <div class="stat-box__number">2456</div>
  <div class="stat-box__label">Description</div>
</div>
```

### Notes de bas de page
```html
<!-- Dans le texte -->
<p>Texte<a href="#fn1" class="footnote">1</a>.</p>

<!-- En fin de body -->
<div class="footnotes">
  <h4 class="footnotes__title">Notes</h4>
  <p id="fn1" class="footnotes__item">1. Texte de la note.</p>
</div>
```

---

## ⚙️ CORRECTIONS SPÉCIFIQUES PAR ARTICLE

### 📄 **COP (cop-lobbycratie)**
- ✅ Déjà presque bon
- ✅ Change `.nav` → `.inav`
- ✅ Change les chemins `../assets/` → `/assets/`
- ✅ Remplace tout le CSS inline par le lien vers `article.css`

### 📄 **Solow**
- ✅ Change `.anav` → `.inav`
- ✅ Ajoute tous les liens du menu (pas juste "Retour")
- ✅ Chemins : `../../../assets/` → `/assets/`
- ✅ Remplace le CSS inline par le lien vers `article.css`

### 📄 **Autres articles** (Illich, Dette, PIB, Limites)
Même procédure que COP :
- ✅ Navigation → `.inav` complète
- ✅ Chemins → `/assets/`
- ✅ CSS externe → `article.css`

---

## 🔍 CHECKLIST PAR ARTICLE

Pour chaque article, vérifie :

☐ **`<head>`**
  - ☐ Titre et meta description corrects
  - ☐ Liens vers `/assets/favicon.ico` (pas `../assets/`)
  - ☐ `<link rel="stylesheet" href="/assets/site.css">`
  - ☐ `<link rel="stylesheet" href="/assets/article.css">`
  - ☐ PAS de CSS inline

☐ **Navigation**
  - ☐ Utilise `<nav class="inav">`
  - ☐ Logo pointe vers `/assets/logo-tree.png`
  - ☐ Tous les liens du menu présents

☐ **Article structure**
  - ☐ `<article class="article">`
  - ☐ `<header class="article__header">` avec meta, title, subtitle
  - ☐ `<div class="article__body">` avec tout le contenu
  - ☐ Byline uniquement pour articles invités

☐ **Composants**
  - ☐ `.alert-box` pour warnings (rouge)
  - ☐ `.highlight-box` pour points importants (teal)
  - ☐ `.stat-box` pour chiffres
  - ☐ `.pullquote` pour citations mises en avant

☐ **Footer**
  - ☐ `<section class="article-footer">` avant le footer global
  - ☐ `<footer class="footer">` avec tous les liens

---

## 🎯 RÉSULTAT FINAL

**Après mise à jour, tous les articles auront :**
- ✅ Design unifié et élégant
- ✅ Navigation complète
- ✅ CSS externe (facile à maintenir)
- ✅ Drop cap automatique
- ✅ Composants riches (pullquotes, stat boxes, etc.)
- ✅ Responsive mobile
- ✅ Liens corrects dans les JSON

---

## 💡 ASTUCE RAPIDE

**Pour aller vite :**

1. Ouvre le template dans un éditeur
2. Fais "Enregistrer sous" → nomme-le `index.html`
3. Copie le contenu de l'ancien article
4. Colle-le dans le nouveau
5. Ajuste titre, meta, dates
6. Sauvegarde dans le bon dossier

**Répète 6 fois = Terminé !**

---

## 📊 RÉCAPITULATIF

| Fichier | Statut | Action |
|---------|--------|--------|
| `assets/article.css` | ✅ Créé | Aucune |
| `articles.json` | ✅ Créé | Aucune |
| `news.json` | ✅ Créé | Aucune |
| `TEMPLATE-ARTICLE.html` | ✅ Créé | Utiliser pour mise à jour |
| 6 articles HTML | ⏳ À mettre à jour | Suivre le guide |

---

**Une fois les 6 articles mis à jour :**
1. Push sur GitHub
2. Attends 2-3 minutes
3. Hard refresh (Ctrl+Shift+R)
4. **Tout fonctionne ! 🎉**
