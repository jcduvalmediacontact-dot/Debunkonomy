---
chapitre: L26.C08
titre: "Même un puits gratuit ne donne pas dix"
livre: 26
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-08
autorite: preparatoire
citable: false
regime: hybride
sources_primaires:
  - ref: S1
    nature: donnees
    reference: "**D. J. Murphy, M. Raugei, M. Carbajales-Dale et B. Rubio Estrada, « Energy Return on Investment of Major Energy Carriers: Review and Harmonization », *Sustainability*, 14(12), 7098, 2022.** Pièce L26-08 du dossier documentaire de l'auteur. **DÉJÀ OUVERTE PAR L26.C03 le 2026-09-08 ; RELUE ICI POUR SA STRUCTURE DE FRONTIÈRES**, qui n'avait pas été exploitée. **DROITS : `libre`, mention CC BY lue dans le document.** **L'apport propre à cette relecture est le tableau 2**, qui donne pour chaque combustible l'investissement énergétique de chaque étape postérieure à l'extraction et **le rendement maximal atteignable à cette étape en supposant un rendement INFINI à l'extraction**."
    date_verification: 2026-09-08
  - ref: S2
    nature: donnees
    reference: "**A. K. Gupta et C. A. S. Hall, « A Review of the Past and Current State of EROI Data », *Sustainability*, 3(10), 2011, p. 1796-1809.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte le 2026-09-08 ; pièce L26-09. **DROITS : mention CC BY lue dans le document — `libre`.** **Le second auteur est celui qui a forgé le concept de rendement énergétique net dans les années 1970.** **C'est la source historique du corpus sur cette grandeur, et elle porte sur elle un jugement que le corpus doit reprendre.**"
    date_verification: 2026-09-08
verifications_en_attente:
  - "**LA QUATRIÈME FRONTIÈRE DEMANDÉE N'EST PAS COUVERTE PAR CES SOURCES, ET
     C'EST LA PLUS PROCHE DE CE QUE LE DISPOSITIF VEUT MESURER.** L'arbitrage
     demande quatre frontières : extraction, énergie livrée, point d'usage et
     **SERVICE FINAL**. **Les deux sources s'arrêtent au point d'usage.** Le
     service final suppose une comptabilité en travail utile ou en exergie de
     service, que ni l'une ni l'autre ne tient. **ACQUISITION DE RANG 1 : les
     travaux d'exergie utile, dont L17.C01 a déjà établi qu'ils constituent le
     seul poste où le découplage relatif n'est PAS observé.**"
  - "**DÉMANTÈLEMENT ET STOCKAGE NE SONT COUVERTS QUE PAR MENTION.** La revue de
     2011 énumère pour l'éolien les postes retenus — fabrication, transport,
     construction, exploitation et maintenance, frais généraux, raccordement au
     réseau, **et démantèlement « where possible »** — en précisant aussitôt que
     **« not all studies include the same scope of analysis »**. **Le corpus tient
     donc la LISTE des postes et non leur VALEUR.** Le stockage, que
     l'intermittence rend décisif, n'est chiffré par aucune des deux sources."
  - "**AUCUNE SÉRIE POSTÉRIEURE À 2022 N'EST TENUE, ET UNE PRÉVISION DE LA SOURCE
     A DÉJÀ ÉTÉ DÉMENTIE PAR LES FAITS.** La revue de 2011 rapporte une
     extrapolation donnant un rendement de 1:1 pour le pétrole et le gaz mondiaux
     **« as soon as about 2022 »**. **Nous sommes en 2026 et cela n'a pas eu
     lieu.** Les auteurs avaient eux-mêmes averti que **« the uncertainty for the
     exact date is large »**. **Le corpus enregistre l'échec de l'extrapolation
     comme un résultat, pas comme une coquille.**"
