# Architecture de reprise de L1.C09 — « L'architecture invisible »

**Établie le 2026-09-14 par Claude, sous l'alternance arrêtée par l'auteur : je
rédige C09, Codex l'auditera.** Lecture seule à ce stade. Le chapitre n'est pas
modifié, rien n'est commité.

**État figé de la lecture.** Chapitre `audit_contradictoire`,
`revision_de_fond` 2026-09-07, régime `hybride`, 219 lignes, 19 sources toutes
`a_requalifier`, 17 entrées en `verifications_en_attente`, 4 renvois déclarés,
30 chapitres entrants.

## 1. Ce que le chapitre fait, et ce qu'il ne prétend pas faire

Le chapitre nomme quatre règles implicites du régime monétaire et soutient
qu'elles forment une grammaire apprise sans conscience de l'apprendre. **Sa
thèse est interprétative et il le déclare deux fois**, en ouverture et en
portée. Chaque règle est confrontée à l'objection que la théorie économique lui
oppose : les finances publiques pour la première, les cadres de mesure existants
pour la deuxième, le fondement théorique de l'actualisation pour la troisième,
la comptabilité nationale pour la quatrième.

**C'est la qualité principale du chapitre, et la réécriture doit la préserver.**
Il ne dit pas que ces réalités sont innommables ; il dit qu'elles sont nommées
ailleurs que dans les comptes qui décident. Il ne dit pas que l'actualisation
est une erreur ; il dit que les paramètres retenus compriment le long terme. Il
ne dit pas que la monnaie est la cause unique de l'invisibilité ; il admet la
cause complémentaire des droits de propriété.

La quatrième règle porte la charge de toute la seconde partie du livre : une
grammaire écrite peut être réécrite.

## 2. Les sources

### 2.1 Quatre sources sont déjà lues, et leur état ne le dit pas

Le bloc commenté de l'en-tête porte des extraits verbatim datés du 2026-09-03.
Ces lectures ont eu lieu ; seul l'état n'a pas suivi.

| Réf. | Ce que le bloc atteste | Action |
|---|---|---|
| S2, Carney 2015 | PDF lu, citation de l'horizon reproduite, et le passage où il **écarte** l'ajustement des règles prudentielles | passer à `ouverte`, mention et date |
| S18, OCDE 2011 | PDF lu sur miroir, citation verbatim sur 19 % en Corée à 53 % au Portugal | passer à `ouverte` |
| S19, Insee 2012 | PDF lu, 42 à 77 milliards d'heures, trois périmètres, 64 % par les femmes | passer à `ouverte` |
| S8, BoE 2014 | ouvert pour L1.C07, où il est S1, `ouverte` et daté | passer à `ouverte` par report |

**Quinze sources restent donc à ouvrir, non dix-neuf.** C'est le premier gain de
cette passe, et il ne coûte rien d'autre que la mise à jour de l'état.

### 2.2 Trois entrées mêlent plusieurs signatures

C'est le contrôle 2 d'AGENTS.md, qui interdit d'attribuer à un auteur ce qu'un
autre a écrit et qui doit être passé sur l'ensemble du dépôt avant tout commit.

| Réf. | Signatures réunies | Action |
|---|---|---|
| S11 | Samuelson 1954 et Musgrave 1959 | scinder ; la théorie des biens publics invoquée au § 2 doit être attribuée au texte qui la porte |
| S13 | Ostrom 1990 et Coase 1960 | scinder ; deux thèses distinctes sur les communs et sur les coûts de transaction |
| S14 | Monnet 2021 et Couppey-Soubeyran, Delandre, Sersiron 2024 | scinder ; deux ouvrages distincts, cités pour un même renvoi général |

### 2.3 Ce que les quinze restantes doivent servir

Plusieurs ne portent qu'un renvoi de courtoisie et pourraient sortir si
l'affirmation qu'elles soutiennent est réduite. À décider à la réécriture, avant
toute acquisition : **le premier gain documentaire vient de la réécriture, pas
de l'ouverture indistincte de quinze références.**

- **S1 Whorf et S17 Boroditsky** portent l'analogie de la langue, employée comme
  instrument d'exposition et non comme preuve. Le chapitre le déclare. Ouvrir
  les deux si l'analogie est conservée, et signaler que la réplication de
  Boroditsky 2001 est discutée dans la littérature.
