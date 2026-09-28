# Tri des 36 sources `a_requalifier` de la seconde partie — 2026-09-27

Ce que cette note tranche : rien. Elle classe les 36 sources de C17 à C30 qui
bloquent le passage à `verifie`, pour que l'acquisition puisse être ordonnée.
Écrite par Fable en lecture seule ; **vérifiée par Opus le 2026-09-27 au soir,
pièce par pièce, en ouvrant les fichiers**.

Ce que la vérification a changé. (1) **Neuf numéros de source sur trente-six
étaient faux** : la ligne nommait une entrée qui n'est pas celle dont elle
parle. Trois désignaient une entrée **déjà `ouverte`** — `C21 S7` est la
directive TVA, `C24 S11` est Tooze —, et corriger la référence d'une entrée
`a_requalifier` lui ferait perdre son état (E-L6). Les numéros ci-dessous sont
appariés au contenu de la référence, puis recoupés à la main sur le chapitre.
(2) **Trois fichiers ne portaient pas l'œuvre que leur nom annonce**, et deux
pièces sont des scans sans couche de texte.

Ce que la vérification n'a pas fait : aucune source requalifiée, aucun chapitre
modifié, aucun état enregistré touché.

Cases : (a) exemplaire sur le disque ; (b) en accès libre, à télécharger ;
(c) à télécharger par l'auteur, ou substitut seulement ; (d) livre ou pièce
sans exemplaire.

## Totaux

| case | sources | avant vérification |
|---|---|---|
| a | 14 | 15 |
| b | 2 | 2 |
| c | 4 | 4 |
| d | 16 | 15 |

L'écart vient de `C20 S10` : le fichier du disque n'est pas la pièce de
l'entrée. « a » compte les exemplaires complets, partiels, à identifier ou à
localiser, **y compris deux scans sans couche de texte qui ne valent pas
ouverture** : le détail est dans la table.

| chapitre | à requalifier | a | b | c | d |
|---|---|---|---|---|---|
| C17 | 6 | 2 | 0 | 0 | 4 |
| C18 | 5 | 2 | 0 | 0 | 3 |
| C19 | 1 | 0 | 0 | 1 | 0 |
| C20 | 6 | 1 | 1 | 1 | 3 |
| C21 | 4 | 2 | 0 | 1 | 1 |
| C22 | 3 | 1 | 0 | 0 | 2 |
| C24 | 4 | 2 | 1 | 0 | 1 |
| C25 | 3 | 1 | 0 | 0 | 2 |
| C26 | 1 | 1 | 0 | 0 | 0 |
| C27 | 1 | 0 | 0 | 1 | 0 |
| C29 | 1 | 1 | 0 | 0 | 0 |
| C30 | 1 | 1 | 0 | 0 | 0 |

## Ce que l'ouverture des pièces a appris

1. **`Downloads/goodhart.pdf` n'est pas Goodhart 1975.** C'est « Analysis of
   Financial Stability », de C. A. E. Goodhart **et D. P. Tsomocos**, une
   collaboration des années 2000, 42 pages. Le nom du fichier désignait
   l'auteur, pas l'œuvre. `C20 S10` passe en case (d).
2. **`Downloads/hayek.pdf` est un scan sans couche de texte** : 13 pages, zéro
   caractère extractible. Le nombre de pages est compatible avec Hayek 1945,
   mais la pièce **ne vaut pas ouverture** au sens de la convention.
3. **La table nommait le mauvais fichier Eichengreen.**
   `Exorbitant_Privilege_Eichengreen.pdf` fait 14 pages, s'ouvre sur « Related
   Resources » et parle de « our speaker » : c'est un document d'événement.
   Le livre est `B_Eichengreen_Exorbitant_Privilege_The_R.pdf`, 172 pages.
4. **`Downloads/bdf248-2_dts_web.pdf` n'est pas les statuts du FMI** : c'est le
   *Bulletin de la Banque de France* 248/2, septembre-octobre 2023, sur le
   recyclage des DTS. Commentaire second, non la pièce de 1968-1969.
