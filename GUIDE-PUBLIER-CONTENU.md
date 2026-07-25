# GUIDE — Publier un nouvel article sur debunkonomy.org

> Version 1.0 — Mai 2026  
> Ce guide couvre la publication complète d'un article (auteur ou invité) sur le site statique Debunk'Onomy, dans toutes les langues.

---

## Sommaire

1. [Vue d'ensemble de l'architecture](#1-vue-densemble)
2. [Checklist complète — article auteur](#2-checklist-article-auteur)
3. [Checklist complète — article invité](#3-checklist-article-invité)
4. [Détail de chaque fichier à modifier](#4-détail-fichier-par-fichier)
5. [Conventions de nommage des slugs](#5-conventions-de-nommage)
6. [Structure HTML d'un article](#6-structure-html-article)
7. [Traduction : niveaux d'effort par langue](#7-niveaux-de-traduction)
8. [Vérification avant déploiement](#8-vérification)

---

## 1. Vue d'ensemble

Le site est **100 % statique**. Il n'existe pas de CMS. Chaque publication implique :

- La création de pages HTML (une par langue)
- La mise à jour manuelle des **listings** (pages statiques hardcodées)
- La mise à jour de deux types de fichiers JSON

| Fichier | Rôle | Dynamique ? |
|---|---|---|
| `articles/index.html` + équivalents langues | Listing des articles (grille de cartes) | ❌ Hardcodé |
| `articles.json` | Source de données pour `articles.js` | ✅ Lu par JS |
| `news.json` × 7 langues | Carousel "Actualités" sur la homepage | ✅ Lu par JS |

**Langues du site :** FR (canonique) · EN · ES · PT · DE · IT · AR

---

## 2. Checklist article auteur

Pour chaque nouvel article de Jean-Christophe Duval, **22 fichiers** sont à créer ou modifier :

### Fichiers à CRÉER (7 pages HTML)

```
articles/auteur/{slug-fr}/index.html              ← version canonique FR
en/articles/{slug-en}/index.html
es/articles/{slug-es}/index.html
pt/articles/{slug-pt}/index.html
de/articles/{slug-de}/index.html
it/articles/{slug-it}/index.html
ar/articles/{slug-en}/index.html                  ← AR réutilise le slug EN
```

### Fichiers à MODIFIER (8 listings)

```
articles/index.html          ← insérer route-card EN TÊTE de .route-grid
en/articles/index.html
es/articles/index.html
pt/articles/index.html
de/articles/index.html
it/articles/index.html
ar/articles/index.html
```

### Fichiers JSON à MODIFIER (8 JSON)

```
articles.json                ← insérer en tête du tableau "auteur"
news.json                    ← insérer en tête du tableau "news"
en/news.json
es/news.json
pt/news.json
de/news.json
it/news.json
ar/news.json
```

**Total : 7 + 7 + 8 = 22 fichiers**

---

## 3. Checklist article invité

Différences par rapport à un article auteur :

| Élément | Article auteur | Article invité |
|---|---|---|
| Chemin FR | `articles/auteur/{slug}/` | `articles/invites/{slug}/` |
| Traductions | 6 langues complètes | Non traduit (FR + lien EN uniquement) |
| `articles.json` | Tableau `auteur` | Tableau `invites` |
| Champ author | Absent | `"author": "Prénom Nom"` |
| Carte listing | `data-article-id` optionnel | Sans `data-article-id` |

**Total article invité : 1 HTML + 1 listing FR + articles.json + news.json = 4 fichiers**  
(les pages listing des autres langues ne listent pas les articles invités)

---

## 4. Détail fichier par fichier

### 4.1 Page article HTML

Copier la structure d'un article existant récent et adapter :

**Dans le `<head>` :**
- `<title>` : Titre de l'article — Debunk'Onomy
- `<meta name="description">` : Extrait de 150-160 caractères
- `<link rel="canonical">` : URL complète de la version FR
- Bloc `hreflang` : 7 entrées (une par langue) + `x-default` → FR
- JSON-LD `Article` : headline, description, datePublished, url, inLanguage
- JSON-LD `BreadcrumbList` : 3 niveaux (accueil → articles → titre)

**Dans le `<nav>` :**
- `href` du logo → `/` (FR) ou `/{lang}/` (autres langues)
- `lang-switch` : 7 liens vers les versions équivalentes dans chaque langue

**Dans `<article>` :**
```html
<header class="article__header">
  <div class="article__meta">
    <span>{date formatée}</span>
    <div class="article__meta-sep"></div>
    <span>{Catégorie · Sous-catégorie}</span>
    <div class="article__meta-sep"></div>
    <span>{N} min</span>
  </div>
  <h1 class="article__title">{Titre}</h1>
  <p class="article__subtitle">{Sous-titre / accroche}</p>
  <!-- Carte auteur : photo N&B ronde + signature (OBLIGATOIRE) -->
  <div class="article__author">
    <img class="article__author-photo" src="/assets/authors/{slug-auteur}.jpg"
         alt="{Nom auteur}" width="76" height="76" loading="lazy"/>
    <p class="article__byline">{Nom auteur}</p>
  </div>
</header>
<div class="article__body">
  <!-- Corps : <p>, <h2>, <h3>, <ul>, <strong>, <em> -->
  <p class="article__signature">Jean-Christophe Duval</p>
</div>
```

**Registre des auteurs (photos d'entête) :** une vignette N&B carrée dans `assets/authors/`, servie ronde par le CSS (`.article__author-photo`). Le `{slug-auteur}` se déduit du byline :

| Byline | Fichier |
|---|---|
| Jean-Christophe Duval (ou variante `By` / `Par` / `بقلم` / arabe) | `assets/authors/jc-duval.jpg` |
| Jean Latreille | `assets/authors/jean-latreille.jpg` |
| Renaud Vignes | `assets/authors/renaud-vignes.jpg` |

Nouvel auteur → ajouter `assets/authors/{slug}.jpg` (240×240, niveaux de gris, recadrage carré centré) et compléter cette table. La carte auteur figure sur **toutes les langues**, à l'identique (le byline reste dans la langue de la page).

**Après `</article>` :**
1. `.related-articles` — 3 articles liés (cartes `.related-card`)
2. `.share-bar` — LinkedIn + X/Twitter + bouton copie
3. `<footer>` — footer localisé
4. `<script>` — scroll nav

**Attributs spéciaux pour l'arabe :**
```html
<html dir="rtl" lang="ar">
```

---

### 4.2 Listing `articles/index.html`

Localiser dans le fichier :
```html
<div class="route-grid">
```

Insérer **immédiatement après** cette balise :
```html
<a class="route-card" data-article-id="{slug-fr}" href="/articles/auteur/{slug-fr}/">
<div class="route-card__kicker">{date} · {Catégorie} · {Sous-catégorie}</div>
<h2 class="route-card__title">{Titre FR}</h2>
<p class="route-card__text">{Extrait 120-150 caractères}</p>
<div class="route-card__arrow">Lire · {N} min →</div>
</a>
```

**Attention :** Ne pas modifier les cartes existantes. Insérer uniquement en tête.

Pour les langues, adapter : `href`, texte du kicker, titre, extrait, et label du CTA (`Read`, `Leer`, `Ler`, `Lesen`, `Leggere`, `قراءة`).

---

### 4.3 `articles.json`

Structure à insérer en **première position** du tableau `auteur` :

```json
{
  "date": "YYYY-MM-DD",
  "title": "Titre FR",
  "excerpt": "Extrait de 100-150 caractères.",
  "link": "/articles/auteur/{slug-fr}/",
  "category": "Catégorie · Sous-catégorie",
  "readTime": "N min"
}
```

Pour un article invité, même structure dans le tableau `invites`, avec en plus :
```json
"author": "Prénom Nom"
```

---

### 4.4 `news.json` (et équivalents par langue)

Structure à insérer en **première position** du tableau `news` :

```json
{
  "type": "texte",
  "date": "YYYY-MM-DD",
  "title": "Titre dans la langue du fichier",
  "excerpt": "Extrait court (80-100 caractères).",
  "link": "/{lang}/articles/{slug-lang}/"
}
```

**Valeurs du champ `type` par langue :**

| Langue | Texte | Vidéo | Podcast |
|---|---|---|---|
| FR | `texte` | `video` | `podcast` |
| EN | `text` | `video` | `podcast` |
| ES | `texto` | `video` | `podcast` |
| PT | `texto` | `video` | `podcast` |
| DE | `text` | `video` | `podcast` |
| IT | `testo` | `video` | `podcast` |
| AR | `نص` | `فيديو` | `بودكاست` |

**Note FR :** Le `news.json` à la racine (`/news.json`) est le fichier FR.

---

## 5. Conventions de nommage

### Slugs URL

- Tout en **minuscules**
- Séparateurs : **tirets** `-` uniquement (pas de `_`, pas d'espaces)
- Pas d'accents, pas de caractères spéciaux
- L'arabe réutilise le **slug anglais**

**Exemple pour cet article :**

| Langue | Slug |
|---|---|
| FR | `pourquoi-ne-plus-craindre-la-decroissance` |
| EN | `why-fear-of-degrowth-is-unfounded` |
| ES | `por-que-no-temer-el-decrecimiento` |
| PT | `por-que-nao-temer-o-decrescimento` |
| DE | `warum-degrowth-nicht-fuerchten` |
| IT | `perche-non-temere-la-decrescita` |
| AR | `why-fear-of-degrowth-is-unfounded` ← même slug EN |

### Chemins complets

| Langue | Chemin |
|---|---|
| FR (canonique) | `/articles/auteur/{slug-fr}/` |
| EN | `/en/articles/{slug-en}/` |
| ES | `/es/articles/{slug-es}/` |
| PT | `/pt/articles/{slug-pt}/` |
| DE | `/de/articles/{slug-de}/` |
| IT | `/it/articles/{slug-it}/` |
| AR | `/ar/articles/{slug-en}/` |

---

## 6. Structure HTML article — récapitulatif

```
<!DOCTYPE html>
<html lang="{lang}" [dir="rtl" pour AR]>
<head>
  ├── charset / viewport
  ├── <title>
  ├── <meta description>
  ├── <link canonical>
  ├── 7 × <link hreflang> + x-default
  ├── Open Graph (type, title, desc, image, url, author, published_time)
  ├── favicon (ico, 32px, 180px)
  ├── theme-color #1C5A60
  ├── JSON-LD Article
  ├── JSON-LD BreadcrumbList
  ├── RSS alternate
  ├── Twitter Card
  └── Fonts (Fraunces + Instrument Sans/Serif) + debunkonomy.css
</head>
<body>
  ├── #read-progress
  ├── <nav.nav> (logo + liens + lang-switch)
  ├── <article.article>
  │    ├── <header.article__header> (meta + h1 + subtitle + carte auteur : photo N&B + byline)
  │    └── <div.article__body> (corps + .article__signature)
  ├── <div.related-articles> (3 × .related-card)
  ├── <div.share-bar> (LinkedIn + X + copy)
  ├── <footer.footer>
  └── <script> (scroll nav)
</body>
```

---

## 7. Niveaux de traduction par langue

| Langue | Niveau attendu | Notes |
|---|---|---|
| **FR** | Texte intégral | Version canonique, toujours complète |
| **EN** | Texte intégral | Traduction complète, haute priorité |
| **ES** | Texte intégral | Traduction complète |
| **PT** | Texte intégral | Traduction complète |
| **DE** | Texte intégral | Traduction complète |
| **IT** | Texte intégral | Traduction complète |
| **AR** | Introduction + résumé + lien EN | Version partielle acceptable + `dir="rtl"` |

> **Pratique actuelle :** ES, PT, DE, IT, AR en traduction complète. La mise à jour du texte complet peut intervenir en second temps sans modifier les JSON ni les listings.

---

## 8. Vérification avant déploiement

Avant de pousser les fichiers sur le repo, vérifier :

### HTML
- [ ] `<link canonical>` pointe vers la bonne URL (FR pour toutes les langues sauf si langue = FR)
- [ ] 7 balises `hreflang` présentes + `x-default`
- [ ] `lang-switch` contient les 7 liens corrects
- [ ] `href` du logo pointe vers `/{lang}/` (pas vers `/` pour les langues non-FR)
- [ ] `dir="rtl"` présent sur la version AR
- [ ] `article:published_time` = date au format `YYYY-MM-DD`
- [ ] 3 articles liés pertinents dans `.related-articles`
- [ ] `<p class="article__signature">` présent en fin de body

### Listings
- [ ] Nouvelle carte insérée en **tête** de `.route-grid` (avant la carte existante la plus récente)
- [ ] `href` de la carte pointe vers le bon chemin localisé
- [ ] `data-article-id` correspond au slug FR (pour les articles auteur)

### JSON
- [ ] `articles.json` : nouvel objet en **index 0** du tableau `auteur`
- [ ] 7 × `news.json` : nouvel objet en **index 0** du tableau `news`
- [ ] `"type"` correctement localisé dans chaque `news.json`
- [ ] JSON valide (pas de virgule manquante ni superflue)

### Validation rapide
```bash
# Vérifier la validité JSON
python3 -c "import json; json.load(open('articles.json'))" && echo "OK"
python3 -c "import json; json.load(open('news.json'))" && echo "OK"
```

---

## Annexe — Structure du repo (rappel)

```
Debunkonomy/
├── articles/
│   ├── index.html                        ← listing FR (hardcodé)
│   ├── auteur/{slug-fr}/index.html       ← pages articles auteur
│   └── invites/{slug}/index.html         ← pages articles invités
├── {en|es|pt|de|it|ar}/
│   ├── articles/
│   │   ├── index.html                    ← listing langue (hardcodé)
│   │   └── {slug-lang}/index.html        ← pages articles traduits
│   └── news.json                         ← carousel langue
├── articles.json                         ← données articles (auteur + invités)
├── news.json                             ← carousel FR
└── assets/
    ├── debunkonomy.css
    ├── articles.js                       ← chargement dynamique (articles.json)
    └── news-carousel.js                  ← carousel (news.json)
```

---

*Debunk'Onomy — Think & Move to Degrowth*  
*contact@debunkonomy.org · debunkonomy.org*