- **S3 Stern, S4 Nordhaus, S12 Ramsey, S16 Quinet** portent les chiffres de
  l'actualisation. Ce sont les seuls chiffres du chapitre, et ils décident du
  § 4. À ouvrir en priorité.
- **S5 SEEA, S6 Dasgupta, S9 SCN 2008, S10 CSRD** portent les cadres de mesure
  existants, c'est-à-dire l'objection que le chapitre s'adresse à lui-même. Les
  affaiblir affaiblirait l'honnêteté du § 3.
- **S7 Tronto** porte le *care*, cité une fois.
- **S15 Webley** porte la socialisation économique de l'enfant, qui soutient
  « s'apprend sans conscience de l'apprendre ». C'est l'appui du § 1.

### 2.4 Deux vérifications documentaires datées

- **S18** : les moyennes « 15 % au coût de remplacement, 27 % au coût
  d'opportunité » avancées par une recherche approfondie **ne figurent pas**
  dans le document de travail n° 116. Les localiser ou ne pas les employer. Le
  bloc le dit déjà ; la réécriture ne doit pas les réintroduire.
- **S10 CSRD** : le paquet dit « Omnibus » proposé en février 2025 a réduit le
  champ et différé les obligations. Le chapitre écrit « obligations de
  publication » et non « obligations comptables », ce qui reste vrai quel que
  soit le périmètre. **Vérifier l'état du droit au jour de la vérification** et
  non à la date d'écriture.

## 3. Écarts relevés

### 3.1 Le chapitre compte quatre règles, son propre corps en annonce six

Le balayage du Livre 6, annexé au corps, écrit : « **Deux règles jamais
énoncées, et ce chapitre n'en comptait que quatre.** » Le § 6 en énumère
quatre. **La contradiction est dans le fichier**, et un lecteur qui extrait
l'annexe lit l'inverse de ce que la portée affirme.

Trois voies, et le choix appartient à l'auteur. Intégrer les deux règles et
passer à six. Les déclarer comme extensions relevées et non instruites. Ou les
sortir du chapitre vers passe-2.

### 3.2 Deux sections de travail sont annexées au corps

« BALAYAGE DU LIVRE 6 » et « BALAYAGE DU LIVRE 18 », toutes deux datées du
2026-09-07, figurent après la portée, en style de passe de septembre, gras et
capitales. Un lecteur et un auditeur les lisent comme du texte. **Même
traitement que pour L1.C07** : sortir du corps, verser la substance là où elle
doit vivre, et garder la trace dans l'architecture.

### 3.3 Le balayage du Livre 18 durcit la thèse et le chapitre ne l'a pas intégré

Il rapporte qu'en octobre 2008 l'IPSASB a décidé de **ne pas** faire une norme
de la soutenabilité de long terme, après consultation, une large majorité de
répondants convenant que les états financiers ne peuvent pas porter cette
information et beaucoup préférant des orientations plutôt que des exigences.

**La conséquence est écrite dans l'annexe et n'est pas traitée** : sur ce point,
l'architecture n'est pas invisible par inadvertance, elle a été arrêtée là
délibérément. Et l'annexe conclut elle-même qu'« une objection contre une
incapacité se traite par une méthode ; une objection contre un choix se traite
par un argument — et le corpus n'en a pas encore produit ».

**C'est la lacune la plus sérieuse du chapitre.** Elle doit être portée dans la
portée, comme limite déclarée, et non rester dans une annexe.

**Contrainte d'acquisition à respecter.** Les cinq documents IPSASB et IFAC ne
doivent pas être ouverts. C09 s'appuie donc sur L18.C01 et L18.C03, qui sont
`brouillon`. **Aucun résultat de chapitre `brouillon` ne peut être présenté
comme un acquis** : le fait de 2008 doit être rapporté comme ce que L18.C03
relève, non comme un établi du corpus.

### 3.4 Le chapitre porte une définition de l'essentiel insolvable devenue périmée

Le § 3 écrit : « ce que le corpus nomme l'essentiel insolvable — les activités
nécessaires à la vie dont la valeur ne peut pas être couverte de façon fiable
par une recette marchande ».

