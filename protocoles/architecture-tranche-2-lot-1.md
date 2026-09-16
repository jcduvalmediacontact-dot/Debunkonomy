# Architecture de reprise — tranche 2, lot 1 : L1.C02, L1.C04, L1.C05, L1.C06

**Écrit le 2026-09-15 par Claude. Régime de travail : METHODE-AUDITS, METHODE-REECRITURES, METHODE-PERIMETRE, METHODE-PARALLELISME (`coordination/DECISIONS_AUTEUR.md`).** Les quatre chapitres sont « conserver » ou « corriger localement » dans le plan de refonte, régime `hybride` : une passe adverse externe, l'audit factuel et le balayage mécanisé ; pas d'audit tiers.

**Ce document ne décide rien.** Il sépare ce qui est déterminé — par la convention, par un arbitrage déjà rendu ou par le texte même du chapitre — de ce qui revient à l'auteur, et il numérote ces décisions pour qu'elles se rendent en une séance. Une affirmation sans source a trois sorts possibles, et le sigle est le même partout :

| sigle | sort | ce que cela coûte |
|---|---|---|
| **A** | **appuyer** sur une source primaire nommée, à ouvrir | une acquisition et une lecture |
| **D** | **déclarer** l'énoncé rapporté sans appui ouvert, dans le corps | une phrase ; l'énoncé perd son statut de fait établi |
| **R** | **retirer** l'énoncé | rien, si le chapitre n'en dépend pas |

**Règle appliquée partout :** `verifie` exige que chaque source déclarée soit `ouverte` et que `verifications_en_attente` soit vide. Tout énoncé factuel non sourcé doit donc recevoir A, D ou R avant le gel. Ce que la relecture a établi et qui commande le lot : **le coût n'est pas dans les dix-neuf sources déclarées, il est dans les affirmations qui n'en ont pas.**

---

## 0. Ce que le relevé mécanique des acquisitions a rendu

Le relevé mécanique (`releve_acquisitions.py`, lecture seule) a inventorié les fichiers laissés par les sous-agents interrompus, calculé leurs empreintes, extrait leur texte page par page et cherché dans chaque document les citations entre guillemets de l'entrée de source correspondante.

| chapitre | sources fermées | avec un document à texte | citations d'entrée retrouvées |
|---|---|---|---|
| C02 | 6 | 6 | 0 / 0 |
| C04 | 9 | 7 | 4 / 4 |
| C05 | 2 | 1 | 0 / 0 |
| C06 | 2 | 2 | 0 / 0 |
| C10 | 22 | 18 | 7 / 9 |
| C13 | 16 | 13 | 7 / 9 |
| C14 | 12 | 7 | 3 / 6 |
| C23 | 17 | 16 | 20 / 37 |
| C25 | 12 | 9 | 17 / 25 |

