# Registre de passe 2

La passe 1 défriche. Les passes suivantes règlent. Ce fichier tient ce qui a
été **délibérément reporté**, pour que la passe 2 reprenne le travail au lieu
de le refaire — et pour qu'aucune session ne repose une question déjà tranchée.

Fichier de travail, hors schéma du corpus.

## Ce qui n'est pas ici

Les vérifications propres à un chapitre vivent dans son en-tête, sous
`verifications_en_attente`, marquées `COHÉRENCE`. Elles n'ont pas à être
recopiées ici : une liste dupliquée pourrit. Ce registre ne tient que ce qui
n'appartient à aucun chapitre en propre.

Les promesses contractées envers la seconde partie vivent dans
[registre-des-promesses.md](registre-des-promesses.md). Les arbitrages
d'architecture des livres vivent sous « ARBITRAGE REPORTÉ » dans
[corpus/livres.yaml](../corpus/livres.yaml).

---

## 1. Décisions prises en passe 1 — ne pas rouvrir

| Décision | Date | Fondement |
|---|---|---|
| **Nom de l'unité : NEMO Green Allocation (NGA)** — ARBITRÉ le 2026-09-05, remplace « NEMO Green SDR » | 2026-09-04, amendé puis REMPLACÉ le 2026-09-05 | Dépouillement de *L'économie de l'équilibre* : `NGDTS` 0 occurrence, `NGSRD` 0, `NEMO Green SDR` sur 29 pages. Arbitré par JC. **PRÉCISION du même jour** : `NGDTS` est absent du LIVRE mais bien présent dans le CAHIER TECHNIQUE (L2.E09), où il développe « NEMO Green Drawing Rights » — expansion différente encore de celle du script audio (Nominatif, Green, Drawing, Ticket, Special). Il y a donc trois nommages, non deux. L'arbitrage tient pour le corpus, mais la divergence livre / cahier reste à traiter au Livre 2. **AMENDEMENT DU 2026-09-05, arbitré par JC.** L'abréviation est autorisée et c'est **NGSDR** ; `NGSRD`, qui figurait ici et dans deux passages de ce fichier, était une **coquille** — les deux dernières lettres inversées — et elle a été corrigée. L'arbitrage d'hier disait « jamais NGSRD » : il rejetait donc une graphie fautive, et l'amendement ne le contredit pas, il le complète. **PRÉCISION QUI ENGAGE LE CORPUS** — dépouillement du 2026-09-05 : le LIVRE écrit « NEMO Green SDR » 47 fois et **n'abrège jamais** ; le CAHIER écrit « NGDTS » 46 fois et **n'écrit jamais** « NEMO Green SDR ». Les deux sources sont **disjointes** sur le nommage, et **NGSDR ne figure dans aucune des deux**. C'est donc une forme PROPRE AU CORPUS, adoptée pour fixer un lexique que les sources ne fixent pas — légitime, mais à déclarer une fois pour toutes plutôt qu'à laisser croire qu'elle est reprise. **Point ouvert mineur** : « Special Drawing » n'apparaît nulle part, ni dans le livre ni dans le cahier. L'expansion de « SDR » est donc supposée par analogie avec les droits de tirage spéciaux du Fonds ; le corpus devrait l'énoncer explicitement au Livre 11. **REMPLACEMENT DU 2026-09-05, arbitré par JC.** L'unité s'appelle désormais **NEMO Green Allocation**, abrégée **NGA**. Motif, établi et non cosmétique : « SDR » ne nomme pas une finalité mais un GENRE d'instrument, défini par quatre propriétés — allocation au prorata des quotes-parts, détention en réserve, intérêt sur les positions nettes, cessibilité entre participants officiels. **L'unité de NEMO IMS diffère sur les quatre.** Le préfixe « Green » modifiait la finalité, pas le genre. S'y ajoutait un effet d'ordre de lecture défavorable : le nom appelait d'abord le critère de règlement, que l'unité échoue (L1.C24 § 4), avant le critère de dette, qu'elle réussit (L1.C22 § 4 — l'allocation de droits de tirage est comptée au passif sous BPM6, la sienne n'a ni principal ni intérêt à saisir). **Écarté en chemin : « NEMO Green Regenerative Certificate »**, qui corrigeait le premier défaut en en créant un pire — « certificat » est le mot de la famille des compensations, dont le corpus s'est extrait en abandonnant l'additionnalité contrefactuelle (L1.C18), et il écrase la distinction d'E09 entre le certificat de qualification, porté à l'ACTIF du GES, et l'unité émise à son PASSIF. **Pourquoi « allocation » :** c'est descriptivement exact — l'unité ne circule jamais, elle vit entre le GES et les banques centrales nationales comme actif transitoire —, le mot garde la filiation sans revendiquer le genre, et il **survit aux deux branches de la bifurcation A/B** : allocation gagée sur une créance si le reflux s'annule, allocation budgétaire s'il alimente le GES. **Portée de la migration :** la voix du corpus est migrée ; toute citation verbatim garde les mots de sa source, le livre écrivant « NEMO Green SDR » 47 fois et le Cahier « NGDTS » 46 fois. |
| **Le numéro de livre est un matricule**, jamais un rang | 2026-09-04 | Convention § 3. Réservation autorisée, matricule brûlé même si le livre n'est pas écrit. |
| **Livre 0 réalisé en fin de premières passes** | 2026-09-04 | Interface entre le `llms.txt` et le contenu du site. Ne peut pas s'écrire tant que les chapitres qu'il indexe bougent. |
| **Livre 5 : « fenêtre de crise »**, non « effondrement » ni « révolution » | 2026-09-04 | Formulation du plan directeur. Un corpus qui paraîtrait compter sur l'effondrement perdrait la recevabilité qu'il cherche. |
| **Licence CC-BY-SA-4.0** | 2026-09-03 | Convention § 14. |
| **Les rapports d'audit et de recherche restent HORS DÉPÔT** | 2026-09-04 | Arbitré par JC. Les trente rapports produits par des modèles tiers sont archivés sur le Drive (`Corpus GPT / SAUVEGARDE CORPUS / audits-et-recherches`) et **ne sont pas versionnés**. Motif : le dépôt GitHub est public et sert debunkonomy.org ; y verser ces rapports publierait trente documents listant les erreurs corrigées et les objections non résolues avant tout arbitrage. **Conséquence à assumer :** les pièces qui justifient les corrections du corpus vivent hors de son historique — quand un chapitre dit « corrigé après audit », la preuve n'est pas dans le dépôt. Une `.gitignore` garde contre une réintroduction accidentelle. |

