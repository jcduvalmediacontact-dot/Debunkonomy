# Refonte du Livre 1 — cartographie contradictoire

**État : cartographie, 2026-09-10. Aucun chapitre n'est réécrit, aucune entrée
du Livre 0 n'est écrite, ni la convention ni le `llms.txt` ne sont modifiés.**

---

## 0. Vérifications préalables

### 0.1 Un fait de structure qui commande tout le reste

**Les 31 chapitres du Livre 1 dans le corpus ne sont pas le texte du livre publié
en 2026. Ce sont les fiches d'examen contradictoire de ce livre, chapitre par
chapitre, dans son ordre.** Les résumés le disent en toutes lettres : *« Ce
chapitre examine le diagnostic que le livre porte et il en réduit la portée »*
(L1.C24), *« Il établit ensuite trois résultats défavorables. Le premier est
bloquant »* (L1.C26), *« la conclusion du chapitre, qui est dirigée contre son
propre titre »* (L1.C24).

**Conséquence pour la commande.** La « deuxième édition du Livre 1 » est un
**texte à écrire**, et le corpus n'en contient pas le brouillon : il contient
l'inventaire de ce que la première édition doit changer. La matrice ci-dessous
n'est donc pas une liste de retouches sur un texte existant dans le dépôt —
c'est la **liste des verdicts déjà rendus** sur le texte de 2026, qui sont la
matière de la seconde édition.

### 0.2 Les trois nombres — vérifiés

| annoncé | mesuré | verdict |
|---|---|---|
| 326 brouillons | **326** | exact |
| 9 en audit contradictoire | **9** | exact |
| aucun chapitre vérifié | **0** | exact |
| | **335 au total** | |

**Et les neuf chapitres en audit contradictoire sont TOUS dans le Livre 1** :
L1.C08 à L1.C16. C'est le noyau du diagnostic — de « Pourquoi la dette change
tout » à « L'ère de la bullshitnovation ».

### 0.3 L'écart 30 / 31 — ce n'est pas une erreur de compte

`livres.yaml` déclare pour le Livre 1 `chapitres_annonces: 30` et
`chapitres_acquis: 30` ; le dossier contient 31 fichiers, série L1.C01 à L1.C31
complète, sans trou.

**L1.C31 n'a pas été acquis du livre : il a été écrit par le corpus le
2026-09-09**, en réponse au falsifieur F10, sur arbitrage de l'auteur du même
jour. Sa source S1 le dit : *« L'auteur du corpus, arbitrage du 2026-09-09 […]
Ce chapitre ne les propose pas : il les enregistre »*. Son régime est
`conception`, là où les seize premiers sont `hybride`.

**Le registre n'est donc pas faux — il ne modélise pas la provenance.** Il n'a
pas de moyen de distinguer *acquis d'une source* de *créé par le corpus*.

**AUCUNE MODIFICATION N'EST RECOMMANDÉE À CETTE ÉTAPE**, pour deux raisons qui se
cumulent. Ajouter un champ au registre serait **une modification du schéma**,
donc de la convention, avec la migration scriptée et l'incrément de journal que
le § 15 exige. Et **un décompte calculable ne devrait pas être saisi à la main** :
le nombre de fichiers d'un livre est lisible dans l'arborescence, et un champ
recopié diverge tôt ou tard de ce qu'il est censé compter.

**La provenance est donc portée ici, dans la cartographie, et nulle part
ailleurs.** Trois modélisations possibles sont proposées **sans être appliquées
ni recommandées**, pour arbitrage séparé :

1. **au chapitre** — un champ de provenance dans l'en-tête, valeurs closes
   (`acquis` / `cree_par_le_corpus`) : la provenance suit le texte, et le
   décompte se calcule ;
2. **au registre** — un champ de comptage : le plus simple à lire, le plus
   exposé à la dérive, et il ne dit pas *quel* chapitre est créé ;
3. **nulle part** — la provenance reste lisible dans les sources primaires du
   chapitre, comme aujourd'hui pour L1.C31 : coût nul, mais rien n'est
   contrôlable par le script.

**Ces trois options relèvent d'un arbitrage sur la convention, non de cette
cartographie.**

### 0.4 La tension sur le Livre 0 — les deux textes ne parlent pas de la même chose

**Convention § 6 :** *« Il s'écrit au fil de l'eau. Dès qu'un livre est vérifié,
ses entrées de livre 0 sont rédigées dans la foulée. Ni avant — ce serait une
promesse — ni à la fin — ce serait une reconstitution de mémoire. »*

**`livres.yaml`, note du Livre 0 :** *« Arbitré le 2026-09-04 : le Livre 0 se
réalise à LA FIN des premières passes du corpus, jamais avant. »* La note
**signale elle-même la tension** : *« à concilier avec la réalisation en fin de
passes, qui est la règle arbitrée »*.

**Interprétation proposée — les deux règles portent sur des objets différents.**

- **§ 6 fixe le déclencheur d'UNE ENTRÉE** : elle s'écrit quand ses chapitres
  sources passent à `verifie`. C'est une règle de *provenance* — on n'écrit pas
  une synthèse de ce qui n'est pas encore établi, et on ne la reconstitue pas de
  mémoire des mois après.
- **`livres.yaml` fixe l'achèvement DU LIVRE** : le Livre 0 n'est pas *complet*
  avant la fin des premières passes, parce qu'il indexe des chapitres qui
  bougent encore.

**Les deux se concilient sans modifier la convention** : *aucune entrée avant que
ses sources soient vérifiées ; aucun Livre 0 complet avant que le corpus cesse de
bouger.* Le « à la fin » de `livres.yaml` porte sur la **complétude**, non sur le
calendrier de chaque entrée — et c'est bien ce que la note veut dire quand elle
appelle à concilier.

**Et aujourd'hui, la question est vide de conséquence pratique : zéro chapitre
est `verifie`. Les deux lectures interdisent d'écrire quoi que ce soit
maintenant.** La tension deviendra réelle au premier chapitre vérifié, et c'est
à ce moment qu'il faudra trancher — pas avant.

### 0.5 Autres écarts relevés, non corrigés

- **L1.C01 ne porte aucune source primaire** et compte 26 vérifications en
  attente. C'est le chapitre d'ouverture du livre fondateur.
- **L1.C13, L1.C14 et L1.C30 ne reçoivent aucun renvoi** du reste du corpus ;
  L1.C11, L1.C16 et L1.C31 n'en reçoivent qu'un. **Cela signale un isolement
  dans le graphe, non un défaut d'instruction** : C13 et C14 sont en audit
  contradictoire avec 16 et 12 sources.
- **La coupure de régime est nette et non déclarée** : L1.C01 à L1.C16 sont en
  `hybride`, L1.C17 à L1.C31 en `conception`. C'est la frontière entre le
  diagnostic et la proposition, et elle n'est nommée nulle part.

---

## 1. La matrice des 31 chapitres

### Légende des natures d'énoncé

Chaque fiche qualifie ce qu'elle porte. **Un programme qui applique correctement
une règle n'est jamais une validation de cette règle.**

**ET AUCUNE MENTION « CONSERVER » NE VAUT VÉRIFICATION.** Les 31 chapitres sont
en `brouillon` ou en `audit_contradictoire` ; **aucun n'est `verifie`**. Tout
verdict « conserver » de cette matrice signifie *conserver la thèse et
l'architecture, sous réserve de l'audit factuel*, jamais *tenir pour établi*.

| code | nature |
|---|---|
| **F** | fait établi par une source ouverte et datée |
| **I** | interprétation du corpus |
| **D** | décision constitutive de l'auteur |
| **H** | hypothèse prospective |
| **O** | mécanisme encore ouvert |
| **M** | résultat produit par un modèle exploratoire — ne vaut pas preuve |

`entrants` = nombre de chapitres d'autres livres qui renvoient à ce chapitre.
**C'est une mesure de CENTRALITÉ DANS LE GRAPHE du corpus, et rien d'autre.**
Elle ne mesure **ni la qualité du chapitre, ni son degré de validation, ni la
quantité de travail qui lui a été consacrée**. Un chapitre très cité peut être
faux ; un chapitre isolé peut être instruit et solide. Le chiffre sert à repérer
ce sur quoi le reste du corpus s'appuie — donc **ce qu'une réécriture
déplacerait le plus** —, pas à classer les chapitres par mérite.

---