**79 sources sur 98 ont un document à couche de texte au dossier.** Les manques du lot 1 : Richardson et al. 2023 (C04 S2, le dépôt PubMed Central a rendu un fichier vide), la page du Planetary Health Check (C04 S4 — le résumé exécutif est au dossier de C02), Friedman 1991 (C05 S2, Hoover a répondu 403), les données AQUASTAT (C02 S6, FAO a répondu 403 et 401 ; seule la page d'accueil est au dossier).

---

## 1. L1.C02 — La grande contradiction

**Verdict du plan :** conserver et sourcer — « un des chapitres les mieux construits du diagnostic ». **Statut :** `brouillon`, 6 sources déclarées, 24 vérifications. **Régime :** hybride ; le § 2 et le § 6 balisent avec soin ce qui est constaté, supposé et déduit.

### 1.1 Corrections déterminées, sans décision

1. **Le chapeau contredit le corps.** Il écrit : « La seconde série n'est pas le prix accidentel de la première : elle en est le moyen. La valeur financière enregistrée est produite par le transfert hors bilan de coûts physiques réels ». Le § 2 écrit, sous `::etat::` : « Rien dans ce chapitre ne permet de trancher », et le § 6 range le lien de production sous « Ce qui est supposé ». **Le chapeau doit dire ce que le § 6 dit** — même défaut que le chapeau de L1.C11 corrigé ce matin.
2. **Le résumé contredit le § 2.** Il écrit « Ce chapitre établit la corrélation » ; le § 2 écrit « Le mot de corrélation lui-même serait prématuré ». Le résumé doit porter « décrit une progression conjointe ».
3. **Une thèse non balisée au § 4.** « Le même mécanisme opère entre États. Un pays qui internaliserait seul ses coûts environnementaux verrait ses entreprises se délocaliser… » est un paragraphe sans marqueur, donc lu au régime descriptif par défaut ; c'est une thèse, comme le paragraphe qui le précède (`::hypothese::`). À baliser.
4. **Renvois.** L'en-tête n'en déclare aucun. Le § 2 annonce « le chapitre suivant » (L1.C03, `audit_contradictoire`) et « les chapitres à partir du cinquième » (L1.C05, L1.C07) ; le § 3 nomme la fausse richesse. Déclarer L1.C03, L1.C05 et L1.C07 aux endroits où le corps les désigne. La vérification « renvoi vers la bullshitnovation » n'a pas d'ancre dans le corps : différée.
5. **Vérifications devenues sans objet :** « production agricole triplée » (déjà retirée du texte), « auto-cannibalisme » (l'expression n'est pas dans le corps), les cinq entrées TEXTILE (le § 3 déclare écarter tout chiffre — c'est une limite portée par le corps), la PRÉCAUTION sur les éditions du Global Resources Outlook (à porter dans l'entrée S5).

### 1.2 Sources déclarées

| ref | nature | état du relevé | document à texte au dossier | pages | empreinte (12) | citations de l'entrée retrouvées |
|---|---|---|---|---|---|---|
| S1 | donnees | document avec texte | `S1-ipbes-ldr-full-report-2018.pdf` | 748 | 8A7ABB38980E | aucune citation dans l'entrée |
| S2 | donnees | document avec texte | `S2-phc2025-executive-summary.pdf` | 13 | 7267D997563C | aucune citation dans l'entrée |
| S3 | donnees | document avec texte | `S3-wwf-lpr2024.pdf` | 94 | 629A7DDFB254 | aucune citation dans l'entrée |
| S5 | donnees | document avec texte | `S5-unep-gro2024-full-report.pdf` | 181 | D068E5A9DF8B | aucune citation dans l'entrée |
| S6 | donnees | document avec texte | `S6-fao-landing.html` |  | 0B8E185DE42F | aucune citation dans l'entrée |
| S4 | donnees | document avec texte | `S4-unep-egr2025-full-report.pdf` | 76 | D5364C4761DF | aucune citation dans l'entrée |

Relevé : `Documents/Codex/2026-09-15/c02/releve-acquisition-c02.md`. **Un document au dossier n'est pas une source ouverte** : l'ouverture est la lecture du passage employé, avec empreinte, édition et folio, faite par Claude après les décisions.

**Deux versements possibles depuis des chapitres vérifiés hier**, sans nouvelle lecture d'ensemble mais avec relecture du passage employé ici : **S5** (Global Resources Outlook 2024, ouvert pour L1.C12 [S2] aux folios 18, xiv et 4 : 30 à 106 Gt, 2,3 % par an) et **S4** (Emissions Gap Report 2025, ouvert pour L1.C12 [S9] sur l'exemplaire fourni par l'auteur : 57,7 GtCO2e en 2024, +2,3 %). Reste à vérifier sur le même exemplaire l'énoncé « baisser de 40 % d'ici 2030 par rapport à 2019 », qui n'a pas été contrôlé pour L1.C12.

### 1.3 Affirmations sans source — décisions demandées

| n° | énoncé (§) | proposition | motif |
|---|---|---|---|
| **D1** | « Le patrimoine cumulé des cent premières fortunes mondiales dépasse le PIB de continents entiers » (§ 1) | **R** | chiffre de plaidoyer sans source institutionnelle ; le chapitre n'en dépend pas |
| **D2** | « Les indices boursiers atteignent des sommets historiques. Le produit mondial brut n'a jamais été aussi élevé » (§ 1) | **A** pour le produit mondial (série de la Banque mondiale, PIB courant) ; **D** pour les indices | un record boursier est daté et périssable ; la série du produit est institutionnelle |
| **D3** | **APPLIQUÉE le 2026-09-15 par **D**, sur la réponse de l'auteur (« D3, D5 : D au lieu de A ») : la phrase reste et ne porte aucun appel.** « Un tiers de la surface forestière mondiale a disparu depuis le milieu du XIXe siècle, principalement au profit de terres agricoles » (§ 1) | **A** si une source primaire est trouvée (Williams 2003 ; FAO) ; sinon **D** | énoncé quantifié, donc attaquable |
| **D4** | « L'agriculture est la première cause de déforestation mondiale » (§ 2) | **A** (FAO, enquête par télédétection de l'évaluation forestière 2020 : l'expansion agricole cause près de 90 % de la déforestation) | source officielle, libre |
| **D5** | **APPLIQUÉE le 2026-09-15 par **A**, après la recherche et la comparaison que l'auteur a demandées : l'énoncé s'adosse à S6 (SOLAW, page PDF 58) et le corps passe de terres cultivables à terres cultivées. Poore et Nemecek 2018 donnent 38 %, écart porté dans l'entrée.** « Un tiers des terres cultivables sert à l'alimentation animale » (§ 2) | **A désormais possible** : FAO, *The State of the World's Land and Water Resources for Food and Agriculture 2021* (SOLAW 2021, publié 2022, 393 pages), fourni par l'auteur le 2026-09-15 : « feed and fodder production taking up roughly one-third of total cropland » (p. 57 et 58 PDF) — à confirmer, l'auteur ayant d'abord retenu D | source officielle, au mot |
| **D6** | « Les sols s'érodent et les nappes s'épuisent » (§ 1) | **A** en rattachant l'énoncé à [S1] (IPBES, dégradation des terres) | S1 porte le constat, il suffit de l'appeler |
| **D7** | **APPLIQUÉE le 2026-09-15 par **A** : S6 réécrite sur SOLAW et ouverte ; le corps passe à 16 % pour l'industrie et 12 % pour les usages municipaux.** « 72 % des prélèvements mondiaux d'eau douce… 15 %… 13 % [S6] » (§ 2) | **A sur SOLAW 2021** (FAO, fourni le 2026-09-15), p. 96 PDF, tableau 1.13 : agriculture 2 950 km3 (72 %), usages municipaux 483 km3 (12 %), industrie 646 km3 (16 %) en 2018 — le corps passe de « l'industrie à 15 % et les services à 13 % » à « l'industrie à 16 % et les usages municipaux à 12 % », et S6 est réécrite sur SOLAW ; l'ancienne proposition (page de méthode AQUASTAT : 69 / 12 / 19) reste possible mais moins proche du texte du chapitre | la source ouverte porte le 72 % du chapitre ; les deux autres parts diffèrent d'un point |
| **D8** | « Dette mondiale cumulée » (vérification 8 ; l'énoncé du § 2 dit seulement « l'endettement progresse ») | **A** par versement de L1.C13 [S1] (IIF, 315 000 Md$ au T1 2024) si le corps chiffre ; sinon rien à faire | le corps ne chiffre pas aujourd'hui |

### 1.4 Cohérence avec les voisins vérifiés

- Le § 2 renvoie l'épreuve empirique au « chapitre suivant » : **L1.C03 établit l'absence de découplage absolu mondial sur 2015-2023, sur des taux observés, non une impossibilité** — le § 2 et le § 6 disent « si le découplage était possible et observé » ; c'est compatible, mais le résumé de L1.C03 doit être relu contre le § 2 après ouverture de ses sources.
- Le § 3 annonce que le passage « de la rentabilité à l'allocation du crédit… n'est pas démontré ici ». **L1.C07 et L1.C11, vérifiés, établissent la sélection des emprunteurs par la solvabilité anticipée** ; le chapitre peut désormais y renvoyer sans changer de sens.

---

## 2. L1.C04 — L'économie à l'intérieur de la nature

**Verdict du plan :** corriger localement, en renvoyant à L1.C23 pour le coût de la robustesse. **Statut :** `brouillon`, 9 sources, 11 vérifications. **Régime :** hybride ; presque chaque paragraphe est balisé.

### 2.1 Corrections déterminées

1. **Renvois.** Aucun déclaré. Le chapeau désigne « le précédent » (L1.C03), le § 3 et le § 6 « le premier chapitre » (L1.C01), le § 6 « Le chapitre 2 » (L1.C02), le § 7 « le chapitre suivant » (L1.C05). Déclarer les quatre.
2. **Le renvoi à L1.C23 que le plan demande.** Le § 5 écrit que la robustesse « se paie en efficacité » sans le développer ; **L1.C23 § 2 établit exactement ce prix** — redondance, diversité, modularité, « une réduction délibérée de l'efficacité mesurée dont quelqu'un supporte le prix ». Une phrase de renvoi au § 5 suffit ; L1.C23 est dans le lot 2 de cette tranche.
3. **La liste du plancher social.** Le § 4 énumère onze dimensions et cite [S7] (2012, onze) puis [S3] (2017, douze). Le corps suit la version de 2012 ; l'écrire, ce que la vérification 3 demandait.
4. **Deux vérifications sont déjà des limites portées par le corps :** les mesures de sensibilité des chaînes (§ 5 : « Leur rassemblement reste à faire pour ce corpus ») et le recensement des cas d'action coordonnée (§ 3 : « suppose un recensement que ce chapitre n'a pas conduit »). Elles quittent le champ sans autre traitement.

