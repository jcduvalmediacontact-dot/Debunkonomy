# `modeles/` — les pièces exécutables du corpus

Ce répertoire est **hors `corpus/`**, et c'est délibéré. Un script n'est pas un
chapitre : il ne doit ni compter dans le nombre de chapitres, ni passer sous le
contrôle de `corpus/convention.md`, ni recevoir un en-tête YAML. Ce qu'il produit
est lu par un chapitre, qui lui porte la convention.

Dépendance : aucune. Python 3, bibliothèque standard seule.

## Avertissement, et il est le plus important de ce fichier

**Une première version de cette matrice a été écrite et réfutée le même jour, le
2026-09-09.** Elle rendait un verdict unique par branche, et deux de ses règles
de rejet étaient fausses. La plus grave **traitait une insuffisance d'actifs
comme une inexistence de passif** : c'est faux, une dette reste une dette quand
son débiteur ne peut pas l'honorer. Ses tests passaient tous — **ils
établissaient que le programme appliquait ses règles, non que les règles étaient
fondées.**

**Un programme qui applique fidèlement une hypothèse fausse produit des résultats
faux avec une régularité parfaite.** C'est pourquoi la version courante sépare
ce qui relève des identités comptables, qui ne se discutent pas, de ce qui relève
d'une **lecture de la norme**, qui se discute et doit être soumise à un
contradicteur humain.

## `a35b_bilans.py` — matrice comptable de l'arbre A35b

Sept secteurs, onze branches, **quatre résultats séparés par branche, et ils ne
se commandent pas** :

| | |
|---|---|
| **R1 cohérence comptable** | identités de bilan, et reconnaissance au sens du § 4.101 du SNA 2025 — une obligation, un débiteur, un créancier, la créance correspondante inscrite chez ce créancier (§ 4.103). **Calculé.** |
| **R2 liquidité immédiate** | la demande maximale exigible à **chaque** étape, contre ce que l'obligé peut mobiliser à cette date. **Calculé, au pic.** |
| **R3 solvabilité intertemporelle** | **non évaluable** : la matrice ne porte qu'un cycle, sans intérêt ni horizon. |
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
paramètre**, parce que A36 n'a pas arrêté l'architecture juridique : selon que
l'émetteur ou l'État perçoit, **le reflux n'éteint pas la même chose**.

Le résultat est lu par **L19.C10**, et le raisonnement vit dans
`protocoles/passe-2.md`.

## `test_a35b.py` — vérification du programme, et de lui seul

```bash
python modeles/test_a35b.py
```

Quatre sections, et la deuxième porte un avertissement en toutes lettres :

- **A. identités comptables** — sabotées une par une ; ce ne sont pas des
  hypothèses, ce sont des identités.
- **B. reconnaissance** — les tests vérifient que le programme met en œuvre la
  lecture retenue. **Ils ne la valident pas.**
- **C. liquidité** — vérifie que le pic est bien contrôlé, et que le bilan final
  seul aurait conclu à tort à la couverture.
- **D. A36** — vérifie que les deux mécanismes restent distincts, et que le choix
  du collecteur change l'encours.

## Comment ajouter une branche

**Une branche qui n'est pas écrite n'est pas rejetée : elle est absente.** Le
résultat de L19.C10 est conditionnel à l'énumération, et un contradicteur qui
produirait une douzième branche déplacerait ses conclusions.

Pour l'écrire : ajouter une `Branche(...)` à la liste `BRANCHES`, en renseignant
ses axes — `circulation`, `inscription`, `allocation`, `beneficiaire`, plus
`souscription` et `collecteur` s'il y a lieu — et sa fiche : l'obligation, le
débiteur, le créancier, la créance inscrite, l'exigibilité, qui sert
l'obligation, le droit, l'extinction, le porteur du risque, et les exigences
juridiques que la branche appellerait. Les écritures s'en déduisent.
