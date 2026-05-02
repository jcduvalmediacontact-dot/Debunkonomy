# Uniformisation des pages Articles — 2026-05-02

Pages corrigées :

- `/articles/` : conversion de l’ancien rendu `card-entry` vers le modèle anglais `route-grid` / `route-card`.
- `/es/articles/` : conversion de l’ancien rendu `article-card` vers le modèle anglais `route-grid` / `route-card`.
- `/articles/` : suppression de l’appel à `/assets/articles.js` sur cette page, car le script réinjectait l’ancien visuel `card-entry` après chargement.
- `/es/articles/` : ajout de la vignette/lien vers l’article espagnol “La arquitectura de la entropía”.

Les autres pages multilingues utilisaient déjà le modèle `route-card`.