### 2.2 Sources déclarées

| ref | nature | état du relevé | document à texte au dossier | pages | empreinte (12) | citations de l'entrée retrouvées |
|---|---|---|---|---|---|---|
| S1 | theorie | document avec texte | `S1-rockstrom2009-ecologyandsociety.pdf` | 33 | 073961D069BD | 1 / 1 |
| S2 | theorie | fichier sans texte exploitable | — |  |  | aucune citation dans l'entrée |
| S3 | theorie | document avec texte | `S3-chelseagreen-doughnut.html` |  | 9C1B91D1A928 | aucune citation dans l'entrée |
| S4 | donnees | page bloquee ou metadonnees | — |  |  | aucune citation dans l'entrée |
| S5 | donnees | document avec texte | `S5-friedlingstein2026-gcb2025-essd.pdf` | 78 | 166E10A66B4D | aucune citation dans l'entrée |
| S7 | theorie | document avec texte | `S7-oxfam-policy-practice-landing.html` |  | A7913BD25C61 | 1 / 1 |
| S8 | theorie | document avec texte | `S8-fanning-raworth2025-nature.pdf` | 24 | 12C504E3D0C1 | 1 / 1 |
| S9 | theorie | document avec texte | `S9-devos-msr.html` |  | 0E05BAE53DC5 | 1 / 1 |
| S6 | theorie | document avec texte | `S6-ipcc-tar-wg1-ch03.pdf` | 56 | C22466727205 | aucune citation dans l'entrée |

