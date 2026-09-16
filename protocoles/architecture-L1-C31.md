# Architecture conceptuelle de L1.C31 — validée et complétée

**Établie le 2026-09-11 par Claude, sur la directive de l'auteur, selon la
méthode éprouvée sur L1.C08 puis L1.C07.** Ouverture en lecture seule : le
chapitre n'est pas modifié, rien n'est commité, aucune réécriture n'est
engagée avant validation de cette architecture. Le document porte l'état du
chapitre, l'examen de ses deux sources et de ce qui doit les remplacer, la
table de ses affirmations, ses dépendances envers A35b et les autres objets du
registre, les écarts relevés, la structure proposée, les décisions à
arbitrer et la séquence.

Ce que cette note n'est pas : un audit contradictoire. L'audit sera conduit
par un modèle tiers sur dossier transmis par l'auteur, après la réécriture,
comme pour L1.C08 et L1.C07.

## 1. État du chapitre au 2026-09-11

**En-tête.** Statut `brouillon`, `revision_de_fond` 2026-09-09, régime
`conception`, `autorite: preparatoire`, `citable: false`. Deux sources, toutes
deux `a_requalifier` (occurrences du manifeste, file D « sans orientation »,
sans trace). Cinq entrées en `verifications_en_attente`. Cinq concepts
déclarés, tous présents au vocabulaire. Neuf renvois. État enregistré :
initialisation tardive du 2026-09-10, jamais qualifiée depuis.

**Origine.** L1.C31 n'a pas été acquis du livre : il a été écrit par le corpus
le 2026-09-09 en réponse au falsifieur F10 (la superfluité), sur arbitrage de
l'auteur, puis corrigé le même jour. Les motifs des corrections sont dans
`protocoles/passe-2.md`, section « Sept corrections de l'auteur sur
l'argument F10 » (neuf sous-sections numérotées). Le fichier a été renommé,
l'identifiant conservé. Le chapitre expose l'état corrigé et lui seul, mais
il conserve dans son corps le récit de ses propres corrections (« ce chapitre
l'avait commise », « ce chapitre avait écrit », « la première version en
omettait deux »), ce que la règle « où vit l'historique d'une correction »
réserve à passe-2.

**Ce qu'est le chapitre.** Un enregistrement d'arbitrage. Il ne porte aucune
source documentaire propre : la proposition centrale, la condition de
démonstration, la condition d'échec, la règle du « réalisable », la partition
des comparateurs et les trois voies de preuve sont des décisions de l'auteur
du 2026-09-09 ; les objections du § 5 sont empruntées à des chapitres du
Livre 18 qui les tiennent d'une évaluation intergouvernementale, avec quatre
citations en anglais reproduites textuellement.

**Ce qui le cite.** Dans le corps d'autres chapitres : L1.C08 (§ 7 et § 8,
`verifie`), qui renvoie à lui pour la proposition corrigée et pour la mesure
de l'apport du dispositif ; L19.C10 (§ sur la disponibilité des ressources
réelles). Dans le registre : A35b, A43, A44, F10, REGLE-D-EMISSION et
OPERATIONNALISATION-INSOLVABLE le portent dans `chapitres`. Aucune promesse du
registre des promesses ne le vise. Passe-2 le nomme dans la synthèse F10 :
« L1.C31 en donne le test ; le portefeuille concurrent n'est pas construit. »

**Ce qu'il cite sans le déclarer.** Le corps renvoie à [L18.C19, L24.C07],
absents de `renvois` ; inversement L11.C30, L13.C01 et L25.C07 sont déclarés
en `renvois` et jamais appelés dans le corps.

**Style.** Passe de septembre : gras et capitales sur la quasi-totalité des
phrases. Même nettoyage que pour L1.C07, sans changement de sens.

**Le troisième chapitre pilote.** Passe-2 (§ 9 des corrections F10) consigne
l'arbitrage de l'auteur du 2026-09-09 : la structure de
`verifications_en_attente` n'est pas modifiée, « les trois chapitres pilotes
diront si le champ doit ensuite être séparé entre vérifications factuelles,
objections non résolues et dettes de conception ». L1.C31 est le troisième
pilote, et son cas est net : aucune de ses cinq entrées n'est une
vérification factuelle (§ 2.3 ci-dessous). Il fournit donc la pièce que cet
arbitrage attendait.

## 2. Sources

### 2.1 Les deux entrées actuelles ne sont pas des sources documentaires

| Réf. | Entrée actuelle | Ce que c'est | Sort proposé |
|---|---|---|---|
| S1 | « L'auteur du corpus, arbitrage du 2026-09-09 et correction du même jour » — `theorie`, `a_requalifier` | Une décision de l'auteur. Le lieu d'une décision est le registre (`corpus/arbitrages.yaml`) et son `texte` ; la convention réserve `sources_primaires` aux « sources documentaires » (§ 6) et fixe cinq natures qui supposent un document. | **Retirer** de `sources_primaires`, comme S7 de L1.C08 (précédent : le contrôle admet le retrait d'une occurrence du manifeste). **Remplacer** par une entrée du registre qui porte la proposition, les deux conditions et la règle du réalisable, et que le texte cite par son identifiant (§ 4.4). |
| S2 | « Le corpus lui-même — L18.C27, L18.C29 et L18.C30 ; L18.C26 ; L1.C15 ; L10.C06 » — `theorie`, `a_requalifier` | Six chapitres du corpus. Ce sont des `renvois`, déjà tous déclarés. | **Retirer.** Les six restent en `renvois`. Ce que le chapitre reproduit textuellement de ces chapitres doit être porté par la source documentaire qu'ils tiennent (§ 2.2), règle appliquée à L1.C08 pour Cottin-Euziol et Sersiron. |

Le retrait des deux entrées et l'inscription des sources documentaires
suivent le précédent de L1.C08 ; `a_requalifier` ne peut pas servir à une
entrée nouvelle (convention § 4, E-L6).

### 2.2 Les sources documentaires que le chapitre doit porter lui-même

Les quatre citations du § 5 et la partition des comparateurs du § 4
proviennent de deux chapitres du rapport d'évaluation méthodologique de
l'IPBES sur les valeurs diverses de la nature (2022). Les deux fichiers sont
sur le disque, acquis le 2026-09-08 (`Documents/Codex/2026-09-08/acquisitions-claude/`),
avec couche de texte. Les passages ont été retrouvés mécaniquement le
2026-09-11 et lus dans le texte autour de chaque occurrence.

