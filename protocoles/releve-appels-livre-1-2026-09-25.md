# Relevé — l'appel `[Sn]` contre ce que son entrée déclare, Livre 1

**Rien n'est corrigé.** L'ordre 5 s'arrête au relevé : il se lit d'abord. Aucun
chapitre n'a été modifié, aucun statut touché.

`python outils_claude/controle_appels.py --livre 1` — code de sortie 1.
Les 143 entrées de la troisième classe s'obtiennent avec `--tout`.

---

## Ce que l'outil a coûté avant de rendre quelque chose de lisible

**Quatre écritures, et chacune a été démentie par un échantillon de cinq cas
tirés au sort.** C'est la seule partie de ce relevé qui vaut d'être lue deux
fois, parce qu'elle dit ce que valent les trois autres contrôles de la file 7a.

| écriture | ce qu'elle rendait | ce que l'échantillon a montré |
|---|---|---|
| 1. mots communs entre la phrase et les passages | 86 | `l'acidification` capturé comme UN jeton : l'élision française colle au mot |
| 2. idem, élision corrigée | 85 | **cinq faux positifs sur cinq** — `productivité`/`productivity`, `atmosphère`/`Atmospheric`, `idéaux-types`/`idéaltype`, un passage en allemand, et un `six` que mon filtre de longueur jetait |
| 3. chiffres, mots de nombre compris | 106 | trois sur cinq dus aux seuls mots : « une planète » rendait 1, « deux opérations différentes » rendait 2 — en français l'article indéfini est un nombre écrit en mots |
| 4. chiffres seuls, hors-champ et granularité | 19 | lisible |

**Le test de mots communs a été abandonné, non réglé.** Les pièces sont en
anglais et en allemand, le corps en français : ce qui se partage n'est pas le
vocabulaire. Ce qui reste est le test que la règle du projet demandait déjà —
« un chiffre n'entre au corps qu'avec un appel vers une pièce lue **qui le
porte** ».

**Quatre artefacts d'extraction trouvés en chemin**, tous dans mon code et
aucun dans le corpus : l'élision, `CO2` qui rendait 2, les dates ISO
`2026-09-23` qui rendaient 9 et 23, et une classe de séparateurs qui avalait
« 2015, 53,2 » d'un trait et rendait `2015532` — un nombre inexistant, donc
absent de toute pièce, donc signalé à coup sûr.

---

## Ce que le relevé ne dit pas

- **Qu'un passage déclaré porte l'énoncé.** Un passage cité qui parle d'autre
  chose passe le contrôle. Seule une lecture le verrait.
- **Qu'une entrée sans citation est en faute.** Une série statistique n'a pas de
  phrase à citer : c'est le cas de plusieurs des 33.
- **Que les 19 chiffres sont des défauts.** Bruit résiduel connu et nommé :
  `UE-28` rend 28 ; `L1.C18 S2` affiche « 20(1)) », un fragment que le
  découpage de phrase a mal borné ; et trois paires — C09 S3/S4, C10 S23/S24,
  C23 S17/S20 — sont une même phrase portant deux appels, dont chacun ne couvre
  qu'une partie des chiffres. **Cette dernière classe n'est pas du bruit** :
  « une phrase qui attribue à plusieurs sources se scinde ».

---

## Sortie brute