## 2. Corrections appliquées, à propager

- **« Extinction élégante » — cadrage écarté le 2026-09-04.** Il a été proposé
  de présenter le rétrécissement de l'assiette dégénérative comme la preuve du
  succès, et l'extinction du dispositif comme une élégance de conception, à
  condition qu'elle soit voulue et écrite. **Le corpus l'écarte sur ses propres
  constats** : le dispositif ne s'éteint que d'un côté. Le reflux décroît avec
  l'assiette, l'émission régénérative n'a aucune raison de décroître et a
  vocation à croître (L1.C21 § 6). Ce qui en résulte n'est pas une extinction
  mais un déséquilibre orienté — la configuration même que Rueff décrit. Une
  extinction assumée reste possible, mais elle suppose de plafonner l'émission
  par le reflux réalisé, donc de renoncer à la dimensionner sur les besoins
  régénératifs : c'est une autre proposition, non une version élégante de
  celle-ci. Ne pas réintroduire ce cadrage.

Un chapitre postérieur a corrigé un chapitre antérieur. Le chapitre corrigé
n'a pas encore été repris.

| Corrigé | Corrigé par | Objet |
|---|---|---|
| L1.C09 § 2, L1.C11 § 2 | L1.C15 § 1 | Le canal budgétaire n'est pas seulement « en aval » du filtre : l'emprunt souverain crée bien de la monnaie, mais déplace le filtre sur l'emprunteur souverain. |
| L1.C12 § 5 | L1.C13 § 2 | « La stabilité des prix ferme la voie de l'érosion » est trop fort : les issues sont transitoires, coûteuses et combattues, non fermées. |
| L1.C19 § 4 | Livre, chapitre 9 | Le § 4 établit qu'il n'y a qu'une monnaie sans en donner la raison. Le livre la donne : deux monnaies impliqueraient deux comptabilités, et le reflux de l'une sur l'autre serait inapplicable. Ce n'est donc pas une atténuation de la thèse mais **la condition de possibilité du reflux**. À porter dans le texte. |

## 3. Tensions entre le corpus et le livre

À trancher, pas à ignorer. Le livre fait autorité sur le contenu ; le corpus
fait autorité sur ce qu'il a lui-même établi et sourcé.

**L'équation quantitative — TRANCHÉE le 2026-09-04 par l'auteur.**

L1.C12 a **abandonné** `MV = PT` comme argument, après avoir constaté que M2 a
triplé pendant que la vitesse était divisée par deux ; la thèse du Jevons
monétaire a été reconstruite sur l'additivité du crédit et la contrainte de
croissance. Le chapitre 9 du livre, lui, s'appuie sur l'équation de Fisher et
propose un « PT = MV transformé ».

Arbitrage de JC : **l'équation de Fisher devient dynamique avec les dispositifs de reflux transactionnels sur
les transactions — on retire de la monnaie là où elle sert des projets
dégénératifs.** Les deux usages ne se contredisent pas, et voici pourquoi.

C12 écarte l'équation comme **preuve causale** : « plus de monnaie, donc plus
d'extraction » est réfuté par les séries. Le livre s'en sert comme **cadre de
conception**, ce qui est un autre usage et un usage licite. Une identité
comptable ne démontre rien par elle-même, mais elle dit où agir : si le
prélèvement porte sur les transactions et qu'il est pondéré par l'impact, la
destruction monétaire devient une fonction du flux lui-même, et non un montant
fixé de l'extérieur. La masse cesse d'être un stock qu'on pilote pour devenir
un flux dont le taux d'extinction dépend de ce que la monnaie sert à faire.
C'est ce que le livre nomme « monnaie-flux plutôt que monnaie-stock ».

Ce que cette résolution ne dit pas encore, et que L1.C20 ou L1.C21 devra dire :

- Un reflux transactionnel **réduit V** — elle renchérit l'échange, c'est son
  objet. À masse égale, une vitesse moindre soutient moins de transactions. Le
  livre en est conscient : c'est la raison d'être du second ressort, le
  demurrage sur encaisses oisives, qui pousse en sens inverse. Mais l'effet net
  sur `PT` dépend alors du calibrage relatif des deux ressorts, et ce calibrage
  est exactement P18.
- L'identité vaut pour les transactions **totales**, non pour leur composition.
  Retirer de la monnaie sur les transactions dégénératives modifie les prix
  relatifs avant d'agir sur le niveau général — c'est l'effet de premier
  receveur relevé en L1.C19 § 6 (P24), pris par l'autre bout.

Le chapitre qui exposera les dispositifs de reflux transactionnels devra donc porter les deux énoncés : que
l'équation est employée comme cadre de conception et non comme preuve, et que
son emploi dynamique déplace la question vers le calibrage plutôt qu'il ne la
résout.

**Périmètre entre le Livre 1 et le Livre 2.** Le chapitre 9 du livre
(« Recommandations macroprudentielles NEMO IMS ») est la matière du **Livre 2**
selon le plan directeur. Mais il porte aussi la matière de **L1.C20**
(émission sans dette) et de **L1.C21** (reflux collectif) : régulation à deux ressorts,
reflux transactionnel, demurrage sur encaisses oisives, réponse à Rueff et à
Keynes, blocage de la fuite par le « NEMO SWIFT ». Il faut décider ce que les
chapitres du Livre 1 exposent et ce qu'ils renvoient au Livre 2, faute de quoi
les deux livres diront la même chose — ou se contrediront.

## 3 bis. « Fonte » désigne deux choses différentes — à trancher avant L1.C21

Signalé le 2026-09-04, à la lecture du chapitre 9.

`vocabulaire.yaml` définit `monnaie_fondante` comme la monnaie de Silvio
Gesell : celle qui perd une fraction de sa valeur nominale si elle n'est pas
dépensée, sauf paiement d'un droit de conservation. C'est une taxe sur la
**détention**.

Or le livre emploie « fonte transactionnelle » pour un prélèvement sur
l'**échange** — 1 % par défaut, modulé jusqu'à plus de 20 % pour les activités
dégénératives et 0 % pour les régénératives — et réserve le mot « demurrage »
au dispositif de Gesell. Le même mot « fonte » couvre donc deux instruments de
sens opposé.

