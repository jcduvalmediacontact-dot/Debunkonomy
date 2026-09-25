# Relevé — le `resume` contre le corps, Livre 1

**Rien n'est corrigé.** L'ordre 6 s'arrête au relevé.

`python outils_claude/controle_resume.py --livre 1 --tout` — code de sortie 0.

---

## Ce relevé rend zéro, et c'est ce qu'il y a de plus difficile à rendre honnête

Un outil en panne rendrait exactement le même résultat. Trois choses le
distinguent d'une panne.

**Un : la matière est comptée.** Les 31 résumés du Livre 1 portent
**3 nombres** en tout, **305 énoncés** et **2675 mots
discriminants**. Le test des nombres n'avait donc presque rien à mordre — trois
nombres, tous retrouvés au corps. **C'est un résultat faible, pas un quitus.**

**Deux : les sabotages prouvent qu'il voit.** `test_controles_7a.py` — **37
contrôles, 0 échec.** Six portent sur cet outil : deux détections (un nombre du
résumé absent du corps ; un énoncé dont aucun mot n'est au corps) et **quatre
contrôles négatifs** qui doivent rester muets — singulier contre pluriel,
granularité décimale, millésime, et le cas conforme.

**Trois : la première écriture rendait deux faux positifs, et ils m'ont servi.**
Elle signalait deux énoncés de L1.C10 comme sans appui. L'un d'eux nommait
« catégories » quand le corps disait « catégorie » : ma troncature retirait UNE
finale parmi `s`, `e`, `x`, de sorte que le pluriel donnait `catégorie` et le
singulier `catégori` — **deux radicaux différents pour le même mot**. Un contrôle
qui déclare absent ce qui est présent est pire qu'absent. Corrigé : la marque du
pluriel d'abord, le `e` muet ensuite.

---

## Ce que ce relevé n'établit pas

- **Qu'un énoncé retrouvé au corps y soit encore vrai.** C'est la limite qui
  compte, et elle est grande. Le résumé de L1.C10 a employé pendant quatre jours
  les mots mêmes de son corps tout en lui faisant dire l'inverse — Wörgl
  « interdit au nom du monopole » quand le corps venait de retirer ce motif. Ce
  contrôle-là aurait été muet. **Seule une lecture le voit.**
- **Que 305 énoncés sur 305 soient soutenus.** Un résumé reformule avec les mots
  du chapitre : partager un mot de cinq lettres est un seuil bas, et le passer
  ne prouve rien.

Ce que le relevé établit, en revanche : **aucun résumé du Livre 1 ne porte un
nombre que son corps ne porte pas.** C'est peu, et c'est mécanique.

---

## Sortie brute

```
31 chapitre(s) à résumé, 305 énoncé(s) relevé(s)

CHIFFRES DU RÉSUMÉ ABSENTS DU CORPS  [0]
    aucun

ÉNONCÉS DU RÉSUMÉ SANS AUCUN MOT AU CORPS  [0]
    aucun

Avertissements seulement. `corpus/controle.py` reste l'autorité.
```

---

## Une règle réutilisée plutôt que réécrite

`controle_resume.py` importe `HORS_CHAMP`, `chiffres_de`, `lire` et `tetes` de
`controle_appels.py` au lieu de les redéfinir. Motif : le 2026-09-25,
`test_generer.py` a bloqué une publication parce qu'il portait sa propre copie
d'une règle de la convention et n'avait pas suivi la révision 15. Deux écritures
de la même règle divergent ; la question est seulement quand.