Relevé : `Documents/Codex/2026-09-15/c04/releve-acquisition-c04.md`. **Un document au dossier n'est pas une source ouverte** : l'ouverture est la lecture du passage employé, avec empreinte, édition et folio, faite par Claude après les décisions.

**Versement possible :** **S5** (Global Carbon Budget 2025, ouvert pour L1.C03 [S2] hier sur la série xlsx et l'article) — la valeur de 422,8 ppm en 2024 reste à lire sur l'exemplaire, elle n'a pas été contrôlée pour L1.C03.

### 2.3 Affirmations sans source — décisions demandées

| n° | énoncé (§) | proposition | motif |
|---|---|---|---|
| **D9** | **SANS OBJET, constaté le 2026-09-15 sur la réponse de l'auteur : la phrase sur le protocole de Montréal n'existe plus dans L1.C02 ni L1.C04.** « Le protocole de Montréal, adopté en 1987 » (§ 3) | **A** (texte officiel du Secrétariat de l'ozone, PNUE) | source officielle libre, un appel suffit |
| **D10** | « l'ouvrage de 1776 d'Adam Smith s'ouvre sur la division du travail » (§ 5) | **A** (domaine public, livre I, chapitre 1) | vérification immédiate |
| **D11** | « plusieurs traditions [de la robustesse en économie] » — contrôle robuste, décision robuste, résilience territoriale (§ 5) | **D** : le site de la RAND a répondu 403 et les deux autres références sont sous droits ; l'énoncé est déclaré rapporté sans appui ouvert, avec les trois noms de tradition | le § 5 affirme contre « ce qui est parfois avancé » ; sans appui ouvert, il doit le dire |
| **D12** | APPLIQUÉE le 2026-09-15 — l'ouvrage de 2017 est introuvable en numérique (copie PDFDrive refusée, article jumeau du Lancet refusé deux fois) et **il n'était nécessaire à rien** : S8, ouverte, atteste l'ouvrage à sa référence 3 avec son titre complet et porte les douze dimensions du plancher social. S3 retirée ; le corps nomme l'ouvrage, adossé à S8, et sa liste passe de onze à douze dimensions — **la connectivité manquait**, et trois libellés étaient raccourcis | aucune | R, comme l'auteur l'avait tranché | [S3] K. Raworth, *Doughnut Economics*, 2017 — ouvrage sous droits, cité pour « développer dans un ouvrage de 2017 » et pour la liste des dimensions | **fournir l'ouvrage** (l'auteur le possède-t-il ?) **ou R** : retirer S3 et garder la mention de l'ouvrage comme fait rapporté, le § 4 reposant sur [S7] et [S8] | une source déclarée doit être ouverte |
| **D13** | **APPLIQUÉE le 2026-09-15 : S6 réduite au chapitre 3 du troisième rapport du GIEC et ouverte ; Indermühle et al. nommé sans être source.** [S6] Indermühle et al., *Nature*, 1999 — sous droits ; le même énoncé (260-280 ppm sur l'Holocène) est porté par le chapitre 3 du troisième rapport du GIEC, acquis | **réduire S6 au GIEC** si le passage y est retrouvé ; sinon fournir l'article | une source suffit si elle porte l'énoncé |
| **D14** | **APPLIQUÉE le 2026-09-15 : S9 scindée, De Vos y reste, Ceballos passe à une entrée S10 créée ; les deux ouvertes, un appel à chacune.** [S9] De Vos et al. 2015 et Ceballos et al. 2015 (accès ouvert) — **De Vos acquis l'après-midi sur la copie en accès ouvert déposée par Duke** (DukeSpace, hdl 10161/23550, 1286882 octets, SHA-256 1152B0B99686…) | **scinder** S9 en deux entrées (contrôle 2 d'AGENTS.md : deux articles, deux thèses) ; ouvrir les deux ; plus de **D** nécessaire pour le taux de fond | l'entrée réunit deux textes aux résultats opposés |

### 2.4 Cohérence avec les voisins vérifiés

- Le § 6 fait reposer la troisième condition sur l'émission monétaire et le § 7 dit qu'elle « n'est pas faite ici ». **L1.C07, L1.C08, L1.C15 sont vérifiés** : le renvoi peut nommer ce qui est établi (sélection par la solvabilité ; contrainte de croissance conditionnelle ; essentiel insolvable défini) sans faire dire à ces chapitres plus qu'ils n'établissent — L1.C08 n'établit pas de contrainte arithmétique, et le § 6 n'en affirme pas.

---

## 3. L1.C05 — Qu'est-ce que la monnaie, vraiment ?

**Verdict du plan :** corriger localement, « 2 sources pour un chapitre pivot est insuffisant ». **Statut :** `brouillon`, 2 sources, 17 vérifications. **Régime :** hybride, balisage complet.

### 3.1 Corrections déterminées

1. **Renvois.** L'en-tête déclare L1.C07 seul. Le § 6 annonce « Le chapitre suivant » (L1.C06) ; le § 4 cite Wörgl, le WIR et les monnaies locales, **que L1.C10 instruit avec dix sources dans cette même tranche** ; le § 4 et le § 6 désignent « les chapitres précédents » et « les chapitres deux et trois ». Déclarer L1.C02, L1.C03, L1.C06, L1.C10.
2. **Vérifications sans objet :** Aristote et Théret ne sont pas nommés dans le corps (vérifications 6 et 7) ; « 92 % » et « doctorat » sont déjà traités par abstention dans le corps (vérifications 1 et 2, le § 3 et le § 5 disent expressément ne rien reprendre) ; la vérification 3 (motivations) est traitée au § 5 (« effet, non intention »).
3. **Le § 5 dit d'une observation qu'elle « se vérifie » sans la vérifier.** « Les manuels introduisent la monnaie par ses fonctions et traitent brièvement de son émission. Cette observation… se vérifie » : soit deux manuels sont cités, soit la phrase dit « n'est pas vérifiée ici ». Voir D18.

### 3.2 Sources déclarées

| ref | nature | état du relevé | document à texte au dossier | pages | empreinte (12) | citations de l'entrée retrouvées |
|---|---|---|---|---|---|---|
| S1 | theorie | document avec texte | `S1-furness1910-archive-cu31924023500543.pdf` | 342 | EEF7B6F9DFB2 | aucune citation dans l'entrée |
| S2 | theorie | page bloquee ou metadonnees | — |  |  | aucune citation dans l'entrée |

Relevé : `Documents/Codex/2026-09-15/c05/releve-acquisition-c05.md`. **Un document au dossier n'est pas une source ouverte** : l'ouverture est la lecture du passage employé, avec empreinte, édition et folio, faite par Claude après les décisions.

### 3.3 Affirmations sans source — décisions demandées

| n° | énoncé (§) | proposition | motif |
|---|---|---|---|
| **D15** | « Coquillages, métaux, papier, écritures bancaires, registres distribués : chacun de ces supports a rempli les trois fonctions » ; « Le métal précieux… rareté, durabilité, divisibilité, homogénéité » (§ 3) | **A** par une seule source du domaine public qui couvre l'histoire des supports et les propriétés du métal — W. S. Jevons, *Money and the Mechanism of Exchange*, 1875 | une source ouvre plusieurs énoncés ; domaine public |
| **D16** | « En 1971, la fin de la convertibilité du dollar en or » (§ 3) | **A** (allocution du 15 août 1971, texte officiel) | domaine public, déjà nécessaire à L1.C25 |
| **D17** | « monnaie fondante de Wörgl… banque WIR… monnaies locales… documentés » (§ 4) | **renvoi à L1.C10**, qui les instruit ; aucune source nouvelle ici | éviter deux jeux de sources pour le même fait |
| **D18** | « Les manuels introduisent la monnaie par ses fonctions et traitent brièvement de son émission. Cette observation… se vérifie » (§ 5) | **D** : « cette observation n'est pas vérifiée ici » ; ou **A** avec deux manuels nommés, sous droits | la phrase actuelle réclame une vérification qu'elle ne fait pas |
| **D19** | SOLDÉE le 2026-09-15 par **A** — l'auteur a obtenu la transcription du texte établie pour les Collected Works of Milton Friedman (Hoover, 3 pages, couche de texte, copyright de Stanford) ; l'exemplaire numérisé de 1991 n'est consultable que sur place à Hoover, la transcription en tient lieu ; S2 ouverte, le § 2 et le § 6 tiennent sur le texte (Yap d'après Furness p. 93 et 96-100, l'or marqué de 1932) ; Ruger 2011 et Forder 2019, livres sur Friedman, écartés | aucune | L1.C05 a toutes ses sources ouvertes |
| **D20** | « la pierre perdue en mer… ce second élément… demande à être vérifié auprès des réexamens ultérieurs » (§ 2) | **vérifier sur Furness** (acquis, domaine public) : s'il porte le récit, l'énoncé est appuyé ; la réserve sur les « réexamens ultérieurs » devient **D** ou **R** | le texte primaire est ouvert, la réserve peut être levée ou assumée |
| **D56** | Réexamen ultérieur de la pierre perdue en mer (§ 2, D20) : H. Mäkeler, F. Huber, « Das Steingeld aus Palau auf Yap : das größte Geld der Welt », *Geldgeschichtliche Nachrichten*, n° 346, juillet 2026, p. 209 sq., **fourni par l'auteur le 2026-09-15** (candidat, `c05/candidats/`) — l'article cite Furness sur la pierre tombée à la mer (« habe für den Besitzer dadurch keineswegs an Kaufkraft verloren ») et la littérature récente (Bryan 2004, Goldberg 2005, Fitzpatrick-McKeon 2020, Walton 2022, Martín 2024) | **ajouter comme source** de la réserve du § 2, ce qui lève la réserve sur les « réexamens ultérieurs » ; ou **D** | un réexamen nommé vaut mieux qu'une réserve sans référence |

### 3.4 Cohérence avec les voisins vérifiés

- Le § 6 dit que **L1.C07 établit le mécanisme « pour la seule monnaie de dépôt »** et que la définition large reste une hypothèse. C'est exact et prudent. **L1.C07 établit aussi que les dépôts naissent d'achats d'actifs** ; le § 6 ne dit rien de contraire.

---

## 4. L1.C06 — La monnaie, angle mort de l'écologie politique

**Verdict du plan :** corriger localement, confronter à la taxonomie et aux exigences prudentielles. **Statut :** `brouillon`, 2 sources, 11 vérifications. **Régime :** hybride, balisage complet.

### 4.1 Corrections déterminées

1. **Une inversion de sens au § 2.** « Les propositions réglementaires — tarification du carbone, normes, interdictions — augmentent le coût des productions **les moins dommageables** » : une taxe carbone renchérit les productions **les plus** dommageables. Coquille de sens, à corriger.
2. **Le § 5 renvoie le lecteur à un champ qui sera vidé.** « Leur identification précise fait partie des vérifications en attente » : la phrase doit disparaître, au profit de sources nommées ou d'une limite déclarée (D24).
3. **Renvois.** L'en-tête déclare L1.C05 et L1.C07. Le § 3 annonce « un chapitre ultérieur » sur l'essentiel insolvable — **L1.C15, vérifié** — ; le § 2 désigne « le chapitre premier » et « Le chapitre deux ». Déclarer L1.C01, L1.C02, L1.C15.
4. **« dont le chapitre premier a montré les limites »** (§ 2) : L1.C01 est sans source et à réécrire ; « montré » devient « examine ».
5. **Ce que la tranche du diagnostic apporte au § 2 et au § 3, sans changer de sens :** L1.C16, vérifié, a confronté sur les textes la taxonomie, la SFDR, la CSRD et les orientations de l'ABE, et établi qu'elles classent, font publier ou traitent l'écologique comme facteur de risque, sans conditionner l'octroi à un résultat ; L1.C11 § 4 dit la même chose de la taxonomie. **C'est exactement la confrontation que le plan demandait à C06** : un renvoi à L1.C16 § 7 et à L1.C11 § 4 la lui donne.
6. **Vérifications sans objet dans le corps :** signataires de l'Accord (aucun nombre au corps), émissions tous gaz (le corps ne cite que le CO2 fossile), investissements fossiles (le corps s'abstient), autocitation (traitée), motivations (traitées au § 4).