```
31 chapitre(s), 326 entrée(s) de source, 664 appel(s) [Sn]

APPELS ORPHELINS — aucune entrée de ce nom  [0]
    aucun

ENTRÉES SANS AUCUNE CITATION  [33]
    L1.C02    S8
    L1.C06    S8
    L1.C08    S4
    L1.C11    S2
    L1.C11    S3
    L1.C12    S1
    L1.C12    S3
    L1.C12    S10
    L1.C13    S3
    L1.C15    S2
    L1.C15    S4
    L1.C15    S10
    L1.C16    S4
    L1.C16    S5
    L1.C16    S10
    L1.C16    S11
    L1.C17    S5
    L1.C17    S6
    L1.C17    S8
    L1.C17    S9
    L1.C17    S12
    L1.C18    S12
    L1.C18    S20
    L1.C18    S22
    L1.C20    S8
    L1.C21    S9
    L1.C22    S4
    L1.C22    S12
    L1.C24    S12
    L1.C25    S11
    L1.C27    S7
    L1.C31    S3
    L1.C31    S4

ENTRÉES DONT LA CITATION PEUT N'ÊTRE QU'UN TITRE  [143]
    (--tout pour les voir)

APPELS DONT LA PHRASE PORTE UN CHIFFRE QU'AUCUN PASSAGE NE PORTE  [19]
    L1.C02    S4   15 | [S4] Une trajectoire compatible avec un réchauffement limité à 1,5 °C supposerait qu'ell
    L1.C02    S9   35500 | L'expansion des terres agricoles a été le moteur de près de 90 % de la déforestation mon
    L1.C03    S7   835 | ::etat:: **Ce qui est établi par une source ouverte.** L'absence de découplage absolu à 
    L1.C04    S6   260,278 | Pendant l'Holocène — environ onze mille sept cents ans —, elle est demeurée comprise ent
    L1.C04    S7   20,21 | Elle en a publié la première formulation le 13 février 2012, dans un document de travail
    L1.C06    S9   485,532,98 | Le total tous gaz suit la même pente : 48,5 gigatonnes d'équivalent CO2 en 2015, 53,2 en
    L1.C09    S3   15,2,55 | Nordhaus, dans sa recension de la revue Stern , adopte dans son modèle de référence un t
    L1.C09    S4   14 | Nordhaus, dans sa recension de la revue Stern [S3], adopte dans son modèle de référence 
    L1.C10    S23  21 | **L'une d'elles a fait coûter la détention de monnaie.** Le taux de la facilité de dépôt
    L1.C10    S24  10,21 | **L'une d'elles a fait coûter la détention de monnaie.** Le taux de la facilité de dépôt
    L1.C13    S1   333 | Elle est libellée en monnaie, chiffrable, et son encours mondial a atteint 315 000 milli
    L1.C13    S18  169,174,188,8 | En 2022 et 2023, le service de la dette extérieure du pays a été de 18,8 puis 17,4 milli
    L1.C14    S7   577 | Multipliée par tous ceux qui, depuis quarante ans, ont eu la transition en charge, elle 
    L1.C16    S9   28,87 | Soffia, Wood et Burchell donnent, pour l'UE-28, une série et non un point : **la proport
    L1.C18    S2   1,20 | 20(1))
    L1.C18    S17  42,91 | Un essai contrôlé randomisé mené en Ouganda — soixante villages traités à soixante-dix d
    L1.C23    S17  10 | Or cette interruption est mesurée : environ 8 % du patrimoine financier des ménages est 
    L1.C23    S20  8 | Or cette interruption est mesurée : environ 8 % du patrimoine financier des ménages est 
    L1.C24    S2   7500,88 | Environ la moitié du volume ne concerne que quelques devises majeures, et le dollar est 

Avertissements seulement. `corpus/controle.py` reste l'autorité ;
aucun de ces points ne refuse une publication.
```

---

## Sabotages

`outils_claude/test_controles_7a.py` — **31 contrôles, 0 échec**, dont douze
nouveaux : quatre détections (appel orphelin, entrée sans citation, citation qui
n'est qu'un titre, chiffre non porté) et **huit contrôles négatifs** qui doivent
rester muets — millésime, `CO2`, date ISO, quantième, appel après le point,
granularité décimale, élision, et le cas conforme.

Les huit négatifs comptent plus que les quatre détections : un contrôle qui
crierait toujours obtiendrait un sans-faute, et les trois premières écritures de
cet outil-ci l'auraient obtenu.