5. **Le Lietaer sur Wörgl fait deux pages** et se déclare lui-même « extracted
   from the work of Bernard Lietaer », repris de `lietaer.com`. Il a servi à
   L1.C10 ; ce n'est pas une pièce primaire sur l'expérience de 1932-1933.
6. **Le Georgescu-Roegen ne passe pas le contrôle positif de `lire_piece.py`** :
   467 pages et 1 310 231 caractères extraits, mais aucune ligne longue, donc
   aucun témoin. La table de matières lue en page 2 est compatible avec
   l'ouvrage ; l'édition reste à identifier.

## Trois constats qui réduisent le travail

1. **Retiré le 28 : ce constat était faux, et l'erreur est de Fable.** Il
   annonçait quatre sources sans appel au corps. Le compte avait été fait
   sur le rang de l'entrée dans la liste et non sur son champ `ref` ; là où
   les deux diffèrent, l'appel cherché n'était pas le bon. Recompté sur
   `ref` : **les trente-six sources sont appelées au moins une fois**, et la
   colonne « appels » de la table est corrigée en conséquence.
2. Quatre entrées se déclarent déjà ouvertes de première main dans leur
   texte : C24 S4, C25 S12, C26 S9, C30 S1. Leur état `a_requalifier` vient du
   manifeste ; il reste à instruire la requalification, non à trouver la pièce.
   `C25 S12` déclare une édition Cambridge Core lue en ligne : **aucun
   exemplaire local n'est attendu**, et l'absence de fichier n'est pas un
   manque.
3. Sept entrées sont composites : C17 S3, S6, S9, S12 ; C18 S12, S15 ;
   C21 S10 (et C29 S4, la même). La règle du 2026-09-20 veut une entrée par
   signature : les scinder isole la partie qu'on peut ouvrir.

Des trente-six sources, 25 portent un seul appel au corps (recompté le 28). Pour
celles de la case (d), la question est celle de l'énoncé unique qui en
dépend : le garder en `::hypothese::`, le renvoyer à un chapitre qui porte la
pièce, ou le retirer.

## Table

Les numéros corrigés portent leur ancienne valeur entre parenthèses.