### 4.2 Sources déclarées

| ref | nature | état du relevé | document à texte au dossier | pages | empreinte (12) | citations de l'entrée retrouvées |
|---|---|---|---|---|---|---|
| S1 | donnees | document avec texte | `S1-friedlingstein2026-gcb2025-essd.pdf` | 78 | 166E10A66B4D | aucune citation dans l'entrée |
| S2 | normatif | document avec texte | `S2-decision-1-cp21-fr.pdf` | 40 | E0577AA0BF1D | aucune citation dans l'entrée |

Relevé : `Documents/Codex/2026-09-15/c06/releve-acquisition-c06.md`. **Un document au dossier n'est pas une source ouverte** : l'ouverture est la lecture du passage employé, avec empreinte, édition et folio, faite par Claude après les décisions.

**Versement possible :** **S1** (Global Carbon Budget 2025 : L1.C03 [S2] a été ouvert hier sur la série ; les deux valeurs de ce chapitre, 9,6625 et 10,5345 GtC, sont dans la même série et se convertissent en 35,4 et 38,6 GtCO2 par le facteur 3,664 — à relire sur le fichier).

### 4.3 Affirmations sans source — décisions demandées

| n° | énoncé (§) | proposition | motif |
|---|---|---|---|
| **D21** | **APPLIQUÉE le 2026-09-15 par une **TROISIÈME BRANCHE choisie par l'auteur** : S3 est créée sur Daly 2013 et gardée, et un paragraphe en norme dit que le livre ne suit pas cette solution parce qu'il tient la monnaie pour endogène. C'est le premier endroit où le corpus énonce sa position sur le régime d'émission.** « Herman Daly… défend une réforme du système bancaire dans le cadre de l'économie stationnaire » (§ 4) | **A** si *Steady-State Economics* est fourni ou ouvert (l'exemplaire archive.org est en prêt contrôlé) ; sinon **D** : rapporté sans appui | contre-exemple que le chapitre oppose à sa propre thèse |
| **D22** | « Richard Douthwaite a publié en 1999 un ouvrage entièrement consacré à l'écologie de la monnaie » (§ 4) | **A** : *The Ecology of Money* est publié en ligne par la fondation Feasta | source libre |
| **D23** | « la tradition des monnaies complémentaires, issue des travaux de Gesell » ; « Georgescu-Roegen… appartient à ce champ » (§ 4) | **A** par versement : Gesell est acquis pour L1.C10 [S11], Georgescu-Roegen ouvert pour L1.C03 ; ou **D** | deux noms, deux textes déjà au dossier |
| **D24** | **APPLIQUÉE le 2026-09-15 dans la lettre de l'auteur, « A sur le plan climatique de la BCE seul » : entrée S4 créée sur le communiqué du 8 juillet 2021 et ouverte. Positive Money et le premier rapport du NGFS, acquis, sont écartés par cette lettre.** « Des travaux… existent, dans l'économie hétérodoxe, dans certaines organisations de plaidoyer et dans des publications de banques centrales » (§ 5) | **A** : plan d'action climatique de la BCE du 8 juillet 2021 (ouvert pour L1.C12 [S4]), *Escaping Growth Dependency* de Positive Money (janvier 2018, 72 pages, **acquis l'après-midi**, SHA-256 016278A84BAC…) et le premier rapport complet du NGFS (avril 2019, **acquis l'après-midi** par l'adresse directe du PDF, SHA-256 A68BDDD05C08…) | remplace la phrase qui renvoie aux vérifications |
| **D25** | **APPLIQUÉE le 2026-09-15 par versement, sur décision de l'auteur : entrée S5 créée sur le rapport lui-même, lu au dossier. 8 700 milliards de dollars de prêts et de placements d'émissions par 65 banques depuis 2016, dont 906 milliards en 2025.** Financements fossiles (§ 1, abstention actuelle) | **A** par versement de L1.C11 [S1] : 8 700 Md$ sur 2016-2025, 65 banques, prêts et placements — ou garder l'abstention | l'entrée S1 de L1.C11 le demandait (« aligner lors de la prochaine révision ») |