Et le livre lui-même met en garde contre exactement cette confusion : « On
invoque souvent Silvio Gesell pour justifier une taxe sur les transactions,
alors que sa monnaie fondante frappait précisément l'inverse, à savoir la
rétention des encaisses oisives. Une taxe sur l'échange freine l'échange ; une
taxe sur la détention l'accélère. Les confondre revient à se priver de l'un des
deux effets. »

Conséquence pour le corpus : l'entrée `monnaie_fondante` est correcte pour
Gesell et **ne doit pas** servir à désigner le reflux transactionnel. Il faut
soit deux entrées distinctes, soit un renommage. À trancher avant L1.C21, qui
expose les deux ressorts — un chapitre qui emploierait le même terme pour les
deux instruments serait illisible, et un fragment extrait le serait davantage.

Cette distinction lève par ailleurs la première réserve du § 3 ci-dessus : le
livre a déjà vu que le reflux transactionnel réduit la vitesse de circulation,
et c'est précisément pourquoi il lui adjoint un second ressort de sens inverse.
La question ne porte donc plus sur l'existence de l'effet, mais sur le calibrage
relatif des deux instruments — P18, une fois de plus.

## 3 ter. Le Cahier Technique L2.E09 résout ce que le Livre 1 a laissé ouvert

Lecture du 2026-09-04, sur invitation de l'auteur. **Ces éléments ne sont pas
encore dans les chapitres.** Ils y entreront en passe 2, et ils obligent à
corriger L1.C20 sur un point de fait.

### ERREUR à corriger dans L1.C20 — qui émet

L1.C20 § 3 et § 4 attribuent l'émission à la banque centrale. **C'est faux
selon le Cahier.** Les rôles sont séparés :

> « Les banques centrales nationales ne créent pas de monnaie néguentropique
> ex nihilo. Elles exécutent des droits de tirage émis par le GES. »

Le GES émet, libellé en unité NES du NEMO Exchange Standard, et fonctionne à ce
niveau « comme une banque centrale néguentropique internationale ». La banque
centrale nationale reçoit le droit de tirage et procède à l'exécution technique.
Cette séparation change la lecture de l'obstacle des art. 123 et 130 : ce n'est
pas une banque centrale qui émet sur instruction, c'est une institution
internationale qui émet et une banque centrale qui exécute une conversion à
taux fixe. L'obstacle ne disparaît pas, il se déplace.

### La contrepartie à l'actif existe — et P23 est résolue

C'est la trouvaille majeure. L1.C19 et L1.C20 concluaient qu'il n'y a rien à
porter à l'actif. Le Cahier donne une **contrepartie double** au niveau du GES :

- un **certificat de qualification régénérative**, qui qualifie l'émission au
  présent ;
- une **créance sur les dispositifs de reflux transactionnels futures**, qui assure la clôture comptable du
  cycle dans le temps.

La seconde est un actif au sens strict — ressource contrôlée, issue d'un
événement passé, dont des avantages économiques futurs sont attendus. Elle
satisfait donc le critère que L1.C19 § 6 déclarait insatisfait, et elle fournit
à la « valeur nette globale » de Buiter (P26) la contribution positive que
L1.C20 § 4 disait manquante : la valeur actualisée des dispositifs de reflux transactionnels futures joue le
rôle du seigneuriage.

Au niveau national, les droits de tirage entrent à l'actif comme **actif
transitoire**, la monnaie nationale sort au passif ; à mesure que les dispositifs de reflux transactionnels
refluent, la banque centrale renvoie proportionnellement les droits au GES.

**Le reflux est donc à deux étages** : des transactions vers les banques
centrales nationales, puis des banques centrales vers le GES, où la créance sur
dispositifs de reflux transactionnels futures s'éteint. C'est la réponse à P23 — l'asymétrie relevée en
L1.C19 § 4. Le cycle boucle là où il a commencé.

### La nature de la dette — réponse à P3

> « une dette collectivisée sur activités dégénératives — remboursée non pas
> par un débiteur identifié, mais par l'ensemble des acteurs économiques dont
> les transactions restent dégradantes, au prorata de l'impact biosphérique et
> social de leurs échanges. »

C'est la définition du reflux collectif que le corpus cherchait depuis L1.C08.

### CARE-TDL : la tension est levée par l'auteur

Le Cahier positionne explicitement les deux : « CARE-TDL diagnostique, NEMO IMS
remédie. » Instrument de mesure d'un côté, instrument d'action de l'autre,
complémentaires par fonction et non concurrents — avec l'image de la
météorologie qui mesure la pluie sans disposer du bouton pour l'arrêter. Cela
clôt ce que L1.C19 § 6 et L1.C20 § 4 traitaient comme une alternative. Le
Cahier nomme aussi **Clément Feger** aux côtés de Richard et Rambaud.

### La dette ancienne

NEMO IMS n'organise pas la répudiation : les flux nouveaux nés des activités
régénératives circulent dans le circuit Yang et alimentent le remboursement des
crédits privés et les recettes fiscales — sans provenir d'une intensification
extractive. À vérifier, mais c'est une réponse directe à P11 et au nœud gordien
de L1.C13.

### Positionnement — la clé pour le § 5 ci-dessous

L'épisode s'ouvre sur l'appel publié dans *Le Monde* le 5 février 2021 par cent
cinquante économistes européens demandant l'annulation des dettes publiques
détenues par la BCE — signataires cités : Aglietta, Piketty, Cahen, Chesnais,
**Dufrêne, Grandjean**, Bourguinat, Théret. C'est là que se joue le
positionnement par rapport à la littérature la plus proche, signalé au § 5.

## 3 quater. Le Cahier Technique est intégralement lisible — inventaire

Constat du 2026-09-04, en défrichant L1.C22. Les **douze épisodes** du Cahier
Technique sont disponibles sous forme de texte extrait, en un seul fichier, sur
le poste de l'auteur :

    Documents/Codex/2026-08-07/bi/work/macroprudential_annexes.txt

Le livre entier l'est aussi, dans le même dossier (`book_extracted.txt`, pagination
identique à celle de l'ouvrage imprimé). Les chapitres L1.C17 à L1.C21 ont été
défrichés sans que cette ressource soit exploitée au-delà de L2.E09. **En passe 2,
lire les onze autres épisodes avant de rouvrir un chapitre.**

Titres relevés :

