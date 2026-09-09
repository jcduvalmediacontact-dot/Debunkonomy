# `modeles/` — les pièces exécutables du corpus

Ce répertoire est **hors `corpus/`**, et c'est délibéré. Un script n'est pas un
chapitre : il ne doit ni compter dans le nombre de chapitres, ni passer sous le
contrôle de `corpus/convention.md`, ni recevoir un en-tête YAML. Ce qu'il produit
est lu par un chapitre, qui lui porte la convention.

Dépendance : aucune. Python 3, bibliothèque standard seule.

## Avertissement, et il est le plus important de ce fichier

**DEUX versions de cette matrice ont été écrites et réfutées le même jour, le
2026-09-09.** La première rendait un verdict unique par branche et **traitait une
insuffisance d'actifs comme une inexistence de passif** : c'est faux, une dette
reste une dette quand son débiteur ne peut pas l'honorer. La seconde écrivait
encore « reconnu comme passif » alors qu'elle vérifiait seulement que des
étiquettes étaient renseignées ; elle figeait un créancier unique pour un
instrument transférable ; et elle concluait que le collecteur d'un prélèvement
décidait de l'extinction. **Les tests passaient dans les deux cas — ils
établissaient que le programme appliquait ses règles, non que les règles étaient
fondées.**

**Un programme qui applique fidèlement une hypothèse fausse produit des résultats
faux avec une régularité parfaite.** C'est pourquoi la version courante sépare
ce qui relève des identités comptables, qui ne se discutent pas, de ce qui relève
d'une **lecture de la norme**, qui se discute et doit être soumise à un
contradicteur humain.

## `a35b_bilans.py` — matrice comptable de l'arbre A35b

Sept secteurs, quatorze branches, **cinq résultats séparés par branche, et ils
ne se commandent pas** :

| | |
|---|---|
| **R1a cohérence arithmétique** | équilibres, miroirs, somme des situations nettes, et l'identité *passif total = somme des avoirs de tous les détenteurs*, contrôlée **à chaque étape**. **Calculée.** |
| **R1b qualification comptable** | **PROPOSÉE, jamais établie.** Le programme n'écrit nulle part « reconnu comme passif » : il constate que des éléments sont renseignés, et suspend sa proposition quand l'un manque. |
| **R2 liquidité** | la demande maximale exigible à **chaque** étape. **Calculée, au pic** — et **par scénarios séparés** quand l'instrument est servi par d'autres participants. |
| **R3 solvabilité intertemporelle** | **non évaluable** : un cycle, sans intérêt ni horizon. |
| **R4 conformité juridique** | **non évaluée** : chaque branche déclare ce qu'elle exigerait. |

```bash
python modeles/a35b_bilans.py
```

**Une branche peut être comptablement cohérente et illiquide.** C'est le cas
normal d'un émetteur qui promet plus qu'il ne détient, et ce n'est pas une
anomalie d'écriture : c'est un risque, et le programme le nomme au lieu de
rejeter la branche.

Le programme imprime la **chronologie des bilans après chaque opération**. Ce
n'est pas un confort d'affichage : une obligation stipulée « à tout moment » ne
se contrôle pas sur le bilan final, et c'est exactement la faute que la version 1
commettait.

**Aucun comportement économique n'y est modélisé** — ni prix, ni salaire, ni
profit, ni élasticité, ni capacité productive, ni transfert international, ni
intérêt. En particulier, **la matrice n'établit aucune incidence économique** :
elle impose par paramètre qui est redevable, puis retrouve ce qu'elle a imposé.

`A36` est respecté : le **démurrage** (assiette : l'encaisse détenue) et le
**prélèvement transactionnel** (assiette : la transaction) sont deux mécanismes,
avec deux redevables et deux règlements. Et le **collecteur du prélèvement est un
paramètre**, parce que A36 n'a pas arrêté l'architecture juridique. Mais **le
collecteur ne décide que de la PREMIÈRE DESTINATION** des unités perçues : à
circuit ultérieur inchangé, son choix modifie l'encours immédiatement après
perception, et **l'encours final dépend ensuite de l'emploi des unités
collectées** — trois sous-branches l'établissent.

Le résultat est lu par **L19.C10**, et le raisonnement vit dans
`protocoles/passe-2.md`.

## `test_a35b.py` — vérification du programme, et de lui seul

```bash
python modeles/test_a35b.py
```

Cinq sections, et la troisième porte un avertissement en toutes lettres :

- **A. identités comptables** — sabotées une par une ; ce ne sont pas des
  hypothèses, ce sont des identités.
- **B. créancier dynamique** — vérifie que la qualité de créancier MIGRE avec
  l'instrument, et que le passif égale la somme des encours de tous les
  détenteurs.
- **C. qualification** — vérifie que le programme SUSPEND sa proposition quand un
  élément manque. **Il ne valide pas la lecture de la norme.**
- **D. liquidité** — vérifie que le pic est contrôlé, que le bilan final seul
  aurait conclu à tort à la couverture, et que les trois scénarios sont publiés
  séparément.
- **E. A36** — vérifie que les deux mécanismes restent distincts, et que
  l'EMPLOI des unités perçues, non le collecteur seul, décide de l'encours.

## Comment ajouter une branche

**Une branche qui n'est pas écrite n'est pas rejetée : elle est absente.** Le
résultat de L19.C10 est conditionnel à l'énumération, et un contradicteur qui
produirait une quinzième branche déplacerait ses conclusions.

**Le jalon suivant est humain** : `protocoles/revue-comptable-a35b.md` pose cinq
questions à un comptable national. **Aucun modèle macroéconomique avant cette
revue.**

Pour l'écrire : ajouter une `Branche(...)` à la liste `BRANCHES`, en renseignant
ses axes — `circulation`, `inscription`, `allocation`, `beneficiaire`, plus
`souscription`, `collecteur`, `emploi_collecte` et `contrib_detenteur` s'il y a
lieu — et sa fiche : l'obligation, le secteur chez qui le passif est inscrit, le
droit attaché, qui sert l'obligation, l'exigibilité, l'extinction, le porteur du
risque, et les exigences juridiques que la branche appellerait. **Le créancier
n'est pas un champ : il est DÉRIVÉ des écritures, et il migre avec
l'instrument.** Les écritures s'en déduisent.
