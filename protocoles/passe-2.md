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

**PRÉCISÉ LE 2026-09-06, sur le chapitre IV de Tinbergen, ouvert de première
main. LA « RÈGLE » A UNE FORME, ET ELLE A UN NOM.** Une fois les cibles fixées,
les valeurs des instruments restent fonctions des **données**, qui changent :
« the values of the instrument variables are **dependent on those of the
data** [...] **In this form we shall call these equations "DIRECTIVES FOR
ECONOMIC POLICY" since they indicate how the political parameters have to be
varied in relation to the changing data.** »

**Un barème réglé n'est donc pas une table de taux : c'est une directive**, de la
forme *taux = f(données observées)*. Trois questions du corpus se rejoignent
là. **A7** opposait règle et pilotage : la directive est la forme de la règle.
**A15**, tranché par l'auteur, indexe le taux sur la disponibilité constatée du
substitut : c'est une directive, la donnée étant ce constat. **L11.C06 § 4** a
établi qu'un barème est trois objets dont le premier est une table : **ce
premier objet est une directive, non une table.**

**CONDITIONNÉ LE 2026-09-06 PAR L11.C20, et il faut le dire ici parce que ce
paragraphe promettait trop.** La directive ne répond à A7 **que si son propre
amendement est réglé** — c'est la quatrième exigence de L11.C12, restée vide
jusqu'au 2026-09-06 et portée en **A23**. Une directive réécrite à volonté
n'oppose rien de plus qu'une table au pilotage discrétionnaire. **A7 est donc
réglé en forme et suspendu à A23 en pratique.**

**Conséquence de rédaction, et elle vaut pour tout le Livre 11 :** publier des
nombres, c'est publier le résultat d'une directive pour un état des données
donné. **Ce qui doit être publié et discuté est la directive.** Un barème qui ne
publie que ses nombres cache ce qui les produit, et rend indiscutable ce qui
devrait l'être.


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

### A8 — Les cinq barèmes sont un seul chantier — RENDU le 2026-09-06 par L11.C17

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

---

**RENDU le 2026-09-06 par L11.C17, après instruction des cinq lieux. CONFIRMÉ
SUR SA THÈSE, CORRIGÉ SUR SON DÉCOMPTE, ET DÉMONTRÉ AU LIEU D'ÊTRE CONJECTURÉ.**

**Ce qui est corrigé.** Les cinq lieux ne sont pas cinq objets de même nature.
**Le tableau de bord n'est pas un barème : c'est l'entrée commune des autres**
(L11.C14). **La valorisation des communs n'est pas un barème distinct : c'est la
décision D2 du barème de qualification** (L11.C13 § 3, L11.C16). **Il reste
trois barèmes et une entrée** — et la correction renforce A8 au lieu de le
démentir : la ressemblance dont il tirait sa conjecture était en partie une
identité. **Reste ouvert de savoir si le prélèvement transactionnel et le
demurrage font un barème ou deux** : trois si c'est un, quatre si ce sont deux.

**Ce qui est démontré.** A8 tenait par récurrence, ce qui n'établit rien : cinq
lacunes peuvent se ressembler sans communiquer. **Trois voies indépendantes
établissent maintenant l'interdépendance** — par citation (Tinbergen, L11.C13
§ 3), par récurrence (P19b aux deux extrémités du circuit, L11.C05 § 6 et
L11.C13 § 7), et **par déduction** (l'égalité de bouclage lie la structure de la
valorisation au taux de reflux, L11.C16 § 3). **La troisième n'a besoin d'aucune
autorité extérieure : elle se lit dans une égalité que le dispositif pose
lui-même.**

**La réponse commune existe et porte un nom : la directive** (L11.C12). Elle
règle A7 — la directive EST la forme de la règle —, elle donne son nom à ce que
l'auteur a tranché en A15, et elle passe l'épreuve des trois barèmes. **Son coût
n'est pas commun** : il croît avec l'irréversibilité de ce que le barème
commande, et il est maximal sur la valorisation.

**Ce que le rendu laisse au chantier, et qui lui appartient en propre :** A5, le
périmètre financé, non instruit ; **le seuil d'exemption pour les personnes
morales, qui manque entièrement et qu'aucun chapitre n'avait relevé** ; et la
matière de A16, dont les trois précédents ne sont toujours pas ouverts.

**A8 est rendu. Le chantier n'est pas clos.**

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

**CORRIGÉ DEUX FOIS LE 2026-09-05, SUR LE TEXTE DE TINBERGEN.** L'auteur a
procuré l'ouvrage intégral dans la journée ; les chapitres V, VI puis II ont été
lus. **Le corpus s'est trompé, puis a sur-corrigé, et voici l'état final.**

**Deux notions distinctes portent chez Tinbergen des noms presque identiques**,
et le compte rendu français les avait fondues. Les ***target conditions*** (ch. V)
sont **des relations entre les valeurs cibles**, au nombre de t = n − n′. Les
***conditional targets*** (ch. II) sont **une catégorie d'objectifs**, « as an
expression of a lower or higher degree of priority that may, under certain
conditions, be attributed to the various targets ». **Le classement que A9
demandait est donc bien chez Tinbergen** — le corpus l'avait nié à tort en
milieu de journée — **et il s'y ajoute une contrainte que A9 ignorait.**

**LA RÈGLE OPÉRATOIRE, ch. VI § 1, et c'est ce qui donne son sens au
classement.** Quand la solution viole une condition-limite : « **To start with we
shall, of course, only give up CONDITIONAL targets.** Instead we shall add one or
more boundary conditions, and it seems the most natural procedure to add those
particular boundary conditions that were, with the previous set-up of the
problem, violated. » **Classer un objectif comme conditionnel, c'est désigner
d'avance ce qu'on abandonnera.**

**LE MODE D'ÉCHEC TERMINAL, que le corpus n'avait pas.** « There is, however, no
guarantee that the new solution will be acceptable. **If the number of violated
boundary conditions surpasses the number of conditional targets**, it may also be
impossible to reformulate the problem beforehand [...] The case may therefore
present itself that **no solution to our policy problem, however restricted by
the elimination of conditional targets, exists.** » **C'est un risque réel pour
ce dispositif**, qui accumule les conditions-limites — légalité de la
consolidation, étanchéité du périmètre, non-régressivité, prix des essentiels,
protection des petits producteurs. **Si elles sont plus nombreuses que les
objectifs qu'on accepte d'abandonner, il n'y a pas de politique.**

**LA MÉTHODE, quand les conditions-limites mordent.** « Generally speaking the
number of possibilities is large and it is, as a rule, difficult if not
impossible to study them or detect them in a systematic way. **It is by trial and
error, albeit perhaps by a somewhat systematicised trial and error method, that
we have to proceed.** » Le tâtonnement n'est donc pas un pis-aller de concepteur
paresseux : **c'est la seule méthode disponible dans le cas où se trouve le
dispositif**, ce qui conforte l'instruction de progressivité de l'auteur (A15).

**LA MÉTHODE POUR CHIFFRER SANS AVOIR LES NOMBRES, ch. VII § 4, lue le
2026-09-06. C'est le versement le plus utile de tout le dépouillement.**

Le corpus répète depuis L11.C02 qu'il n'a **aucune borne empirique** : trois
facteurs au rendement du reflux, aucun connu. Il en tirait qu'aucun chiffrage
n'était possible. **Tinbergen établit que c'est faux, et donne le procédé.**

« As to the consequences of possible errors in the numerical values assumed for
the coefficients, **a simple practical procedure is to indicate VARIATION
INTERVALS for these coefficients and to solve the problems for different extreme
values of these coefficients.** » Il le fait sur son propre exemple — six jeux de
coefficients extrêmes — et constate que la solution pour un instrument varie de
−0,037 à −0,039, « **evidently the variance in ξ₀ is very small in this
particular case** », tandis que pour un autre instrument « the variance [...] is
larger ».

**Ce que cela change pour le Livre 13, et c'est considérable.** On ne cherche
pas les valeurs vraies des trois facteurs : **on pose un intervalle plausible
pour chacun, on résout aux bornes, et on regarde lesquels des résultats sont
robustes.** Un résultat identique aux six coins de l'intervalle est acquis même
si aucun facteur n'est connu. Un résultat qui change de signe entre deux coins
désigne exactement la grandeur qu'il faut aller mesurer. **Le chiffrage cesse
d'être bloqué par l'ignorance : l'ignorance devient l'objet du calcul.**

**Deux garde-fous que Tinbergen ajoute et que le corpus retient.**
*Contre la fausse précision* : « one would not write more decimal places for the
values [of the instruments] than for those of [the target] and therefore avoid
such suggestions of false accuracy ». *Contre la linéarité indue*, avec un test
qu'il attribue à Frisch : si le coefficient du terme du premier degré est du
même ordre que la variation visée de l'objectif, le terme du second degré est du
même ordre que le premier et **l'approximation linéaire est très inexacte** —
« this may easily be tested ». Règle générale : l'ordre de grandeur des
coefficients de la solution **doit être supérieur** à celui des objectifs et des
données. **Le corpus tenait la linéarité pour une réserve sans test ; il a le
test.**

**UNE CATÉGORIE QUE LE COMPTE DE L11.C03 IGNORAIT.** Tinbergen distingue des
grandeurs introduites « in the form of **conditions** [...] since they are **not
in themselves elements of well-being but rather technical expressions of a
"sound policy"** » — son exemple étant le solde de la balance des paiements.
**Le bouclage volumétrique (O5) est de cette espèce**, et la collision O1 contre
O5 relevée en L11.C03 § 4 n'oppose donc pas deux objectifs de même rang : elle
oppose **un objectif de bien-être à une condition de solidité**.

*Ce que le corpus avait compris.* « Objectifs-conditions » désignerait des
objectifs à préserver en priorité — donc un classement, ferme contre souple.

*Ce que Tinbergen écrit.* Les **target conditions** sont **des relations que les
valeurs cibles doivent satisfaire** : « the values to be chosen for the target
values have to satisfy these conditions if the problem of policy is to be
soluble at all. **Targets are not free then** ; had they been chosen otherwise,
they would have been *incompatible* among themselves and their set would be
*inconsistent* » (ch. V, § 3). Leur nombre est **t = n − n′**, l'excédent
d'objectifs sur les instruments.

**Ce que A9 demande devient donc plus précis, et plus exigeant qu'un
classement.** Non pas « quels objectifs sont fermes », mais : **quelles
relations les valeurs visées doivent-elles satisfaire pour que l'ensemble soit
seulement soluble ?** Deux objectifs de plus que d'instruments, c'est deux
relations entre les valeurs. Choisir les valeurs sans elles ne donne pas une
politique difficile : **cela donne un ensemble inconsistant.**

**ET LE COMPTE EST PLUS DÉFAVORABLE QUE CELUI DE L11.C03.** Tinbergen établit
que **les conditions-limites entrent dans le compte des objectifs** : « the
addition of these boundary conditions [...] means in fact that **we add one or
two conditions and hence have 5 or 6 targets against 4 instruments** », et
« boundary conditions play **a much more important rôle than is often
believed** ». Or le corpus traitait comme des contraintes extérieures au compte
l'étanchéité du périmètre (P29), la légalité de la consolidation (L1.C21 § 6)
et le refus de frapper qui ne peut pas prouver (A11). **Ce sont des objectifs de
plus.** Travail préalable à A9, et il est mécanique : **dresser la liste
complète des conditions-limites du dispositif**, puis recompter.

**UN RÉSULTAT FAVORABLE, du même chapitre.** Tinbergen ne dit pas seulement
qu'il faut ajouter des instruments : il dit que l'analyse d'une incompatibilité
peut **en faire apparaître un**. Et son exemple travaillé est celui du
dispositif — deux objectifs contradictoires exigeant l'un un taux bas, l'autre
un taux élevé, et la sortie est « **conceiving a variable tax rate** which need
not be a high rate then ». **Un barème modulé n'est donc pas un contournement
de la règle de comptage : c'est le remède que son auteur recommande.**

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

### A11 — Le niveau de la valeur par défaut — OUVERT le 2026-09-05

**Origine : L11.C06**, qui instruit la seule sortie connue à l'objection de la
connaissance dispersée. Si l'empreinte cumulée est une grandeur que personne ne
détient, le centre n'a pas besoin de savoir : il lui faut une **valeur par
défaut** que celui qui sait mieux puisse faire réviser. **Le niveau auquel on
place ce défaut n'est pas un réglage technique. C'est la décision politique
centrale du dispositif, et elle est habituellement traitée comme un détail
d'exécution.**

| Niveau du défaut | Qui documente | Ce que devient l'instrument |
|---|---|---|
| **Clément** (performance moyenne ou favorable) | personne — le gain ne paie pas la démarche | le défaut devient la valeur universelle, la modulation s'éteint, l'instrument **perçoit sans orienter** |
| **Punitif** (performance la plus défavorable observée) | tous ceux qui font mieux, c'est-à-dire presque tous | la modulation vit, l'instrument **oriente** — et fait payer le plein tarif à qui ne peut pas prouver |

**Ce que l'arbitrage demande vraiment.** Non pas « quel niveau », mais **quelle
part de l'efficacité on accepte de perdre pour ne pas frapper celui qui ne peut
pas prouver.** Car le défaut punitif ne frappe pas qui pollue le plus : il
frappe **qui ne peut pas documenter** — petit producteur, filière informelle,
économie sans appareil statistique.

**Où la réponse se lit, et ce n'est pas dans le barème.** Elle se lit dans le
**coût et le délai de la procédure de révision**. Une table sévère avec une
procédure gratuite et rapide est exigeante mais équitable ; la même table avec
une procédure coûteuse frappe les petits. **Le taux est identique dans les deux
cas** — et c'est ce qui rend cette régressivité plus dangereuse qu'une
régressivité de taux : elle est invisible dans le document qu'on discute.

**Ce que A11 impose à la rédaction du reste du livre.** Un barème est trois
objets : une **table par défaut**, une **procédure de révision**, une **charge
de la preuve**. Le livre n'écrit que le premier, et c'est le deuxième qui
commande l'incidence. **On ne publie donc pas un barème, on publie un triplet**,
et le Livre 13 ne peut pas chiffrer le premier sans le second.

**Une récurrence que le corpus relève sans encore l'expliquer.** C'est la
troisième fois dans ce livre qu'un mécanisme unique porte l'effet recherché ET
son contraire, sans qu'aucun réglage ne les sépare : l'effet de position
(L11.C03 § 5), la cascade (L11.C05 § 4), le niveau du défaut (L11.C06 § 2).
**Trois occurrences suggèrent une propriété générale plutôt que trois défauts
locaux.** À nommer avant la fin de la passe 1.

**AJOUT DU 2026-09-06, chapitre X de Tinbergen, et il éclaire le biais sans
l'excuser.** Parmi les facteurs **techniques** qui façonnent à bon droit une
mesure, Tinbergen range « the **costs** of their realisation, the **delays** to
be expected or the **number of subjects to be affected** », avec l'exemple :
entre deux mesures dont l'une « **hits a large number of people and may
therefore be costly** » et l'autre « affects few and therefore is less costly »,
on choisit la seconde — les taxes ou allocations portant sur des biens
« produced in **few, but large establishments** ».

**C'est la justification administrative de la valeur par défaut, et c'est aussi
le mécanisme du biais que L11.C09 a trouvé.** Frapper peu d'acteurs, grands et
documentés, coûte moins à administrer que d'en atteindre beaucoup. **Le biais de
concentration n'est donc pas un oubli : c'est ce que l'efficacité administrative
recommande.** Cela change la nature de la correction demandée en A14 : il ne
s'agit pas de réparer une négligence, **il s'agit de payer délibérément un
surcoût administratif pour atteindre ceux que l'efficacité conseille
d'ignorer.** C'est un arbitrage politique et il doit être présenté comme tel.

**Tinbergen nomme aussi la situation du corpus.** Parmi les facteurs « of a more
doubtful nature » il place le **manque de données** : « it often means that
**rather arbitrary decisions have to be taken instead of decisions that are
based on economic principles**. Economies effected by the government are often
for lack of better data distributed **proportionally** over a number of items ;
or **intuitive methods** are applied to estimate priority. » **Une valeur par
défaut est cela même** — et le dispositif doit l'assumer comme une décision
arbitraire assumée, non la présenter comme une mesure.

**Ce qui bloque A11.** Le règlement pris pour modèle n'a pas été ouvert. Tant
qu'on ignore sur quelle population de référence sa valeur par défaut est
établie et ce que coûte sa procédure de révision, l'arbitrage se pose sans son
seul précédent. **À instruire après acquisition, pas avant.**

### A12 — Le nœud de prélèvement du demurrage — OUVERT le 2026-09-05

**Origine : L11.C07**, qui solde trois renvois laissés ouverts par L1.C21 § 6,
L11.C02 § 4 et L11.C04 § 5. Le second ressort du reflux doit prélever quelque
part, et **aucune des trois positions possibles n'est bonne**.

| Nœud | Cible juste | Praticable en droit | Assiette tenable |
|---|---|---|---|
| **Encaisses consolidées par bénéficiaire effectif** — position du livre | **oui** | **À ÉTABLIR** — corrigé le 2026-09-06, ce n'était pas « non » | oui |
| **Réserves bancaires à la banque centrale** — position des voisins, 0,1 % mensuel | **non** — frappe les banques, pas les thésauriseurs | oui | oui |
| **Comptes, sans consolidation** | oui | oui | **non** — le fractionnement la vide |

**Aucune ligne n'a trois oui.** Le choix n'est donc pas un réglage à optimiser :
c'est un arbitrage entre trois défauts, et il appartient à l'auteur.

---

**LA PRÉMISSE JURIDIQUE DE CET ARBITRAGE ÉTAIT FAUSSE. CORRIGÉE LE 2026-09-06,
L'ARRÊT AYANT ÉTÉ OUVERT DE PREMIÈRE MAIN** — CJUE, grande chambre, 22 novembre
2022, affaires jointes C-37/20 et C-601/20, ECLI:EU:C:2022:912, texte intégral.
**Douzième autocorrection du corpus, et la première appuyée sur une source
juridique lue.**

**Ce que le corpus soutenait.** Que la consolidation des soldes par bénéficiaire
effectif se heurte à « un obstacle **de droit** et non d'administration », parce
que « la forme la moins intrusive » du registre aurait été jugée
disproportionnée.

**Ce que l'arrêt dit.** Est invalide le seul article 30 § 5, premier alinéa,
sous c), en ce qu'il rend les informations accessibles « **dans tous les cas à
tout membre du grand public** ». **Le registre n'est pas invalidé.** Le point 84
affirme au contraire que ces informations « doivent être accessibles, **dans
tous les cas, aux autorités compétentes** et aux cellules de renseignement
financier, **sans aucune restriction** ». Et le point 85 qualifie le régime
antérieur à 2018 — accès des autorités et des personnes justifiant d'un intérêt
légitime — de **considérablement moins attentatoire**, c'est-à-dire exactement
l'inverse de ce que le corpus lui faisait dire.

**Conséquence pour A12 : l'obstacle n'est pas là où le corpus le mettait.** Une
autorité qui consolide n'est pas devant une interdiction ; ce qui est interdit
est de **publier** la consolidation, ce dont aucun prélèvement n'a besoin.

**Ce que la correction ne donne PAS, et le corpus le marque aussitôt.** Le
registre porte sur les bénéficiaires effectifs de **sociétés et autres entités
juridiques** ; **il ne recense pas les encaisses d'une personne physique
réparties entre ses comptes.** Consolider des SOLDES relève d'autres instruments
— registres nationaux de comptes bancaires, échange automatique d'informations —
**que l'arrêt ne traite pas**. Le corpus n'a donc pas établi que la
consolidation des encaisses est licite : il a établi qu'il invoquait **le
mauvais obstacle**, et il doit maintenant instruire le bon.

**ET L'ARRÊT FOURNIT LE TEST QUI REMPLACE L'INTERDICTION.** Point 64 : les
limitations « s'opèrent dans les limites du **strict nécessaire** », et lorsqu'un
choix s'offre « entre plusieurs mesures appropriées à la satisfaction des
objectifs », il faut retenir **la moins intrusive**. **Cela retourne l'arbitrage
A12 au lieu de le trancher** : le troisième nœud — prélèvement par compte, sans
consolidation — **est** une mesure moins intrusive. Retenir le premier nœud
suppose donc de démontrer que le troisième ne suffit pas, c'est-à-dire de
**chiffrer la fuite par fractionnement**. **A12 devient une question mesurable
là où le corpus la croyait fermée par principe.**

**Nouvelle acquisition qui en découle** : les registres nationaux de comptes
bancaires — leur base juridique, leur périmètre, et qui y accède. C'est là que
se trouve le vrai obstacle, s'il existe.

**UNE REQUALIFICATION QUE LE CORPUS SE DOIT, versée le 2026-09-06 sur le
chapitre X de Tinbergen.** Le corpus a traité l'obstacle juridique comme **une
gêne à contourner**, et il a cherché le nœud de prélèvement qui l'évite.
Tinbergen range ce genre de facteur parmi ceux qui co-déterminent la politique
**à bon droit** : « a sound policy has to satisfy certain **principles** [...]
laid down in the constitution or in the laws : **equality of all citizens in
questions of jurisdiction generally**, and to quote an economic example, in
taxes », et « an example of a purely **juridical** factor that will often be the
determinant [...] is the necessity to **respect contracts or agreements**,
national as well as international ».

**Ce n'est donc pas un obstacle, c'est une condition-limite légitime** — et
L11.C03 a établi le même jour, sur le chapitre V, que **les conditions-limites
comptent comme des objectifs**. Deux conséquences. **A12 ne se règle pas en
trouvant l'astuce qui évite le droit** : un contournement doit être défendable
au même titre que le barème lui-même. Et **le nœud « réserves bancaires » cesse
d'être neutre** : il n'évite pas seulement une difficulté administrative, il
évite une exigence d'égalité devant l'impôt, ce qui est un choix à énoncer.

**Ce qui pourrait rouvrir la première ligne, et c'est la vérification la plus
rentable du dossier.** Le corpus fait dire à l'arrêt de 2022 que la
consolidation par bénéficiaire effectif est fermée. **Si l'arrêt ne vise que
l'ACCÈS DU GRAND PUBLIC au registre — et non la tenue d'un registre accessible
aux seules autorités fiscales — alors le nœud du livre redevient praticable et
A12 se règle tout seul.** Une lecture de l'arrêt suffit à le savoir. **À faire
avant de trancher.**

**Une piste construite par le corpus sur la troisième ligne**, donnée pour ce
qu'elle est — non instruite. Le fractionnement n'est pas gratuit : ouvrir et
tenir des comptes multiples coûte des frais et de l'attention. Or l'objet du
second ressort n'est pas de percevoir mais de **rendre la thésaurisation
coûteuse**. Sous cette lecture, un demurrage par compte atteint partiellement
son but même sans rien collecter. **Trois raisons qu'elle ne vaille rien**, à
éprouver dans cet ordre : le coût du fractionnement peut être négligeable, il
est régressif, et ce qui est payé en frais bancaires ne détruit aucune monnaie —
donc F1 reste entier.

**Ce que A12 change au compte des objectifs (A9).** L11.C07 § 5 établit que la
compensation contracyclique entre les deux ressorts — présentée par L1.C21 § 5
comme la vertu principale de l'architecture — **défaille dans l'état pour lequel
elle est conçue** : le moment où la thésaurisation appelle le demurrage est
celui où son assiette est la plus mobile. **L'objectif de contracyclicité (O4)
perd donc son instrument dans l'état qui le motive**, et le compte de A9, déjà
en défaut de deux, se dégrade d'autant.

**Convergence à porter au dossier de P49.** La restriction de la mobilité des
capitaux ferme **deux** fuites indépendantes : celle du triangle
d'incompatibilité (L1.C26 § 4) et celle du demurrage (L1.C21 § 6). Les deux
chapitres proposaient la même mesure sans voir qu'ils désignaient la même chose.
**L'arbitrage de P49 ne porte donc plus seulement sur le change : il décide
aussi si le second ressort tient.**

### A13 — Le périmètre des dérogations au demurrage — OUVERT le 2026-09-05

**Origine : instruction de conception de l'auteur**, adressée au corpus le
2026-09-05 après lecture de L11.C07 : « Il faudra cependant envisager des
mécanismes de dérogations. Je ne souhaite pas que des gens soient soumis au
demurrage s'ils placent leur argent sur des plans épargne logement écologiques
ou des maisons à énergie positive par exemple. » Instruite en L11.C08.

**L'arbitrage porte sur le PÉRIMÈTRE, non sur le principe.** Le corpus tient
l'instruction pour fondée et porte à son crédit un apport de conception : une
dérogation transforme le demurrage d'une **peine** en un **prix du refus
d'investir** dans ce que le système veut financer. Un instrument qui prétend
orienter doit offrir la direction qu'il recommande.

**Point préalable, et il évite une disposition inutile.** Les deux exemples de
l'instruction ne relèvent pas du même instrument. **Acheter un logement à
énergie positive est une transaction** — l'argent a circulé, le demurrage n'a
jamais eu prise. Cela relève du barème du PREMIER ressort, où un tel bien
devrait déjà être au taux le plus bas ; **s'il faut une dérogation pour l'y
mettre, c'est que le barème ne fonctionne pas.** Seul le plan d'épargne, qui
demeure une encaisse, appelle une dérogation au demurrage.

**Ce que la dérogation coûte, et il faut l'avoir en tête pour arbitrer.** Une
dérogation est **un substitut créé par décret**. Les deux premiers substituts
que Keynes nomme dans l'objection qui borne le demurrage sont « monnaie de
banque, créances à vue » — la forme même d'un plan d'épargne. Et le raisonnement
se referme quel que soit le support : **liquide**, il est un substitut parfait
et l'assiette disparaît ; **immobilisé**, il déplace la thésaurisation au lieu
de la défaire. **Le bénéfice ne peut donc pas être la circulation : il ne peut
être que l'affectation.**

**La bande dans laquelle la dérogation tient, et elle se calcule.**

| Capacité d'absorption des placements éligibles | Effet |
|---|---|
| très inférieure au stock d'encaisses au-dessus du seuil | **sans danger et sans effet** — une exemption que presque personne ne peut utiliser |
| comparable ou supérieure | **l'assiette du second ressort disparaît** — le bouclage volumétrique n'est plus assuré (L11.C04 § 4) |

Les deux grandeurs existent — statistiques de patrimoine financier d'un côté,
encours et capacités des filières éligibles de l'autre. **Elles n'ont jamais été
rapprochées, et tant qu'elles ne le sont pas on ignore si la dérogation demandée
est inoffensive ou si elle supprime l'instrument.** Renvoi au Livre 13.

**Deux effets structurels à porter à l'arbitrage.** La dérogation **transfère
l'assiette du second ressort au barème de qualification** : une seule table
gouvernerait alors les deux extrémités du circuit, ce qui entre par l'émission
et ce qui échappe au reflux. Et elle crée **une prime monétaire chiffrable à
l'obtention du label** (P37), sur la partie du barème la plus difficile à
établir, puisqu'elle exige de tracer l'emploi des fonds collectés — l'obstacle
métrologique de L11.C05 déplacé de la chaîne de production vers la chaîne de
financement.

**Ce qui bloque A13 en amont.** L1.C21 § 3 a relevé que le livre exclut de
l'assiette du premier ressort les « flux purement financiers » tout en y incluant
les acquisitions d'actifs, sans concilier les deux énoncés. **Un plan d'épargne
tombe exactement dans cet interstice.** Cette ambiguïté doit être levée avant que
le régime de la dérogation puisse être arrêté.

### MIS DE CÔTÉ — la récurrence des effets appariés — RELEVÉ le 2026-09-05

**Mis de côté à la demande de l'auteur le 2026-09-05**, pour ne pas être nommé
trop tôt. Consigné ici pour ne pas être perdu, et à reprendre quand la passe 1
du Livre 11 sera plus avancée.

**Le constat.** Quatre fois dans le Livre 11, **un même curseur produit l'effet
recherché ET son contraire**, dans la même proportion, sans qu'aucun réglage ne
les sépare.

| Où | Le curseur | L'effet voulu | Son contraire |
|---|---|---|---|
| L11.C03 § 5 | le taux sur le dégénératif | décourager l'usage | sur les biens de position, le prix EST l'attribut recherché |
| L11.C05 § 4 | le taux par paiement | pénaliser les chaînes longues | primer l'intégration verticale |
| L11.C06 § 2 | le niveau du défaut | faire documenter, donc moduler | faire payer qui ne peut pas prouver |
| L11.C08 § 6 | l'étendue de la dérogation | orienter l'épargne vers le régénératif | vider l'assiette du reflux |
| L11.C10 § 6 | la durée de la trajectoire | laisser le temps de transformer | profiter d'abord à qui peut investir pendant qu'elle court |

**Le seul élément d'analyse acquis à ce stade**, apporté par la quatrième
occurrence : dans les quatre cas, **l'effet contraire porte sur l'assiette ou
sur l'incidence, jamais sur l'effet direct.** L'instrument fait bien ce qu'on
lui demande ; ce qui se dégrade est ce sur quoi il s'appuie, ou qui le supporte.

**SIXIÈME OCCURRENCE, versée le 2026-09-06 sur le chapitre IX de Tinbergen, et
elle porte sur le remède lui-même.** Le chapitre V prescrit d'ajouter des
instruments pour lever une incompatibilité. Le chapitre IX établit ce que cela
coûte : « policies with a **small** number of instruments tend to use
**overall-instruments of an objective nature**, judging each individual case on
the basis of well-defined objective criteria. Policies with a **large** number of
instruments will tend to **detailed controls and to discriminatory treatment of
individual cases**. »

**Le curseur est ici le nombre d'instruments.** L'augmenter lève
l'incompatibilité du comptage — effet recherché — et pousse le dispositif vers
le contrôle détaillé et le traitement discriminatoire au cas par cas — effet
contraire, et c'est exactement ce que F7 condamne sous le nom de pilotage
discrétionnaire. **Le remède au déficit d'instruments aggrave le problème de la
règle contre le pilote.** Sixième occurrence, et la première qui frappe une
solution plutôt qu'un instrument.

**Pourquoi ne pas nommer tout de suite.** Quatre occurrences dans un seul livre
peuvent tenir à la manière dont ce livre est écrit plutôt qu'à une propriété du
dispositif. **Le test est de chercher la même forme ailleurs** — au Livre 2 sur
les instruments macroprudentiels, au Livre 13 au moment du chiffrage. Si elle
n'y apparaît pas, c'est un artefact de méthode ; si elle y apparaît, c'est un
résultat, et il faudra alors le nommer et l'expliquer.

**Ce que le corpus s'interdit en attendant** : traiter les quatre cas comme
quatre défauts locaux à corriger séparément, ce qui reviendrait à nier la
récurrence sans l'avoir éprouvée.

### A14 — Les corrections d'incidence — OUVERT le 2026-09-05

**Origine : L11.C09**, qui pose une question absente du livre et du Cahier — non
pas combien retirer, mais **sur qui le retrait pèse.** Le mot incidence n'y
figure nulle part.

**Le constat, obtenu par convergence de quatre chapitres et non par une
objection extérieure.** La cascade favorise les ensembles **intégrés** ; la
valeur par défaut favorise ceux qui savent **documenter** ; la consolidation par
bénéficiaire effectif favorise ceux qui disposent de **structures** ; la
dérogation favorise ceux qui disposent d'un **conseil**. Aucun de ces quatre
mécanismes n'a été choisi pour cela, et chacun résout un problème réel et
distinct. **C'est un effet d'accumulation, et les effets d'accumulation ne se
voient pas dans l'examen pièce à pièce.**

**Ce qui rend l'arbitrage nécessaire, et urgent.** Les quatre biais sont
**procéduraux et jamais tarifaires** : ils dépendent du nombre de transactions,
du coût d'une procédure, d'un régime juridique, de l'accès au conseil.
**Aucune correction par les taux ne les atteint.** On peut baisser tous les
taux — les quatre biais demeurent identiques. C'est pourquoi ils sont invisibles
dans un tableau de taux, qui est le seul document que le dispositif publie.

**Les quatre corrections connues, à écrire dans le dispositif et non à renvoyer
à sa mise en œuvre :**

| Biais | Correction connue | Statut |
|---|---|---|
| Cascade | assiette sur la consommation finale | **déjà retenue par le livre** — il n'est pas exposé |
| Valeur par défaut | procédure de révision **gratuite et rapide** | à écrire (A11) — **FORME INSTRUITE le 2026-09-06 par L11.C19, arbitrage A22** : trois garanties déduites, et le contentieux se révèle être **le mécanisme d'apprentissage du barème** — assorti d'un **sixième biais** qui se compose avec le temps |
| Consolidation | seuil pour les **personnes morales**, qui manque entièrement | ~~**manque de conception**, pas un paramètre~~ — **INSTRUIT le 2026-09-06 par L11.C18, arbitrage A21.** Quatre formes comparées ; la franchise est la seule sans effet de seuil et la plus coûteuse en assiette. **Résultat inattendu** : le reproche de fragmentation ne tient pas ici, B2 rendant l'échappatoire déjà gratuite et illimitée — le seuil la borne et la tarife. **Résultat défavorable** : il creuse l'assiette par le bas sans la reconstituer par le haut. La forme est au Livre 11, **le montant est une décision D2** |
| Dérogation | accès **automatique** plutôt que déclaratif | à écrire (A13) |

**Ce que l'arbitrage ne peut pas trancher, et qui n'est pas de son ressort.** Il
manque **deux nombres**, et ils ne se comblent pas par un arbitrage mais par une
lecture : **l'élasticité de l'empreinte au revenu**, qui décide du signe de
l'incidence du premier ressort ; et **la composition du patrimoine par décile**,
qui décide si le demurrage atteint le sommet ou le milieu. Les deux existent,
aucun n'a été cherché, **et ils décident ensemble de la nature politique du
dispositif.**

### A15 — La forme de la trajectoire — TRANCHÉ le 2026-09-05

**Origine : instruction de conception de l'auteur** du 2026-09-05 : « Il convient,
je pense, d'appuyer l'idée d'une progressivité de la mise en place de ces
dispositifs. De sorte que les industries aient le temps de remettre en question
leurs processus pour le rendre moins impactants. » Instruite en L11.C10.

**Le principe n'est pas en cause, et le corpus le porte au crédit de l'auteur.**
Un instrument qui prétend déclencher un investissement de transformation doit
laisser le temps de l'amortissement, faute de quoi il **perçoit sans orienter**.
La progressivité est donc une condition de fonctionnement, pas un adoucissement —
et elle rejoint le « tâtonnement » que Tinbergen prescrit lorsque les
conditions-limites ne peuvent être satisfaites.

**Ce que l'arbitrage doit trancher est la FORME, et il y en a trois.**

| Forme | Crédibilité | Prévisibilité pour l'investisseur | Exposition à Lucas |
|---|---|---|---|
| **Calendrier de dates** | faible — un report est une décision, et l'échéance est le moment où la pression est maximale | forte | maximale — fenêtre datée, donc exploitable |
| **Formule publiée** | moyenne — écrite d'avance, mais révisable | moyenne | forte |
| **Indexation sur une observation** — le taux monte quand le substitut est effectivement disponible | **forte** — reporter suppose de nier un fait, non de prendre une décision | **faible** | atténuée — la fenêtre n'est plus datée |

**Ce que le corpus recommande sans trancher.** La troisième forme, pour une
raison de cohérence interne et non de préférence : L11.C06 § 3 a établi que la
carte des classes du barème **est** la carte des substitutions praticables. Une
trajectoire indexée sur la disponibilité du substitut en est le prolongement
direct — *le taux monte quand la substitution devient possible, c'est-à-dire
quand la classe devient utile.*

**Ce que cette recommandation coûte, et il faut l'énoncer.** On échange **une
prévisibilité qui n'est pas crédible contre une crédibilité qui n'est pas
prévisible**, et rien n'établit que le second terme vaille mieux. Et la question
de gouvernance ne disparaît pas : elle se déplace de la date vers le constat —
qui déclare un substitut disponible déclenche la hausse. **A4 la reçoit.**

**Un point qui corrige une intuition, et il n'est pas favorable.** On attend
d'une trajectoire longue qu'elle protège les petits. **Elle profite d'abord à
ceux qui peuvent investir pendant qu'elle court** — capital et capacité de
prévision. La petite entreprise affronte le même taux final avec moins de moyens
d'étaler. **La durée seule ne rend pas la progressivité équitable**, et une
trajectoire différenciée selon la capacité d'investissement est à instruire, ce
qui ajoute une dimension au barème.

**Ce qui bloque A15.** Lucas 1976, Kydland-Prescott 1977 et Friedman 1968 portent
l'argument du chapitre et **aucun n'a été ouvert**, à leur troisième emploi. Les
trois sont libres en ligne. Voir ci-dessous, F7.

**TRANCHÉ LE JOUR MÊME PAR L'AUTEUR.** Texte de l'arbitrage : « *Le taux monte
quand le substitut est effectivement disponible — capacité et prix constatés —
et non à une date fixée d'avance.* **OUI !** » **La troisième forme est
retenue.**

**CE QUE L'ARBITRAGE OUVRE, et il faut l'instruire avant toute rédaction du
barème.**

**1. Le défaut propre de la forme retenue, et il est lourd.** Une trajectoire qui
monte lorsque le substitut apparaît **ne monte jamais là où aucun substitut
n'apparaît**. Les secteurs les plus verrouillés — ceux dont les procédés n'ont
pas d'alternative connue — sont exemptés par construction et indéfiniment. Or ce
sont ceux qu'il faudrait atteindre en premier. **On a troqué une trajectoire qui
FORCE la technique contre une trajectoire qui la SUIT**, et gagné en crédibilité
ce qu'on a perdu en capacité d'entraînement.

**Réparation proposée, non tranchée, et cohérente avec A8.** Là où aucun
substitut n'existe, l'instrument qui agit n'est pas le reflux : **c'est
l'émission.** Financer le développement de l'alternative relève du barème de
qualification — exactement comme L11.C03 § 4 a établi que l'abondance des
essentiels relevait de la qualification et non d'un taux. **Le reflux suit la
technique ; l'émission la provoque.** C'est la deuxième fois que A8 fournit la
réparation d'un défaut apparu ailleurs. Prix de cette réparation : elle charge le
barème de qualification d'une fonction de plus, et suppose qu'un financement
suffise à faire apparaître une technique — ce que le Livre 5 devra instruire.

**2. Ce que « disponible » veut dire.** L'arbitrage dit « capacité et prix
constatés » et ne fixe pas les seuils. Un substitut vendu au triple du prix est
techniquement disponible et économiquement absent. **Il faut donc deux seuils** :
une part de capacité, et un rapport de prix — et ces deux seuils sont eux-mêmes
un barème.

**3. Qui constate.** La question de gouvernance ne disparaît pas, elle se
déplace de la date vers le constat : **qui déclare un substitut disponible
déclenche la hausse.** A4 la reçoit, et elle n'est plus hypothétique.

**4. Ce que l'arbitrage ne fait pas.** Il ne vérifie aucune des trois sources non
ouvertes sur lesquelles le chapitre repose, et il ne supprime pas le constat que
**la durée seule ne rend pas la progressivité équitable** — une trajectoire
longue profite d'abord à qui peut investir pendant qu'elle court.

**5. CONFORTÉ LE 2026-09-06, sur le chapitre X de Tinbergen.** L'arbitrage rendu
par l'auteur n'est pas une invention : **il figure dans la typologie reçue des
remèdes à l'incertitude.** Tinbergen en énumère trois — « uncertainty sometimes
is removed by (a) **choosing some average** [...] or (b) **WAITING FOR SOME
IMPORTANT DECISIVE FACTOR THAT IS AS YET UNKNOWN**, or (c) the application of the
**rule of simplicity** (e.g. taking an integer number for a price to be fixed by
government if the relevant interval is only known approximately) ».

**(b) est exactement la trajectoire indexée** : on n'arrête pas la date, on
attend le facteur décisif — la disponibilité du substitut. L'auteur a retrouvé
seul l'une des trois voies que la théorie nomme.

**Et (c) répond à deux questions ouvertes du livre.** La règle de simplicité —
prendre un nombre entier quand l'intervalle n'est connu qu'approximativement —
est la réponse au « combien de classes » de A10 et de L11.C06 § 3, et le pendant
du refus de la fausse précision du chapitre VII. **Elle a un second motif, qui
n'est pas épistémique mais politique** : parmi les facteurs qui influencent la
politique **à tort**, Tinbergen range « **the aversion of the complex** : many
officials [...] dislike to accept somewhat more complicated reasonings or the
results of calculations even if from the scientific point of view they are
decidedly better than the rules of thumb often accepted before ». **Un barème
plus juste mais plus complexe peut être rejeté pour cette seule raison. La
simplicité n'est pas qu'une hygiène : c'est une condition d'adoption**, et le
corpus ne l'avait inscrite nulle part.

### A16 — La légitimation de l'organe qui arrête les valeurs — OUVERT le 2026-09-05

**Origine : L11.C11**, qui rassemble les questions que quatre chapitres avaient
poussées vers A4 et montre qu'elles ne portent pas sur le même objet.

**LA DÉCOMPOSITION, et c'est l'apport qui dissout le caractère binaire de A4.**
Arrêter un barème n'est pas une décision mais **quatre**, de natures
différentes, qui n'appellent pas la même institution.

| | L'acte | Nature | Rythme |
|---|---|---|---|
| **D1** | Fixer la **méthode** | règle | rare, quasi constitutionnel |
| **D2** | Fixer les **valeurs** | norme | périodique |
| **D3** | **Constater** qu'un substitut est disponible | fait | continu, sectoriel |
| **D4** | **Trancher un recours** | juridiction | au cas par cas |

**Le livre n'en distingue aucune**, et c'est ce qui rendait A4 insoluble tant
qu'il était posé comme un choix d'échelle.

**CE QUE LA DÉCOMPOSITION RÈGLE.** La contrainte tirée de Mundell — le rendement
doit être uniforme sur le périmètre, sinon l'écart est arbitré — **ne porte que
sur D2**. D'où une réponse à A4 que ni l'une ni l'autre de ses branches ne
portait : **valeurs centralisées, constats et recours décentralisés.** C'est le
principe d'affectation appliqué à la gouvernance elle-même. *(Réserve : la
contrainte est transposée d'un résultat sur les taux d'intérêt ; elle vaut pour
le demurrage, elle n'est pas établie pour le prélèvement sur les transactions —
il se pourrait donc que seul le second ressort doive être uniforme. L11.C04 a
été précisé en conséquence.)*

**CE QUE LA DÉCOMPOSITION N'ÉLIMINE PAS, et c'est l'objet de A16.** P52 vise
**exactement la même décision que Mundell, en sens contraire** :

> **Les valeurs doivent être uniformes** — sinon l'écart est arbitré et le
> dispositif se vide.
> **Des valeurs uniformes décident de la souveraineté** — et aucune légitimité
> ne les fonde.

**Deux issues, et deux seulement.** Légitimer l'organe qui arrête les valeurs —
c'est A16. Ou rompre le lien entre le barème et l'équilibre extérieur établi en
L1.C27 — **ce qui sacrifierait la face favorable de P52**, c'est-à-dire la
meilleure réponse du livre à l'objection extractiviste. La seconde issue coûte
plus cher qu'il n'y paraît.

**CE QUE LE CORPUS A POUR RÉPONDRE : rien, et son seul précédent est
décourageant.** L'allocation de DTS de 2021 a réparti l'équivalent de 650
milliards de dollars au prorata des quotes-parts, dont **environ 3,3 % aux pays
à faible revenu** (P31). C'est le seul organe mondial existant qui arrête une
clé chiffrée, et sa clé produit l'inverse du but poursuivi. **Trois précédents
publics restent à ouvrir** : quotes-parts du Fonds et leur révision, règle d'une
voix par membre à l'OMC et ce qu'elle produit en pratique, rotation du conseil
des gouverneurs de la BCE.

**À TRAITER AVEC P31.** Les deux demandent la même chose : **une règle de
représentation qui ne reconduise pas le poids économique.** Les traiter
séparément produirait deux réponses possiblement incohérentes.

### A17 — Le calibrage du barème de qualification face à l'asymétrie des erreurs — OUVERT le 2026-09-06

**Origine : L11.C13**, premier chapitre du Livre 11 sur le versant émission. Le
barème de qualification ne répartit pas une charge : **il crée le flux.** Il en
résulte une asymétrie que le corpus n'avait pas relevée.

| L'erreur | Ce qu'elle produit | Quand on s'en aperçoit |
|---|---|---|
| **Sur-qualifier** | de la monnaie émise **sans contrepartie réelle** — l'objection de Rueff que L1.C21 existe pour écarter | tard, par l'effet agrégé |
| **Sous-qualifier** | **l'essentiel demeure non financé** — l'échec du but poursuivi | **jamais**, faute de contrefactuel |

**Ce que l'arbitrage doit trancher.** Les deux fautes n'ont pas la même
détectabilité. La sur-qualification finit par se voir : la monnaie circule et
l'effet promis manque. **La sous-qualification ne se voit pas** — le projet non
certifié n'existe pas, et rien ne signale son absence. **Un barème calibré sur
ce qui s'observe sera donc systématiquement trop strict**, d'autant plus que
l'autorité redoutera l'erreur visible. Faut-il corriger ce biais, et par quoi ?

**Ce qui rend l'arbitrage difficile, et qu'il faut avoir en tête.** Corriger vers
la sur-qualification, c'est accepter d'émettre parfois contre rien — donc
affaiblir la réponse à Rueff, qui est la raison d'être du reflux. Ne pas
corriger, c'est accepter que le dispositif finance moins que ce qu'il pourrait,
**et sans jamais savoir de combien.**

**Ce que le corpus ne peut pas encore instruire.** L'additionnalité suppose un
contrefactuel — établir que l'acte n'aurait pas eu lieu sans l'émission —, or
L11.C10 a établi que l'annonce d'un dispositif déforme les comportements avant
qu'il n'existe. **Le contrefactuel est déformé par l'annonce du barème qu'il doit
servir à calibrer.**

**Un conflit d'exigences à trancher en même temps.** Le registre nomme trois
remèdes à l'objection de Goodhart (P25) : révision périodique, **indicateurs non
annonçables à l'avance**, ou audit contradictoire des pratiques. **Le deuxième
contredit frontalement L11.C12**, qui exige qu'un barème soit une directive
publiée. **On ne peut pas à la fois publier la fonction et cacher l'indicateur.**
Le corpus tient les deux exigences pour fondées et n'a pas de sortie.

### A18 — Le statut des six familles du tableau de bord — OUVERT le 2026-09-06

**Origine : L11.C14.** Depuis que L11.C12 a établi qu'un barème est une
**directive** — une fonction des données observées —, le tableau de bord cesse
d'être le cinquième barème pour devenir **l'entrée des quatre autres**. Il est
donc antérieur, alors que le plan du livre le plaçait en dernier.

**Ce que l'arbitrage doit trancher : le statut de chaque famille.** Tinbergen
sépare les DONNÉES — « external to the economic complex considered [...] as far
as not under the command of the authority » — des VARIABLES-OBJECTIFS. **Une
directive lit les premières.** Appliquée aux six familles, la distinction les
coupe en deux :

| Famille | Statut proposé par le corpus |
|---|---|
| biosphérique | **objectif** — le dispositif existe pour l'améliorer |
| sociale | **objectif** — finalité explicite de l'auteur |
| économique réelle | mixte |
| financière | mixte |
| monétaire | **condition** au sens du ch. II — expression technique d'une politique saine |
| internationale | **donnée**, sauf à couverture complète |

**Pourquoi cela ne peut pas attendre.** Faire lire à une directive ce qu'elle est
censée produire est **une boucle de rétroaction, non une règle de politique** —
ce qui peut être un bon dispositif, mais auquel les résultats de L11.C12 sur la
falsifiabilité et la crédibilité ne se transportent pas sans examen.

**Et le compte de L11.C03 en dépend.** Si les familles COMMANDENT, elles sont des
cibles et non des indicateurs, et **le compte des objectifs s'aggrave d'autant.**
De combien ? Le corpus ne le sait pas : il faut savoir lesquelles le dispositif
entend **améliorer** et lesquelles il se contente d'**observer**. **A18 est donc
préalable au compte et non consécutif.**

**Ce que l'arbitrage doit trancher en second.** Publier la règle d'agrégation, ou
renoncer à commander. Un indice composite assumant ses pondérations et un tableau
de bord qui informe sans commander sont **l'un et l'autre tenables** ; ne choisir
ni l'un ni l'autre ne l'est pas — et c'est la position actuelle.

**Le cas qui doit être traité en premier par la règle, parce que le dispositif le
produit lui-même.** Le succès sur la famille biosphérique contracte l'assiette
dégénérative et dégrade la famille monétaire (L1.C21 § 6, F1). **La seule règle
énoncée par le Cahier prescrit quoi faire quand la biosphère va mal et se tait
sur le moment où le bouclage se défait parce qu'elle va bien.**

**Une règle que le chapitre énonce et qui ne dépend d'aucun arbitrage.** Si la
trajectoire est indexée sur un constat (A15), **ce constat doit être aussi
public et aussi contestable que la table elle-même.** D3 est la décision la plus
exposée à la capture — technique, sectorielle, répétée, et de conséquence
monétaire immédiate : *déclarer qu'un substitut n'est pas encore disponible,
c'est repousser la hausse sans avoir à la contester.* **Un barème publié adossé
à des constats opaques n'est pas une règle : c'est un pilotage discrétionnaire
déguisé, et il tombe sous F7 par la porte de service.**



### A19 — Le critère de révision des parités du référentiel — OUVERT le 2026-09-06

**Origine : L11.C15.** Troisième des cinq barèmes de A8. L1.C26 § 3 avait laissé
la procédure de révision vide ; L1.C28 § 6 a relevé sous P54 le seul critère que
l'ouvrage nomme. **Trois réponses incompatibles figurent désormais au dossier**,
et la position actuelle du dispositif est la seule des trois qui ne soit pas un
objet de conception.

| | La réponse | D'où elle vient | Ce qu'elle fait de la parité |
|---|---|---|---|
| **1** | fixe, non révisable — « fixes par conception » | L1.C26 | une **constante** |
| **2** | révisable, sans procédure — « restent à discuter » | L1.C26 § 3 | une **décision** |
| **3** | révisable sur critères, dont **la croissance du PIB** | L1.C28 § 6, P54 | une **fonction** |

**Ce que l'arbitrage doit trancher en premier : une constante ou une directive.**
L11.C12 a établi qu'un barème est l'un ou l'autre — il n'y a pas de troisième
forme. La réponse 2 n'en est donc pas une : c'est l'absence de forme. **La
constante est parfaitement tenable** — maximalement crédible, et L1.C26 a porté
au crédit du dispositif qu'aucune parité ne peut être attaquée faute de marché
où l'attaquer — **au prix de ne jamais absorber un déséquilibre réel**, que le
solde commercial déverse alors intégralement sur la masse monétaire interne
(P50).

**Le point le plus net, et il ne vient d'aucune objection extérieure.** Le seul
critère de révision que l'ouvrage nomme est **la croissance du produit intérieur
brut** — dans un livre dont L1.C28, « Au-delà du PIB », est tout entier consacré
à établir que cet agrégat ne mesure pas ce qui compte. Le conditionnel est de
l'auteur et l'énoncé est prospectif ; **mais c'est le seul critère nommé de tout
l'ouvrage, et une conjecture qui reste seule finit par tenir lieu de position.**

**La sortie proposée par P54 tient, mais restreinte par A18.** Prendre les
critères dans le tableau de bord reste juste — sauf que L11.C14 vient d'établir
que la moitié de ses familles sont des **objectifs**, non des données. Indexer la
parité sur la famille biosphérique ferait lire à une directive ce qu'elle est
censée produire. **Seules les familles qui échappent au commandement de
l'autorité peuvent servir d'entrée** : l'internationale, et la part subie des
familles économique réelle et financière. Cela ramène très près des critères
classiques d'ajustement d'un change fixe, ce qui est un renseignement en soi.
**A19 est donc postérieur à A18.**

**Ce que l'arbitrage doit trancher en second : qui supporte la révision.**
L'arbitrage du 2026-09-05 a établi que le Symposium détient des avoirs en
monnaies nationales (L11.C01). **Une révision de parité les revalorise : c'est un
transfert, et personne n'a dit qui le supporte.** Trois réponses, qui ne se
valent pas — le Symposium l'absorbe, et ses fonds propres déjà négatifs entre
émission et reflux s'en trouvent chargés (L11.C02 § 2) ; le membre l'absorbe, et
la révision devient une sanction ; ou l'on répartit, et il faut une clé, qui est
P31 sous un autre nom. **Une révision dont on ignore qui la paie sera reportée.**

**Le mécanisme, lui, est déjà connu du corpus.** Une parité « fixe mais
ajustable » promet un ajustement que l'autorité aura intérêt à différer
précisément lorsqu'il deviendra nécessaire — c'est l'incohérence temporelle que
L11.C10 § 2 a traitée sur la trajectoire. **Le dispositif hérite donc, sur les
parités, du problème qu'il a résolu ailleurs.**

**La forme de sortie est celle que l'auteur a lui-même retenue en A15.**
*Révision déclenchée par un écart constaté franchissant un seuil publié* est une
directive au sens strict, elle échappe au reproche de la réponse 2, et elle rend
le report coûteux — différer supposerait de nier un fait plutôt que d'arbitrer
une opportunité. C'est chez Tinbergen le troisième remède reconnu à l'incertitude.
**Elle coûte ce que coûtait A15 : on échange une prévisibilité non crédible
contre une crédibilité non prévisible**, et un exportateur a besoin de la
première pour investir. Le corpus ne prétend pas que le second terme vaille mieux.

**Ce qui bloque la spécification.** L'observable qui s'impose est l'écart de
productivité entre secteurs exposés et abrités (Balassa 1964, Samuelson 1964,
versés en L1.C26 § 6). **Ces deux textes ne sont pas ouverts**, et le corpus
refuse de spécifier une donnée de directive sur une littérature qu'il n'a pas
lue. Portés en acquisition.

**Et une source manque sur le précédent.** L11.C15 § 6 affirme qu'un régime fixe
mais ajustable a déjà échoué par report politique de l'ajustement. **Le corpus le
tient de sa culture générale**, alors qu'il dispose de Keynes CW XXV et
d'Eichengreen, tous deux acquis. Rien n'en doit sortir hors corpus avant lecture.


### A20 — La valorisation des communs, et ce qu'elle décide vraiment — OUVERT le 2026-09-06

**Origine : L11.C16.** Dernier des cinq barèmes de A8, **seul porteur d'une
promesse bloquante** (P52). L11.C11 § 4 avait isolé le nœud, L11.C13 § 3 l'avait
domicilié en **D2 — fixer les valeurs** ; le chapitre l'instruit. **Il compose
avec A4 et A16 sans s'y réduire**, et il durcit P52 au lieu de l'alléger.

**Ce que le corpus n'avait pas vu, et qui change la question.** Le NIVEAU de la
valorisation n'est pas une décision : la condition de bouclage le lie au produit
du reflux, lui-même borné par B1 — au-delà d'un taux compris entre −0,5 % et
−1 %, l'évitement devient massif. **L'Assemblée des Communs ne décide donc pas
combien de monnaie existe : elle décide comment se partage une enveloppe
plafonnée.**

| | Ce qui est décidé | Par qui, ou par quoi |
|---|---|---|
| **Le niveau** | contraint par le bouclage, borné par B1 | ni l'Assemblée, ni personne |
| **La structure** | décidé — c'est **D2**, domicile de P52 | l'Assemblée des Communs |

**Et cela aggrave P52.** À plafond atteint, la valorisation est un **partage à
somme quasi nulle entre membres** : relever la valeur d'un acte abaisse en termes
réels tout ce que le barème ne relève pas. **Ce n'est plus seulement qu'une
institution non élue décide de la solvabilité extérieure de ses membres — elle la
décide aux dépens les uns des autres.** La nuance qui limite le résultat : la
somme n'est nulle qu'à saturation. **Mais la thèse du dispositif est que
l'essentiel insolvable est immense (L1.C15) : la saturation est l'état visé, non
le cas extrême.**

**Ce que l'arbitrage doit trancher en premier : le couple, pas la table.** La
même table doit ORDONNER les actes selon leur mérite écologique et BOUCLER un
volume monétaire — un instrument, deux objectifs, ce que la règle du compte
interdit. **Le couple ne se ferme qu'avec le taux de reflux**, qui commande
l'autre membre de l'égalité. **A8 est ainsi démontré une troisième fois, et pour
la première fois par déduction** : l'interdépendance se lit dans l'égalité de
bouclage, elle n'a plus besoin d'être invoquée.

**Ce que l'option polycentrique fait, et ce qu'elle ne fait pas.** L1.C22 § 2
avait enregistré la sortie — norme votée au centre, qualification instruite à
l'échelle d'emploi, émission centrale. **Rapportée aux quatre décisions, elle
rend D3 local et laisse D2 central**, c'est-à-dire qu'elle ne touche pas le
domicile du nœud. **Et la polycentricité est interdite sur D2** par le résultat
que L11.C04 § 6 tire de Mundell : un barème modulé nationalement recrée la
contrainte qu'un barème global annule. Conjoint au second argument d'Ostrom — une
unité gouvernementale unique est « inherently weak because of free-rider
problems » —, cela donne une alternative dont les deux branches sont mauvaises :
**uniforme il est arbitraire, non uniforme il est arbitré.**

**Ce que l'arbitrage doit trancher en second : la révisabilité.** La forme
directive (L11.C12) s'applique — voter la FONCTION plutôt que la table. Elle
supprime la surface d'influence annuelle que L11.C11 § 6 identifiait comme la
plus dangereuse et rend le favoritisme coûteux. **Mais elle concentre la question
de souveraineté dans un acte unique** : une fonction choisie une fois détermine
la balance des paiements de chaque membre pour toute sa durée de vie. **Et
l'exigence de révisabilité est ici plus forte que sur les quatre autres barèmes**
— une fonction mauvaise sur un taux de reflux se corrige à la révision suivante,
une fonction mauvaise sur la valorisation prive durablement un membre de sa
capacité d'importer — **alors même que la crédibilité y demande l'inverse.**

**Un point sans arbitrage possible : il n'existe pas de valeur par défaut
défendable sur ce barème.** Un défaut bas ferme le canal d'émission — nul ne
restaure à perte ; un défaut haut EST la sur-qualification, l'erreur dont
L11.C13 § 2 établit qu'on ne s'aperçoit que tard. **La sortie métrologique de
L11.C06 n'est pas disponible ici**, et c'est la troisième fois que les deux
versants du circuit refusent de se transporter — après l'inversion de la
métrologie et le changement de face du défaut. **Le corpus enregistre que la
symétrie émission/reflux, que le dispositif présente comme son architecture, ne
vaut pas au niveau des instruments.**

**Douzième condition-limite versée à L11.C03 § 5.** **B12 — la valorisation d'un
acte ne peut descendre sous le coût de le réaliser.** Inégalité au sens de
Tinbergen : elle mord dès que l'enveloppe se resserre, donc dans l'état de
saturation qui est l'état visé. Six des douze ne mordent que sous tension.

**Un chiffrage que le corpus nomme et ne fait pas.** Enveloppe plafonnée et
valeur unitaire plancher donnent **un nombre maximal d'actes finançables par
an**, à comparer à l'ampleur de l'essentiel insolvable (L1.C15). Personne n'a
comparé les deux grandeurs. Relève de F1, classe (d).

**Et deux promesses jamais instruites composent, ce que P52 demandait
explicitement.** P35 — la restauration est lente et capitalistique quand le
besoin de liquidité est immédiat — et P50 — sous parité fixe, le déséquilibre
commercial se déverse intégralement sur la masse monétaire interne. **Composées :
la contraction arrive au règlement du solde ; le recours exige un capital que la
contraction vient de retirer et produit son effet après des années.** C'est le
mécanisme de Friedman sur un TROISIÈME instrument, par une voie entièrement
distincte — non plus le délai de transmission monétaire, mais le délai
biologique. **Le corpus marque qu'il tient ce délai pour évident sans l'avoir
établi sur aucune source.**

**Enfin P43 limite la face favorable.** La contrainte extérieure n'est pas levée
mais **rebasée** sur la nature encore fonctionnelle, dotation au moins aussi
inégalement distribuée que les actuelles. Le transfert vers les pays riches en
fonds naturels est réel ; **il ne bénéficie pas aux pays pauvres en fonds
naturels**, souvent les mêmes que ceux que le dispositif entend servir.



### A21 — La forme du seuil d'exemption pour les personnes morales — OUVERT le 2026-09-06

**Origine : L11.C18.** Dernière pièce que le chantier des barèmes gardait en
propre après le routage du périmètre vers le Livre 7. **A21 prolonge A14 sans s'y
réduire** : A14 demande SI l'on corrige l'incidence, **A21 demande PAR QUELLE
FORME** — et A14 classait déjà ce seuil comme « manque de conception, pas un
paramètre ».

**Ce qui est établi avant l'arbitrage, et qu'il n'a pas à rouvrir.**

**La question porte sur le prélèvement sur les ENCAISSES**, non sur le
prélèvement transactionnel : l'assiette du livre est la consommation finale, où
la personne morale est collectrice et non redevable — sauf sur les acquisitions
d'actifs. **Le corpus consigne qu'il avait d'abord raisonné à l'envers**, et
qu'un chapitre entier en aurait été faux.

**Le seul seuil que le livre spécifie est déjà une directive** — indexé sur le
revenu médian. **L'auteur a donc choisi la forme directive avant que le corpus ne
la nomme, et deux fois plutôt qu'une**, l'autre étant A15. Fait favorable, versé
au même titre que les autres. Réserve : c'est la plus facile des directives, sa
donnée étant un agrégat public produit par un tiers.

**Le reproche classique ne tient pas ici, et c'est un résultat inattendu.** On
objecte d'ordinaire qu'un seuil incite à la scission. **Mais la condition-limite
B2 — la consolidation par bénéficiaire effectif est juridiquement impossible —
rend l'assiette réelle « par compte »**, de sorte que répartir ses encaisses
échappe **déjà** au prélèvement, sans borne et sans tarif. **Le seuil n'introduit
pas l'échappatoire : il la borne et la chiffre.** Si B2 tombait — registre
consolidé des détentions, transfrontalières comprises —, l'objection
redeviendrait valide.

**Ce que l'arbitrage doit trancher en premier : la forme.**

| | La forme | Sans effet de seuil ? | Coût en assiette |
|---|---|---|---|
| **1** | pas de seuil | oui | nul — mais **régressif par le coût de conformité** |
| **2** | seuil en niveau | **non** | modéré |
| **3** | **franchise** — les premiers *X* pour tous | **oui, la seule** | **le plus élevé** — proportionnel au NOMBRE de personnes morales |
| **4** | seuil indexé sur une grandeur d'exploitation | non, mais lissable | inconnu — la donnée n'est pas ouverte |

**Ce que l'arbitrage doit savoir en le tranchant : la correction se paie en
financement régénératif.** L11.C16 § 2 a établi que le produit du reflux plafonne
l'enveloppe d'émission. **Exempter réduit l'assiette, donc l'enveloppe, donc ce
qui peut être financé.** C'est le premier arbitrage du corpus dont **les deux
termes sont de même nature** — une quantité d'assiette contre une quantité
d'émission — et dont le coût est **observable** : L11.C17 § 6 établit que le
déficit d'émission est détectable en agrégat, de sorte qu'un seul chiffre porte
le prix du seuil et le contrôle du barème de qualification.

**Ce que l'arbitrage ne peut pas régler, et le corpus le dit.** Le seuil ne
corrige pas un défaut d'assiette. Si l'hypothèse de L11.C09 § 3 est exacte — le
demurrage atteint le milieu et manque le sommet, les grandes fortunes détenant
des actifs et non des encaisses —, **exempter les personnes morales creuse
l'assiette par le bas sans la reconstituer par le haut** et resserre l'incidence
sur la zone médiane déjà atteinte à tort. **La sortie est dans A12, le nœud de
prélèvement, pas dans A21.** RÉSERVE : cette hypothèse n'est toujours pas
vérifiée, la donnée existant dans les enquêtes patrimoine sans avoir été ouverte.

**Troisième occurrence du conflit efficacité / légitimité recensé par L11.C17
§ 7.** Publier la fonction du seuil rend son optimisation triviale ; ne pas la
publier, ce n'est plus une règle. **Mais ce cas-ci est moins grave que les deux
autres**, et il faut le dire : l'optimisation d'un seuil est **bornée par
construction** — on ne gagne pas plus que le montant exempté — quand celle d'un
indicateur de qualification ne l'est pas (A17). **C'est un argument pour
publier.**

**Ce qui remonte au Livre 7.** Le **niveau** du seuil est un arbitrage
distributif, donc une décision de type **D2** au sens de L11.C11. Le Livre 11
établit la forme ; **il n'arrête pas le montant.**


### A22 — L'architecture du recours — OUVERT le 2026-09-06

**Origine : L11.C19.** **D4 était la seule des quatre décisions d'un barème
qu'aucun chapitre n'avait instruite.** L11.C06 § 5 avait pourtant écrit que le
dispositif « a besoin d'une table, d'une procédure et d'un tribunal » ; le corpus
n'avait écrit que les deux premiers. **Le silence du livre est intégral** : ni
organe, ni procédure, ni délai, ni charge de la preuve.

**A22 n'est pas un chantier de plus : c'est la pièce dont trois arbitrages
attendent la forme.** A11 demande une procédure de révision gratuite et rapide —
c'est la correction nommée du biais de documentation. A13 suppose qu'une
dérogation refusée puisse être contestée. **A14 en dépend entièrement** : les
quatre biais d'incidence étant procéduraux et jamais tarifaires, **la procédure
est le seul lieu où ils se corrigent.**

**Ce que l'arbitrage doit trancher en premier : les trois garanties.** Le corpus
les déduit de la cohérence interne du dispositif et marque qu'il n'a ouvert aucun
régime de contentieux existant.

| | La garantie | Pourquoi elle n'est pas négociable |
|---|---|---|
| **1** | **indépendance** de celui qui perçoit | la valeur contestée n'est pas un montant dû mais un **classement**, et le même organe qui classe fixe l'assiette de son produit |
| **2** | **gratuité** ou quasi-gratuité | un recours payant **reproduit exactement le biais qu'il corrige** — le coût d'accès trie comme le coût de documentation |
| **3** | **délai borné et opposable**, avec **décision implicite favorable** à l'expiration | ce qui décide n'est pas le bon droit mais la capacité à porter l'écart pendant l'instance : **dix-huit mois sont une formalité pour qui a de la trésorerie et un refus pour qui n'en a pas** |

**Ce que l'arbitrage doit trancher en second : un tribunal ou quatre.** « Le
recours » recouvre **quatre objets de natures différentes** — une valeur par
défaut appliquée (technique et métrologique) ; un refus de qualification
(application d'une norme) ; une valorisation arrêtée (**distributive, c'est D2
appliquée, donc P52**) ; un refus de dérogation (administrative). **Le troisième
n'a pas de forme évidente et c'est le plus lourd** : juger une valeur, c'est la
refaire. **Le recours sur D2 est soit impossible, soit une seconde chambre de
décision déguisée.** Le corpus n'a pas de sortie et le dit.

**UN RÉSULTAT FAVORABLE QUE LE CORPUS N'ATTENDAIT PAS, et qui change le statut du
contentieux.** La valeur par défaut existe pour déplacer le coût de la mesure du
centre vers celui qui en tire avantage. **Il s'ensuit que chaque valeur contestée
puis révisée est une mesure que quelqu'un a payée et qui entre dans le barème.**
Le contentieux **produit la métrologie que F2 déclare manquante** : le recours
n'est pas un coût du système, **c'est son mécanisme d'apprentissage**, et le seul
dont il dispose. Cela **renforce la branche punitive de A11** — un défaut clément
n'engendre aucun contentieux, donc aucun apprentissage.

**ET SON REVERS, QUI EST UN SIXIÈME BIAIS DE CONCENTRATION — le premier qui se
compose avec le temps.** Ceux qui contestent sont ceux que L11.C09 a nommés :
intégrés, documentés, structurés, conseillés. **La métrologie acquise reproduit
donc la structure de qui a les moyens de contester.** Le barème devient précis là
où les requérants sont équipés et **reste grossier là où personne ne conteste** —
c'est-à-dire dans les secteurs que le dispositif vise. **Et le défaut grossier est
punitif** : ces secteurs paient indéfiniment un plein tarif dont personne ne
démontrera qu'il est faux. **C'est aussi le seul biais qui s'aggrave quand le
dispositif fonctionne bien**, puisqu'il se nourrit du contentieux. La correction
connue — instruire d'office la révision des classes sans contentieux — revient à
**dépenser au centre la mesure qu'on avait voulu déplacer**, et le motif
administratif de Tinbergen dit que personne ne l'entreprendra pour ceux qui ne se
plaignent pas.

**Ce que le recours ne couvre pas, et ce qui le complète.** Il ne corrige que les
erreurs dont quelqu'un se plaint, et L11.C13 § 2 a établi que la plus grave n'a
pas de plaignant — **le projet non certifié n'existe pas.** L11.C17 § 6 fournit
l'autre moitié : le bouclage rend détectable en agrégat la sous-qualification
systématique. **Le recours et le bouclage couvrent deux populations disjointes et
aucun ne remplace l'autre.**

**Ce qui remonte au Livre 7 :** **qui juge.** C'est D4, donc une question
d'organe, comme le niveau du seuil (A21) et comme les valeurs elles-mêmes.

**UNE LIMITE POSÉE À UN RÉSULTAT ANTÉRIEUR.** L11.C17 § 4 établissait que la
réponse commune aux barèmes existe et se nomme **directive**. **Le recours n'en
est pas une et ne peut pas l'être** : ce n'est pas une fonction des données, c'est
une adjudication. **La forme directive répond à la question du BARÈME, non à celle
du DISPOSITIF** — et L11.C06 § 4 avait raison plus tôt : un barème est trois
objets, et **seul le premier est une directive.**


### A23 — La procédure d'amendement de la directive — OUVERT le 2026-09-06

**Origine : L11.C20.** **C'est la quatrième exigence que L11.C12 avait posée sans
la remplir** — une directive doit contenir « sa propre procédure d'amendement,
faute de quoi elle n'est qu'un pilotage discrétionnaire muni d'étapes ». Trois
des quatre ont été instruites ; **celle-ci porte tout l'appareil et elle était
vide.** Sans elle, **A7, A19, A20 et A21 sont des choix de forme sans mode
d'emploi**, et la réponse apportée à A7 par la directive ne vaut pas mieux qu'une
table.

**Ce que l'arbitrage doit trancher en premier : séparer deux objets que le
dispositif confond.**

| | L'objet | Ce qui change | Qui décide |
|---|---|---|---|
| **La variation** | la fonction lit des données nouvelles | **le taux** | **personne** — c'est un calcul |
| **L'amendement** | la fonction est réécrite | **la règle** | une autorité, par décision |

Le dispositif annonce un « ajustement annuel des taux » **sans dire lequel des
deux il désigne**. **Présenter un amendement comme une variation est une
soustraction au contrôle**, et c'est le mode d'échec le plus probable de la forme
directive.

**LE CRITÈRE QUI LES SÉPARE EST EXÉCUTABLE, et c'est l'apport principal.**

> **Une variation est reproductible par un tiers ; un amendement ne l'est pas.**

Fonction publiée plus données publiées : n'importe qui recalcule et retrouve le
nombre. **Un écart entre le taux annoncé et le taux recalculé est la signature
d'un amendement non déclaré**, détectable avec une feuille de calcul et sans
accès aux délibérations. **Second test exécutable du Livre 11**, après le critère
d'échec terminal de Tinbergen (L11.C03). **Il impose une exigence d'archivage** :
publier la fonction ne suffit pas, il faut publier **les données dans l'état exact
où la fonction les a lues**, horodatées — sans quoi le test tombe. C'est la
disposition la moins coûteuse du dispositif.

**Ce que l'arbitrage doit trancher en second : la rétroactivité, et aucune branche
n'est gratuite.** Rétroagir en alourdissant détruit la propriété pour laquelle la
directive a été choisie. Ne pas rétroagir crée une **prime à l'ancienneté** :
l'installation ancienne et plus dégénérative garde son classement favorable et
paie moins que celle qui la remplacerait — **le barème punit ce qu'il voulait
encourager**. RÉSERVE : le corpus impute cet effet à l'attribution fondée sur les
positions acquises **sans l'avoir vérifié sur source**.

**Et l'auteur a déjà réglé ce point sur un barème, sans que personne ne le
relève.** A15 indexe la hausse sur la disponibilité **constatée** du substitut :
**un changement déclenché par un fait public ne surprend personne**, donc la
rétroactivité ne se pose pas dans les mêmes termes. **Troisième bénéfice de cet
arbitrage**, après la crédibilité et le coût du report. **Il ne couvre pas les
amendements de doctrine — qui sont ceux qui alourdissent.**

**RÈGLE DE CONCEPTION PROPOSÉE PAR LE CORPUS, marquée comme proposition et non
comme résultat.** Deux exigences établies s'opposent : la crédibilité demande de
ne pas réécrire (L11.C10, L11.C12), la révisabilité est plus nécessaire là où
l'objet est irréversible (L11.C16 § 6). **La sortie n'est pas dans le rythme,
elle est dans la fonction.**

> **La fréquence d'amendement admissible est inverse de l'irréversibilité de ce
> que le barème commande ; et ce qu'on retire en fréquence doit être rendu en
> conditionnalité.**

Une fonction qui prévoit le cas n'a pas besoin d'être amendée quand il survient —
d'où l'intérêt de lui faire lire les conditions-limites, qui sont des inégalités
ne mordant que lorsqu'elles sont menacées. **Conséquence inattendue :
l'exigence est maximale sur la valorisation, là où la matière est minimale.**

**Une convergence à enregistrer, et c'est une impasse.** L11.C19 § 7 a établi que
le recours contre une valorisation n'a pas de forme — juger une valeur, c'est la
refaire. **L'amendement d'une valorisation rencontre la même impasse par l'autre
côté** : l'enveloppe étant plafonnée, tout amendement qui relève une valeur en
abaisse d'autres en termes réels, donc **c'est un transfert entre membres**, comme
une révision de parité. **Sur D2, le recours et l'amendement sont deux noms de la
même décision**, et cette décision est celle que P52 déclare illégitime sans
organe légitimé — soit A16, toujours sans matière.

**QUATRIÈME OCCURRENCE DU CONFLIT EFFICACITÉ / LÉGITIMITÉ, ET LE CORPUS CHANGE
LE STATUT DE L'OBSERVATION.** Une directive **sans terme** se pérennise par
inertie — ne rien faire suffit à la maintenir. Une directive **à terme fixe**
force l'amendement à être une décision active et détruit la crédibilité, chacun
anticipant la renégociation. **Après A17, A20 et A21, c'est la quatrième
occurrence par un quatrième chemin indépendant.** Le corpus cesse de les traiter
comme des difficultés locales : **c'est une propriété de gouverner par barème.**

**EXIGENCE DE RÉDACTION QUI EN DÉCOULE, et elle vaut pour tous les arbitrages de
barème à venir :** **chacun doit énoncer de quel côté il paie — efficacité ou
légitimité — et le corpus refusera tout arbitrage qui prétend ne pas payer.**


### A24 — L'architecture de la perception — OUVERT le 2026-09-06

**Origine : L11.C21.** La chaîne par laquelle le produit du reflux va du payeur à
l'institution émettrice **n'a jamais été instruite** : le corpus avait retenu
comme solide l'argument selon lequel « le mécanisme de perception existe sous la
forme de la taxe sur la valeur ajoutée », et **aucun chapitre n'avait demandé qui
perçoit, à qui le produit va, dans quel délai, ni qui contrôle celui qui
perçoit.** Ni le livre ni le Cahier ne répondent.

**Pourquoi la question existe maintenant et n'existait pas avant.** L'arbitrage de
l'auteur du 2026-09-05 a retenu la **lecture B** : le produit n'est pas éteint au
paiement, **il arrive quelque part et y demeure.** Sous la lecture écartée il n'y
avait ni chaîne, ni délai, ni destinataire.

**CE QUE L'ARBITRAGE DOIT SAVOIR EN PREMIER : l'argument de praticabilité est
plus faible que le corpus ne l'avait retenu.** La machinerie de la taxe sur la
valeur ajoutée existe et se transporte — déclaration, autoliquidation, contrôle,
contentieux. **Son motif ne se transporte pas.** Sous ce régime, l'administration
perçoit **pour l'État dont elle relève** : le produit alimente son budget, le
contrôle sert son intérêt. **Ici, elle percevrait pour une institution
supranationale, sur une somme qui quitte son économie.** Le corpus ne retire pas
l'argument ; il en réduit la portée.

**Et l'effet redouté n'est pas un refus, ce qui le rend difficile à traiter.** Un
État qui refuse de percevoir est visible et sanctionnable. **Un État qui perçoit
sans zèle ne l'est pas** : effectifs de contrôle, priorités d'audit, rythme des
relances — tout cela relève de son administration intérieure et **aucun engagement
ne le mesure.**

**UNE FIGURE NOUVELLE DANS LE DOSSIER, et rien ne la traite.** L1.C27 tient le
passager clandestin pour un non-membre profitant d'un bien collectif, et le
dispositif y répond par le prélèvement aux frontières et le seuil d'activation
(P51). **Le passager clandestin interne échappe aux deux** : il est dans le club,
il applique le barème, et il perçoit à quatre-vingts pour cent.

**L'argument d'Ostrom change de place.** L11.C16 § 5 l'employait sur la fixation
des valeurs. **Il porte avec plus de force sur la perception** : sur les valeurs,
il dit que l'organe central décidera mal ; **sur la perception, il dit qu'il ne
sera pas obéi** — « inherently weak because of **free-rider problems** », ce qui
est son sens propre.

**Ce que l'arbitrage doit trancher : trois architectures.**

| | L'architecture | Ce qu'elle règle | Ce qu'elle coûte |
|---|---|---|---|
| **1** | administrations nationales, remise à l'institution | machinerie existante, coût marginal faible | **le motif ne se transporte pas**, et le contrôle n'a pas d'organe |
| **2** | **les banques, au règlement** | le flotteur disparaît presque | **change l'assiette** — c'est le prélèvement par paiement, qui frappe le chiffre d'affaires cumulé (L11.C05 § 2). Sort du champ : relève de A10 |
| **3** | **organe propre** | alignement parfait, le percepteur est le bénéficiaire | **c'est une administration fiscale mondiale**, et L11.C01 § 6 a établi que le dispositif y tend déjà |

**UN MÉCANISME D'ALIGNEMENT EXISTE DANS UN RÉGIME VOISIN, NON OUVERT.** L'Union
européenne fait percevoir ses ressources propres par les administrations
nationales **en leur laissant un pourcentage au titre des frais de perception** —
c'est-à-dire en rendant le percepteur intéressé au produit. **C'est exactement la
réponse au défaut de motif**, et le corpus refuse de la détailler avant lecture.
**Portée en acquisition, priorité 2.**

**TROISIÈME DÉLAI DU DISPOSITIF, trouvé par une voie indépendante des deux
autres.** Entre l'acquittement et la remise, la monnaie n'a pas reflué : **le
reflux effectif est décalé du reflux comptabilisé**, et le bouclage est donc
vérifié sur deux flux qui ne coïncident pas dans le temps. Après le délai de
transmission monétaire (L11.C10, sur Friedman) et le délai biologique de la
restauration (L11.C16 § 8). **Aucun des trois n'a été cherché ; les trois ont été
trouvés en instruisant autre chose.** Le corpus note que **les délais sont la
difficulté structurelle du dispositif**, qu'un chapitre les traitant ensemble
aurait sa place, et que **le troisième est le seul réglable par décision** — la
périodicité de remise est un paramètre.

**TREIZIÈME CONDITION-LIMITE, versée à l'inventaire de L11.C03 § 5.**

> **B13 — le délai entre perception et remise ne peut excéder la période sur
> laquelle le bouclage est vérifié.**

Elle mord **sous tension** : un percepteur dont l'économie se contracte a toutes
les raisons de retarder une remise qui sort de chez lui, **donc elle est maximale
au moment où le bouclage est le plus sollicité.** Sept des treize ne mordent que
sous tension.

**De quel côté cet arbitrage paie**, par l'exigence de rédaction posée en A23 :
l'architecture 1 paie en **efficacité** — elle perçoit moins bien — ; l'architecture
3 paie en **légitimité** — elle concentre. Il n'y a pas de branche gratuite.

**Ce qui remonte au Livre 7 :** qui perçoit. **Ce qui n'a de domicile nulle
part :** qui contrôle le percepteur.


### A25 — Le traitement des délais — OUVERT le 2026-09-06

**Origine : L11.C22, chapitre réclamé par le corpus lui-même** en L11.C21 § 3.
**En le préparant, le corpus a trouvé cinq délais là où il en avait nommé
trois.** Deux étaient établis depuis plusieurs chapitres **sans avoir jamais été
nommés comme des délais** — le constat de qualification, rangé comme surface de
capture (L11.C13, L11.C11 § 6), et le recours, rangé comme paramètre d'incidence
(L11.C19 § 3). **C'est un effet de classement**, le même qui avait fait compter
cinq barèmes là où il y en a trois.

| # | Le délai | Entre quoi et quoi | Réglable ? |
|---|---|---|---|
| **D₁** | transmission monétaire | modification d'un taux et effet sur les comportements | **non** |
| **D₂** | **constat de qualification** | l'acte régénératif et sa reconnaissance | partiellement — coûte de l'argent public |
| **D₃** | restauration écologique | l'acte financé et son effet mesurable | **non** — propriété du monde vivant |
| **D₄** | recouvrement administratif | l'acquittement et le reflux effectif | **oui — seule marge franche** |
| **D₅** | **recours** | la valeur appliquée et la valeur juste | partiellement — délai borné, et c'est une garantie qui a un prix |

**Ils occupent des segments distincts, donc ils sont EN SÉRIE.** Le délai de
bouclage est leur somme, **et personne ne l'a additionnée** — le corpus non plus,
faute d'ordres de grandeur. **Vérifier une égalité entre deux flux dont les
horloges diffèrent de plusieurs segments n'est pas la vérifier.**

**CE QUE L'ARBITRAGE DOIT SAVOIR : ils ne sont pas indépendants.** Chacun
s'allonge sous tension par un mécanisme propre — variabilité de la transmission
(Friedman), contraction des moyens administratifs, raréfaction du capital quand
la restauration est capitalistique, rétention du percepteur (**B13**),
engorgement du contentieux. **Le délai total est donc maximal au moment précis où
la correction est le plus nécessaire.** Ce n'est pas un défaut de réglage :
**c'est une propriété de composition, et elle va toujours dans le même sens.**
DÉDUITE, NON OBSERVÉE — testable sur données publiées pour D₄ et D₅.

**Et cela confirme, par une voie distincte, un résultat obtenu ailleurs.**
L11.C03 établit que **le compte est au plus mauvais sous tension**, sept des
treize conditions-limites ne mordant que dans cet état. **Les délais et le compte
se dégradent au même moment et pour des raisons différentes.**

**CONSÉQUENCE SUR O4, ET C'EST LA QUATRIÈME FOIS.** Un objectif contracyclique
suppose que la correction arrive pendant la phase qu'elle corrige. **Un instrument
dont le retard croît avec l'urgence est procyclique par retard.** Le corpus y
arrive maintenant par quatre voies : L11.C07 (la vertu contracyclique du demurrage
échoue dans l'état pour lequel elle est conçue), L11.C10 (la correction
discrétionnaire agit sur un état déjà changé), L11.C16 § 8 (le correcteur du
déséquilibre extérieur est plus lent que le déséquilibre), et le présent chapitre.
**O4 est le plus exposé des six objectifs, aucun chapitre ne l'a instruit de
front, et il mériterait le sien.**

**CE QUE LA DIRECTIVE FAIT, ET C'EST MOINS QU'IL N'Y PARAÎT.** Le circuit comporte
un sixième segment — le **délai de décision**, entre le moment où les données
justifient un changement et celui où l'autorité le décide. **La directive supprime
celui-là et lui seul** : elle ne raccourcit ni la transmission, ni le constat, ni
la restauration, ni le recouvrement, ni le recours. **Elle répond à un sixième du
problème.** SECONDE LIMITATION posée à ce résultat, après L11.C19 § 8 qui
établissait que le recours n'est pas une directive.

**A15 en est le cas le mieux réussi**, et pour une raison précise : indexer sur la
disponibilité **constatée** ne supprime pas seulement la délibération, **cela fait
coïncider le déclencheur avec l'observation**. C'est le maximum qu'une directive
puisse faire sur les délais ; les quatre autres segments demeurent.

**CE QUE L'ARBITRAGE DOIT TRANCHER.** Quatre des cinq échappent au réglage. **La
seule marge franche est la périodicité de remise (D₄), et c'est vraisemblablement
le plus petit des cinq** — A25 ne peut donc pas être rendu séparément de **A24**.
La stratégie disponible n'est pas de raccourcir mais **de faire porter à la
fonction ce que le délai empêche de corriger à temps** — lire des données
**avancées** plutôt que constatées, ce que L11.C20 § 6 proposait déjà pour
l'amendement. **Cela déplace le problème vers la qualité des indicateurs avancés,
dont le corpus ne sait rien, et vers A18**, qui établit que la moitié des familles
du tableau de bord ne sont pas des données.

**De quel côté cet arbitrage paie**, par l'exigence de A23 : raccourcir D₂ et D₅
coûte de l'**efficacité administrative** ; les laisser longs coûte de la
**légitimité**, puisque L11.C19 § 3 a établi que le délai trie comme le coût.

**UNE DETTE DE SOURCE, ET ELLE CROÎT.** Ce chapitre repose sur Friedman 1968 plus
que tout autre, **et Friedman 1968 n'est pas ouvert** — employé depuis L1.C21 § 6
sur sa notoriété. C'est le même mécanisme que pour Kydland-Prescott, relevé au
balayage n° 1 : **une source dont la charge probatoire augmente à chaque emploi
est plus urgente qu'une source neuve.** Priorité relevée.


### A26 — De quel cycle O4 parle, et ce que devient l'enveloppe en bas de cycle — OUVERT le 2026-09-06

**Origine : L11.C23, second chapitre écrit sur commande interne** — L11.C22 § 4
avait relevé que quatre chapitres ont trouvé O4 fragile en instruisant autre
chose, qu'aucun ne l'avait examiné de front, et qu'« il mériterait le sien ».
**A26 est préalable au compte de L11.C03**, comme A18 : deux arbitrages sur six
objectifs conditionnent désormais le décompte.

**UN RÉSULTAT FAVORABLE QUE LE CORPUS N'AVAIT JAMAIS ÉNONCÉ EN VINGT-DEUX
CHAPITRES.** L'assiette du premier ressort étant faite de transactions, **le
prélèvement transactionnel est un stabilisateur automatique** : il prélève
davantage en haut de cycle **sans qu'aucune autorité ne le décide**, et
vraisemblablement plus que proportionnellement, les transactions les plus taxées
— biens durables, énergie, transport, construction — étant réputées les plus
cycliques. **L'élasticité n'est pas mesurée** ; elle existe par branche dans les
comptabilités nationales et est versée au bon de commande du Livre 13.

**Ce que cela fait à la thèse du corpus sur la directive.** L11.C22 § 5 a établi
qu'une directive supprime **le délai de décision et lui seul** — un sixième du
circuit. **L'automaticité fait mieux : elle supprime la décision.** Ni diagnostic,
ni délibération, ni annonce, ni anticipation d'un report. **C'est le seul
mécanisme du dispositif auquel ni Lucas ni Kydland-Prescott ne s'appliquent.**

**LE REVERS SORT DE LA MÊME PROPRIÉTÉ, ET IL EST PLUS LOURD.** La condition de
bouclage liant le volume émissible au produit du reflux (L11.C16 § 2), **le cycle
du reflux devient le cycle de l'émission.**

> **Le dispositif est automatiquement contracyclique sur son versant reflux et
> automatiquement procyclique sur son versant émission. C'est le bouclage
> lui-même qui transmet le cycle de l'un à l'autre.**

**Aucun taux ne le corrige** : l'émission dépend du reflux et non l'inverse, donc
relâcher le reflux en bas de cycle réduit l'enveloppe une seconde fois. **Et cela
heurte la fonction assignée au dispositif** : un dispositif dont la capacité de
financement se contracte avec l'économie **ne finance pas l'essentiel insolvable
au moment où il est le plus insolvable** — au moment, précisément, où les
capacités physiques que P35 déclare contraintes sont disponibles.

**LA SEULE SORTIE CONNUE ROUVRE UNE PROMESSE BLOQUANTE.** Vérifier le bouclage
sur une période **plus longue que le cycle** rétablit la contracyclicité de
l'émission — mais émettre au-delà du reflux encaissé, **c'est émettre contre un
reflux futur**, soit la construction que **P55** déclare intenable, la créance
portant sur une assiette que le dispositif existe pour contracter. **Plus le
lissage est efficace contre le cycle, plus la créance qu'il suppose est fragile.**
La lecture B retenue par l'auteur ne règle pas ce point : elle change le registre
de P55, elle ne le résout pas.

**CE QUE L'ARBITRAGE DOIT TRANCHER EN PREMIER : de quel cycle O4 parle.**

| | Le cycle | Ce que « contracyclique » y voudrait dire |
|---|---|---|
| **économique** | activité, emploi, prix | durcir en expansion, relâcher en récession |
| **biosphérique** | pression sur les limites physiques | durcir quand la pression croît — **pas au même moment** |

**Les deux ne coïncident que si la pression écologique suit l'activité, et le
corpus a établi le contraire** : le succès sur la famille biosphérique contracte
l'assiette dégénérative et dégrade la famille monétaire (L1.C21 § 6, F1). **Tel
qu'il est énoncé, O4 est une direction sans référent** — donc pas encore un
objectif au sens du compte. **S'il se dédouble, le compte s'aggrave ; s'il se
résout en un seul cycle, il faut dire lequel et assumer l'autre.**

**Ce que l'arbitrage doit trancher en second : la priorité.** « Corréler à la
politique macroprudentielle » ne dit ni le sens, ni le décalage, ni **lequel des
deux instruments cède en cas de conflit.** Engone Mve fournit la règle manquante
sous la forme d'une position constituée — en cas de conflit d'objectifs,
« **priority is given to a single objective** ». Versée, non tranchée.

**Et l'argument du pôle de l'intégration porte ici.** Les instruments
macroprudentiels, « **because they are more targeted, are easily circumvented** ».
**Un prélèvement modulé par barème est ciblé au sens exact de cette phrase**, et
sa contracyclicité suppose que l'assiette ne se déplace pas quand on la durcit —
ce que **B1** dit qu'elle fait. **Durcir en haut de cycle est le moment où
l'assiette est la plus mobile.**

**QUATORZIÈME CONDITION-LIMITE, versée à L11.C03 § 5.**

> **B14 — la période sur laquelle le bouclage est vérifié ne peut être plus
> courte que le cycle, sans quoi le bouclage transmet le cycle à l'émission.**

Elle ne s'introduit pas tant que l'économie est stable et **devient active dès
qu'un retournement survient.** Elle compose avec **B13**, les deux portant sur la
même horloge. **Huit des quatorze ne mordent que sous tension.**

**De quel côté cet arbitrage paie**, par l'exigence de A23 : lisser paie en
**légitimité** — la créance suppose ce que P55 conteste ; ne pas lisser paie en
**efficacité** — le dispositif finance le moins quand il faudrait le plus. **Il
n'y a pas de branche gratuite, et celle-ci est la plus chère du Livre 11.**


### A27 — La forme du barème aux frontières — OUVERT le 2026-09-06

**Origine : L11.C24.** Le dispositif est une coalition, **donc son barème a une
frontière, et aucun chapitre n'avait écrit ce qui s'y passe.** Trois résultats du
corpus s'y rapportaient sans avoir jamais été réunis : la contrainte est fonction
de ce qui demeure dehors (L11.C04 § 6, sur Mundell), le seuil d'activation est
affirmé et non dérivé (P51), les valeurs par défaut ont un précédent opérant
(L11.C06).

**Ce que l'arbitrage doit savoir en premier : le mécanisme de la valeur par
défaut ne se transporte pas à la frontière.** À l'intérieur, le producteur
documente **parce qu'il est dans le régime** — la charge le frappe de toute façon
et documenter la réduit. **À l'extérieur, il n'y est pas.** Documenter n'a
d'intérêt que si le marché de la coalition vaut le coût de la démarche.

> **La question cesse d'être « le défaut est-il assez punitif ? » et devient
> « le marché est-il assez grand ? »** — et le corpus confondait les deux.

Un défaut très punitif appliqué par une coalition petite ne fait pas documenter :
**il fait renoncer au marché.**

**APPORT PROPRE : LE SEUIL D'ACTIVATION A UN JUMEAU MICROÉCONOMIQUE, jamais
énoncé.** P51 le pose au niveau des pays ; **il existe aussi au niveau des
entreprises.**

> **Un exportateur ne documente son empreinte que si la part de son chiffre
> d'affaires exposée au marché de la coalition excède le coût de conformité.**

**Et ce coût est largement fixe** — comptabilité de flux, données de
fournisseurs, vérification varient peu avec le volume. **Un seuil fondé sur un
coût fixe rapporté à un chiffre d'affaires exclut les petits, mécaniquement.**

**SEPTIÈME BIAIS DE CONCENTRATION, et le premier qui joue ENTRE PAYS.** Le grand
exportateur documente, obtient le taux modulé et entre ; **le petit exportateur
d'un pays pauvre paie le défaut punitif ou renonce.** Après les quatre biais
procéduraux (L11.C09), l'exclusion du financement (L11.C13 § 6) et le biais
d'apprentissage (L11.C19 § 6). **Il s'ajoute à P43** — la contrainte extérieure
rebasée sur la nature encore fonctionnelle : **deux mécanismes indépendants
désavantagent les mêmes pays**, et le second est purement administratif.

**Correction connue, et elle coûte** : valeurs par défaut sectorielles et
régionales favorables aux petits exportateurs, ou prise en charge de la
certification. **Troisième occurrence du motif administratif de Tinbergen** —
la mesure qui « affects few » coûte moins cher, donc corriger suppose de payer
délibérément un surcoût. Après A14 et L11.C13 § 6.

**LA LACUNE PRINCIPALE, ET ELLE EST PLUS GRAVE ICI QU'AILLEURS.** Le règlement
(UE) 2023/956 et ses actes d'exécution sur les valeurs par défaut sont **le seul
précédent opérant d'un barème d'impacts appliqué hors du régime qui l'édicte**.
Ils sont en priorité 1 depuis L11.C06 et **ne sont pas ouverts** ; le corpus
raisonne de seconde main. **Ils décideraient A11 et A27.**

**Et l'analogie qui a servi à chiffrer le seuil est doublement favorable au
dispositif.** P51 avait relevé qu'elle transporte les propriétés d'un instrument
**sectoriel** vers un instrument **universel**. Le corpus en ajoute une seconde
raison : **un mécanisme sectoriel porte sur des biens dont l'empreinte est déjà
mesurée par les industriels concernés**, ce qui n'est pas le cas d'un instrument
universel.

**LA RÉCIPROCITÉ EST UN QUATRIÈME CAS QUE RIEN NE TRAITE**, et il faut le
distinguer des trois autres : F6 porte sur l'adoption contre le créancier, P51
sur le passager clandestin **externe**, L11.C21 § 5 sur le passager clandestin
**interne**. **La riposte est un non-membre qui applique son propre barème aux
exportations de la coalition.** Le résultat de Mundell donne la forme de l'issue :
la contrainte étant fonction de ce qui reste dehors, **une guerre de barèmes est
une compétition sur la taille des blocs**, et le mécanisme d'escalade est **le
même que le mécanisme d'adoption**. Renseignement, non garantie. Compose avec F4,
dont les pièces décisives ne sont pas ouvertes non plus.

**CE QUE L'ARBITRAGE AJOUTE À A6, ET QUI N'AVAIT PAS ÉTÉ FORMULÉ.** Trois
résultats convergent : tout est plus facile quand la coalition est déjà grande.
**Mais la difficulté n'est pas seulement politique, elle est métrologique.** Une
petite coalition n'obtient pas les données qui lui permettraient de moduler, donc
elle applique des défauts punitifs à presque tout, **donc son barème perçoit sans
orienter** — soit le mode d'échec que A11 nomme, atteint ici **par le dehors et
non par le dedans**. **Il faut donc à la stratégie d'adoption un SECOND seuil,
jamais estimé : celui à partir duquel les exportateurs documentent.** Rien ne dit
qu'il coïncide avec le premier.

**De quel côté cet arbitrage paie**, par l'exigence de A23 : un défaut punitif
uniforme paie en **légitimité** — il exclut les petits exportateurs des pays
pauvres ; des défauts modulés par taille et par région paient en **efficacité** —
ils coûtent l'administration que la valeur par défaut existait pour éviter.


### A28 — L'architecture du contrôle et le pouvoir de sanction — OUVERT le 2026-09-06

**Origine : L11.C25, dernier chapitre annoncé du Livre 11.** Il réunit **trois
lacunes que le corpus avait trouvées séparément** en instruisant trois choses
différentes, et qui sont **trois maillons du même circuit** : le déclarant
(L11.C06 — l'empreinte est autodéclarée, qui la vérifie ?), le certificateur
(L11.C11 § 6 — la décision la plus capturable, qui l'audite ?), le percepteur
(L11.C21 § 5 — *« la question n'a de domicile dans aucun livre du plan »*).

**Ce que la réunion dit et qu'aucune ne disait seule.** Le dispositif a déplacé
la charge de la mesure vers ceux qui en tirent avantage — c'est l'économie de
L11.C06 et ce qui le rend administrable. **Déplacer la mesure sans déplacer la
vérification laisse le circuit entier sur la parole de ceux qu'il taxe et de ceux
qu'il finance.**

**APPORT PROPRE, ET C'EST LE PLUS LOURD : LE RECOURS EST UN CORRECTEUR
UNILATÉRAL.** Celui qui est classé plus dégénératif qu'il n'est conteste ; **celui
qui est classé moins dégénératif se tait.** Le recours corrige donc les
surestimations et **jamais les sous-estimations**.

> **Un barème doté d'un recours et privé de contrôle dérive vers le bas, et il y
> dérive d'autant plus vite qu'il apprend mieux.**

Cela **durcit** le sixième biais de L11.C19 § 6 au lieu de le répéter : le barème
apprend **là où** l'on conteste **et dans le sens où** l'on conteste. Les deux se
composent — **précis, bas, et précis surtout pour ceux qui ont les moyens.** Et
c'est encore une propriété que l'analogie de la taxe sur la valeur ajoutée ne
transporte pas, après le motif de la perception (L11.C21 § 4) : **sous ce régime,
l'administration contrôle parce que le produit lui revient.**

**PREMIÈRE LIMITE POSÉE AU SEUL RÉSULTAT FAVORABLE DU CHANTIER.** L11.C17 § 6
établissait que le bouclage rend détectable en agrégat la sous-qualification
systématique. **Il détecte un déficit ; il ne dit pas d'où il vient.** Trois
causes ont la même signature : **le dispositif réussit** (les transactions
dégénératives reculent — F1), **l'économie se contracte** (L11.C23 § 4), **on
perçoit mal** (le présent chapitre). **Le résultat tient mais il est aveugle au
sens de l'écart** ; le tableau de bord sépare les deux premières, **la troisième
ne se distingue que par vérification.**

**Ce que l'arbitrage doit trancher : trois objets de natures différentes.**

| | Contrôler qui | Nature | Difficulté propre |
|---|---|---|---|
| **1** | le **déclarant** | technique | **c'est ce que la valeur par défaut existait pour éviter** |
| **2** | le **certificateur** | technique et sectorielle | **la compétence requise est dans le secteur contrôlé** — capture réglementaire ordinaire, sur la décision la plus exposée |
| **3** | le **percepteur** | administrative — **c'est un État** | aucune forme connue n'existe sans **pouvoir de sanction** |

**L'ARGUMENT D'OSTROM TROUVE ICI SON OBJET PROPRE.** Employé sur les valeurs
(L11.C16 § 5), déplacé sur la perception (L11.C21 § 5), il porte en réalité sur
**le pouvoir** : « inherently weak because of **free-rider problems** ». **Une
unité centrale sans sanction n'est pas faible parce qu'elle décide mal : elle est
faible parce que rien n'oblige à lui obéir.**

**ET LA SEULE SANCTION DISPONIBLE EST DÉMESURÉE.** Réduire les allocations d'un
membre défaillant revient à **le priver de son équilibre extérieur** — P52 et
L1.C27 § 6 ayant établi que la valorisation le détermine. **Un instrument
démesuré ne s'emploie pas** : c'est le mécanisme de report rencontré sur les
parités (L11.C15 § 6). **La sanction existante est inutilisable, et il n'y en a
pas d'autre.**

**LE CONTRÔLE DÉFAIT L'ÉCONOMIE QUI RENDAIT LE DISPOSITIF ADMINISTRABLE.**
Contrôler, c'est mesurer au centre — donc refaire ce que le dispositif avait
délégué. **Il y a un optimum et personne ne l'a cherché.** La forme connue est le
contrôle par échantillon, dissuasif seulement si le produit de la probabilité de
détection par la sanction excède le gain — **ce qui suppose une sanction**, soit
ce dont le paragraphe précédent établit l'absence.

**QUATRIÈME EMPLOI DU MOTIF ADMINISTRATIF DE TINBERGEN, ET LE PREMIER COMME
EXPLICATION.** Entre une mesure qui « hits a large number of people » et une qui
« affects few », l'efficacité recommande la seconde. **Cela explique pourquoi les
sept biais de concentration existent** : ce ne sont pas des négligences, **c'est
ce que le contrôle bon marché produit.** Le corpus enregistre que **sa propre
critique de ces biais revient à demander un contrôle cher**, et qu'il doit le
dire au lieu de réclamer les deux.

**QUINZIÈME CONDITION-LIMITE, et c'est celle qui explique les autres.**

> **B15 — le coût du contrôle ne peut excéder le produit qu'il protège.**

Elle ne mord pas sur les gros dossiers et **elle mord sur les petits** — soit
exactement la structure des sept biais. **Active en permanence sur la queue de la
distribution**, et elle s'aggrave à mesure que le dispositif s'étend vers les
petits acteurs, c'est-à-dire vers ceux qu'il vise.

**LE COMPTE FINAL DES OBJETS MANQUANTS.** L11.C06 § 4 avait établi qu'un barème
est **trois objets** — une table, une procédure, une charge de la preuve. Le
Livre 11 en a ajouté trois : **un tribunal** (A22), **un contrôleur** et **une
sanction** (A28). **Le dispositif en publie un.**

**De quel côté cet arbitrage paie**, par l'exigence de A23 : contrôler peu paie
en **légitimité** — le barème dérive vers le bas et les biais s'installent ;
contrôler beaucoup paie en **efficacité** — on refait au centre la mesure qu'on
avait déléguée, et c'est l'économie du dispositif qui disparaît.

**Ce qui remonte au Livre 7 :** qui contrôle. **Ce qui n'a de domicile nulle
part :** avec quelle sanction.

---

## Le balayage rétrospectif — ce qu'une passe rend aux passes antérieures

**Établi le 2026-09-06, et c'est le premier.** Le corpus disposait d'un mécanisme
pour enregistrer ce qu'une passe REPORTE — ce fichier — et d'un autre pour
enregistrer ce qu'un livre DOIT à un autre — la table de routage. **Il n'avait
rien pour enregistrer ce qu'une passe REND à celles qui l'ont précédée**, alors
que c'est la raison d'être de la méthode : *chaque passe se sert de la précédente
pour répondre aux blancs des passes antérieures* (J.-C. Duval, 2026-09-06).

**La règle qui en découle, et elle est désormais de tenue obligatoire.** Quand
une passe se termine sur un livre, **on balaie les promesses des passes
antérieures que ce livre a touchées**, et l'on inscrit le résultat dans la
colonne « Soldée par » du registre — jamais dans un fichier séparé, qui
divergerait. Le balayage n'est pas facultatif : sans lui, un travail qui répond à
un blanc laisse ce blanc ouvert au registre, et la passe suivante le rouvre.

### Balayage n° 1 — passe 1 du Livre 11 sur les promesses du Livre 1

**Périmètre : 18 promesses touchées par les dix-sept chapitres du Livre 11.**
Trois avaient été traitées au fil de l'eau (P52, P53, P54) ; **les quinze autres
ont été balayées le 2026-09-06** et leur colonne est renseignée.

**LE RÉSULTAT D'ENSEMBLE, ET IL FAUT LE DIRE DANS CE SENS : la passe n'a pas
réduit le dossier, elle l'a durci.**

| Ce que le balayage produit | Combien | Lesquelles |
|---|---|---|
| **Soldée** | **0** | — |
| **Soldée sur une moitié** | 1 | P29 — le mécanisme de la borne est acquis, l'étanchéité non |
| **Aggravée ou élargie** | 6 | P16, P25, P31, P37, P43, P49 |
| **Déplacée sans être résolue** | 3 | P19b, P52, P55 |
| **Instruite, avec une méthode qu'elle n'avait pas** | 3 | P18, P48, P50 |
| **Instruite par composition** | 2 | P34, P35 |
| **Reliée à une autre, calcul toujours dû** | 1 | P51 |
| **Instruite, non soldée** | 2 | P53, P54 |

**Aucune promesse n'est soldée, et une seule l'est à moitié.** Le corpus
enregistre ce résultat comme tel : dix-sept chapitres d'instruction, quatre
sources primaires ouvertes de première main, et **le dossier des objections est
plus lourd qu'avant, non plus léger.** C'est ce qu'on attend d'une passe qui
travaille — mais c'est aussi un renseignement sur le dispositif, et il ne doit
pas être présenté autrement.

**Ce que le balayage a trouvé et que personne ne cherchait — deux défauts de
tenue du corpus lui-même.**

**1. Deux conventions de numérotation coexistent dans le registre.** « P19b » et
« P19c » sont des promesses distinctes, avec leur propre ligne. « P34b » désigne
le POINT (b) de la ligne P34 et n'a pas de ligne. **Les deux notations sont
identiques à l'œil**, et le corpus a cherché une ligne P34b qui n'existe pas.
Signalé dans la colonne de P34 ; **non renuméroté**, la renumérotation d'un
identifiant employé dans cinq fichiers étant une migration scriptée et non une
correction de passage.

**2. Une dette qui croît avec l'usage.** Kydland-Prescott 1977 fonde le falsifieur
F7, la promesse P48 et le point (b) de P34 — **et le corpus s'en sert maintenant
une troisième fois, en L11.C10, sans l'avoir jamais lu.** Le tirage acquis est un
scan sans couche de texte. La liste d'acquisition portait « employé deux fois » :
c'est trois. **Une source dont la charge probatoire augmente à chaque emploi est
plus urgente qu'une source neuve**, et le corpus ne l'avait pas hiérarchisée
ainsi.

### Ce qui restait à balayer après le n° 1

**Le balayage n° 1 ne couvre que les promesses.** Trois gisements de blancs
antérieurs n'ont pas été balayés et le seront à la passe suivante :

- **les `verifications_en_attente` des trente chapitres du Livre 1** — le Livre 11
  a ouvert Tinbergen, Mundell et dépouillé Ostrom ; plusieurs vérifications du
  Livre 1 en dépendent sans le savoir ;
- **les falsifieurs** — F1 et F7 ont été requalifiés en cours de route
  (`falsification.md`), mais F2 à F6 n'ont pas été relus à la lumière du Livre 11 ;
- **le Livre 2**, dont les douze épisodes sont acquis et qui porte la macroprudence
  — L11.C03 § 6 a établi que la doctrine de la séparation n'est pas unanime, ce
  qui touche directement son objet.

### Balayage n° 2 — passe 1 du Livre 11 sur les `verifications_en_attente` du Livre 1

**Périmètre mesuré : 459 entrées de vérification dans les trente chapitres du
Livre 1**, dont **51 touchées** par un objet du Livre 11 — Tinbergen, Mundell,
Ostrom, Hayek, Kydland-Prescott, Friedman, Lucas, Goodhart, ou l'un des mots du
chantier des barèmes. **Quinze ont été renseignées le 2026-09-06**, celles où la
passe 1 du Livre 11 rend l'entrée **fausse**, **périmée** ou **répondue**. Les
trente-six autres sont des concordances de vocabulaire sans apport.

**Ce que le balayage a corrigé, et il faut le dire en premier : une entrée était
devenue fausse.** L1.C18 portait sur la connaissance dispersée que « **aucun
chapitre ne la traite encore** ». Deux la traitent — L11.C05 § 6, où l'objection
est versée par l'auteur lui-même sous la forme du crayon, et L11.C13 § 7 — et
L11.C16 § 5 la localise sur la décision D2. **Une objection que le corpus tient
pour la plus forte du dossier était portée comme non traitée alors qu'elle
l'était deux fois.**

**Ce que le balayage a débloqué.** Six entrées disaient « renvoi à ajouter vers
le Livre 11 **quand il existera** ». Il existe : dix-sept chapitres, A8 rendu.
Trois d'entre elles sont désormais actionnables et nomment leurs cibles.

**Ce que le balayage a répondu — les huit entrées de fond.**

| Chapitre | L'entrée demandait | Ce que le Livre 11 rend |
|---|---|---|
| L1.C18 | la formule d'équilibre dérivée | elle n'est pas exposée, mais sa **structure** l'est : le niveau est contraint, seule la structure est décidée (C16 § 2) |
| L1.C21 | Friedman, Lucas, Kydland-Prescott non ouverts | **Lucas requalifié** sans être ouvert (Goutsmedt et al. 2017, lu) ; les deux autres toujours pas, et K-P employé une troisième fois |
| L1.C21 | existe-t-il un barème automatique éprouvé ? | **la forme existe** — la directive (C12) — **et un précédent réel** : les valeurs par défaut du CBAM (C06). Ce qui reste ouvert est plus étroit |
| L1.C21 | élasticité de l'assiette | la contraction ne prive pas seulement de recettes : **elle réduit ce qui peut être financé** (C16 § 2 et § 4) |
| L1.C22 | l'option « norme au centre, qualification locale » | **partiellement tranchée, et pas dans le sens espéré** : elle laisse D2 centrale, et Mundell y interdit la polycentricité (C16 § 5) |
| L1.C23 | la contradiction robustesse / centralisation | **A4 est partiellement tranché** sans que ce chapitre l'ait su |
| L1.C26 | quelle procédure de révision des parités ? | **instruit par C15** : trois réponses incompatibles, dont la croissance du PIB ; et la forme est tranchée — constante ou directive |
| L1.C27 | ce que le barème détermine réellement | **une quatrième borne, jamais nommée** : le produit du reflux (C16 § 2) |
| L1.C28 | piloter sur un tableau de bord non agrégé | **la question a changé d'objet** : le tableau est l'entrée des barèmes, et la moitié de ses familles sont des objectifs (C14, A18) |
| L1.C29 | le demurrage peut-il gager l'émission ? | **le corpus retire sa qualification de « voie la moins coûteuse »** : trois nœuds, aucun bon, et sa vertu contracyclique échoue quand on en a besoin (C07) |

**Une seule qualification est retirée**, et c'est celle de L1.C29 : le demurrage
n'est pas la voie de sortie la moins coûteuse. **Aucune entrée n'est close.**

### Ce que le balayage n° 2 a trouvé dans l'instrument de contrôle

**`controle.py` calcule deux empreintes et n'en compare qu'une.** L'empreinte
**éditoriale** porte sur le corps et le résumé ; c'est elle qui déclenche la
demande d'arbitrage « fond ou éditorial ». L'empreinte **métadonnées** porte sur
tout le reste de l'en-tête — donc sur `sources_primaires`, `date_verification`,
`statut`, `citable`, `concepts`, `renvois`. **Elle est calculée, stockée dans
`.etat-corpus.json`, et jamais relue** : `ancien.get("metadonnees")` n'apparaît
nulle part.

**Conséquence, et elle porte sur le champ le plus sensible du corpus.** Une
modification de `date_verification` passe sans aucun signal. Or c'est le champ
que la règle fondatrice protège — *ne jamais écrire une `date_verification`
avant qu'un humain ait ouvert la source*. **L'empreinte qui permettrait de
détecter une altération existe et n'est pas branchée.**

**Le corpus ne corrige pas de lui-même.** `controle.py` est l'autorité, et la
convention § 15 exige une migration scriptée et un incrément du journal des
révisions pour toute modification du schéma ou de son contrôle. **Signalé à
l'auteur le 2026-09-06 ; décision à rendre.** Effet de bord favorable à noter :
c'est parce que l'empreinte métadonnées n'est pas comparée que les quinze
entrées ci-dessus ont pu être renseignées sans que quinze chapitres du Livre 1
voient leur `revision_de_fond` bougée — ce qui est le bon classement, le dossier
de vérification étant matière de travail et non assertion du chapitre.

### Ce qui restait à balayer après le n° 2

- **les falsifieurs F2 à F6**, jamais relus à la lumière du Livre 11 — F1 et F7
  l'ont été en cours de route ;
- **le Livre 2**, dont les douze épisodes sont acquis et qui porte la
  macroprudence : L11.C03 § 6 a établi que la doctrine de la séparation n'est pas
  unanime, ce qui touche directement son objet ;
- **les trente-six concordances sans apport** du présent balayage : elles n'ont
  pas été relues une à une, seulement écartées sur lecture rapide.

### Balayage n° 3 — passe 1 du Livre 11 sur les falsifieurs F2 à F6

**Périmètre : les cinq falsifieurs jamais relus à la lumière du Livre 11.** F1 et
F7 l'avaient été en cours de route — F1 qualifié en classe (d) de Tinbergen, F7
élargi à la trajectoire puis repondéré. **Les cinq autres sont annotés le
2026-09-06 dans `falsification.md`.**

**Aucun falsifieur n'est levé. Trois sont durcis, un est localisé, un est
inchangé.**

| | Ce que la passe 1 du Livre 11 lui fait |
|---|---|
| **F2** — métrologie | **DURCI SUR TROIS POINTS, ADOUCI SUR UN.** Le falsifieur est écrit du mauvais côté : mesurer un mal a des instruments imparfaits mais existants, mesurer un bien n'en a presque aucun. Un second canal d'échec apparaît, **indépendant de l'instrumentation** — le contrefactuel d'additionnalité est déformé par l'annonce du barème —, et **le test que F2 se donne ne l'atteint pas.** La sortie qu'il se donne — n'allouer que sur les fonds bien mesurés — **est le cinquième biais de concentration**, et l'efficacité administrative la recommande. Adouci par L11.C17 § 6 : le bouclage ferme une boucle de contrôle que F2 supposait absente |
| **F3** — connaissance dispersée et Goodhart | **LOCALISÉ, ET SON ESPACE DE TEST A RÉTRÉCI.** « Ni adoptée ni écartée » n'est plus exact : l'option polycentrique laisse D2 centrale et **Mundell l'y interdit**. Elle localise D3 — **soit la décision que L11.C11 § 6 identifie comme la plus capturable.** Et **un des trois remèdes que F3 nommait est exclu par le corpus lui-même** : la révision non annonçable contredit l'exigence de directive publiée (A17, non résolu) |
| **F4** — droit positif | **INCHANGÉ, et le corpus le dit plutôt que de meubler.** Les deux pièces qui le décideraient — arrêt CJUE de novembre 2022, règlement CBAM et actes d'exécution — sont en priorité 1 et **aucune n'est ouverte**. Une seule donnée nouvelle, modeste : le CBAM est un barème d'impacts administré **opérant dans l'ordre juridique même que F4 vise** |
| **F5** — antériorité | **LES TROIS ANTÉRIORITÉS ONT UNE GRILLE DE LECTURE**, qu'elles n'avaient pas. Chiemgauer : il opère à l'échelle où la condition-limite B2 ne mord pas — **l'antériorité prouve que le mécanisme marche ET indique pourquoi il ne transporte pas.** VECTOR : **le seul endroit du dossier où A19 peut être posé à un dispositif réel.** FIN4 : à lire comme une décomposition D1/D2/D3/D4, et surtout — y a-t-il une valeur par défaut, et de quel côté penche-t-elle ? |
| **F6** — adoption contre le créancier | **AGGRAVÉ PAR UNE VOIE NOUVELLE.** F6 suppose UN adversaire ; l'enveloppe plafonnée en donne plusieurs. À saturation, la valorisation est un partage à somme quasi nulle : **chaque membre a une raison de contester la clé**, et cette clé est P31, non écrite. Le durcissement du 2026-09-04 établissait que le seuil de tolérance du créancier est très bas ; celui-ci établit que **le nombre de parties ayant une raison de refuser est plus grand que F6 ne le supposait** |

**Ce que le balayage n° 3 apporte de plus utile, et ce n'est pas un durcissement.**
F5 exigeait depuis le 2026-09-04 d'être éprouvé contre ses trois antériorités
« **nommément plutôt que dans l'abstrait** », et il lui manquait la grille pour
cela. **Le Livre 11 la fournit** : les quatre décisions, la condition-limite B2,
la dichotomie constante/directive, la question de la valeur par défaut. Les trois
fiches ne sont toujours pas ouvertes — **mais le corpus sait désormais quoi y
chercher**, ce qui rend l'ouverture rentable.

**Une piste versée sous réserve explicite.** L11.C15 § 6 apporte à F6 le
précédent des parités « fixes mais ajustables » de Bretton Woods, dont
l'ajustement politiquement coûteux était reporté jusqu'à la crise. **Le corpus
tient ce point de sa culture générale et non d'une source ouverte**, alors qu'il
dispose de Keynes *CW* XXV et d'Eichengreen. C'est une piste pour F6, pas une
donnée.

### Ce qui restait à balayer après le n° 3

- **le Livre 2**, dont les douze épisodes sont acquis et qui porte la
  macroprudence : L11.C03 § 6 a établi, sur Engone Mve 2022, que la doctrine de
  la séparation **n'est pas unanime** — pôle de la séparation contre pôle de
  l'intégration — et que l'étude porte sur un régime de change fixe, celui du
  dispositif. **C'est le dernier gisement identifié**, et le seul qui touche un
  livre déjà acquis ;
- **les trente-six concordances sans apport** du balayage n° 2, écartées sur
  lecture rapide et jamais relues une à une.

### Balayage n° 4 — passe 1 du Livre 11 sur le Livre 2 (macroprudence)

**Le Livre 2 n'est pas dans le dépôt.** Ses douze épisodes sont acquis et vivent
hors du corpus ; seul L2.E09 y est cité, dix-sept fois. **Le balayage ne peut
donc pas annoter ses chapitres** — il verse huit acquis à la section des
couplages et annote les quatre promesses que la table de routage lui attribue.
**Le corpus enregistre au passage qu'il ne peut pas balayer un livre qu'il ne
détient pas**, ce qui vaut aussi pour les Livres 3 à 10 et 12 à 18.

**L'acquis principal touche l'objet même de ce livre, et il est défavorable.**

**La doctrine macroprudentielle n'est pas unanime**, et un livre de
recommandations macroprudentielles ne peut pas écrire la séparation comme un
acquis. Engone Mve 2022, ouvert le 2026-09-05, établit deux pôles — séparation
(Svensson, Bernanke, Beau et al.) contre intégration (Adrian-Shin, Mishkin,
Eichengreen et al., au motif que les instruments macroprudentiels « **because
they are more targeted, are easily circumvented** ») — plus une position
conditionnelle.

**Et le corpus peut désormais aller plus loin que constater le désaccord.** Le
pôle de la séparation se fonde explicitement sur « **Tinbergen's consistency
rule (1952) and Mundell's rule of efficient instrument allocation** » — soit les
deux textes que la passe 1 du Livre 11 a ouverts intégralement. Il en résulte
deux réserves que le corpus tient de première main :

- L11.C03 § 9 établit que le cadre de Tinbergen est bâti pour ses classes (a) et
  (b), et **range le changement de structure monétaire en classe (d)**, où
  « our empirical quantitative knowledge of human behaviour under different
  structural conditions is **so restricted** » ;
- Tinbergen assortit l'affectation un-pour-un d'une réserve explicite : elle
  suppose « **a very special structure** ».

**Les deux fondements de la doctrine que ce livre applique sont qualifiés dans le
texte même dont ils sortent.** Ce n'est pas une réfutation de la séparation ;
c'est que le Livre 2 devra la choisir plutôt que la supposer, et dire pourquoi.

**Un point favorable, et rare.** L'estimation d'Engone Mve porte sur un **régime
de change fixe**, celui du dispositif. **La source la plus proche de l'objet du
Livre 2 est aussi la plus proche de sa configuration**, ce qui n'arrive presque
jamais dans ce dossier et doit être exploité.

**Trois autres acquis, versés à la section des couplages.** L'instrument
contracyclique du dispositif — le demurrage — **échoue dans l'état pour lequel
il est conçu** (L11.C07), de sorte que le complément macroprudentiel cesse d'être
un complément et devient le seul porteur de O4. La seule règle de modulation
énoncée par le Cahier **ne traite pas le cas que le dispositif produit lui-même**
— le succès biosphérique contracte l'assiette et dégrade la famille monétaire.
Et la règle de modulation, étant une directive dont le tableau de bord est
l'entrée, **hérite de A18 avant d'être écrite** : la moitié des familles sont des
objectifs, non des données.

**Les quatre promesses attribuées au Livre 2 sont annotées.** P23 et P26 voient
leur réserve s'alourdir — les fonds propres du Symposium supporteraient en outre
la perte d'une révision de parité, et le volume émis n'est pas une grandeur
libre. **P28 est celle qui gagne le plus** : la « piste trouvée » est devenue une
doctrine complète (L11.C06) assortie d'un avertissement (L11.C13 § 6, L11.C16
§ 7) — le défaut change de face sur le versant émission, et sur la valorisation
il n'existe pas. **P36 a désormais son mécanisme de première main** : Mundell,
plus le canal non compté de P50, plus le délai de L11.C16 § 8.

### Fin de la série des balayages, et ce qu'elle a produit

**Quatre balayages en un jour, sur les quatre gisements identifiés.** Le
mécanisme n'existait pas le matin même ; il est né du principe énoncé par
l'auteur — *chaque passe se sert de la précédente pour répondre aux blancs des
passes antérieures*.

| | Objet | Volume | Résultat |
|---|---|---|---|
| **n° 1** | les promesses du Livre 1 | 18 touchées, 15 renseignées | **aucune soldée**, une à moitié, six aggravées |
| **n° 2** | les `verifications_en_attente` du Livre 1 | 459 entrées, 51 touchées, 15 renseignées | **une entrée était devenue fausse**, une qualification retirée |
| **n° 3** | les falsifieurs F2 à F6 | 5 annotés | **aucun levé**, trois durcis, un localisé |
| **n° 4** | le Livre 2 | 8 acquis versés, 4 promesses annotées | **la doctrine appliquée n'est pas unanime** |

**Ce que la série établit, et il faut le dire dans ce sens : le corpus n'a rien
fermé.** Dix-sept chapitres d'instruction, quatre sources primaires ouvertes de
première main, quatre balayages — **et le dossier des objections est plus lourd
qu'au matin.** Une seule fermeture partielle (P29, dont la borne empirique a
maintenant son mécanisme) et une seule qualification retirée (le demurrage n'est
pas la voie de sortie la moins coûteuse). C'est ce qu'on attend d'une passe qui
travaille ; **c'est aussi un renseignement sur le dispositif, et il ne doit pas
être présenté autrement.**

**Deux défauts de tenue du corpus lui-même ont été trouvés en chemin**, et
aucun n'était cherché : deux conventions de numérotation coexistent dans le
registre des promesses ; et `controle.py` calcule une empreinte sur
`date_verification` qu'il ne compare jamais. **Le second est le plus grave et
il appelle une décision de l'auteur.**


### A29 — Le financement du Symposium — TRANCHÉ le 2026-09-06, UNE SOUS-FORME OUVERTE

**Arbitrage de l'auteur, rendu en réponse au constat de L7.C10 § 5** — le livre
ne décrit nulle part le financement de l'institution. **Le surplus du reflux
collectif finance le GAÏA Economic Symposium.**

**Ce qu'il active.** La TROISIÈME FORME que L11.C01 § 5 avait nommée et mise de
côté : « le reflux s'annule pour la part qui correspond à des allocations
effectivement émises, **et alimente un fonds pour la part qui excède** ». Elle
était écartée pour un motif de méthode — on ne définit pas une exception avant
la règle — et le régime de base a été tranché le 2026-09-05 (lecture B).
**L'ordre a été respecté.**

**Ce qu'il résout.** L7.C10 § 5 avait établi que la capture documentée des
instituts statistiques passe par le BUDGET — INDEC 2007-2015, ELSTAT et les
poursuites contre A. Georgiou. **Aucun État ne votant le budget, aucun ne peut
affamer l'institution.** L'exigence de L1.C18 § 6 — « une dotation pluriannuelle
sanctuarisée, soustraite au vote budgétaire annuel » — est satisfaite **par une
voie que le corpus n'avait pas envisagée** : non par une règle qui protège la
dotation, mais **en supprimant l'acte qui pourrait la menacer.** Plus solide que
ce qui était demandé. **L'immunité légale des cadres techniques reste absente**,
et c'est le second vecteur de capture — celui du cas grec.

**Ce qu'il crée : une TROISIÈME forme de conflit d'intérêts.** L'organe qui fixe
le barème des impacts est financé par le produit de ce barème. **Moins grave que
les deux autres** — la séparation des pouvoirs mord ici, l'Assemblée ne percevant
ni ne dépensant, et l'incitation pousse dans le sens de la thèse. **Ce qui reste
est que l'incitation pousse au barème le plus PRODUCTIF DE RECETTES, non au plus
juste** : au-delà de la borne B1 les recettes chutent par évitement, donc
l'institution a intérêt au taux qui maximise le produit — **et ce n'est pas le
taux qui maximise l'effet écologique.**

**Ce qu'il oblige le corpus à corriger.** L11.C16 § 2 posait que le niveau de
l'émission est lié au produit du reflux. **Si le bouclage est une ÉGALITÉ, il n'y
a pas de surplus.** Financer l'institution sur le surplus exige donc que le
reflux excède structurellement l'émission : le niveau devient « le produit du
reflux **diminué des coûts institutionnels** ». **L'enveloppe qui finance les
communs est amputée du coût de l'institution qui la distribue** — et L11.C16 § 4
a établi que cette enveloppe est plafonnée et le partage à somme quasi nulle.
**Aucun ordre de grandeur n'est au dossier.**

**CE QUI RESTE À TRANCHER, et cela décide de tout.**

| | Le financement est | Ce que cela donne |
|---|---|---|
| **En tête** | prélevé avant le calcul de l'enveloppe | budget **stable** ; l'institution servie la première, les communs après |
| **En résidu** | ce qui reste après émission | budget **volatil**, et nul si le bouclage est exact |

**En résidu, le budget se comprime exactement quand il faut le plus agir** : en
crise la fuite est maximale (L11.C07) et la demande de financement régénératif
ne baisse pas. **Cela annulerait le gain.** L'arbitrage ne résout complètement
l'objection de L7.C10 **que sous la première sous-forme.** Question posée à
l'auteur en L7.C11 § 5.

**PRÉCISION DE L'AUTEUR LE MÊME JOUR : « il faudra certes un point de
démarrage ».** Instruite en L7.C12, et elle RESTREINT la portée de A29.

**La protection est réelle et DIFFÉRÉE.** Pendant la phase de démarrage il n'y a
pas de surplus, donc pas d'autofinancement, **donc il y a un financeur** — et le
vecteur de capture que A29 élimine est entièrement ouvert.

**Et cette phase n'est pas neutre : c'est celle où se fixent D1, D2 et D3**, soit
trois des quatre décisions, dont celle qui porte P52. L11.C16 § 6 a établi qu'une
fonction de valorisation choisie une fois détermine la balance des paiements d'un
membre pour sa durée de vie. **Le premier barème est celui qui compte le plus, et
c'est celui qui sera arrêté sous financement extérieur.** L'institution est donc
**protégée du financeur quand ses décisions ont le moins de portée, et exposée
quand elles en ont le plus.**

**Le précédent est net et ne demande aucune transposition.** Dans les statuts du
Fonds, ouverts le même jour, le poids de vote est fonction de la QUOTE-PART,
c'est-à-dire de la souscription initiale : **celui qui finance le démarrage
obtient durablement le pouvoir.** Composé avec F6 — la disposition qui contraint
le créancier est celle qui saute —, cela donne que **le créancier du lancement
écrit la règle et s'en sert d'abord pour ne pas se contraindre.**

**AUCUNE DES TROIS FORMES D'AMORÇAGE N'EST NEUTRE.** La souscription des membres
fondateurs installe une clé fondée sur l'apport, **qui contredit la règle de vote
du livre** — personne n'avait vu que les deux se contraignent. L'émission
d'amorçage **rouvre P55 pour toute la durée du démarrage**, aucune recette
n'existant en face. La dotation d'un tiers concentre le risque au pire endroit.

**CE QUE L'ARBITRAGE DOIT ENCORE COUVRIR** : une règle propre à la phase de
démarrage — financeur identifié, contribution plafonnée, **droits éteints à une
date fixée d'avance**, sur le modèle du délai d'entrée en vigueur versé par
L8.C31 § 6. Le but n'est pas d'empêcher que le financeur ait du pouvoir, ce qui
est inévitable, **mais que ce pouvoir soit borné dans le temps.**


---

### Balayage n° 5 — passe 1 du Livre 20 sur tout ce qu'il touche

**Livre 20 ouvert et clos le 2026-09-06, vingt-trois chapitres, six instruments
ouverts par téléchargement direct le même jour.** Le balayage porte sur les
Livres 1, 7, 8 et 11, et il rend plus qu'il ne prend — ce qui n'était arrivé à
aucun des quatre balayages précédents.

| Ce que le balayage produit | Combien | Lesquelles |
| --- | --- | --- |
| Promesses ou affirmations **fermées** | 2 | L1.C27 § 4 (l'équivalence stricte EST le texte) ; L1.C18 § 6 (le verrou est tranché, après coup et partiellement) |
| Constructions du corpus **corrigées par un texte en vigueur** | 3 | L7.C06 (la double majorité existe depuis 1944) ; L7.C09 (une addition suffit là où le corpus posait une racine carrée) ; L7.C05 (une liste de pouvoirs réservés fait mieux que quatre chambres) |
| Blancs **comblés par un mécanisme éprouvé** | 4 | L11.C15 (porteur d'une révision de parité) ; L11.C25 (certificateur doublement indépendant) ; L7.C11 (financement de la phase de constitution) ; L7.C12 (première marche de la séquence) |
| Demandes routées ici et **NON résolues** | 1 | L7.C10 § 5 — l'immunité des cadres techniques : trois textes, trois techniques, **le même angle mort** |
| Objections **aggravées** | 2 | La qualification juridique de l'unité émise ; l'instabilité de toute sanctuarisation |

**LE RÉSULTAT QUI COMMANDE LE RESTE, ET IL EST FAVORABLE.** Les verrous
procéduraux sont **faibles**. L'article 20 des statuts du SEBC — logé dans la
liste que l'article 106 § 6 du traité rend modifiable à la majorité qualifiée
**sans avis conforme du Parlement** — autorise le conseil des gouverneurs à
décider **aux deux tiers** de « such other operational methods of monetary
control as it sees fit ». La seule réserve tient en trois mots : « **respecting
Article 2** ». **Le mur est une porte, avec une serrure, et la serrure est la
hiérarchie des objectifs.** Tout ce que le corpus doit obtenir dans l'ordre
juridique européen tient en un point, et ce point n'est ni la prohibition du
financement monétaire, ni le monopole d'émission, ni la lourdeur des traités.

**CE QUE CELA IMPOSE AU CORPUS EN RETOUR.** L20.C03 a établi que le mandat étroit
applique une théorie que le corpus tient pour valide ailleurs. **On ne peut pas
demander l'égalisation des rangs sans fournir, pour l'objectif écologique, une
règle aussi contraignante qu'une cible d'inflation.** Le corpus a produit cette
règle — les barèmes du Livre 11 — **et ne l'a jamais revendiquée sous cet
angle.** C'est un travail de présentation, pas de conception, et il est à faire.

**CE QUE LE BALAYAGE REND À LA DERNIÈRE SECTION DE CE FICHIER.** L'arbitrage sur
le financement du démarrage se terminait sur ce qu'il devait « encore couvrir » :
une règle propre à la phase de démarrage, **financeur identifié, contribution
plafonnée, droits éteints à une date fixée d'avance**. Le mécanisme existe et il
est plus simple que ce que le corpus cherchait. **Statuts du Fonds, article XX
§ 2 (d)** : chaque gouvernement signataire verse **un cent-millième** de sa
souscription totale, le dépositaire le conserve sur un compte spécial, le
transmet à l'institution à sa première réunion — **et le restitue si l'accord
n'est pas en vigueur à une date écrite dans le traité.** Contribution plafonnée
par construction (proportionnelle à la souscription future), financeur identifié
(tous les signataires), **droits éteints par la restitution.** Le financeur
n'acquiert rien parce qu'il n'avance presque rien : le montant sert aux frais
administratifs, pas au capital. **P52 et la crainte du financeur unique tombent
si le démarrage est financé ainsi.**

**CE QUE LE BALAYAGE NE FAIT PAS, ET IL FAUT LE DIRE.** Il n'annote aucun
chapitre des Livres 1, 7, 8 et 11. Les correspondances ci-dessus sont
enregistrées ici et **dans les chapitres du Livre 20 seulement** ; les chapitres
visés continuent de porter leur état antérieur. **C'est la charge de la passe
suivante**, et elle est lourde : six chapitres du Livre 7 et trois du Livre 11
sont touchés.

**DEUX AVERTISSEMENTS À PORTER PLUS HAUT QUE CE FICHIER.**

**Premier — aucune sanctuarisation observée n'a tenu.** L20.C17 : l'article
311 § 6 de la convention de 1982 interdit d'amender le principe du patrimoine
commun **et** d'être partie à tout accord y dérogeant ; l'article 309 interdit
les réserves. **Trois verrous coordonnés, contournés en douze ans** par un accord
de 1994 qui ne s'appelle pas un amendement — il s'appelle un accord
d'application — et qui dispose qu'en cas d'incompatibilité **ses dispositions
l'emportent.** Motif écrit au préambule : les approches de marché, et le
ralliement de ceux qui refusaient d'adhérer. **La clause n'a pas été violée : on
a changé ce à quoi le principe se combine.** L7.C13 fait de la sanctuarisation la
condition sine qua non de l'émergence des unités ; elle est réalisable, **elle
n'est pas stable**, et le motif du contournement est exactement celui qu'un
dispositif mondial invoquerait.

**Second — le corpus tient trois textes fondateurs sans la transaction qui les a
rendus applicables.** Statuts du Fonds de 1944 (avant 1969 et 1978), régime des
fonds marins de 1982 (avant l'accord de 1994), traité européen d'avant Lisbonne.
**Pour un seul des trois la transaction a été trouvée — et elle a inversé la
conclusion du chapitre.** Il n'y a donc aucune raison de supposer que les deux
autres seraient anodins. **Les chercher est prioritaire sur toute nouvelle
lecture.**

---

## Arbitrage A30 — la qualification juridique de l'unité émise, et le corpus n'en a aucune

**2026-09-06, à l'issue de la passe 1 du Livre 20.**

**Ce que le livre a établi.** L20.C02 : la prohibition du financement monétaire
vise trois opérations — le découvert, le crédit sous toute autre forme, et
l'acquisition directe d'un instrument de dette auprès d'un émetteur public.
**Une unité qui n'est le crédit de personne ne tombe sous aucun des trois**,
puisqu'il n'y a pas d'instrument de dette. Lue littéralement, la prohibition ne
l'atteint pas.

**Et l'objection ne disparaît pas : elle se déplace.** Elle passe de « ce que la
banque centrale a le droit de faire » à « **ce que l'unité émise est en
droit** » — titre de créance, réserve, instrument sui generis, moyen de
paiement. **Le corpus n'a jamais qualifié juridiquement l'unité NEMO, en
soixante-dix-huit chapitres.**

**Pourquoi cela ne peut plus attendre.** Trois chapitres du Livre 20 butent sur
cette absence. L20.C02 ne peut pas dire si la prohibition s'applique. L20.C05 ne
peut pas dire ce que vaut une unité sans cours légal — **elle ne libère pas le
débiteur, donc elle ne circule que par consentement**, et le corpus ne tient
aucun régime de monnaie complémentaire. L20.C11 ne peut pas dire si l'immunité
fiscale des titres émis par une institution internationale la couvre.

**Ce que l'arbitrage doit trancher, et c'est une décision de fond, pas de
rédaction.** L'unité est-elle (i) un titre de créance sur l'institution
émettrice — auquel cas elle est une dette, et L1.C20 tombe ; (ii) un avoir de
réserve créé ex nihilo et alloué, sur le modèle du droit de tirage spécial —
auquel cas le précédent existe et il faut l'ouvrir ; (iii) un instrument sui
generis créé par le traité — auquel cas le traité doit le définir, et personne
ne peut le qualifier avant lui. **Le corpus penche pour (ii) et ne détient pas
l'amendement de 1969 qui a créé les droits de tirage spéciaux.** Acquisition
prioritaire.

### A30 — ARBITRÉ PAR L'AUTEUR LE 2026-09-07, et une quatrième branche apparaît

**CE QUE L'AUTEUR A TRANCHÉ, verbatim** : « La banque centrale émet la monnaie à
but régénératif **adossée à une dette collective** ; son mécanisme de reflux est
collectif et se fait par des prélèvements (fontes) sur les transactions. **Ces
reflux diffèrent des mécanismes traditionnels de reflux particuliers où l'agent
rembourse son crédit.** Ce dispositif répond à une critique où la "monnaie sans
dette" serait une monnaie permanente et donc, inflationniste. » Sur (ii) : « On
peut l'étudier et s'en inspirer **si c'est pertinent**. » Sur (iii) : « **C'est
envisageable.** »

**CE QUE CELA RÈGLE — LA BRANCHE (i) TOMBE, ET PROPREMENT.** Elle demandait si
l'unité est un titre de créance **sur l'institution émettrice**, c'est-à-dire une
créance que le porteur détiendrait contre l'émetteur. **La réponse est que la
dette court dans l'autre sens et qu'elle est collective** : l'émission est
adossée à une dette collective, dont l'extinction ne passe pas par un débiteur
nommé mais par des prélèvements sur les transactions. **L1.C20 ne tombe pas.**

**ET LA FORMULATION DE L'AUTEUR EST PLUS FORTE QUE CELLE DU VOCABULAIRE.**
`reflux_collectif` énonce que « l'extinction ne dépend d'**aucun débiteur
nommé** » ; l'auteur dit « **adossée à une dette collective** ». **Ce n'est pas
la même chose : la seconde nomme un débiteur, il est simplement pluriel.** À
répercuter sur le vocabulaire en passe 2.

**QUATRIÈME BRANCHE, ET C'EST LA POSITION DU CORPUS :** *(iv) unité adossée à une
dette collective, à reflux collectif.* **Elle n'exclut pas (iii) — elle la
remplit.** L'auteur juge (iii) envisageable ; **(iii) est le véhicule, (iv) est
le contenu**, et le traité définirait l'unité comme adossée à une dette
collective à reflux collectif. **L6.C06 a montré qu'une catégorie irréductible
aux types existants fonctionne** pourvu qu'on puisse nommer ses traits —
inhérence, opposabilité, indifférence à la publicité.

**SUR (ii), UNE RÉSERVE DE PERTINENCE À PORTER AVANT D'OUVRIR L'AMENDEMENT DE
1969.** Un droit de tirage spécial **règle entre membres** ; L1.C26 pose que le
référentiel de change « n'est ni détenu, ni échangé, ni accepté en règlement ».
**On peut donc s'inspirer de sa MÉCANIQUE D'ALLOCATION sans emprunter sa
NATURE**, et c'est la lecture du texte qui le dira. Acquisition toujours
prioritaire, motif changé.

**DEUX POINTS OÙ LA RÉPONSE BUTE, TOUS DEUX DÉJÀ ENREGISTRÉS PAR LE CORPUS, ET
AUCUN N'EST JURIDIQUE.**

**Le premier est comptable, et il vient d'un arbitrage de l'auteur lui-même.**
`reflux_transactionnel`, arbitrage du 2026-09-05 : « ce reflux **n'est PAS une
annulation** [...] **La monnaie quitte donc la circulation sans être détruite.** »
**Si le reflux ne détruit pas, la dette collective n'est pas éteinte : elle est
transférée à l'actif de l'institution.** Cohérent avec P26 et L2.E09 — la
contrepartie est « une créance sur les fontes futures ». **Mais alors l'unité
n'est pas gagée sur une dette qu'on solde, elle est gagée sur un flux qu'on
encaisse**, et ce n'est pas le même objet juridique. **À trancher.**

**Le second est celui que `falsification.md` a enregistré le 2026-09-04 en
RETIRANT un crédit qu'il avait accordé**, et c'est le plus dur : « La créance
portée à l'actif du GES est un droit sur le produit futur d'un prélèvement assis
sur les transactions dégénératives — **c'est-à-dire sur l'assiette même que le
dispositif a pour mission de faire disparaître.** Les deux contreparties du même
passif reposent sur des hypothèses opposées quant à l'avenir [...] **Plus le
certificat dit vrai, moins la créance vaut.** »

**CE N'EST PAS UNE OBJECTION À LA QUALIFICATION : C'EST UNE OBJECTION À CE QUI LA
GARANTIT.** La dette collective à laquelle l'émission est adossée **a une assiette
qui s'érode par le succès même du dispositif.** Réparations possibles renvoyées à
**P55 et P56**.

### A30 — RÉVISION DU 2026-09-07, APRÈS OUVERTURE DU BLOC COMPTABLE

**LE BLOCAGE RÉSIDUEL ÉTAIT COMPTABLE, ET LE CORPUS L'INSTRUISAIT SUR LE MAUVAIS
RÉFÉRENTIEL.** Le vocabulaire posait qu'« un actif doit être une ressource
contrôlée par l'émetteur dont des avantages futurs sont attendus POUR LUI ».
**C'est le test du secteur privé.** Le cadre conceptuel IPSASB, ouvert le
2026-09-07, énonce autre chose : **un actif est « a resource presently
controlled by the entity as a result of past events »**, une ressource étant
**« a right to either SERVICE POTENTIAL or the capability to generate economic
benefits »**, et le potentiel de service permettant d'atteindre les objectifs de
l'entité **« without necessarily generating net cash inflows »**.

**CONSÉQUENCE : L'OBJECTION QUE LE CORPUS S'OPPOSAIT À LUI-MÊME N'EST PAS LE
TEST APPLICABLE.** Une émission dont la contrepartie n'engendre aucun flux de
trésorerie pour l'émetteur **n'est pas, par ce seul fait, sans contrepartie
recevable.**

**ET UNE TROISIÈME CONTREPARTIE APPARAÎT, versée à `falsification.md`.** IPSAS 51
reconnaît à l'actif **une ressource naturelle détenue pour sa conservation**, à
trois conditions cumulatives — potentiel de service probable, **contrôle** par
l'entité, **mesure fiable**. **Si la contrepartie est la ressource conservée et
non une créance sur les fontes futures, elle ne s'érode pas quand le dispositif
réussit : elle s'apprécie.**

**TROIS CONDITIONS RESTENT À ÉTABLIR, ET AUCUNE N'EST ACQUISE.** **Le contrôle** —
la ressource est sur le territoire d'un tiers, et le Livre 6 a établi qu'un
commun opposable pèse sur des propriétaires réels. **La mesure** — critère
bloquant de la norme, à défaut duquel la ressource est portée **en annexe et non
au bilan** ; le SEEA des Nations unies est le candidat, et il est ouvert.
**L'applicabilité** — rien n'établit que l'institution émettrice relève de la
comptabilité publique.

**A30 EST DONC DÉBLOQUÉ SUR LE DROIT ET SUR LA NORME, ET IL RESTE OUVERT SUR
TROIS FAITS.** Ce ne sont plus des questions de conception mais **des questions
de vérification**, ce qui change leur nature.

**ÉTAT DE A30 APRÈS CET ARBITRAGE.** **Il cesse d'être une question ouverte et
devient une question de rédaction** — (iii) comme véhicule, (iv) comme contenu,
(ii) à lire pour sa mécanique. **Il reste bloquant sur un seul point, et il n'est
pas juridique** : ce qui garantit la dette collective s'érode quand le dispositif
réussit. **L20.C02 peut désormais conclure ; L1.C29 et le bouclage ne le peuvent
pas.**

---

## Arbitrage A31 — la protection interne des cadres techniques n'a aucune solution documentée

**2026-09-06, à l'issue de la passe 1 du Livre 20.**

**L7.C10 § 5 avait routé vers le Livre 20 l'immunité légale des cadres techniques
pour leurs avis méthodologiques**, après avoir établi deux vecteurs de capture —
la poursuite pénale (INDEC, ELSTAT) et le budget — et jugé le second plus
difficile à fermer.

**Le Livre 20 a ouvert trois textes qui traitent la question, et les trois ferment
le même vecteur.**

- **Article 107 du traité européen** : interdit de solliciter ou d'accepter des
  instructions. Vise **les organes de décision**, non le personnel technique.
- **Article IX section 8 des statuts du Fonds** : immunité de procédure pour les
  actes accomplis en qualité officielle — « **except when the Fund waives this
  immunity** ». **L'immunité appartient à l'institution**, qui peut la lever.
- **Article XII section 4 (c) des mêmes statuts** : devoir de loyauté dû « **entirely
  to the Fund and to no other authority** », et obligation faite aux États de
  **s'abstenir de toute tentative d'influence**. Technique supérieure aux deux
  précédentes — elle vise le personnel, et elle porte sur le puissant — **et elle
  aggrave le second vecteur** : le paragraphe (b) confie au directeur général
  « the organization, appointment and dismissal of the staff ». **Résister à un
  État est fidélité ; résister à sa hiérarchie est manquement.**

**RÉSULTAT : trois techniques, un même angle mort.** Toute protection dirigée
vers l'extérieur laisse l'institution seule juge de ce qu'elle fait à
l'intérieur. **La demande de L7.C10 § 5 sort du Livre 20 DÉPLACÉE ET NON
RÉSOLUE**, et le corpus refuse de la porter comme satisfaite.

**Une seule piste, et elle n'est pas transportable.** L'article 36.2 des statuts
du SEBC donne compétence à une cour extérieure pour les litiges entre
l'institution et ses agents. **Cela suppose une juridiction acceptée par tous les
membres** — ce qui distingue un ordre juridique intégré d'une organisation
conventionnelle, et le dispositif du corpus est conventionnel.

**CE QUI RESTE À CHERCHER** : le statut de la fonction publique internationale et
la jurisprudence des tribunaux administratifs internationaux. **C'est le corps de
règles qui répondrait à la question, et il n'est pas au dossier.**

---

## Arbitrage A32 — le régime de change est la PARITÉ FIXE, et le triangle est respecté et non contourné

**2026-09-06. Arbitrage de l'auteur, rendu le jour où le corpus a relevé la divergence.**

**La divergence.** L2.C18 a établi que le livre et le Cahier Technique
énonçaient **deux régimes de change différents**. Le livre, chapitre 8 : « le
taux de change entre devises **demeure fixe par conception** », d'où « les
nations recouvrent toute la latitude de leurs politiques monétaires, **ainsi
que la libre circulation des capitaux** ». Le Cahier, épisode 11 : le triangle
« est contourné puisque le référentiel fixe une référence stable **sans exiger
la fixité des parités bilatérales** ». La divergence traversait même l'épisode
11, qui pose « parité fixe libellée en NES » au paragraphe de l'exécution.

**L'ARBITRAGE : « PARITÉ FIXE ! »** L'énoncé du **livre** l'emporte.
**Conséquences immédiates.** L11.C04 — *les instruments du reflux sous parité
fixe* — **conserve sa prémisse et n'est pas à reprendre**. C'est **l'épisode 11
du Cahier qui est à corriger**, sur la phrase du triangle.

**CE QUE L'ARBITRAGE A PRODUIT, ET QUE LE CORPUS N'ATTENDAIT PAS.** En rendant
la question précise — comment tenir la fixité sans nier le théorème —, il a
conduit à chercher le mécanisme, et **le mécanisme est dans le chapitre 9 du
livre**, que le corpus avait extrait sans le lire sur ce point : « [...]
**contrôle des capitaux** exposés au chapitre 8. **La fuite vers les actifs
spéculatifs ou polluants est interceptée par le premier ressort**, puisque la
fonte transactionnelle s'applique également à **l'acquisition d'actifs** :
acheter un bien à fort impact pour échapper au demurrage entraîne une perte
immédiate et bien supérieure. **Il ne reste donc qu'une issue : les actifs
réels domestiques à faible impact.** »

**LE DISPOSITIF A DONC UN CONTRÔLE DES CAPITAUX, ET IL NE LE NOMME PAS AINSI
LÀ OÙ IL PARLE DU TRIANGLE.** Le contrôle n'est pas administratif — nulle
autorisation préalable, nulle interdiction — **il est économique** : la sortie
reste licite et devient coûteuse.

**RÉSULTAT : LE TRIANGLE N'EST PAS CONTOURNÉ, IL EST RESPECTÉ.** Le dispositif
prend **fixité des parités + autonomie monétaire**, et paie par **une mobilité
des capitaux restreinte**. C'est **le coin de Bretton Woods**, et c'est une
position défendable — infiniment plus solide que la prétention à tenir les
trois sommets, qui exigerait de réfuter un théorème et n'en fournit pas le
moyen.

**PRÉCÉDENT EXPRÈS, ouvert le même jour.** Statuts du Fonds de 1944, **article
VI section 3** : « **Members may exercise such controls as are necessary to
regulate international capital movements**, but no member may exercise these
controls in a manner which will **restrict payments for current transactions**
or which will unduly delay transfers of funds in settlement of commitments. »
Et **section 1 (a)** : le Fonds pouvait **demander** à un membre d'exercer de
tels contrôles, à peine d'inéligibilité. **Le contrôle des capitaux n'est pas
une tolérance : c'est un droit écrit dans le traité qui organisait les parités
fixes.**

**CE QUE L'ARBITRAGE EXIGE À SON TOUR — contrainte nouvelle pour le Livre 11.**
L'article VI assortit ce droit d'une limite : les contrôles **ne doivent pas
restreindre les paiements des transactions courantes**. Or la fonte
transactionnelle frappe **les transactions**, sans que L11.C05 ait jamais
distingué celles qui sont **en capital** de celles qui sont **courantes**. Un
prélèvement sur l'acquisition d'un actif est un contrôle des capitaux, licite ;
**un prélèvement sur le paiement d'une importation est une restriction des
transactions courantes**, que le même article interdit — et L20.C19 a montré
que le droit du commerce pose une contrainte parallèle sur les charges à la
frontière.

**À FAIRE EN PASSE 2, et c'est chiffrable :** séparer, dans l'assiette du
reflux transactionnel, les transactions en capital des paiements courants. **La
définition des seconds est fournie par l'article XIX (i) des mêmes statuts, que
le corpus détient et n'a pas employé** — il y énumère les paiements dus au
titre du commerce extérieur, les intérêts et revenus d'investissement, les
amortissements d'un montant modéré, et les envois de famille modérés.

---

## Arbitrage A33 — le nombre de chapitres d'un livre n'est pas contraignant

**2026-09-06. Arbitrage de l'auteur : « Le nombre n'est pas fixé. »**

**La question.** `corpus/livres.yaml` annonçait **douze** chapitres pour le
Livre 2 — les douze épisodes du Cahier Technique —, et la passe 1 en a produit
**vingt**, en ajoutant huit chapitres de doctrine que le Cahier ne cite pas. Le
corpus a signalé l'écart plutôt que de le résoudre, la règle voulant que le
plan directeur tranche et que le registre soit corrigé, jamais l'inverse.

**L'ARBITRAGE.** Le compte annoncé **n'est pas contraignant**.
`chapitres_annonces` passe à `null` pour le Livre 2.

**PORTÉE GÉNÉRALE, à appliquer aux autres livres.** Le Livre 11 avait déjà
dépassé son annonce, et le registre l'avait enregistré comme une anomalie.
**Sous cet arbitrage, ce n'en est plus une.** Le champ `chapitres_annonces`
cesse d'être une contrainte de conception : **il est une estimation, et la
matière décide.** Ce qui reste contraignant est le **matricule** du livre, que
la convention interdit de réattribuer, d'insérer ou de renuméroter — et cette
règle-là n'est pas touchée.

## Arbitrage A34 — le barème qui dit vrai exclut, et le corpus ne l'a jamais traité

**POSÉ LE 2026-09-07, en défrichant L6.C10.** Le dispositif module ses
prélèvements sur l'impact : L1.C21 construit un reflux transactionnel dont le
taux suit l'empreinte, L11.C24 pose un barème aux frontières, L11.C03 affecte
chaque instrument à l'objectif sur lequel il agit le plus directement. **Toute
cette construction repose sur une idée unique — faire dire au prix la vérité
écologique.**

**LE CORPUS N'A JAMAIS INSTRUIT QUI CE SIGNAL EXCLUT.** L1.C21 et L11.C24
raisonnent sur l'orientation des comportements ; ils supposent que l'agent
confronté au prix modifie son choix. **Ils ne traitent pas l'agent qui ne peut
pas payer le prix et qui n'a pas de choix à modifier.**

**LE DROIT FRANÇAIS A TRANCHÉ CE DILEMME, DANS L'AUTRE SENS, ET PAR LA LOI.**
Le régime d'indemnisation des catastrophes naturelles repose depuis 1982 sur
une **surprime uniforme non indexée sur le risque**, adossée aux contrats
d'habitation et réassurée publiquement. **Une prime indexée sur le risque
rendrait l'assurance inaccessible là où elle est le plus nécessaire** : le
législateur a donc retiré au prix sa fonction de signal, sur ce marché-là, et
assumé de faire porter l'écart par la solidarité nationale. **C'est un choix
explicite, ancien de quarante-quatre ans, et il vise exactement la propriété que
le dispositif recherche.**

**CE QUE LE CORPUS DOIT TRANCHER, ET CE N'EST PAS À LUI DE LE FAIRE.**

| | La question | Ce qu'elle engage |
|---|---|---|
| **1** | **Le dispositif comporte-t-il une franchise, un seuil d'exemption ou un abattement selon la capacité contributive ?** | Le demurrage en a un — « au-delà d'un seuil d'exemption indexé », dit le vocabulaire. **Le reflux transactionnel n'en a aucun**, et rien n'explique cette asymétrie entre les deux instruments du reflux collectif |
| **2** | **Ou bien l'exclusion est-elle assumée, et compensée en aval** par une allocation, un transfert ou une gratuité d'accès ? | Alors le dispositif comporte **deux mécanismes de sens opposé**, et la question de leur bouclage se pose comme celle de L11.C01 § 4 |
| **3** | **Ou bien certains biens sortent-ils de l'assiette** parce qu'ils sont des essentiels au sens de L1.C06 ? | Alors il faut une **liste**, donc un barème de plus, et l'arbitrage A8 sur le chantier unique des barèmes s'élargit |

**CE QUE L'ARBITRAGE N'EST PAS.** Ce n'est pas l'objection distributive
classique — « les taxes écologiques sont régressives » — que le corpus peut
traiter par le rendement. **C'est plus étroit et plus dur : sur les biens dont
l'empreinte est la plus élevée, le signal doit être fort pour agir, et c'est là
qu'il exclut le plus.** L'effet Veblen, déjà versé en L11.C03, dit que sur les
biens de position le renchérissement n'a pas de signe établi ; **A34 dit qu'aux
autres extrémités de l'échelle, il en a un et qu'il n'est pas celui qu'on
cherche.**

**RÉSERVE.** Le régime de 1982 est connu par le registre du Livre 6 et **son
texte n'a pas été lu**, non plus que le rapport de 2024 ni l'exercice
prudentiel de décembre 2024 qui en projettent la tension. **L'arbitrage porte
sur une figure, non sur un chiffre.**

---

## Balayage rétrospectif de la passe 1 du Livre 6 — exécuté le 2026-09-07

**QUATRE PASSES DE DETTE SOLDÉES D'UN COUP**, sur décision de l'auteur : le
balayage se fait **à la clôture de la passe**, non à la fin du corpus. Motif
retenu — avec onze livres encore à ouvrir, **le graphe des renvois deviendrait
trop dense pour être balayé** si l'annotation était différée.

**SEIZE CHAPITRES ANNOTÉS**, hors Livre 6, chacun recevant ce que la passe 1 du
Livre 6 lui rend. Chaque annotation porte l'en-tête « BALAYAGE DU LIVRE 6 » et
déclare que **ce qui est versé n'a pas été instruit dans le chapitre d'accueil
et ne modifie pas ce qui précède** : c'est un dépôt pour la passe 2.

| Chapitre | Ce qu'il reçoit |
|---|---|
| **L1.C07** | le créancier hypothécaire décide **de ce qui peut être protégé**, pas seulement de ce qui se finance — et la sortie italienne : une charge inhérente ne demande pas sa permission |
| **L1.C09** | **cinquième règle jamais énoncée : ce qui devient finançable est LE LITIGE**, monétisé, avancé, assuré contre l'annulation |
| **L1.C11** | la troisième malédiction **s'énonce en droit des biens**, acte par acte, sans faute d'aucune partie |
| **L1.C21** | **arbitrage A34** — le barème qui dit vrai exclut ; le régime de 1982 a tranché l'inverse par la loi ; et **le signe de l'effet d'anticipation n'est pas acquis** |
| **L7.C13** | la sanctuarisation demandée **armera aussi ceux qui viendront après**, et ce qu'elle produirait serait **une servitude, non un commun** |
| **L11.C03** | un instrument existant **retire au prix sa fonction de signal, par la loi** — l'affectation suppose un préalable non posé |
| **L11.C16** | la **valorisation à bénéficiaire nommé** existe en droit positif ; et **ce n'est pas l'inaliénabilité qui fait tenir un commun** |
| **L11.C24** | appui **et limite** de l'extraterritorialité ; **le seuil défini par sa conséquence** et son coût |
| **L11.C25** | **la filiale cédée pendant l'instance** ; et l'outil probatoire qui survit au régime qui l'entourait |
| **L11.C29** | **un plancher converti en plafond** : changement de nature, non de calibration ; deux techniques de dérogation bornée |
| **L20.C03** | l'égalisation de rang **existe** en droit national — **mais le contrôle est restreint : elle autorise, elle n'oblige pas** |
| **L20.C12** | **la réciproque** : ce que le traité ne pose pas, aucun échelon inférieur ne le posera valablement |
| **L20.C14** | **le juge n'était pas le maillon manquant** — et un quatrième cas où c'est la lenteur, non l'inexécution |
| **L20.C16** | le manque déclaré est **comblé** ; et la règle qui remplace celle du bloc |
| **L20.C17** | **la question est répondue et la technique protège l'investisseur** — vingt et un ans, cliquet à trois crans |
| **L20.C19** | l'appui extraterritorial et **sa limite exacte** ; le préambule visant **les autres peuples** |

**CE QUE LE BALAYAGE A COÛTÉ** : une exécution, sans arbitrage nouveau. **Ce
qu'il a révélé** : les couplages tenaient déjà tout — le retard n'était pas dans
la découverte mais dans le portage. **La leçon pour les onze livres à venir est
que le portage doit suivre la clôture immédiatement**, faute de quoi il devient
un chantier au lieu d'être une écriture.

## Balayage rétrospectif de la passe 1 du Livre 5 — exécuté le 2026-09-07

**LA RÈGLE ACQUISE À LA CLÔTURE DU LIVRE 6 EST APPLIQUÉE** : le portage suit la
clôture immédiatement. **Aucune dette de balayage n'est ouverte cette fois.**

**DIX CHAPITRES ANNOTÉS**, hors Livre 5, chacun recevant ce que la passe 1 du
Livre 5 lui rend. Chaque annotation porte l'en-tête « BALAYAGE DU LIVRE 5 » et
déclare que **ce qui est versé n'a pas été instruit dans le chapitre d'accueil
et ne modifie pas ce qui précède** : c'est un dépôt pour la passe 2.

| Chapitre | Ce qu'il reçoit |
|---|---|
| **L1.C20** | **un test normatif extérieur sur l'unité** — principe 9, « little or no credit or liquidity risk » ; **A30 a fixé la contrepartie sans dire si elle le satisfait** |
| **L1.C25** | **ses trois épisodes portent sur une SUBSTITUTION**, le dispositif s'ajoute ; la première branche de F6 est déplacée — **contre une absence de précédent** |
| **L1.C27** | **le seuil est un solde, pas une somme** ; et **les trois leviers de club opèrent par soustraction**, ce qui ne vaut plus quand le dispositif s'ajoute ; la densité du commerce interne est un paramètre du seuil |
| **L3.C05** | **le prix de « joignable »** — opposabilité binaire par juridiction ; **la participation en paliers** ; et les trois voies ne sont pas des alternatives mais des pièces |
| **L3.C09** | **son résultat commande toute l'analyse de l'adoption** — avantage d'entrée, absence de bénéfice, **et motif pour lequel la seconde branche de F6 tient** : un seul fait vu trois fois |
| **L6.C09** | **F8 s'applique à un second objet : la base juridique d'un rail** — une base désarmée **autorise la dépense** au lieu de l'arrêter |
| **L7.C05** | **fixer reste central, vérifier gagne à être régional** — il manque un échelon qui ne délibère pas mais constate, et sa forme n'est pas décidée |
| **L7.C12** | **le mécanisme cherché est trouvé** — participation en paliers, principe 19 ; **le premier entrant gagne une position d'intermédiaire**, seul gain d'entrée indépendant du succès |
| **L11.C10** | **troisième occurrence d'un patron** — obligation indexée sur un état observable ; **le coût est structurel** ; et **la réparation transforme le problème** |
| **L20.C13** | **il tient les portes, non la réaction de ce qui les entoure** ; la protection expire quand la couche déplace des flux, **et rien ne couvre ce moment** |

**CE QUE LE BALAYAGE A PORTÉ AUX PROTOCOLES.** **F6** reçoit l'état que le Livre 5
lui laisse — première branche déplacée, seconde intacte et **expliquée par le
livre lui-même**. **F8** reçoit un élargissement à une seconde famille d'objets :
tout instrument dont le dispositif tire son opposabilité.

**CE QU'IL A RÉVÉLÉ, ET C'EST UN RÉSULTAT ET NON UNE TÂCHE.** **Le meilleur
acquis du livre et son échec devant F6 sont le même fait.** L'adhésion qui ne
retire rien protège l'entrée et épargne le créancier. **Le corpus n'a donc pas
à chercher une meilleure voie d'entrée : il a à écrire la seconde phase**, celle
où la couche épaissit — **et c'est le seul endroit où F6 peut se lever.**

**CE QUE LE BALAYAGE N'A PAS FAIT.** Il n'a estimé **aucun coût humain** et
**aucune probabilité**, alors que la contrainte arrêtée par l'auteur le
2026-09-04 les exigeait et que L5.C01 l'avait déclarée opposable à chaque
chapitre du livre. **L5.C09 l'enregistre comme un manquement et non comme une
réserve**, et relève que **l'omission joue dans un sens** : elle allège les
quatre voies, et le plus celle qui touche des habitants. **À solder en passe 2,
faute de quoi la contrainte n'est pas une contrainte mais une intention.**

## Balayage de la première tranche du Livre 18 — exécuté le 2026-09-07

**CE BALAYAGE NE SUIT PAS UNE CLÔTURE DE PASSE, ET C'EST DÉLIBÉRÉ.** La passe 1
du Livre 18 **reste ouverte** : CARE/TDL et la comptabilité multicapitaux, que
l'auteur a nommés le 2026-09-07 comme termes de comparaison centraux, **ne sont
pas ouverts** — téléchargement échoué sur une épreuve anti-robot non contournée,
PDF demandés à l'auteur. **Le portage est néanmoins exécuté maintenant**, par
application de la leçon tirée du Livre 6 : ce qui est acquis contredit ou
corrige dès aujourd'hui des chapitres de cinq livres, **et différer le portage
en ferait un chantier au lieu d'une écriture.**

**ONZE CHAPITRES ANNOTÉS**, hors Livre 18, sous l'en-tête « BALAYAGE DU LIVRE 18 ».

| Chapitre | Ce qu'il reçoit |
|---|---|
| **L1.C09** | **le gradient des quatre instruments** — charge, annexe, rapport de gestion, rapport facultatif ; et **l'arrêt devant le bilan a été DÉCIDÉ en octobre 2008**, après consultation |
| **L1.C18** | son § 5 **confirmé sur source primaire** ; et **un second mode d'échec que F2 ne capture pas** — à mesure parfaite, l'unité de compte reste la mauvaise |
| **L1.C20** | **la partie double** — charge chez l'émetteur et produit chez le bénéficiaire se déclenchent au même fait ; **produire l'actif ou assumer de s'écarter du référentiel** |
| **L1.C29** | **les trois conditions d'A30 n'ont plus le même sort** — applicabilité immobile, mesure échouée par structure, **contrôle devenu exclusion de définition** |
| **L5.C05** | **les impacts matériels sont déplacés hors de la région par le commerce** — la proximité géographique ne coïncide pas avec la proximité des effets |
| **L5.C08** | le rapport qu'il déclarait non instruit l'est ; **le substitut vient du sous-sol, hors de portée du barème** — **le déverrouillage passe par un secteur exempté** |
| **L6.C06** | **le droit réel inhérent EST la « capacité de restreindre » que la norme comptable réclame** ; et la question qui lui est renvoyée |
| **L6.C08** | **plus de trois milliards de tonnes de minéraux de transition** — le détachement du sous-sol ne vise pas un cas marginal mais la voie de sortie |
| **L11.C13** | **réguler ne vaut pas contrôler** — la voie « nous encadrons » est fermée par le texte ; **et le SEEA sert la calibration du barème** |
| **L11.C16** | **la valorisation à bénéficiaire nommé est l'une des deux moitiés de la sortie de F9** ; et la valeur d'échange la rend systématiquement inférieure |
| **L20.C02** | **qualification juridique et qualification comptable de l'unité ne sont pas indépendantes**, et le corpus les traitait séparément |

**CE QUE LE BALAYAGE A PORTÉ AUX PROTOCOLES.** **F2** reçoit sa confirmation sur
source primaire **et son rétrécissement** : il porte sur le seuil d'allocation,
non sur le bilan. **F9 EST POSÉ** — le titre, et non la mesure.

**CE QU'IL A RÉVÉLÉ.** **Le corpus cherchait une mesure ; l'obstacle était un
titre.** Cinq chapitres ont été écrits en supposant que la difficulté était
d'évaluation, et la norme dit que **la capacité d'exclure distingue l'actif du
bien public accessible à tous** — c'est-à-dire que **la propriété définitoire du
commun est celle qui l'exclut du bilan.** **Le Livre 18 renvoie donc sa question
au Livre 6**, et non à la statistique.

**CE QU'IL N'A PAS FAIT.** La comparaison que le plan annonce — comptabilité
conventionnelle contre CARE/TDL et comptabilités multicapitaux — **n'est pas
commencée.** Le livre tient le versant des normes en vigueur **et aucun modèle
concurrent**, ce qui rend son verdict provisoire : **un modèle alternatif est
précisément une proposition de réécrire ce que ce balayage vient de constater.**

## Arbitrage A35 — QUI PORTE LA DETTE COLLECTIVE ? La question qui commande tout le reste

**OUVERT LE 2026-09-07 (nuit), à l'issue de la première tranche du Livre 10.**
**Ce n'est pas une question de droit : c'est une question de conception, et elle
revient à l'auteur.**

**CE QUI EST ARRÊTÉ.** A30, le 2026-09-07 : « **La banque centrale émet la monnaie
à but régénératif adossée à une dette collective ; son mécanisme de reflux est
collectif.** » **Le corpus n'a nulle part dit DE QUI cette dette est la dette.**

**POURQUOI CELA NE PEUT PLUS ATTENDRE.** **Règlement (CE) n° 3603/93, article
premier § 1 b) iii)** : « autre type de crédit » = **« toute opération avec le
secteur public qui se traduit ou est susceptible de se traduire par une créance
sur celui-ci »**. **Article 3** : le secteur public comprend « les institutions ou
organes de la Communauté, les administrations centrales, les autorités régionales
ou locales, les autres autorités publiques et **les autres organismes ou
entreprises publics** ».

**L'ALTERNATIVE EST BINAIRE, ET AUCUNE INGÉNIERIE DE L'UNITÉ NE LA DÉPLACE.**

| Terme | Conséquence |
|---|---|
| **Le débiteur relève du secteur public** — États membres, institution commune détenue par eux, entreprise publique | **Crédit prohibé de plein droit.** La troisième branche n'exige aucun instrument : elle vise **l'opération et son résultat**. La forme de la monnaie devient indifférente, et l'échappatoire de L20.C02 est sans objet |
| **Le débiteur n'en relève pas** | **La prohibition ne l'atteint pas du tout**, et quatre chapitres du Livre 10 deviennent sans objet sur ce point. **Mais il reste à dire QUI, hors du secteur public, porte une dette collective mondiale** — le corpus n'en a aucune idée, et c'est peut-être plus difficile que le problème qu'on résout |

**CE QUE LE CORPUS PEUT DIRE, ET C'EST PEU.** L1.C27 fait reposer le seuil
d'activation sur une **coalition d'États** ; L20.C13 tient un mécanisme
d'amorçage par **contributions d'États** ; L7 organise une institution
internationale. **Tout ce que le corpus a écrit oriente vers le premier terme**,
c'est-à-dire vers celui qui déclenche la prohibition.

**CE QUE L'ARBITRAGE DOIT TRANCHER, EN UNE PHRASE.** *La dette collective est-elle
une dette DES ÉTATS MEMBRES envers l'institution émettrice, une dette DE
L'INSTITUTION envers ses membres, ou une obligation portée par LES BÉNÉFICIAIRES
DE L'ÉMISSION eux-mêmes ?* **Les trois réponses produisent trois dispositifs
différents, et une seule sort du champ de l'article 123.**

### A35 ARBITRÉ LE 2026-09-07 (nuit) — LA SOCIÉTÉ ENTIÈRE, ET LE DISPOSITIF CHANGE DE BRANCHE DU DROIT

**RÉPONSE DE L'AUTEUR, citée intégralement en L10.C06 [S1].** « L'idée de dette
collective **s'oppose au concept de dette individuelle** et n'est pas liée aux
mêmes mécanismes d'émission monétaire [...] **La monnaie à vocation régénérative
ne peut pas suivre ce même concept, car LA RENTABILITÉ N'EST PAS COMPATIBLE AVEC
LA RÉGÉNÉRATION (essentiel insolvable).** [...] il faut donc envisager des
**dispositifs de reflux alternatif**. **Et c'est la société entière qui porte
cette dette.** [...] La consommation de biens et services à fort impact implique
des reflux (fontes) **graduellement plus forts**. »

**LE SECOND TERME EST RETENU. TROIS CONSÉQUENCES, DONT DEUX N'ÉTAIENT PAS PRÉVUES.**

**CORRECTION DU 2026-09-07 (nuit), SUR REVUE CONTRADICTOIRE — À LIRE AVANT LES
TROIS CONSÉQUENCES CI-DESSOUS.** **La conséquence (1) était trop forte et devient
conditionnelle ; la conséquence (3) n'est qu'une branche parmi six.**

**SUR (1).** « Aucun débiteur individuel identifié » et « aucune obligation
juridiquement opposable à une entité » **sont deux propositions différentes**.
Une charge collective peut être portée en droit par une personne publique, une
organisation internationale, un fonds, une communauté d'États, ou par les membres
au titre d'une obligation commune. **A35 décrit L'INCIDENCE ÉCONOMIQUE de la
charge ; il ne dit pas qui l'assume EN DROIT.** **Conclusion exacte** : *si* les
textes constitutifs ne créent aucune créance opposable à une entité du secteur
public, la branche sort du champ ; *si* une entité garantit, rembourse, convertit
ou compense l'unité, **le test de l'article 123 doit être refait**. **AUCUNE
CONCLUSION SUR L'ARTICLE 123 NE DOIT ÊTRE PROPAGÉE** avant qu'une **fiche de
spécification de l'unité** soit écrite — droits du détenteur, obligations de
l'émetteur, règle de conversion, extinction, détenteurs autorisés, sort en cas de
sortie d'un membre.

**SUR (3).** Ni IPSAS 48 ni IPSAS 47 n'imposent la qualification de dépense
publique. Leur application suppose d'identifier **la ressource remise, le contrôle
antérieur, le bénéficiaire, l'existence d'un accord contraignant et le référentiel
applicable** — le corpus n'en tient aucun. **Et la fonte n'est pas automatiquement
un prélèvement obligatoire** : l'arbre de qualification posé en L10.C06 compte
**six branches** — impôt, contribution affectée, redevance, **frais de réseau**,
**règle monétaire**, obligation conventionnelle — et **huit critères** les
départagent. **La branche « règle monétaire » n'exige aucune compétence fiscale**,
mais exige que l'unité soit celle de l'émetteur, **ce qui ramène à la question du
passif que A35 laisse ouverte.**

**CE QUI SUBSISTE SANS RÉSERVE.** La conséquence (2) — IPSAS 47 § 18 exclut le
flux futur de fontes de l'actif, « an intention to levy taxation is not a past
event ». Et la question ouverte : **qui lève la fonte, et de quel titre**, quelle
que soit la branche retenue.

**(1) L'OBSTACLE JURIDIQUE EST LEVÉ, ET SUR UN MOTIF MEILLEUR QUE CELUI DU
CORPUS.** La société entière n'est aucune des institutions énumérées à l'article 3
du règlement 3603/93. **La définition-balai ne l'atteint pas, parce qu'il n'y a
pas de créance sur le secteur public.** **L'échappatoire de L20.C02 est rétablie :
l'obstacle réel n'était pas l'absence d'INSTRUMENT, c'était L'ABSENCE DE
DÉBITEUR.** **L10.C02 à C05 gardent leur valeur d'instruction et perdent leur
portée d'objection.**

**(2) LA MÊME PROPRIÉTÉ REFERME LA QUESTION COMPTABLE, ET UNE NORME VISE LE CAS
NOMMÉMENT.** Sans débiteur, aucune créance ; et l'article 6 de l'orientation
BCE/2016/34 exige **le transfert à l'entité de l'essentiel des risques et
avantages**. Reste la voie du **flux futur de fontes** — **IPSAS 47 § 18 l'exclut
par un exemple qui est exactement le cas** : « Transactions or events **expected to
occur in the future do not in themselves give rise to assets** — for example,
**AN INTENTION TO LEVY TAXATION IS NOT A PAST EVENT** that gives rise to an asset
in the form of a claim against a taxpayer. » **Le fait générateur n'aura lieu
qu'à la consommation.** **ON NE PEUT PAS SIMULTANÉMENT N'AVOIR AUCUN DÉBITEUR —
pour échapper à l'article 123 — ET DÉTENIR UNE CRÉANCE RECONNAISSABLE.**

**(3) LE DISPOSITIF CHANGE DE BRANCHE DU DROIT, ET C'EST LE RÉSULTAT PRINCIPAL.**
Une émission sans débiteur, recouvrée par un prélèvement gradué sur l'impact,
**n'est pas une opération de crédit : c'est une DÉPENSE PUBLIQUE dont la ressource
est un PRÉLÈVEMENT** — charge à l'émission, produit au reflux, ce que décrivent
précisément IPSAS 48 et IPSAS 47. **Le dispositif y gagne un régime comptable
cohérent, au prix de cesser d'être adossé.** Cela **explique** pourquoi la
rentabilité n'a pas à être compatible avec la régénération — une dépense
publique n'a pas de taux de rendement — et pourquoi le reflux est alternatif —
un impôt n'est pas un remboursement.

**CE QUE L'ARBITRAGE OUVRE, ET C'EST LA NOUVELLE QUESTION LA PLUS URGENTE DU
CORPUS.** **Une fonte graduée selon l'impact, levée sur les agents, est un
PRÉLÈVEMENT OBLIGATOIRE.** **Un prélèvement suppose une compétence fiscale, et une
compétence suppose un titulaire.** **Le corpus n'a jamais dit QUI LÈVE LA FONTE NI
DE QUEL TITRE**, et ne tient ni traité fiscal, ni compétence déléguée, ni
précédent d'un prélèvement levé à l'échelle mondiale. **Le problème du secteur
public n'a pas disparu : il a changé de côté du bilan, passant de l'actif au
prélèvement.**

**PRÉCISION DE FORMULE, PORTÉE SANS OBJECTION.** L'auteur écrit que la société
entière porte la dette, et que **le choix est donné aux agents**. Si la charge est
modulée par la décision de chacun, **la dette est collective PAR SA CAUSE et
individuelle PAR SON INCIDENCE** — c'est la structure d'un impôt pigouvien, dont
l'assiette est un comportement et le motif un dommage commun. **La formule
décrit le motif, non le porteur.** **L11.C09 reçoit la question de savoir qui
paie effectivement, répercussion comprise** — et **L1.C15 ayant établi que
l'essentiel est insolvable, il faut vérifier que l'assiette ne le reproduit pas.**

**CE QUE L'ARBITRAGE NE TRANCHE PAS.** **Il porte sur l'actif** — de qui l'unité
est la créance — **et ne dit rien du passif.** Si l'unité n'est la dette de
personne en particulier, **est-elle une dette de l'émetteur ?** Un billet figure
au passif d'une banque centrale ; **le corpus n'a jamais dit ce que l'unité est au
passif, et A30 ne l'a pas tranché non plus.**

**NE PAS TRANCHER A UN COÛT, ET IL EST DÉSORMAIS CHIFFRABLE EN CHAPITRES.** Quatre
chapitres du Livre 10 raisonnent sur des cas de figure faute de cette décision ;
L20.C02 tient une échappatoire défaite ; L18.C06 avait déjà déclaré que le corpus
« n'a jamais dit quelle entité comptable porterait l'écriture ». **C'est la même
question, rencontrée par deux livres qui ne se parlaient pas.**

## RÈGLE DE MÉTHODE ACQUISE LE 2026-09-07 (nuit) — LE PAS DE TROP

**ÉNONCÉ.** *Le corpus passe trop vite de l'énoncé conceptuel ou politique à la
qualification juridique ou comptable. Entre « la société porte cette dette » et
« il n'existe aucun débiteur en droit », il y a un pas ; entre « une fonte graduée
sur l'impact » et « un prélèvement obligatoire », il y en a un autre. Ce pas doit
être écrit, et il doit être étayé.*

**COMMENT ELLE A ÉTÉ ACQUISE.** Une revue contradictoire extérieure, le 2026-09-07,
a relevé **six erreurs en une soirée** : trois qualifications trop rapides
(L10.C06), une confusion de catégories (L18.C05), et **deux erreurs comptables**
— une analogie fausse sur l'achat de titre par une banque centrale (L11.C02) et
la partie double présentée comme une loi de conservation mondiale (L18.C05).

**CE QUI REND LA LEÇON UTILE PLUTÔT QUE MORTIFIANTE.** **Quatre des six corrections
jouent EN FAVEUR du dispositif.** Le corpus s'était donné pour règle de ne jamais
flatter ; **il a dérivé vers la faute symétrique, la sévérité hâtive**, qui n'est
pas plus rigoureuse. **Conclure trop vite contre une thèse n'est pas plus honnête
que conclure trop vite pour elle : c'est le même défaut de démonstration.**

**CE QU'IL FAUT FAIRE, CONCRÈTEMENT.** **(1)** Quand un chapitre passe d'un plan à
un autre — politique vers juridique, conceptuel vers comptable — **le marquer et
le justifier**, jamais l'enchainer. **(2)** Devant une qualification, **poser
l'arbre des branches possibles et les critères qui les départagent AVANT de
choisir**. **(3)** Ne jamais employer un terme technique — « commun », « bien
public », « dette », « prélèvement » — **sans dire lequel des sens on retient**.
**(4)** Vérifier une écriture comptable **avant** de s'en servir comme analogie.

**CINQ OBJETS À VERROUILLER AVANT DE CONCLURE, ordre de travail retenu.**
**L'UNITÉ** — fiche de spécification : droits du détenteur, obligations de
l'émetteur, conversion, extinction, détenteurs autorisés, sortie d'un membre.
**LE DÉBITEUR** — qui, s'il en est un, porte l'obligation en droit. **LE PASSIF**
— ce que l'unité est au passif de l'émetteur. **LE PRÉLÈVEMENT** — quelle branche
de l'arbre, quelle autorité, quelle voie d'adoption. **LES ÉCRITURES
INTER-ENTITÉS** — trois jeux complets et séparés : émetteur, banque centrale
nationale, bénéficiaire, avec les branches destruction, accumulation et fonds
propres négatifs assumés.

## Arbitrage A36 — LA FONTE EST-ELLE UN PRÉLÈVEMENT OU UNE DÉCOTE ? Le choix décide de la nature du dispositif

**OUVERT LE 2026-09-07, à l'issue de L23.C06**, qui a emprunté pour la première
fois l'arbre de qualification posé par L10.C06. **Ce n'est pas une question de
droit : c'est une question de conception, et elle revient à l'auteur.**

**CE QUI EST ÉTABLI.** L'arbre comptait **six branches**. **Quatre tombent**, et sur
des critères simples. **La redevance** — la fonte croît avec le dommage causé à des
tiers, donc **celui qui paie le plus NUIT le plus, il ne reçoit pas le plus**.
**Les frais de réseau** — s'y soustraire signifierait **sortir de l'économie
monétaire**, et un choix qui coûte de cesser d'acheter n'est pas contractuel.
**L'obligation conventionnelle** — un agent qui utilise une monnaie **n'a rien
souscrit** ; la branche reste ouverte entre ÉTATS, elle est fermée à l'égard des
AGENTS, que A35 désigne comme payeurs. **Restent DEUX branches.**

**L'ALTERNATIVE, ET LES DEUX TERMES NE DIFFÈRENT PAS PAR LEUR EFFET ÉCONOMIQUE.**
Un prélèvement gradué et une décote graduée **peuvent produire le même signal de
prix** ; **ils ne s'obtiennent pas au même endroit ni du même monde.**

| | **BRANCHE FISCALE** — contribution affectée | **BRANCHE MONÉTAIRE** — règle de décote |
|---|---|---|
| **Autorité** | compétence des États | compétence de l'émetteur |
| **Voie d'adoption** | traité fiscal, compétence déléguée ou harmonisation | décision de politique monétaire |
| **Percepteur** | administrations nationales | **aucun** |
| **Obstacles instruits au Livre 23** | **les quatre** — souveraineté préservée par le mandat onusien, défaut d'alignement du percepteur, correctif qui est lui-même une variable de négociation, vérification restreinte par les droits fondamentaux | **aucun** |
| **Obstacle propre** | **F10 y frappe le plus fort** : un accord fiscal mondial servirait aussi bien à supprimer 2 000 milliards de subventions, quand l'écart n'est que de 351 | **la question du passif**, qu'A30 et A35 laissent ouverte et **que le Livre 19 porte** |

**POURQUOI LA BRANCHE MONÉTAIRE ÉCHAPPE À TOUT, et le corpus le dit aussi nettement
que les objections.** **Une décote ne prélève rien sur un patrimoine extérieur :
elle modifie la valeur d'un instrument que l'émetteur a lui-même créé.** **Ce
n'est pas une créance sur l'agent, c'est une propriété de l'unité qu'il détient.**
Pas de compétence fiscale, pas de percepteur, pas d'assiette à reconstituer chez
des tiers opaques, pas de budget.

**ET POURQUOI ELLE NE SUFFIT PAS EN L'ÉTAT.** **Une décote ne frappe que l'ENCOURS
détenu.** **La gradation selon l'impact suppose de frapper LA TRANSACTION.** **Une
décote sur transaction ressemble à un prélèvement ; une décote sur encours ne peut
pas être graduée selon l'impact.** **LA BRANCHE LA PLUS FAVORABLE JURIDIQUEMENT EST
LA MOINS COMPATIBLE AVEC LA MÉCANIQUE ARBITRÉE EN A35.** S'y ajoute qu'un agent qui
convertit immédiatement échappe à une décote sur encours.

**CE QUE L'ARBITRAGE DOIT TRANCHER, EN UNE PHRASE.** *La fonte frappe-t-elle
L'ENCOURS détenu — auquel cas elle est une règle monétaire, ne demande aucune
compétence fiscale, et ne peut être graduée que par la durée de détention — ou LA
TRANSACTION — auquel cas elle peut être graduée selon l'impact, et demande une
compétence de lever que le droit international ne crée nulle part à ce jour ?*

**UNE TROISIÈME VOIE EXISTE PEUT-ÊTRE ET LE CORPUS NE LA TIENT PAS** : **un
dispositif à DEUX ÉTAGES**, décote sur encours par règle monétaire pour la partie
qui ne demande aucune compétence, **et** contribution graduée sur transaction pour
la partie qui exige le signal d'impact. **Le corpus n'a instruit aucun instrument
hybride de ce genre**, et la combinaison hériterait des obstacles de la seconde pour
sa seconde moitié.

**CE QUE L'AUTEUR A DÉJÀ DIT ET QUI ORIENTE.** **A35 décrit des fontes
« graduellement plus fortes » selon l'impact de la consommation** — ce qui pointe
vers la transaction, donc vers la branche fiscale. **A30 décrivait une unité
adossée** — ce qui pointait vers la branche monétaire. **Les deux arbitrages
n'orientent pas du même côté**, et c'est ce qui rend celui-ci nécessaire.

**NE PAS TRANCHER A UN COÛT DÉSORMAIS CHIFFRABLE.** Six chapitres du Livre 23
raisonnent sur une qualification indéterminée ; **le Livre 19 ne peut pas commencer
sans savoir si l'unité porte une décote** ; et **L11 ne peut pas calibrer un
instrument dont il ignore s'il porte sur un stock ou sur un flux.**

## Arbitrage A37 — QUELLE EST LA FORME JURIDIQUE DE L'INSTITUTION ÉMETTRICE ? Un texte vient d'en faire une condition d'existence

**POSÉ LE 2026-09-07 par L21.C06, après ouverture de la directive 98/26/CE.
ADRESSÉ À L'AUTEUR. Le corpus ne peut pas y répondre : c'est une décision de
conception, et personne ne l'a jamais prise par écrit.**

**CE QUI REND LA QUESTION INÉVITABLE MAINTENANT.** **Article 2 b) de la
directive** : est une « institution », donc un participant possible à un
système bénéficiant de la protection du caractère définitif, **un établissement
de crédit**, **une entreprise d'investissement**, « **un organisme public, ou une
entreprise contrôlée opérant sous garantie de l'État** », ou une entreprise
établie hors de la Communauté dont les fonctions correspondent aux premières.
**La liste est fermée.**

**L'ÉMETTEUR N'Y ENTRE QUE PAR LA PORTE DE L'« ORGANISME PUBLIC ».** Et le
corpus ne sait pas s'il y entrerait, **parce qu'il n'a jamais dit ce qu'est
l'institution émettrice**.

**QUATRE FORMES SONT CONCEVABLES, ET ELLES NE DONNENT PAS LE MÊME DISPOSITIF.**

1. **Organisation internationale créée par traité.** Argument sérieux pour la
   qualité d'organisme public ; immunités et personnalité juridique
   internationale ; **mais un traité se négocie et se ratifie**, ce que le
   Livre 20 chiffre en années, et **le Livre 23 a établi sur un cas réel ce que
   coûte une négociation multilatérale en cours.**
2. **Institution financière internationale adossée à des États actionnaires**,
   sur le modèle des banques de développement. **Capital appelé, gouvernance
   pondérée** — donc L20.C10 s'applique, et la question du vote revient.
3. **Fondation ou association de droit national.** **Rapide à constituer, et
   sans aucun argument** pour la qualité d'organisme public. **La jambe
   émetteur / banques centrales ne serait alors pas protégeable**, et
   L21.C06 § 5 dit ce que cela coûte.
4. **Filiale ou département d'une institution existante** — banque des
   règlements internationaux, institution multilatérale. **Hérite d'une
   personnalité et d'un réseau de comptes** ; **hérite aussi de sa gouvernance
   et de ses mandats**, ce qui est exactement ce que le dispositif cherche à
   contourner.

**CE QUE LA RÉPONSE COMMANDE, ET C'EST PLUS QUE L21.C06.** Elle décide **de la
protection du caractère définitif** ; **de la qualification de l'émetteur comme
infrastructure**, que L21.C01 tenait pour non établie et dont tout le chapitre
dépendait ; **de la capacité à ouvrir des comptes chez les banques centrales**,
dont L21.C03 a fait le pivot du circuit ; **et de l'application ou non des
régimes d'immunité**, que le corpus n'a jamais instruits.

**LE CORPUS N'EXPRIME PAS DE PRÉFÉRENCE.** Il constate que **les quatre formes
déplacent la difficulté plutôt qu'elles ne la suppriment** — vers la
ratification, vers la gouvernance pondérée, vers la perte de protection, ou vers
l'héritage d'un mandat étranger. **Et il enregistre que ne pas trancher revient
à laisser le Livre 20 et le Livre 21 raisonner sur un sujet indéterminé.**

## Règle de méthode — « LIRE LE CORPUS AVANT D'OUVRIR LA NORME »

**VERSÉE LE 2026-09-07 par L21.C07, à la clôture de la première tranche du
Livre 21, et elle naît d'une autocritique.**

**CE QUI S'EST PASSÉ.** Le Livre 21 a opposé le standard des infrastructures de
marché au dispositif **pendant quatre chapitres**, en supposant que son unité
circulait et devait être réglée. **La phrase qui renverse le livre était écrite
depuis le 2026-09-05, dans L11.C01 § 3** : « l'allocation ne circule jamais [...]
ce qui circule dans l'économie est de la monnaie nationale ordinaire,
indiscernable de toute autre ». **Elle n'a été prise au sérieux qu'au cinquième
chapitre.**

**LA RÈGLE.** *Avant d'opposer un standard externe au dispositif, établir ce que
l'architecture arbitrée exige réellement, et déclarer explicitement à quelle
branche l'objection s'applique. Une objection qui ne dit pas de quelle branche
elle parle n'est pas une objection : c'est un décor.*

**POURQUOI ELLE N'EST PAS UNE ÉVIDENCE.** Le corpus a plusieurs branches ouvertes
en permanence — A30 et ses quatre branches, A35, A36, et désormais A37. **Une
objection peut être juste sous une branche et sans objet sous une autre**, et le
défaut de mention fait passer la seconde pour la première. **C'est la faute
symétrique de celle que la revue contradictoire du 2026-09-07 a sanctionnée** :
non plus la sévérité hâtive, mais **la sévérité hors sujet**.

**CE QU'ELLE COÛTE, ET IL FAUT LE DIRE.** Elle allonge chaque chapitre d'une
déclaration de branche. **Le corpus la retient quand même, parce que la
constatation de L21.C05 lui a coûté quatre chapitres de portée mal déclarée.**

## Arbitrage A38 — L'ÉPARGNE RETRAITE EST-ELLE DE LA THÉSAURISATION ? Les deux réponses coûtent

**POSÉ LE 2026-09-07 par L22.C05, après ouverture de « Pension Markets in
Focus 2025 » de l'OCDE. ADRESSÉ À L'AUTEUR : c'est une décision de justice
distributive, et le corpus n'exprime pas de préférence.**

**CE QUI REND LA QUESTION INÉVITABLE MAINTENANT.** **L22.C02 § 5** a établi que
les deux instruments de reflux conçus par le corpus — prélèvement sur les
réserves, assiette de consommation finale — **n'atteignent pas les 51 % des
actifs financiers mondiaux détenus hors des banques**, et qu'un **troisième
instrument** serait nécessaire : un prélèvement sur les encours détenus hors du
système bancaire. **Sa plus grande assiette disponible est l'épargne
retraite** : **69 800 milliards de dollars dans l'OCDE à fin 2024**, plus 2 900
hors OCDE.

**LA QUESTION.** *Le demurrage vise à décourager la thésaurisation (L11.C07).
L'épargne retraite est une thésaurisation ORGANISÉE PAR LA LOI et VOULUE PAR LA
SOCIÉTÉ. Le dispositif la traite-t-il comme telle ?*

**PREMIÈRE BRANCHE — LA FRAPPER.** **L'instrument devient efficace** : assiette
la plus grande hors banques ; **concentrée à plus de 70 % en Amérique du Nord**,
donc corrigeant l'asymétrie géographique que L22.C02 § 4 reprochait aux deux
autres ; **et déjà mesurée, déclarée, auditée et publiée**, ce qui lève
l'obstacle d'identification. **LE PRIX** : plus des deux tiers des actifs sont
désormais dans des régimes **sans garant** — 31,9 % seulement à prestations
définies à fin 2024, contre 39,7 % dix ans plus tôt — **de sorte que la perte
est supportée directement par le futur retraité, sans aucun tampon.**

**SECONDE BRANCHE — L'EXEMPTER.** **Cohérent avec L11.C18**, qui borne les
exemptions par la nature essentielle du besoin couvert. **LE PRIX** :
**l'exemption vide l'instrument de sa partie la mieux mesurée et la plus facile
à atteindre**, ne laissant que celle qui pose précisément le problème
d'identification des détenteurs.

**TROISIÈME VOIE, INDIQUÉE ET NON INSTRUITE.** **Un seuil par personne** —
exemption en dessous, prélèvement au-dessus. C'est la structure de L11.C18
appliquée à un STOCK. **Elle demande la consolidation des encours par
détenteur**, dont le corpus tient déjà que l'obstacle n'est pas une interdiction
mais un appareil (correction du 2026-09-06, L23.C04).

**CE QUE L'AUTEUR A DÉJÀ DIT ET QUI ORIENTE.** **A35** décrit des fontes
« graduellement plus fortes » selon **l'impact de la consommation** — ce qui
vise le flux, non le stock, et **n'oriente donc pas cet arbitrage.** **L1.C15**
tient l'essentiel pour insolvable, et la retraite est un besoin essentiel — ce
qui oriente vers l'exemption.

**NE PAS TRANCHER A UN COÛT.** **Le Livre 25 ne peut pas écrire sa répartition
sans savoir si le dispositif prélève sur l'épargne retraite** ; **et F1 reste
ouvert dans sa formulation la plus dure** (L22.C02), puisque le seul instrument
capable de fermer la fuite est celui dont l'assiette est ici en question.

## Règle de méthode — « LE DROIT DONNE LES CATÉGORIES, PAS LES CHIFFRES »

**VERSÉE LE 2026-09-07 par L25.C05, après l'ouverture de quatre corps de règles
dans la même journée.**

**CE QUI L'ÉTABLIT.** **Le barème écologique en vigueur NE MESURE PAS la
régénération : il CERTIFIE UN PROCÉDÉ** — état initial documenté, plan
décennal, audit tiers, garantie de permanence, **aucun seuil chiffré** [L22.C04].
**Le noyau dur des droits économiques et sociaux N'EST PAS CHIFFRÉ : il se
CONSTATE** par privation observée, et se sanctionne par un renversement de la
charge de la preuve [L25.C02]. **Le cadre des limites planétaires N'AGRÈGE PAS :
il juxtapose neuf variables sans total, sans indice composite et sans
pondération** [L24.C01]. **Le droit climatique NE RÉPARTIT PAS : il DIFFÉRENCIE**,
par l'équité, les responsabilités communes mais différenciées et les capacités
respectives, **sans dire de combien** [L25.C05].

**LA RÈGLE.** *Sur la répartition d'un effort mondial entre souverainetés, le
droit fournit des CATÉGORIES, des PROCÉDURES et des CHARGES DE PREUVE ; il ne
fournit pas de nombres. Le corpus doit donc cesser d'espérer trouver dans un
texte le montant, le taux, la clé ou la pondération dont le dispositif a besoin,
et établir explicitement, chaque fois qu'il en produit un, QUE C'EST UNE
DÉCISION ET NON UNE LECTURE.*

**CE QUE LA RÈGLE NE DIT PAS, ET LA BORNE EST IMPORTANTE.** **Le droit chiffre
ailleurs, et le corpus en tient quatre exemples de la même journée** : un ratio
de levier de **3 %** [L21.C04], un plafond d'aide directe de **37,5 %** et une
enveloppe de **65 milliards d'euros** [L25.C04], des seuils de décarbonation
renvoyés à des actes délégués [L22.C06]. **La régularité vaut là où il faut
répartir entre États souverains un effort dont personne n'a la mesure ; elle ne
vaut pas pour le droit en général.**

**CONSÉQUENCE PRATIQUE POUR LA PASSE 2.** **Chaque fois qu'un chapitre avance un
nombre, il doit dire s'il le LIT dans une source ou s'il le DÉCIDE.** **Et
lorsqu'il le décide, il doit porter la mention que L24.C01 a déjà exigée pour la
clé d'agrégation : décision politique explicite, révisable et attaquable, qui ne
peut pas être présentée comme un fait scientifique.**


## Arbitrage A39 — À QUELLE FRONTIÈRE LE CORPUS CALCULE-T-IL UN RENDEMENT ÉNERGÉTIQUE ?

**POSÉ LE 2026-09-08 PAR L26.C03, APRÈS OUVERTURE DES DEUX HARMONISATIONS
MONDIALES PUBLIÉES DU RENDEMENT ÉNERGÉTIQUE NET.** **NON ARBITRÉ.**

**LE FAIT QUI OBLIGE À TRANCHER.** Deux équipes, disposant des mêmes
données, publient sur les mêmes technologies des rapports qui varient d'un
facteur voisin de quatre. **Murphy et al. 2022** : l'électricité hydraulique,
éolienne et photovoltaïque est « **all at or above 10** », les carburants
fossiles au point d'usage « **well below 10** », le pétrole plafonnant à
**8,7** quand bien même son rendement au puits vaudrait mille. **De Castro et
Capellán-Pérez 2020** : au périmètre du système entier, seule la
grande hydroélectricité dépasse six, l'éolien terrestre vaut **2,9**,
l'éolien en mer **2,3**, le photovoltaïque **1,8**, le solaire à
concentration **moins de 1** — et « **very likely, the global average EROIext
levels of variable RES are currently BELOW those of fossil fuel-fired
electricity** ».

**ET LE DÉSACCORD N'EST PAS EMPIRIQUE.** **Au périmètre standard, les deux
sources s'accordent** — « EROIst levels found fall within the respective
literature ranges ». **Le renversement vient entièrement d'une convention
déclarée** : « in this work we assume that the indirect investments of RES
represent **at least 100 %** of the total direct energy investments estimated ».
**Doubler le dénominateur divise le rapport par deux.** L'une ferme le
système au point d'usage, l'autre au niveau du système complet, et chacune
dit pourquoi.

**LA QUESTION POSÉE À L'AUTEUR.** *À quelle frontière le corpus
calcule-t-il un rendement énergétique lorsqu'il évalue la faisabilité
du dispositif ?*

**PROPOSITION DU CORPUS : LA FRONTIÈRE LA PLUS LARGE DISPONIBLE**, pour une
raison qui n'est pas physique mais logique. **Un dispositif d'émission finance
des investissements indirects — réseaux, stockage, remplacement — et ce
sont précisément ceux que le périmètre étroit exclut.** Évaluer un
instrument financier au périmètre qui exclut ce qu'il finance serait
incohérent. **CE CHOIX EST DÉFAVORABLE AU DISPOSITIF, ET C'EST UNE RAISON DE
PLUS DE LE FAIRE TRANCHER PLUTÔT QUE DE LE SUPPOSER.**

**CE QUE L'ARBITRAGE COMMANDE, QUEL QU'IL SOIT.** F11 est aujourd'hui
**indécidable** : déclenché sous une frontière, écarté sous l'autre.
**Un falsifieur indécidable est pire qu'un falsifieur défavorable, parce qu'il
n'interdit rien et n'autorise rien.** L'arbitrage de A39 est la seule chose qui
le remette au travail.

**ET IL COMMANDE AUSSI UNE DISCIPLINE D'ÉCRITURE, DÈS MAINTENANT ET SANS
ATTENDRE LA DÉCISION.** **Aucun chapitre ne peut citer un rendement
énergétique sans nommer la frontière à laquelle il est calculé**, et
**aucun ne peut comparer deux valeurs calculées à des frontières
différentes.**

## RÈGLE DE MÉTHODE — « LA PHYSIQUE DONNE DES CHIFFRES, PAS LA FRONTIÈRE »

**VERSÉE LE 2026-09-08 PAR L26.C03.** **Elle est le symétrique exact de la
règle versée la veille sur quatre corps de règles juridiques.**

**LA RÈGLE.** *Sur les grandeurs physiques dont le dispositif a besoin, la
science fournit des NOMBRES ; elle ne fournit pas la FRONTIÈRE du système
à laquelle ils sont calculés, et cette frontière décide du nombre. Le
corpus doit donc, chaque fois qu'il avance une grandeur physique, DÉCLARER LE
PÉRIMÈTRE, et ne jamais comparer deux grandeurs qui n'en partagent pas.*

**LES DEUX RÈGLES ENSEMBLE, ET C'EST LE RÉSULTAT LE PLUS GÊNANT DES DEUX
JOURNÉES.** **Le droit donne les catégories et pas les chiffres. La physique
donne les chiffres et pas les catégories.** **Le dispositif a besoin des deux
ensemble, et aucune discipline ne les lui fournit ensemble.** **Ce qui manque au
milieu n'est ni une acquisition ni une lecture : c'est une décision, et elle
n'appartient à aucune source.**


## PRÉCISION PROPOSÉE — `jevons_monetaire`, dont le vocabulaire appelle lui-même la confirmation

**PROPOSÉE LE 2026-09-08 PAR L26.C04. LE VOCABULAIRE N'EST PAS MODIFIÉ :
c'est une décision de l'auteur.** La définition en vigueur porte la mention
« nom provisoire (celui du livre), à confirmer en passe 2 ».

**CE QUE LE CHAPITRE APPORTE.** Le corpus tenait `effet_rebond` au vocabulaire
depuis L1.C03 et `jevons_monetaire` depuis L1.C12 **sans avoir jamais ouvert
l'argument qui les fonde**. La revue de référence est désormais ouverte :
trente-trois études, moyennes de **58 %** et **71 %** selon la famille de
méthodes, conclusion **« economy-wide rebound effects erode MORE THAN HALF of
the energy savings from improved energy efficiency »**.

**CE QU'ELLE NE FONDE PAS, ET C'EST L'ESSENTIEL.** **Cette littérature mesure
ce qui arrive quand un service énergétique devient MOINS CHER. Le dispositif
ne rend rien moins cher : il ÉMET.** **Le transfert de l'efficacité à
l'allocation est une inférence du corpus, pas une lecture.**
`jevons_monetaire` **reste une analogie.**

**LA PRÉCISION PROPOSÉE, QUI NE CHANGE NI LE NOM NI LA PORTÉE.** Le
mécanisme transférable est **l'effet de revenu**, et il prend sous le
dispositif une forme **plus défavorable que sous une politique d'efficacité,
pour une raison de comptabilité et non de degré** : sous l'efficacité, le
revenu dépensé est LIBÉRÉ par une économie physique déjà
réalisée et le rebond en REPREND une part ; **sous le dispositif, le pouvoir
d'achat est ÉMIS — il ne reprend rien, IL S'AJOUTE.** Énoncé
opératoire : **« une émission fléchée engendre une dépense NON
fléchée dont l'intensité matérielle est celle de l'économie
ordinaire »** — ce qui n'est pas l'argument quantitatif « plus de monnaie, plus
d'extraction » que la définition en vigueur écarte déjà explicitement.

**ET UNE LIMITE DE CONCEPTION QUI EN DÉCOULE, À VERSER OÙ L'AUTEUR
jugera.** **Un barème qualifie une activité financée ; il ne qualifie pas
la dépense de ceux qui reçoivent le paiement.** **Aucun instrument de
qualification n'atteint le second tour** : contre cet effet, le dispositif ne
dispose que d'instruments de NIVEAU — reflux et fonte — jamais d'instruments
de COMPOSITION.

**CE QUI MANQUE POUR TRANCHER : UN CHIFFRE.** Que la dépense induite reprenne
dix pour cent ou cent dix pour cent du gain **décide de tout**, et rien dans le
corpus ne permet de le dire. **Seul le simulateur du Livre 13 pourrait le
produire, et il n'existe pas.**


## A30 ET A37 — CE QUE LE PRÉCÉDENT OUVERT LE 2026-09-08 LEUR APPORTE

**L19.C02 a ouvert le traitement normatif du seul instrument mondial qu'une
institution internationale crée et alloue à ses participants sans
contrepartie préalable.** Ce qui suit ne tranche ni A30 ni A37 : **cela leur
fournit une pièce, et il faut dire exactement laquelle.**

**CE QUE CELA APPORTE À A30.** L'arbitrage restait bloquant sur un point non
juridique : *ce qui garantit la dette collective s'érode quand le dispositif
réussit*. **La norme statistique mondiale écrit depuis 2008 que la
créance porte « ON THE PARTICIPANTS COLLECTIVELY AND NOT ON THE IMF ».** **La
construction retenue par A35 — la société entière porte la dette —
est donc REPRÉSENTABLE, ce qui n'allait pas de soi et que rien n'établissait.**
**Elle n'est pas pour autant ÉPROUVÉE** : le système qui la porte n'a
jamais été soumis à l'érosion que A30 redoute. **Le point bloquant
reste bloquant ; il n'est plus isolé.**

**CE QUE CELA APPORTE À A37, ET C'EST PLUS LOURD.** A37 demande la forme
juridique de l'institution émettrice. **Ce précédent transforme cette
question en question DE MONTANT.** Sous le traitement ouvert, **l'émetteur
n'inscrit aucun passif et n'a donc pas de fonds propres négatifs** — ce qui
fait tomber l'objection que L21.C01 tenait pour acquise et que L11.C02 et
L21.C03 avaient établie. **Mais ce traitement suppose un émetteur d'avoirs
de réserve entre autorités monétaires**, et le dispositif verse à des
prestataires privés. **A37 ne décide donc plus seulement d'un régime de
protection : IL DÉCIDE SI LE DISPOSITIF A OU N'A PAS DE FONDS PROPRES
NÉGATIFS.** **C'est la question la plus coûteuse encore ouverte du corpus.**

**ET UNE QUESTION NOUVELLE EST POSÉE, QUI N'APPARTIENT À AUCUN ARBITRAGE
EXISTANT.** Le précédent fait payer l'USAGE et non la DÉTENTION : « SDRs
attract interest [...] as interest PAID BY participants holding MORE than their
allocation EXACTLY MATCHES the interest OWING TO participants holding LESS ».
**C'est la structure du reflux collectif, par l'autre face.** **Mais ici le
prélèvement est un TRANSFERT entre participants, tandis que la fonte
DÉTRUIT.** **Un transfert laisse l'encours inchangé ; une destruction le
réduit — et le corpus n'a jamais comparé les deux.** À verser où
l'auteur jugera : c'est une question de calibrage du reflux, pas de sa
légitimité.


## A30 — LE POINT BLOQUANT REÇOIT SON MÉCANISME LE 2026-09-08, ET IL EST SIMPLE

**A30 était débloqué sur le droit et sur la norme, et restait bloquant sur
un seul point, non juridique** : *ce qui garantit la dette collective s'érode
quand le dispositif réussit.* **Le corpus savait que quelque chose
s'érodait ; il ne savait pas quoi, ni par quel canal.** **L19.C05 le dit.**

**PREMIER PAS — UN DÉBITEUR COLLECTIF N'EXISTE PAS.** La norme définit
une unité institutionnelle comme « **an economic entity that is capable, IN
ITS OWN RIGHT, of owning assets, INCURRING LIABILITIES** » [§ 4.2], et exige
d'un passif qu'il oppose **deux unités nommées**. **« La société
entière » ne signe pas, ne paie pas, ne peut être ni poursuivie ni
libérée.** **Prise à la lettre, la formule de A35 ne désigne aucun
débiteur.**

**DEUXIÈME PAS — CE QUI SAUVE LA CONSTRUCTION.** Le précédent ouvert par
L19.C02 fait porter la créance « on the participants COLLECTIVELY », **et cela
fonctionne parce que chaque participant est lui-même une unité,
individuellement obligée pour sa propre part** : « interest PAID BY
participants holding MORE than their allocation exactly matches the interest
OWING TO participants holding LESS ». **Le « collectivement » est une
AGRÉGATION, pas une entité.** **Un débiteur collectif comme TOTALITÉ
n'est pas représentable ; comme SOMME DE DÉBITEURS IDENTIFIÉS, il l'est
parfaitement — et ce n'est pas une version affaiblie du premier, c'est autre
chose.**

**TROISIÈME PAS — LE CORPUS TENAIT DÉJÀ LA RÉPONSE.** L19.C03 a
établi qu'une fonte inscrite dans les termes est un **INTÉRÊT dû par le
détenteur**. **LE DÉBITEUR N'EST DONC PAS LA SOCIÉTÉ : C'EST LE
DÉTENTEUR, À PROPORTION DE CE QU'IL DÉTIENT.**

**ET L'ÉROSION SUIT IMMÉDIATEMENT.** **L'assiette qui garantit la dette est
l'encours détenu.** Or le dispositif vise à faire circuler la monnaie
plutôt qu'à la faire dormir — c'est la raison d'être du demurrage, que
L11.C07 justifie par l'objection de la thésaurisation. **Plus il réussit,
moins il y a d'encaisses oisives ; moins il y a d'encaisses, plus l'assiette est
étroite.** **CE QUI GARANTIT LA DETTE COLLECTIVE S'ÉRODE QUAND LE DISPOSITIF
RÉUSSIT PARCE QUE LA GARANTIE EST L'ENCOURS ET QUE LE SUCCÈS LE RÉDUIT.**

**CE QUE CELA CHANGE À L'ÉTAT DE A30, ET IL FAUT être précis.** **Le point
n'est pas levé : il est EXPLIQUÉ.** Une objection qui a un mécanisme est
attaquable — on peut mesurer l'élasticité, calibrer, compenser par l'autre
ressort. **Une objection sans mécanisme ne l'était pas.** **Ce qui manque
désormais est un chiffrage, et seul le simulateur du Livre 13 pourrait le
produire — il n'existe pas.**

**ET DEUX CONSÉQUENCES LATÉRALES, DONT UNE FAVORABLE.** **La répartition de
la charge ne suit aucun critère politique : elle suit la DÉTENTION** — le
Livre 25 cherchait une clé que le droit ne donne pas, et il en existe une que
personne n'a choisie. **Et qui ne détient rien ne doit rien** : la dette n'est
collective qu'en ce qu'aucun débiteur n'est désigné à l'avance, **nul
n'étant engagé sans avoir reçu.** **Le corpus ne l'avait pas
énoncé.**


## PRÉCISION DE LA RÈGLE « LE DROIT DONNE LES CATÉGORIES, PAS LES CHIFFRES » — versée le 2026-09-08 par L17.C04

**La règle versée le 2026-09-07 énonce que, sur la répartition d'un effort
mondial, le droit fournit des CATÉGORIES, des PROCÉDURES et des CHARGES DE
PREUVE, et pas de nombres.** **L17.C04 y ajoute une précision de même nature,
tirée d'un cas et non d'une série.**

**LA PRÉCISION.** *Quand le droit institutionnalise un objectif de long terme,
il oblige à S'EXPLIQUER, non à RÉUSSIR. La sanction du manquement n'est ni
la nullité de la décision ni une pénalité : c'est la publicité de la
raison.*

**LE CAS.** Une loi en vigueur depuis dix ans inscrit sept objectifs de
bien-être, dont la définition de la prospérité mentionne « **the limits of
the global environment** », crée un commissaire aux générations futures, des
indicateurs nationaux, un rapport de tendances longues et des examens de
l'auditeur général. **Son obligation centrale est que le corps public « must
act in a manner which SEEKS TO ENSURE » — obligation de moyens, écrite comme
telle.** **Et son unique obligation inconditionnelle est que « a public body MUST
PUBLISH its response [...] the response MUST INCLUDE THE BODY'S REASONS ».** Les
recommandations du commissaire se suivent « unless [...] **IT DECIDES ON AN
ALTERNATIVE COURSE OF ACTION** » — **une échappatoire sans aucune
condition.**

**CE QUE LA PRÉCISION N'EST PAS.** **Elle n'est pas une règle générale et
le corpus ne la pose pas comme telle : UN SEUL CAS EST OUVERT.** Elle demande
à être éprouvée sur les autres — Bonheur national brut,
Nouvelle-Zélande, Écosse, Islande — **dont aucun n'est ouvert.** **Et elle
n'établit pas que cette forme était la seule disponible** : qu'un
législateur ait choisi l'obligation de s'expliquer n'établit pas qu'il ne
pouvait pas choisir l'obligation de résultat. **Le corpus tient un choix, non
une nécessité.**

**CONSÉQUENCE PRATIQUE.** **Chaque fois que le corpus s'appuiera sur une
institution existante pour soutenir qu'un objectif est « porté par le droit
», il devra dire CE QUE LE MANQUEMENT COÛTE.** **Si la réponse est « une
explication publiée », l'appui existe et il est faible — et le dire n'est pas
dénigrer l'institution, c'est mesurer l'appui.**


## Arbitrage A40 — LE BARÈME AUX FRONTIÈRES OU LA RÉPONSE À L'OBJECTION DE FUITE : LE CORPUS NE PEUT PAS GARDER LES DEUX

**POSÉ LE 2026-09-08 PAR L16.C02, APRÈS OUVERTURE DU TEXTE DONT LE DISPOSITIF
TIRE SON SECOND RESSORT DE REFLUX. NON ARBITRÉ.**

**LE FAIT QUI OBLIGE À TRANCHER.** **L1.C10 porte depuis sa rédaction que
l'objection de fuite devant une monnaie fondante trouve sa réponse dans la
réforme foncière de l'auteur, « non traitée ici ».** L16.C02 l'a
traitée. **La réponse consiste à supprimer la terre comme objet de
propriété** — nationalisation intégrale, indemnisation totale, location
par enchères mondiales, rente redistribuée aux mères selon le nombre de
leurs jeunes enfants.

**ET LES DEUX RÉFORMES SONT INSÉPARABLES DANS LA CONCEPTION** : « **we
propose to introduce the money reform SIMULTANEOUSLY WITH THE NATIONALISATION OF
THE LAND** ». **La première finance la seconde — la baisse du taux
d'intérêt éteint la dette de nationalisation « in less than 20 years » —
et la seconde ferme le refuge que la première ouvrirait.**

**LA CONTRADICTION.** La même réforme énonce que « **no private individual,
NO STATE, no society may retain any kind of privileges over the land** », qu'« il
n'y a **NO RIGHTS OF NATIONS, NO PREROGATIVES OF SOVEREIGNTY** » sur la terre, et
que « **NO NATION HAS THE RIGHT TO ERECT BOUNDARIES AND TO LEVY IMPORT-DUTIES** »,
d'où « **UNIVERSAL FREE-TRADE and COMPLETE ELIMINATION OF ALL TARIFF
BOUNDARIES** ». **L11.C24 CONSTRUIT UN BARÈME AUX FRONTIÈRES.**

**LA QUESTION POSÉE À L'AUTEUR.** *Le corpus garde-t-il le barème aux
frontières, en assumant de n'avoir aucune réponse à l'objection de fuite ?
Ou prend-il la réponse, en abandonnant l'instrument que L11.C24 construit ?*

**CE QUE LE CORPUS PEUT DIRE, ET IL NE PEUT PAS DIRE PLUS.** **Il ne peut pas
garder les deux.** **Et il ne le savait pas** : L11.C24 a reçu trois
complications en trois jours — fongibilité de l'effet [L24.C04], fongibilité
du coût [L26.C03], existence d'un prix [L17.C05] — **et celle-ci n'est pas
une complication, c'est une INCOMPATIBILITÉ.**

**UNE TROISIÈME VOIE EXISTE PEUT-ÊTRE ET N'EST PAS INSTRUITE.** **La réponse
à la fuite pourrait être cherchée ailleurs que dans la réforme
foncière**, l'auteur de 1916 n'ayant pas connu les instruments de contrôle des
mouvements de capitaux ni les registres de bénéficiaires effectifs que le
corpus a rencontrés au Livre 23. **Mais cette voie n'est ouverte par personne,
et la seule réponse dont le corpus dispose aujourd'hui est celle-ci, avec son
prix.**

### A40 — LA TROISIÈME VOIE EXISTE, ELLE A ÉTÉ APPLIQUÉE, ET ELLE N'EST PAS GRATUITE (2026-09-08, quelques heures après la pose)

**L16.C03 a ouvert le rapport de première main sur la seule application que le
corpus connaisse.** **La fuite y était traitée SANS réforme foncière, PAR
UN PRIX DE SORTIE.**

**LE MÉCANISME, DANS LE TEXTE** : « **there was to be NO FINAL REDEMPTION ; but
every holder of the scrip was to have the privilege of redeeming it at the town
treasury or at the local banks AT ANY TIME ; but for such redemption A SERVICE
CHARGE OF TWO PER CENT had to be paid. As the stamp was only 1 per cent, the
disadvantages of redemption at 2 per cent were, at any given moment, GREATER than
the probable disadvantages of going on at 1 per cent. Redemption, therefore, was
not likely to hurt the circulation of the scrip** ».

**LA FUITE N'EST PAS EMPÊCHÉE : ELLE EST RENDUE PLUS CHÈRE QUE LE
SÉJOUR.** Sortir coûte deux ; rester coûte un. **Le porteur qui veut fuir le
peut à tout instant, et il n'y a aucun intérêt.**

**A40 A DONC TROIS BRANCHES ET NON DEUX.** **(1) Garder le barème aux
frontières et n'avoir aucune réponse à la fuite. (2) Prendre la réforme
foncière et perdre le barème. (3) TARIFER LA SORTIE AU-DESSUS DU COÛT DE
DÉTENTION**, ce qui ne demande ni nationalisation du sol ni abolition des droits
de douane.

**MAIS LA TROISIÈME N'EST PAS GRATUITE, ET SON PRIX TOUCHE LE POINT LE PLUS
INCERTAIN DU DOSSIER.** **Elle exige un GUICHET DE RACHAT** — donc que
l'émetteur détienne de quoi racheter. **La commune tenait un fonds de garantie
à la caisse d'épargne locale.** **Le Livre 19 a passé sept chapitres à
établir que l'actif de l'émetteur est le point le plus incertain du corpus** :
L11.C02 y porte « à l'actif, rien encore », L21.C03 a tranché en ce sens,
et L19.C06 a établi que trois registres distincts commandent la question.
**UN ÉMETTEUR SANS ACTIF NE PEUT PAS OFFRIR UN RACHAT.**

**CE QUE CELA CHANGE À L'ARBITRAGE.** **La troisième branche déplace la
question de la fuite vers la question de l'actif** — c'est-à-dire vers A37, qui
décide déjà de quatre autres choses. **Le corpus ne gagne donc pas une
sortie facile : il gagne une quatrième raison de trancher A37.**


## Arbitrage A41 — LE MOT « ENTROPIE » EST-IL ÉPROUVÉ OU MÉTAPHORIQUE ? Une source somme le corpus de choisir

**POSÉ LE 2026-09-08 PAR L26.C07, APRÈS OUVERTURE D'UNE CRITIQUE
INTERDISCIPLINAIRE ÉCRITE PAR UN THERMODYNAMICIEN ET UN ÉCONOMISTE.**
**NON ARBITRÉ.**

**LE FAIT QUI OBLIGE À TRANCHER.** La source conclut en cinq points
numérotés, dont deux visent directement l'usage que le corpus fait de ces
notions. **(iv)** les apports thermodynamiques au processus économique et
à la rareté des ressources sont « **simply ANALOGUES OR METAPHORS OF
REALITY** ». **(v)** ces apports « **should therefore be EMPIRICALLY TESTED
AGAINST THE REAL WORLD** ». Et la recommandation est explicite : « **a NEW
VOCABULARY for ecological economics is needed that STANDS ON ITS OWN ; one that
evolves a unique terminology, RATHER THAN CO-OPT THAT OF THERMODYNAMICS** »,
le vocabulaire emprunté pouvant « **MISLEAD AS MUCH AS ENLIGHTEN** »
hors des systèmes énergétiques.

**LE NOM TECHNIQUE DU DÉFAUT EXISTE, ET IL EST CITÉ PAR LA SOURCE.**
L'**entropie vulgaire** désigne « **the generic, but vague or ill-defined,
application of entropy to various kinds of disorder** ». **C'est l'emploi du
mot hors du domaine où il est défini.**

**CE QUE LE CORPUS FAIT AUJOURD'HUI.** Le concept `entropie` figure au
vocabulaire contrôlé et sert dans plusieurs livres à désigner une
dégradation qui **n'est mesurée en joules nulle part dans le corpus**. La
tranche du Livre 26 l'a confirmé en creux : elle tient des rapports et des
observations, **elle ne tient aucune quantité absolue**.

**LES DEUX BRANCHES, ET AUCUNE N'EST GRATUITE.**

**(1) ÉPROUVER.** Le corpus assume l'emploi au sens strict et produit, là
où il l'emploie, la mesure qui le justifie — un flux d'exergie, un
rendement, une quantité. **Prix : c'est un chantier de données que le
Livre 26 a déclaré ne pas avoir mené, et que seul le Livre 13
pourrait outiller. Il n'existe pas.**

**(2) DÉCLARER MÉTAPHORIQUE.** Le corpus applique au mot le patron des
métaphores restituables déjà prévu par la convention, et le
signale à chaque emploi. **Prix : le mot cesse alors de porter aucune
démonstration**, et tout passage qui s'appuyait sur lui pour conclure doit
être réécrit ou retiré. **C'est une migration à mener sur
plusieurs livres.**

**CE QUI N'EST PAS UNE BRANCHE.** Garder le mot au sens strict sans le mesurer.
**C'est l'état actuel, et c'est précisément ce que la source
nomme.**

**CE QUE L'AUTEUR A DÉJÀ DIT ET QUI ORIENTE.** La convention prévoit
déjà le patron `(*Image : ...*)` pour les métaphores restituables,
**ce qui rend la branche (2) techniquement disponible sans changement de
schéma**. Aucune décision antérieure ne porte sur ce mot.

---

## Règle de méthode versée le 2026-09-08 par L26.C07 — CE QU'UNE FILIATION AUTORISE

**Une filiation autorise à reprendre ce qu'un auteur a écrit. ELLE
N'AUTORISE JAMAIS À SE PRÉVALOIR DE SON AUTORITÉ POUR CE QU'IL N'A PAS
ÉCRIT, ET ENCORE MOINS POUR CE QU'IL A REFUSÉ.**

**La règle naît de deux constats de forme opposée, trouvés à
un jour d'intervalle dans deux traditions différentes.** **L16.C05** : le
corpus prend un instrument et **laisse la règle qui le gouvernait** — le
ressort de reflux sans la règle d'émission, la monnaie sans la terre.
**L26.C07** : le corpus prend un diagnostic et **ajoute un instrument que
l'auteur avait exclu** — le levier monétaire, quand le programme du
fondateur compte huit points dont aucun n'est monétaire et qu'il écarte
expressément le mécanisme de prix.

**Dans un cas le corpus retranche, dans l'autre il ajoute. Le défaut est le
même : LA FILIATION EST INVOQUÉE POUR HÉRITER DE PROPRIÉTÉS QUI
NE VIENNENT PAS AVEC ELLE.**

**Ce que la règle n'interdit pas.** Argumenter contre un auteur dont on
reprend le diagnostic est licite. **Ce qu'elle impose est de l'écrire ainsi**,
et non de présenter comme un héritage ce qui est une divergence.


---

## A39 — ARBITRÉ LE 2026-09-08 PAR L'AUTEUR, DANS LA FORME ET NON DANS LA VALEUR

**LA DÉCISION.** **Le corpus ne retiendra AUCUN COEFFICIENT UNIQUE.** Il
poursuivra avec **plusieurs frontières comparables — extraction, énergie
livrée, point d'usage et SERVICE FINAL —** en intégrant, là où les
données le permettent, **transformation, stockage, réseau, maintenance et
démantèlement**. **A39 et F11 NE POURRONT ÊTRE CLOS PAR UN COEFFICIENT
UNIQUE : il faudra une ANALYSE DE SENSIBILITÉ et LA PUBLICATION DES CONVENTIONS
DE CALCUL.**

**CE QUE CELA TRANCHE, ET CE QUE CELA NE TRANCHE PAS.** **Cela tranche la FORME
de la réponse** — une échelle et une plage, non un nombre. **Cela ne
tranche aucune valeur**, et n'en autorise aucune : le corpus reste sans chiffre
pour toute technologie.

**EXÉCUTÉ LE JOUR MÊME PAR L26.C08.** Le chapitre construit l'échelle
sur trois des quatre frontières demandées et **déclare que la
quatrième — le service final — n'est couverte par aucune source
ouverte**, faute d'une comptabilité en travail utile. **La source elle-même
fonde la décision** : « **it is unreasonable to expect to arrive at a SINGLE
VALUE (or a very tight range of estimates)** ». **Le refus du coefficient
unique n'est donc pas une prudence du corpus : c'est une propriété de la
grandeur.**

## A41 — ARBITRÉ LE 2026-09-08 PAR L'AUTEUR, LE JOUR MÊME DE SA POSITION

**LA RÈGLE, DANS LES TERMES DE L'AUTEUR.** Le terme « entropie » ne
pourra désormais apparaître **au sens physique** que si le passage
précise : **la grandeur effectivement étudiée ; son unité ou son
indicateur ; la frontière du système ; la méthode de mesure ou de calcul ;
le résultat empirique susceptible de réfuter l'affirmation.**

**À défaut, le terme devra être explicitement qualifié de
métaphore et NE POURRA SOUTENIR AUCUNE DÉDUCTION CAUSALE, INSTITUTIONNELLE
OU NORMATIVE.** **Les emplois qui ne sont ni mesurés ni déclarés
métaphoriques devront être SUPPRIMÉS OU REMPLACÉS** par des termes
autonomes : flux matériel, dissipation, exergie, énergie utile,
irréversibilité, dégradation, perte.

**PORTÉE RÉTROSPECTIVE, SANS RÉÉCRITURE IMMÉDIATE.** L'auteur
demande d'abord **la liste des passages concernés et leur classement**.

**EXÉCUTÉ LE JOUR MÊME.** L'inventaire est porté à
`protocoles/inventaire-entropie.md` : **73 occurrences dans 27 fichiers, classées
en six classes.** **RÉSULTAT PRINCIPAL : AUCUN EMPLOI NE SATISFAIT LES CINQ
CONDITIONS — le corpus n'a jamais mesuré une entropie.** **Mais SIX
occurrences seulement appellent une réécriture**, trente-deux étant des
mentions rapportées et neuf servant à BORNER une inférence plutôt
qu'à en tirer une.

**LES DEUX POINTS OÙ LA RÈGLE MORD, ET ILS SONT AU CENTRE.** **L1.C15** tire
une déduction institutionnelle non mesurée — « la création
monétaire est couplée à la production d'entropie » — et porte le
concept de tête `essentiel_insolvable` ; **sa proposition survit à la
réécriture et en sort vérifiable**, puisqu'elle portera sur des flux et
des stocks. **Et le quatrième fondement de F11 est « production d'entropie »**
— or **un fondement de falsifieur non mesurable ne falsifie rien**, et c'est
précisément là que la cinquième condition est obligatoire.

**PREMIÈRE APPLICATION FAITE.** Les conditions d'emploi sont portées dans
l'entrée `entropie` du vocabulaire contrôlé. **Le vocabulaire bloquant la
publication, la règle devient opposable à TOUT CHAPITRE FUTUR sans qu'aucun
chapitre existant soit touché.**


### A41 — PRÉCISÉ LE 2026-09-08, LE JOUR MÊME DE SON ARBITRAGE : LA RÈGLE ÉTAIT TROP LARGE

**CE QUI ÉTAIT MAL FORMULÉ.** L'entrée portée au vocabulaire exigeait
les cinq conditions **pour tout emploi au sens physique**. **Or l'inventaire
établi le même jour dispensait déjà, dans sa classe B, les
énoncés explicatifs ou de portée qui ne soutiennent aucune
déduction.** **Le vocabulaire était donc plus strict que l'inventaire qui
l'appliquait, et il aurait bloqué des passages que l'inventaire déclarait
licites** — dont celui de L1.C03 § 4 qui REFUSE à l'argument entropique le
pouvoir de trancher le découplage.

**LA RÈGLE CORRIGÉE.** **Les cinq conditions s'appliquent AUX SEULS EMPLOIS
QUI SERVENT UNE CONCLUSION causale, institutionnelle ou normative.** **Sont
dispensés** les énoncés explicatifs ou de portée qui ne soutiennent
aucune déduction — exposé d'un principe, restriction d'une inférence,
réfutation d'un argument — **ainsi que les mentions rapportant la position
d'un tiers.** **Ces emplois restent tenus de NOMMER LA FRONTIÈRE DU
SYSTÈME quand elle porte l'argument**, ce que deux passages de L1.C03 ne font
pas.

**CE QUE LA CORRECTION NE CHANGE PAS.** **Les six emplois de classe D restent
à réécrire**, et l'ordre de traitement est inchangé : l'entrée
de vocabulaire, puis le quatrième fondement de F11, puis L1.C15.
**L'inventaire des 73 occurrences n'est pas modifié : il était juste, et
c'est le vocabulaire qui débordait.**

---

## Correction du 2026-09-08 — TROIS CONCLUSIONS EXCESSIVES RETIRÉES DE L26.C09 ET L26.C10

**L'auteur a relu les deux chapitres le jour de leur rédaction et y a
identifié quatre excès de conclusion, tous dans le même sens : une
inférence tirée au-delà de ce que la source établissait.** **Ils
sont corrigés à l'endroit où ils se trouvaient, et non
dissimulés.**

**(1) L'ÉMISSION NE PRODUIT PAS MÉCANIQUEMENT DU PRODUIT INTÉRIEUR BRUT.**
L26.C10 concluait que le dispositif fabrique « par construction » le
découplage illusoire par financiarisation. **La norme statistique définit le
produit comme le résultat d'une PRODUCTION et range l'émission parmi les
TRANSACTIONS FINANCIÈRES, qui n'y entrent pas.** **La source parle de la
financiarisation de COMPOSANTES du produit, non de la création
monétaire.** **Conclusion retirée ; une DETTE COMPTABLE est versée au
Livre 19 à la place** — par quel agrégat, sous quelle rubrique, avec
quelle intensité physique associée.

**(2) AYRES ET WARD NE SE CONTREDISENT PAS.** L'un traite du recyclage d'un
**stock constant** avec apport d'exergie ; l'autre d'une **croissance permanente**
avec plancher d'intensité. **Les deux propositions peuvent être vraies
ensemble.** **Le corpus l'avait correctement compris dans L26.C01 avant de
reconstruire la contradiction dans L26.C10.** **Et le résultat vrai est plus
défavorable que la fausse controverse** : **le régime permanent est le seul état
qui satisfasse les deux propositions étudiées.** **Cela ne suffit pas à en faire la
seule possibilité réelle pour le dispositif** — le modèle de Ward est conditionnel à un
pays, un scénario, un plancher argumenté et une classe de ressources supposées non
substituables. **Ce qui est acquis est plus étroit : le corpus ne peut plus invoquer le
résultat de L26.C01 pour soutenir une croissance matérielle.**

**(3) LES DEUX CHIFFRES DE REBOND NE SONT PAS COMPARABLES.** « Au moins 10 % »
est une **borne inférieure** ; 58 % et 71 % sont des **moyennes** sur d'autres
périmètres. **Aucun facteur de révision n'en est déductible**, et
il n'y a pas « une même équipe » mais **un auteur commun**. **Ce qui
subsiste est une réserve d'indépendance.**

**(4) EXIGER DEUX TERMES PHYSIQUES SUPPRIME LE DÉCOUPLAGE ÉCONOMIQUE.**
Celui-ci se définit comme la relation entre une pression environnementale et
une **variable économique**. **Règle retenue à la place : publier
SIMULTANÉMENT la pression physique absolue, l'empreinte importée et le
ratio pression sur activité.**

**RÈGLE DE MÉTHODE QUI EN SORT, ET ELLE VAUT POUR TOUT LE CORPUS.**
**VÉRIFIER LA NATURE DES QUANTITÉS AVANT DE LES COMPARER** — une borne
n'est pas une moyenne, un plafond n'est pas une valeur, un périmètre n'est
pas un autre. **C'est la règle sur laquelle le corpus a fauté deux fois le
même jour, après avoir passé la journée à établir que les
conventions décident des chiffres.**


## Règle éditoriale versée le 2026-09-08 — OÙ VIT L'HISTORIQUE D'UNE CORRECTION

**LE CORPUS CANONIQUE EXPOSE L'ÉTAT CORRIGÉ, ET LUI SEUL. L'historique d'une
correction vit dans git et dans ce fichier.**

**LE MOTIF EST DANS LE § 10 DE LA CONVENTION.** Celui-ci pose qu'une IA
n'extrait que quelques passages et que **chacun doit tenir debout seul**. **Une
formulation fautive conservée dans un chapitre pour être aussitôt
rétractée ne tient PAS debout seule** : extraite hors de sa
rétractation, elle réactive l'affirmation fausse, et elle la réactive
avec l'autorité du corpus. **La chaîne « X, mais c'est faux » se
coupe toujours au « mais ».**

**LA DISTINCTION QUI COMMANDE, ET ELLE N'EST PAS UNE NUANCE.**

**(1) LA CORRECTION DE RÉDACTION SORT DU CHAPITRE.** Un brouillon a
écrit ce qu'une source n'établissait pas, et la phrase est remplacée
par l'énoncé juste. **Rien n'est perdu** : git porte le texte, ce fichier
porte le motif. **C'est le cas de L26.C08, C09 et C10 le 2026-09-08.**

**(2) LA RÉTRACTATION CONTRE UNE SOURCE RESTE DANS LE CHAPITRE.** Le corpus
avait AFFIRMÉ une proposition, une source ouverte l'a réfutée, et
**le fait que le corpus l'ait affirmée est lui-même un résultat** :
il dit ce que le dispositif tenait pour acquis sans l'avoir vérifié.
**C'est le cas de L1.C17 § 4 contre Ayres**, et cela ne se retire pas. **Un
corpus qui effacerait ses rétractations de fond cesserait d'être
contradictoire.**

**LE CRITÈRE PRATIQUE.** **L'erreur a-t-elle été tenue par le corpus, ou
seulement écrite dans un brouillon du jour ?** Tenue → elle reste, avec sa
réfutation. Écrite et corrigée avant d'avoir rien versé → elle
sort, et son motif vient ici.


## Forme structurelle nommée le 2026-09-08 — LE SUCCÈS ÉRODE SA PROPRE BASE

**Quatre occurrences indépendantes, trouvées dans quatre livres, sur quatre
grandeurs différentes. Ce n'est plus une coïncidence : c'est une propriété
de forme, et le corpus la nomme.**

**(1) A30, par L19.C05.** La base qui garantit la dette collective est l'encours
en circulation, **que le reflux réduit à mesure qu'il fonctionne.**

**(2) LE REFLUX TRANSACTIONNEL.** Son assiette est la transaction dommageable,
**qui disparaît si le dispositif réussit** — or les besoins
régénératifs, eux, ne disparaissent pas.

**(3) LA CONVENTION DE CONVERSION ÉLECTRIQUE, par L26.C08.** Le facteur qui
convertit l'électricité en énergie primaire dépend de la composition du
réseau. **Un barème calibré aujourd'hui devient faux à mesure que la
transition avance.**

**(4) L'INCITATION ELLE-MÊME, par L13.C01.** Dans le modèle stock-flux-fonds
ouvert, des dommages plus faibles donnent « **LESS INCENTIVES for the
materialisation of green investment projects** ». **Le succès réduit le
motif du succès**, et l'effet est produit à l'intérieur du modèle, non
ajouté après coup.

**L'ÉNONCÉ GÉNÉRAL.** **Un dispositif qui agit sur une grandeur dont il
dépend produit mécaniquement une boucle de ce type.** **Ce n'est pas un
défaut de conception : c'est une propriété de la classe d'instruments à
laquelle le dispositif appartient**, et les instruments fiscaux comportementaux
la connaissent déjà — une taxe qui réussit vide son assiette.

**CE QUE LE CORPUS N'A PAS, ET QUI EST LE MÊME DANS LES QUATRE CAS.** **AUCUN
MÉCANISME DE RECALIBRAGE.** **Ni règle de révision, ni périodicité,
ni autorité compétente pour la conduire, ni critère de déclenchement.**

**CE QUE CELA APPELLE, ET CE N'EST PAS UN ARBITRAGE DE PLUS.** **Une PIÈCE DE
CONCEPTION MANQUANTE**, à écrire une fois pour les quatre cas : **la règle
de recalibrage du dispositif.** **Elle relève du Livre 11 pour les barèmes et
du Livre 13 pour son épreuve**, et elle n'existe dans aucun des deux.


## Arbitrage A42 — QUE FAIT LE DISPOSITIF DE LA CIBLE 8.1 ? Le cadre qu'il prétend accélérer prescrit la croissance

**POSÉ LE 2026-09-08 PAR L12.C01, APRÈS OUVERTURE DU CADRE DES OBJECTIFS DE
DÉVELOPPEMENT DURABLE ET DE SON RAPPORT DE SUIVI.** **NON ARBITRÉ.**

**LE FAIT QUI OBLIGE À TRANCHER.** L'objectif 8 s'intitule « **Promouvoir une
croissance économique soutenue, partagée et durable** », et sa première
cible est chiffrée : « **un taux de croissance annuelle du produit
intérieur brut d'AU MOINS 7 % dans les pays les moins avancés** ». **Sa
quatrième cible demande l'inverse du même mouvement** : « s'attacher à
ce que **la croissance économique n'entraîne plus la dégradation de
l'environnement** ».

**ET LE DISPOSITIF SE RÉCLAME D'ACCÉLÉRER CE CADRE.**

**CE QUI REND LA QUESTION INÉVITABLE.** **L17.C03 a donné la première
description positive du dispositif** : il n'est pas une stratégie de
trajectoire, **il ENTREPREND DE RETIRER À LA CROISSANCE SA NÉCESSITÉ**. **La
cible 8.1 est précisément une inscription de cette nécessité dans un
texte adopté par les Nations unies.**

**LES TROIS POSITIONS, ET UNE SEULE EST INTENABLE.**

**(1) ACCÉLÉRER AUSSI 8.1.** Le dispositif finance alors de la croissance du
produit dans les pays les moins avancés. **C'est défendable** — le Livre 25
instruit les motifs de justice qui fondent cette cible — **mais cela contredit
la description de L17.C03**, et le corpus devrait alors réécrire ce qu'il
dit de lui-même.

**(2) L'ÉCARTER, ET LE DÉCLARER.** Le dispositif accélère le cadre en
en excluant une cible. **C'est également défendable** — un cadre s'amende
— **mais ce n'est plus « accélérer les ODD »**, et la revendication
doit être reformulée partout où elle figure.

**(3) NE RIEN DIRE. C'EST LA POSITION ACTUELLE, ET C'EST LA SEULE QUI SOIT
INTENABLE**, parce qu'elle laisse le corpus revendiquer une accélération
dont il n'a pas lu le contenu.

**CE QUE L'AUTEUR A DÉJÀ DIT ET QUI ORIENTE.** A32 a tranché en faveur de
l'énoncé du livre contre celui du Cahier lorsque les deux divergeaient.
**Ici, la divergence n'est pas interne au corpus : elle est entre le corpus et un
texte extérieur qu'il invoque.** **Aucune décision antérieure ne
s'applique.**

**UNE DIFFICULTÉ SUPPLÉMENTAIRE, ET ELLE N'EST PAS ARBITRABLE.** La cible
8.4 — que la croissance n'entraîne plus la dégradation — **est une cible
dont l'atteinte ne se constate pas avec les instruments que le corpus a
instruits** : la frontière décide du rendement énergétique [L26.C08],
la méthode décide du coefficient de rebond [L26.C09], la composition du champ
décide de ce qui est regardé [L26.C10]. **Quelle que soit la position
retenue sur 8.1, 8.4 restera non vérifiable.**


### A42 — ARBITRÉ LE 2026-09-08 PAR L'AUTEUR, LE JOUR MÊME DE SA POSITION

**LA DÉCISION.** **Le dispositif est en DÉSACCORD avec l'idée de
croissance, MÊME PRÉTENDUMENT VERTE.** Il n'accélère donc pas la cible
8.1, et il ne se contente pas de l'écarter : **il en conteste le principe.**

**C'EST LA BRANCHE (2), ET C'EST PLUS QUE LA BRANCHE (2).** L'arbitrage
proposé offrait d'écarter la cible en le déclarant. **L'auteur va au-delà
: le désaccord porte sur la croissance elle-même et non sur une cible.**

---

**CE QUI SUIT N'EST PAS LA DÉCISION DE L'AUTEUR MAIS CE QUE LE CORPUS EN
DÉRIVE.** Les trois conséquences ci-dessous sont des résultats de
lecture, et deux d'entre elles créent des dettes.

**PREMIÈRE CONSÉQUENCE — LA PORTÉE EXCÈDE LA CIBLE 8.1, ET IL FAUT LE
DIRE.** La cible **8.4** demande que « la croissance économique n'entraîne
plus la dégradation de l'environnement ». **C'est la définition même de
la croissance verte.** **Si le dispositif est en désaccord avec la croissance
verte, il conteste aussi la PRÉMISSE de 8.4**, et non seulement la cible 8.1.
**Ce n'est donc pas une cible qui sort du périmètre, c'est l'objectif 8 dans
son principe.** **Le corpus enregistre cette extension et la soumet à l'auteur
: elle découle de sa décision, elle n'y était pas énoncée.**

**DEUXIÈME CONSÉQUENCE — LE CORPUS PEUT ENFIN SE SITUER, ET C'EST UN
GAIN.** L17.C01 avait établi que **le dispositif n'entre dans aucune case de la
taxonomie du champ dont il se réclame** — ni croissance verte, ni
décroissance. **La décision le place**, et en deux temps. **Sur le
DIAGNOSTIC, il rejoint la décroissance** : la croissance, même verte, est
refusée. **Sur la MÉTHODE, il s'en sépare**, et L17.C03 avait déjà
dit comment — la sobriété demande aux États de renoncer à la
croissance, **le dispositif entreprend de retirer à la croissance sa
nécessité.** **Le corpus tient donc désormais une position localisable :
le diagnostic de la décroissance, sans sa méthode.** **L17.C01 est à
reprendre sur ce point.**

**TROISIÈME CONSÉQUENCE — UNE DETTE, ET C'EST LA PLUS DURE.** **La cible
8.1 vise LES PAYS LES MOINS AVANCÉS, et elle a des motifs de justice que le
Livre 25 instruit.** **Refuser un objectif de croissance pour les pays les plus
pauvres oblige à dire ce qu'on leur donne à la place.** **C'est l'objection
la plus sérieuse à la position retenue, et le corpus ne la tient pas.**
**COMMANDE AU LIVRE 25** : établir ce que le dispositif propose aux pays les
moins avancés en lieu et place d'une croissance du produit. **Tant que cette
commande n'est pas honorée, la position est tenable en principe et
indéfendable en pratique.**

**PORTÉE DE LA REFORMULATION, ET ELLE EST PLUS ÉTROITE QU'ON POUVAIT LE
CRAINDRE.** **La revendication n'est presque pas propagée dans le corpus** :
elle vit principalement **dans le titre même du matricule 12 — « Comment
réaliser les ODD avec NEMO IMS ? » — qui présuppose la réalisation et
non la contestation.** **Le registre étant la projection du plan directeur, LE
PLAN TRANCHE ET LE REGISTRE EST CORRIGÉ, JAMAIS L'INVERSE** (convention § 3)
: **le corpus signale la tension et ne touche pas au titre.** **La reformulation
porte donc sur les documents hors corpus — livre, cahier, site — que le
corpus ne peut pas modifier.**

---

### A37 — NON ARBITRÉ LE 2026-09-08, MAIS UNE ORIENTATION EST DONNÉE

**CE QUE L'AUTEUR A DIT.** La question reste à trancher. **L'institution
émettrice se situe au même niveau juridique que des institutions mondiales
telles que l'Organisation des Nations unies, l'Organisation mondiale du commerce
ou l'UNESCO.**

**CE QUE CELA RÈGLE : LE RANG.** Les trois institutions nommées sont des
**organisations internationales créées par traité**. **L'orientation
désigne donc la branche 1 sans la choisir formellement**, et elle écarte de
fait la branche 3 — fondation ou association de droit national — qui
n'offrait aucun argument pour la qualité d'organisme public.

**CE QUE CELA NE RÈGLE PAS, ET C'EST PRÉCISÉMENT CE QUE L21.C08 A RENDU
CRITIQUE : LA FORME FINANCIÈRE.** **Aucune des trois institutions nommées
n'est un émetteur.** Aucune ne crée de monnaie, aucune ne porte de passif
monétaire, aucune ne tient un bilan soumis à une exigence de fonds propres.
**L'analogie fixe le rang et laisse entière la nature.**

**ET LE CORPUS TIENT DÉJÀ UN MEILLEUR PRÉCÉDENT QUE LES TROIS NOMMÉS.**
L19.C02 a ouvert le cas des droits de tirage spéciaux : **une institution du
même rang, créée par traité, MAIS DOTÉE D'UNE FONCTION MONÉTAIRE**,
qui alloue sans contrepartie et dont la créance porte sur les participants
collectivement. **C'est l'analogue pertinent, et il porte un avertissement : son
passif n'a été reconnu qu'après quinze ans de non-reconnaissance.**

**UN POINT QUE L'ORIENTATION APPORTE SANS LE VOULOIR, ET IL EST DÉFAVORABLE.**
**On quitte l'UNESCO.** Des États l'ont fait, et y sont revenus. **Une
organisation créée par traité SE QUITTE** — or le corpus n'a **aucun
régime de retrait, de liquidation ni de succession**, et la norme des
infrastructures exige à tout moment de quoi assurer « **a recovery or orderly
wind-down of critical operations** » [L21.C08]. **L'orientation rend donc cette
lacune plus urgente, pas moins.**

**CE QUI RESTE À TRANCHER, PRÉCISÉMENT.** **Non plus le rang, mais quatre
choses** : la **fonction monétaire** — l'institution émet-elle en son nom
propre ou opère-t-elle pour le compte des banques centrales membres ; le
**capital** et son mode d'appel, que le principe 15 exige en fonds propres ; le
**régime d'adhésion et de retrait** ; et le **régime d'immunité**, que le
corpus n'a jamais instruit.

**ACQUISITION DE RANG 1 QUI EN DÉCOULE, ET ELLE EST PRÉCISE.** **Les statuts
d'une institution internationale DOTÉE D'UNE FONCTION MONÉTAIRE**, non ceux
d'une organisation technique. **Le corpus a déjà déclaré cette
acquisition sous un autre nom** — les statuts du Fonds monétaire
international figurent dans ses acquisitions de rang 1 depuis le 2026-09-07 et ne
sont toujours pas ouverts. **L'orientation de l'auteur en fait la plus rentable
des acquisitions ouvertes.**


### A42 — CORRECTION DE DOCTRINE DU 2026-09-08 : LA DÉRIVATION DU CORPUS ÉTAIT FAUSSE

**CE QUE LE CORPUS AVAIT DÉRIVÉ ET QUI EST RETIRÉ.** Il avait conclu que le
dispositif « rejoint la décroissance sur le diagnostic et s'en sépare sur
la méthode », et que la cible 8.1 était contestée dans son principe.
**Les deux étaient faux.**

**LA DOCTRINE, DANS LES TERMES DE L'AUTEUR.** **La position du dispositif est
celle d'une CROISSANCE ET D'UNE DÉCROISSANCE SÉLECTIVES.** Il ne poursuit ni
la croissance générale du produit intérieur brut ni sa diminution
générale. Il cherche **la croissance des activités nécessaires à
l'atteinte des besoins essentiels et du plancher social** ; **la décroissance
des activités qui provoquent les dépassements écologiques ou dont
l'utilité sociale ne justifie pas les dommages** ; **le maintien ou la
transformation des activités compatibles avec les deux bornes.** **La
sélection s'effectue par ACTIVITÉ, TERRITOIRE ET PÉRIODE.** **Le mouvement
du produit est un résultat possible de la transformation, pas son objectif.**
**Pour les pays les moins avancés, une croissance matérielle ciblée reste
possible et souvent nécessaire.**

**LE DÉFAUT ÉTAIT DANS LA QUESTION AVANT D'ÊTRE DANS LA RÉPONSE.** Les
trois branches proposées par l'arbitrage — accélérer 8.1, l'écarter,
se taire — **supposaient toutes que le rapport au produit agrégé soit
binaire.** **La position retenue est une quatrième, et elle n'était pas dans
l'énoncé.** **Un arbitrage dont aucune branche ne contient la réponse est
un arbitrage mal posé**, et le corpus l'enregistre à sa charge.

**CE QUE CELA CHANGE POUR LES DEUX CIBLES.** **LA FINALITÉ DE DÉVELOPPEMENT DES PAYS LES MOINS
AVANCÉS EST RETENUE ; LA PRESCRIPTION D'UN TAUX DE CROISSANCE AGRÉGÉ DU PRODUIT
INTÉRIEUR BRUT COMME CIBLE EST REJETÉE** — formulation arrêtée par l'auteur le
2026-09-08. **La formule antérieure — « 8.1 n'est pas contestée dans son CONTENU » —
était ambiguë : le contenu explicite de 8.1 EST la croissance agrégée et le seuil
de 7 %.** **Ce qui est retenu est la FIN ; ce qui est rejeté est le TAUX AGRÉGÉ
PRIS POUR CIBLE.** **Une croissance ciblée des capacités et services essentiels y
reste nécessaire, pouvant exiger localement et temporairement l'augmentation
de certains stocks et flux matériels.** **Et 8.4 CESSE D'ÊTRE SA VARIABLE
DE PILOTAGE DIRECTE, MAIS RESTE UN CRITÈRE DE VALIDATION EX POST DES EFFETS
PHYSIQUES AGRÉGÉS** — le dispositif ne pilote pas sur le couplage mais sur la
position d'une activité dans un couloir, **et il doit néanmoins être jugé sur le
couplage, un barème pouvant qualifier correctement chaque activité et échouer
globalement par addition, rebond ou déplacement.**

**CORRECTIONS DE L'AUTEUR DU 2026-09-08, VERSÉES À A42.** **(a)** la formule
« croissance matérielle ciblée » est remplacée ci-dessus : le débit matériel n'est
pas la finalité. **(b)** **LA SÉLECTIVITÉ N'EST PAS UNE FAMILLE SANS PRÉCÉDENT** —
la décroissance contemporaine préconise couramment la réduction des productions
destructrices et l'expansion des services essentiels, et certaines conceptions de
la croissance verte décrivent aussi une croissance sectorielle différenciée. **La
singularité éventuelle du dispositif est son MÉCANISME MONÉTAIRE, son COULOIR
social et écologique et son AUTORITÉ DE QUALIFICATION — non l'idée de
sélectionner.** **ACQUISITION : aucun chapitre n'a comparé ce mécanisme à ceux que
ces courants proposent.**

**LA COMMANDE AU LIVRE 25 SE RESSERRE ET DEVIENT PLUS DURE.** Elle ne porte plus
sur un substitut à la croissance — la doctrine y répond. **Elle porte sur
LE CRITÈRE DE SÉLECTION ET SON AUTORITÉ** : dans un pays dont les besoins
essentiels ne sont pas couverts, **décider quelles activités croissent et
lesquelles décroissent est une décision de répartition avant d'être une
décision technique.**

---

## Règle de méthode — DEUXIÈME OCCURRENCE DE « LIRE LE CORPUS AVANT D'OUVRIR LA NORME », SOUS UNE FORME NOUVELLE

**LA RÈGLE EXISTE DEPUIS LE 2026-09-07**, versée par L21.C07 : avant d'opposer
un standard externe au dispositif, établir ce que l'architecture arbitrée
exige réellement. **Elle vient d'être enfreinte une seconde fois, autrement.**

**CE QUI S'EST PASSÉ.** Pour situer le dispositif, le corpus est allé chercher
une case dans la taxonomie d'une littérature externe — croissance verte,
décroissance — **et il a conclu que le dispositif rejoignait l'une d'elles.**
**Or la position était écrite dans le corpus depuis L1.C04** : `plancher_social`
et `plafond_ecologique` figurent au vocabulaire contrôlé depuis ce chapitre,
**et le couloir qu'ils définissent EST la position.**

**LA RÈGLE S'ÉTEND DONC.** *Avant de situer le dispositif dans une taxonomie
externe, établir ce que le corpus dit déjà de lui-même.* **Ce n'est pas
la taxonomie qui manquait d'une case pour le dispositif : c'est le corpus qui
avait la sienne et ne l'a pas relue.**

**CE QUE CELA CONFIRME SUR L'APPAREIL.** L14.C01 a établi que **le contrôle
détecte l'absence et reste aveugle à l'excès**. **Voici un troisième
type d'erreur qu'il ne voit pas non plus : la redécouverte fautive d'une chose
déjà établie ailleurs dans le corpus.** **Aucun mécanisme ne relie un
chapitre neuf aux acquis des chapitres anciens sur le même objet**, sinon la
mémoire du rédacteur — et c'est à verser à la grille du Livre 14.


## RÉVISION DE FOND À FAIRE — L19.C05, établie le 2026-09-08 par L19.C09

**Ce n'est pas une correction à propager mais un chapitre à réécrire, et le
motif est inhabituel : LE CHAPITRE A RAISON ET N'A PLUS D'OBJET.**

**L19.C05 établit qu'un collectif n'est pas une unité institutionnelle, et donc
qu'un créancier collectif doit se résoudre en unités identifiées.** Il
travaillait sur la formule de l'édition 2008 du *System of National Accounts*,
qui faisait des droits de tirage spéciaux une « **claim on the participants
collectively and not on the IMF** ».

**LA RÉVISION 2025 A OPÉRÉ ELLE-MÊME CETTE RÉSOLUTION** : elle écrit
désormais un droit d'obtenir des avoirs de réserve « **from other IMF
members** ». **Le raisonnement du chapitre est donc CONFIRMÉ par la rédaction
du normalisateur — et sa MATIÈRE a disparu de la norme en vigueur.**

**CE QUE LA RÉVISION DE FOND DOIT FAIRE.** Réécrire le chapitre sur la norme
EN VIGUEUR, et traiter la formule de 2008 comme **un état antérieur dont la
correction confirme l'analyse** — ce qui est un appui plus fort que celui dont
le chapitre disposait, non plus faible. **Porter aussi l'assouplissement de la
définition de l'unité institutionnelle**, qui joue en sens inverse et doit être
déclaré comme tel : « incurring liabilities » (§ 4.2, 2008) devient
« **typically able to incur liabilities** » (§ 5.2, 2025). **Le résultat
principal tient néanmoins, car il repose sur « in its own right », maintenu
intact.**

**CONSÉQUENCE POUR L19.C02, À TRAITER DANS LA MÊME PASSE.** Son titre — « le
seul précédent et le passif reconnu **en 2008** » — est dépassé :
**le passif n'est plus daté de 2008, il est en vigueur, et la révision en donne
désormais le MOTIF** (obligation de remboursement conditionnelle, intérêt qui
court). **Le précédent est donc renforcé quant au passif et dissous quant au
créancier collectif** — et c'est le second trait qui le rendait analogue au
dispositif.


## A39 — la quatrième frontière est ouverte le 2026-09-08, et l'écart est d'un ordre de grandeur

**L'AUTEUR A POSÉ QUE A39 ET F11 NE POURRAIENT ÊTRE CLOS PAR UN COEFFICIENT
UNIQUE, ET QU'IL FAUDRAIT UNE ANALYSE DE SENSIBILITÉ ET LA PUBLICATION DES
CONVENTIONS DE CALCUL. LA QUATRIÈME FRONTIÈRE CONFIRME CETTE EXIGENCE ET LA
CHIFFRE.**

**ÉTAT DES QUATRE FRONTIÈRES DEMANDÉES.**

- **Extraction** — couverte (L26.C08) : taux de retour énergétique maximal en
  supposant l'extraction infinie, pétrole 8,7, gaz 5,6, charbon 10, éthanol de
  maïs 1,6, granulés de bois 1,6.
- **Énergie livrée** — couverte (L26.C08) : gaz de schiste passant de 83 à 5,2 ;
  copeaux 32 contre granulés 1,6 ; facteurs de conversion 0,3 et 0,7.
- **Point d'usage** — couverte (L26.C08), et c'est là que les deux sources
  s'arrêtaient.
- **SERVICE FINAL** — **OUVERTE LE 2026-09-08 PAR L26.C11** : rendement
  exergétique agrégé national de **11 % à 15 %** dans trois pays.

**CE QUE CELA ÉTABLIT POUR L'ARBITRAGE : L'ÉCART ENTRE LA PREMIÈRE ET LA
QUATRIÈME FRONTIÈRE EST D'UN ORDRE DE GRANDEUR.** **Un barème adossé à « un »
rendement énergétique ne dit rien tant qu'il n'a pas dit À QUELLE FRONTIÈRE il se
place.**

**CE QUI RESTE INTERDIT, ET LE CORPUS S'EST INTERDIT DE LE FAIRE.** **Les quatre
frontières NE SE COMPOSENT PAS PAR MULTIPLICATION** : elles ne portent ni sur les
mêmes périmètres, ni sur les mêmes années, ni sur les mêmes pays, ni sur les
mêmes vecteurs, et certaines se recouvrent partiellement. **Une chaîne composée
serait une construction du corpus, non un résultat de source — et elle serait
exactement le coefficient unique que l'arbitrage refuse.**

**ACQUISITION QUE L'ARBITRAGE APPELLE DÉSORMAIS : une étude qui compose
explicitement plusieurs frontières SUR UN PÉRIMÈTRE UNIQUE**, ou à défaut la
déclaration que le corpus n'en dispose pas et que la sensibilité ne peut donc
pas être calculée sur une chaîne complète.

**ET UN FAIT NOUVEAU QUE A39 DOIT PORTER : LA DILUTION D'EFFICACITÉ.** Le
rendement agrégé d'un pays peut stagner **alors que chaque appareil s'améliore**,
par déplacement de la composition des usages. **Un barème calibré sur des
rendements d'appareils dériverait donc du résultat national sans qu'aucun de ses
paramètres ne soit faux.** **C'est un mode de décalibrage que l'arbitrage n'avait
pas envisagé, et il est structurel, non comportemental.**

**RESTENT NON COUVERTS, ET L26.C08 LES AVAIT DÉJÀ DÉCLARÉS :** transformation en
partie seulement, **stockage** — poste décisif puisque l'intermittence le
commande —, réseau, maintenance, **démantelèment**. **Aucune valeur n'est retenue
pour aucune technologie.**


## A37 — le précédent le plus proche est trouvé le 2026-09-08, et il s'arrête où le dispositif commence

**L18.C12 a établi ce que sont EN PRATIQUE les paiements pour services
écosystémiques**, c'est-à-dire la famille d'instruments la plus proche du
dispositif : « the **vast majority** [...] are **run by states** under public
regulation frameworks. Funds are typically **collected through taxes** and the
level of payments is **politically set**, mainly based on **opportunity costs** or
negotiations with concerned stakeholders. » Beaucoup fonctionnent comme des
« green rural subsidies ».

**TROIS CONSÉQUENCES POUR L'ARBITRAGE, ET ELLES NE VONT PAS DANS LE MÊME SENS.**

**(1) FAVORABLE.** La famille la plus proche n'est **pas un marché** mais une
allocation publique à prix administré. **Le dispositif n'est donc pas une
anomalie dans son genre**, et l'objection « c'est du marché » ne tient pas
d'office — y compris lorsqu'elle vient de la critique écologique, dont ce texte
rapporte qu'elle est contestée sur ce point par d'autres chercheurs.

**(2) DÉFAVORABLE, SUR LE CRITÈRE.** Ces dispositifs fixent leur niveau
**politiquement, principalement sur le COÛT D'OPPORTUNITÉ** — ce que le
bénéficiaire renonce à gagner, **non ce que la nature vaut**. C'est la réponse
empirique à la question que L25.C01 tient ouverte, **et elle n'est pas
écologique**.

**(3) ET C'EST CELLE QUI ISOLE LE DISPOSITIF.** Les paiements existants sont
financés **PAR L'IMPÔT**. **Le dispositif ne l'est pas : il alloue une unité
émise.** **LE PRÉCÉDENT LE PLUS PROCHE S'ARRÊTE DONC EXACTEMENT LÀ OÙ COMMENCE
CE QUE LE DISPOSITIF A DE PROPRE.** A37 gagne un analogue pour la FONCTION et
n'en gagne aucun pour la FORME DE L'ÉMISSION — ce qui laisse entières les
questions de forme financière, de capital, d'adhésion et de retrait, et
d'immunité.


## A39 — la dispersion de méthode est chiffrée le 2026-09-08, et elle vaut UN FACTEUR DEUX À FRONTIÈRE ÉGALE

**L'AUTEUR A EXIGÉ UNE ANALYSE DE SENSIBILITÉ ET LA PUBLICATION DES CONVENTIONS DE
CALCUL. L26.C12 MONTRE QUE CE N'EST PAS UNE PRÉCAUTION DE MÉTHODE : C'EST LA SEULE
CHOSE QUI REND LES CHIFFRES COMPARABLES.**

**LE FAIT.** À frontière **égale** — le rendement exergétique agrégé d'une
économie nationale — les estimations publiées du rendement **des États-Unis en
1970** valent **22 %** chez un auteur et **11 %** chez un autre. **Du simple au
double, même pays, même année, même grandeur.** Autres écarts documentés :
États-Unis 1960, 8 % contre 11 % ; États-Unis 2010, 14 % contre 11 %.

**ET LES MOTIFS SONT DES CONVENTIONS, NON DES DÉSACCORDS EMPIRIQUES.** Apport
alimentaire attribué au travail musculaire (dont le rendement est d'environ 2 %) ;
rendements retenus pour les véhicules (22 % contre 13 %) ; température de service
de la chaleur industrielle (20 % contre 10 %) ; allocation entre chaleur haute et
basse température. **ET SURTOUT, UNE CONVENTION QUI COUVRE À ELLE SEULE UN FACTEUR
D'ENVIRON DIX : le facteur de conversion des renouvelables, pris entre 0,07 et 0,13
par les analyses exergétiques et ÉGAL À 1,00 par l'Agence internationale de
l'énergie.**

**LA RÈGLE QUE A39 DOIT PORTER, ET ELLE EST PLUS EXIGEANTE QUE CE QUI ÉTAIT
INSCRIT.** Publier le chiffre ne suffit pas. **Publier la frontière NE SUFFIT PAS
NON PLUS.** Il faut publier :
1. **les facteurs de conversion PAR VECTEUR** — celui des renouvelables suffisant
   à lui seul à déplacer le résultat d'un ordre de grandeur ;
2. **l'allocation retenue entre classes d'usage** — chaleur, force motrice,
   travail musculaire, électricité ;
3. **les rendements par tâche**, et non le seul agrégé.

**Deux barèmes qui déclareraient la même frontière et le même indicateur
pourraient encore différer DU SIMPLE AU DOUBLE.**

**ET UN PIÈGE DE LECTURE QUE A39 DOIT NOMMER : L'ACCORD SUR LE TOTAL PEUT MASQUER
LE DÉSACCORD SUR TOUTES LES COMPOSANTES.** Deux études s'accordent sur le
rendement britannique de 2000 **par COMPENSATION** : chaleur 12 % contre 17 % et
électricité 14 % contre 20 % d'un côté, force motrice 19 % contre 14 % et moindre
allocation au travail musculaire de l'autre. **Un corpus qui ne lirait que les
totaux publiés conclurait à un consensus qui n'existe pas.**

**ET UN FAIT SUR LA TRAÇABILITÉ, QUI VAUT AVERTISSEMENT.** Une même équipe donne
pour le Royaume-Uni de 1960 une valeur de **10 %** dans une publication et de
**8 %** dans une publication ultérieure, et la source qui le rapporte écrit que
« **the reasons for differences to their later results cannot be determined** ».
**Une valeur publiée peut changer d'un tiers sans que le motif soit reconstituable
par un lecteur attentif.**


## La pièce de conception manquante — MOITIÉ FAITE LE 2026-09-08 PAR L11.C30

**LA PASSE 2 AVAIT DÉCLARÉ : « une PIÈCE DE CONCEPTION MANQUANTE, à écrire une
fois pour les quatre cas : la règle de recalibrage du dispositif. »** **Elle est
structurée, elle n'est pas écrite — et le premier résultat est qu'IL EN FAUT
TROIS, NON UNE.**

**LES CAS SONT SIX, ET NON QUATRE.** Aux quatre déjà tenus s'ajoutent **la
DILUTION D'EFFICACITÉ** (L26.C11, L26.C12) et **le DÉPLACEMENT DES MOTIVATIONS**
(L18.C12 corrigé par L18.C15).

**TROIS TYPES, ET LE RANGEMENT CHANGE LE REMÈDE.**
- **TYPE A — ÉROSION D'ASSIETTE** (encours garantissant la dette ; assiette du
  reflux). **Sens connu, grandeur observable dans les comptes du dispositif.**
  **Remède : une règle de révision avec seuil et périodicité.** Cas déjà traité
  ailleurs par les instruments fiscaux comportementaux.
- **TYPE B — DÉRIVE DE CONVENTION** (conversion électrique ; dilution
  d'efficacité). **Le coefficient ne s'use pas : il mesure correctement une
  réalité qui n'est plus la même. Sens variable, grandeur observable de
  l'extérieur.** **A39 impose déjà de PUBLIER la convention ; RIEN N'IMPOSE DE LA
  REFAIRE, ni ne dit quand.** **C'est le manque le plus facile à combler.**
- **TYPE C — RÉPONSE À L'INSTRUMENT** (incitation à investir ; déplacement des
  motivations). **Ni le sens ni l'ampleur ne sont connus à l'avance.** **AUCUNE
  RÈGLE DE CALIBRAGE PRÉALABLE NE PEUT LE COUVRIR.** **Il appelle un DISPOSITIF
  DE MESURE EX POST et une capacité d'arrêt, que le corpus n'a pas.**

**CE QUE CHAQUE RÈGLE DOIT CONTENIR, ET LE CINQUIÈME POINT EST UN ARBITRAGE DE
L'AUTEUR.** (1) un critère de déclenchement chiffré — sans seuil, la révision est
discrétionnaire ; (2) une périodicité minimale indépendante du seuil ; (3) une
autorité compétente **distincte de celle qui émet** ; (4) la publication de
l'ancienne convention, de la nouvelle **et du motif** ; **(5) LE SORT DES
ENGAGEMENTS PRIS SOUS L'ANCIEN CALIBRAGE.**

**LE CINQUIÈME EST UNE QUESTION DE DROITS, NON DE TECHNIQUE, ET LE CORPUS NE L'A
PAS TRANCHÉE.** Trois branches, exclusives : **rétroactivité** (cohérent,
imprévisible pour ceux qui s'engagent) ; **non-rétroactivité** (prévisible,
accumule des positions calibrées sur des conventions périmées) ; **extinction
progressive** (praticable, exige une comptabilité par millésime que rien dans
l'architecture arbitrée ne prévoit). **À ARBITRER.**

**ACQUISITION DE RANG 1 QUE CETTE PIÈCE APPELLE, ET ELLE EST DOCUMENTÉE :** la
révision des **tarifs d'achat de l'électricité renouvelable** en Europe, et **ce
qu'il est advenu des engagements pris sous l'ancien tarif** — parfois tranché
devant les tribunaux. **C'est le précédent le plus proche du cinquième point.**

**À SOUMETTRE À L'AUDIT CONTRADICTOIRE EN POSANT LA QUESTION EXPLICITEMENT : la
typologie en trois types tient-elle ?** Le rangement de la dilution d'efficacité
est contestable — elle se lirait comme un type A si l'on tenait le rendement
lui-même pour l'assiette.


## A37 — l'analogue financier est ouvert le 2026-09-08, et il répond aux quatre traits laissés ouverts

**L'AUTEUR AVAIT DONNÉ LE RANG INSTITUTIONNEL ET LAISSÉ OUVERTS LA FORME
FINANCIÈRE, LE CAPITAL, L'ADHÉSION ET LE RETRAIT, ET L'IMMUNITÉ.** **Les statuts
du Fonds monétaire international sont ouverts** (L20.C24), obtenus par le Recueil
des traités des Nations unies après refus du site de l'institution.

**RÉSERVE PRÉALABLE, ET ELLE COMMANDE TOUT CE QUI SUIT : LE TEXTE LU EST CELUI DE
1945, NON LE TEXTE EN VIGUEUR.** Test refaisable : **l'expression « special
drawing » n'y apparaît pas une seule fois.** **Aucune disposition ci-dessous n'est
le droit actuel avant collationnement.**

**COMPOSITION.** « Membership shall be open to **the governments** of other
countries [...] in accordance with such terms **as may be prescribed by the
Fund** ». **L'adhérent est un gouvernement, et l'institution fixe elle-même les
conditions d'admission.**

**CAPITAL.** « The **subscription of each member shall be EQUAL TO ITS QUOTA** and
shall be **PAID IN FULL** ». **L'institution est dotée par ses membres.** **Le
dispositif propose d'émettre sans contrepartie souscrite : le précédent le plus
proche fonctionne à l'inverse**, et c'est la **seconde** occurrence de cette
exigence après L21.C08 (fonds propres exigés par la norme des infrastructures).

**IMMUNITÉS.** Personnalité juridique pleine ; immunité de **toute forme de
procédure judiciaire** sauf renonciation expresse ; immunité contre saisie par
action exécutive ou législative ; archives inviolables ; **immunité de toute
taxation** ; et avoirs « **free from restrictions, regulations, controls and
moratoria OF ANY NATURE** ». **Ce régime s'obtient PAR TRAITÉ, non par
déclaration.** **Et il faut en voir le coût : une institution ainsi immunisée
n'est pas contrôlable par les moyens ordinaires** — ce que L7.C22 tient déjà
comme la difficulté centrale.

**RETRAIT, ET C'EST LE RÉSULTAT LE PLUS LOURD.** « **Any member may withdraw from
the Fund AT ANY TIME** by transmitting a notice in writing [...] **Withdrawal shall
become effective ON THE DATE SUCH NOTICE IS RECEIVED.** » **Ni préavis, ni délai,
ni condition.** **UN REFLUX COLLECTIF ADOSSÉ À UNE APPARTENANCE DONT LA SORTIE EST
IMMÉDIATE N'EST PAS OPPOSABLE À CELUI QUI SORT.** À rapprocher de L19.C05 et de
L19.C09.

**ACQUISITIONS QUE CE CHAPITRE INSCRIT.** **(1) LE TEXTE CONSOLIDÉ EN VIGUEUR et
la liste datée des amendements** — rang 1, sans quoi rien de ce qui précède n'est
citable comme droit actuel. **(2) LES STATUTS DE LA BANQUE INTERNATIONALE POUR LA
RECONSTRUCTION ET LE DÉVELOPPEMENT**, dans le MÊME volume et sous le MÊME numéro
d'enregistrement, **non lus** — or **c'est l'institution qui ÉMET DES TITRES**, là
où le Fonds gère des quotes-parts, **et elle pourrait être un analogue plus proche
du dispositif que le Fonds lui-même.** **(3) L'accord de relation avec les Nations
unies et les conventions générales sur les privilèges et immunités**, qui
complètent le régime de l'article IX.


## A37 — CORRECTION JURIDIQUE DE L'AUTEUR, 2026-09-08 : LA SECTION PORTE LE RÉGIME

**CECI EST L'HISTORIQUE D'UNE CORRECTION DE RÉDACTION**, au sens du cas (1) de la
règle « Où vit l'historique d'une correction » versée le même jour. **Le chapitre
L20.C24 expose l'état corrigé et lui seul ; le motif est ici.**

**CE QUI S'EST PASSÉ.** L'article VI des statuts de la Banque internationale pour
la reconstruction et le développement a été ouvert et lu en entier le 2026-09-08,
dans sa version portant la mention « as amended effective June 27, 2012 ». **Le
chapitre en a tiré trois conclusions, dont deux que le texte ne porte pas.**

**PREMIÈRE ERREUR — LA RÉTENTION.** Le chapitre a présenté la section 4 (c) (i)
comme « une garantie de fait » de la part appelable. **Le texte dit l'inverse** :
*« No amount shall be withheld on account of the liability of the government
resulting from its subscription for shares under Article II, Section 5 (ii). »*
**La rétention garantit la dette du sortant COMME EMPRUNTEUR OU GARANT, et le
traité en exclut expressément la responsabilité de souscription.** Le délai de six
mois de la même section est une disposition distincte, qui porte sur le paiement
des parts et joue *« in any event »* — **ce n'est pas une sûreté.**

**SECONDE ERREUR — LE DOMAINE DE LA SECTION 5 (c).** Le chapitre a versé au régime
du retrait la disposition selon laquelle la responsabilité des membres pour les
souscriptions non appelées se prolonge jusqu'à extinction de toutes les créances.
**Cette disposition est dans la SECTION 5, qui traite de la SUSPENSION PERMANENTE
DES OPÉRATIONS DE LA BANQUE.** Elle n'atteint un sortant que par la section 4 (d),
et seulement si la Banque suspend définitivement ses opérations **dans les six
mois** de sa sortie.

**FORMULES RETIRÉES.** « Le texte le dit trois fois » et « une survivance de
responsabilité assortie d'une rétention et d'un délai ». **Elles additionnaient
comme trois confirmations d'une même règle ce que le traité distingue en
mécanismes de portées différentes.**

**RÈGLE DE MÉTHODE VERSÉE — LA SECTION PORTE LE RÉGIME.** Le corpus s'était donné
le 2026-09-08 la règle de lire **tous les instruments d'un même volume** avant de
conclure, puis celle de lire **l'article entier**. **Aucune des deux ne suffit.**
**Une disposition tient son domaine de la SECTION qui la porte**, et deux
dispositions voisines par leur objet peuvent relever de régimes qui ne se
rencontrent pas. **À vérifier avant toute citation d'un instrument conventionnel.**

**CE QUI RESTE ACQUIS, ET C'EST UNE CONTRAINTE DE CONCEPTION.** Le capital
appelable survit au retrait [section 4 (c) (iv)], **borné à l'état constaté à la
date où le prix de rachat des parts est arrêté**, et **sans sûreté** — le traité
garantit la dette d'emprunteur dans la même phrase où il refuse de garantir
celle-là. **Le seul précédent que le corpus tienne d'un engagement de capital
survivant à la sortie est donc un engagement NON GAGÉ.** Un reflux adossé à une
appartenance ne peut pas compter sur une sûreté que le modèle le plus proche a
refusé d'organiser.

**CORRECTION D'UNE ENTRÉE ANTÉRIEURE DE CE FICHIER.** La section « A37 — le
précédent le plus proche est trouvé le 2026-09-08 » se termine sur la phrase
suivante : « UN REFLUX COLLECTIF ADOSSÉ À UNE APPARTENANCE DONT LA SORTIE EST
IMMÉDIATE N'EST PAS OPPOSABLE À CELUI QUI SORT. » **CETTE CONCLUSION EST RETIRÉE
DEPUIS LE 2026-09-08** : elle était tirée du texte de 1945 alors que le chapitre
avait lui-même déclaré ce texte périmé. **Les textes en vigueur disent le
contraire** — le retrait met fin à l'appartenance, non aux obligations nées d'elle.
**La même entrée inscrit les statuts de la Banque comme « non lus » : l'article VI
l'est depuis le 2026-09-08, le reste ne l'est pas.**

**ACQUISITIONS QUI RESTENT, ET ELLES SONT PRÉCISES.** **(1) L'ANNEXE J des statuts
du Fonds**, à laquelle l'article XXVI renvoie pour le règlement des comptes à
défaut d'accord. **(2) L'ARTICLE II SECTION 5 (ii) des statuts de la Banque**,
auquel l'article VI renvoie pour les appels de capital. **(3) Les statuts
CONSOLIDÉS COMPLETS des deux institutions**, dont le corpus ne tient qu'un article
chacun. **Le corpus tient les articles qui RENVOIENT, non les textes AUXQUELS ils
renvoient.**

## Règle de citation versée le 2026-09-08 — UN CHIFFRE DE COMPTABILITÉ SE CITE AVEC SON ÉDITION

**LE CAS QUI L'ÉTABLIT, ET IL S'EST PRODUIT DANS LA MÊME NUIT.** L18.C22 a
rapporté, d'après un ouvrage tiers, que la comptabilité de la richesse des
nations faisait croître le capital naturel par habitant de 26 % entre 1995 et
2018, et il a opposé ce chiffre au constat que sept limites planétaires sur neuf
sont franchies. **Quelques heures plus tard, L18.C23 a ouvert de première main
l'édition en vigueur de cette comptabilité : elle donne un RECUL de plus de 20 %
du capital naturel renouvelable par habitant sur 1995-2020.**

**CE QUI A CHANGÉ N'EST PAS SEULEMENT LA PÉRIODE.** L'édition récente calcule ses
mesures réelles au moyen d'un **indice de volume enchaîné** au lieu d'un
**déflateur fondé sur les prix**, et l'institution présente ce changement comme
un alignement sur les meilleures pratiques internationales — ce qu'il est
vraisemblablement. **Une amélioration de méthode n'est pas une nouvelle du
monde.**

**RÈGLE.** **Un chiffre de comptabilité ne se cite jamais sans son ÉDITION, sa
PÉRIODE et sa CONVENTION.** Et lorsqu'un chiffre est repris d'un ouvrage tiers,
**le corpus doit dire de quelle édition ce tiers le tenait**, faute de quoi il
présente comme la position d'une institution ce qui n'est que son état à une
date.

**CE QUI A ÉTÉ CORRIGÉ DANS L18.C22.** Le titre du chapitre et celui de sa
section 2, qui affirmaient que deux comptabilités décrivent deux mondes ; le
résumé ; et le corps, qui expose désormais la PROPRIÉTÉ — une valeur peut monter
quand la quantité descend — sans l'adosser à un chiffre périmé. **Le fichier a
été renommé, l'identifiant L18.C22 conservé.** **Ce qui subsiste intact du
chapitre est le désaccord entre la Banque mondiale et le Programme des Nations
unies, dont la corrélation rapportée est de 0,144, et la leçon de l'indice bâti
pour conclure.**

**LA RÈGLE PRÉCÉDENTE EST CONFIRMÉE ET ÉTENDUE.** L19.C09 avait établi qu'une
révision de norme comptable peut DÉPLACER un résultat. **Ce cas établit qu'elle
peut en INVERSER LE SIGNE.**


## ÉTAT APRÈS LA NUIT DU 8 AU 9 SEPTEMBRE 2026 — CE QUI A CHANGÉ, ET CE QUI RESTE À L'AUTEUR

**TREIZE CHAPITRES ÉCRITS, DIX SOURCES OUVERTES, AUCUNE PUBLICATION.** Le corpus
passe de 316 à 329 chapitres. **Le contrôle passe sans blocage à chaque étape, et
rien n'a été poussé.**

### CE QUI A ÉTÉ OUVERT

**Textes en vigueur.** Article II et article IV des statuts de la Banque
internationale pour la reconstruction et le développement, dans leur version
amendée en 2012. **La moitié de l'acquisition bloquante d'A37 est close.**

**Le traité de référence du débat sur la soutenabilité.** Cinq chapitres sur sept
de Neumayer, cinquième révision rédigée en 2024 : introduction, chapitre 2
partiel, chapitres 3, 4, 5 et conclusions.

**La critique du cadre des limites planétaires.** Biermann et Kim, 2020, revue de
synthèse — **l'acquisition que F13 réclamait depuis le 2026-09-07.**

**Le bilan annuel du cadre.** Planetary Health Check 2025, institut de Potsdam.

**La comptabilité de la richesse des nations.** Rapport phare de la Banque
mondiale, édition 2024, résumé exécutif et deux passages de méthode.

**L'évaluation intergouvernementale des valeurs de la nature.** IPBES 2022,
résumés exécutifs des chapitres 3, 4 et 6.

### LES CINQ RÉSULTATS QUI COMMANDENT

**UN — F13 A TROIS CONFIRMATIONS INDÉPENDANTES, ET LA CHARGE DE LA PREUVE A
CHANGÉ DE CÔTÉ.** Sciences du système terrestre, économie de la soutenabilité,
évaluation intergouvernementale. Cette dernière énonce avec sa cote la plus forte
qu'aucun consensus n'existe sur les procédures d'agrégation. **Un dispositif qui
agrège doit désormais expliquer pourquoi il fait ce qu'une évaluation
intergouvernementale déclare sans procédure consensuelle.**

**DEUX — LA MÊME ISSUE S'EST PRÉSENTÉE CINQ FOIS PAR CINQ CHEMINS, ET ELLE N'EST
TOUJOURS PAS PRISE.** Assumer la pondération comme un choix politique déclaré,
révisable et attaquable. **Elle vient désormais de l'adversaire lui-même** :
Nordhaus recommande d'identifier l'objectif, d'écarter directement les tests
coûts-bénéfices, et de rendre le coût de cet écart transparent, *« rather than
allowing technicians to hide the choices in abstruse arguments »*. **C'est un
arbitrage de l'auteur, et il commande le reste.**

**TROIS — LE PARTAGE SOURCE / PUITS EST DEVENU LE POINT LE PLUS URGENT.** Le
verdict du traité de référence est coupé par côté de l'économie : substituabilité
mieux soutenue pour les ressources en entrée de production, non-substituabilité
mieux soutenue pour la capacité d'absorption. **Le dispositif n'est du côté
soutenu que si la grandeur qu'il qualifie est une grandeur de PUITS**, et le
corpus n'a jamais tranché.

**QUATRE — LA DESCENTE D'ÉCHELLE SE FAIT DÉJÀ, SANS MONNAIE, ET F10 S'EST
DÉPLACÉ TROIS FOIS.** Des méthodes fondées sur l'analyse de cycle de vie
traduisent les limites planétaires à l'échelle du produit et permettent d'évaluer
si un impact tient dans sa part allouée. **Ce que le dispositif doit justifier
n'est plus la mesure : c'est l'ajout monétaire, et cet argument n'est écrit nulle
part.**

**CINQ — LA FAMILLE D'INSTRUMENTS DU DISPOSITIF EST CLASSÉE EN DESSOUS D'UNE
AUTRE PAR UNE SOURCE INTERGOUVERNEMENTALE.** Les instruments socioculturels et de
droits coutumiers montrent un potentiel plus élevé que les instruments
économiques et juridiques pour opérationnaliser les valeurs diverses. **Le corpus
n'a jamais examiné ces deux familles. Tant qu'il ne l'a pas fait, il ne peut pas
soutenir que son instrument est nécessaire.**

### CE QUI EST FAVORABLE AU DISPOSITIF, ET IL FAUT LE PORTER AUSSI

**L'objection de croissance verte est écartée** par un auteur qui ne défend pas la
soutenabilité forte : les améliorations environnementales procèdent d'abord de
choix de politique publique, non de la croissance.

**Le motif de l'échec de la cible sur les incitations dommageables est orienté** :
défaut de mécanisme de conformité, et périmètre de mandat sectoriel. **Un
instrument monétaire porte sa contrainte dans son mécanisme et opère par
l'économie : il est dirigé sur le mode d'échec constaté.**

**Les valeurs de marché l'emportent quand l'arbitrage est inévitable**, ce qui est
l'argument le plus direct pour placer la grandeur écologique DANS le mécanisme
plutôt qu'en face.

**On ne compare pas un rendement à un insubstituable** — la critique par le
meilleur emploi des ressources rares est refusée par le traité de référence
lui-même.

**Atteindre la cible climatique ne suffit pas** : le mélange énergétique de
moindre coût compatible avec deux degrés franchit cinq limites sur huit.

### CE QUI EST DÉSORMAIS INTERDIT AU CORPUS

**Présenter la soutenabilité forte comme établie et la faible comme une
croyance.** Les deux sont non falsifiables, et le corpus l'est pour une autre
raison que l'adversaire — parce que sa position est NORMATIVE.

**Invoquer les préférences observées.** Elles sont majoritairement compatibles
avec la substitution.

**Attaquer la métrologie des comptes de richesse.** Leurs auteurs concéderont les
lacunes et le résultat tiendra ; le défaut est le concept, non la mesure.

**Se réclamer de la valeur de la nature pour fixer une échelle.** Les décisions de
prélèvement sont marginales, les valeurs totales ne servent pas à en décider.

**Citer un chiffre de comptabilité sans son édition, sa période et sa
convention.** Une révision de méthode a inversé le signe du capital naturel entre
deux éditions du même programme.

### LES QUATRE ACQUISITIONS QUI RESTENT, PAR ORDRE

**UN.** Les méthodes couplant limites planétaires et analyse de cycle de vie —
**trois chapitres du corpus réclament désormais la même littérature.**

**DEUX.** La section 6.5 de l'évaluation intergouvernementale, qui porte le guide
d'opérationnalisation — **c'est ce que CRITERE-L25 cherche, et c'est sur le
disque.**

**TROIS.** L'ANNEXE J des statuts du Fonds monétaire international. **Les voies
automatisées sont épuisées** : l'édition en ligne ne sert pas les annexes et le
site institutionnel refuse tout. **Récupération manuelle nécessaire.**

**QUATRE.** La citation de Nordhaus, à sa source de 1999. Elle porte l'argument le
plus utile de la nuit et elle est de seconde main.


## CINQ ARBITRAGES RENDUS PAR L'AUTEUR LE 2026-09-09 — A35, A36, SOURCE/PUITS, F13 ET A37

**CE SONT DES ARBITRAGES DE L'AUTEUR, NON DES PROPOSITIONS DU CORPUS.** Ils sont
rendus après la campagne de lecture des 8 et 9 septembre, et ils tranchent quatre
points que le corpus tenait ouverts depuis son ouverture. **Le registre les
projette ; ce texte fait foi.**

### A35 — LA DETTE COLLECTIVE : DEUX NOTIONS QUE LE CORPUS CONFONDAIT

**ARBITRAGE.** **La société n'est PAS qualifiée de débiteur juridique.**
**L'unité émise constitue un PASSIF DE L'ÉMETTEUR.** **La société supporte
L'INCIDENCE ÉCONOMIQUE du reflux.** **Ce sont deux notions différentes.**

**CE QUE CELA FERME.** La question que L19 devait clore et n'a pas close. Le
corpus cherchait qui « porte » la dette collective en traitant la charge
économique et l'obligation juridique comme une seule chose. **Elles ne le sont
pas** : un passif figure au bilan de celui qui l'a émis, et l'incidence se
répartit sur ceux qui en subissent l'effet, sans qu'aucun d'eux soit tenu.

**CE QUE CELA OUVRE, ET IL FAUT L'ÉCRIRE.** **La question de l'incidence devient
une question à part entière, et elle est distributive.** L11.C09 l'avait
découverte sans pouvoir la traiter ; le Livre 25 la porte. **Séparer les deux
notions ne dispense pas d'établir QUI supporte l'incidence, dans quelles
proportions, et si cette répartition est défendable.**

**ET UNE CONSÉQUENCE POUR L20.C24 ET L20.C26.** Ces chapitres ont établi qu'une
part appelable survit au retrait, sans sûreté, plafonnée, et bornée à l'état des
engagements à la date de sortie. **Un passif d'émetteur assorti d'appels sur les
membres est exactement la structure qu'ils décrivent** — et l'arbitrage rend
cette lecture pertinente là où elle n'était qu'une analogie.

### A36 — LA FONTE : DEUX MÉCANISMES, ET NON UN

**ARBITRAGE.** **Séparer deux mécanismes que le corpus tenait sous un seul mot.**
**(1) LE DÉMURRAGE SUR LES ENCAISSES est une RÈGLE MONÉTAIRE.**
**(2) LE PRÉLÈVEMENT LIÉ À L'IMPACT DES TRANSACTIONS relève d'une CONTRIBUTION
FISCALE, PARAFISCALE OU DE RÉSEAU, selon son architecture juridique.**

**CE QUE CELA FERME.** L'alternative « prélèvement ou décote » était mal posée :
elle demandait une réponse unique pour deux opérations qui n'ont ni la même
assiette, ni le même fait générateur, ni le même destinataire. **Le démurrage
frappe une DÉTENTION ; le prélèvement frappe une TRANSACTION QUALIFIÉE.**

**CE QUI RESTE OUVERT, ET C'EST NOMMÉ.** **La nature juridique du second dépend
de son architecture, et cette architecture n'est pas arrêtée.** Fiscal,
parafiscal ou de réseau ne sont pas équivalents : ils ne supposent pas la même
autorité, ne s'attaquent pas devant les mêmes juges, et n'ont pas les mêmes
conditions de légalité.

**CORRECTION QUE CET ARBITRAGE COMMANDE, ET ELLE EST APPLIQUÉE.** L18.C31 avait
suspendu à A36 la question de savoir si le dispositif « réalise » une réforme
fiscale écologique. **La réponse est désormais partagée** : le démurrage est une
règle monétaire et n'en relève pas ; le prélèvement pourrait en relever selon son
architecture. **Le chapitre est corrigé en ce sens le 2026-09-09.**

### PARTAGE SOURCE / PUITS — LES DEUX, DANS DES COMPTES SÉPARÉS

**ARBITRAGE.** **Conserver les deux côtés, dans des COMPTES SÉPARÉS.**
**LES PUITS portent des PLAFONDS PHYSIQUES NON COMPENSABLES.**
**LES SOURCES portent sur les DOMMAGES D'EXTRACTION, la DÉPENDANCE MATÉRIELLE et
la JUSTICE DISTRIBUTIVE — SANS INVOQUER UNE RARETÉ GÉNÉRALE QUI N'EST PAS
ÉTABLIE.**

**CE QUE CET ARBITRAGE CONCÈDE, ET C'EST À PORTER À SON CRÉDIT.** L18.C20 a
établi que la branche de la rareté des ressources est répondue, et répondue
CONTRE la position que le dispositif supposait : les preuves disponibles
soutiennent fortement la substituabilité du côté des entrées de production, et
l'auteur le plus cité du camp adverse tient que le danger est qu'il y ait TROP
d'hydrocarbures pour le climat, non trop peu. **L'arbitrage ne conteste pas ce
constat : il retire l'argument de rareté et refonde le côté source sur trois
autres motifs.**

**CE QUE CELA CHANGE POUR LE DISPOSITIF.** **Les trois motifs retenus ne sont pas
des raretés mais des DOMMAGES et des RÉPARTITIONS**, et ils échappent donc au
verdict de L18.C20, qui portait sur la disponibilité. **L18.C20 relevait
d'ailleurs que l'auteur écarte explicitement de son champ les dommages causés PAR
l'extraction** : l'abondance qu'il établit est une abondance de STOCK, non une
innocuité de PRÉLÈVEMENT.

**ET LA SÉPARATION DES COMPTES EST UNE RÉPONSE DIRECTE À F13.** Deux comptes qui
ne se compensent pas ne demandent aucun taux de change entre eux.

### F13 ET CRITERE-L25 — L'ISSUE EST PRISE

**ARBITRAGE.** **RENONCER À UN SCORE ÉCOLOGIQUE MONDIAL UNIQUE.** **Employer
PLUSIEURS SEUILS NON COMPENSABLES.** **Puis ASSUMER PUBLIQUEMENT que la
pondération restante est une DÉCISION POLITIQUE, PARTICIPATIVE ET
CONTESTABLE.**

**C'EST LA TROISIÈME VOIE DE F13, ET ELLE S'ÉTAIT PRÉSENTÉE CINQ FOIS SANS ÊTRE
PRISE.** Par la non-falsifiabilité d'un énoncé normatif (L18.C20) ; par la
position de droit assortie d'un seuil de conséquence (L18.C21) ; par la
prescription de Nordhaus d'énoncer l'objectif au lieu de le cacher dans le taux
(L18.C24) ; par la méthode multicritère qui laisse les critères exister sans
échelle commune (L18.C29) ; et par le guide qui RECONNAÎT l'incommensurabilité au
lieu de la résoudre et traite le rapport de pouvoir (L18.C31). **L'arbitrage la
prend.**

**CE QUE CELA COÛTE, ET IL FAUT L'ÉCRIRE SANS L'ADOUCIR.** **Le dispositif
renonce à prétendre que le montant émis MESURE la régénération.** Il ne peut plus
présenter son barème comme la traduction d'un fait naturel — ce que trois
littératures indépendantes lui interdisaient déjà. **Ce qu'il gagne est la
cohérence : une pondération déclarée politique est attaquable, donc révisable,
donc défendable.**

**CE QUE CELA N'ÉTEINT PAS.** **F13 reste OUVERT.** Ce qui est arbitré est la
RÉPONSE du dispositif, non la disparition de l'objection. **Et il reste un pas
non franchi, nommé par L18.C29 et L18.C31 : celui qui va d'une DÉCISION à un
MONTANT.** Plusieurs seuils non compensables organisent une décision ; **il faut
encore dire comment un montant en sort.**

### A37 — L'ÉMETTEUR : UNE BRANCHE À MODÉLISER EN PRIORITÉ

**ARBITRAGE.** **Modéliser PRIORITAIREMENT une institution internationale
émettant une UNITÉ DE RÉSERVE aux banques centrales, celles-ci émettant ensuite
leur monnaie nationale.** **Motif : c'est la branche la plus proche du précédent
des droits de tirage spéciaux, et la plus facile à comptabiliser.**

**CE QUE CELA RESPECTE.** L13.C01 avait établi, sur correction de l'auteur, que
la forme juridique de l'émetteur doit être un **PARAMÈTRE** du modèle et non une
hypothèse figée. **Cet arbitrage ne fige rien : il ordonne les branches.**

**ET IL DÉPLACE UNE ACQUISITION.** Le précédent des droits de tirage spéciaux
devient la référence de modélisation. **Le corpus ne l'a pas ouvert** : l'article
XV et les articles XVIII à XXV des statuts du Fonds, qui organisent le compte de
tirages spéciaux, ne sont pas au dossier — et l'édition qu'il en tiendrait serait
celle de 1944, qui ne les contient pas, ces droits n'existant pas encore.
**ACQUISITION DE RANG 1 : les articles du compte de tirages spéciaux, dans le
texte en vigueur, sur l'hôte qui répond.**


## SEPT CORRECTIONS DE L'AUTEUR SUR L'ARGUMENT F10 — 2026-09-09, LE JOUR MÊME DE SON ÉCRITURE

**L1.C31 A ÉTÉ ÉCRIT ET CORRIGÉ LE MÊME JOUR.** Le chapitre canonique expose
l'état corrigé et lui seul ; les motifs sont ici, au titre de la règle « où vit
l'historique d'une correction ». **Le fichier a été renommé, l'identifiant L1.C31
conservé.**

### 1. A35 ÉTAIT DÉJÀ ARBITRÉ, ET LE REGISTRE LE DISAIT OUVERT

**UNE DIVERGENCE REGISTRE / TEXTE EST RELEVÉE ET CORRIGÉE.** Le registre portait
A35 comme `ouvert`, avec la note « L19 devait la clore et ne l'a pas close ».
**Or L10.C06 et L1.C29 portent que A35 EST ARBITRÉ depuis un arbitrage antérieur
de l'auteur** : la dette est portée par l'ensemble de la société, refluée par des
fontes graduées. **Et L10.C06 porte la correction du 2026-09-07 : « A35 décrit
L'INCIDENCE ÉCONOMIQUE, non le porteur juridique. »** **La règle du registre a
joué : le texte fait foi, et le registre est corrigé.**

### 2. A35 EST SCINDÉ

**ARBITRÉ — le PORTEUR.** L'unité émise est un **PASSIF DE L'ÉMETTEUR**. La
société n'est pas débiteur juridique ; elle supporte l'incidence économique.
**C'est ce que la nomenclature de l'auteur appelle A35a.**

**OUVERT — A35b, cinq questions que le porteur ne tranche pas.** Ce que le
**DÉTENTEUR** peut réclamer. Comment le passif **S'ÉTEINT**. Quelle est sa
**CONTREPARTIE** à l'actif. Qui absorbe les pertes ou une **INSUFFISANCE DE
REFLUX**. Et si le bénéficiaire reçoit une **subvention, un crédit ou un droit
monétaire conditionnel**.

**L'IDENTIFIANT A35 EST CONSERVÉ, ET LE MOTIF EST MÉCANIQUE.** Une trentaine de
fichiers le citent, dont le titre d'un chapitre — L10.C06, « L'arbitrage A35, et
ce qu'il déplace ». **Le registre pose que les identifiants sont permanents et ne
sont jamais réattribués ; renommer A35 en A35a briserait ces renvois pour un
gain de forme.**

**ET LA CONTRADICTION QUE CETTE SCISSION SUPPRIME.** L1.C31 déclarait A35 arbitré
puis demandait au simulateur d'en comparer plusieurs branches. **Le simulateur
compare les branches d'A35b.**

### 3. « RENDRE FINANÇABLE » NE SUFFIT PAS — LA CORRECTION CENTRALE

**LA CRÉATION MONÉTAIRE PRODUIT DU POUVOIR D'ACHAT. ELLE NE PRODUIT NI TRAVAIL,
NI ÉNERGIE, NI MATÉRIAUX, NI CAPACITÉS PRODUCTIVES.**

**Une activité peut devenir nominalement finançable et rester matériellement
irréalisable.** **Elle peut aussi mobiliser des ressources en les retirant à
d'autres usages.** **Le test porte donc sur LES RESSOURCES RÉELLES MOBILISÉES,
l'inflation, les importations et l'incidence distributive** — non sur la
disponibilité d'un financement.

**La proposition est reformulée en conséquence, et la clause de contraintes n'y
est pas un ornement de prudence : c'est une CONDITION D'ÉCHEC.**

### 4. LE TROISIÈME ÉNONCÉ DÉPASSAIT SA DÉMONSTRATION

**« Financer à la réalisation » ne signifie PAS qu'aucun revenu futur ne sera
requis.** Cela dépend de **la créance éventuelle sur le bénéficiaire**, de **la
nature du passif de l'émetteur** et du **mécanisme de reflux** — c'est-à-dire
d'A35b, qui est ouvert.

**DEUX CHOSES DOIVENT ÊTRE DISTINGUÉES, ET LE CHAPITRE LES CONFONDAIT.** **Le
financement non remboursable DU BÉNÉFICIAIRE** — il ne doit rien, aucune
rentabilité future n'est exigée de lui. **Le passif monétaire DE L'ÉMETTEUR** —
il subsiste, et son extinction est une question distincte. **Ce qui subsiste de
l'énoncé porte sur la position du bénéficiaire, non sur celle de l'émetteur.**

### 5. LA CONDITION DE RÉFUTATION ÉTAIT TROP PROTECTRICE

**Exiger des solutions concurrentes « les mêmes activités, au même volume, avec
moins de coûts et de risques » impose une identité presque impossible et
IMMUNISE le dispositif.** **Il faut comparer des RÉSULTATS écologiques et sociaux
définis, non les mêmes projets ni les mêmes montants.**

**CONDITION DE DÉMONSTRATION, ARRÊTÉE PAR L'AUTEUR.** *NEMO IMS démontre un ajout
propre si, pour un résultat écologique et social défini, il permet de mobiliser
des ressources réelles que le meilleur portefeuille institutionnellement
réalisable d'instruments existants ne peut mobiliser dans le même délai, à coût
social total, risque macroéconomique et qualité de gouvernance comparables.*

**CONDITION D'ÉCHEC RÉCIPROQUE.** *Si un portefeuille réalisable d'instruments
existants atteint le même résultat à coût et risque égaux ou inférieurs,
l'avantage comparatif de NEMO n'est pas établi. Si NEMO ne l'atteint qu'en
franchissant les contraintes inflationnistes, extérieures, physiques ou
distributives, il échoue également.*

**LE TEST A CHANGÉ D'OBJET.** **Il ne demande plus si le dispositif est
NÉCESSAIRE — question qu'aucune expérience ne tranche — mais s'il a un AVANTAGE
COMPARATIF.** **Plus faible en apparence, plus dur en pratique : il oblige à
construire l'adversaire au lieu de le supposer absent.**

**DIFFICULTÉ NON TRANCHÉE, INSCRITE AU BALAYAGE.** Le mot **« réalisable »**
décide du résultat. **Politiquement réalisable** donne un adversaire affaibli par
des obstacles que le dispositif rencontrerait aussi. **Techniquement possible**
donne un adversaire que personne n'a jamais assemblé. **Le choix appartient à
l'auteur.**

### 6. LES COMPARATEURS ÉTAIENT MÉLANGÉS — ERREUR DE CATÉGORIE

**INSTRUMENTS DE FINANCEMENT, qui allouent des ressources** : transferts fiscaux,
investissement public, banques publiques de développement, garanties, subventions,
mécanismes de dette, allocations internationales existantes. **Ce sont eux qui
composent le portefeuille de comparaison.**

**MÉCANISMES D'AUTORITÉ, DE CONSENTEMENT ET DE CONTRÔLE, qui ne financent pas** :
cogestion, aires et territoires conservés par les communautés, revitalisation des
savoirs, codes de conduite, consentement préalable. **Ils déterminent QUI DÉCIDE,
QUI CONSENT, QUI CONTRÔLE.**

**LEUR DEMANDER DE FINANCER EST UNE ERREUR DE CATÉGORIE.** **Ils ne sont pas des
concurrents : ils sont une DIMENSION de la clause « qualité de gouvernance », et
peuvent accompagner CHACUNE des solutions de financement, y compris le
dispositif.**

### 7. LE SIMULATEUR NE TRANCHE PAS TOUT — TROIS VOIES DE PREUVE

**Le chapitre écrivait que les quatre énoncés étaient « des questions de
simulateur ». Ils ne le sont pas tous.**

**ENQUÊTE EMPIRIQUE** — l'existence et la TAILLE des activités insuffisamment
financées ne se déduisent d'aucun modèle. **MODÈLE COMPTABLE ET
MACROÉCONOMIQUE** — cohérence des bilans, flux, inflation, importations, reflux,
répartition. **COMPARAISON INSTITUTIONNELLE** — coûts administratifs et risques
de capture, par études comparatives et cas historiques. **La clause « qualité de
gouvernance » en dépend entièrement, et aucun modèle ne la produira.**

### 8. ET LA SÉPARATION SOURCE / PUITS N'EST PAS UNE RÉPONSE DIRECTE À F13

**L'absence de compensation entre deux comptes évite UNE PARTIE du problème ;
elle ne le résout pas.** **Il reste à passer de plusieurs contraintes à une
décision d'éligibilité, puis à un montant.**

**CHAÎNE ARRÊTÉE PAR L'AUTEUR LE 2026-09-09, ET ELLE EST À TROIS ÉTAGES.**
**(1) SEUILS PHYSIQUES SERVANT DE VETO.**
**(2) PRIORITÉ SOCIALE ET TERRITORIALE DÉCIDÉE POLITIQUEMENT.**
**(3) MONTANT DÉTERMINÉ PAR LES COÛTS RÉELS, LES CAPACITÉS DISPONIBLES ET LA
CONTRAINTE MACROÉCONOMIQUE.**

**Le modèle doit distinguer ces trois étages, et ne pas les confondre en un
score.**

### 9. CE QUI N'EST PAS CHANGÉ, ET POURQUOI

**La structure de `verifications_en_attente` n'est PAS modifiée.** L'auteur
arbitre le 2026-09-09 d'attendre : **les trois chapitres pilotes diront si le
champ doit ensuite être séparé entre vérifications factuelles, objections non
résolues et dettes de conception.** **La question posée par
protocoles/candidats-verifie.md reste donc ouverte, et elle est datée.**


## LA MATRICE COMPTABLE D'A35b — 2026-09-09 : ÉCRITE, RÉFUTÉE DEUX FOIS, REFAITE DEUX FOIS

**L'auteur a donné le feu vert pour le NOYAU COMPTABLE SEUL.** Trois versions ont
été écrites le même jour, et **les deux premières ont été réfutées par
l'auteur**. Ce qui suit tient l'état corrigé et le motif de chaque correction,
parce que les erreurs sont instructives et que le corpus ne masque pas les
siennes.

### VERSION 1 — DEUX RÈGLES DE REJET FAUSSES

**ELLE CONFONDAIT L'EXISTENCE D'UN PASSIF ET LA CAPACITÉ DE LE PAYER.** Elle
rejetait une branche où l'émetteur promettait une conversion sans détenir de quoi
la servir. **Une dette reste une dette quand son débiteur ne peut pas
l'honorer** : l'insuffisance produit un risque de liquidité ou de solvabilité,
et des banques centrales fonctionnent avec des fonds propres négatifs.

**ELLE MESURAIT LA COUVERTURE APRÈS LE REFLUX.** Une obligation stipulée « à tout
moment » se contrôle **au pic**, et le pic vaut l'émission entière. Le bilan
final affichait une couverture exacte et cachait un découvert permanent.

**ET SES TESTS NE PROUVAIENT PAS CE QU'ILS SEMBLAIENT PROUVER.** Ils
établissaient que le programme appliquait ses règles, non que les règles étaient
fondées.

### VERSION 2 — QUATRE FAUTES DE PLUS, RELEVÉES LE MÊME JOUR

**ELLE MÊLAIT ENCORE CALCUL ET QUALIFICATION.** Elle écrivait « reconnu comme
passif au sens du § 4.101 » alors qu'elle vérifiait seulement que **quatre
étiquettes étaient renseignées**. **Une qualification comptable ne se calcule
pas.**

**ELLE ÉCARTAIT LA STRUCTURE COLLECTIVE POUR UN MOTIF INEXACT.** Elle invoquait
un débiteur « collectif ». **Or chaque membre est le débiteur DÉTERMINÉ de sa
propre allocation, et la norme reconnaît explicitement ce traitement** [S1,
§ 12.49]. Ce qui est collectif, c'est le dispositif qui **sert le droit
d'échange** — cela relève de la liquidité, non de la reconnaissance. **Cette
architecture contredit A35a ; elle n'est pas comptablement méconnaissable.**

**ELLE FIGEAIT UN CRÉANCIER UNIQUE DANS LA FICHE.** Un instrument transférable
change de créancier avec son détenteur, **et la créance de chacun vaut son
encours du moment.** L'identité « passif total = somme des avoirs de tous les
détenteurs » est désormais contrôlée **après chaque opération**.

**ELLE CONCLUAIT QUE LE COLLECTEUR DÉCIDAIT DE L'EXTINCTION.** Il ne décide que
de la **première destination** des unités perçues.

### CE QUE LA VERSION 3 REND — CINQ RÉSULTATS, DEUX SEULEMENT CALCULÉS

**R1a COHÉRENCE ARITHMÉTIQUE — calculée**, y compris l'identité créancier /
débiteur à chaque étape. **R1b QUALIFICATION — PROPOSÉE, jamais établie** : le
programme n'écrit plus « reconnu comme passif ». **R2 LIQUIDITÉ — calculée**, au
pic, et **par scénarios séparés** quand l'instrument est servi par d'autres
participants. **R3 SOLVABILITÉ — non évaluable** sur un cycle sans intérêt ni
horizon. **R4 CONFORMITÉ JURIDIQUE — non évaluée.**

**UNE BRANCHE PEUT ÊTRE ARITHMÉTIQUEMENT COHÉRENTE ET ILLIQUIDE ; ELLE PEUT
L'ÊTRE ET SA QUALIFICATION RESTER À EXAMINER.** **Confondre ces plans est ce qui
a produit toutes les fautes précédentes.**

### L'ÉNONCÉ CORRECT SUR A36, ET IL REMPLACE LE PRÉCÉDENT

**Trois sous-branches établissent ce que devient l'unité perçue par l'État :
conservation, remise en circulation, transfert à l'émetteur.** **L'encours final
vaut soixante-cinq dans les deux premiers cas et quarante dans le troisième —
soit exactement celui du cas où l'émetteur percevait lui-même.**

**ÉNONCÉ À RETENIR :** *à circuit ultérieur inchangé, le choix du collecteur
modifie l'encours immédiatement après perception ; l'encours final dépend ensuite
de l'emploi des unités collectées.*

### UNE OBLIGATION D'ACCEPTATION NE VAUT QUE SI QUELQUE CHOSE EST DÛ

Le droit du détenteur est de remettre l'unité en règlement de ce qu'il doit à
l'émetteur. **Encore faut-il qu'il doive quelque chose.** Une contribution
statutaire est désormais inscrite **avec son fait générateur**, et une branche
témoin en est dépourvue : **sans elle, la proposition de qualification est
SUSPENDUE**, le droit restant une possibilité future. **La branche n'est pas
rejetée pour autant** — la distinction est le cœur de la correction.

### LE PLAFOND DE DÉSIGNATION A ÉTÉ SOURCÉ, ET IL A RÉVÉLÉ UNE ERREUR

**Deux acquisitions avaient échoué en 403** le 2026-09-09 — la foire aux
questions du Fonds et son document de politique de 2023, tous deux sur
`imf.org`. **L'auteur a indiqué que le texte était accessible ailleurs, et il
l'était** : l'eLibrary sert l'article XIX en clair, comme elle servait déjà le
texte en vigueur des Statuts. **Ouvert et lu le 2026-09-09.**

**ET LA LECTURE A INFIRMÉ LE MODÈLE.** « *A participant's obligation to provide
currency shall not extend beyond the point at which its holdings of special
drawing rights IN EXCESS OF its net cumulative allocation are equal to TWICE its
net cumulative allocation* » [art. XIX § 4(a)]. **C'est l'EXCÉDENT qui est borné
à deux allocations, non les avoirs totaux : le plafond total vaut TROIS
allocations.** Le modèle écrivait « deux allocations moins les avoirs » et
**sous-estimait la capacité d'une allocation entière**. **Et le § 4(b) ajoute
qu'un participant PEUT fournir au-delà : la limite borne l'obligation, jamais la
possibilité.**

**L'ERREUR ÉTAIT MASQUÉE PAR LE SCÉNARIO**, la ressource étant nulle de toute
façon, et le test ne contrôlait que ce minimum. **Le calcul est désormais une
fonction pure, éprouvée hors de tout scénario.** **Leçon de méthode : un test qui
ne regarde que le résultat composé ne voit pas l'erreur de l'un de ses facteurs.**

### LES ACCORDS VOLONTAIRES ONT ÉTÉ OUVERTS À LEUR TOUR, ET ILS DÉPLACENT LE RÉSULTAT

**Même chemin, même succès** : l'`Annual Update on SDR Trading Operations`, Policy
Papers 2025/032, renvoie 403 sur `imf.org` et s'ouvre en clair sur l'eLibrary.
**Lu dans le texte le 2026-09-09.**

**QUARANTE ET UN ACCORDS VOLONTAIRES**, tous employés depuis l'allocation
générale de 2021. Capacités agrégées au 31 août 2025 : « *about SDR 202 billion
and SDR 170 billion, respectively* » à l'achat et à la vente. **Et sur le
mécanisme que le modèle plafonne** : « *these plans have not been activated and
remained precautionary SINCE 1987* ».

**CE QUE CELA CHANGE POUR LA LECTURE DES TROIS SCÉNARIOS.** La désignation est un
**dernier ressort dormant depuis près de quarante ans**. **Le premier scénario —
le fonctionnement normal — est donc le SEUL CANAL INSTITUTIONNEL correspondant à
la pratique observée** ; **son montant et ses autres paramètres restent
illustratifs et non calibrés.**

**ET UNE PREMIÈRE RÉDACTION AVAIT SURQUALIFIÉ LA SOURCE.** Elle écrivait
« accords révocables, non une obligation », et faisait passer la liquidité « du
droit au comportement ». **Le rapport n'établit ni l'un ni l'autre** : il décrit
des accords bilatéraux par lesquels les participants acceptent d'acheter et de
vendre dans certaines limites, mentionne des périodes de notification et la
possibilité qu'un accord prenne fin, **et ne dit rien de la portée juridique de
l'engagement pendant sa durée.** **Le caractère volontaire porte au minimum sur
l'ADHÉSION.**

**TROIS QUALIFICATIONS DISTINCTES, ET ELLES NE SE CONFONDENT PAS.** L'ACCORD
VOLONTAIRE : engagement contractuel dans des limites convenues, conditions de
sortie à établir. LA DÉSIGNATION : obligation statutaire conditionnelle, activée
par le Fonds pour certains participants. AU-DELÀ DU PLAFOND : fourniture
volontaire possible.

**ET LA LIQUIDITÉ ORDINAIRE REPOSE CONJOINTEMENT** sur un cadre contractuel, des
capacités financières, la coordination du Fonds et le comportement effectif des
participants. **Aucun de ces quatre termes ne se réduit aux trois autres.**

### CE QUI RESTE NON SOURCÉ, ET DOIT LE RESTER

**Les modalités contractuelles individuelles des accords** — fourchette par
participant, clauses de DURÉE, de SUSPENSION et de SORTIE. Les données publiques
agrégées existent ; ces clauses-là peuvent ne pas être publiques, et le corpus ne
les tient pas. **Tant qu'il ne les tient pas, il ne peut rien conclure sur la
portée juridique de l'engagement : ni qu'il oblige, ni qu'il n'oblige pas.**

**Les passifs constructifs du § 4.102** ne sont pas représentés : le modèle exige
un instrument explicite, ce qui peut le rendre **plus sévère que la norme**.

**Les passifs constructifs du § 4.102** ne sont pas représentés : le modèle exige
un instrument explicite, ce qui peut le rendre **plus sévère que la norme**.

### LE JALON SUIVANT EST HUMAIN

`protocoles/revue-comptable-a35b.md` pose HUIT questions, dont SEPT à un comptable national
et UNE — la sixième, sur le passage du plafond statutaire individuel à une capacité
de secours exigible et mobilisable — à un juriste en droit monétaire international
ou à un praticien des opérations de réserves
ou à un spécialiste des bilans de banque centrale. **Aucun modèle
macroéconomique avant cette revue** : le corpus a atteint une frontière où une
boucle supplémentaire entre modèles déplacerait des conventions sans les valider.


## CONCLUSION DE L'AUTEUR SUR NEMO IMS — 2026-09-09

**ÉNONCÉ QUI FAIT FOI, ET IL EST DE L'AUTEUR :**

> **NEMO IMS constitue une hypothèse d'architecture monétaire et écologique
> suffisamment cohérente pour justifier un programme expérimental. Une version
> limitée peut être testée. Sa stabilité macroéconomique, son avantage sur les
> instruments existants, sa capacité à corriger les déséquilibres internationaux
> et sa voie d'adoption mondiale restent à démontrer.**

**Ce n'est ni « NEMO fonctionne » ni « NEMO est irréalisable ».** Les deux
formules seraient également fausses, et le corpus a mis onze mois à pouvoir
écrire la troisième.

### 1. TROIS PROPOSITIONS SOUS UN SEUL NOM — A43

| Composante | État arrêté |
|---|---|
| Financement monétaire ciblé d'activités écologiques et sociales | **pilotable sous fortes limites** |
| Unité de réserve internationale entre banques centrales | **techniquement plausible ; comptablement et juridiquement à finaliser** |
| NEMO Exchange Standard obligatoire à parités fixes | **non applicable en l'état** |

**La séparation est l'apport principal de cette conclusion.** Le corpus discutait
un objet unique dont les trois moitiés n'avaient ni la même maturité, ni les
mêmes obstacles, ni le même verdict.

### 2. CE QUE LE CORPUS TIENT DÉJÀ

**Les activités essentielles peuvent être insuffisamment financées** parce que
leurs bénéfices sont diffus, tardifs ou non captables — c'est le filtre à quatre
conditions de L1.C15, dont l'opérationnalisation est commandée par
`OPERATIONNALISATION-INSOLVABLE`.

**Une unité de réserve internationale est concevable**, et le précédent existe :
L19.C10 en a lu le régime comptable et statutaire dans le texte.

**Une infrastructure commune de règlement multidevise est techniquement
réalisable.** ACQUISITION FAITE LE 2026-09-09 : le projet Agorá de la Banque des
règlements internationaux, `bis.org/about/bisih/topics/fmis/agora.htm`, **lu dans
le texte**. « *It brings together eight central banks, including those of five
major reserve currencies, and over 40 leading financial institutions [...] The
prototype demonstrates that tokenised commercial bank deposits can be
successfully combined with the trust and safety of tokenised central bank
reserves on a shared platform. The prototype enables atomic, multi-currency
settlement of wholesale cross-border payments* ». **DEUX RÉSERVES QUE LE TEXTE
IMPOSE, ET QU'IL NE FAUT PAS EFFACER : c'est un PROTOTYPE, et le règlement
continu n'est possible que « *if implemented* ». Le périmètre est de GROS, non de
détail** — ce qui coïncide avec le pilote recommandé, mais par accident et non
par démonstration.

**L'allocation peut être séparée des paiements au public** : l'institution alloue
aux banques centrales, les bénéficiaires reçoivent de la monnaie nationale.
C'est la circulation `monnaie_nationale` de la matrice A35b.

**Les seuils écologiques peuvent être non compensables** — un bon résultat
climatique n'autorise pas un dépassement sur l'eau, l'azote ou la biodiversité.

**Et le corpus distingue désormais contrainte physique, décision politique et
montant financier** : c'est la chaîne à trois étages arrêtée le 2026-09-09.

### 3. LES CINQ OBSTACLES QUI CONDITIONNENT L'APPLICABILITÉ

**AUCUN DES QUATORZE FALSIFIEURS N'EST LEVÉ.**

**(1) LE BOUCLAGE MACROÉCONOMIQUE.** Volume d'émission, reflux transactionnel,
démurrage, inflation, importations supplémentaires, capacités productives
disponibles, répartition entre pays et secteurs. **La condition d'échec est déjà
écrite en F1** : qu'aucun couple de paramètres ne satisfasse simultanément un
volume suffisant pour financer et un reflux suffisant pour ne pas produire
d'inflation nette.

**(2) LE RÉGIME DE CHANGE.** Le dispositif ne peut pas conserver ensemble parités
fixes, liberté des capitaux et autonomie monétaire nationale. **PRÉCISION DUE À
L1.C26, ET ELLE EST PLUS ÉTROITE QUE « LE CORPUS LE DÉMONTRE »** : le chapitre ne
conclut pas que le dispositif est inopérant, il conclut que **le livre revendique
trois propriétés dont deux sont acquises et une est impossible**, et que deux
réponses sont tenables. **L'auteur tranche pour un premier pilote : LIMITER LES
MOUVEMENTS DE CAPITAUX**, en cantonnant NEMO aux règlements liés aux projets et à
certains échanges commerciaux.

**(3) LES DÉSÉQUILIBRES COMMERCIAUX.** Un pays déficitaire détruit plus de
monnaie qu'il n'en reçoit ; sa masse se contracte. **Supprimer le besoin de
réserves de change ne supprime pas la contrainte extérieure.** L1.C26 pose déjà
la question — *qu'est-ce qui empêche un pays durablement déficitaire de se
vider ?* — et le livre y répond par les émissions régénératives, **thèse forte et
entièrement non instruite**. Le dispositif doit donc ajouter : facilité
temporaire de liquidité, plafonds de solde débiteur ET créditeur, mécanisme
symétrique sur les excédents persistants, procédure de correction structurelle,
et éventuellement des parités ajustables selon une règle annoncée. **Faute de
quoi il impose une déflation permanente aux pays structurellement déficitaires.**

**(4) L'AVANTAGE COMPARATIF — F10.** La question n'est plus « peut-on créer de la
monnaie ? » mais **« NEMO mobilise-t-il davantage de ressources réelles, plus
vite et avec moins de risques, que la meilleure combinaison réalisable
d'instruments existants ? »** Les concurrents sont nommés : réforme des
subventions dommageables, investissement et commande publics, banques publiques
de développement, garanties publiques, fiscalité écologique, réglementation et
quotas, allocations de droits de tirage spéciaux, coopération existante.
**L1.C31 en donne le test ; le portefeuille concurrent n'est pas construit.**

**(5) NEMO AJOUTE SANS RETIRER — F14.** Financer du renouvelable ne ferme aucune
mine. **Et l'auteur en tire la conséquence la plus lourde de tout le corpus :
NEMO IMS NE PEUT PAS, SEUL, GARANTIR LES CONDITIONS DE LA VIE SUR TERRE.** Il
peut financer et accélérer une politique qui les protège, **à condition que cette
politique contienne aussi des obligations physiques de réduction et de
fermeture** : suppression des subventions dommageables, normes absolues,
moratoires, calendriers de fermeture, interdictions, reconversion
professionnelle et territoriale, garanties sociales pour les populations
touchées.

### 4. LA FORME EXPÉRIMENTABLE — UN NEMO MINIMAL

**PÉRIMÈTRE INSTITUTIONNEL.** Coalition de quelques pays volontaires aux
situations différentes — importateurs, exportateurs, riches, du Sud. **La banque
centrale de chaque membre est le seul détenteur direct de l'unité.** Paiements
aux bénéficiaires en monnaie nationale. Institution commune créée par accord
limité, ou hébergée provisoirement. **Aucun usage de détail, aucun compte pour
les particuliers.**

**PÉRIMÈTRE ÉCONOMIQUE.** Une ou quelques catégories de projets bien mesurables.
Montant d'émission strictement plafonné. **Aucun financement fondé sur une
promesse de résultat écologique invérifiable.** Analyse préalable des
travailleurs, matériaux, machines, énergie et capacités industrielles.
**Interruption automatique en cas de tension excessive sur les prix, les
importations ou des ressources critiques.**

**QUALIFICATION — L'ORDRE EST CELUI DÉJÀ ARRÊTÉ.** (1) veto physique ; (2)
priorité politique et territoriale, participative et contestable ; (3) montant
selon les coûts réels, les capacités et la marge macroéconomique.

**ET LA SÉPARATION DES ORGANES EST UNE EXIGENCE, NON UN ORNEMENT.** Définir les
seuils, instruire les projets, décider l'émission, vérifier les résultats,
sanctionner les déclarations inexactes, juger les recours : **six fonctions, six
organes. Une seule organisation les concentrant serait trop facile à capturer** —
c'est la réponse directe à MODELE-ADVERSAIRE.

**REFLUX ET DÉMURRAGE, POUR LE PILOTE.** Démurrage sur les seuls soldes
institutionnels en unités, **pas sur l'épargne des ménages**. Prélèvement
transactionnel traité séparément, sa nature restant à choisir — A36. **Écrire
précisément qui collecte, qui conserve, qui remet en circulation et qui éteint**
— ce que la matrice A35b a montré déterminant. **Et prévoir un régime d'urgence
lorsque le reflux devient procyclique en période de crise.**

### 5. LA TRAJECTOIRE, EN SEPT ÉTAPES

**(1) SPÉCIFICATION** — achever A35b, A36, le mécanisme de correction des
déficits extérieurs, la règle de recalibrage, les clauses de retrait et de
liquidation. **(2) VALIDATION EXTERNE** — comptable national, juriste monétaire,
macroéconomiste, spécialiste des infrastructures de paiement, experts écologiques
indépendants. **(3) EXPÉRIENCE FICTIVE** — qualifier rétrospectivement plusieurs
dizaines de projets **sans émettre**, mesurer les désaccords entre évaluateurs,
comparer aux financements réellement obtenus. **(4) SIMULATION MACROÉCONOMIQUE**
— plusieurs pays, prix, salaires, importations, capacités, soldes commerciaux,
mouvements de capitaux, scénarios de crise. **(5) PILOTE FERMÉ** à valeur
limitée, convertibilité et liquidation explicites. **(6) EXTENSION RÉGIONALE**,
seulement si le pilote établit additionnalité, stabilité, mesurabilité,
résistance à la fraude et répartition acceptable des coûts. **(7) ÉCHELLE
MONDIALE**, envisageable seulement après démonstration du bénéfice pour les
premiers entrants et d'un chemin politique face à ceux qui profitent du système
actuel.

**L'ÉTAPE 3 EST CELLE QUE LE CORPUS PEUT ENTREPRENDRE SANS PERSONNE**, et elle
recoupe exactement le protocole `validation-essentiel-insolvable.md` : constituer
des cas, faire classer par des tiers, documenter les désaccords.

### 6. LES OPPOSITIONS, ET ELLES SONT NOMMÉES

Banques centrales craignant la perte d'autonomie ; ministères des Finances y
voyant un contournement budgétaire ; pays à monnaie de réserve et pays
durablement excédentaires ; banques et infrastructures privées menacées dans
leurs revenus ; industries dont les actifs devraient fermer ; **pays du Sud
craignant une conditionnalité écologique définie par les pays riches** ;
contribuables et épargnants si le reflux est perçu comme régressif ; défenseurs
des libertés publiques si le système exige une traçabilité excessive ; et **ceux
qui pourront influencer ou contourner la qualification**.

**ACQUISITION FAITE LE 2026-09-09** : la page du Conseil de stabilité financière
sur les paiements transfrontaliers, `fsb.org/work-of-the-fsb/
financial-innovation-and-structural-change/cross-border-payments/`, **ouverte et
lue**. Le diagnostic qu'elle porte — l'interopérabilité technique progresse
tandis que la fragmentation juridique et réglementaire demeure l'obstacle central
— **est cohérent avec le corpus, mais la page acquise est une page de
présentation : elle renvoie à des rapports que le corpus n'a pas ouverts.** **À
citer comme point d'entrée, pas comme démonstration.**

### 7. CE QUE CETTE CONCLUSION CHANGE POUR LE CORPUS

**LA VERSION LA PLUS PROMETTEUSE EST NOMMÉE, ET ELLE EST ÉTROITE** : une facilité
internationale de financement et de règlement entre banques centrales, adossée à
des seuils écologiques non compensables, **complétée par des politiques
obligatoires de substitution**. **Le remplacement mondial du système monétaire
actuel n'est pas une proposition applicable**, et le corpus cesse de l'instruire
comme telle.

**F14 REÇOIT UNE CONCESSION MAJEURE**, et elle est de l'auteur : le dispositif ne
garantit pas seul les conditions de la vie. **Cela ne lève pas F14 ; cela en
accepte le contenu et déplace la thèse.**

**ET LE CORPUS PEUT DÉSORMAIS CONCLURE SANS SE CONTREDIRE.** Il a passé onze mois
à instruire une proposition unique. Il en sort avec trois propositions séparées,
une seule expérimentable, cinq obstacles nommés et une trajectoire en sept
étapes dont il peut entreprendre la troisième seul.


## DÉCISION DE PRINCIPE SUR LES CAPITAUX — 2026-09-09, ET ELLE FERME P49

**NEMO IMS ABANDONNE LA LIBRE CIRCULATION INCONDITIONNELLE DES CAPITAUX.**

Le NEMO Exchange Standard retient désormais explicitement trois propriétés, et
les nomme : **parités stables ou administrées, autonomie monétaire nationale,
compte de capital réglementé.**

### 1. CE QUE CETTE DÉCISION FERME

**P49 ÉTAIT BLOQUANTE, ET ELLE DEMANDAIT EXACTEMENT CELA.** L1.C26 § 4
établissait que le livre revendique trois propriétés dont deux sont acquises et
une est impossible, et que **deux réponses seulement sont tenables** :
restreindre la mobilité des capitaux, ou admettre l'autonomie monétaire perdue.
**L'auteur rend la première.** **Le triangle n'est plus contourné : un sommet
est nommé.**

**LE DISPOSITIF OCCUPE DÉSORMAIS LE SOMMET DE BRETTON WOODS**, ce que L1.C21
suggérait déjà en mentionnant un contrôle des capitaux — **et la contradiction
interne du corpus est levée** : L1.C21 disait le contrôle, la source du livre
revendiquait la libre circulation, **c'est le contrôle qui l'emporte.**

### 2. CE QUE LA DÉCISION NE FERME PAS, ET IL FAUT LE DIRE AUSSI FORT

**LES PAIEMENTS INTERNATIONAUX NE SONT PAS FERMÉS.** Restent exécutables : le
commerce de biens et de services, les revenus, les transferts familiaux, le
règlement des engagements. **Les investissements directs productifs peuvent
rester autorisés**, sous conditions de transparence, de durée et de traçabilité.

**CE QUI EST ENCADRÉ EST NOMMÉ** : flux financiers de portefeuille, mouvements
spéculatifs de court terme, crédit international à effet de levier, dérivés, et
canaux de contournement. **Les instruments le sont aussi** : autorisation,
plafonds, réserves obligatoires, délais de détention, prélèvements variables.
**Et les mesures temporaires peuvent porter SYMÉTRIQUEMENT sur les entrées et
sur les sorties** — la symétrie n'est pas un détail, c'est ce qui distingue un
régime d'un contrôle de sortie de crise.

### 3. LA FORMULATION PUBLIQUE, ARRÊTÉE PAR L'AUTEUR

> « **NEMO IMS garantit la continuité des paiements courants légitimes et soumet
> les mouvements de capitaux à des règles communes, transparentes,
> proportionnées et révisables afin de préserver la stabilité monétaire et
> l'autonomie des collectivités.** »

### 4. CE QUE CET ARBITRAGE COÛTE

**LA LIGNE ENTRE PAIEMENT COURANT ET MOUVEMENT DE CAPITAL EST UN OBJET DE DROIT
ET DE PRATIQUE, NON UNE ÉVIDENCE.** C'est elle qui décide de tout, et **c'est
exactement là que se loge le contournement** : une avance commerciale est un
paiement courant, un paiement courant surfacturé est une sortie de capital.
**Rien de cela n'est conçu.**

**PIÈCE OUVERTE LE MÊME JOUR — `CONTROLE-DES-CAPITAUX`.** À concevoir : la ligne
entre paiements courants et compte de capital ; le régime des investissements
directs ; **les règles anti-contournement** ; l'autorité compétente ; **les voies
de recours** ; et les mesures de crise. **Le principe est tranché, aucune
modalité ne l'est.**

**ET L'ARBITRAGE NE TOUCHE PAS AU § 5 DE L1.C26.** **Les déséquilibres
commerciaux restent entiers** : le solde continue de se déverser intégralement
sur la masse monétaire interne, sans réserves et sans taux de change pour
l'absorber. **Fermer le compte de capital ne corrige pas le compte courant** —
c'est P50, et elle demande toujours son chiffrage.

### 5. CE QUE LE CORPUS DOIT MAINTENANT PORTER SANS L'ADOUCIR

**UN CONTRÔLE DES CAPITAUX EST UNE CONTRAINTE SUR LES PERSONNES, PAS SEULEMENT
SUR LES FLUX.** Il suppose une autorité qui autorise, donc qui refuse ; une
traçabilité, donc une collecte ; des recours, donc des litiges. **La formulation
publique retient « proportionnées et révisables », et ces deux mots sont des
engagements, non des ornements** : ils appellent une procédure et un juge.

**Les oppositions nommées le 2026-09-09 s'appliquent ici en premier** : les
défenseurs des libertés publiques si le système exige une traçabilité excessive,
et les pays du Sud si le régime est défini par les pays riches. **Un contrôle des
capitaux mal conçu reproduit exactement l'asymétrie que le dispositif prétend
corriger.**


## LES DÉSÉQUILIBRES COURANTS PERSISTANTS — MODÈLE À TROIS PAYS, 2026-09-09

**SOLUTION DE RÉFÉRENCE ARRÊTÉE PAR L'AUTEUR** : comptes des banques centrales
auprès de l'institution, corridor toléré de déficit ET d'excédent, obligations
graduées des deux côtés, facilité temporaire de liquidité, parités administrées
— stables mais révisables. **Deux exigences** : un déficit causé par
l'importation de biens essentiels ne doit pas imposer de contraction ; et
l'accumulation indéfinie d'excédents doit être empêchée. **Seuils non fixés,
délibérément.**

**MODÈLE CONSTRUIT** — `modeles/nemo_soldes.py`, éprouvé par
`modeles/test_nemo_soldes.py`. Trois pays, huit périodes, quatre scénarios :
référence, choc énergétique, mauvaise récolte, rupture commerciale. Sont suivis
séparément, comme demandé : les échanges réels en volume, les soldes NEMO, les
masses monétaires, la liquidité, les parités et la répartition de l'effort.

### CE QUE F6 A IMPOSÉ À LA CONCEPTION AVANT QUE LE MODÈLE TOURNE

**LA SYMÉTRIE EST UN PARAMÈTRE, JAMAIS UNE HYPOTHÈSE.** Le corpus a lu sur
pièces les *Collected Writings* de Keynes, volume XXV [L1.C25, S12] : la charge
symétrique de l'Union internationale de compensation existait — « *whether it
is a credit or a debit balance* » — **mais le déficitaire subissait et
l'excédentaire délibérait**, Keynes l'avait déclarée non essentielle, **et elle
a été refusée quand même.** Chaque scénario est donc joué DEUX FOIS.

### TROIS RÉSULTATS, ET LES TROIS SONT CONTRE LA SOLUTION DE RÉFÉRENCE

**(1) LA PROTECTION DES IMPORTATIONS ESSENTIELLES CÈDE QUAND LE CHOC DURE PLUS
LONGTEMPS QUE LA FACILITÉ.** Elle tient au choc énergétique jusqu'à la période
six, puis **le remboursement à échéance rétablit la contraction pendant que le
choc dure encore.** **Une facilité temporaire ne supprime pas la contraction :
elle la DIFFÈRE.** Le test l'établit par isolement de la cause — allonger la
durée fait disparaître le manquement, augmenter le plafond ne le fait pas.

**(2) LE CORRIDOR NE BORNE PAS, IL TARIFE.** L'exigence n'est tenue dans aucun
des quatre scénarios. Et le test précise le mécanisme : **un taux appliqué au
dépassement fait converger le solde vers « corridor plus flux divisé par
taux »** — il borne asymptotiquement, **il ne pose aucun plafond**, et la
convergence peut être plus lente que le choc. À barème fort, l'excédent croît
encore de cinq par période au lieu de quarante-trois. **Empêcher demande un
plafond DUR, ou une charge croissant plus vite que le solde.**

**(3) MÊME CONTRAIGNANTE, LA SYMÉTRIE EST NOMINALE.** Au choc énergétique,
l'excédentaire porte **cinq pour cent** de l'effort sous obligation
contraignante, et **zéro** sous obligation délibérative — la configuration
historiquement adoptée. **La charge graduée est d'un ordre de grandeur
inférieure à la contraction qu'elle devrait compenser.**

**ET UNE ASYMÉTRIE COMPTABLE A ÉTÉ CORRIGÉE EN COURS DE CONSTRUCTION.** Une
première version comptait la contraction du déficitaire comme un effort sans
compter l'expansion de l'excédentaire comme un avantage. **Ce sont les deux
faces d'un même transfert** : au choc énergétique, cinq cents de contraction
d'un côté, cinq cent quatre-vingt-quatre d'expansion de l'autre. **Ne compter
que la première fait passer un transfert pour un coût unilatéral.**

### CE QUE CELA NE DIT PAS

**Que le mécanisme soit impossible.** Cela dit que **ces paramètres** ne
satisfont ni l'une ni l'autre exigence, **et pourquoi dans chaque cas** — durée
trop courte, taux au lieu de plafond, barème d'un ordre de grandeur trop bas.
**Les seuils sont à fixer, et l'auteur a demandé de ne pas le faire avant ce
modèle.**

**Aucun comportement n'est modélisé** : ni élasticité, ni substitution
d'importations, ni réaction des prix intérieurs, ni capacité productive. **Les
chocs sont imposés, non expliqués.** Et les mouvements de capitaux sont hors
périmètre : ils sont réglementés par A32.


## LA PROMESSE CENTRALE EST RESTREINTE — 2026-09-09, A44

**CE QUE NEMO IMS NE PEUT PAS PROMETTRE, ET L'AUTEUR LE RETIRE.** **Aucune
institution monétaire ne contrôle à elle seule les ressources, les techniques,
les écosystèmes, les États et les comportements humains.** La promesse de
garantir les conditions de la vie sur Terre est donc abandonnée — elle
prolongeait la concession déjà versée à F14 le même jour, et elle la rend
définitive.

**FORMULATION RETENUE, ET ELLE EST FALSIFIABLE :**

> « **NEMO IMS garantit la disponibilité du financement pour les besoins
> essentiels matériellement réalisables, dans les limites écologiques reconnues
> et sous contrôle démocratique.** »

**DEUX ENGAGEMENTS VÉRIFIABLES, ET C'EST TOUT LEUR INTÉRÊT.**

**(1) L'ABSENCE DE FINANCEMENT NE DOIT PAS BLOQUER UNE ACTION ESSENTIELLE
MATÉRIELLEMENT RÉALISABLE.** **Se vérifie par un contre-exemple** : une action
jugée essentielle, physiquement faisable, et qui n'a pas eu lieu faute de
financement alors que le dispositif fonctionnait.

**(2) AUCUNE ÉMISSION NE DOIT FINANCER UNE ACTIVITÉ INCOMPATIBLE AVEC LES
CONTRAINTES ÉCOLOGIQUES RETENUES.** **Se vérifie par un contre-exemple aussi** :
une émission tracée jusqu'à une activité qui franchit une contrainte adoptée.

**CE QUE CETTE RESTRICTION COÛTE, ET CE QU'ELLE GAGNE.** Elle abandonne la
prétention la plus large du projet. **Elle gagne deux énoncés qu'un
contradicteur peut attaquer avec un seul cas**, là où la promesse précédente ne
pouvait ni être tenue ni être réfutée. **Une promesse invérifiable n'est pas une
promesse forte : c'est une promesse absente.**

**ET ELLE DÉPLACE LA CHARGE.** Garantir la DISPONIBILITÉ du financement n'est pas
garantir le RÉSULTAT écologique. **Ce que le dispositif promet désormais, c'est
de ne pas être le facteur bloquant, et de ne pas être le facteur aggravant.** **Le
résultat, lui, dépend des politiques de substitution que F14 a établies
nécessaires et que le dispositif ne contient pas.**

## L'ORDRE DE TRAVAIL — NEUF CHANTIERS, ARRÊTÉ LE 2026-09-09

**(1) Compensation des déséquilibres internationaux** — modèle construit le
2026-09-09, aucune des deux exigences tenue au barème déclaré. **(2) RÈGLE
D'ÉLIGIBILITÉ DES PROJETS** — chantier central, ouvert ce jour sous
`REGLE-D-EMISSION`. **(3) Plafond et rythme de l'émission.** **(4) Réponse à
l'inflation et aux pénuries.** **(5) Gouvernance des décisions et des recours.**
**(6) Porteur juridique et comptable du passif** — A35b, en attente de la revue
humaine. **(7) Destination des prélèvements et de la fonte** — A36. **(8) Modèle
macroéconomique à plusieurs pays.** **(9) Expérimentation limitée avant toute
institution mondiale.**

**CE QUE CET ORDRE ENGAGE.** Les points 6 et 7 sont déjà ouverts et attendent
des tiers ; les points 1 et 2 sont ceux que le corpus peut avancer seul ; **le
point 8 ne doit pas être entrepris avant que 3, 4 et 5 aient une forme**, sans
quoi le modèle macroéconomique modéliserait des règles qui n'existent pas.


## LA COMPENSATION, VERSION 2 — CINQ CORRECTIONS DE L'AUTEUR, 2026-09-09

**LA VERSION 1 AVAIT PRODUIT UN RÉSULTAT UTILE — elle réfutait la version naïve
de la compensation — MAIS TROIS DE SES CONCLUSIONS ÉTAIENT MAL FONDÉES.**

### CE QUI ÉTAIT FAUX, ET LE PLUS GRAVE D'ABORD

**(1) LA CONCLUSION SUR LE CORRIDOR ÉTAIT EN PARTIE TAUTOLOGIQUE.** Les flux
commerciaux étaient fixés indépendamment des charges et des parités : **aucune
taxe ne pouvait donc supprimer leur accumulation, et le modèle retrouvait ce
qu'il avait supposé.** **Avec des échanges élastiques, le solde de l'excédentaire
CULMINE puis REDESCEND** — de 413 à 199 en vingt périodes, contre 779 à flux
rigides. **Le corridor borne, et la version 1 disait le contraire.**

**(2) UN PLAFOND DUR N'EST PAS UN MÉCANISME.** La version 1 le recommandait sans
dire ce qui se passe quand il est atteint. **Trois procédures sont désormais
implémentées, et elles diffèrent** : le blocage est dépassé à CHAQUE période —
vingt sur vingt — le recyclage n'est dépassé que neuf fois, la conversion ramène
le solde de 666 à 274. **Un plafond sans procédure est un nombre, pas un
mécanisme.**

**(3) LES 499 DE CONTRACTION ET 584 D'EXPANSION N'ÉTAIENT PAS RÉCONCILIÉS.**
L'identité stock-flux est désormais vérifiée par pays et par période. **La
réconciliation donne la réponse : l'écart est un EFFET DE PARITÉ.** En unités
NEMO tout se boucle ; en monnaies nationales rien ne se boucle, **parce que les
masses monétaires nationales NE SONT PAS SOMMABLES entre pays**. **La version 1
avait donc tort d'en tirer un « effort » agrégé, et le mot est retiré du
programme.**

**(4) L'HORIZON MASQUAIT LE PROBLÈME.** Allonger la durée de la facilité
repoussait simplement l'échéance hors des huit périodes. **L'horizon est porté à
vingt**, un contrôle vérifie qu'aucun tirage ne subsiste à la fin, **et un report
n'est plus comptabilisé comme une résolution.**

**(5) UNE VARIATION DE MASSE MONÉTAIRE N'EST PAS UN EFFORT RÉEL.** Sont publiés
séparément : contraction, expansion, production, part des importations
essentielles effectivement reçue, transfert réel de ressources. **Aucun n'est
agrégé avec un autre.** **Et la tension inflationniste n'est PAS publiée** : les
prix ne sont pas endogènes, et le corpus ne fabriquera pas un indicateur qu'aucun
mécanisme ne produit.

### LA DÉCISION QUE LE MODÈLE ÉCLAIRE — A45

**L'AUTEUR POSE LA QUESTION ET LA TRANCHE : OUI, une part du soutien aux
importations essentielles doit être DÉFINITIVEMENT NON REMBOURSABLE.**

**LE MODÈLE LE DOCUMENTE, sur choc énergétique STRUCTUREL.** Facilité
remboursable seule : **94 %** des besoins essentiels servis, **567** de
contraction, **204** de dette résiduelle. Facilité **plus** allocation solidaire :
**100 %**, **53** de contraction, **aucune** dette. **Sans allocation, le
dispositif protège temporairement puis restitue la contraction sous forme de
remboursement.**

**ET LA FACILITÉ N'EST PAS INUTILE POUR AUTANT** : sur un choc TEMPORAIRE, elle
suffit seule — cent pour cent. **L'allocation n'est pas une réponse à tout, donc
elle n'est pas une réponse à rien.** **Ce sont deux guichets pour deux natures de
choc, et le test vérifie que chacun tient sur le sien.**

### CE QUE LA SYMÉTRIE VEUT DIRE, ET CE QU'ELLE NE VEUT PAS DIRE

**Les deux côtés ont une OBLIGATION D'AJUSTEMENT. Cela n'exige pas l'égalité
nominale des sacrifices.** La contribution doit dépendre de la capacité, de la
cause du déséquilibre et du caractère essentiel ou non des flux. **La version 1
mesurait un « effort » agrégé et concluait à une symétrie nominale : la mesure
était invalide, et la conclusion est retirée avec elle.**

### CE QUI RESTE OUVERT

**QUI FINANCE L'ALLOCATION** — c'est la question suivante, et elle est politique.
**L'ordre d'intervention proposé par l'auteur** : financement garanti des
importations essentielles ; recyclage d'une partie des excédents ; prélèvements
progressifs sur les positions persistantes ; révision encadrée de la parité ;
restrictions sur les opérations non essentielles ; restructuration ou transfert
collectif lorsque le déficit essentiel est structurel.

**ET LE RISQUE SIGNALÉ PAR L'AUTEUR EST VÉRIFIÉ.** À plafond serré, **retirer le
guichet d'allocation fait bloquer 579 d'importations essentielles contre 145
avec** : un plafond peut bel et bien bloquer le règlement de biens essentiels, et
**c'est le guichet non remboursable qui écarte ce risque**, non le plafond
lui-même.


## LA RÈGLE D'ÉMISSION ET SES SEPT CAS LIMITES — 2026-09-09

**LE CŒUR DE NEMO IMS : qui peut créer combien de monnaie, pour quoi, selon
quelles limites, et avec quel pouvoir d'arrêt.** La règle est construite à trois
décisions séparées, comme l'auteur l'a posée, puis soumise aux sept cas limites
qu'il a nommés. `modeles/nemo_emission.py`, vérifié par
`modeles/test_nemo_emission.py`.

### LES TROIS DÉCISIONS, ET CE QUI LES SÉPARE

**(1) LE VETO PHYSIQUE REFUSE, IL N'AUTORISE JAMAIS.** Le test le vérifie en
déclarant le même projet vital puis indifférent : **le verdict ne bouge pas.**
Deux motifs, et ils ne sont pas de même nature — **une INDISPONIBILITÉ résiste
même à un bilan agrégé** (aucune pondération ne fabrique du lithium qui n'existe
pas) alors qu'**un FRANCHISSEMENT y cède**. C'est cette asymétrie qui rend le
cas 2 décisif.

**(2) LA PRIORITÉ APPARTIENT AU POLITIQUE, ET LE MÉCANISME REND LA MAIN.** Il ne
classe jamais deux besoins essentiels entre eux. Le non-essentiel cède devant
l'essentiel — ce n'est pas un arbitrage entre besoins, c'est la qualification
elle-même.

**(3) LE CALIBRAGE ÉCHELONNE, IL NE REFUSE PAS AU FOND.** Un arrêt monétaire
substantiel rendrait à la monnaie le pouvoir que NEMO lui retire. Le test vérifie
que la demande est servie **intégralement** sur la fenêtre.

### LE POUVOIR D'ARRÊT — TROIS ARRÊTS, UN SEUL INCONDITIONNEL

**ARRÊT PHYSIQUE**, à l'organe d'observation des limites : **inconditionnel**,
non surmontable par une majorité politique — sans quoi ce n'est pas un veto.
**ARRÊT DÉMOCRATIQUE**, à l'institution compétente : **borné**, il ne reprend
jamais une émission non remboursable déjà délivrée. **ARRÊT MONÉTAIRE**, à
l'organe de calibrage : **délai seulement**.

### LES SEPT CAS, ET CINQ METTENT LA RÈGLE EN DÉFAUT

**CAS 1 — ESSENTIEL MAIS INFLATIONNISTE. TRANCHÉ, ET IL RESTREINT A44.** 1100 de
besoin essentiel pour 1000 de capacité : la règle échelonne, sert 91 % à la
première période et tout à la seconde. **« Garantir la disponibilité du
financement » ne peut donc pas vouloir dire « immédiatement » : la promesse vaut
SUR LA FENÊTRE, pas à la date.** Et ce que le programme ne dit pas : que
l'échelonnement était nécessaire. **Il publie un écart de capacité, qui est une
condition NÉCESSAIRE et NON SUFFISANTE d'une tension sur les prix. Les prix n'y
sont pas endogènes, et aucun indicateur d'inflation n'est produit.**

**CAS 2 — ÉCOLOGIQUE MAIS DÉPENDANT D'UNE RESSOURCE RARE. DILEMME NON TRANCHÉ.**
Un parc solaire soulage le carbone de 150 et franchit la biodiversité de 40.
**Veto strict : il est refusé, et la transition est bloquée par le veto censé la
protéger.** Veto agrégé : il passe — **mais seulement parce qu'une limite a été
pondérée contre une autre, ce qu'aucune donnée physique ne fait.** La variante
agrégée n'est donc plus un veto physique, c'est une décision politique déguisée
en mesure. **Le corpus mesure les deux et n'en choisit aucune.**

**CAS 3 — DEUX BESOINS ESSENTIELS. INDÉCIDABLE PAR LE MÉCANISME, et c'est le bon
comportement.** Quatre départages plausibles, **deux gagnants différents** : coût
par bénéficiaire et nombre désignent le logement, gravité et antériorité
désignent l'hôpital. **Choisir le départage EST la décision.** Une règle qui
trancherait ici imposerait silencieusement une théorie du besoin — utilitariste,
agrégative, hiérarchique ou arbitraire selon le départage retenu. **Ce qu'il faut
n'est pas un critère mais une procédure, et elle n'existe pas.**

**CAS 4 — ERREUR DE QUALIFICATION. TRANCHÉ CONTRE LA RÈGLE.** L'argent est versé
et **rien ne le ramène** : les trois procédures testées récupèrent zéro. **Ce
n'est pas une lacune d'implémentation, c'est la contrepartie de l'absence de
dette, qui est le cœur même de NEMO.** Seule la compensation mord, en prenant 960
sur les émissions futures de la même autorité — **l'erreur d'hier est payée par
le bénéficiaire essentiel de demain, qui n'y est pour rien.** Le taux d'erreur
est une hypothèse posée, non une donnée : le programme montre la FORME du coût,
pas son ampleur.

**CAS 5 — CHANGEMENT SCIENTIFIQUE. TENU JUSQU'À UN SEUIL, ET IL RESTREINT A44.**
Un programme régulièrement admis, puis la limite est révisée. **À −40 %, l'arrêt
et la transition ramènent le dépassement à zéro — au prix de 350 et 175
d'émission échouée, c'est-à-dire d'hôpital à moitié construit. À −60 %, plus
aucune procédure ne tient**, parce que le passé n'est pas révisable. **Le second
engagement de A44 doit donc se lire comme une obligation À LA DATE DE LA
DÉCISION** ; sans cela une révision scientifique ORDINAIRE suffit à falsifier la
promesse sans qu'aucune faute n'ait été commise. **Et la contrepartie doit être
écrite — délai, sort des tranches non versées, et QUI PAIE L'ÉCHOUAGE — sinon
« à la date » devient un permis d'ignorer la science postérieure.**

**CAS 6 — URGENCE HUMANITAIRE. BORNÉ, NON FERMÉ.** Un canal d'urgence contourne
les décisions 1 et 2. **15 % de l'émission échappe par construction au veto
physique ; 540 n'auraient pas dû être émis ; zéro récupérable — le même mur qu'au
cas 4.** La ratification postérieure ne reprend rien : elle refuse les tranches à
venir. **Et le plafond d'urgence est un nombre politique : trop bas il laisse
mourir, trop haut il vide le veto. Aucun calcul ne peut le fixer, et le mécanisme
n'a pas d'avis là-dessus.**

**CAS 7 — CAPTURE POLITIQUE DE L'AUTORITÉ. NON DÉTECTÉ. C'EST LE RÉSULTAT LE PLUS
DÉFAVORABLE DU CHANTIER.** L'autorité qualifie une centrale thermique
d'essentielle et déclare une pression carbone de 340 au lieu de 500. **500 sont
détournés, et les cinq contrôles restent au vert.** Le contrôle cumulé E5 a été
ajouté **pour** l'attraper : il mord — la pression déclarée atteint 390 pour 400
de budget — **et la capture se contente de déclarer en dessous. UN CONTRÔLE DE
PLUS DÉPLACE LE MENSONGE, IL NE LE VOIT PAS.**

**Le pouvoir d'arrêt ne rattrape rien**, et il faut le dire précisément :
**l'arrêt physique s'exerce sur une pression DÉCLARÉE**, l'arrêt démocratique
appartient à l'institution captée, l'arrêt monétaire ne porte que sur le rythme.
**Tout contrôle interne porte sur une déclaration.** Ce qu'il faudrait — pression
constatée et non déclarée, registre du besoin tenu hors de l'autorité qui
qualifie, droit de saisine d'un tiers — **n'est pas conçu. Tant que cela n'existe
pas, la garantie de A44 est CONDITIONNELLE À LA PROBITÉ DE L'AUTORITÉ, et cette
condition n'est écrite nulle part dans la promesse.**

### CE QUE LE CHANTIER LAISSE DERRIÈRE LUI

**Six pièces de conception manquantes, chacune nommée par un cas** :
`DEPARTAGE-ESSENTIELS`, `VETO-AGREGATION`, `CORRECTION-D-ERREUR`,
`REVISION-SCIENTIFIQUE`, `PLAFOND-D-URGENCE`, `MESURE-EXTERIEURE`. **F3 est
instruit défavorablement** — le cas 7 est Goodhart en conditions de laboratoire,
produit par le corpus contre lui-même. **F7 est déplacé, non traité** : le
pilotage devient une question de rythme et non d'objet, et **si ce rythme est
pilotable n'est pas répondu.** **F13 reçoit sa face physique** avec
`VETO-AGREGATION`.

**ET IL FAUT REDIRE CE QUE CE PROGRAMME NE FAIT PAS.** Il n'établit pas que la
règle soit bonne. Un programme qui applique une règle prouve qu'il l'applique,
jamais qu'elle est fondée. **Les projets sont fictifs, aucun seuil n'est calibré,
et les cinq mises en défaut sont des mises en défaut DE LA RÈGLE, pas des
incidents du programme.**


## LA RÈGLE D'ÉMISSION, VERSION 2 — QUATRE CORRECTIONS DE L'AUTEUR, 2026-09-09

**LES SEPT CAS LIMITES ÉTAIENT UTILES ET DEUX DE LEURS CONCLUSIONS ÉTAIENT
FAUSSES.** Elles l'étaient dans le même sens — celui de l'impuissance — et cela
mérite d'être noté : **un corpus qui cherche les échecs peut aussi en inventer.
C'est la faute symétrique de la complaisance, et elle n'est pas moins grave.**

### LES QUATRE CORRECTIONS

**(1) « LE CAS 7 NE SE RÉPARE PAS » ÉTAIT FAUX.** Un contrôle qui ne porte que
sur des DÉCLARATIONS ne détecte pas leur falsification — cela reste vrai. Mais
**la capture ne s'élimine jamais avec certitude ET SE DÉTECTE** : données
satellitaires, mesures indépendantes, traçabilité des matières, audits
aléatoires, pluralité des experts, publication des données, lanceurs d'alerte,
recours juridictionnels.

**(2) « L'ABSENCE DE REPRISE EST LA CONTREPARTIE DE L'ABSENCE DE DETTE » ÉTAIT
FAUX.** Non remboursable veut dire qu'un bénéficiaire **conforme** ne rembourse
pas. Cela n'interdit ni la récupération des sommes **inutilisées**, ni le gel des
tranches **futures**, ni la restitution pour **erreur manifeste**, ni le
recouvrement pour **fraude**, ni la responsabilité personnelle des dirigeants
fautifs. **A45 protège le bénéficiaire LÉGITIME contre l'endettement ; il ne crée
aucune irrévocabilité au profit d'un bénéficiaire INDU.**

**(3) LA CONTRAINTE PHYSIQUE N'EST PAS SON CONSTAT INSTITUTIONNEL.** Une loi
physique ne se vote pas ; une estimation de stock de lithium, de pression
environnementale ou de seuil reste **incertaine, révisable et contestable**.
**Donner un veto incontestable à l'organisme qui produit l'estimation créerait
exactement la capture du cas 7.** Le modèle sépare désormais partout la valeur
VRAIE de la valeur CONSTATÉE, et la première s'applique au monde que la seconde
ait vu juste ou non.

**(4) F3 N'EST PAS VALIDÉ EMPIRIQUEMENT.** Le cas 7 établit une **vulnérabilité
logique**, non une observation. La formulation retenue est « vulnérabilité
instruite, cas théorique défavorable établi ».

### A46 — CINQ FONCTIONS SÉPARÉES, VALIDÉ PAR L'AUTEUR LE 2026-09-09

**Dans sa formulation, qui est plus large que la première rédaction du corpus :**

1. **MESURE SCIENTIFIQUE** des ressources, pressions physiques, limites
   écologiques **et incertitudes** ;
2. **QUALIFICATION** des **projets** et des besoins essentiels ;
3. **PRIORITÉ DÉMOCRATIQUE** entre les projets **admissibles** ;
4. **CALIBRAGE** du montant, du rythme et des **tranches** de l'émission ;
5. **CONTRÔLE, SUSPENSION, CORRECTION, RÉCUPÉRATION ET RECOURS.**

**« Aucune autorité ne peut cumuler la mesure physique, la qualification, la
priorité, l'émission ET SON PROPRE CONTRÔLE. »**

**PREMIÈRE CORRECTION DE PORTÉE — CINQ FONCTIONS N'EST PAS CINQ
INSTITUTIONS.** A46 exige **cinq centres de responsabilité indépendants** :
mandats, nominations, budgets et responsabilités séparés. Qu'ils soient cinq
personnes juridiques distinctes ou cinq organes indépendants d'une même
organisation internationale est une **modalité encore ouverte**. Le corpus
n'impose pas une bureaucratie de cinq institutions obligatoirement distinctes ;
il exige l'indépendance, pas le siège.

**SECONDE CORRECTION DE PORTÉE — INTERDIRE L'AUTOCONTRÔLE N'EST PAS INTERDIRE
L'AUTOCORRECTION.** L'autorité monétaire **doit** pouvoir suspendre
immédiatement un versement qu'elle estime erroné ; la lui interdire ferait durer
l'erreur au nom de la séparation des pouvoirs. Ce qu'elle ne peut pas, c'est
**être l'unique ou le dernier juge de la régularité de son propre acte**, ni
clore seule le contentieux. **Trois niveaux se distinguent** : contrôle interne
immédiat avec capacité de suspension ; contrôle indépendant de conformité ; audit
externe et recours juridictionnel.

**S3 A ÉTÉ RÉÉCRIT SUR CE POINT.** Il ne signale plus toute intervention d'une
institution sur son propre acte, mais trois choses : qu'un contrôle de
**conformité indépendant** a eu lieu ; que la **clôture** n'est pas le fait d'un
auteur ; qu'une **voie de recours extérieure** existe, tenue par une institution
distincte de l'auteur et du contrôleur de conformité. **La suspension
conservatoire par le payeur ne déclenche rien**, et le test le vérifie
explicitement.

**ET S3 RESTE DISTINCT DE S1.** Le non-cumul se lit sur l'organigramme ; l'unicité
du juge se lit sur le dossier. Un dispositif peut satisfaire l'une et violer
l'autre — la sortie du programme le montre sur trois dossiers.

**PROVENANCE — UNE FORMULE QUI N'A PAS ÉTÉ ADOPTÉE.** « La réalité physique
demeure contraignante ; son constat institutionnel reste motivé, documenté,
pluraliste, révisable et susceptible d'un recours indépendant. » Cette phrase
accompagnait la validation d'A46 **sans en faire partie**. Elle est cohérente
avec A46, mais l'auteur ne l'a pas expressément adoptée : `VETO-SCIENTIFIQUE-
PLURALISTE` reste donc **orienté et non tranché**, et la décision porte la
mention « formule proposée, non adoptée ».

**Le contrôle S1 le vérifie sur la structure**, et c'est le point : la version 1
cherchait la capture dans la SORTIE du dispositif, qui restait verte. **La
version 2 la voit dans la STRUCTURE DE L'INSTITUTION.** Le contrôle S2 vérifie
les neuf états — proposé, physiquement admissible, politiquement prioritaire,
financièrement programmé, versé par tranches, contrôlé, achevé, suspendu,
récupéré — et refuse deux fautes : **un versement qui saute la priorisation
politique**, et **une admissibilité physique déclarée par l'autorité de
qualification**. La seconde est très exactement ce que le cas 7 exploitait.

### LES SEPT CAS REJOUÉS AVEC LEUR MÉCANISME

**CAS 1 — DÉLAI MAXIMAL ET CALENDRIER PUBLIC.** Le délai **rend A44
falsifiable** : sans lui, « la disponibilité est garantie » n'a pas de démenti
possible, tout retard se lisant comme un échelonnement. Avec lui, le scénario à
capacité serrée est un **manquement public** — quatre périodes pour un engagement
de trois. **Le calendrier doit être publié d'avance**, sinon il se réécrit après
coup.

**CAS 2 — ARBITRAGE DE PORTEFEUILLE, ET LE RÉSULTAT EST RETOURNÉ.** La version 1
disait le veto trop strict. **Il est aussi TROP PERMISSIF** : trois usages admis
isolément demandent **105 de lithium pour 100 disponible**, aucun ne franchissant
seul ce que les trois franchissent ensemble. L'arbitrage de portefeuille borne à
**six lots faisables**, le meilleur soulageant **260**. **Et il ne sauve pas le
projet qui franchit seul** : le veto garde son rôle de refus.

**CAS 3 — PROCÉDURE DE DÉPARTAGE.** Quatre départages, deux gagnants : le choix
du départage reste la décision. **Ce que la version 2 ajoute n'est pas un critère
mais une SAISINE** — instance nommée, motif publié, **recours devant un organe
distinct de celui qui tranche**, réexamen daté du perdant. **La procédure ne dit
pas qui gagne et ne le doit pas ; elle rend la décision traçable et attaquable.**

**CAS 4 — TRANCHES, GEL ET RESTITUTION.** **82 % sauvés** en détection à la
première tranche, **30 %** à la quatrième, **55 %** à la quatrième en cas de
fraude établie. **Le gel est compté à part de la restitution** : l'argent jamais
versé n'est pas de l'argent revenu, et les confondre gonflerait le rendement de
la procédure. **Ce qui reste vrai : la part déjà employée ne revient qu'à 35 %,
et seulement pour fraude.**

**CAS 5 — RÉEXAMEN PÉRIODIQUE DES AUTORISATIONS.** À −40 %, le dépassement tombe
de **120 à zéro** ; à −60 %, de **200 à 80**. **L'autorisation devient
révocable.** Ce qui résiste est la pression déjà émise : **le réexamen borne le
dommage futur, il ne répare pas le passé.** Et son pas est un arbitrage — trop
court, il finance mal un ouvrage long.

**CAS 6 — RÉSERVE PRÉDÉFINIE À EXPIRATION AUTOMATIQUE.** **65 %** du montant
révélé inadmissible sont sauvés au contrôle rapide. Trois propriétés non
facultatives : **prédéfinie**, sinon elle se redéfinit à chaque urgence ;
**expirante**, sinon elle devient un guichet permanent sans veto ; **contrôlée
vite**, car les tranches ne sauvent que ce qui n'est pas parti. **Le plafond reste
un nombre politique qu'aucun calcul ne fixe.**

**CAS 7 — MESURE EXTÉRIEURE, PLURALITÉ, AUDIT.** Le résultat central de la
version 2. **Sous une règle à organisme unique, UNE capture suffit** ; sous la
médiane, **trois** ; sous la règle prudente, **les cinq — mais elle refuse à tort
trois projets légitimes sur cinq**. **LA MÉDIANE AVEC RECOURS DOMINE LES DEUX** :
cinq captures nécessaires, **aucun refus à tort**, parce qu'**une capture
PARTIELLE crée de la divergence, et que la divergence saisit la mesure
extérieure. Le désaccord des experts devient l'alarme au lieu d'être le
problème.** La mesure physique directe détecte dès la première période mais ne
couvre que 60 % des projets ; l'audit couvre tout et arrive à la troisième. **Et
la détection précoce récupère 89 % contre 54 % en détection tardive.**

### LE DILEMME QUI RESTE, ET IL EST NOMMÉ

**Comment donner aux connaissances physiques un pouvoir réellement contraignant
sans donner un pouvoir absolu aux experts qui les interprètent ?** La réponse
posée par l'auteur — **veto pluraliste, motivé, public, révisable, susceptible de
recours, la contrainte physique demeurant infranchissable** — est celle que le
modèle mesure et qu'il trouve dominante. **Le trou restant est nommé par le
modèle lui-même : une collusion UNANIME ne diverge pas, donc ne déclenche rien.**

**ET CE QUI N'A PAS BOUGÉ.** Un contrôle qui ne porte que sur des déclarations ne
détecte pas leur falsification. Le passé n'est pas révisable. Aucun critère neutre
ne départage deux besoins essentiels. **Les prix ne sont toujours pas endogènes :
l'écart de capacité publié au cas 1 est une condition nécessaire et NON
SUFFISANTE d'une tension inflationniste, et aucun indicateur d'inflation n'est
produit.**


## LE RECOURS N'ÉTAIT PAS UN INSTRUMENT, C'ÉTAIT UN ORACLE — 2026-09-09

**LA VERSION 2 A CONCLU TROP FORT À SON TOUR, ET DANS L'AUTRE SENS.** Elle
publiait que la règle « médiane avec recours » dominait toutes les autres : cinq
captures nécessaires, aucun refus à tort. **Ce résultat était un artefact.** Dans
le programme, dès que la divergence entre organismes dépassait le seuil, la règle
rendait **la valeur vraie de la simulation** — elle possédait gratuitement ce
qu'aucun dispositif réel ne possède. L'auteur l'a relevé le jour même.

**LE RECOURS EST DEVENU UN CANAL DE MESURE INDÉPENDANT** — et le mot compte,
l'auteur ayant corrigé « observation physique directe » qui restait trop fort.
Ce à quoi ce canal accède est nommé : une information — imagerie, traçabilité
des matières, relevés de terrain — **qui ne passe ni par la déclaration du
porteur ni par les modèles des organismes**. C'est là son apport réel. **Mais ce
n'est pas une observation directe de la vérité** : un satellite, un capteur, une
analyse matière dépendent d'un **étalonnage**, d'un **traitement** et parfois
d'un **modèle**. **Aucun instrument ne possède la vérité** — il a sa méthode, sa
marge d'erreur et son risque de capture propres, et c'est pourquoi son biais est
déclaré dans le programme comme celui des organismes.

**ET LE RÉSULTAT PUBLIÉ TOMBE.**

| règle de constat | captures nécessaires | refus à tort sur 5 | cibles |
|---|---|---|---|
| unique | 1 | 0 | un organisme |
| médiane | 3 | 0 | trois organismes |
| prudente | 5 | 3 | tous les organismes |
| médiane avec recours | **2** | 0 | un organisme, puis l'instrument |
| recours pluriel | 3 | 0 | un organisme, deux instruments |

**UN RECOURS À INSTRUMENT UNIQUE DÉPLACE LE POINT DE DÉFAILLANCE, IL NE LE
SUPPRIME PAS** : capter un organisme fait diverger, et capter l'instrument saisi
suffit ensuite à museler l'alarme — **deux captures, contre trois pour la simple
médiane.** Le mécanisme qui paraissait le plus robuste était en réalité le
deuxième plus fragile.

**CE QUI LE RÉTABLIT EN PARTIE : PLURALISER LE RECOURS LUI-MÊME.** Trois
instruments indépendants en médiane portent l'exigence à **trois captures**, sans
aucun refus à tort. **La règle prudente reste la plus résistante — cinq captures
— au prix de trois refus à tort sur cinq projets légitimes.** Aucune règle n'est
gratuitement supérieure.

**LE DILEMME DE L'AUTEUR N'EST DONC PAS LEVÉ, IL EST DÉPLACÉ D'UN CRAN.** La
pluralité protège **tant qu'elle porte aussi sur les canaux du recours**, et le
désaccord des experts ne sert d'alarme **que si ce qu'il déclenche n'est pas
capturable d'un seul coup.**

**ET CES NOMBRES SE LISENT POUR CE QU'ILS SONT.** Le nombre minimal de captures
est une **propriété structurelle de l'architecture simulée**. Il ne mesure **ni
la probabilité d'une capture ni son coût**. Corrompre deux organismes
scientifiques indépendants peut être bien plus difficile que compromettre cinq
capteurs de même modèle — ou bien plus facile. Le programme compare des
architectures **à effort de capture supposé égal**, ce qu'aucun dispositif réel
ne garantit.

**UN CONTRÔLE DE MÉTHODE A ÉTÉ AJOUTÉ AU TEST** pour que cette faute ne puisse
pas revenir : il échoue si la mesure de recours rend la valeur vraie. Le corpus a
maintenant deux gardes symétriques — l'un contre l'invention d'échecs, l'autre
contre l'invention de solutions.


## A47 — DÉCIDER SOUS INCERTITUDE. RÈGLE PROPOSÉE, NON ADOPTÉE

**Ouvert le 2026-09-09. La règle ci-dessous est celle que l'auteur propose ; elle
n'est pas encore arbitrée, et le corpus ne la traite pas comme acquise.**

1. **Matériellement impossible** : refus.
2. **Risque grave, irréversible et suffisamment établi** : refus ou suspension.
3. **Incertitude importante portant sur un dommage potentiellement
   irréversible** : suspension provisoire et acquisition de connaissances.
4. **Risque limité et réversible** : autorisation par tranches, surveillance et
   capacité d'arrêt.
5. **Besoin essentiel urgent** : autorisation minimale et temporaire, sauf
   impossibilité physique ou risque catastrophique suffisamment établi.
6. **Ressource rare** : arbitrage au niveau du portefeuille des usages
   concurrents.
7. **Recours** : examen par une instance indépendante, sur la base de données ou
   de méthodes supplémentaires.

**Et une règle sur l'effet du recours :** un recours **ne suspend pas
automatiquement** une mesure protégeant contre un dommage irréversible ; il peut
cependant la **réviser rapidement** si les nouvelles preuves modifient le
constat.

**CE QUE CETTE RÈGLE ARTICULE AVEC CE QUI PRÉCÈDE.** Le point 1 est le veto
physique. Le point 6 est l'arbitrage de portefeuille du cas 2. Le point 4 est le
versement par tranches du cas 4. Le point 5 est la réserve d'urgence du cas 6. Le
point 7 est le troisième niveau de contrôle de S3. **Les points 2 et 3 sont
neufs, et c'est là que se trouve la difficulté** : « suffisamment établi » et
« incertitude importante » sont des seuils de preuve, non des faits, et le corpus
n'en a aucun. **Ils ne sont pas modélisés, et ne doivent pas être inventés.**


## A47 — DÉCIDER SOUS INCERTITUDE. ARBITRÉ DANS SON PRINCIPE LE 2026-09-09

**LA DOCTRINE, DANS LES TERMES DE L'AUTEUR — PRÉCAUTION PROPORTIONNÉE.**

1. Toute décision distingue **gravité, étendue, réversibilité et urgence**.
2. **L'incertitude ne produit automatiquement ni autorisation ni refus.**
3. Risque plausible de dommage **grave et irréversible** : le **porteur** doit
   établir une compatibilité suffisante.
4. Risque **limité et réversible** : autorisation par tranches et sous
   surveillance possible ; **l'autorité doit motiver tout refus**.
5. **Besoin essentiel urgent** : la solution réalisable la moins risquée, en
   quantité minimale, avec réexamen rapide.
6. **Ressources rares** : arbitrage au niveau du portefeuille des usages
   concurrents.
7. **Données, méthodes, incertitudes, seuils normatifs et avis minoritaires
   sont publics.**
8. Le **recours** repose sur des examinateurs et des **canaux de mesure
   indépendants**, qui conservent leurs propres marges d'erreur.
9. Les **seuils propres à chaque domaine sont fixés AVANT l'examen des
   dossiers**, publiés et périodiquement révisés.

**CE QUE CETTE DOCTRINE FAIT, ET C'EST SON MÉRITE PRINCIPAL : elle n'arrête
aucun seuil numérique.** Elle répartit la **charge de la preuve** et définit la
**procédure** par laquelle les seuils seront établis. Les seuils sectoriels
restent ouverts à l'expertise scientifique et à la décision démocratique.

**MISE À L'ÉPREUVE — `modeles/nemo_a47.py`, vérifié par
`modeles/test_nemo_a47.py`.** Six dossiers fictifs, quatre régimes.

### CE QUE LA DOCTRINE TIENT

**LE POINT 2 EST TENU, et c'est ce qui la rend applicable sans chiffre.**
L'incertitude ne produit ni autorisation ni refus automatiques : **elle déplace
la charge de la preuve.** C'est une règle de procédure, non une règle de fond.

**LE POINT 9 MORD, ET LE PROGRAMME LE MONTRE.** Selon que le seuil de
plausibilité est publié d'avance ou choisi après lecture des dossiers, le nombre
de dossiers mis à la charge du porteur passe de **2 à 0** — si l'on veut tout
admettre — ou **à 3** si l'on veut tout refuser. **Les trois seuils sont dans la
même plage de valeurs plausibles, et rien dans le dossier ne distingue un seuil
de principe d'un seuil taillé sur mesure. Fixer le seuil d'avance est ce qui en
fait une contrainte plutôt qu'une description.**

**Mais le point 9 ne se suffit pas** : « périodiquement révisés » rouvre la main
à chaque révision. Ce qui protège est la fixation **plus** la publication **plus**
le fait que la révision ne s'applique pas au dossier en cours. **La troisième
condition manque.**

**LES POINTS 6, 7 ET 8 sont tenus** : l'arbitrage de portefeuille est déjà
construit et mesuré ; la publicité est contrôlée et non déclarée — et **sans les
incertitudes publiées le point 3 est inapplicable, sans les avis minoritaires la
divergence entre organismes disparaît du dossier alors qu'elle est l'alarme** ;
le recours instrumenté est acquis, et le contrôle de méthode qui interdit
l'oracle est en place.

### LES DEUX TROUS, ET ILS SONT DANS LA SORTIE

**TROU 1 — LA QUALIFICATION DÉCIDE DE L'ISSUE, ET LA DOCTRINE NE DIT PAS QUI
L'OPÈRE.** Sur le stockage géologique de CO2, deux lectures **également
défendables** de la réversibilité — réversible sur cinquante ans, irréversible à
l'échelle humaine — font basculer la charge de la preuve **de l'autorité au
porteur**, et l'issue probable avec elle. **La doctrine répartit la charge après
une classification dont elle ne règle ni l'auteur ni la procédure.** Ce n'est pas
un détail de rédaction : **y placer l'autorité qui qualifie ramène la capture du
cas 7 ; y placer l'organisme de mesure lui donne la souveraineté que A46 lui
refuse**, car « réversible à quel horizon » est un choix normatif, non une
mesure. Pièce ouverte : `QUALIFICATION-DU-RISQUE`.

**TROU 2 — LES POINTS 3 ET 4 NE PARTITIONNENT PAS L'ESPACE.** Deux dossiers sur
six n'en relèvent ni l'un ni l'autre : **grave mais réversible** — un pesticide à
large spectre — et **irréversible mais peu plausible** — une mine de lithium. **La
charge de la preuve n'y est attribuée à personne, et ce sont les cas ordinaires.**
Pièce ouverte : `ZONE-INTERMEDIAIRE`.

### UNE CONTRADICTION À LEVER

**Les points 3 et 5 s'appliquent ENSEMBLE au dossier urgent** — un traitement
essentiel en épidémie, grave et irréversible — **avec des instructions
contraires** : l'un refuse tant que le porteur n'a pas établi la compatibilité,
ce qu'une incertitude non levée lui interdit par construction ; l'autre accorde
provisoirement parce que le besoin n'attend pas. **La rédaction du 2026-09-09 a
laissé tomber l'exception « sauf impossibilité physique ou risque catastrophique
suffisamment établi » que portait la version précédente.** Le programme applique
le point 5 et **signale que c'est un choix d'implémentation, non une lecture du
texte.**

**ET « LA SOLUTION LA MOINS RISQUÉE » SUPPOSE UN ORDRE.** Trois options
réalisables aux profils incomparables — grave et étroit, léger et très large,
moyen et irréversible — donnent **trois gagnants différents** selon qu'on
ordonne par gravité, par étendue, par réversibilité ou par produit. C'est la
même frontière qu'au cas 2 de la règle d'émission : **une pondération entre
dimensions incommensurables, que la doctrine ne peut pas fournir et ne doit pas
prétendre fournir.**

### CE QUE CETTE MISE À L'ÉPREUVE NE DIT PAS

**Elle ne dit pas que la doctrine est mauvaise** : elle tient sur cinq de ses
neuf points, et ses deux trous sont des **pièces manquantes**, non des
contradictions internes. **Elle ne dit pas non plus qu'elle est bonne** : aucun
seuil n'est éprouvé, aucun dossier n'est réel, et **un programme qui applique une
règle ne la valide jamais.**