**S-IPBES-6 — chapitre 6.** *Policy options and capacity development to
operationalize the inclusion of diverse values of nature in decision-making*,
auteurs principaux coordonnateurs Eszter Kelemen, Suneetha M. Subramanian,
Barbara Nakangu ; « final text version of Chapter 6 » (note 1 de la première
page) ; 146 pages PDF ; folio imprimé = page PDF − 4 (relevé sur les folios
15 à 23) ; DOI porté en tête du fichier : `doi.org/10.5281/zenodo.6522359`,
**à résoudre avant inscription comme `url`** ; empreinte SHA-256
`04acb9622d7333f6da12d94209e5c7da8efc8b82025f28b4992ca76f180c2cda`
(5 218 704 octets). Les entrées du Livre 18 ne portent pas d'URL.

| Citation reproduite par L1.C31 | Page imprimée | Antécédent exact dans le texte |
|---|---|---|
| « lower transaction costs compared to payments for ecosystem services as the existing fiscal system can be used for the transfers (i.e., no new allocation system is generated in most cases) » | 21 | Les transferts fiscaux écologiques, comparés aux paiements pour services écosystémiques (renvoi à Ring 2008, Ring & Barton 2015, Schröter-Schlaack et al. 2014). |
| « These instruments follow a more focused, market-oriented logic, and do not offer stimulus for institutional change or adaptive governance. » | 22 | « These instruments » = les phrases précédentes : permis échangeables, compensations de biodiversité, taxes et redevances liées à la biodiversité, produits dérivés et contrats à terme sur matières premières. **Non** les paiements pour services écosystémiques, les transferts fiscaux ni les subventions. |
| « but are insufficient to shift the current economic paradigm to one which is more aware of other values of nature » | 23 | Des « actions de court terme » s'appuyant principalement sur ce « troisième groupe », exemples cités : suppression des subventions dommageables, normes relevées pour l'investissement privé vert, bonus-malus dans la fiscalité environnementale. |
| « has also been observed to contribute to a recentralisation of forest governance by bringing forests under renewed forms of government control » | 22 | REDD+ (réduction des émissions dues à la déforestation), avec quatre références. |

Pages 28 à 34 (sous-sections 6.2.2.3 à 6.2.2.5) pour la liste des
mécanismes d'autorité et de consentement du § 4, lues par L18.C30 ; à relire
dans le texte lors de la réécriture si le § 4 les conserve nommément.

**S-IPBES-4 — chapitre 4.** *Value expression in decision-making*, 141 pages
PDF ; folio imprimé = page PDF − 6 ; empreinte SHA-256
`ce017dd05c69391463a36d6a812e69fe6edfe2c1e5a8a314fb3e84852c0dd42f`. Résumé
exécutif, page 1 : « higher for the targets that are typically within the
mandate and resources of a ministry of environment […] than for targets that
require cross-sectoral cooperation and co-investment » et « Compliance
mechanisms beyond good intentions are still lacking ». Page 28 du corps ajoute
« One reason for limited progress may be the lack of compliance mechanisms »,
formulé comme une raison possible. Nécessaire seulement si l'objection 4 du
§ 5 reste portée comme un fait ; sinon un renvoi à L18.C26 suffit.

**Ce qu'aucune source ne porte, et qui n'en demande pas.** La proposition
centrale, les deux conditions, la règle du réalisable, la partition des
comparateurs et les trois voies de preuve sont des décisions ; elles se
citent par l'identifiant du registre, non par une source. Le cas chiffré de
F10 (PNUE, *State of Finance for Nature 2026*) vit en L18.C09 et n'est pas
repris par le chapitre.

### 2.3 Les cinq entrées de `verifications_en_attente`

Aucune n'est une tâche de vérification factuelle au sens de la règle arrêtée
sur L1.C08.

| n° | Entrée | Nature réelle | Destination proposée |
|---|---|---|---|
| 1 | La proposition n'est pas établie ; aucun énoncé n'est mesuré | Limite constitutive du chapitre | Corps (§ portée), résumé, bloc commenté de l'en-tête |
| 2 | Le meilleur portefeuille réalisable n'est pas construit ; cinq grandeurs non tenues ; « acquisition de rang 1 » | Dette de conception et programme de recherche | Pièce de conception au registre (§ 4.4) ; corps ; bloc commenté |
| 3 | La règle du « réalisable » est arrêtée et appelle un travail non fait ; deux portefeuilles à construire | Même dette ; contient en outre un écart interne (§ 5, écart 2) | Même pièce ; corps |
| 4 | Le coût propre du dispositif n'est pas évalué, et une source le désigne comme décisif | Limite, dimension « coût social total » de la même dette | Corps (objection 1) ; même pièce |
| 5 | Le troisième énoncé dépend d'A35b, ouvert | Dépendance envers un arbitrage ouvert, déjà inscrite au registre (A35b porte L1.C31) | Corps (§ énoncés et § portée) ; bloc commenté |

Ce qui reste comme vérification factuelle après la réécriture : la
localisation des citations IPBES (faite le 2026-09-11, à refaire par script
sur le texte réécrit) et la résolution du DOI. La liste peut donc être vidée
sans qu'aucune limite ne disparaisse, à la condition que chacune reste
visible.

## 3. Table des affirmations du chapitre actuel

Régime : `E` = `::etat::`, `H` = `::hypothese::`, `N` = `::norme::`.
Appui : `D` = décision de l'auteur (registre), `S` = source documentaire,
`R` = renvoi interne, `I` = inférence du corpus, `∅` = aucun.

