# Correctif R2 — coins arrondis des fenêtres / cadres

Date : 2026-05-02

## Problème corrigé

Les cadres de certaines pages, notamment `/commencer-ici/`, avaient perdu leur arrondi visuel.
La cause était une règle d’arrondi globale fondée sur `:where(...)`, dont la spécificité CSS était trop faible face aux anciennes règles locales comme `.intro-panel { border-radius: 2px; }` ou `.cta-band { border-radius: 2px; }`.

## Correction appliquée

- Ajout d’un bloc CSS R2 dans `assets/theme.css` avec `:is(...)` et `!important` pour restaurer l’arrondi réel des cadres.
- Classes explicitement couvertes : `intro-panel`, `cta-band`, `newsletter-box`, `route-card`, `article-card`, `faq-item`, `glossary-term`, cartes médias, cartes contact, cartes livre, blocs NEMO, citations et callouts.
- Ajout d’un paramètre de version `?v=20260502-r2` aux appels de `theme.css` pour éviter les problèmes de cache navigateur après remise en ligne.
- Sur les quelques pages où `theme.css` n’était pas chargé en dernier, ajout d’un appel final à `theme.css` avant `</head>`.