| chapitre | source | appels | pièce | case | exemplaire, remarque |
|---|---|---|---|---|---|
| C17 | S3 | 1 | Doolittle 1981 ; Dawkins 1982 (composite) | d | `Downloads/OMalley-Doolittle_dreamer.pdf` est un texte SUR Doolittle, non de lui. Entrée à scinder. |
| C17 | S5 | 1 | Prigogine, Stengers, La Nouvelle Alliance, 1979 | d | livre ; aucun exemplaire |
| C17 | S6 | 1 | Schrödinger 1944 ; Georgescu-Roegen 1971 (composite) | a partiel | **OUVERT** : `Codex/2026-09-14/c03/georgescu-entropy-law-1971.pdf`, 467 p., 1 310 231 car. — mais **contrôle positif impossible**, aucune ligne longue ; édition à identifier. Schrödinger : aucun. Entrée à scinder. |
| C17 | S8 | 1 | Tucker, Unelected Power, 2018, 2e partie | d | livre ; aucun exemplaire trouvé |
| C17 | S9 | 1 | Bank Charter Act 1844 ; Act 1694 ; Riksbank ; Goodhart 1988 (composite) | a partiel | **CONFIRMÉ** : `Codex/2026-09-15/c17/candidats/S9-uk-bank-charter-act-1844-legislation-gov-uk-fourni.pdf`, 8 p., « An Act to regulate the Issue of Bank Notes… 1844 CHAPTER 32 ». Le reste : aucun. Entrée à scinder. |
| C17 | S12 | 1 | Knapp 1905 ; Ingham 2004 (composite) | d | livres ; aucun exemplaire. Entrée à scinder. |
| C18 | S7 | 2 | Tucker, Unelected Power, chap. 4, p. 77-108 | d | l'entrée cite une page et une phrase : dire d'où vient la citation |
| C18 | S12 (table : S11) | 2 | Buchanan, Tullock 1962 ; Tsebelis 2002 (composite) | a partiel | **CONFIRMÉ** : `Codex/2026-09-15/c14/S11-buchanan-tullock-calculus-of-consent-oll.pdf`, 270 p. — **édition Online Library of Liberty**, non University of Michigan Press comme l'entrée la nomme. Tsebelis : aucun. Entrée à scinder. |
| C18 | S15 (table : S14) | 1 | Ramsar 1971 ; CITES 1973 ; CDB 1992 (composite) | a partiel | **CONFIRMÉS, tous deux au Recueil des traités des Nations unies** : `C18-S15-convention-ramsar-1971.pdf` (n° 14583, 10 p.) et `C18-S15b-cites-1973.pdf` (n° 14537, 61 p.), dans `Codex/2026-09-16/acquisitions-c17-c30/`. **Les noms de fichiers portaient déjà le bon numéro.** CDB : texte libre sur le site du traité (b). Entrée à scinder. |
| C18 | S20 (table : S18) | 1 | INDEC, Argentine 2007-2015 | d | aucune pièce nommée dans l'entrée : un fait d'actualité sans signature |
| C18 | S22 (table : S19) | 1 | Doctrine fiduciaire, public trust | d | aucune pièce nommée |
| C19 | S7 (table : S6) | 2 | Rambaud, Richard 2015, CPA 33 | c | substitut HAL sur le disque (`courses-c17-c30/fournis/SUBSTITUT-rambaud-…`), non la pièce |
| C20 | S2 | 2 | Rueff 1963 et 1971 (composite) | d | livres ; aucun exemplaire |
| C20 | S3 | 1 | Fisher 1911, chap. II | a | **CONFIRMÉ** : `Codex/2026-09-14/c12/fisher-1911-ppm.pdf`, 543 p., « THE PURCHASING POWER OF MONEY », numérisation FRASER / Federal Reserve Bank of St. Louis. Déjà lu pour L1.C12. |
| C20 | S4 | 1 | Gurley, Shaw 1960, chap. 3 | d | l'entrée cite p. 72-73 : dire d'où vient la citation |
| C20 | S7 | 1 | Rambaud, Richard 2015 | c | comme C19 S7 : substitut seulement |
| C20 | S8 | 1 | FMI, premier amendement, DTS, 1968-1969 | b | statuts du FMI en accès libre. **`Downloads/bdf248-2_dts_web.pdf` N'EST PAS cette pièce** : c'est le *Bulletin de la Banque de France* 248/2, sept.-oct. 2023, 9 p., sur le recyclage des DTS — commentaire second. |
| C20 | S10 | 1 | Goodhart 1975 | **d** (était a) | **`Downloads/goodhart.pdf` N'EST PAS Goodhart 1975** : « Analysis of Financial Stability », Goodhart **et Tsomocos**, 42 p., années 2000. Aucun exemplaire de la pièce de 1975. |
| C21 | S5 | 1 | Rueff 1963 et 1971 | d | comme C20 S2 |
| C21 | S9 (table : S7) | 1 | Wörgl, 1932-1933 | a | **OUVERT, mais pièce mince** : `Codex/2026-09-15/c10/S1-lietaer-worgl.pdf` ne fait **2 pages** et se dit « extracted from the work of Bernard Lietaer », repris de `lietaer.com`. Déjà lu pour L1.C10 ; renvoi possible vers L1.C10. **`C21 S7` est la directive TVA, déjà `ouverte` : ne pas y toucher.** |
| C21 | S10 (table : S8) | 1 | Bovenberg, de Mooij 1994 ; Fullerton, Metcalf 1997 (composite) | a partiel | **SCAN SANS COUCHE DE TEXTE, confirmé** : `Codex/2026-09-19/c29/C29-S4-nber-w6199-fullerton-metcalf-1997-SCAN-SANS-TEXTE.pdf`, 42 p., **0 caractère**. Ne vaut pas ouverture. |
| C21 | S11 | 1 | Umlauf 1993, JFE | c | deux substituts sur le disque, non la pièce |
| C22 | S4 | 3 | Ostrom 1990, Governing the Commons | d | substitut : Ostrom 2009, Banque mondiale WPS5095, sur le disque |
| C22 | S10 | 1 | Hayek 1945, AER | a | **`Downloads/hayek.pdf` : 13 p., 0 caractère extractible.** Le nombre de pages est compatible avec l'article de 1945, mais la pièce **ne vaut pas ouverture**. |
| C22 | S12 | 1 | Baumol, Panzar, Willig 1982 | d | livre ; aucun exemplaire |
| C24 | S3 | 1 | Mehrling, notes de cours | a | **CONFIRMÉ, et c'est bien la leçon citée** : `Codex/2026-09-15/c25/S5-mehrling-lec14-money-and-the-state-international.pdf`, 6 p., titrée « 14. Money and the State, International ». |
| C24 | S4 | 6 | Eichengreen 2011 | a | **LE FICHIER DE LA TABLE ÉTAIT LE MAUVAIS.** `Exorbitant_Privilege_Eichengreen.pdf` fait 14 p. et est un document d'événement. Le livre est `Downloads/B_Eichengreen_Exorbitant_Privilege_The_R.pdf`, **172 p., 505 257 car.** L'entrée se dit ouverte le 09-04, ouvrage procuré par l'auteur : requalification à instruire. |
| C24 | S5 | 1 | Triffin 1960 | d | livre ; substituts sur le disque (Maes-Pasotti 2016, Faudot 2022) |
| C24 | S12 (table : S11) | 2 | BRI, enquête triennale 2022 | b | adresse dans l'entrée. **`C24 S11` est Tooze, déjà `ouverte` : ne pas y toucher.** |
| C25 | S6 | 2 | Despres, Kindleberger, Salant, The Economist, 1966 | d | aucun exemplaire |
| C25 | S11 | 1 | Triffin 1960 | d | comme C24 S5 |
| C25 | S12 | 5 | Keynes, Collected Writings XXV | a | **l'entrée déclare une édition Cambridge Core (DOI 10.1017/UPO9781139520188) lue en ligne le 09-04** : aucun exemplaire local n'est attendu, et l'absence de fichier n'est pas un manque. Requalification à instruire. |
| C26 | S9 (table : S6) | 2 | Eichengreen 2011 | a | comme C24 S4, même livre de 172 p. |
| C27 | S5 | 1 | Barrett 1994, OEP 46 | c | revue sous abonnement ; les fichiers « barrett » du disque sont d'un autre auteur |
| C29 | S4 | 1 | Bovenberg, de Mooij 1994 ; Fullerton, Metcalf 1997 | a partiel | comme C21 S10 : scan sans texte, 0 caractère |
| C30 | S1 | 10 | J.-C. Duval, épisode 30 | a | pièce de l'auteur, sur son Drive ; requalification à instruire |

