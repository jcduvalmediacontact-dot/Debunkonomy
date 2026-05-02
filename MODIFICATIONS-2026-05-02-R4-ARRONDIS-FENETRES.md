# Modifications R4 — arrondis ciblés des fenêtres éditoriales

Date : 2026-05-02

## Correction

Cette version corrige la R3 qui appliquait des sélecteurs trop larges (`[class*="-card"]`, `[class*="-box"]`, etc.) et un `overflow: hidden` global aux cartes/vignettes.

## Changements effectués

- Suppression du bloc CSS R3 trop générique.
- Suppression du forçage global d’`overflow: hidden` sur les vignettes/cartes.
- Ajout d’un arrondi ciblé sur la grande fenêtre de citation de la page d’accueil (`.gaia-quote`).
- Conservation des arrondis des vrais encadrés éditoriaux : newsletter, panneaux, citations, notes, callouts.
- Respect du design propre des vignettes d’articles, cartes d’actualités et cartes de navigation.
- Cache-busting CSS mis à jour en `?v=20260502-r5`.

## Objectif

Arrondir les grandes fenêtres éditoriales comme celle contenant la citation :

> « Et Gaïa dit aux hommes : Il est vain de me soigner avec une monnaie que vous puisez au plus profond de mes blessures ! »

sans tronquer les textes ou les angles internes des vignettes.
