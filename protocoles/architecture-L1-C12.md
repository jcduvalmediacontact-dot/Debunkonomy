# Architecture de reprise de L1.C12 — « La deuxième malédiction monétaire »

**Écrite le 2026-09-14. Aucune modification n'est appliquée au chapitre.**
Document soumis à l'auteur : il demande quatre décisions, et propose une
séquence pour les exécuter.

**État de départ, relevé et non supposé** : `audit_contradictoire`,
`revision_de_fond` du 2026-09-03, `citable: false`, 2 185 mots, **douze sources
toutes `a_requalifier`, aucune ouverte**, seize vérifications en attente, sept
concepts tous présents au vocabulaire.

---

## 1. Ce que le chapitre fait, et il le fait bien

**Ce chapitre n'est pas dans l'état où était L1.C09.** Il a déjà traversé un
audit contradictoire — Gemini, le 2026-09-03 — et les corrections ont été
appliquées. Trois affirmations fausses du texte source ont été retirées et les
vérifications en gardent la trace :

1. l'empreinte matérielle européenne « continue de grimper » — **Eurostat dit
   l'inverse**, et le chapitre le dit maintenant ;
2. l'argument quantitatif tiré de `MV = PT` — **abandonné**, les séries
   monétaires le réfutent ;
3. la « masse monétaire mondiale d'environ 130 000 milliards » — **retirée**,
   aucun agrégat officiel de ce type n'existe.

**C'est un chapitre qui a déjà renoncé à ses arguments faciles.** La thèse qui
reste est plus étroite, et le § 3 la déclare falsifiable. Ce qui suit ne remet
pas cela en cause : **le problème de L1.C12 est documentaire, pas
argumentatif.**

**Ce qu'il établit.** Verdir le crédit produit des découplages réels — sectoriels
et nationaux, importations comprises — et ne produit pas de découplage mondial
absolu, pour trois raisons : le service d'un encours croissant exige une
expansion nette indifférente à la couleur du crédit ; les capacités nouvelles
s'ajoutent tant que les anciennes restent solvables, leur retrait étant ce que
la stabilité financière protège ; et la stabilité des prix ferme la voie de
l'érosion par l'inflation.

**Ce qu'il ne prétend pas.** Il ne conteste ni les effets de la finance verte ni
la possibilité d'un découplage local. Il ne prétend pas que les flux
d'investissement démontrent l'additivité — le § 3 le dit expressément.

---

## 2. Les sources — l'état déclaré ne dit pas l'état réel

### 2.1 Trois sources ont été lues, et leur état ne le dit pas

**C'est exactement le défaut relevé sur L1.C09, et il se répète ici.** Les
vérifications en tête de chapitre portent, sous le titre « Sources ouvertes le
2026-09-03 (Claude) », des relevés de valeurs précis qui ne peuvent provenir que
d'une lecture directe :

| source | ce que la vérification enregistre | lecture réelle |
|---|---|---|
| **S1** Eurostat | sept valeurs RMC/hab UE-27 et six pour l'Allemagne | **API lue** |
| **S3** FRED | M2V et M2SL, valeurs, maxima, minima, dates | **CSV lus** |
| **S10** OWID | six valeurs de CO2 allemand par la consommation | **CSV lu** |

**Ces trois entrées devraient être `ouverte` avec leur date.** Elles portent
`a_requalifier`. Le chapitre s'interdit ainsi `verifie` pour une raison qui n'est
pas la bonne.

**Distinction à ne pas manquer, et elle vaut décision.** Les vérifications disent
aussi « S2, S4, S5 : recoupés sur pages institutionnelles » et, pour S9,
« existence et valeurs confirmées par recoupement ». **Un recoupement n'est pas
une ouverture.** Ces quatre-là restent fermées, et leur passage à `ouverte`
demande une lecture du texte.

### 2.2 Une entrée réunit deux signatures — contrôle 2 d'AGENTS.md