## Ce qui reste à faire, et par qui

- **À l'auteur** : la pièce de `C20 S10` (Goodhart 1975) et celle de `C22 S10`
  (Hayek 1945 avec une couche de texte) ne sont pas sur le disque. Deux scans
  sans texte — `C21 S10` et `C29 S4`, la même pièce — sont à reprendre ou à
  remplacer.
- **À instruire, sans acquisition** : les quatre entrées qui se déclarent
  ouvertes de première main et dont l'état `a_requalifier` vient du manifeste.
- **À scinder, avant toute ouverture** : les sept entrées composites. Une
  entrée, une signature.
- **Rien n'est requalifié ici.** Aucune source ne change d'état, aucun chapitre
  n'est modifié.

## Complément du 2026-09-28 — les acquisitions de l'auteur

Dossier : `Documents/Codex/2026-09-28/courses-livre-1/fournis`, 77 PDF renommés
par Codex après inspection des pages d'identification ; correspondance et
empreintes dans `correspondance-renommage.csv`. Rien n'y a été renommé,
déplacé ni supprimé par Fable.

Ce que Fable a fait : extraction par `pdftotext` des huit fichiers
prioritaires, lecture des pages de titre et de copyright, compte des pages
sans texte, recherche des termes des entrées avec contrôle positif. Ce que
Fable n'a pas fait : lire les pièces. Les pages données ci-dessous disent où
lire, non ce que la lecture établira. Aucune source n'est requalifiée.