C'était la définition du vocabulaire jusqu'au 2026-09-13. Elle a été remplacée
par la disjonction des quatre conditions. **L'ancienne formulation correspond au
seul ¬M** ; la nouvelle est plus large. Le chapitre énonce donc aujourd'hui une
définition plus étroite que celle qui fait foi.

**Et ma table de propagation du 2026-09-13 ne l'a pas vu**, parce qu'elle
cherchait les chapitres citant `L1.C15` et que C09 paraphrase la définition sans
la citer. Relevé fait ce jour, quatre chapitres sont dans ce cas :

| Chapitre | Statut | Formulation portée |
|---|---|---|
| L1.C09 | audit_contradictoire | « les activités nécessaires à la vie dont la valeur ne peut pas être couverte de façon fiable par une recette marchande » |
| L6.C10 | brouillon | « sa valeur sociale ne peut pas être couverte de façon fiable par une recette marchande » |
| L18.C21 | brouillon | « désigne précisément ce qui ne peut pas être couvert de façon fiable par une recette marchande » |
| L18.C23 | brouillon | « indispensable au maintien des conditions de vie, et sans recette marchande » |

L1.C01 et L1.C10 emploient « recette marchande » sans en faire une définition ;
à examiner, priorité moindre.

**Conséquence de méthode, qui vaut au-delà de ce chapitre.** Une propagation ne
se détecte pas seulement par l'identifiant cité. Une définition paraphrasée sans
citation échappe au filtre. Le critère doit désormais porter aussi sur la
formulation elle-même.

### 3.5 Les renvois sont incomplets

Déclarés : L1.C01, L1.C05, L1.C07, L1.C08. Le corps cite en outre L1.C02,
L6.C12, L18.C01 et L18.C03. Et trois notes demandent d'ajouter L1.C10, L1.C15
et L1.C17 « quand ils existeront » : **les trois existent**, et L1.C15 est
`verifie` depuis le 2026-09-13.

### 3.6 Une affirmation sans appui, signalée par le bloc lui-même

« des acteurs couramment évalués à des échéances plus courtes encore », au § 4.
Le bloc demande de la sourcer sur des données de durée de détention ou de
fréquence de reporting, ou de la laisser en limite. **Elle n'est ni sourcée ni
déclarée comme limite.**

## 4. Matrice affirmation-preuve

Régime : `E` pour `::etat::`, `H` pour `::hypothese::`, `N` pour `::norme::`.