resume: "Ce chapitre répond dans sa forme à l'arbitrage rendu sur la frontière de calcul du rendement énergétique net, en construisant l'échelle de frontières demandée plutôt qu'un coefficient unique. Il établit d'abord, à partir du tableau d'harmonisation d'une revue de 2022, que la chaîne postérieure à l'extraction suffit à elle seule à plafonner le rendement livré, puisque ce tableau donne pour chaque combustible le rendement maximal atteignable à chaque étape en supposant un rendement infini à l'extraction, et que ce plafond vaut moins de neuf pour le pétrole et moins de deux pour les granulés de bois. Il en tire que la qualité du gisement ne suffit plus à déterminer le résultat, puisque la transformation, le transport et la distribution imposent un plafond indépendant d'elle, sans que l'énergie dépensée à l'extraction cesse pour autant d'abaisser le rendement réel en dessous de ce plafond. Il montre ensuite que le même écart se retrouve dans les chiffres réels, un gaz de schiste passant de quatre-vingt-trois à l'extraction à cinq au point d'usage, et que la seule convention de conversion vers l'électricité primaire déplace tous les classements, ce pour quoi les auteurs publient deux jeux de résultats et non un. Il ouvre enfin la revue historique écrite par l'inventeur du concept, qui donne une baisse séculaire non monotone, une dispersion de deux ordres de grandeur pour le nucléaire attribuée aux frontières de système, un écart systématique entre études conceptuelles et études d'exploitation pour l'éolien, et surtout un jugement de l'auteur sur sa propre grandeur, à savoir que les travaux disponibles relèvent souvent du plaidoyer et que les décisions se prennent sur une base analytique très maigre. Le chapitre conclut que le falsifieur physique cesse d'être indécidable sans devenir décidable, puisqu'il devient conditionnel à la publication des conventions et d'une plage de sensibilité, et il verse cette exigence comme contrainte de conception sur le barème et sur le simulateur."
concepts: [bareme, qualification_regenerative, decouplage]
renvois: [L1.C17, L8.C37, L11.C13, L17.C01, L24.C05, L26.C01, L26.C03, L26.C06, L26.C07]
---

# Même un puits gratuit ne donne pas dix

::etat:: **L26.C03 avait établi que deux équipes, disposant des mêmes données, publient sur les mêmes technologies des rapports variant d'un facteur voisin de quatre, et que le désaccord n'est pas empirique mais tient à une convention de périmètre.** Il en avait conclu que le falsifieur physique était **indécidable**, et posé A39.

::etat:: **A39 a été tranché le 2026-09-08, et il l'a été dans la FORME et non dans la valeur** : le corpus ne retiendra pas un coefficient unique, mais **plusieurs frontières comparables, une analyse de sensibilité et la publication des conventions de calcul**. **Ce chapitre exécute cette décision.** Il n'apporte pas le chiffre que le corpus n'a pas ; **il apporte l'échelle sur laquelle un chiffre pourrait être lu.**

## 1. La chaîne d'aval plafonne le rendement, même si l'extraction est gratuite

::etat:: La revue d'harmonisation de 2022 contient un dispositif de calcul que L26.C03 n'avait pas exploité [S1]. Pour chaque combustible et à chaque étape postérieure à l'extraction, elle donne l'investissement énergétique de l'étape, l'investissement cumulé depuis l'extraction, **et le rendement maximal atteignable à cette étape en supposant un rendement INFINI à l'extraction.**

::etat:: **C'est une expérience de pensée rigoureuse, et son résultat est net.** Un gisement dont l'exploitation ne coûterait rien du tout — un puits gratuit — **ne délivrerait pas pour autant un rendement élevé à l'usager**, parce que la préparation, le transport, le raffinage, la purification et la distribution consomment à eux seuls une fraction fixe du contenu énergétique livré.