| # | Épisode |
|---|---|
| E01 | Le principe d'emboîtement systémique |
| E02 | De la stabilité financière à la robustesse systémique |
| E03 | Du contrôle quantitatif du crédit au contrôle qualitatif |
| E04 | Des risques financiers aux risques planétaires |
| E05 | De la neutralité financière à l'allocation stratégique du crédit |
| E06 | Les mécanismes bancaires du contrôle monétaire |
| E07 | Des bulles financières aux bulles écologiques |
| E08 | De la résilience bancaire à la résilience des territoires |
| E09 | De la gestion de la dette au reflux monétaire (§ 3 ter ci-dessus) |
| E10 | De la surveillance bancaire à la gouvernance des biens communs |
| E11 | De la coopération entre banques centrales à la gouvernance monétaire mondiale |
| E12 | De la macroprudence défensive à la macroprudence régénérative |

### AVERTISSEMENT — le Cahier porte des états antérieurs

**E10 décrit le GES en cinq collèges** délibérant conjointement — scientifique,
économique, sociétés civiles, territoires, générations futures. C'est la
conception que le chapitre 7 du livre déclare intenable et remplace par quatre
chambres séparées (L1.C18 § 3). La même précaution vaut pour tout le Cahier :
**lire le chapitre du livre avant d'en tirer quoi que ce soit.** E10 emploie
aussi le sigle « NGDTS ». Le corpus écrit NEMO Green Allocation (NGA)
depuis l'arbitrage du 2026-09-05.

### Ce que le Cahier apporte, et où le porter

- **E10** donne la référence à Ostrom que le livre ne fait pas, et nomme des
  « indicateurs de gouvernance polycentrique effective ». Employé en L1.C22 § 2.
- **E11** expose le NEMO Exchange Standard comme « pur nombre notionnel » servant
  de référentiel de change, et NEMO SWIFT. Matière des chapitres à venir.
- **E12** donne le tableau de bord en six familles d'indicateurs, et l'appel de
  l'auteur à un *think tank* dont la première mission serait « la formulation
  comptable définitive de la contrepartie des NGDTS » — c'est-à-dire la question
  laissée ouverte en L1.C19 § 6 et L1.C20 § 4. **L'auteur la déclare lui-même non
  résolue.** Le corpus doit le citer plutôt que de trancher à sa place.

### Repère de numérotation

Le Cahier renvoie à la série principale par numéro d'épisode, et ces renvois
concordent avec les chapitres du corpus : 18 = GES, 21 = dispositifs de reflux transactionnels
transactionnelles, 26 = NEMO Exchange Standard et privilège exorbitant,
27 = NEMO SWIFT, 28 = tableau de bord multidimensionnel, 29 = contrepartie
comptable. **Utile pour vérifier les intitulés de L1.C23 à L1.C30 contre le plan
directeur** — cette vérification n'a pas été faite pour L1.C22, dont l'intitulé
« Financer les communs » repose sur la note déposée en L1.C17 et sur la page
`nemo-ims/financer-les-communs.html` du site.

### Arbitrage rendu nécessaire par L1.C22 § 4

Qui porte l'écriture durable de la contrepartie ? Le livre attribue l'émission
aux banques centrales nationales (chapitre 7, « la création de monnaie sans dette
[...] serait exclusivement le fait des banques centrales ») ; le Cahier E09 la
réserve au GES, les banques centrales n'exécutant que des droits de tirage
(§ 3 ter). L1.C22 § 4 enregistre la divergence sans la trancher. **À trancher en
passe 2, avant toute correction de L1.C20.**

## 4. Noms provisoires à confirmer

Cinq entrées de `vocabulaire.yaml` portent la mention « nom provisoire, à
confirmer en passe 2 » : `bullshitnovation`, `sisyphe_economique`,
`noeud_gordien`, `jevons_monetaire`, `qualification_regenerative`. Chacune est
le nom de l'auteur, du livre ou du corpus, retenu faute de mieux. La passe 2
décide de les garder ou de les renommer — en sachant qu'un renommage n'a aucun
coût technique, les concepts ne portant pas d'URL.

## 5. À vérifier sur les sources

- **Appels de notes du livre, possible décalage d’une unité.** Dans le texte
  extrait de l’ODT, l’épigraphe de Rocard porte l’appel (68) alors que la note
  67 est sa notice biographique et la note 68 celle de Bretton Woods ; le
  décalage se poursuit sur Jamaïque et Triffin. **Peut être un artefact
  d’extraction** et non une erreur du livre composé. À vérifier sur le PDF de
  composition avant toute correction. Relevé le 2026-09-04 en écrivant L1.C25 ;
  aucun effet sur le fond.

- **Positionnement du livre — FAIT le 2026-09-04, à porter dans les chapitres.**
  Le test d'antériorité (F5) est clos : aucune proposition publiée ne combine
  émission sans dette et destruction calibrée. Mais le corpus doit désormais
  porter ce positionnement dans son texte, et il n'y est nulle part. Trois
  énoncés à intégrer, probablement en L1.C20 § 1 et L1.C21 § 6 :
  1. Les propositions voisines émettent sans dette et **assument
     l'irréversibilité** — Dufrêne et Grandjean, Couppey-Soubeyran et
     l'Institut Veblen. L'apport de NEMO est le mécanisme d'extinction.
  2. Elles n'ont pas omis ce que NEMO propose : elles l'ont **écarté**. Elles
     découplent le retrait monétaire de la fiscalité ciblée, et abandonnent le
     calcul d'empreinte transactionnelle au profit d'un ciblage par les
     intrants. Le corpus a redécouvert leurs motifs sans les connaître.
  3. **L'échelle ne tranche pas — argument RÉTRACTÉ le 2026-09-04.** Une
     version antérieure de ce registre affirmait ici que les voisins chiffrent
     cent à cent cinquante milliards par an pour la zone euro contre un besoin
     de sept cent cinquante à huit cents, soit un facteur trois à quatre. Un
     second rapport documentaire donne des chiffres tout autres — cent
     milliards pour la seule France, trois cents à quatre cents pour la zone
     euro chez Dufrêne et Grandjean ; deux à trois pour cent du produit
     européen chez Couppey-Soubeyran et ses coauteurs. Si ces chiffres sont les
     bons, les voisins proposent **déjà à l'échelle du besoin** et assument
     l'irréversibilité à cette échelle-là. Les deux rapports se contredisent et
     aucun n'a été vérifié sur l'ouvrage : **ne rien porter dans un chapitre
     tant que le chiffre n'est pas lu dans *Une monnaie écologique*.** Voir
     falsification.md, F5, seconde passe, point 4.
  Voir protocoles/falsification.md, F5, seconde passe.