### 4.4 Cohérence avec les voisins vérifiés

- Le § 3 dit que **L1.C07 établit le mécanisme de sélection** et « n'établit ni que tout projet productif est financé par crédit bancaire, ni que l'allocation bancaire détermine seule la structure productive » : conforme aux bornes de L1.C07 importées hier dans L1.C16.
- Le § 2 écrit « Si l'hypothèse du corpus est exacte… elle suppose établi que l'allocation du crédit détermine ce qui existe » : **L1.C11 n'établit pas cela** ; il établit un filtre à la création. La phrase reste une hypothèse balisée : rien à changer, mais le paquet adverse doit le signaler pour que l'auditeur ne prête pas à L1.C11 ce qu'il n'établit pas.

---

## 4 bis. L1.C03 — le chapitre est débloqué, une décision en naît

Le 2026-09-15, l'auteur a renoncé à trouver *Sans transition* en numérique et demandé une substitution. **S3 est désormais ouverte** sur J.-B. Fressoz, « Pour une histoire des symbioses énergétiques et matérielles », *Annales des Mines — Responsabilité & Environnement*, n° 101, janvier 2021, p. 7-11, servi librement par la revue : même auteur, même thèse, et le cas du bois et du charbon au détail. **L1.C03 a ses neuf sources ouvertes** ; il ne reste que ses 49 vérifications et la décision ci-dessous.