::etat:: **Les plafonds, tels qu'ils sortent du tableau** [S1]. Pour le **pétrole**, l'investissement cumulé d'aval atteint **11,5 % de l'énergie livrée**, ce qui plafonne le rendement à **8,7** — sous dix, avec une extraction gratuite. Pour le **gaz**, le cumul atteint **17,9 %** et le plafond tombe à **5,6**. Pour le **charbon**, le cumul vaut **9,8 %** et le plafond **10**. Pour l'**éthanol de maïs**, le seul raffinage consomme **61 %** et le plafond s'effondre à **1,7**, puis **1,6** en fin de chaîne. Pour les **granulés de bois**, la préparation consomme **51 %** et le plafond vaut **2,0**, puis **1,6** après distribution.

::hypothese:: **La qualité du gisement NE SUFFIT DONC PLUS À DÉTERMINER LE RÉSULTAT.** **Elle continue de peser** — l'énergie dépensée à l'extraction s'ajoute à celle de la chaîne d'aval et abaisse le rendement réel en dessous du plafond calculé ici. **Ce que le tableau établit est que le plafond existe INDÉPENDAMMENT d'elle**, et qu'aucune richesse de gisement, si grande soit-elle, ne le franchit. **Deux ressources séparées d'un facteur quatre à l'extraction peuvent ainsi se retrouver à quelques dixièmes l'une de l'autre à l'usage** — non parce que l'extraction cesserait de compter, **mais parce qu'un terme commun borné s'ajoute aux deux et écrase leur écart relatif.**

::etat:: **Le même écart apparaît sur des chiffres réels et non fictifs** [S1]. Le **gaz de schiste** passe de **83 au point d'extraction à 5,2 au point d'usage**, *« due mainly to the large energy investments in the transmission and distribution stages »* — **un facteur seize.** Le pétrole conventionnel a une **médiane de 4,2** une fois harmonisé au point d'usage, et *« none of the conventional oil products have an EROI above 10 »*. Le charbon dur vaut **8,8**.

::etat:: **Et l'écart intérieur à une même catégorie peut dépasser l'écart entre catégories.** Les **plaquettes de bois** locales atteignent **32** ; les **granulés de bois**, dans la même famille des biomasses solides, plafonnent à **1,6**. Les auteurs préviennent expressément que le premier chiffre *« should not be misconstrued to be representative of the wider spectrum of solid biomass fuels »*.

::hypothese:: **C'est une objection directe à toute qualification par famille technologique.** Un barème qui accorderait un traitement à la « biomasse solide » ferait entrer dans la même case deux objets séparés d'un facteur vingt. **Le `bareme` doit donc porter sur des chaînes d'approvisionnement, non sur des catégories de ressources** — et le corpus ne dispose d'aucune donnée par chaîne.

## 2. La sensibilité, et pourquoi elle donne deux tableaux et non un

::etat:: **Pour l'électricité, une seule convention déplace tous les résultats** : le facteur de conversion en énergie primaire équivalente. **Les auteurs ne le choisissent pas — ils publient deux jeux de résultats** [S1], l'un pour un facteur de **0,3**, représentatif d'un réseau dominé par la production thermique, l'autre pour **0,7**, représentatif d'un réseau largement décarboné.

::etat:: **Sous le facteur 0,3**, l'hydroélectricité domine largement ; le nucléaire, l'éolien et parfois le photovoltaïque forment le deuxième groupe ; le solaire à concentration et la géothermie le troisième ; **toutes ces technologies dépassent 10**, l'énergie océanique se tenant exactement sur cette ligne. **L'électricité thermique au charbon et au gaz se situe entre 10 et 12**, la biomasse en plaquettes à **16**, et **le biogaz comme la bioénergie avec capture tombent entre 2 et 5**.

::hypothese:: **Deux enseignements pour le dispositif, et ils vont en sens contraire.** D'une part, **le classement n'est pas celui qu'un préjugé attendrait** : sous cette convention, le charbon et le gaz produisent une électricité dont le rendement est du même ordre que celui des renouvelables intermittentes, et supérieur à celui du biogaz. D'autre part, **la convention elle-même dépend de l'état du réseau, donc du résultat de la transition** — un barème calibré sur 0,3 devient faux à mesure qu'il réussit. **C'est une boucle que le corpus n'avait pas identifiée.**