- **L'impératif de croissance — DEUX THÈSES LUES le 2026-09-04.** JC a
  communiqué les thèses d'Augustin Sersiron (Paris 1, 2021) et d'Édouard
  Cottin-Euziol (Limoges, 2013). Elles portent sur la question laissée ouverte
  en L1.C23 § 4 et sont désormais dans le chapitre comme [S18] et [S19].

  **Sersiron — LUE, exploitée.** Elle donne au corpus une TROISIÈME position,
  distincte de Jackson-Victor (pas d'impératif) et de Binswanger (impératif issu
  du profit) : une contradiction gérée par un mode de régulation jusqu'à ce
  qu'elle ne le soit plus. C'est la position que le corpus avait retenue par
  prudence, et il la découvre défendue devant un jury comprenant Orléan et
  Giraud. Elle apporte deux choses qu'il n'avait pas : le mécanisme du report
  (la baisse continue des taux, jusqu'au plancher), et l'inversion — le fardeau
  de la dette pousse les agents à **sous-emprunter** par rapport aux conditions
  de la stabilité macroéconomique, ce qui explique mieux la décennie de taux
  nuls que l'exigence de croissance.

  **Cottin-Euziol — PARTIELLEMENT LUE, à rouvrir.** L'extraction automatique
  s'arrête au chapitre 2 ; or l'apport est aux chapitres 3 (« Les conditions de
  remboursement des crédits bancaires ayant financé les investissements
  passés ») et 5 (modèle de Domar avec crédits sur plusieurs périodes). **C'est
  la pièce manquante du débat**, puisqu'elle instruit précisément ce que Jackson
  et Victor tranchent par la négative. À obtenir en texte lisible, ou à lire
  dans le PDF.

  **Effet sur F5 :** la thèse de Sersiron conclut à un régime d'émission
  exogène inspiré du 100% Money. Elle rejoint la ligne « Plan de Chicago,
  Positive Money » du tableau de la seconde passe — émission sans dette oui,
  destruction liée à un critère écologique non. F5 est inchangée. Voir
  protocoles/falsification.md.

- **Tucker, critère DC5.** Deux rapports documentaires le situent
  différemment — chapitre 4, p. 107-108 pour l'un, p. 569 pour l'autre. Ne
  citer aucune page tant que l'ouvrage n'est pas ouvert.
- **Magnitudes de Felsenthal et Machover.** Les pourcentages avancés sur le
  transfert de pouvoir de vote de Nice à Lisbonne ne sont pas confirmés et ne
  figurent dans aucun chapitre. Le mécanisme et le sens de l'effet, eux, sont
  établis (L1.C18 § 4).

## 6. Règle de méthode acquise en passe 1

**Lire le chapitre du livre avant de convertir le texte source.** Les fichiers
d'adaptation contiennent des états antérieurs de la pensée : L1.C18 a d'abord
été défriché sur un dispositif que le livre qualifie lui-même de « conception
initiale » intenable et qu'il a remplacé. Le livre fait autorité ; le script
est une source seconde, utile pour ce qu'il ajoute, jamais pour ce qu'il
contredit.

## 7. Arbitrages de corpus à rendre — décisions de l'auteur

À distinguer des promesses tenues dans `registre-des-promesses.md` : celles-ci
sont des objections adressées à la thèse. Ce qui suit porte sur le corpus
lui-même, et aucune recherche documentaire ne les fermera.

### A1 — CLOS le 2026-09-04 : la numérotation du Livre 1 est vérifiée

Le plan directeur a été ouvert (feuille « PLAN DIRECTEUR — CORPUS GPT —
Debunk'Onomy », Drive, onglet « LIVRES ADOPTÉS ET LIVRES CANDIDATS »).
**Les vingt-deux chapitres défrichés correspondent exactement au plan, rang et
intitulé.** Le doute est levé : « Financer les communs » est bien le chapitre 22.

Les huit rangs restants du Livre 1 sont donc connus, et ils concordent avec les
renvois du Cahier Technique à la série principale — ce qui les confirme une
seconde fois :

| Rang | Intitulé au plan directeur | Concordance Cahier |
|---|---|---|
| C23 | L'économie de la robustesse | — |
| C24 | Pourquoi le dollar ne peut pas durer | — |
| C25 | Histoire des systèmes monétaires internationaux | — |
| C26 | Le NEMO Exchange Standard | E11 : « le NES, présenté à l'épisode 26 » |
| C27 | Une économie mondiale coopérative — NEMO SWIFT | E11 : « présentée à l'épisode 27 » |
| C28 | Au-delà du PIB | E10 et E12 : tableau de bord, « épisode 28 » |
| C29 | Vision globale et chantiers ouverts | E12 : contrepartie comptable, « épisode 29 » |
| C30 | Imagine l'année 2100 | — |

Tous portent au plan le statut « Acquis — conversion corpus requise ».

**Conséquence de méthode :** le plan directeur devait être consulté dès le
premier chapitre de cette série, et il ne l'a pas été — les rangs C17 à C22 ont
été défrichés sur des indices convergents plutôt que sur la source qui fait
autorité. Le résultat s'est trouvé exact, ce qui ne rend pas la méthode bonne.
**Vérifier le plan avant d'ouvrir un chapitre**, au même titre qu'on lit le
chapitre du livre avant de convertir un texte source (§ 6).

### A2 — CLOS le 2026-09-05 : une coalition, et non l'un ou l'autre

**Arbitrage de l'auteur, après lecture de L11.C01.** La question était mal
posée par le corpus, qui l'avait construite en alternative. La réponse est une
**troisième voie** : « NEMO IMS prévoit une grande coalition entre le GAÏA
Economic Symposium et les banques centrales du monde entier ». Le Symposium
émet les NEMO Green Allocation au titre des activités qu'il définit ; les
banques centrales les **convertissent** en monnaie de banque centrale à
finalités extra-financières et tiennent une **comptabilité en miroir**.

Deux émissions à deux étages, donc, et non une émission disputée entre deux
candidats. Le corpus enregistre au passage que l'appellation retenue le même
jour — « monnaie de banque centrale à finalités extra-financières » — **fixe
cette architecture dans le nom** : elle affirme que ce qui circule est de la
monnaie de banque centrale nationale, ce qui est exact sous la coalition.

Voir L11.C01 § 7 pour les conséquences, et l'entrée suivante pour la
bifurcation reflux/destruction, tranchée le même jour.

### A2 bis — CLOS le 2026-09-05 : le reflux est retenu, non annulé

**Arbitrage de l'auteur.** « La question de savoir si le GES peut capter
(accumuler) plus d'avoirs en comptabilités de monnaie nationales qu'elle n'a
émis de NGA est **mathématiquement oui**. » Accumuler au-delà de l'émission est
précisément ce qu'une extinction par annulation interdit : le reflux **parvient
au Symposium et y demeure**.

Conséquences enregistrées en L11.C01 § 7. Trois comptent pour la suite du
corpus. La contrepartie comptable est assainie et P55 change de nature. **En
revanche l'érosion de l'assiette s'aggrave** : elle tarissait un actif, elle
tarit désormais une recette, et un financement privé de recette s'arrête
aussitôt — le « mathématiquement oui » est exact, le « durablement oui » reste
F1. Et un embranchement s'ouvre à l'intérieur de la décision : **que fait le
Symposium de ce qu'il accumule ?** Dépenser, conserver ou redistribuer donnent
trois dispositifs différents, et le statut « sans dette » de l'émission dépend
de la réponse.

### A2 ter — ANCIEN ÉNONCÉ, conservé pour mémoire : qui émet, le GES ou les banques centrales nationales

Le livre attribue l'émission aux banques centrales ; le Cahier E09 la réserve
au GES, les banques centrales n'exécutant que des droits de tirage (§ 3 ter).
L1.C22 § 4 enregistre la divergence sans la trancher, et L1.C20 § 3-4 suit
encore la version du livre. **À trancher avant toute correction de L1.C20**,
car l'obstacle des articles 123 et 130 se lit différemment selon la réponse.

### A3 — La polysémie de « fonte »

Voir § 3 bis. Décision de vocabulaire, donc non reportable au-delà de la
première publication (convention § 9 : renommer un concept est une migration
scriptée).

### A4 — Centralisation ou polycentricité — RELEVÉ EN PRIORITÉ le 2026-09-04

**ENJEU RELEVÉ UNE SECONDE FOIS le 2026-09-04, en défrichant L1.C27 § 6.**
Cet arbitrage était posé comme une question d'efficacité allocative : un barème
mondial unique oriente-t-il l'effort là où il produit le plus (P19b, P25, F3).
Il est davantage. En faisant du financement régénératif l'instrument de
rééquilibrage des économies nationales, et la parité de change étant fixe donc
fermée comme canal d'ajustement, **le barème voté par l'Assemblée des Communs
déterminerait la balance des paiements de chaque pays membre.** L'arbitrage
décide donc de la souveraineté économique des membres, et non plus seulement
de la qualité de l'allocation. Voir P52.

Option de conception enregistrée en L1.C22 § 2 et en P19b, à partir de la
littérature des communs. Elle abaisse l'objection de la connaissance dispersée
et relève celle de la capture locale.

**Le défrichage de L1.C23 change le statut de cet arbitrage.** La même objection
est désormais arrivée par **trois traditions sans rapport entre elles** :

1. la gouvernance des communs et la polycentricité (Ostrom) — L1.C22 § 2, P19b ;
2. la théorie des réseaux de flux, dont le livre tire son objectif de robustesse,
   et qui fait dépendre celle-ci de la diversité et de la modularité des canaux
   (Ulanowicz, Goerner, Lietaer) — L1.C23 § 2 et § 5 ;
3. la théorie des zones monétaires, appliquée à des chocs écologiques
   asymétriques sous taux de conversion fixe (Mundell, McKinnon) — L1.C23 § 5,
   P36.

Trois chemins séparés, trois motifs différents, un seul reproche : le dispositif
est uniforme là où sa propre littérature de référence recommande la diversité.
**Une objection qui se présente trois fois par des voies indépendantes n'est plus
une objection, c'est un résultat.**

L'arbitrage n'est donc plus reportable au même titre que les autres. Deux issues
seulement : adopter une part de polycentricité — norme votée au centre,
qualification instruite à l'échelle d'usage —, ou **démontrer** que l'uniformité
est le prix nécessaire de la comparabilité du signal. Le dispositif ne peut pas
se réclamer de la robustesse et laisser la question ouverte.

### A5 — Le périmètre financé

L1.C22 § 1 établit que « communs » recouvre trois catégories aux défaillances
distinctes, plus une quatrième entrée — le monopole naturel des réseaux — dont
le remède éprouvé n'est pas monétaire. Décider ce que le dispositif finance est
un préalable au calibrage, non une suite (P32).

### A6 — Quel scénario porte la stratégie d’adoption — RELEVÉ le 2026-09-04

**Ce que le livre tient à quelques pages d’intervalle, sans le confronter.**

Scénario 1 : les grandes réformes monétaires « n’ont jamais été le fruit d’une
planification sereine — elles ont été arrachées à des moments de crise aiguë ».
La stratégie qui en découle est d’être prêt pour la fenêtre.

Scénario 2 : la coalition de pionniers, dont le précédent invoqué est
« exactement la dynamique qui a présidé à la naissance de la zone euro » —
c’est-à-dire trente ans de rapports, de traités et de ratifications, hors de
toute crise aiguë.

**Les deux ne peuvent pas être vrais ensemble**, et L1.C25 § 3 a établi que la
loi historique placée en épigraphe du livre — « à chaque fois que le monde a
changé de système monétaire international, cela ne s’est fait qu’à la sortie
d’une grande guerre » — est **fausse telle qu’elle est écrite** : ni la rupture
de 1971, décidée unilatéralement en pleine guerre du Vietnam, ni la
construction de l’union monétaire européenne n’ont eu lieu à la sortie d’une
grande guerre.

**Ce que l’arbitrage change concrètement.** Les deux scénarios n’appellent pas
le même travail. Attendre une fenêtre demande un projet documenté et une veille
; construire une coalition demande des interlocuteurs, un seuil de pouvoir de
marché et un calendrier. Tant que l’arbitrage n’est pas rendu, le corpus ne
peut pas dire ce que la proposition attend de qui.

**Ce que le corpus recommande sans le trancher à la place de l’auteur.** Le
scénario 1 est le plus fragile des deux : sa prémisse historique est fausse, et
son précédent — Bretton Woods — se retourne contre lui, puisque le projet prêt
y a perdu (L1.C25 § 4, falsifieur F6). Le scénario 2 a pour lui un précédent
réel et vérifiable. Il porte en revanche un seuil de pouvoir de marché que le
livre reconnaît lui-même indispensable, et qui n’a pas été examiné.

Voir P45, P46, P47 au registre des promesses.

### A7 — Règle automatique ou pilotage discrétionnaire — RELEVÉ le 2026-09-04

**Origine.** Session de travail du 2026-09-04, où l'auteur décrit le pilotage
envisagé : ajuster les taux de reflux à l'année, avec l'appui de statisticiens,
d'économistes et de mathématiciens, pour que l'émission égale le reflux.

**Ce que cette description expose.** Deux résultats établis portent sur le
pilotage discrétionnaire et sur lui seul : les délais longs et variables de la
politique monétaire (Friedman 1968) et la déformation de l'assiette par
anticipation de la règle annoncée (Lucas 1976). Voir L1.C21 § 6 et le
falsifieur F7.

**Ce que l'arbitrage change.** Il ne porte pas sur la qualité de l'estimation
mais sur la forme de la décision, et il commande le profil d'équipe. Un barème
automatique demande d'écrire une formule et de la publier — travail de
conception, fait une fois, contestable publiquement. Un pilotage annuel demande
une capacité d'expertise permanente et une gouvernance de la révision. **Les
deux ne mobilisent pas les mêmes personnes ni le même calendrier**, et
l'arbitrage doit donc précéder la constitution de l'équipe, non la suivre.

**Ce que le corpus recommande sans trancher à la place de l'auteur.** La règle
lève les deux objections d'un coup ; le pilotage n'en lève aucune et se paie
d'une souplesse devant l'imprévu. Le coût de la règle est réel et doit être
énoncé : elle est rigide, et une formule mal spécifiée est plus difficile à
corriger qu'une décision annuelle. Voir P48.

### A8 — Les cinq barèmes sont un seul chantier — RELEVÉ le 2026-09-04

**Constat obtenu par récurrence, en défrichant L1.C28.** La même question
revient sous cinq formes que le corpus a traitées séparément, et elle est à
chaque fois la même : **qui pondère, selon quelle règle, et cette règle est-elle
écrite ?**

| Où | Ce qui est pondéré | Promesse |
|---|---|---|
| L1.C18 § 6, L1.C20 § 6 | Le barème de qualification des activités régénératives | P19b, P25 |
| L1.C21 § 6 | Les taux de reflux, et leur mode de fixation | P48, F7 |
| L1.C26 § 3 | Les parités du référentiel de change, et leur révision | P54 |
| L1.C27 § 6 | La valorisation des communs certifiés, qui commande l'équilibre extérieur | P52 |
| L1.C28 § 4 | Les six familles du tableau de bord, qui modulent les instruments | P53 |

**Ce que la récurrence établit.** Le dispositif remplace en cinq points des
mécanismes de marché par des barèmes administrés, et **il n'a écrit la règle
d'aucun d'entre eux**. Ce n'est pas cinq lacunes indépendantes : c'est une seule
lacune de conception, répétée. Les traiter séparément conduirait à cinq
réponses possiblement incohérentes entre elles — et le corpus a déjà constaté
que deux de ces barèmes interagissent, le succès sur la famille biosphérique
contractant l'assiette qui alimente la famille monétaire.

**Ce que cela change pour la passe 2.** L'arbitrage A4 (centralisation ou
polycentricité) et l'arbitrage A7 (règle ou pilotage) ne portent pas sur des
objets distincts : ce sont deux dimensions du même chantier. A4 demande à
quelle échelle le barème est établi ; A7 demande s'il s'applique par formule ou
par décision. **Les deux questions se posent identiquement aux cinq barèmes**,
et une réponse commune serait plus solide et plus économe que cinq réponses
locales.

Recommandation du corpus, non tranchée : traiter le chantier des barèmes comme
un objet unique, et lui consacrer un chapitre ou un livre dédié plutôt que de
le laisser réparti en cinq promesses.

### A9 — Le classement des objectifs du reflux — OUVERT le 2026-09-05

**Origine : L11.C03, qui compte.** La règle de comptage de la politique
économique veut que pour atteindre N objectifs indépendants, il faille au moins
N instruments indépendants. Le corpus a appliqué la règle au chantier des
barèmes. **Le compte ne passe pas**, et il ne passe pas de peu.

| | Ce que le dossier contient |
|---|---|
| Objectifs indépendants | **six** — niveau général des prix, prix relatif du dégénératif, stabilité du prix des essentiels, contracyclicité, bouclage volumétrique, abondance des essentiels |
| Instruments dans la même main | **trois** — taux moyen du prélèvement, forme du barème, taux du demurrage |
| Instrument dans une autre main | **un** — le volume d'émission, commandé par la qualification au Symposium |
| Instrument déjà affecté ailleurs | le référentiel de change, affecté à l'équilibre extérieur, et déjà en difficulté (P49) |

**Ce que le chapitre a réparé sans arbitrage, parce que c'était une erreur et
non un choix.** L'abondance des produits essentiels est un objectif de
**quantité de biens**. Aucun taux ne la produit : exempter le pain de
prélèvement ne fait pas apparaître de blé. Elle relève du barème de
qualification — financer la production essentielle —, non du barème de reflux.
C'est la première application utile de A8 : **un objectif mal affecté à un
barème était atteignable par un autre, et seul le traitement conjoint des cinq
le fait voir.**

**Ce qui reste et qui est un arbitrage.** Après correction, cinq objectifs
monétaires pour trois instruments coordonnés. La concurrence n'est pas répartie
uniformément : **trois objectifs réclament le taux moyen, deux réclament la
forme du barème, et le demurrage n'est réclamé qu'en second rang** — c'est
l'instrument qui a le plus de marge disponible.

**La collision décisive, et elle est irréductible.** Le niveau général des prix
(O1) et le bouclage volumétrique (O5) réclament le même instrument, le taux
moyen. Or ce sont deux nombres différents : ce que le niveau des prix exige et
ce que la couverture de l'émission exige ne coïncident que par accident.
L11.C01 § 1 l'avait établi sous une autre forme — l'émission est dimensionnée
par des besoins physiques, le reflux par un comportement d'agents. **O1 et O5
ne peuvent pas être fermes ensemble.** L'un des deux doit être accepté comme un
intervalle qui dérive.

**Ce que l'arbitrage demande à l'auteur**, sous la forme d'un tableau à quatre
colonnes : pour chaque objectif, l'instrument affecté, le statut — **ferme** ou
**souple** —, et le comportement en cas de conflit avec un autre objectif.

**PRÉCISÉ le 2026-09-05, sur sources procurées le jour même.** Trois apports
modifient la forme de l'arbitrage sans en changer l'objet.

*Le premier remède n'est pas le classement, c'est l'addition — et pour un motif
que le corpus n'avait pas.* Dans le cas « plus d'objectifs que d'instruments »,
Tinbergen prescrit d'abord d'**accroître le nombre des instruments**, parce que
cela « distribue plus équitablement et plus efficacement la pression de la
politique économique ». Ce n'est donc pas qu'une question de nombre :
**concentrer trois objectifs sur le taux moyen concentre la pression sur ce que
ce taux frappe.** Le classement vient en second, quand l'addition ne suffit pas
— et Tinbergen le formule alors ainsi : renoncer aux objectifs les moins
importants, et procéder par tâtonnements.

*Le classement a un précédent constitué, et l'arbitrage n'a donc pas à
l'inventer.* La position conditionnelle du débat sur le dosage monétaire /
macroprudentiel prescrit exactement cette forme : en cas de conflit d'objectifs,
la priorité va à un seul, et lorsqu'il est atteint on se tourne vers le second.

*Une inversion de méthode, qui vaut pour tout le Livre 11.* Chez Tinbergen, les
relations de structure prennent **les objectifs pour données et les instruments
pour inconnues**. On ne fixe pas un taux pour observer ce qu'il produit : on pose
les cibles et l'on résout pour les taux. Le dossier a fait l'inverse jusqu'ici,
un taux de 0,5 % y circulant sans qu'aucune cible ne le commande.

**Point de méthode, et il n'est pas négociable.** Le classement doit être écrit
**avant le premier chiffrage**. Sinon c'est le chiffrage qui le fera
silencieusement, en retenant les objectifs qu'il est commode de calculer et en
abandonnant les autres sans que personne l'ait décidé. Cela concerne
directement le Livre 13, que le Livre 11 bloque déjà.

~~**Ce que le corpus recommande sans trancher à la place de l'auteur.** Faire du
bouclage volumétrique (O5) l'objectif souple et du niveau des prix (O1)
l'objectif ferme, le dispositif disposant d'un second levier sur le volume et
d'aucun autre sur les prix.~~

**RECOMMANDATION RETIRÉE LE JOUR MÊME, après ouverture de Mundell 1963
(L11.C04).** Elle supposait qu'un barème national puisse tenir un objectif de
prix. Sous parité fixe et capitaux mobiles, c'est exactement ce qu'un
instrument national ne peut pas faire : « la banque centrale n'a pas davantage
de pouvoir sur la masse monétaire lorsque le taux de change est fixe ». Et elle
sous-estimait le bouclage, dont L11.C04 § 4 établit qu'il n'est pas un réglage
mais la condition qui empêche l'émission de fuir par le compte financier. Le
corpus ne lui substitue pas la recommandation inverse : il n'a pas de quoi
trancher, et il l'écrit.

**CE QUI REMPLACE LA RECOMMANDATION : UNE SECONDE DIMENSION.** A9 demandait de
classer les objectifs en fermes et souples. Il faut désormais les classer
**aussi selon l'échelle à laquelle ils sont atteignables — globale ou
nationale.** Le résultat de Mundell dit que la case « objectif de prix,
instrument national, parité fixe, capitaux mobiles » est **vide**. Un classement
à une seule dimension y logerait un objectif que rien ne peut atteindre, et
personne ne s'en apercevrait avant le chiffrage.

**Ce qui demeure de la recommandation retirée, et qu'il faut garder :** un
bouclage souple fait dériver les fonds propres du Symposium, et L11.C02 § 2 a
montré que cette dérive est portée par les banques centrales nationales sous
forme de créance perpétuelle. **Ce qui n'est en aucun cas défendable reste de
déclarer O1 et O5 fermes ensemble.**

**Ce que A9 ne traite pas.** Le signe de l'effet sur les biens de position
(L11.C03 § 5) et le motif de la séparation macroprudentielle (§ 6) sont des
questions de fait, non d'arbitrage. La première appelle une mesure, la seconde
une source. Elles figurent en `verifications_en_attente` du chapitre et en
priorité de `protocoles/sources-a-ouvrir.md`.

Compose avec A4 (à quelle échelle le barème est établi), A7 (règle ou
pilotage), A8 (les cinq barèmes sont un seul chantier), P48, F1 et F7.

### A10 — L'assiette du reflux transactionnel — OUVERT le 2026-09-05

**Origine : L11.C05**, écrit après ouverture de la proposition voisine. Le
corpus a découvert qu'il comparait deux assiettes de nature différente en
croyant comparer deux calibrages du même instrument.

| | Assiette « chaque paiement » (les voisins) | Assiette « consommation finale × empreinte » (le livre) |
|---|---|---|
| Mesurable aujourd'hui | **oui** — les systèmes de paiement la comptent déjà | **non** — la métrologie n'existe pas (L1.C21 § 6) |
| Mesure la bonne grandeur | **non** — elle mesure la longueur de chaîne | **oui** — c'est l'empreinte visée |
| Effet sur la structure productive | prime à l'intégration verticale | neutre |
| Rendement | élevé, assiette très large | inconnu, assiette étroite et érodable (P29, F1) |

**Ce que l'arbitrage demande.** Trancher entre **une base observable qui mesure
la mauvaise grandeur** et **une base juste qui n'est pas mesurable** — ou
énoncer la voie intermédiaire et l'instruire : prélever sur la consommation
finale mais moduler sur quelques classes grossières de produits plutôt que sur
une empreinte calculée bien par bien. On y perd en justesse ce qu'on y gagne en
existence, et **le nombre de classes suffisant pour que l'instrument agisse
encore est calculable.**

**Pourquoi cet arbitrage passe avant les autres.** Un barème ne se règle que sur
une assiette arrêtée. Tant que A10 n'est pas tranché, ni le taux (A9), ni le
mode de fixation (A7), ni l'échelle (A4) ne portent sur un objet défini. **A10
commande le reste du Livre 11.**

**Ce que l'arbitrage NE demande pas.** Le livre n'est pas exposé à l'effet de
cascade, puisqu'il frappe la consommation finale : le reproche vise la
proposition voisine, pas la sienne. Le corpus l'enregistre à son crédit.

**Conséquence déjà tirée, hors arbitrage.** Le corpus ne dispose d'aucune borne
empirique sur son propre instrument. Le taux de 0,5 % qu'il employait depuis
L11.C02 porte sur une autre assiette. La grandeur qui rendrait les deux
propositions comparables — le rapport du chiffre d'affaires cumulé à la valeur
finale — est à produire, et elle existe sous des formes voisines dans les
comptabilités nationales. Renvoi au Livre 13.