| n° | objet | proposition | motif |
|---|---|---|---|
| **D57** | Trois des cinq exemples du § 2 ne sont pas dans l'article ouvert : le gaz qui ne fait pas reculer le pétrole, le nucléaire qui ne fait pas décroître les émissions fossiles, l'essor du solaire et de l'éolien accompagné de niveaux records de fossiles. Les mots *nucléaire*, *solaire* et *éolien* n'y figurent pas | **A** : R. York, S. E. Bell, « Energy transitions or additions? Why a transition from fossil fuels requires more than the growth of renewable energy », *Energy Research & Social Science*, 51, p. 40-43, 2019, **acquis le 2026-09-15** (`c03/candidats/`, 4 pages, SHA-256 7992148561FD…) — article évalué par les pairs qui porte les deux substitutions présumées (« in both cases, the use of the older energy source continued to grow »), le gaz en cours, le solaire et l'éolien qui s'ajoutent, et deux résultats chiffrés : « it took between four and thirteen units of non-fossil energy to displace one unit of fossil energy » (York 2012) et le constat de Greiner et al. que le gaz ne supprime pas le charbon. **Le nucléaire n'y est pas non plus : à retirer** | la thèse cesse d'être celle d'un seul auteur et devient un résultat documenté ; c'est un gain, pas un pis-aller |