::etat:: **Les auteurs refusent en outre de resserrer une dispersion qui est réelle.** Pour le photovoltaïque, l'écart tient aux technologies et à l'ensoleillement — de **1 000 à plus de 2 300 kWh·m⁻²·an⁻¹** selon la latitude — et ils déclarent avoir délibérément renoncé à l'harmoniser, *« since it represents a real-world variable and not a methodological inconsistency per se »*. Leur conclusion est explicite : *« it is unreasonable to expect to arrive at a SINGLE VALUE (or a very tight range of estimates) »*.

::etat:: **C'est, écrite par la source, la raison de fond de l'arbitrage rendu sur A39.** **Le refus du coefficient unique n'est pas une prudence du corpus : c'est une propriété de la grandeur.**

## 3. Ce que dit l'inventeur du concept de sa propre grandeur

::etat:: La seconde source est une revue de l'ensemble des données publiées, écrite par l'auteur qui a forgé le concept dans les années 1970 [S2]. **Elle donne une série historique, et elle donne un jugement.**

::etat:: **La série** : le rendement de la production de pétrole et de gaz aux États-Unis vaut *« roughly 30:1 in the 1950s which declined irregularly to 20:1 in the 1970s and 11-18:1 in the mid 2000's »*. Au niveau mondial, une autre équipe trouve **26:1 en 1992, 35:1 en 1999, et 18:1 en 2006**.

::hypothese:: **La série mondiale monte avant de redescendre, et cela compte.** **Le rendement énergétique net n'est pas une grandeur monotone décroissante** : il remonte quand l'effort de forage se relâche, et retombe quand il s'intensifie. **Un corpus qui présenterait la baisse comme une loi confondrait une tendance séculaire avec une réponse conjoncturelle** — et les deux ensemble expliquent, selon la source, environ **92 %** de la variabilité observée.

::etat:: **Une prévision de cette source a été démentie par les faits, et le corpus l'enregistre.** Elle rapporte une extrapolation linéaire selon laquelle le rendement du pétrole et du gaz conventionnels mondiaux pourrait atteindre **1:1 *« as soon as about 2022 »***. **Nous sommes en 2026.** Les auteurs avaient assorti ce chiffre d'un avertissement explicite — *« the uncertainty for the exact date is large »* — et noté qu'une autre hypothèse de coût repousserait le point d'équilibre.

::hypothese:: **C'est une leçon de méthode que le corpus doit porter au-delà de ce livre.** **Une extrapolation linéaire sur une grandeur non monotone produit une date, et la date était fausse.** Le corpus emploie ailleurs des trajectoires ; **il doit dire lesquelles sont extrapolées et sous quelle hypothèse de forme.**

::etat:: **La dispersion attribuée aux frontières est mesurée.** Pour le **nucléaire**, la revue rapporte des rendements *« of up to almost 60:1, to as low as even less than 1:1 »* — **deux ordres de grandeur** — et les auteurs écrivent que *« the differences in EROI can sometimes be attributed to differences in SYSTEM BOUNDARIES and technologies »*, avant d'ajouter que *« overall there is a LACK OF EMPIRICAL INFORMATION on the subject »*.

::etat:: **Pour l'éolien, un écart systématique sépare le modèle de l'exploitation.** Une méta-analyse de **112 turbines dans 41 études** trouve une moyenne de **24,6:1** pour l'ensemble, mais de **18,1:1 pour les seules études d'exploitation** — les modèles conceptuels retenant des conditions plus favorables. **Les postes déclarés y sont exactement ceux que l'arbitrage demande** : fabrication, transport, construction, exploitation et maintenance, frais généraux, raccordement au réseau, **et démantèlement *« where possible »*** — avec cette réserve immédiate : *« not all studies include the same scope of analysis »*.