| n° | § | Affirmation | Régime actuel | Appui actuel | Appui disponible | Proposition |
|---|---|---|---|---|---|---|
| 1 | intro | F10 « s'est déplacé trois fois » entre le 8 et le 9 septembre, contre le dispositif | E | R (L18.C19, L18.C27, L24.C07, dont deux hors `renvois`) | passe-2, falsification.md | **Retirer** : chronique du corpus ; une phrase de provenance suffit |
| 2 | intro | « la mesure existe, la descente jusqu'au produit est outillée » | E | ∅ | aucun dans le chapitre | **Retirer** : affirmation sur le barème, sans appui ici |
| 3 | intro | Le chapitre enregistre la forme corrigée, la décompose, l'expose à la réfutation ; il ne l'établit pas | E | D | identifiant du registre | Conserver, comme ouverture |
| 4 | 1 | La création monétaire produit du pouvoir d'achat, ni travail, ni énergie, ni matériaux, ni capacités productives | E [S1] | D | L1.C07 § 1 (`verifie`) : la création est une écriture ; L1.C05 : définition de `creation_monetaire` | Conserver en E, appuyé sur L1.C07 et L1.C05 ; ce n'est pas une décision mais une conséquence de la définition |
| 5 | 1 | Trois conséquences : finançable sans être réalisable ; financement par retrait à d'autres usages ; ce qui se mesure | H | I | — | Conserver en H |
| 6 | 1 | Proposition centrale (citation) | H [S1] | D | registre | Conserver en H, verbatim, citée par identifiant |
| 7 | 1 | La clause finale est une condition d'échec | E | D | registre | **Requalifier en N** : règle posée par l'auteur |
| 8 | 2 | Énoncé 1 : l'ensemble existe et n'est pas vide ; « le seul des quatre que le corpus ait déjà instruit » ; sa taille manque | H | R (L1.C15) | L1.C15 (`audit_contradictoire`, 21 vérifications, 15 sources `a_requalifier`) ; OPERATIONNALISATION-INSOLVABLE : « l'inscription ne vaut pas validation », « la mesure décide de F10 » | **Réduire** : « instruit » ne peut signifier qu'« défini et argumenté », non « établi » |
| 9 | 2 | Énoncé 2 : le crédit privé filtre par la solvabilité anticipée | H | ∅ | L1.C07 § 7 (`verifie`) | Conserver, renvoi à L1.C07 à ajouter |
| 10 | 2 | Énoncé 2 : le budget public filtre par la contrainte budgétaire ; les deux filtres ne se recouvrent pas exactement | H | ∅ | L1.C15 § 1 (le filtre change de porteur), L1.C13 (`audit_contradictoire`) | Conserver en H ; renvois |
| 11 | 2 | Énoncé 3 : financer à la réalisation ne dispense pas par soi d'un revenu futur ; distinction bénéficiaire / émetteur ; dépend d'A35b | H, puis E pour l'état d'A35b | D, registre | A35b (ouvert), A35 (arbitré) | Conserver ; l'état d'A35b en E |
| 12 | 2 | Un crédit exige du bénéficiaire un revenu futur ; un financement non remboursable ne l'exige pas ; « le corpus les confondait » | H | I | L1.C07 § 2 (remboursement), L1.C08 § 2 (intérêts) | Conserver l'inférence, renvois ; **retirer** l'auto-histoire |
| 13 | 2 | Énoncé 4 : additionnalité sur les ressources, non sur la monnaie | H | I | — | Conserver |
| 14 | 3 | Condition de démonstration (citation) | H [S1] | D | registre | Conserver verbatim, **en N** |
| 15 | 3 | Condition d'échec réciproque (citation, cinq dimensions) | H [S1] | D | registre — **mais passe-2 porte la version à trois dimensions** (écart 1) | Conserver verbatim, en N, après arbitrage sur le texte de référence |
| 16 | 3 | Les deux conditions portent les mêmes cinq dimensions ; la première version en omettait deux ; corrigé le 2026-09-09 | E | D | passe-2 | Conserver la première phrase ; **retirer** l'historique |
| 17 | 3 | La comparaison porte sur un résultat défini, non sur les mêmes activités au même volume ; l'échec est possible des deux côtés | E | D | registre | Conserver, en N pour la règle, H pour le motif |
| 18 | 3 | Règle du « réalisable » : symétrie (délai, effort, capacités comparables) ; ni adversaire affaibli ni adversaire idéal | E [S1] | D | passe-2 dit « non tranchée, le choix appartient à l'auteur » (écart 2) | Conserver en N après arbitrage |
| 19 | 3 | Deux résultats produits séparément : système disponible, meilleur portefeuille techniquement possible | E [S1] | D | idem | Conserver en N |
| 20 | 3 | Le test demande un avantage comparatif, non une nécessité ; plus dur en pratique | H | I | — | Conserver |
| 21 | 4 | Deux familles : instruments de financement (liste) ; mécanismes d'autorité, de consentement et de contrôle (liste) | E | D ; R (L18.C30) | S-IPBES-6 pp. 28–34 pour la seconde liste | Conserver ; la partition en N, la seconde liste sourcée ou en renvoi |
| 22 | 4 | Leur demander de financer est une erreur de catégorie ; ils sont une dimension de la clause gouvernance ; « ce chapitre l'avait commise » | H | D | registre | Conserver en N ; **retirer** l'auto-histoire |
| 23 | 5 | Objection 1 : coût de transaction, « no new allocation system » ; le dispositif est un système d'allocation nouveau ; la clause de coût joue contre lui | E, citation | R (L18.C29) | S-IPBES-6 p. 21 (retrouvée) | Conserver ; citation sourcée ; l'inférence en H |
| 24 | 5 | Objection 2 : « les instruments de logique marchande » ne stimulent pas le changement institutionnel ; insuffisants pour déplacer le paradigme ; défense étroite | E, citations | R (L18.C29) | S-IPBES-6 pp. 22–23 (retrouvées) ; **antécédent = permis, compensations, taxes et redevances, dérivés** | **Réduire** : nommer l'antécédent exact ; le verdict ne vise ni les paiements pour services écosystémiques, ni les transferts fiscaux, ni une émission |
| 25 | 5 | Objection 3 : REDD+ et recentralisation ; « un flux monétaire dont l'émission est conditionnée par une qualification crée un enjeu à contrôler qui qualifie et qui perçoit » | E, citation | R (L18.C29) | S-IPBES-6 p. 22 (retrouvée) ; le mécanisme est en `::hypothese::` dans L18.C29 § 3 | Conserver ; **requalifier le mécanisme en H** |
| 26 | 5 | Objection 4 : l'échec de la cible tient au défaut de conformité et au mandat sectoriel, causes remédiables ; d'où le meilleur portefeuille réalisable | E | R (L18.C26) | S-IPBES-4 résumé exécutif p. 1 (retrouvé) ; L18.C26 : « n'établit aucune causalité », « oriente » | **Réduire** : différentiel de progrès et absence de mécanisme de conformité rapportés ; « causes remédiables » en H |
| 27 | 6 | Aucun énoncé ne se tranche par raisonnement ; trois voies de preuve ; ce que chacune couvre | H / E | D | passe-2 correction 7 | Conserver ; en N pour l'assignation des voies |
| 28 | 6 | « Ce chapitre avait écrit […] questions de simulateur » | H | D | passe-2 | **Retirer** |
| 29 | 6 | Ce que le premier modèle doit faire : chaîne complète, trois scénarios, branches d'A35b, pouvoir conclure à l'échec | H | D | A35b : « aucun modèle macroéconomique avant [la revue comptable] » ; L13.C01 | Conserver en N, **avec le rang** : après la revue comptable d'A35b |
| 30 | 7 | N'établit pas la proposition ; ne construit pas le portefeuille ; « réalisable » porte une difficulté non tranchée | E | D | contradit le § 3 (écart 2) | Conserver, harmoniser |
| 31 | 7 | A35 arbitre le porteur (l'émetteur) ; règle de conception, non qualification validée ; A35b porte nature, exigibilité, contrepartie, extinction, reflux insuffisant, réclamation du détenteur | E [L10.C06] | registre A35, A35b | L10.C06 (`brouillon`) porte l'incidence ; le porteur est arbitré dans passe-2 | Conserver ; citer A35 et A35b par identifiant, L10.C06 en renvoi |

## 4. Dépendances

### 4.1 A35b — ouvert, non tranché

**Objet.** Nature, exigibilité, contrepartie et extinction du passif de
l'émetteur. Statut `ouvert`, `tranche_par: non-tranche`, `lie_a: [A35]`,
`texte: protocoles/passe-2.md`, `chapitres: [L10.C06, L19.C02, L19.C06,
L19.C10, L1.C31]`, `maj: 2026-09-09`. La version 3 de la matrice comptable
(L19.C10) rend cinq résultats séparés : cohérence arithmétique et liquidité
calculées ; qualification comptable seulement proposée ; solvabilité
intertemporelle et conformité juridique non évaluées. Quatorze branches,
aucune conclusion exclusive.

**Prochain jalon.** Revue par un comptable national, et pour la question 6 par
un juriste de droit monétaire international ou un praticien des réserves
(`protocoles/revue-comptable-a35b.md`, huit questions). **« Aucun modèle
macroéconomique avant elle. »**

**Ce que L1.C31 en tire, et ce qu'il doit dire.**
- Le troisième énoncé (le moment du financement) ne se mesure qu'une fois
  A35b tranché : la créance éventuelle sur le bénéficiaire, la nature du
  passif et le mécanisme d'extinction en décident. Le chapitre le dit ; il
  doit le dire comme une limite, non comme une vérification en attente.
- Le « premier modèle » du § 6 est rangé par A35b après la revue comptable.
  Le chapitre ne porte pas ce rang aujourd'hui ; il doit le porter.
- Le chapitre n'anticipe aucune branche d'A35b et ne doit pas le faire. La
  distinction qu'il tient (financement non remboursable du bénéficiaire,
  passif subsistant de l'émetteur) est compatible avec les quatorze branches
  et n'en privilégie aucune.

### 4.2 A35 — arbitré (le porteur)

Arbitré en deux temps : incidence économique portée par la société (arbitrage
antérieur, corrigé par L10.C06 le 2026-09-07) ; porteur arbitré le
2026-09-09 : l'unité est inscrite au passif de l'émetteur, règle de
conception dont A35b doit identifier l'obligation présente. L1.C31 § 7 le
restitue exactement. Le chapitre cite L10.C06 pour cela ; L10.C06 (`brouillon`,
révision 2026-09-09) porte l'incidence et sa correction, tandis que
l'arbitrage du porteur est dans passe-2 et dans l'entrée A35 du registre :
citer l'identifiant.

### 4.3 A43, A44, F10, OPERATIONNALISATION-INSOLVABLE, REGLE-D-EMISSION

- **A44** (arbitré le 2026-09-09) : NEMO IMS ne garantit pas les conditions de
  la vie ; il garantit la disponibilité du financement pour les besoins
  essentiels **matériellement réalisables**, dans les limites écologiques et
  sous contrôle démocratique. C'est la restriction qui rend la proposition
  de L1.C31 cohérente avec le reste du corpus (pouvoir d'achat, non
  ressources) ; le chapitre ne la cite pas et devrait la citer.
- **A43** (arbitré) : trois composantes de maturité inégale ; seule l'unité
  de réserve entre banques centrales est expérimentable ; le remplacement
  mondial du système monétaire n'est pas applicable. Le chapitre ne dit pas
  sur quelle composante porte son test. La chaîne du § 6 (émission de l'unité
  de réserve, inscription à la banque centrale, conversion en monnaie
  nationale, versement au bénéficiaire) désigne la deuxième composante
  servant la première ; à déclarer.
- **F10** (ouvert, non tranché, `texte: protocoles/falsification.md`) : le
  registre porte déjà que l'argument est écrit en L1.C31, corrigé le même
  jour, et « n'est pas établi : le portefeuille de comparaison n'a jamais
  été construit ». Falsification.md nomme l'acquisition qui lèverait F10
  (l'histoire des réformes de subventions dommageables : tentatives, période,
  mécanismes de défaite) et la forme déplacée de F10 par L24.C03 (« faire
  mieux que les instruments existants »). Le chapitre ne mentionne ni l'une
  ni l'autre ; sa condition de démonstration est précisément la forme
  déplacée. L18.C09 et L24.C03, qui instruisent F10, ne sont pas en
  `renvois`.
- **OPERATIONNALISATION-INSOLVABLE** (orienté, auteur, `lie_a: [F10]`) :
  cinq critères et l'ordre de l'épreuve empirique (définir, constituer des
  cas, faire classer par des tiers, documenter les désaccords, puis mesurer),
  « la mesure décide de F10 ». C'est la voie de preuve du premier énoncé ; le
  chapitre parle d'« enquête empirique » sans la nommer.
- **REGLE-D-EMISSION** (orienté) porte L1.C31 dans `chapitres`, mais le
  chapitre ne parle pas de la règle d'émission ; le lien tient au
  troisième étage de la chaîne arrêtée le 2026-09-09 (montant déterminé par
  les coûts réels, les capacités disponibles et la contrainte
  macroéconomique — passe-2, correction 8), qui est la traduction de
  « mobiliser des ressources réelles sans dépasser les contraintes ». À
  mentionner en une phrase ou à retirer du registre : décision de l'auteur.

### 4.4 Ce qui manque au registre

Les décisions que L1.C31 enregistre n'ont pas d'entrée propre : le registre
les mentionne dans F10 (`decision`, 500 signes) et renvoie à passe-2, dont le
texte porte une version antérieure de la condition d'échec (écart 1). Deux
objets sont proposés, identifiants et rédaction à l'auteur :

1. **Un arbitrage** (`arbitre`, `auteur`, `maj` 2026-09-09) portant la
   proposition centrale, la condition de démonstration, la condition d'échec
   à cinq dimensions, la règle du réalisable et les deux résultats séparés,
   avec `lie_a` vers A35b, A44, F10 et la pièce ci-dessous, `chapitres:
   [L1.C31, L1.C08]`. Son `texte` peut pointer sur cette note, qui
   reproduit les énoncés dans leur forme corrigée (§ 6.2), comme
   REGIME-NEGATIF pointe sur `architecture-L1-C08.md`.
2. **Une pièce de conception manquante** (`ouvert`, `non-tranche`) : le
   portefeuille de comparaison, avec ses cinq grandeurs, ses deux versions
   (système disponible, meilleur portefeuille techniquement possible) et
   son `acquisition_bloquante` (les études comparatives et cas historiques
   de la troisième voie de preuve). Les entrées 2, 3 et 4 de
   `verifications_en_attente` y trouvent leur destination.

## 5. Écarts relevés

1. **Deux textes de la condition d'échec.** Le chapitre cite une condition à
   cinq dimensions (résultat, délai, coût social total, risque
   macroéconomique, qualité de gouvernance) et déclare que la première
   version en omettait deux, corrigée le 2026-09-09. Passe-2, correction 5,
   porte la version à trois dimensions (« à coût et risque égaux ou
   inférieurs »). Le texte de référence de la forme corrigée n'existe donc
   que dans le chapitre. À arbitrer : quel document fait foi, et où la forme
   corrigée est consignée (§ 6.2 la reproduit).
2. **« Réalisable » : arrêté ou non tranché.** § 3 : « la règle de
   "réalisable" est arrêtée, et elle est symétrique », avec deux résultats à
   produire séparément ; entrée 3 des vérifications : « arrêtée le
   2026-09-09 » ; § 7 : « le mot "réalisable" porte une difficulté non
   tranchée » ; passe-2, correction 5 : « difficulté non tranchée […] le
   choix appartient à l'auteur ». Lecture proposée : la règle de symétrie et
   l'exigence de deux résultats séparés **sont** la décision, et elles
   remplacent le choix binaire entre politiquement réalisable et
   techniquement possible ; ce qui reste non fait est le jugement sur ce qui
   est techniquement possible. À confirmer par l'auteur ; le § 7 sera
   harmonisé sur cette lecture.
3. **Antécédent de l'objection 2.** Le verdict « do not offer stimulus for
   institutional change or adaptive governance » vise, dans le texte lu, les
   permis échangeables, les compensations de biodiversité, les taxes et
   redevances liées à la biodiversité, et les produits dérivés ; le verdict
   « insufficient to shift the current economic paradigm » vise des actions
   de court terme s'appuyant principalement sur ce groupe, dont la
   suppression des subventions dommageables. Le chapitre écrit « les
   instruments de logique marchande », plus large. L'objection s'en trouve
   réduite, et sa « défense étroite » devient exacte plutôt qu'étroite. Ce
   relevé ferme en partie la troisième vérification de L18.C29 (composition
   du « troisième groupe »), ce qui relève de ce chapitre-là, non de C31.
4. **Un mécanisme en `::etat::` qui est une hypothèse.** « Un flux monétaire
   dont l'émission est conditionnée par une qualification crée un enjeu à contrôler qui qualifie et qui
   perçoit » est marqué `::hypothese::` dans L18.C29 § 3 et `::etat::` dans
   L1.C31 § 5.
5. **Objection 4 plus forte que sa source.** L18.C26 écrit qu'il « n'établit
   aucune causalité sur l'échec de la cible » et qu'il « oriente » ; le
   chapitre 4 de l'IPBES rapporte un différentiel de progrès et l'absence de
   mécanismes de conformité, et donne, page 28, le défaut de conformité
   comme « one reason [that] may be ». L1.C31 en fait « le motif de
   l'échec […] c'est-à-dire des causes remédiables ». À réduire.
6. **« Le seul des quatre que le corpus ait déjà instruit. »** L1.C15 est en
   `audit_contradictoire`, ses quinze sources `a_requalifier` ; la pièce
   OPERATIONNALISATION-INSOLVABLE pose que l'inscription ne vaut pas
   validation. Le mot « instruit » doit signifier « défini et argumenté ».
7. **Chronique du corpus dans le corps.** Cinq passages racontent les
   corrections (voir table, n° 1, 12, 16, 22, 28). Passe-2 les tient déjà.
8. **Renvois.** [L18.C19, L24.C07] cités et non déclarés ; L11.C30, L13.C01,
   L25.C07 déclarés et non cités ; L1.C05, L1.C07, L1.C13, L18.C09, L24.C03,
   L1.C29 (A44) absents alors que le texte réécrit s'y appuiera.
9. **Rang du modèle.** Le § 6 spécifie un premier modèle sans dire qu'A35b le
   range après la revue comptable.
10. **Composante d'A43 visée** non déclarée.

## 6. Structure proposée

### 6.1 Titre

Le titre actuel, « L'ajout est une mobilisation de ressources réelles, ou il
n'est rien », est un slogan. Proposition, dans la ligne de L1.C07 et L1.C08 :
**« Ce que le dispositif doit démontrer : mobiliser des ressources réelles
que les instruments existants ne mobilisent pas »**. Le fichier serait
renommé, l'identifiant L1.C31 et l'URL conservés (convention § 3).
Alternative plus courte : « L'apport propre du dispositif, et comment il
peut échouer ». Décision de l'auteur.

### 6.2 Les énoncés de référence, dans leur forme corrigée

Reproduits ici pour qu'un objet du registre puisse y pointer.

**Proposition centrale.** NEMO IMS ajoute aux instruments existants la
capacité de mobiliser des ressources réelles — travail, énergie, matériaux,
capacités productives — au profit d'activités écologiquement et socialement
nécessaires que ni le critère de rentabilité du crédit privé ni les
contraintes budgétaires nationales ne permettent d'engager, et sans dépasser
les contraintes inflationnistes, extérieures, physiques et distributives.

**Condition de démonstration.** NEMO IMS démontre un apport propre s'il obtient
un meilleur résultat matériel, ou un résultat inaccessible au meilleur
portefeuille effectivement construit, sans détérioration disproportionnée des
quatre autres dimensions.

**Condition d'échec réciproque.** Si un portefeuille institutionnellement
réalisable atteint un résultat matériel équivalent ou supérieur dans un délai
comparable, avec un coût social total et des risques macroéconomiques et
financiers égaux ou inférieurs, et une gouvernance au moins équivalente,
l'avantage comparatif de NEMO IMS n'est pas établi. Si NEMO n'atteint ce
résultat qu'en franchissant les contraintes inflationnistes, extérieures,
physiques ou distributives, il échoue également.

**Règle de défaut.** Hors de ces deux conditions, le verdict est non concluant :
l'apport propre n'est pas démontré, l'avantage comparatif n'est pas écarté et
F10 demeure ouvert.

**Règle du réalisable.** Comparer le dispositif à des solutions pouvant être
mises en place dans le même délai, avec un effort juridique, institutionnel
et administratif comparable, et des capacités administratives comparables :
ni adversaire affaibli, ni adversaire idéal. Le coût institutionnel
d'établissement de NEMO entre dans son propre délai et son propre coût social.
Deux résultats sont produits séparément : la comparaison décisive avec le
meilleur portefeuille institutionnellement réalisable et la comparaison
exploratoire avec le meilleur portefeuille techniquement possible.

### 6.3 Plan

Ouverture (trois phrases) : ce que le chapitre enregistre (la proposition,
ses deux conditions, arbitrage de l'auteur du 2026-09-09) ; ce que le test
mesure (des ressources réelles, non la disponibilité d'un financement) ; ce
qu'il n'établit pas (aucun énoncé n'est mesuré, le portefeuille de
comparaison n'est pas construit).

1. **Ce que la création monétaire produit.** L'écriture crée du pouvoir
   d'achat (L1.C07, L1.C05) ; trois conséquences (`::hypothese::`).
2. **La proposition et sa clause de contraintes.** Texte verbatim, cité par
   identifiant ; la clause comme condition d'échec (`::norme::`) ; la
   restriction A44.
3. **Quatre énoncés mesurables séparément.** Existence et taille (L1.C15,
   OPERATIONNALISATION-INSOLVABLE) ; deux filtres (L1.C07 § 7, L1.C15 § 1,
   L1.C13) ; le moment et A35b ; l'additionnalité sur les ressources.
4. **Condition de démonstration, condition d'échec, règle du réalisable.**
   Verbatim (`::norme::`) ; pourquoi des résultats et non des activités
   (`::hypothese::`) ; avantage comparatif, non nécessité.
5. **Les comparateurs.** Instruments de financement (le portefeuille) ;
   mécanismes d'autorité, de consentement et de contrôle (dimension
   gouvernance, S-IPBES-6 pp. 28–34 ou renvoi L18.C30) ; l'erreur de
   catégorie.
6. **Ce que l'évaluation intergouvernementale oppose.** Quatre objections,
   citations sourcées sur S-IPBES-6 pp. 21–23 avec leurs antécédents exacts
   et S-IPBES-4 p. 1, inférences du corpus en `::hypothese::`.
7. **Trois voies de preuve, et le rang du modèle.** Enquête empirique,
   modèle comptable et macroéconomique, comparaison institutionnelle ; le
   premier modèle après la revue comptable d'A35b ; composante d'A43 visée.
8. **Portée et limites.** Non établi ; portefeuille non construit (pièce du
   registre) ; coût propre non évalué ; A35b ; l'acquisition qui lèverait
   F10 ; ce que le chapitre ne compare pas.

Régime `conception` conservé. Marquage : `::norme::` pour les règles posées
(conditions, règle du réalisable, partition des comparateurs, assignation des
voies de preuve), `::hypothese::` pour la proposition et les inférences,
`::etat::` pour ce qui est sourcé ou renvoyé.

### 6.4 En-tête proposé

- `sources_primaires` : S1 = IPBES 2022, chapitre 6 (pages 21–23 ; 28–34 si
  le § 5 conserve la liste), `theorie`, `ouverte`, `date_verification`
  2026-09-11, mention « OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08
  (acquisition du Livre 18), pages lues dans le texte le 2026-09-11,
  citations retrouvées par script, folio = page PDF − 4 », empreinte, `url`
  après résolution du DOI ; S2 = IPBES 2022, chapitre 4, résumé exécutif
  page 1, mêmes règles — ou renvoi seul à L18.C26 si l'objection 4 est
  réduite à un renvoi.
- `verifications_en_attente: []`, avec bloc commenté au format L1.C12 :
  provenance des cinq entrées déplacées et leur destination ; à compléter
  après l'audit contradictoire.
- `concepts` : les cinq actuels ; `affectation_des_instruments` n'apparaît
  qu'une fois (« affectation ») et `qualification_regenerative` par
  « qualification » : à confirmer à la réécriture.
- `renvois` : ajouter L1.C05, L1.C07, L1.C13, L1.C29, L18.C09, L24.C03,
  L18.C19 et L24.C07 s'ils restent cités ; retirer L11.C30, L13.C01 et
  L25.C07 s'ils ne sont pas appelés (L13.C01 le sera par le § 7).
- `revision_de_fond` : 2026-09-11 si l'auteur retient les réductions des
  objections 2 et 4 et l'harmonisation du « réalisable » ; sinon éditorial.
- `citable: false` maintenu.

### 6.5 Retraits et réductions

Retraits : la chronique des déplacements de F10 et des corrections du
chapitre (n° 1, 12, 16, 22, 28) ; « la mesure existe, la descente jusqu'au
produit est outillée » (n° 2) ; les deux entrées S1 et S2 ; le style en
capitales. Réductions : « instruit » (n° 8) ; l'antécédent de l'objection 2
(n° 24) ; le mécanisme de capture en hypothèse (n° 25) ; l'objection 4 en
différentiel rapporté (n° 26). Aucune thèse n'est retirée : la proposition,
les conditions et la partition sont conservées telles quelles.

## 7. Décisions demandées à l'auteur

1. Le titre (§ 6.1) et le renommage du fichier.
2. Le sort de S1 et S2 : retrait et remplacement par un arbitrage et une
   pièce du registre (§ 4.4), identifiants à fixer.
3. Le texte de référence de la condition d'échec à cinq dimensions et le
   document qui le consigne (écart 1).
4. La lecture du « réalisable » : règle de symétrie plus deux résultats
   comme décision arrêtée (écart 2).
5. La réduction de l'objection 2 à son antécédent exact et de l'objection 4
   au différentiel rapporté (écarts 3 et 5).
6. L'inscription du rang du modèle après la revue comptable d'A35b et de la
   composante d'A43 visée.
7. Le déplacement des cinq entrées de `verifications_en_attente` vers le
   corps et le registre, avec bloc commenté, et ce que ce troisième cas
   pilote fait à l'arbitrage du 2026-09-09 sur la structure du champ.
8. L'ouverture de S-IPBES-4 comme source propre ou le renvoi seul à
   L18.C26.
9. Le lien REGLE-D-EMISSION : une phrase dans le chapitre ou retrait de
   L1.C31 de ses `chapitres`.

## 8. Séquence

1. Validation de cette architecture, avec les neuf décisions.
2. Réécriture du chapitre selon § 6 ; résolution du DOI ; entrée des sources.
3. Vérification par script des citations IPBES sur le texte réécrit
   (vérificateur de session, pages imprimées, tolérance de saut de page).
4. Contrôle structurel ; diff soumis à l'auteur.
5. Dossier d'audit contradictoire à coller, transmis par l'auteur à un
   modèle tiers (Codex ou Gemini) ; synthèse objection par objection ;
   arbitrage.
6. Objets du registre (arbitrage, pièce), `verifications_en_attente` vidées
   avec bloc commenté, statut selon l'arbitrage de l'auteur ; `verifie`
   attesterait des sources contrôlées et d'une structure cohérente, non de
   l'importance empirique de la proposition, qu'aucune mesure ne soutient.
7. Enregistrement de l'état par le script ; commits séparés (renommage,
   réécriture, registre, état) ; aucun push.

## 9. Décisions postérieures intégrées — 2026-09-12

Cette section fait foi lorsqu'elle diffère des propositions ou questions des
sections 1 à 8. Elle consigne les décisions rendues après la rédaction initiale
de cette note. Elles ne doivent plus être présentées comme des choix ouverts.

### 9.1 Titre et objet

Titre retenu : **« L'apport propre de NEMO IMS, et comment il peut échouer »**.
L'identifiant L1.C31 et son URL demeurent inchangés ; le fichier sera renommé
séparément.

C31 est un chapitre de conception et de mise à l'épreuve. Il demande si NEMO
IMS permet de mobiliser des ressources réelles en faveur de besoins essentiels
et de la régénération des communs que les instruments existants ne mobilisent
pas, à délai, coût, risque et qualité de gouvernance comparables. Il ne présente
pas NEMO IMS comme démontré.

### 9.2 Vocabulaire

Le mot **« adossé »** est retiré pour décrire NEMO IMS : il suggère une
convertibilité ou un droit sur un actif écologique. La formulation de référence
est :

> NEMO IMS est une monnaie affectée à la préservation et à la régénération des
> communs. Son émission est conditionnée par la qualification d'activités
> essentielles, dans les limites physiques reconnues et sous contrôle
> démocratique.

« Flux monétaire adossé à une qualification » devient « flux monétaire dont
l'émission est conditionnée par une qualification ».

### 9.3 Sources

Les décisions de l'auteur et les chapitres du corpus sortent des
`sources_primaires`. Les chapitres 6 et 4 de l'évaluation IPBES sur les valeurs
de la nature entrent comme sources directes, avec leur édition, leur URL et les
passages effectivement lus. L'IPBES n'évalue pas NEMO IMS ; il documente des
instruments existants, leurs limites et certains risques institutionnels.

### 9.4 Test à cinq dimensions

La version à cinq dimensions est la référence :

1. résultat matériel obtenu ;
2. délai nécessaire ;
3. coût social total ;
4. risques macroéconomiques et financiers ;
5. qualité de la gouvernance, scindée entre architecture attachée et risque de
   capture intrinsèque au mécanisme d'allocation.

NEMO démontre un apport propre s'il obtient un meilleur résultat matériel, ou
un résultat inaccessible au meilleur portefeuille effectivement construit,
sans détérioration disproportionnée sur les quatre autres dimensions. Il
échoue à démontrer cet apport si un
portefeuille institutionnellement réalisable obtient un résultat équivalent ou
supérieur, dans un délai comparable, avec un coût social, des risques et une
gouvernance comparables ou meilleurs. Il échoue aussi s'il franchit les
contraintes inflationnistes, extérieures, physiques ou distributives.

Hors de ces conditions, le verdict est non concluant : l'apport propre n'est
pas démontré, l'avantage comparatif n'est pas écarté et F10 demeure ouvert.
Chaque dimension est évaluée séparément, sans score agrégé. Les seuils de
proportion sont fixés avant la comparaison par l'autorité démocratique après
expertise pluraliste, puis appliqués par une qualification motivée. Cette forme
transpose A47 à une comparaison d'instruments sans étendre silencieusement le
domaine propre d'A47.

La version à trois dimensions portée par `passe-2.md` est un état antérieur,
explicitement dépassé par cette version.

### 9.5 Deux comparaisons distinctes

La comparaison décisive porte sur le meilleur portefeuille
**institutionnellement réalisable** dans le même délai, compte tenu des
capacités juridiques, politiques, administratives et productives disponibles.
L'effort juridique, institutionnel et administratif ainsi que les capacités
administratives doivent être comparables des deux côtés. Le coût
institutionnel d'établissement de NEMO entre dans son propre délai et son
propre coût social total.

La comparaison exploratoire porte sur le meilleur portefeuille
**techniquement possible**, même s'il n'est pas actuellement réalisable
politiquement ou juridiquement. Elle situe une frontière technique et ne suffit
pas seule à déclarer NEMO superflu ou applicable.

Le principe de comparaison est arrêté. La construction empirique des deux
portefeuilles reste ouverte.

### 9.6 Registre

Deux identifiants sémantiques sont retenus, sans créer de nouveau matricule
d'arbitrage :

- `TEST-APPORT-PROPRE`, décision de l'auteur portant la question centrale, les
  cinq dimensions, les deux comparaisons et les conditions d'échec ;
- `PORTEFEUILLE-COMPARAISON`, pièce de conception ouverte portant les solutions
  adverses, leurs capacités, délais, coûts, risques et gouvernance.

`PORTEFEUILLE-COMPARAISON` est lié réciproquement à F10 et à
`OPERATIONNALISATION-INSOLVABLE`. L'acquisition bloquante de F10 ne se limite
plus à la cogestion : elle couvre les budgets publics, la fiscalité, le crédit
dirigé, les banques publiques, les garanties, les achats d'actifs, les
transferts internationaux, les restructurations de dette, la réglementation et
les autres instruments pertinents.

### 9.7 Portée des objections IPBES

- L'absence de transformation institutionnelle est attribuée uniquement aux
  instruments visés par le passage.
- L'insuffisance pour changer de paradigme reste limitée au groupe d'actions
  concerné.
- La recentralisation observée dans certains dispositifs comme REDD+ est un
  fait documenté ; le risque que la qualification de NEMO reproduise cette
  capture est une hypothèse.
- L'IPBES ne démontre ni une cause unique de l'échec des objectifs ni que les
  causes seraient toutes remédiables.

### 9.8 Dépendances et rang du modèle

A44 borne la promesse aux besoins essentiels matériellement réalisables. A35b
reste ouvert : le non-remboursement par le bénéficiaire ne permet aucune
conclusion sur le passif de l'émetteur. A43 borne le domaine le plus mûr à
l'unité de réserve entre banques centrales ; les autres composantes demeurent
prospectives.

Le chapitre conserve son lien avec `REGLE-D-EMISSION` et porte cette phrase :

> Le test de l'apport propre suppose une émission calibrée sur les coûts réels,
> les capacités disponibles et les contraintes physiques et
> macroéconomiques ; la règle précise de ce calibrage demeure un chantier de
> conception distinct.

Le modèle macroéconomique intervient après la revue humaine d'A35b et
représente explicitement les branches encore ouvertes.

### 9.9 Métadonnées, historique et audit

Les limites restent dans le corps et le résumé ; les décisions vont dans
`corpus/arbitrages.yaml` ; les dettes de conception vont dans les pièces
ouvertes. `verifications_en_attente` ne garde que les tâches documentaires
effectivement vérifiables. Aucune migration générale du schéma n'est lancée
pendant C31 ; le constat du troisième pilote est conservé pour réexamen après
C15.

L'historique interne des corrections sort du corps public et demeure dans
cette architecture et `passe-2.md`. Après la réécriture, C31 passe d'abord par
un audit contradictoire : aucun passage direct à `verifie`. L'audit conduit par
Claude sera une passe adverse supplémentaire ; Claude ayant rédigé
l'architecture initiale, l'audit tiers indépendant prévu par
`protocoles/audit-contradictoire.md` reste obligatoire.

## 10. Traitement de la passe adverse Claude — 2026-09-12

Le rapport `protocoles/rapport-audit-L1-C31-claude.md` a formulé douze
objections, dont deux bloquantes. Les cinq décisions doctrinales ont été
rendues par l'auteur et consignées dans
`protocoles/arbitrage-auteur-L1-C31-2026-09-12.md`. Leur application détaillée
figure dans `protocoles/traitement-objections-L1-C31.md`.

La version corrigée rétablit la symétrie du réalisable, ajoute le verdict non
concluant, restreint l'inaccessibilité au meilleur portefeuille effectivement
construit, transpose explicitement la forme procédurale d'A47 et scinde la
gouvernance entre architecture attachée et risque de capture intrinsèque. Elle
expose aussi le cas arithmétique de F10, rectifie les marqueurs de régime et
applique l'affectation des instruments à NEMO comme aux solutions concurrentes.

Ces corrections rendent le programme de preuve cohérent ; elles n'apportent
aucun résultat empirique. F10, A35b et `PORTEFEUILLE-COMPARAISON` restent
ouverts. L'auteur a validé le texte corrigé le 2026-09-12 ; le chapitre passe à
`audit_contradictoire` et son dossier est préparé pour un modèle tiers
indépendant.

## 11. Traitement de l'audit tiers Gemini — 2026-09-13

Le rapport `protocoles/rapport-audit-L1-C31-tiers.md` respecte les six sections
du protocole et formule six objections. Elles sont traitées dans
`protocoles/traitement-objections-tiers-L1-C31.md`.

La correction principale rend explicite ce que le chapitre posait déjà en
principe : la monnaie ne crée aucune ressource. Le résultat matériel devient
un résultat **net**, après imputation des ressources retirées à d'autres usages,
des effets d'éviction et des coûts d'opportunité. Le modèle doit représenter la
réallocation et la formation des prix.

La réserve comptable est maintenue avec une rédaction non ambiguë. Le
non-remboursement par le bénéficiaire ne suffit pas à qualifier le passif de
l'émetteur ; A35 impose séparément son inscription comme règle de conception,
et A35b doit encore identifier l'obligation présente qui la justifierait.

Les chiffres du cas arithmétique renvoient désormais directement au rapport du
PNUE ouvert et relu, ainsi qu'au passage de l'IPBES sur le facteur dix. Le coût
juridique reçoit un cas documenté et délimité : l'article 123 TFUE lorsque la
branche choisie mobilise les banques centrales de l'Union au bénéfice des
entités publiques visées. L'objection de l'ajustement par les prix est inscrite
comme risque distributif à mesurer, sans transformer toute émission en quantité
d'inflation déterminée.

Ces corrections n'établissent toujours aucun avantage de NEMO IMS. Elles
resserrent le test qui pourrait le démontrer ou le faire échouer.

## 12. Validation et audit factuel — 2026-09-13

L'auteur a validé le texte corrigé après l'audit tiers. La passe factuelle a
ensuite contrôlé les quatre sources et les onze appels de citation du corps.
Les passages annoncés ont tous été retrouvés dans les éditions identifiées :
six appels au chapitre 6 de l'IPBES, deux au chapitre 4, deux au rapport 2026
du PNUE et un à l'article 123 du TFUE.

Les affirmations non documentées sur NEMO restent dans les régimes
`::hypothese::` ou `::norme::`. Le chapitre dit explicitement que les
portefeuilles concurrents ne sont pas construits, que l'ampleur de l'essentiel
insolvable n'est pas mesurée, que F10 demeure ouvert et qu'A35b n'est pas
tranché. Ces limites empêchent de conclure à la nécessité, à la supériorité ou
à l'applicabilité de NEMO ; elles n'empêchent pas de vérifier la méthode et les
attributions du chapitre.

Le statut `verifie` atteste donc ici des sources contrôlées et datées et d'une
structure cohérente. `citable: false` demeure inchangé : aucune publication
n'est autorisée par ce statut.