### L1.C01 — Pourquoi l'humanité a besoin d'un nouveau paradigme économique
`hybride` · 0 source · 26 en attente · 17 468 signes · **5 entrants**

**Fonction.** Ouverture : énonce les trois propositions du livre sans les
démontrer.
**Thèse.** Les crises procèdent d'une mécanique commune — l'émission contre
dette et rendement. **(H)**
**Affirmations documentaires.** Aucune n'est sourcée : production mondiale,
émissions, extraction, artificialisation, déclin des vertébrés, paternité de
« polycrise », horizon des investisseurs — **26 énoncés attendent une source**.
**Apports depuis.** L26 (thermodynamique), L2, L18 ont instruit le diagnostic
physique ; L8 a instruit les angles morts théoriques.
**Arbitrages.** Aucun ne le nomme. **A44 le touche indirectement** : la promesse
qu'il annonce est plus large que celle qu'A44 autorise.
**Trop fort.** *« procèdent d'une mécanique commune »* — le corpus a établi
ailleurs que la contrainte est **conditionnelle** (L1.C08, L1.C14) et non
arithmétique.
**Reste valide.** La structure d'annonce en trois propositions, et l'honnêteté du
« sans encore les démontrer ».
**Sources nécessaires.** Les 26. C'est le chapitre le plus démuni du livre.
**Action : réécrire substantiellement.** Un chapitre d'ouverture sans source
n'est pas publiable en seconde édition.
**Dépendance bloquante.** L'acquisition des 26 sources.
**Livre 0.** Pas avant vérification. Questions candidates : *« Qu'est-ce que la
polycrise ? »*, *« La monnaie est-elle neutre ? »*

---

### L1.C02 — La grande contradiction
`hybride` · 6 sources (données) · 24 en attente · **6 entrants**

**Fonction.** Poser la corrélation richesse financière / dégradation et l'ériger
en hypothèse à trancher.
**Thèse.** La valeur financière serait obtenue par le non-report de coûts. **(H)**
**Affirmations.** Corrélation documentée **(F)** ; lien de production **(H)**.
**Apports.** L18 (comptabilités écologiques), L26 (entropie), L2.
**Trop fort.** Rien de bloquant : le chapitre pose déjà l'hypothèse *comme*
hypothèse et nomme ses deux épreuves.
**Reste valide.** L'essentiel — c'est un des chapitres les mieux construits du
diagnostic.
**Action : conserver, corriger localement.** Compléter les 24 vérifications.
**Livre 0.** *« Richesse financière et dégradation écologique progressent-elles
ensemble ? »*

---

### L1.C03 — Une croissance infinie peut-elle exister sur une planète finie ?
`hybride` · 7 sources · 19 en attente · **10 entrants** (dont 6 du Livre 26)

**Fonction.** Trancher le découplage.
**Thèse.** Le découplage absolu mondial n'est pas observé ; trois mécanismes
l'expliquent. **(F** pour l'observation, **I** pour l'explication**)**
**Résultat propre, et il est rare.** *« Le chapitre n'établit pas qu'une
croissance économique perpétuelle soit impossible : il établit qu'une croissance
perpétuelle du volume physique produit l'est. »* **C'est une auto-limitation
explicite, et elle doit survivre à la refonte.**
**Apports.** Le Livre 26 entier l'instruit ; A41 (le mot « entropie » éprouvé ou
métaphorique) le contraint.
**Arbitrages.** **A41 (arbitré).**
**Action : conserver.** Le meilleur chapitre du diagnostic.
**Livre 0.** *« Le découplage absolu est-il observé ? »*

---

### L1.C04 — L'économie à l'intérieur de la nature
`hybride` · 9 sources · 11 en attente · **3 entrants**

**Fonction.** Poser le cadre — trois niveaux emboîtés, limites planétaires,
donut.
**Thèse.** L'économie est un sous-système. **(F** pour les cadres, **I** pour la
substitution robustesse/performance**)**
**Trop fort.** *« sept limites sur neuf évaluées comme franchies »* — vérifier
l'édition et la date de l'évaluation ; le chiffre bouge.
**Apports.** L1.C23 y revient et **établit ce que la robustesse coûte**, ce que
C04 n'énonce pas.
**Action : corriger localement**, en renvoyant explicitement à C23 pour le coût.
**Livre 0.** *« Combien de limites planétaires sont franchies ? »*

---

### L1.C05 — Qu'est-ce que la monnaie, vraiment ?
`hybride` · 2 sources · 18 en attente · **3 entrants**

**Fonction.** Définir la monnaie comme registre de créances plutôt que par ses
fonctions.
**Thèse.** Les règles d'émission relèvent d'une décision, non d'une nécessité.
**(I)** — c'est le pivot de tout le livre.
**Apports.** L10 (monnaies, banques, banques centrales), L16 (typologie des
alternatives), L20 (droit monétaire).
**Trop fort.** Rien. Mais **2 sources pour un chapitre pivot est insuffisant**.
**Action : corriger localement**, en renforçant l'appareil.
**Livre 0.** *« Qu'est-ce que la monnaie ? »* — entrée très probable.

---

### L1.C06 — La monnaie, angle mort de l'écologie politique
`hybride` · 2 sources · 13 en attente · **2 entrants**

**Fonction.** Montrer que les trois familles de propositions écologistes ne
touchent pas les conditions du crédit.
**Thèse.** La limite est structurelle. **(I)**
**Pièce.** `OPERATIONNALISATION-INSOLVABLE` **le nomme**.
**Apports.** L6 (droits de la nature), L5 (trajectoires).
**Trop fort.** *« elles ne modifient pas les conditions auxquelles le crédit est
accordé »* — à confronter à la taxonomie et aux exigences prudentielles
climatiques instruites depuis (L2).
**Action : corriger localement.**
**Livre 0.** *« Pourquoi les politiques écologiques ne suffisent-elles pas ? »*

---

### L1.C07 — Comment les banques créent vraiment la monnaie
`hybride` · 3 sources · 12 en attente · **13 entrants**