::hypothese:: **Le corpus retient donc un biais d'optimisme mesuré, d'environ un quart, entre ce qu'un modèle promet et ce qu'une installation rend.** **C'est une correction applicable à toute qualification faite sur dossier plutôt que sur relevé** — et L11.C13 établit que le barème en vigueur certifie un procédé sur dossier.

## 4. Le jugement de l'auteur sur son propre instrument

::etat:: **La source porte sur son propre objet une appréciation que le corpus ne peut pas taire** [S2]. Peu d'études ont été menées depuis les années 1980, et celles qui l'ont été sont *« often marked more by ADVOCACY THAN OBJECTIVITY »*. Les décisions se prennent, écrivent les auteurs, *« on a VERY MEAGER ANALYTICAL AND DATA BASE, and with few scientists trained to cut through the reams of insufficiently analyzed energy advocacy »*.

::hypothese:: **Cela interdit deux usages au corpus, et le second est celui qui le tentait.** Il ne peut pas invoquer un rendement énergétique isolé comme s'il s'agissait d'une mesure établie. **Et il ne peut pas fonder un falsifieur sur une grandeur dont l'inventeur déclare la base de données maigre** — non que la grandeur soit fausse, mais **parce qu'un falsifieur exige une mesure susceptible de trancher, et que celle-ci ne tranche pas encore.**

## 5. Ce que devient le falsifieur, et ce qu'il ne devient pas

::etat:: **F11 cesse d'être indécidable sans devenir décidable.** L26.C03 l'avait déclaré indécidable parce que la convention de périmètre décidait du résultat et qu'aucune n'était retenue. **Une règle de forme est désormais arrêtée** : plusieurs frontières comparables, sensibilité publiée, conventions publiées. **F11 devient donc CONDITIONNEL** — il pourra être éprouvé dès que ces trois conditions seront remplies sur un cas, et il ne l'est encore sur aucun.

::etat:: **Ce qui a été gagné dans ce chapitre.** Le plafond imposé par la chaîne d'aval, indépendant de la qualité du gisement. L'ordre de grandeur des écarts entre frontières — un facteur seize sur un cas réel. La preuve, écrite par les auteurs, qu'un chiffre unique n'est pas atteignable. Le biais d'optimisme d'environ un quart entre modèle et exploitation. Et la dispersion de deux ordres de grandeur attribuée aux frontières sur une technologie.

::etat:: **Ce qui n'a pas été gagné, et il faut le dire aussi net.** **Aucune valeur n'est retenue pour aucune technologie.** **La quatrième frontière demandée — le service final — n'est couverte par aucune des deux sources**, qui s'arrêtent au point d'usage. **Le stockage n'est chiffré nulle part**, alors que l'intermittence en fait le poste décisif. **Et le démantèlement n'est présent que comme mention.**

## 6. Ce que le chapitre verse comme contrainte de conception

::etat:: **Sur le barème** [L11.C13]. Une qualification qui s'appuierait sur un rendement énergétique doit **nommer sa frontière, publier sa convention de conversion et donner sa plage de sensibilité**, faute de quoi elle n'est pas auditable. **Et elle doit porter sur une chaîne d'approvisionnement, non sur une famille technologique** — l'écart intérieur à la biomasse solide valant un facteur vingt.

::etat:: **Sur le simulateur** [L8.C37]. **Le Livre 13 ne pourra pas contenir un coefficient énergétique par technologie.** Il devra contenir, pour chaque technologie, **une frontière déclarée, une convention déclarée et une plage** — ce qui change la structure de données du simulateur avant même qu'il soit conçu. **C'est une exigence de conception, et elle n'y est pas inscrite.**

::hypothese:: **Sur la boucle que le chapitre a trouvée.** Le facteur de conversion vers l'énergie primaire dépend de la composition du réseau, donc de l'avancement de la transition. **Un barème calibré aujourd'hui devient faux à mesure qu'il réussit.** **Le corpus n'a aucun mécanisme de recalibrage**, et cette boucle est de même forme que celle que L24.C05 avait relevée sur les stocks : **une grandeur de référence que l'action modifie.**