| § | Affirmation | Régime actuel | Appui | Décision proposée |
|---|---|---|---|---|
| 1 | La monnaie fonctionne comme une langue | H | analogie déclarée, S1 et S17 | conserver, avec la réserve de réplication sur S17 |
| 1 | L'enfant acquiert entre trois et douze ans des règles implicites sur l'argent | H | S15 | ouvrir S15 ; c'est l'appui de « sans conscience de l'apprendre » |
| 1 | La grammaire rend finançable, elle ne rend pas impensable | H | inférence | conserver ; c'est la restriction qui sauve la thèse |
| 2 | L'essentiel de la monnaie est créé par les banques à l'occasion du crédit | non marqué | S8, et L1.C07 `verifie` | **E**, en s'appuyant sur L1.C07 plutôt que sur S8 seul |
| 2 | Le critère d'octroi est la solvabilité anticipée | non marqué | L1.C07 § 7, vocabulaire | **E** |
| 2 | Le canal budgétaire est en aval, à deux titres | H | S11, L1.C08 § 4, L1.C01 § 3 | conserver ; scinder S11 |
| 2 | La décision d'émettre n'est l'objet d'aucun mandat démocratique explicite pour cette fonction | H | S14 | conserver, scinder S14, et vérifier que la formule n'excède pas ce que les deux ouvrages soutiennent |
| 3 | Les cadres de mesure existent, et il serait faux de dire ces réalités innommables | non marqué | S5, S6, S7, S10, S18, S19 | **E** ; c'est l'objection que le chapitre s'adresse, elle doit être en régime descriptif |
| 3 | Entre un tiers et la moitié de l'activité valorisable échappe aux comptes nationaux | non marqué | S18, lu | **E**, avec la citation verbatim déjà relevée |
| 3 | Aucun de ces cadres n'entre au compte de résultat ni ne modifie la décision de crédit | H | inférence | **conserver en H** ; c'est le cœur de la deuxième règle et ce n'est pas mesuré |
| 3 | Définition de l'essentiel insolvable | non marqué | vocabulaire périmé | **corriger**, voir § 3.4 |
| 4 | À 5 % l'an, une valeur à cent ans vaut moins de 1 % | E | arithmétique | conserver |
| 4 | Stern 1,4 %, Nordhaus 5,5 %, Quinet 2,5 puis 1,5 %, et 4,5 % avec risque | E | S3, S4, S16 | **ouvrir les trois avant de conserver les chiffres** |
| 4 | Les acteurs sont couramment évalués à des échéances plus courtes | H | aucun | **sourcer ou déclarer comme limite**, voir § 3.6 |
| 4 | Carney nomme la tragédie des horizons, et écarte l'ajustement prudentiel | non marqué | S2, lu | **E** ; la seconde moitié est la correction d'un audit antérieur et doit rester visible |
| 4 | Les remèdes de Carney sont nécessaires et insuffisants | H | thèse du corpus, déclarée telle | conserver, la déclaration est déjà faite |
| 5 | La production non marchande est comptée à son coût | non marqué | S9 | **E** |
| 5 | Quatre verbes n'ont pas de place dans la grammaire du crédit | H | inférence | conserver ; la distinction entre ce que la comptabilité nationale enregistre et ce que le crédit ignore est bien tenue |
| 6 | Quatre règles | non marqué | le corps en annonce six | **trancher**, voir § 3.1 |
| 6 | Une grammaire écrite peut être réécrite | H | inférence | conserver ; c'est la charge de la seconde partie |

## 5. Structure proposée

La structure actuelle est bonne et je ne propose pas de la refondre. Les
modifications sont locales.

1. **Ouverture** inchangée. La double déclaration du caractère interprétatif est
   un atout.
2. **§ 1, la grammaire.** Conserver, avec la réserve sur S17.
3. **§ 2, qui écrit la grammaire.** S'appuyer sur L1.C07 `verifie` plutôt que
   sur S8 seul. Scinder S11 et S14.
4. **§ 3, le lexique.** Corriger la définition de l'essentiel insolvable et
   renvoyer à L1.C15, désormais `verifie`.
5. **§ 4, le temps.** Ouvrir les quatre sources d'actualisation avant de
   conserver leurs chiffres. Sourcer ou déclarer la limite sur l'horizon des
   gestionnaires.
6. **§ 5, les verbes.** Conserver.
7. **§ 6, portée.** Trancher le compte des règles. **Ajouter la limite du § 3.3**
   : sur la soutenabilité de long terme, le corpus fait face à un choix
   délibéré et non à une incapacité, et il n'a pas encore produit l'argument que
   cela réclame.
8. **Les deux balayages sortent du corps.**

## 6. Décisions demandées à l'auteur

1. **Quatre règles ou six ?** Intégrer les deux règles du balayage du Livre 6,
   les déclarer comme extensions non instruites, ou les verser à passe-2.
2. **Le sort des deux balayages** : où va leur substance.
3. **La limite sur le choix délibéré de 2008** : la porter dans la portée, ou
   ouvrir une pièce de conception pour l'argument qui manque.
4. **L'analogie de la langue** : conservée avec ses deux sources, ou réduite à
   un procédé d'exposition sans appui documentaire.
5. **La propagation de la définition périmée** : traiter les quatre chapitres
   maintenant, ou après la réécriture de C09.

## 7. Séquence

1. Validation de l'auteur sur les cinq décisions.
2. Passage à `ouverte` des quatre sources déjà lues, avec mentions et dates.
3. Scission de S11, S13 et S14.
4. Réécriture selon le § 5, sans ouvrir de source nouvelle.
5. Ouverture des sources restantes, une par une, pour leur seul passage utile,
   en commençant par les quatre de l'actualisation.
6. Relais à Codex pour l'audit adverse, selon l'alternance arrêtée.
7. Audit tiers indépendant, puis audit factuel.

Le chapitre demeure `audit_contradictoire` et `citable: false` jusque-là.
