# `modeles/` — les pièces exécutables du corpus

Ce répertoire est **hors `corpus/`**, et c'est délibéré. Un script n'est pas un
chapitre : il ne doit ni compter dans le nombre de chapitres, ni passer sous le
contrôle de `corpus/convention.md`, ni recevoir un en-tête YAML. Ce qu'il produit
est lu par un chapitre, qui lui porte la convention.

Dépendance : aucune. Python 3, bibliothèque standard seule.

## `a35b_bilans.py` — matrice comptable statique de NEMO IMS

Éprouve les branches de l'arbitrage **A35b** — nature de l'obligation, droits du
détenteur, contrepartie à l'actif, reflux, extinction, traitement des pertes. Six
secteurs, neuf branches, sept contrôles dont chacun peut en rejeter une à lui
seul.

```bash
python modeles/a35b_bilans.py
```

Le code de sortie vaut `0` si au moins une branche se ferme, `1` sinon.

**Aucun comportement économique n'y est modélisé** : ni prix, ni élasticité, ni
capacité productive, ni délai, ni importation, ni intérêt. C'est l'arbitrage de
l'auteur du 2026-09-09 — valider les écritures avant d'étudier les effets.

Le résultat est lu par **L19.C10**, et le raisonnement vit dans
`protocoles/passe-2.md`.

## `test_a35b.py` — sabotage des contrôles

Un contrôle qui n'a jamais rien rejeté peut être mort sans que personne le sache.
Ce fichier casse délibérément chaque règle — supprime une contrepartie, retire un
motif, fait s'enrichir un secteur sans en appauvrir aucun autre, inscrit un
encours sans miroir, présente un passif sans obligation — et **exige que le
contrôle correspondant le voie**. Il vérifie aussi les invariants des branches
qui se ferment, et mesure le seuil au-delà duquel une promesse de conversion
cesse d'être servable.

```bash
python modeles/test_a35b.py
```

Le code de sortie vaut `0` si tout sabotage est détecté, `1` sinon. **Un sabotage
non détecté déclare la matrice sans valeur sur ce point**, et le dit en toutes
lettres.

## Comment ajouter une branche

Une branche qui n'est pas écrite n'est pas rejetée : elle est absente. Le
résultat de L19.C10 est donc conditionnel à l'énumération, et un contradicteur
qui produirait une dixième branche fermant sans payer l'un des deux prix
identifiés renverserait sa conclusion.

Pour l'écrire : ajouter une `Branche(...)` à la liste `BRANCHES`, en renseignant
ses quatre axes de conception — `circulation`, `inscription`, `allocation`,
`beneficiaire`, plus `souscription` s'il y a lieu — et sa fiche : l'obligation
présente, le secteur envers qui elle court, son type, le droit du détenteur,
l'extinction, le porteur des pertes. Les écritures s'en déduisent.