Notation des pages : « f. » est le folio imprimé, « pdf » la page du fichier.

### Exemplaires confirmés — la pièce est celle de l'entrée

| source | pièce, édition relevée sur le fichier | complet | texte | où lire |
|---|---|---|---|---|
| C22 S12 | Baumol, Panzar, Willig, *Contestable Markets and the Theory of Industry Structure*, Harcourt Brace Jovanovich, © 1982 ; numérisation Internet Archive | oui, 552 p. pdf | oui, 20 pages vides | définition 2A2 du monopole naturel par la sous-additivité, f. 17 (pdf 53) ; « natural monopoly is not, in general, a sufficient condition for marginal cost pricing to be unprofitable », f. 16 (pdf 52) ; chap. 2 en entier |
| C20 S4 | Gurley, Shaw, *Money in a Theory of Finance*, Brookings, 1960, sixième tirage 1970 | oui, 385 p. pdf | oui, 12 pages vides | f. 72-73 (pdf 86-87) ; f. 135 (pdf 149) ; glossaire f. 363-364 (pdf 377-378) |
| C22 S4 | Ostrom, *Governing the Commons*, Cambridge University Press, série Political Economy of Institutions and Decisions | oui, 295 p. pdf | oui, OCR bruité | tableau des principes, f. 90 (pdf 104) ; huertas, f. 69-82 ; zanjeras, f. 82-88 ; accès libre, f. 32 et 48. L'année du tirage est à lire sur la page de copyright |
| C17 S12, partie Ingham | Ingham, *The Nature of Money*, Polity, 2004 | oui, 338 p. pdf | oui | Knapp et l'impôt : pdf 64-67 et 74 ; les folios ne sont pas extraits, à relever à l'écran |
| C17 S6, partie Schrödinger | *What Is Life? with Mind and Matter and Autobiographical Sketches*, Cambridge University Press, édition Canto | oui, 196 p. pdf | oui | chap. 6, f. 67-75 (pdf 79-86), dont la note au chapitre 6, f. 74 |
| C19 S7, partie livre | Richard, avec Rambaud, *Révolution comptable*, 2020 | oui, 109 p. pdf | oui | les douze propositions du modèle CARE/TDL, pdf 54-78 ; annexe 1. **Édition numérique sans folios** : les pages du fichier ne sont pas celles du livre imprimé, l'entrée devra citer le chapitre et la proposition |

### Pièces partielles ou d'une autre édition

| source | fichier | écart |
|---|---|---|
| C18 S12, partie Tsebelis | Tsebelis, *Veto Players*, manuscrit « Forthcoming », daté 11/01/01, 440 p., texte présent | l'entrée cite l'édition Princeton 2002. Le manuscrit porte la thèse (argument général, p. 12-13 du manuscrit) ; ses pages ne sont pas celles du livre. À entrer comme manuscrit, ou à tenir pour substitut |
| C17 S6, partie Schrödinger | « texte recomposé », 31 p. | même texte apparent, sans édition ni folios : ne sert qu'à la recherche, l'édition Canto fait foi |
| C19 S7 et C20 S7, partie article | Rambaud, Richard 2015, *Critical Perspectives on Accounting* | toujours absent. Le livre de 2020 porte le même modèle ; C20 S7 ne cite que l'article et devra changer de pièce ou l'obtenir |

### Substituts — ils ne sont pas la pièce de l'entrée