**S11 porte le NGFS 2019 *et* le discours de Carney de 2015.** C'est la même
double signature que la scission du 2026-09-14 a séparée dans L1.C09. L'appel du
§ 3 — « au sens du risque de transition que les superviseurs ont identifié
[S11] » — ne dit pas laquelle des deux signatures porte la qualification.

**La scission est obligatoire, et elle est immédiatement rentable** : le discours
de Carney **est déjà ouvert**, en L1.C09 [S2], le 2026-09-14, texte intégral lu.
La moitié Carney est versable le jour même ; seul le NGFS 2019 reste à acquérir.

### 2.3 Deux versements sont disponibles — et leur portée est limitée

**S2, le Global Resources Outlook 2024, est ouvert en L1.C08 [S14] depuis le
2026-09-11**, avec trois passages vérifiés : p. xiv, p. 4 et p. 24. Le passage de
la p. 4 porte précisément ce dont le § 3 de C12 a besoin :

> *« between 2015 (reference year of the 2019 edition) and 2023 there was no
> absolute decoupling of any environmental impact on the global scale »*

**Mais le versement ne couvre pas tout.** Les chiffres d'extraction que C12
emploie — 30 Gt en 1970, 106,6 Gt en 2024, 8,4 puis 13,2 t/hab — sont sur une
**autre page**, non ouverte par L1.C08. Comme pour Ostrom en C09, `ouverte`
signifie que le **passage pertinent** a été lu. Il faut donc ouvrir cette page-là.

**Et elle a été localisée.** Le texte intégral extrait lors de l'audit de L1.C08
est conservé sous `Documents/Codex/2026-09-10/audit-C08/GRO-2024.txt`. Il porte
la phrase mot pour mot :

> *« Global material extraction surged from 30 billion tonnes in 1970 to 106.6
> billion tonnes in 2024, an average annual growth of 2.3%. Consequently, the
> global average per capita demand for materials rose from 8.4 tonnes in 1970 to
> 13.2 tonnes in 2024. »*

**Folio relevé, non supposé** : page PDF 36, folio imprimé **18** — l'écart
imprimé = PDF − 18 est constant sur 155 pages, et la page 36 porte elle-même le
nombre 18.

### 2.4 Ce que les douze demandent réellement

| source | voie | état |
|---|---|---|
| S1 Eurostat RMC | API publique | **lue le 2026-09-03**, à requalifier |
| S3 FRED M2 | CSV public | **lus le 2026-09-03**, à requalifier |
| S10 OWID CO2 | CSV public | **lu le 2026-09-03**, à requalifier |
| S2 PNUE GRO 2024 | versement L1.C08 + une page à ouvrir | texte sur disque, folio établi |
| S11b Carney 2015 | **versement L1.C09 [S2]** | immédiat |
| S11a NGFS 2019 | PDF public | à acquérir |
| S4 BCE | communiqués publics | à ouvrir |
| S5 Umweltbundesamt | page publique | à ouvrir |
| S6 AIE WEI 2025 | rapport AIE | à acquérir |
| S9 PNUE EGR 2025 | PDF public | à acquérir |
| S7 Fisher 1911 | **domaine public** | à acquérir, sans obstacle |
| **S8 Fressoz 2024** | Seuil, sous droits | **bloqué** |
| **S12 Aghion 2020** | Odile Jacob, sous droits | **bloqué** |

**Dix des douze sont atteignables par une voie propre.** C'est un rapport tout
autre que celui de L1.C09, où six ouvrages sous droits bloquaient le chapitre.

---

## 3. Écarts relevés

### 3.1 Un chiffre de 2024 publié en mars 2024 est une projection

Le § 1 écrit : *« L'extraction mondiale de matières est passée de 30 milliards de
tonnes en 1970 à 106,6 milliards en 2024. »* **C'est le chiffre du rapport, et le
rapport a paru le 1er mars 2024.** La valeur pour 2024 ne peut donc pas être un
constat : c'est une estimation du Panel international des ressources pour
l'année en cours.