**Fonction.** Le mécanisme comptable — socle factuel du livre.
**Thèse.** Le crédit précède le dépôt. **(F)** — reconnu par la Banque
d'Angleterre en 2014.
**Apports.** L19 (comptabilité monétaire de l'émission sans dette), L21
(plomberie financière), L2.
**Reste valide.** La thèse et l'architecture, sous réserve de l'audit factuel :
**12 vérifications restent en attente et le chapitre est en brouillon**.
**Action : conserver la thèse et l'architecture, SOUS RÉSERVE DE L'AUDIT
FACTUEL.** Un chapitre intellectuellement solide n'est pas pour autant vérifié.
**Livre 0.** *« Les banques prêtent-elles l'épargne des déposants ? »* — entrée
canonique évidente.

---

### L1.C08 — Pourquoi la dette change tout
`hybride` · **audit contradictoire** · 11 sources · 17 en attente · **12 entrants**

**Fonction.** Établir la contrainte de croissance.
**Thèse, dans sa forme corrigée.** *« Une économie stationnaire endettée est
théoriquement possible si l'encours est stable et les intérêts redépensés. »*
**(I)** — **la contrainte est conditionnelle, pas arithmétique.**
**Ce que la refonte doit propager.** Cette correction **contredit la version
forte que C01 et C14 laissent encore passer**. C'est la contradiction interne la
plus importante du livre.
**Action : conserver, et faire de C08 la référence** que C01, C13 et C14 doivent
suivre.
**Livre 0.** *« La croissance est-elle mathématiquement obligatoire ? »*

---

### L1.C09 — L'architecture invisible
`hybride` · **audit contradictoire** · 19 sources · **18 entrants**

**Fonction.** Nommer les quatre règles implicites.
**Thèse.** Interprétative, **et balisée comme telle par le chapitre lui-même**.
**(I)**
**Apports.** L18 (huit chapitres y renvoient), L2, L22.
**Reste valide.** La quatrième règle — *« cette grammaire, parce qu'elle est
écrite, peut être réécrite »* — porte la charge de toute la seconde partie.
**Action : conserver.**
**Livre 0.** *« Qu'est-ce que l'architecture invisible de la monnaie ? »*

---

### L1.C10 — Une monnaie peut-elle être conçue autrement ?
`hybride` · **audit contradictoire** · 22 sources · **3 entrants**

**Fonction.** Inventaire des alternatives, et cahier des charges d'une refonte.
**Thèse.** Une autre monnaie est techniquement possible ; les alternatives
existantes ne touchent chacune qu'une des quatre règles. **(F** pour les cas,
**I** pour la grille**)**
**Falsifieur.** **F12 (l'indiscernabilité)** est né de ce terrain.
**Action : conserver, corriger localement** — le cahier des charges doit
maintenant intégrer A46 (cinq fonctions séparées).
**Livre 0.** *« Wörgl, WIR, monnaies locales : qu'ont-elles prouvé ? »*

---

### L1.C11 — La première malédiction monétaire
`hybride` · **audit contradictoire** · 9 sources · **1 entrant**

**Fonction.** Le point de création : le filtre de solvabilité.
**Thèse.** Ce qui ne rembourse pas n'est finançable que par redistribution.
**(I)**, appuyée sur des ordres de grandeur **(F)**.
**Trop fort.** Les deux chiffres — 8 700 Md$ de financements fossiles, 7 300 Md$
de flux nuisibles contre 220 Md$ de solutions fondées sur la nature — **doivent
porter leur périmètre et leur millésime** ou ils seront attaqués.
**Action : conserver, corriger localement.**
**Livre 0.** *« Pourquoi le crédit ne finance-t-il pas la régénération ? »*

---

### L1.C12 — La deuxième malédiction monétaire
`hybride` · **audit contradictoire** · 12 sources · **4 entrants**

**Fonction.** Pourquoi verdir le crédit ne suffit pas.
**Résultat propre.** Le chapitre **écarte lui-même l'argument quantitatif** que
le livre avançait — *« que les séries monétaires réfutent »*. **(F)**
**C'est un exemple du travail que la seconde édition doit généraliser** :
abandonner un argument faux pour en garder trois défendables.
**Action : conserver.**
**Livre 0.** *« La finance verte peut-elle suffire ? »*

---

### L1.C13 — La troisième malédiction monétaire
`hybride` · **audit contradictoire** · 16 sources · **0 entrant**

**Fonction.** Nouer dette financière et dette écologique.
**Thèse.** Le nœud ne se défait pas de l'intérieur. **(I)**
**Trop fort.** *« ne se défait pas de l'intérieur »* est en tension avec la forme
conditionnelle établie en C08. **À aligner.**
**Zéro entrant : le chapitre est ISOLÉ DANS LE GRAPHE.** Cela ne dit pas
qu'il n'a pas été instruit — il est en audit contradictoire et porte 16 sources
— mais qu'aucun autre livre ne s'y adosse.
**Action : corriger localement**, après alignement sur C08.

---

### L1.C14 — La dette, un mythe de Sisyphe économique
`hybride` · **audit contradictoire** · 12 sources · **0 entrant**

**Fonction.** Donner la figure d'ensemble des trois malédictions.
**Ce que le chapitre fait déjà bien.** Il **délimite strictement sa portée** et
isole la part monétaire au lieu de tout lui attribuer.
**Action : conserver**, mais **candidat à la fusion** avec C13 dans la seconde
édition : une figure littéraire et un mécanisme, deux chapitres pour un seul
mouvement.

---

### L1.C15 — L'essentiel insolvable
`hybride` · **audit contradictoire** · 15 sources · **35 entrants**

**Fonction.** **Le concept central du livre.** Quatre conditions cumulatives de
solvabilité.
**Thèse.** Les activités qui entretiennent les conditions de la vie échouent sur
plusieurs conditions à la fois, par construction. **(I)**
**Ce qu'il traite déjà.** L'objection décisive de l'emprunt d'État : *« le filtre
ne disparaît pas, il change de porteur »*. **(I, solide)**
**Pièce.** `OPERATIONNALISATION-INSOLVABLE` **(orienté par l'auteur)** — cinq
critères arrêtés, cinq étapes empiriques, **non circularité tenue à moitié**.
**Action : conserver la thèse et l'architecture, sous réserve de l'audit
factuel — c'est le pivot.** Et **ajouter le renvoi à la pièce ouverte** : le
concept est **prospectif**, et **son ampleur empirique reste inconnue**. **Cela
n'empêche pas la vérification documentaire du chapitre** : `verifie` certifie des
sources contrôlées et une structure cohérente, non la justesse d'une thèse — voir
§ 5.
**Livre 0.** *« Qu'est-ce que l'essentiel insolvable ? »* — entrée majeure.

---

### L1.C16 — L'ère de la bullshitnovation
`hybride` · **audit contradictoire** · 12 sources · **1 entrant**

**Fonction.** Ce que le filtre finance à la place.
**Thèse retenue, et elle est étroite.** *« À l'instant de la décision de
financement, une innovation qui traite un problème et une innovation qui le
simule présentent le même profil. »* **(I)**
**Ce que le chapitre fait bien.** Il **éprouve sa formule sur un
contre-exemple** — l'hépatite C — et **distingue la catégorie de la fraude**.
**Action : conserver.** Le mot lui-même est un risque éditorial ; la thèse ne
l'est pas.
**Livre 0.** *« Qu'est-ce que la bullshitnovation ? »*

---

### L1.C17 — Et si la planète avait sa propre banque ?
`conception` · 14 sources · **12 entrants**

**Fonction.** **Charnière du livre** : ouvre la seconde partie en posant une
question.
**Arbitrages.** **A44 (arbitré)** — la promesse centrale ; **`REGLE-D-EMISSION`
(orienté)**.
**Ce que le chapitre pose déjà.** *« l'émission et le reflux forment un mécanisme
unique »*, et les **cinq problèmes non résolus** : légitimité, qualification,
calibration, ancrage, aléa moral.
**Ce qu'A44 change.** La question *« et si la planète avait sa propre banque ? »*
doit désormais recevoir la réponse restreinte : **NEMO IMS garantit la
disponibilité du financement, pas les conditions de la vie**.
**Ce qu'A46 change.** L'institution unique devient **cinq centres de
responsabilité indépendants**.
**Action : réécrire substantiellement.**
**Dépendance.** A46 et `REGLE-D-EMISSION`.

---

### L1.C18 — Le GAÏA Economic Symposium
`conception` · 22 sources · 32 en attente · 36 985 signes · **57 entrants — le
maximum du livre**

**Fonction.** Répondre au problème de la légitimité.
**Ce que le chapitre a déjà corrigé.** L'affirmation *« aucune institution ne
représente le vivant »* — fausse : conventions contraignantes, personnalité
juridique en Équateur, Colombie, Nouvelle-Zélande. **Ce qui manque est plus
étroit : le mandat monétaire.** **(F)**
**Architecture exposée.** Quatre chambres étanches. **(D)**
**Ce qu'A46 commande, et ce n'est pas un décompte.** A46 arrête **cinq
fonctions séparées** — mesure scientifique, qualification, priorité démocratique,
calibrage et versement, contrôle et recours — **et cinq centres de responsabilité
indépendants, sans imposer cinq institutions**. Quatre chambres peuvent donc
porter cinq fonctions, à condition que la séparation soit **interne, réelle et
vérifiable**. **CE QU'IL FAUT ÉTABLIR, ET QUI N'EST PAS FAIT** : une table
reliant chaque fonction d'A46 à la ou aux chambres existantes, faisant
apparaître (a) les **cumuls interdits** — nul ne mesure, qualifie, verse et se
contrôle —, (b) les **fonctions absentes** de l'architecture actuelle, (c) les
**séparations internes possibles** à l'intérieur d'une chambre. **La réécriture
de C18 dépend du résultat de cette analyse, non du rapport quatre à cinq.**
**Falsifieurs.** F3 (connaissance dispersée, **vulnérabilité instruite**), F4
(obstacle de droit positif — l'interdiction faite aux BCN de l'Union).
**Action : réécrire substantiellement.** C'est le chapitre le plus travaillé du
corpus et celui qu'A46 déplace le plus.
**Dépendance.** L'analyse de correspondance fonctions d'A46 ↔ chambres — à
conduire, et elle peut conclure que quatre chambres suffisent.

---

### L1.C19 — Le Yin et le Yang de la finance
`conception` · 9 sources · **5 entrants**

**Fonction.** Articuler finance marchande et financement de la régénération.
**Ce que le chapitre a déjà écarté.** *« Il ne s'agit pas de deux monnaies ni de
deux circuits étanches »* — **une seule monnaie, deux orientations**. **(I)**
**Ce qu'il laisse ouvert.** La régulation mutuelle des deux orientations *« reste
affirmée sans être spécifiée »*, le triangle d'incompatibilité, l'aléa moral, le
statut comptable de la contrepartie.
**Arbitrages.** **A32 (régime de change, arbitré)** répond au triangle ; **A35 et
A35b** portent la contrepartie.
**Action : réécrire substantiellement** — trois de ses quatre questions ouvertes
ont reçu depuis une réponse ou un arbitrage.

---

### L1.C20 — De l'argent sans dette
`conception` · 10 sources · **26 entrants**

**Fonction.** Le mécanisme d'émission.
**Force du chapitre.** Il **pose l'objection de Rueff à sa force maximale et la
concède**. **(I)**
**Ce qui reste ouvert.** *« Il n'y a rien à porter à l'actif qui satisfasse la
définition d'un actif. »* Le dispositif retenu — réduction transitoire des fonds
propres — *« n'est pas stabilisé »*.
**Arbitrages.** **A35 (arbitré, porteur du passif)**, **A35b (ouvert : nature,
exigibilité, contrepartie, extinction)**, **A30 (qualification juridique de
l'unité)**.
**Résultat de modèle.** **(M)** `modeles/a35b_bilans.py` a produit **six
résultats séparés**, dont un seul est calculé mécaniquement ; **la qualification
en passif est proposée, jamais établie**. **Ce programme ne valide rien.**
**Action : réécrire substantiellement.**
**Dépendance bloquante.** **A35b** — et la revue par les deux compétences
humaines nommées au dossier `protocoles/revue-comptable-a35b.md`.

---

### L1.C21 — Le reflux collectif
`conception` · 15 sources · 24 en attente · 34 830 signes · **47 entrants**

**Fonction.** Le mécanisme de destruction, sans lequel l'émission est
indéfendable.
**Ce que le chapitre établit.** Deux instruments — reflux transactionnel,
demurrage — et **pourquoi il en faut deux**. **(I, solide)**
**Ce qu'il établit contre le livre.** *« Le calibrage n'existe pas. »* Le pilotage
décrit est **discrétionnaire annuel**, et deux résultats établis convergent vers
une **règle automatique** — arbitrage que le livre n'a pas tranché.
**Conclusion du chapitre.** *« L'objection inflationniste est adressée et non
résolue. »*
**Arbitrages.** **A32 (arbitré)**, **A36 (nature de la fonte, orienté)**, **A38
(épargne retraite, ouvert)** ; pièce **`CONTROLE-DES-CAPITAUX` (ouvert)**.
**Falsifieurs.** **F1 (calibration)**, **F7 (pilotage — déplacé, non traité)**.
**Action : réécrire substantiellement.**
**Dépendance bloquante.** F1 et le `RECALIBRAGE`.

---

### L1.C22 — Financer les communs
`conception` · 14 sources · **24 entrants**

**Fonction.** Périmètre, limites, répartition entre pays.
**Ce que le chapitre établit contre le livre.** L'alternative *« impôt ou
marché »* est **incomplète** — la gouvernance polycentrique est une troisième
voie établie, **et son principal auteur argumente contre l'échelle mondiale
unique**. **(F)**
**Et la ligne du livre cesse de tenir** *« dans le régime des services,
c'est-à-dire là même où se trouve ce qui a motivé la démarche »*. **C'est un
résultat défavorable majeur.**
**Objection ajoutée.** La **fongibilité de l'aide** : l'effet obtenu est le
volume émis **moins** ce que les budgets nationaux retirent.
**Test acquis.** Le critère de dette élargi en 2016, appliqué à l'unité décrite,
**ne trouve ni principal ni intérêt à saisir**. **(F)**
**Action : réécrire substantiellement.**

---

### L1.C23 — L'économie de la robustesse
`conception` · 19 sources · **8 entrants**

**Fonction.** Reprendre la question laissée par C04.
**Ce que le chapitre établit et que le livre n'énonce pas.** *« Un gain de
robustesse est une réduction délibérée d'efficacité mesurée dont quelqu'un
supporte le prix. »* **(I, forte)**
**Objection centrale, et elle atteint un seuil.** Le dispositif est **centralisé
là où la littérature de la robustesse recommande diversité et modularité** — et
l'objection arrive **par trois traditions sans rapport entre elles**. *« Une
objection qui se présente trois fois par des chemins séparés cesse d'être une
objection pour devenir un résultat. »*
**Action : conserver, et en faire un chapitre d'objection assumée.**
**Ce que la seconde édition doit décider.** A46 (cinq fonctions séparées) est une
**réponse partielle** à cette objection : elle décentralise le pouvoir, pas la
connaissance.

---

### L1.C24 — Pourquoi le dollar ne peut pas durer
`conception` · 12 sources · **20 entrants**

**Fonction.** Diagnostic du système monétaire international.
**Ce que le chapitre conclut, contre son propre titre.** *« Le corpus n'établit
pas que le dollar ne peut pas durer ; il établit que sa position repose sur une
infrastructure privée que la proposition ne touche pas. »* **(F + I)**
**Condition décisive posée.** *« Une unité de compte qui permet de libeller un
prix mais non d'éteindre une dette n'est pas une devise clé. »*
**Action : réécrire substantiellement, ET CHANGER LE TITRE.** Un titre que son
propre chapitre réfute ne peut pas passer en seconde édition.
**Livre 0.** *« Le dollar peut-il être remplacé par décision ? »* — la réponse du
corpus est **non, et elle est établie**.

---

### L1.C25 — Histoire des systèmes monétaires internationaux
`conception` · 12 sources · **20 entrants**

**Fonction.** Chronologie, et thèse stratégique de l'adoption.
**Ce que le chapitre réfute.** *« Les réformes ne se font qu'à la faveur d'une
crise aiguë »* — **faux tel qu'énoncé** : 1971 n'est pas une sortie de guerre, et
le livre porte lui-même le contre-exemple de la zone euro. **(F)**
**Le résultat le plus lourd du livre.** *« À Bretton Woods, le projet de Keynes
était prêt et il a perdu. Il a perdu sur la disposition qui aurait pénalisé les
pays excédentaires. »* Trois épisodes, même schéma : **ce qui décide est la
position du créancier, non la qualité du projet.** **(F)**
**Pièce.** **`COMPENSATION-SYMETRIQUE` (orienté)** — c'est exactement la
disposition que ce chapitre montre perdue à Bretton Woods : la charge sur les
excédents. **A45 ne s'applique pas ici** : il porte sur le soutien aux
importations essentielles, non sur le traitement des soldes persistants.
**Falsifieur.** **F6 (l'adoption contre le créancier)** — c'est ce chapitre qui
le fonde.
**Action : conserver et renforcer.** C'est le chapitre qui donne au livre sa
lucidité stratégique.

---

### L1.C26 — Le NEMO Exchange Standard
`conception` · 9 sources · **28 entrants**

**Fonction.** Le référentiel de change.
**Deux propriétés favorables et solides.** Neutralité monétaire globale au pivot ;
**suppression des réserves de change**. **(I)**
**Trois résultats défavorables, dont un bloquant.** Le livre affirme neutraliser
le triangle de Mundell *« sans donner aucun mécanisme »* ; **le dispositif ne le
neutralise pas, il en occupe un sommet — et c'est l'autonomie monétaire qui est
perdue.** **(F)**
**Et A32 tranche depuis** : NEMO IMS **abandonne la libre circulation
inconditionnelle des capitaux**, ce qui **résout le trilemme dans l'autre sens** :
parités administrées + autonomie monétaire + compte de capital réglementé.
**Deuxième résultat.** Le solde commercial *« se déverse intégralement sur la
masse monétaire nationale »*. **C'est `COMPENSATION-SYMETRIQUE` qui y répond** —
corridor des deux côtés, obligations graduées, parités administrées —, **et non
A45**, qui ne traite que le soutien aux importations essentielles. Le modèle
`modeles/nemo_soldes.py` mesure les deux dispositifs séparément **(M)** ; **il ne
valide ni l'un ni l'autre**, et ses seuils ne sont pas calibrés.
**Action : réécrire substantiellement.** **La phrase sur le triangle doit être
retirée, et A32 mise à sa place.**

---

### L1.C27 — Une économie mondiale coopérative — NEMO SWIFT
`conception` · 9 sources · **39 entrants**

**Fonction.** Ce qui fait tenir une zone monétaire volontaire.
**Force reconnue.** La page sur le passager clandestin est *« la meilleure de son
argumentation institutionnelle »*.
**Quatre résultats, dont le dernier est le plus lourd.** *« En faisant dépendre le
rééquilibrage des économies nationales des émissions régénératives, le dispositif
fait dépendre l'équilibre extérieur de chaque pays du barème voté au centre. »*
C'est **à la fois l'argument social le plus fort du livre et sa concentration de
pouvoir la plus considérable**.
**Correction déjà acquise.** La suppression des réserves **ne vaut que pour le
commerce intrazone**.
**Falsifieur.** **F8 (le désarmement)**, **F5 (l'antériorité)**.
**Action : réécrire substantiellement.**
**Ce qu'A46 apporte.** La séparation des cinq fonctions **atténue** la
concentration sans la supprimer : l'assemblée qui vote le barème ne mesure plus,
ne verse plus et ne se contrôle plus elle-même.

---

### L1.C28 — Au-delà du PIB
`conception` · 7 sources · **15 entrants**

**Fonction.** Ce qui remplace le PIB.
**Quatre résultats.** Le tableau de bord **n'arbitre pas** ; la famille
« robustesse » **ne mesure qu'une des trois propriétés** ; l'objection de
l'indicateur pris pour cible **s'étend au tableau entier** ; et **une
contradiction interne** — le seul critère de révision des parités **indexe sur la
croissance du PIB**.
**Falsifieurs.** **F2 (métrologie)**, **F3 (indicateur pris pour cible)**, **F13
(incommensurabilité, orienté)**.
**Action : réécrire substantiellement.** La contradiction interne est
rédhibitoire en l'état.

---

### L1.C29 — Vision globale et chantiers ouverts
`conception` · 6 sources · **18 entrants**

**Fonction.** La contrepartie comptable, et l'état du dossier.
**Résultat qui oblige le corpus à se corriger lui-même.** *« L'actif qui gage
l'émission est un droit sur un flux que le succès éteint. »* **(I, décisif)**
**Issue proposée, plus solide que celle du Cahier.** Renoncer à refermer la partie
double et **assumer des fonds propres négatifs** — tenable pour un émetteur, mais
suppose d'établir que le GES en est un.
**Arbitrages.** **A35 (arbitré)**, **A44 (arbitré)**, **A37 (forme juridique,
orienté)**.
**Action : réécrire substantiellement**, et **actualiser les huit arbitrages du
chemin critique** : ils sont aujourd'hui **19 arbitrages, 14 falsifieurs et 20
pièces**.

---

### L1.C30 — Imagine l'année 2100
`conception` · 2 sources · **0 entrant**

**Fonction.** Récit de clôture.
**Ce que le corpus a déjà tranché.** *« Un récit ne porte pas de thèse
falsifiable, et lui appliquer le traitement contradictoire serait une erreur de
catégorie. »*
**Trois résultats.** Le récit **finance par l'émission le soin et l'enseignement**,
là où le critère cesse de tenir — *« la version racontée au public est plus large
que celle que la conception peut justifier »* ; il **attribue au changement
monétaire des effets qu'aucun mécanisme ne produit** ; il fournit des **jalons
datés** contre lesquels juger.
**Action : réécrire substantiellement, ou retirer de la seconde édition.**
**L'écart entre le récit et la conception se compte en points de PIB**, et A44
restreint désormais la promesse : le récit dit plus que ce que NEMO IMS promet.

---

### L1.C31 — L'ajout est une mobilisation de ressources réelles, ou il n'est rien
`conception` · 2 sources · **1 entrant** · **écrit par le corpus, non acquis**

**Fonction.** Enregistrer la proposition centrale de l'auteur contre F10.
**Décision constitutive.** **(D)** *« La création monétaire produit du pouvoir
d'achat et non des ressources réelles. »*
**Arbitrages.** **A35b (ouvert)**, **A44**, **A43** ; **F10 (ouvert)** ; pièces
**`REGLE-D-EMISSION`**, **`OPERATIONNALISATION-INSOLVABLE`**.
**Action : conserver — c'est une pièce neuve et centrale.**
**Où le placer.** **Pas en dernier.** Cette distinction commande la lecture de
C17 à C29 et doit être posée **avant** elles.
**Livre 0.** *« Créer de la monnaie crée-t-il des ressources ? »* — entrée
majeure, et elle corrige un malentendu répandu.


---

## 2. Synthèse transversale — les cinq ensembles

### 2.1 Ce qui reste inchangé

**Le mécanisme de création monétaire (L1.C07).** Le crédit précède le dépôt.
Reconnu par la Banque d'Angleterre en 2014. **(F)** Rien dans le corpus ne
l'entame ; treize chapitres d'autres livres s'y appuient.

**Le filtre de solvabilité à quatre conditions (L1.C15).** Traduction en flux
monétaire, captation par le financeur, horizon du crédit, survie à
l'actualisation. **(I)** Trente-cinq chapitres y renvoient. **C'est le concept
qui a le mieux résisté**, et l'objection de l'emprunt d'État y a été traitée : le
filtre ne disparaît pas, **il change de porteur**.

**L'absence de découplage absolu mondial (L1.C03)**, avec sa délimitation
explicite : c'est le volume physique qui ne peut croître perpétuellement, non la
valeur ajoutée. **(F + I)**

**L'architecture invisible et ses quatre règles (L1.C09)**, y compris son propre
balisage comme interprétation. **(I)**

**La possibilité technique d'une autre convention monétaire (L1.C10)**, appuyée
sur des cas réels et sur leurs limites connues. **(F)**

**Et la lucidité stratégique de L1.C25** : ce qui décide d'une réforme monétaire
est **la position du créancier**, non la qualité du projet. **(F)** C'est le
résultat le plus dur du livre et il n'a pas bougé.

### 2.2 Ce qui subsiste mais doit être reformulé

**La contrainte de croissance.** Elle est **conditionnelle, non arithmétique**
(L1.C08, L1.C14, L1.C23). L1.C01 et L1.C13 portent encore la version forte.
**C'est la contradiction interne la plus répandue du livre, et elle se corrige
par alignement sur C08.**

**La promesse centrale — A44.** *« NEMO IMS garantit la disponibilité du
financement pour les besoins essentiels matériellement réalisables, dans les
limites écologiques reconnues et sous contrôle démocratique. »* **(D)**
Conséquence éditoriale : **tout passage qui laisse entendre que NEMO IMS garantit
un résultat écologique ou social doit être repris.** Sont concernés C01, C17, C30
au minimum. Et **deux engagements deviennent vérifiables par contre-exemple** :
ne pas bloquer une action essentielle réalisable, ne pas financer l'incompatible.

**L'institution.** Les quatre chambres de L1.C18 deviennent **cinq fonctions
séparées (A46)** : mesure scientifique, qualification, priorité démocratique,
calibrage et versement, contrôle et recours. **(D)** *« Aucune autorité ne cumule
la mesure, la qualification, la priorité, l'émission et son propre contrôle. »*
**Cinq fonctions n'impose pas cinq institutions** : cinq centres de
responsabilité indépendants, l'organisation juridique restant ouverte.

**Le titre de L1.C24.** Le chapitre réfute son propre titre. **Il doit changer.**

**Le récit de L1.C30.** Il promet plus que ce que A44 autorise.

### 2.3 Les mécanismes modifiés depuis la rédaction

| mécanisme | état dans le livre | état après le corpus |
|---|---|---|
| **Régime de change** | triangle de Mundell « neutralisé », sans mécanisme | **A32** : parités administrées + autonomie monétaire + **compte de capital réglementé**. Le trilemme n'est pas nié, il est **tranché** — et c'est la libre circulation des capitaux qui est abandonnée **(D)** |
| **Paiements courants** | non distingués des mouvements de capitaux | **maintenus** ; seul le compte de capital est réglementé **(D)** |
| **Déséquilibres courants persistants** | absorbés « par le pivot » | **`COMPENSATION-SYMETRIQUE`** (orienté) : comptes des banques centrales à l'institution, corridor des deux côtés, obligations graduées, parités administrées. **Deux exigences posées, aucune tenue au barème déclaré (M)**. Seuils **non fixés (O)** |
| **Soutien aux importations essentielles** | non traité | **A45** : deux guichets — facilité **remboursable** pour une difficulté temporaire, allocation **non remboursable** pour certains besoins structurels **(D)**. **Qui finance l'allocation reste ouvert (O)**. **A45 ne traite pas le traitement symétrique des soldes** |
| **Émission** | une institution, un critère | **A46** : cinq fonctions séparées ; `REGLE-D-EMISSION` à trois étages **(D + O)** |
| **Décision sous incertitude** | non traitée | **A47** : précaution proportionnée, neuf points, **aucun seuil numérique** ; charge de la preuve répartie ; grille fixée d'avance par l'autorité démocratique après expertise pluraliste **(D)** |
| **Pouvoir d'achat / ressources réelles** | confondus | **L1.C31** : l'émission produit du **pouvoir d'achat**, pas des ressources. Une activité peut devenir nominalement finançable et rester matériellement irréalisable **(D)** |
| **Reprise d'une émission** | « sans dette » lu comme irrévocable | **non remboursable ≠ irrévocable** : récupération des sommes inutilisées, gel des tranches futures, restitution pour erreur manifeste, recouvrement pour fraude **(D)** |

### 2.4 Ce qui est abandonné

**La libre circulation inconditionnelle des capitaux.** **(D)** C'est
l'abandon le plus lourd, et il est explicite.

**La phrase de L1.C26 sur la neutralisation du triangle d'incompatibilité.**
Elle est fausse et le chapitre l'établit. **(F)**

**La thèse « les réformes ne se font qu'à la faveur d'une crise aiguë »** telle
qu'énoncée. **(F)** Deux contre-exemples, dont 1971.

**L'argument quantitatif de L1.C12** — plus de monnaie, plus d'extraction —
réfuté par les séries monétaires. **(F)**

**La reformulation de l'équation quantitative de L1.C21**, qui n'ajoute rien.

**L'additionnalité contrefactuelle** dans le régime probatoire (L1.C18), au
profit d'états physiques mesurés.

**Et l'affirmation qu'aucune institution ne représente le vivant** (L1.C18) :
fausse, et déjà corrigée.

### 2.5 Ce qui reste trop ouvert pour une formulation affirmative

**Le passif.** **A35b est ouvert** : nature, exigibilité, contrepartie,
extinction. Le modèle `a35b_bilans.py` rend **six résultats séparés**, dont **un
seul est calculé mécaniquement** ; la qualification en passif est **proposée,
jamais établie**. **(M — et ce programme ne valide rien.)** Le dossier de revue
attend **deux compétences humaines** : comptable national ou spécialiste de
bilan de banque centrale, et juriste en droit monétaire international.

**La liquidité et l'incidence.** Calculées au pic et **conditionnelles aux
paramètres déclarés**. **(M)**

**Le reflux — sa nature (A36) et son calibrage (F1).** *« Le calibrage n'existe
pas »* (L1.C21). Le pilotage décrit est discrétionnaire ; deux résultats établis
poussent vers une règle automatique, **arbitrage non tranché**. **(O)**

**La forme juridique de l'institution (A37, orienté)** et **la qualification
juridique de l'unité (A30, orienté)**. **(O)**

**Le barème.** `CRITERE-L25` (orienté), **A34 « le barème qui dit vrai exclut »
(ouvert)**, `RECALIBRAGE` (orienté), `DESCENTE-D-ECHELLE` (ouvert). **(O)**

**Les seuils sectoriels d'A47** — horizons de réversibilité, seuil de confiance,
délai utile. **Seule pièce ouverte d'A47**, et **la calibration sur cas réels
n'est pas exécutée**. **(O)**

**Et l'objection de centralisation (L1.C23)**, arrivée par trois traditions
indépendantes. A46 y répond **partiellement** : il décentralise le **pouvoir**,
pas la **connaissance**. `MODELE-ADVERSAIRE` et `MESURE-EXTERIEURE` restent
ouverts.

---

## 3. Architecture proposée pour la deuxième édition

**Principe.** Le Livre 1 porte **la démonstration générale et doit rester
lisible**. Les développements techniques, juridiques et documentaires **restent
dans leurs livres spécialisés**, avec renvois précis. La cartographie ci-dessus
montre que la tentation inverse est réelle : vingt-six livres ont produit de la
matière, et la verser dans le Livre 1 le rendrait illisible.

**Aucun matricule n'est renuméroté ni réattribué. Les identifiants L1.C01 à
L1.C31 restent ce qu'ils sont.** La nouvelle architecture est un **ordre de
lecture**, non une renumérotation.

**Le livre de 2026 est conservé comme texte fondateur et état historique.**

### Les huit mouvements

**I — LE DIAGNOSTIC (ce qui est observé)**
De la contradiction observée à son mécanisme. Rien de prospectif.
→ C02, C03, C04, C01 *(refondu comme ouverture sourcée)*

**II — LA MONNAIE (ce qui est établi)**
Ce qu'est la monnaie, comment elle est créée, ce que cela change.
→ C05, C07, C08, C09

**III — L'ESSENTIEL INSOLVABLE (le problème posé)**
Le filtre, ce qu'il exclut, ce qu'il finance à la place.
→ C15, C11, C12, C13+C14 *(fusionnés)*, C16, C06

**IV — CE QU'UNE ÉMISSION PEUT ET NE PEUT PAS (la clé de lecture)**
**Nouveau mouvement, et il est court.** L'émission crée du pouvoir d'achat, non
des ressources réelles. Sans cette distinction, tout ce qui suit est mal lu.
→ **C31** *(déplacé de la fin au milieu)*, C10

**V — LA PROPOSITION (ce qui est décidé)**
La promesse restreinte, les trois composantes, l'institution à cinq fonctions.
→ C17 *(réécrit sous A44)*, C20, C21, C18 *(réécrit sous A46)*, C19

**VI — LES CONDITIONS (ce qui doit tenir)**
Matérielles, macroéconomiques, juridiques, internationales.
→ C22, C26 *(réécrit sous A32)*, C27, C24 *(retitré)*, C25

**VII — LA GOUVERNANCE ET LA MESURE**
Cinq fonctions, décision sous incertitude, ce qu'on mesure.
→ **nouveau chapitre A46/A47**, C28, C23

**VIII — CE QUI RESTE À DÉMONTRER**
Objections, critères d'abandon, et la distinction finale.
→ C29 *(actualisé)*, **nouveau chapitre de clôture** : ce qui est **établi**, ce
qui est **décidé**, ce qui reste **à démontrer**.

**C30 (le récit) : à retirer de la seconde édition, ou à réécrire sous A44 et à
publier hors du livre.**

### Table de correspondance

| ancien | mouvement | action | motif principal |
|---|---|---|---|
| C01 | I | réécrire | 0 source, 26 en attente ; promesse trop large |
| C02 | I | conserver + sourcer | — |
| C03 | I | conserver | le mieux établi du diagnostic |
| C04 | I | corriger | renvoyer à C23 pour le coût |
| C05 | II | corriger + sourcer | 2 sources pour un pivot |
| C06 | III | corriger | confronter à la taxonomie |
| C07 | II | conserver **sous réserve de l'audit factuel** | thèse et architecture non contestées ; 12 vérifications en attente |
| C08 | II | conserver | **devient la référence sur la contrainte** |
| C09 | II | conserver | — |
| C10 | IV | corriger | cahier des charges à mettre sous A46 |
| C11 | III | corriger | millésimer les ordres de grandeur |
| C12 | III | conserver | — |
| C13 | III | **fusionner avec C14** | aligner sur C08 |
| C14 | III | **fusionner avec C13** | doublon de mouvement |
| C15 | III | conserver | **le pivot du livre** |
| C16 | III | conserver | — |
| C17 | V | réécrire | A44, A46 |
| C18 | V | réécrire | **A46 : analyse de correspondance fonctions ↔ chambres à conduire** |
| C19 | V | réécrire | 3 de ses 4 questions ont reçu réponse |
| C20 | V | réécrire | A35b ouvert |
| C21 | V | réécrire | calibrage inexistant, F1 |
| C22 | VI | réécrire | la ligne cesse de tenir sur les services |
| C23 | VII | conserver | objection assumée |
| C24 | VI | réécrire **+ retitrer** | le chapitre réfute son titre |
| C25 | VI | conserver + renforcer | F6 |
| C26 | VI | réécrire | A32 remplace la phrase fausse |
| C27 | VI | réécrire | concentration de pouvoir, A46 |
| C28 | VII | réécrire | contradiction interne sur le PIB |
| C29 | VIII | réécrire | 8 arbitrages → 19 + 14 + 20 |
| C30 | — | **retirer ou sortir du livre** | promet plus que A44 |
| C31 | IV | conserver, **déplacer** | clé de lecture, pas conclusion |

**DEUX chapitres réellement nouveaux** sont nécessaires : **la gouvernance
A46/A47** (mouvement VII) et **la clôture en trois colonnes** (mouvement VIII).

**L'ouverture du mouvement I N'EST PAS un chapitre nouveau : c'est C01 refondu.**
Le décompte précédent la comptait deux fois. Sa fonction ne change pas — énoncer
les propositions du livre — ; ce qui change est qu'elle devra être sourcée et que
sa promesse devra tenir dans les limites d'A44.

**Et les deux chapitres nouveaux prendraient des matricules neufs.** **Si le
plan est validé et si aucun autre chapitre n'est déclaré auparavant, les
identifiants suivants disponibles seraient L1.C32 et L1.C33.** **Aucun
identifiant n'est attribué ni réservé à ce stade** : les annoncer comme acquis
avant l'arbitrage reviendrait à les réserver, ce que la règle du matricule
n'admet pas davantage qu'une renumérotation.

**La fusion de C13 et C14 ne supprime aucun matricule non plus.** Les deux
chapitres du corpus restent ce qu'ils sont ; c'est **le texte de la seconde
édition** qui réunit leurs deux mouvements en un seul.

---

## 4. Dépendances encore bloquantes

**TROIS DEGRÉS DE BLOCAGE, ET ILS NE SE CONFONDENT PAS.** Une dépendance
ouverte n'interdit presque jamais d'écrire : elle interdit de conclure.

| degré | ce qu'il empêche | ce qu'il laisse faire |
|---|---|---|
| **bloque la rédaction** | écrire le passage du tout | rien |
| **bloque la conclusion** | affirmer, trancher, refermer | **exposer l'architecture, les branches possibles et les critères qui départageront** |
| **bloque le passage à `verifie`** | le statut, donc l'entrée de Livre 0 | rédiger, publier en brouillon, soumettre à l'audit |

**Aucune des dépendances ci-dessous ne bloque la rédaction.** Toutes bloquent la
conclusion, la vérification, ou les deux.

1. **A35b — le passif.** **Bloque la conclusion** de C20, C29 et d'une partie
   de C19, **et leur passage à `verifie`**. Le dossier de revue est écrit ;
   **il attend deux compétences humaines et n'a pas été envoyé**. **Ce qui reste
   possible sans lui** : exposer les branches — passif exigible, passif non
   exigible, fonds propres négatifs assumés — et écrire les critères qui les
   départageront.
2. **F1 et le calibrage du reflux.** **Bloque la conclusion** de C21 et C28.
   *« Le calibrage n'existe pas. »* Aucun seuil n'est fixable par le corpus seul.
   **Ce qui reste possible** : établir le choix entre pilotage discrétionnaire et
   règle automatique, et écrire ce qui déciderait — les deux résultats sur les
   délais et sur la déformation de l'assiette y suffisent.
3. **L'analyse de correspondance fonctions d'A46 ↔ chambres du GES.** Elle
   doit produire les cumuls interdits, les fonctions absentes et les séparations
   internes possibles. **Bloque la conclusion** de C18 et du chapitre de
   gouvernance ; **ne bloque pas leur rédaction**, qui peut exposer les branches.
4. **`CRITERE-L25` et A34 — le barème.** **Bloquent la conclusion** de C22 et
   C27 : la clé de répartition *« porte tout le contenu politique du dispositif
   et n'est pas écrite »*. **Ce qui reste possible** : écrire que la clé porte ce
   contenu, et à quelles conditions une clé serait défendable.
5. **Les vérifications en attente** — 26 pour C01, 24 pour C02, 19 pour C03,
   18 pour C05. **Bloquent le passage à `verifie` seulement.** Ni la rédaction ni
   la conclusion : un énoncé peut être écrit et tenu pour probable tant qu'il est
   balisé comme non vérifié.
6. **Les seuils sectoriels d'A47** et la **calibration sur cas réels** — deux
   équipes, trois dossiers documentés. **Bloquent la conclusion** du chapitre VII
   sur la transférabilité. **Ce qui reste possible, et c'est déjà fait** : le
   protocole et l'instrument de comparaison existent et discriminent.
7. **A37 et A30** — forme juridique de l'institution, qualification juridique
   de l'unité. **Bloquent la conclusion** des passages juridiques de C18 et C20.
   **Ce qui reste possible** : exposer les formes candidates et ce que chacune
   emporte, ce que le Livre 20 a commencé.

**Non bloquant mais à ordonner.** L'alignement de C01 et C13 sur la forme
conditionnelle de C08 peut se faire immédiatement : il ne dépend d'aucune
acquisition.

---

## 5. Chapitres prioritaires vers `verifie`

**TROIS CRITÈRES, ET ILS NE SE CONFONDENT PAS.** Un chapitre peut être
stratégiquement central et documentairement loin du but ; l'ordre de travail se
lit au croisement des trois, non sur l'un d'eux.

| critère | ce qu'il mesure |
|---|---|
| **importance stratégique** | ce dont la seconde édition ne peut pas se passer |
| **proximité documentaire** | vérifications en attente, et dépendances ouvertes |
| **ouverture du Livre 0** | ce qu'une entrée pourrait dire dès la vérification |

**ET LA BOUCLE DE PRODUCTION NE SE SAUTE PAS.** Le § 11 fixe l'ordre :
brouillon → audit contradictoire → audit factuel → `verifie`. **Sur les quatre
chapitres ci-dessous, un seul a franchi la première marche.**

| chapitre | statut réel | ce qui reste | ouvre le Livre 0 sur |
|---|---|---|---|
| **L1.C08** | `audit_contradictoire` | **audit contradictoire ACQUIS** ; audit factuel à terminer, **17 vérifications** | la contrainte de croissance |
| **L1.C07** | `brouillon` | thèse et architecture à conserver ; **audit contradictoire à conduire**, puis audit factuel — **12 vérifications** | la création monétaire |
| **L1.C31** | `brouillon` | **5 vérifications** seulement, le moins chargé du livre, mais **audit contradictoire à conduire** et **dépendance A35b à maintenir explicitement ouverte** | ce qu'une émission produit |
| **L1.C15** | `audit_contradictoire` | audit contradictoire acquis ; **21 vérifications** | l'essentiel insolvable — voir ci-dessous |

**PREMIÈRE TRANCHE PROPOSÉE : C08, C07, C31, dans cet ordre.** C08 est le plus
avancé — il ne lui manque que l'audit factuel. C07 et C31 sont **en brouillon** :
ils demandent d'abord la confrontation aux objections adverses, et le compter
comme « en attente d'audit factuel » était faux.

### Ce que `verifie` certifie, et ce qu'il ne certifie pas

**La convention le dit deux fois, et je l'avais contredite.** § 1 : *« Un
chapitre `verifie` a des sources contrôlées et une structure cohérente. Rien de
plus. »* § 4 : *« `verifie` ne dit rien de la justesse du raisonnement. Le mot
est choisi pour ne pas suggérer davantage. »*

**Conséquence pour C15, et elle renverse ce que cette matrice disait.**
L'opérationnalisation de l'essentiel insolvable **ne bloque pas la vérification
documentaire du chapitre**. C15 peut passer à `verifie` s'il établit seulement :

1. la **définition prospective** du concept ;
2. ses **quatre conditions** cumulatives ;
3. sa **distinction** d'avec les catégories voisines — échec commercial,
   externalité, bien public ;
4. les **conditions de son épreuve** ;
5. et le fait que **son ampleur empirique reste inconnue**.

**Ce que `OPERATIONNALISATION-INSOLVABLE` bloque est une conclusion, pas un
statut** : l'affirmation que le phénomène est **assez important pour justifier
NEMO IMS**. Un chapitre qui expose honnêtement cette incertitude est vérifiable ;
un chapitre qui la masque ne l'est pas, quel que soit son sourçage.

**Et cela sépare deux questions du Livre 0 qu'il ne faut pas confondre.**

| question | possible quand |
|---|---|
| *« Qu'est-ce que l'essentiel insolvable ? »* | **dès C15 vérifié**, en présentant le concept comme **prospectif** |
| *« L'essentiel insolvable est-il un phénomène assez important pour justifier NEMO IMS ? »* | **impossible avant l'épreuve empirique** |

**TRANCHE SUIVANTE — le diagnostic**, déjà en audit contradictoire : **C09, C12,
C11, C03**.

**Ce que le passage à `verifie` déclenche.** Chaque chapitre vérifié ouvre ses
entrées de Livre 0, selon § 6. **Une première tranche vérifiée suffirait à ouvrir
la couche de réponse** sur trois **questions structurantes proposées** : la
création monétaire, la contrainte de croissance, et ce qu'une émission produit.

**« Structurantes proposées » et non « les plus demandées » : le corpus ne
dispose d'aucune donnée d'usage.** Ces trois questions sont retenues parce
qu'elles commandent la lecture du reste, ce qui est un jugement du corpus **(I)**.
**Les priorités du Livre 0 devront être confrontées** aux recherches des
visiteurs, aux journaux de questions posées à l'assistant, ou à une étude
d'usage — **aucun de ces trois instruments n'existe aujourd'hui**.

---

## 6. Ampleur de la refonte — estimation motivée

**Verdict : véritable deuxième édition.** Ni révision limitée, ni réécriture
partielle.

**Ce qui l'établit, par les nombres.**

- **12 chapitres sur 31 sont à réécrire substantiellement** — soit
  **39 %**, et ils portent **la quasi-totalité de la seconde partie**
  (C17 à C29, sauf C23 et C25) plus l'ouverture C01.
- **1 chapitre est à retirer ou sortir du livre** (C30).
- **2 chapitres sont à fusionner** dans le texte de la seconde édition (C13+C14),
  **sans qu'aucun matricule disparaisse du corpus**.
- **2 chapitres réellement nouveaux** sont nécessaires — gouvernance, clôture.
- **1 titre de chapitre est réfuté par son propre contenu** (C24).
- **4 arbitrages constitutifs** — A44, A45, A46, A47 — **ont été pris après la
  rédaction du livre**, et trois d'entre eux touchent l'institution même.
- **1 abandon majeur** : la libre circulation inconditionnelle des capitaux.
- **La contradiction interne la plus répandue** — contrainte arithmétique vs
  conditionnelle — traverse au moins trois chapitres.

**Ce qui empêche de conclure « révision limitée ».** La première partie
tiendrait, moyennant du sourçage. **La seconde ne tient pas** : l'institution a
changé de forme (A46), le régime de change a changé de solution (A32), la
promesse a été restreinte (A44), le traitement des soldes persistants a été
orienté (`COMPENSATION-SYMETRIQUE`) et le soutien aux importations essentielles
a reçu ses deux guichets (A45). Un lecteur de 2026 ne reconnaîtrait pas le
dispositif.

**Ce qui empêche de conclure « réécriture partielle ».** L'ordre lui-même doit
changer : **C31 doit passer de la fin au milieu**, parce que la distinction
pouvoir d'achat / ressources réelles commande la lecture de tout ce qui suit.
Déplacer la clé de lecture n'est pas une retouche.

**Ce que la seconde édition ne doit PAS faire.** Absorber les vingt-six livres.
Le corpus a produit 436 renvois entrants vers le Livre 1 ; **les verser dans le
texte le rendrait illisible et lui ferait perdre sa fonction**, qui est de porter
la démonstration générale.

**Estimation de charge, à titre indicatif et sans valeur d'engagement.** Le
Livre 1 fait **615 505 signes**. Les 12 chapitres à réécrire en représentent
**310 755**, soit **50 % du volume**.

**LE DÉCOMPTE COMPLET DES TRENTE ET UN.**

| verdict | nombre | chapitres |
|---|---|---|
| conserver, sous réserve de l'audit factuel | **11** | C02, C03, C07, C08, C09, C12, C15, C16, C23, C25, C31 |
| corriger localement | **5** | C04, C05, C06, C10, C11 |
| réécrire substantiellement | **12** | C01, C17, C18, C19, C20, C21, C22, C24, C26, C27, C28, C29 |
| fusionner dans le texte de la 2ᵉ édition | **2** | C13, C14 |
| retirer du livre | **1** | C30 |
| **total** | **31** | |
| chapitres réellement nouveaux | **2** | gouvernance, clôture |

**Chapitres du texte de la seconde édition** : 31 − 1 retiré − 1 par fusion + 2
nouveaux = **31**. Le volume change plus que le nombre.

---

## 7. Le futur Livre 0 — questions candidates, aucune réponse

**Aucune entrée n'est rédigée. Aucune ne peut l'être : zéro chapitre est
`verifie`.**

**Questions candidates, par chapitre susceptible d'être conservé.**

**Ces questions sont PROPOSÉES par le corpus, non observées chez des
lecteurs.** Aucune donnée d'usage du site n'est disponible ; l'ordre dans lequel
elles seront traitées devra être revu quand elle le sera.

| chapitre | question structurante proposée |
|---|---|
| C07 | Les banques prêtent-elles l'épargne des déposants ? |
| C08 | La croissance est-elle mathématiquement obligatoire ? |
| C15 | Qu'est-ce que l'essentiel insolvable ? **— en le présentant comme prospectif** |
| C31 | Créer de la monnaie crée-t-il des ressources réelles ? |
| C03 | Le découplage absolu est-il observé quelque part ? |
| C05 | Qu'est-ce que la monnaie ? |
| C09 | Qu'est-ce que l'architecture invisible ? |
| C10 | Wörgl, le WIR, les monnaies locales : qu'ont-ils prouvé ? |
| C11 | Pourquoi le crédit ne finance-t-il pas la régénération ? |
| C12 | La finance verte peut-elle suffire ? |
| C16 | Qu'est-ce que la bullshitnovation ? |
| C24 | Le dollar peut-il être remplacé par décision ? |
| C25 | Qu'est-ce qui décide d'une réforme monétaire ? |
| C23 | Qu'est-ce que la robustesse coûte ? |
| C02 | Richesse financière et dégradation progressent-elles ensemble ? |
| C04 | Combien de limites planétaires sont franchies ? |
| C06 | Pourquoi les politiques écologiques ne suffisent-elles pas ? |

**ET UNE QUESTION N'EST PAS OUVRABLE, MÊME APRÈS VÉRIFICATION DE C15** : *« L'essentiel insolvable est-il un phénomène assez important pour justifier NEMO IMS ? »* Elle attend l'épreuve empirique, non un statut documentaire.

**Les chapitres à réécrire n'ouvrent aucune question aujourd'hui** : une entrée
de Livre 0 adossée à un chapitre en cours de réécriture serait la « promesse »
que § 6 interdit.

---

## 8. Le flux vers le site — proposé, non développé

```
chapitres vérifiés
      ↓  (§ 6 : une entrée par question, dès qu'un livre est vérifié)
entrées du Livre 0
      ↓  (§ 13 : générateur, non implémenté)
pages HTML et Markdown du corpus
      ↓
index des questions et des concepts
      ↓  (généré, jamais rédigé)
llms.txt
      ↓
assistant du site
```

**Trois règles à tenir, et elles découlent de ce que le corpus a déjà établi.**

**Le `llms.txt` est une projection, jamais une source.** Le rédiger à la main en
ferait une doctrine parallèle non contrôlée par `controle.py`. Il doit être
**généré à partir des contenus vérifiés et renvoyer vers eux**.

**La base de connaissances statique actuelle du widget ne fait pas autorité.**
Elle reflète un état antérieur du livre et du projet — antérieur à A32, A43, A44,
A45, A46, A47. **Elle dira des choses que le corpus a retirées.**

**Le générateur du § 13 n'est pas implémenté**, et c'est le premier verrou
technique du flux. Aucune page, aucun index, aucun `llms.txt` de corpus n'existe
aujourd'hui. Les deux empreintes du § 5 sont calculées et stockées ; le reste est
à écrire.

---

## 9. Ce que cette cartographie n'est pas

**Elle ne réécrit rien.** Aucun chapitre canonique, aucune entrée du Livre 0,
aucune ligne de la convention, du site ou du `llms.txt` n'a été modifiée.

**Elle ne corrige pas les écarts qu'elle relève** — l'écart 30/31, la tension du
Livre 0, l'absence de sources de C01. Elle les signale et propose.

**Elle ne fait autorité sur rien.** Les verdicts qu'elle rassemble sont ceux que
les chapitres du corpus ont déjà rendus, et les décisions qu'elle cite sont
celles de l'auteur. **Là où elle interprète, elle le dit.**

**Et aucun résultat de modèle n'y vaut preuve.** Les programmes de `modeles/`
appliquent des règles ; **un programme qui applique correctement une règle ne
valide jamais cette règle**, et les résultats marqués **(M)** sont donnés pour ce
qu'ils sont : des mesures faites sur des paramètres non calibrés.