| source | pièce attendue | ce que le dossier contient |
|---|---|---|
| C17 S3 | Doolittle 1981 ; Dawkins 1982 | O'Malley sur Doolittle ; un résumé Bookey et une recension de Dawkins ; littérature sur Gaïa (Bourrat, Dutreuil, Lenton et Williams, Levine) |
| C17 S5 | Prigogine, Stengers, *La Nouvelle Alliance* | Stengers, *Cosmopolitiques 3* ; une recension de Gerbaud |
| C17 S8, C18 S7 | Tucker, *Unelected Power* | deux recensions de six pages, un entretien, une présentation de 51 pages |
| C17 S9, partie Goodhart | Goodhart, *The Evolution of Central Banks*, 1988 | un chapitre de Goodhart de 2016 ; Ugolini, *The Evolution of Central Banking* |
| C17 S12, partie Knapp | Knapp 1905 | Greitens 2022, Waizbort 2020, Buza : sur Knapp, non de Knapp |
| C20 S2, C21 S5 | Rueff 1963, 1971 | Grin 1999, de Larosière, Teulon et Fischer 2011 : sur Rueff |
| C24 S5, C25 S11 | Triffin 1960 | Grin 1999 ; Maes et Pasotti 2022 |
| C25 S6 | Despres, Kindleberger, Salant 1966 | Laffer (deux pièces), Mikesell, un extrait de 1987 : la même controverse, d'autres auteurs |
| C21 S9 | Umlauf 1993 | cinq études ultérieures sur les taxes de transaction |
| C27 S5 | Barrett 1994 | Rubio et Ulph 2004 ; McEvoy et Stranlund 2006 ; une revue de littérature |

### Toujours manquantes, sans substitut dans le dossier

C18 S12 partie Buchanan-Tullock exceptée, déjà sur le disque. C18 S18
(statistique argentine) et C18 S19 (doctrine fiduciaire), qui ne nomment
aucune pièce. C21 S8 et C29 S4 : Bovenberg et de Mooij 1994 absent,
Fullerton et Metcalf en scan sans texte. C17 S9 : les actes de 1694 et la
Riksbank.

### Un écart relevé dans une entrée, à instruire avant tout

**C20 S4 cite entre guillemets deux phrases que l'exemplaire ne contient
pas.** L'entrée donne, p. 72-73 : « Inside money is money that is issued on
the collateral of private domestic debt [...] Outside money is money that
represents a net claim by the private sector on the government or the rest
of the world » ; et p. 135 : « backed by foreign or government debt or by
gold, or is fiat money issued by the government ».

Relevé sur le texte extrait, césures recollées : « issued on the », «
represents a net claim », « rest of the world » et « backed by foreign or
government debt » : zéro occurrence chacun. Contrôle positif : « inside
money » 35 occurrences, « outside money » 51.

Ce que l'exemplaire porte : aux f. 72-73, la distinction elle-même, en
d'autres mots (« It is based on internal debt, so we refer to it as "inside"
money ») ; au f. 135, l'exemple chiffré et la doctrine de la monnaie nette ;
au glossaire, f. 363-364 : « Inside money — Money based on private domestic
primary securities » et « Outside money — Money that is backed by foreign or
government securities or gold; or fiat money issued by the government ».

Le fond de l'entrée paraît donc porté par la pièce ; les guillemets, eux,
entourent une paraphrase, et la seconde citation est au glossaire et non à
la p. 135. Limite de ce relevé : il repose sur une reconnaissance de
caractères ; il se confirme en lisant les trois pages à l'écran.

### Ce que les acquisitions changent au compte

Des quinze sources classées « sans exemplaire » le 27, quatre ont désormais
leur pièce (C20 S4, C22 S4, C22 S12, et la partie Ingham de C17 S12) ; deux
entrées composites gagnent leur partie manquante (C17 S6 en entier avec
Georgescu-Roegen déjà sur le disque ; C19 S7 par le livre). Dix restent sans
pièce, avec ou sans substitut : C17 S3, S5, S8 ; C18 S7, S18, S19 ; C20 S2 ;
C21 S5 ; C24 S5 ; C25 S6 et S11 valant la même pièce que C24 S5.