**Le chapitre l'énonce comme un fait observé.** La correction est mince — nommer
l'estimation — et elle protège contre une objection facile. La même prudence vaut
pour l'investissement « 2 200 milliards de dollars en 2025 » tiré d'un rapport du
5 juin 2025 [S6].

### 3.2 La pagination avancée pour S2 est fausse

La vérification en attente dit : *« chapitre 2, p. 20-22 selon Deep Research ;
ouvrir le rapport. »* **Le relevé mécanique donne le folio 18**, et une seconde
occurrence au folio 26. Ni l'une ni l'autre n'est entre 20 et 22.

**Ce n'est pas une coquille, c'est la règle qui se vérifie** : un rapport tiers
est une piste, jamais une vérification. La vérification doit être soldée par le
folio réel.

### 3.3 Une vérification affirme une ouverture que l'état contredit

La vérification « Sources non ouvertes par un humain » dit : *« S6 : ouvert pour
L1.C11. »* **Le relevé sur le corpus dit le contraire** : L1.C11 [S5], qui porte
le même rapport de l'Agence internationale de l'énergie, est `a_requalifier`.
**S6 n'est ouverte nulle part.** La vérification doit être corrigée avant de
servir d'appui à quoi que ce soit.

### 3.4 Deux occurrences de « 2,3 % » qui ne désignent pas la même chose

Le § 1 porte deux fois ce nombre :

- **croissance annuelle moyenne de l'extraction de matières**, 2,3 % — vérifié
  sur le texte du GRO ;
- **hausse des émissions mondiales en 2024**, 2,3 % — attribué au rapport du PNUE
  sur l'écart des émissions [S9], **non vérifié**.

La coïncidence peut être réelle. Elle peut aussi être une contamination d'un
chiffre par l'autre. **À trancher sur le texte de S9, pas par raisonnement.**

### 3.5 Deux affirmations sans appui

- *« Cette intuition est mise en œuvre depuis deux décennies »* — aucune source.
  L'appel [S4] qui suit ne couvre que la Banque centrale européenne à partir de
  2021.
- *« le double de l'investissement fossile, alors que le rapport était inverse
  dix ans plus tôt »* [S6] — la comparaison à dix ans doit être trouvée dans le
  rapport ou retirée.

### 3.6 Les renvois sont incomplets

**Déclarés** : L1.C03, L1.C08, L1.C11. **Cités dans le corps** : les trois, plus
**L1.C09 et L1.C10**, au § 5. Les deux manquants sont à ajouter.

### 3.7 S8 Fressoz porte une charge réelle — ce n'est pas un renvoi de courtoisie

**Le point demande d'être dit franchement, parce qu'il diffère de L1.C09.** Là,
les cinq ouvrages fermés ne portaient qu'un renvoi de courtoisie et la réduction
ne coûtait rien. Ici, Fressoz porte l'appui empirique d'une des deux hypothèses
du § 3 :

> *« Fressoz a montré, pour l'énergie, que les sources se sont historiquement
> empilées au lieu de se remplacer [S8] (L1.C03). »*

**Retirer cette source affaiblirait l'hypothèse, pas seulement l'apparat.** Une
issue existe et n'est pas une substitution : **L1.C03 porte le même ouvrage**
[S3], et C12 renvoie déjà à ce chapitre. Si L1.C03 ouvre Fressoz, C12 peut
s'appuyer sur le chapitre au lieu de citer l'ouvrage. C'est une décision de
l'auteur, pas de l'agent.

---

## 4. Matrice affirmation-source