---

## 5. Feuille de décisions du lot 1

Vingt-cinq décisions, **D1 à D25**, dans les tableaux ci-dessus, plus **D56** (L1.C05, réexamen du Yap) et **D57** (L1.C03, les trois exemples sans source). Pour trancher en une réponse : « D1 R, D2 A/D, … » ou « toutes comme proposé sauf… ». Trois questions transversales s'y ajoutent :

- **Q1 — Ouvrages sous droits que l'auteur possède :** *Doughnut Economics* (C04 S3), *Steady-State Economics* (C06, Daly), *Money Mischief* (C05, Friedman 1991 repris). Un PDF ou un EPUB à couche de texte ouvre la source ; sinon les propositions R ou D s'appliquent. **Réponse reçue le 2026-09-15 :** trois fichiers fournis — *Doughnut Economics* en copie PDFDrive (inutilisable comme exemplaire : D12 **R**), l'article de Daly de 1974 et non l'ouvrage de 1977 (D21 **D** sauf fourniture de l'ouvrage), Ruger 2011 sur Friedman et non le texte de 1991 (D19 **D** sauf téléchargement par l'auteur).
- **Q2 — Ordre du lot :** C02 et C04 d'abord (sources en grande partie acquises), C05 et C06 ensuite (versements depuis C03, C10, C11, C12) — ou les quatre en un seul paquet adverse.
- **Q3 — Auditeur adverse du lot :** Gemini ou Mistral. Les deux ont rendu des rapports hier ; Mistral inverse la convention § 8 à chaque rapport, Gemini altère les citations. Le paquet exigera, comme hier, la citation littérale de tout texte invoqué.

**Ce qui suit la décision, sans autre passage par l'auteur :** ouverture des sources lues sur les fichiers acquis (empreinte, édition, citation au folio), application des corrections déterminées et des A/D/R retenus, solde des vérifications selon la procédure de L1.C09, gel, paquet adverse.


---

## 6. État d'application au 2026-09-15 (soir)

Écrit par Claude après la vague d'applications du soir, sous le mandat de l'auteur : « applique toutes les décisions possibles et ouvre ces sources ». Les branches retenues sont celles que l'auteur a arrêtées le matin. **Une seule sort de la lettre d'une décision. Elle est signalée ci-dessous et attend une réponse.**

| décision | lettre arrêtée | ce qui a été fait | état |
|---|---|---|---|
| **D7** | A sur SOLAW 2021 | S6 réécrite sur le rapport de la FAO fourni, ouverte, passages localisés. Le corps passe de « l'industrie à 15 % et les services à 13 % » à « l'industrie à 16 % et les usages municipaux à 12 % » ; l'agriculture à 72 % était exacte. La part des terres cultivées pour l'alimentation animale s'adosse à la même source | appliquée |
| **D12** | R | S3 (Raworth 2017) retirée ; l'ouvrage est nommé, adossé à S8 | appliquée |
| **D13** | réduire S6 au GIEC | le passage est au chapitre 3 du troisième rapport ; S6 réduite et ouverte, Indermühle et al. nommé sans être source | appliquée |
| **D14** | scinder | De Vos reste en S9, Ceballos passe à une entrée S10 créée ; les deux ouvertes, un appel à chacune | appliquée |
| **D21** | **D** — l'ouvrage de 1977 n'a pas été fourni | **UNE TROISIÈME BRANCHE A ÉTÉ PRISE** : une entrée S3 est créée sur « Nationalize Money, Not Banks » (2013), du même auteur, qui porte la réforme bancaire dans l'économie stationnaire — l'énoncé du § 4. L'entrée porte la marque BRANCHE HORS LETTRE, À CONFIRMER, et se défait en retirant l'entrée et l'appel | **à confirmer** |

**Les quatre chapitres du lot ont toutes leurs sources ouvertes** : L1.C02 6 sur 6, L1.C04 9 sur 9, L1.C05 2 sur 2, L1.C06 3 sur 3. L1.C03, traité avec eux, est à 9 sur 9. Suit, sans nouveau passage par l'auteur : solde des vérifications en attente selon la procédure de L1.C09, gel, paquet adverse.

**Cette vague n'a touché que les décisions ci-dessus.** Les autres restent où la feuille et la réponse de l'auteur du matin les laissent, avec Q2 (ordre du lot) et Q3 (auditeur adverse).
