# Modifications R5 — Arrondis précis des encarts de citation

Date : 2026-05-02

## Correction principale

La R4 avait arrondi la grande section verte de la page d’accueil (`.gaia-quote`), alors que la demande portait sur la fenêtre blanche contenant la citation de Gaïa (`.gaia-quote__text`).

## Changements réalisés

- Suppression de l’arrondi appliqué à la grande section verte `.gaia-quote`.
- Ajout d’un arrondi ciblé sur la fenêtre blanche de citation `.gaia-quote__text`.
- Ajout d’un arrondi global aux encarts éditoriaux de type `blockquote`, `pullquote`, `callout`, citations NEMO, citations manifeste, notes et blocs newsletter.
- Aucun `overflow:hidden` global n’est appliqué aux vignettes ou cartes d’articles.
- Aucun sélecteur générique de type `[class*="card"]` n’est utilisé.
- Cache CSS mis à jour en `?v=20260502-r5`.

## Objectif

Arrondir les coins des fenêtres blanches de citation / encarts éditoriaux, sans tronquer les contenus des vignettes ni modifier brutalement les cartes d’articles.