| § | affirmation | source | régime | état de l'appui |
|---|---|---|---|---|
| 1 | La BCE oriente ses réinvestissements selon des scores climatiques depuis le 1er oct. 2022 | S4 | — | recoupé, **non ouvert** |
| 1 | 2 200 Md$ dans les technologies propres en 2025, double du fossile | S6 | — | **non ouvert**, et estimation |
| 1 | Renouvelables allemands : 6,3 % (2000) → 51,8 % (2023) | S5 | — | recoupé, **non ouvert** |
| 1 | CO2 allemand par la consommation : 1 037 (2008) → 768 Mt (2023) | S10 | — | **lu le 2026-09-03** |
| 1 | RMC/hab UE-27 : 16,1 (2000) → 13,7 t (2023) | S1 | — | **lu le 2026-09-03** |
| 1 | Extraction mondiale : 30 → 106,6 Gt ; 8,4 → 13,2 t/hab | S2 | — | **texte et folio 18 établis** |
| 1 | Émissions mondiales 57,7 GtCO2e en 2024, +2,3 % | S9 | — | **non ouvert** — voir § 3.4 |
| 2 | `MV = PT` est une identité comptable, non une causalité | S7 | `::etat::` | **non ouvert**, domaine public |
| 2 | M2 ×2,97 (2008-2025), vitesse −30 % | S3 | `::etat::` | **lus le 2026-09-03** |
| 3 | L'exigence porte sur le volume, non la couleur | L1.C08 § 1 et § 2 | `::etat::` | renvoi, chapitre `verifie` |
| 3 | Les sources d'énergie se sont empilées au lieu de se remplacer | S8 | `::hypothese::` | **bloqué, sous droits** |
| 3 | Le retrait anticipé des capacités est ce que la stabilité financière évite | S11 | `::hypothese::` | **double signature**, Carney versable |
| 3 | Le découplage absolu n'est pas observé globalement | S2, L1.C03 | `::hypothese::` | **versable depuis L1.C08, p. 4** |
| 3 | Objection de la dématérialisation | S12 | — | **bloqué**, renvoi de courtoisie |
| 4 | Le cas allemand : découplage sectoriel sans baisse de l'empreinte matérielle | S1, S5, S10 | `::hypothese::` | deux sur trois lues |
| 5 | Quatre verrous | L1.C08, L1.C11, S3 | `::hypothese::` | renvois + S3 lue |

---

## 5. Séquence proposée

1. **Requalifier S1, S3 et S10** en `ouverte` avec la date du 2026-09-03, sur la
   foi des relevés que les vérifications portent déjà. Aucune acquisition.
2. **Scinder S11** et verser la moitié Carney depuis L1.C09 [S2]. Acquérir le
   NGFS 2019 séparément.
3. **Ouvrir S2** sur son folio 18 et verser le passage de la p. 4 depuis L1.C08.
4. **Acquérir et ouvrir** S4, S5, S9, S6 et S7 — toutes accessibles, S7 étant du
   domaine public.
5. **Solder les trois vérifications fausses ou périmées** : la pagination de S2,
   l'ouverture supposée de S6, et le doublon de 2,3 %.
6. **Corriger les renvois** : ajouter L1.C09 et L1.C10.
7. **Traiter S8 et S12** selon la décision de l'auteur.
8. Geler par empreinte et passer la main pour la passe adverse.

## 6. Décisions demandées à l'auteur

1. **S8 Fressoz** — acquérir l'ouvrage, faire porter l'appui par L1.C03 via le
   renvoi, ou réduire l'hypothèse ? **C'est la seule décision qui engage
   l'argument.**
2. **S12 Aghion** — réduire comme les cinq de L1.C09, ou conserver ?
3. **Les chiffres de l'année en cours** — nommer l'estimation pour 106,6 Gt en
   2024 et 2 200 Md$ en 2025, ou les laisser tels quels ?
4. **La requalification de S1, S3 et S10** sur la foi des relevés du 2026-09-03,
   sans relire les séries : acceptée, ou faut-il relire ?
