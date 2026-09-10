---
chapitre: L1.C12
titre: "La deuxième malédiction monétaire"
livre: 1
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: audit_contradictoire
revision_de_fond: 2026-09-03
autorite: preparatoire
citable: false
regime: hybride
sources_primaires:
  - ref: S1
    nature: donnees
    reference: "Eurostat, Material footprints — main indicators (env_ac_rme), consommation de matières premières (RMC) en tonnes par habitant, UE-27 et Allemagne, 2000-2023, mise à jour du 21 juillet 2026"
    url: "https://ec.europa.eu/eurostat/databrowser/view/env_ac_rme/default/table"
    etat_lecture: a_requalifier
  - ref: S2
    nature: donnees
    reference: "PNUE, Panel international des ressources, Global Resources Outlook 2024 — Bend the Trend, Nairobi, mars 2024, chapitre 2 (extraction mondiale de matières 1970-2024)"
    url: "https://www.unep.org/resources/Global-Resource-Outlook-2024"
    etat_lecture: a_requalifier
  - ref: S3
    nature: donnees
    reference: "Federal Reserve Bank of St. Louis, FRED, séries M2SL (M2, milliards de dollars, mensuel) et M2V (vitesse de circulation de M2, trimestriel), 1997-2025"
    url: "https://fred.stlouisfed.org/series/M2V"
    etat_lecture: a_requalifier
  - ref: S4
    nature: normatif
    reference: "Banque centrale européenne, communiqués du 8 juillet 2021 (plan d'action climatique issu de la revue stratégique), du 4 juillet 2022 (intégration du climat aux achats d'obligations d'entreprises et au collatéral) et du 19 septembre 2022 (scores climatiques ; orientation des achats à compter du 1er octobre 2022)"
    url: "https://www.ecb.europa.eu/press/pr/date/2022/html/ecb.pr220704~4f48a72462.en.html"
    etat_lecture: a_requalifier
  - ref: S5
    nature: donnees
    reference: "Umweltbundesamt / AGEE-Stat, part des énergies renouvelables dans la consommation brute d'électricité en Allemagne : 6,3 % en 2000, 51,8 % en 2023"
    url: "https://www.umweltbundesamt.de/en/indicator-share-of-renewables-in-gross-electricity"
    etat_lecture: a_requalifier
  - ref: S6
    nature: donnees
    reference: "Agence internationale de l'énergie, World Energy Investment 2025, 5 juin 2025"
    url: "https://www.iea.org/reports/world-energy-investment-2025"
    etat_lecture: a_requalifier
  - ref: S7
    nature: theorie
    reference: "I. Fisher (avec H. G. Brown), The Purchasing Power of Money, Macmillan, New York, 1911, chap. II p. 21 (MV = PT) et chap. III p. 48-53 (MV + M'V' = PT)"
    etat_lecture: a_requalifier
  - ref: S8
    nature: theorie
    reference: "J.-B. Fressoz, Sans transition. Une nouvelle histoire de l'énergie, Seuil, 2024"
    etat_lecture: a_requalifier
  - ref: S9
    nature: donnees
    reference: "PNUE, Emissions Gap Report 2025: Off Target, Nairobi, 4 novembre 2025 — émissions mondiales de gaz à effet de serre de 57,7 GtCO2e en 2024, en hausse de 2,3 %"
    url: "https://www.unep.org/resources/emissions-gap-report-2025"
    etat_lecture: a_requalifier
  - ref: S10
    nature: donnees
    reference: "Global Carbon Project, Global Carbon Budget — émissions de CO2 de l'Allemagne en comptabilité par la consommation, série reprise par Our World in Data"
    url: "https://ourworldindata.org/grapher/consumption-co2-emissions?country=~DEU"
    etat_lecture: a_requalifier
  - ref: S11
    nature: theorie
    reference: "Network for Greening the Financial System (NGFS), A call for action: Climate change as a source of financial risk, avril 2019 ; M. Carney, « Breaking the tragedy of the horizon », Bank of England, 29 septembre 2015 (risque de transition, actifs échoués)"
    url: "https://www.bankofengland.co.uk/-/media/boe/files/speech/2015/breaking-the-tragedy-of-the-horizon-climate-change-and-financial-stability.pdf"
    etat_lecture: a_requalifier
  - ref: S12
    nature: theorie
    reference: "P. Aghion, C. Antonin, S. Bunel, Le pouvoir de la destruction créatrice, Odile Jacob, 2020 (croissance par l'innovation et découplage)"
    etat_lecture: a_requalifier
verifications_en_attente:
  # — Sources ouvertes le 2026-09-03 (Claude) —
  # S1 : API Eurostat lue — RMC/hab UE-27 : 16,1 t (2000), 18,5 (2008), 14,8 (2010), 14,0 (2015), 14,9 (2019), 14,9 (2022), 13,7 (2023) ; Allemagne : 15,6 (2008), 14,1 (2010), 14,0 (2015), 14,8 (2019), 15,8 (2022), 14,3 (2023).
  # S3 : CSV FRED lus — M2V : 2,174 (T1 1997), max 2,192 (T3 1997), min 1,126 (T2 2020), 1,409 (T4 2025) ; M2SL : 7 514 Md$ (janv. 2008), 15 425 (janv. 2020), 22 355 (déc. 2025).
  # S10 : CSV OWID lu — Allemagne, CO2 par la consommation : 1 200 Mt (1990), 1 045 (2005), 1 037 (2008), 846 (2019), 839 (2022), 768 (2023).
  # S9 : existence et valeurs confirmées par recoupement — Deep Research affirmait à tort que l'édition 2025 n'existait pas.
  # S2, S4, S5 : recoupés sur pages institutionnelles.
  # — Objections de l'audit contradictoire (Gemini, 2026-09-03) traitées dans le texte —
  # 1. Troisième verrou : le mécanisme était inversé (une banque centrale qui craint l'inflation restreint le crédit) — réécrit : la stabilité des prix ferme la voie de l'érosion des dettes, non « traduit le crédit en volumes ».
  # 2. Actifs échoués : intégrés en § 3 avec [S11] ; réponse du corpus balisée.
  # 3. Additivité : deux flux concomitants ne prouvent pas l'additivité ; § 3 le dit et réduit la thèse à ce que les données portent.
  # 4. Marqueurs : ajoutés sur les deux fondements du § 3.
  # 5. Destruction monétaire par remboursement : intégrée — le Jevons monétaire porte sur l'expansion nette et le stock de capacités, non sur les flux bruts.
  # — Corrections critiques identifiées à la conversion —
  - "CRITIQUE — Le texte source affirmait que « l'empreinte matérielle des économies européennes […] continue de grimper » et que « l'empreinte matérielle par habitant de l'Allemagne a augmenté » sur 2000-2023. Eurostat [S1] dit l'inverse (UE-27 : −14,9 % depuis 2000, −25,9 % depuis 2008 ; Allemagne stable). Le chapitre s'appuie sur l'extraction mondiale [S2] et reformule la thèse."
  - "CRITIQUE — Le texte source déduisait de MV = PT que « plus de monnaie égale plus de transactions égale plus de pression matérielle » et affirmait qu'« aucune période prolongée de déconnexion » n'avait été observée. Faux : M2 américain ×2,97 entre janvier 2008 et décembre 2025, vitesse de M2 −30 % sur la même période et −49 % depuis 1997 [S3] ; zone euro, vitesse-revenu de M3 d'environ 1,76 (1999) à 0,81 (2020) selon les calculs de Deep Research sur les séries BCE, non ouvertes (API indisponible). L'argument est abandonné."
  - "CRITIQUE — « Masse monétaire mondiale d'environ 130 000 milliards de dollars » : aucun agrégat officiel de ce type (Deep Research : agrégations privées non additives entre devises). Retiré."
  - "CRITIQUE — « Francfort, mars 2021 » : plan d'action climatique du 8 juillet 2021 ; orientation des achats selon des scores climatiques à compter du 1er octobre 2022 [S4]. « Plusieurs centaines de milliards d'obligations à composante verte achetées » : non sourcé, retiré — le dispositif est un rééquilibrage des réinvestissements, non un volume dédié."
  - "CRITIQUE — Émissions importées de l'Allemagne « qui ont grimpé » : faux. En comptabilité par la consommation, les émissions de CO2 de l'Allemagne passent de 1 037 Mt (2008) à 768 Mt (2023) [S10] ; le solde net importé reste positif (de l'ordre de 100 à 130 Mt selon Deep Research, à confirmer sur le Global Carbon Atlas) mais l'empreinte carbone totale décroît. Le chapitre le dit."
  - "« Théorie quantitative formulée au 17e siècle » : Bodin (1568), Hume (1752) ; équation MV = PT chez Fisher (1911) [S7]. Corrigé."
  # — Données à confirmer —
  - "S2 : 30 Gt (1970) → 106,6 Gt (2024), 8,4 → 13,2 t/hab, +2,3 %/an — chapitre 2, p. 20-22 selon Deep Research ; ouvrir le rapport. Ne citer que l'édition 2024 (les éditions successives révisent les séries, cf. L1.C02)."
  - "Zone euro : vitesse de M3 — ouvrir la série BCE BSI.M.U2.Y.V.M30.X.1.U2.2300.Z01.E et le PIB nominal pour confirmer les valeurs avancées par Deep Research avant de les citer dans le corps du texte (elles ne le sont pas)."
  - "S11 : ouvrir le rapport NGFS 2019 ; le discours de Carney est ouvert pour L1.C09."
  - "S12 : ouvrage non ouvert ; cité pour l'objection de la dématérialisation, à confirmer."
  # — Objections acceptées comme limites —
  - "LIMITE — Facteurs de la vitesse de circulation (confiance, habitudes, techniques de paiement, répartition entre agents) : décomposition standard, non sourcée spécifiquement ; laissée en hypothèse balisée."
  - "LIMITE — « Aucun parti de gouvernement, aucune institution multilatérale ne porte » un autre régime d'émission : atténué en « peu présent », comme en L1.C09."
  - "LIMITE — Découplage par dématérialisation (Aghion) [S12] : mentionné en § 3 et renvoyé à L1.C03, où la question empirique est traitée."
  # — Sources non ouvertes par un humain —
  - "S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE)."
  # — Cohérence interne —
  - "COHÉRENCE — Le chapitre reprend la distinction découplage relatif / absolu de L1.C03, la contrainte de croissance et le reflux particulier de L1.C08 ; il n'ajoute pas de mécanisme monétaire distinct — la deuxième malédiction est l'articulation crédit vert / expansion nette / stock de capacités."
  - "COHÉRENCE — L1.C11 § 5 annonçait la deuxième malédiction comme « l'effet rebond […] opérant à l'échelle du régime monétaire » ; aligner L1.C11 sur la formulation retenue ici lors de sa prochaine révision."
  - "COHÉRENCE — L1.C08 § 2 cite l'inflation parmi les mécanismes qui absorbent la charge de la dette ; le troisième verrou du § 5 de ce chapitre s'appuie sur ce point (la stabilité des prix ferme cette voie). Vérifier la concordance."
  - "COHÉRENCE — jevons_monetaire au vocabulaire en nom provisoire ; définition alignée sur la reformulation."
  # — Renvois —
  - "Renvoi à ajouter vers L1.C13 (troisième malédiction) quand il existera"
  - "Renvoi à ajouter vers L1.C17 (seconde partie du livre) quand il existera"
resume: "La parade évidente à la première malédiction consiste à verdir le crédit. Ce chapitre établit pourquoi cette réorientation, réelle et utile, ne suffit pas, et il le fait en écartant l'argument quantitatif souvent avancé — plus de monnaie, plus de transactions, plus d'extraction —, que les séries monétaires réfutent. La formulation défendable tient en trois éléments : dans le régime actuel, le service d'un encours croissant exige une expansion nette du crédit, indifférente à sa composition ; les capacités que finance le crédit vert s'ajoutent, tant que les capacités anciennes restent solvables, au stock existant — et les actifs échoués qui les retireraient sont précisément ce que la stabilité financière cherche à éviter ; et la stabilité des prix ferme la voie par laquelle l'inflation érodait les dettes. Il en résulte des découplages sectoriels et nationaux réels — l'Europe a réduit son empreinte matérielle par habitant — sans découplage mondial absolu : l'extraction mondiale de matières a plus que triplé depuis 1970."
concepts: [malediction_monetaire, jevons_monetaire, decouplage, effet_rebond, reflux_monetaire, solvabilite_anticipee, creation_monetaire]
renvois: [L1.C03, L1.C08, L1.C11]
---

# La deuxième malédiction monétaire

Ce chapitre établit pourquoi verdir le crédit ne suffit pas, et il le fait en écartant d'abord un argument que le texte dont il est issu employait et que les données réfutent. La proposition : dans le régime d'émission actuel, la réorientation du crédit vers des activités moins dégradantes produit des découplages réels à l'échelle de secteurs et de pays, et ne produit pas de découplage mondial absolu, parce que le service d'un encours croissant exige une expansion nette du crédit indifférente à sa composition, parce que les capacités nouvelles s'ajoutent aux anciennes tant que celles-ci restent solvables, et parce que le régime ferme lui-même les deux issues qui relâcheraient cette exigence — l'érosion des dettes par l'inflation et leur destruction par défaut. La délimitation : le chapitre ne conteste ni les effets de la finance verte ni la possibilité d'un découplage local ; il conteste que la réorientation du crédit puisse, seule, faire décroître ce qu'elle déplace.

L1.C11 a décrit la première malédiction : à sa création, la monnaie est filtrée par la solvabilité anticipée. La parade évidente est de déplacer le filtre — de rendre solvable le vert et coûteux le brun. Ce chapitre examine ce que cette parade obtient et ce qu'elle ne peut pas obtenir.

## 1. Une intuition juste, et ce qu'elle a produit

L'intuition réformiste, dans sa formulation la plus solide, tient en une phrase : si les banques créent la monnaie par leurs décisions de crédit, il suffit de les inciter à décider autrement — fiscalité, bonus et malus prudentiels, taxonomie, obligations de publication, engagements de neutralité. Cette intuition est mise en œuvre depuis deux décennies, jusque dans les banques centrales : la Banque centrale européenne a adopté un plan d'action climatique en juillet 2021 et oriente depuis le 1er octobre 2022 ses réinvestissements en obligations d'entreprises selon des scores climatiques [S4].

Elle a produit des résultats réels. L'investissement mondial dans les technologies propres a atteint 2 200 milliards de dollars en 2025, le double de l'investissement fossile, alors que le rapport était inverse dix ans plus tôt [S6]. En Allemagne, la part des renouvelables dans la consommation brute d'électricité est passée de 6,3 % en 2000 à 51,8 % en 2023 [S5], et les émissions de dioxyde de carbone comptées selon la consommation — importations comprises — ont reculé de 1 037 millions de tonnes en 2008 à 768 millions en 2023 [S10]. Dans l'Union européenne, la consommation de matières premières par habitant, qui compte elle aussi les matières incorporées aux importations, a reculé de 16,1 tonnes en 2000 à 13,7 tonnes en 2023 [S1]. Ce ne sont pas des résultats « à peine mesurables » ; ce sont des découplages, sectoriels et nationaux, et le corpus ne les minimise pas.

Et pourtant deux courbes ne fléchissent pas. L'extraction mondiale de matières est passée de 30 milliards de tonnes en 1970 à 106,6 milliards en 2024 — de 8,4 à 13,2 tonnes par habitant [S2]. Les émissions mondiales de gaz à effet de serre ont atteint 57,7 milliards de tonnes d'équivalent CO2 en 2024, en hausse de 2,3 % [S9]. L'investissement fossile mondial se maintient à 1 100 milliards de dollars par an [S6]. Le découplage est réel là où on le mesure ; il n'est pas absolu là où cela compte, à l'échelle du monde.

::hypothese:: Ce contraste appelle une explication structurelle, qui ne soit ni la mauvaise foi des banquiers ni la timidité des régulateurs — l'une et l'autre existent, aucune ne suffit. Le corpus, à la suite du livre, nomme ce mécanisme le Jevons monétaire, par extension de l'effet rebond rencontré en L1.C03. Il faut d'abord dire ce que ce nom ne désigne pas.

## 2. L'argument qu'il faut écarter

Une version courante de l'argument s'appuie sur l'équation des échanges de Fisher [S7] : la masse monétaire multipliée par sa vitesse de circulation égale le niveau des prix multiplié par le volume des transactions. Si la vitesse et les prix sont stables, plus de monnaie signifie plus de transactions, donc plus de pression matérielle. Le texte dont ce chapitre est issu affirmait qu'aucune déconnexion durable entre masse monétaire et empreinte matérielle n'avait jamais été observée.

::etat:: Cette version ne résiste pas aux données. Aux États-Unis, M2 est passé de 7 500 milliards de dollars en janvier 2008 à 22 400 milliards en décembre 2025 — il a presque triplé — pendant que la vitesse de circulation de M2 tombait de 2,19 en 1997 à 1,13 en 2020, avant de remonter à 1,41 en 2025 [S3]. La monnaie a crû beaucoup plus vite que l'activité, et la vitesse n'a rien de stable. L'équation des échanges est une identité comptable, vraie par construction ; elle ne dit pas dans quel sens la causalité opère, et son terme de transactions inclut les échanges financiers, qui n'ont pas de contrepartie matérielle proportionnelle. On ne peut pas en déduire qu'un euro de plus soit un kilogramme de plus.

Le corpus abandonne donc cet argument. La deuxième malédiction ne tient pas à la quantité de monnaie ; elle tient à ce que le régime d'émission exige de l'activité, et à la manière dont le crédit vert s'y insère.

## 3. Le Jevons monétaire, formulé de manière défendable

Trois éléments le composent ; le premier est établi ailleurs dans le corpus, les deux autres sont des hypothèses de ce chapitre.

::etat:: **L'exigence porte sur le volume, non sur la couleur.** Dans un régime où l'encours de dette croît et où les revenus d'intérêts sont accumulés, le service de la dette exige des revenus croissants, donc une activité croissante (L1.C08 § 2, sous les conditions qui y sont posées). Cette exigence porte sur le volume total de l'activité solvable et lui est indifférente quant à sa composition : un crédit vert et un crédit brun servent également l'encours. Elle porte aussi sur un flux net : la monnaie créée par le crédit est détruite par son remboursement (L1.C08 § 1) ; ce que le régime exige n'est pas que le crédit brut augmente, mais que les crédits nouveaux excèdent les remboursements — que l'encours croisse.

::hypothese:: **Les capacités s'ajoutent tant que les anciennes restent solvables.** Fressoz a montré, pour l'énergie, que les sources se sont historiquement empilées au lieu de se remplacer [S8] (L1.C03). Le chapitre ne prétend pas que les flux d'investissement le démontrent : que 2 200 milliards aillent aux technologies propres et 1 100 aux fossiles en 2025 [S6] établit une coexistence, non une addition — nul ne sait ce que les fossiles auraient capté sans le crédit vert. Ce que le chapitre soutient est plus précis. Le crédit vert finance des capacités nouvelles — réseaux, batteries, panneaux, infrastructures — qui exigent cuivre, lithium, silicium, béton. Les capacités anciennes ne sont retirées que si elles cessent d'être solvables ; or elles servent le même encours, et les retirer avant leur terme — les *échouer*, au sens du risque de transition que les superviseurs ont identifié [S11] — c'est détruire du capital et, par les défauts, de la monnaie. C'est exactement ce que le mandat de stabilité financière cherche à éviter, et ce que l'orientation graduelle des achats de la Banque centrale européenne [S4] évite délibérément. Dans ce régime, l'échouage est le mécanisme de reflux que l'on redoute, non celui que l'on organise ; il reste partiel et lent, et le stock de capacités s'accroît net.

::hypothese:: **Le Jevons monétaire est la conjonction des deux.** Le crédit vert, parce qu'il est solvable, franchit le filtre de la première malédiction et contribue à l'expansion nette que le régime exige ; il finance des capacités nouvelles sans que les anciennes soient retirées au même rythme, parce que leur retrait est ce que le régime protège. À l'échelle d'un secteur ou d'un pays, la substitution peut l'emporter et le découplage être réel — l'Europe le montre [S1] [S10]. À l'échelle du monde, l'addition l'emporte : l'activité totale croît, et l'extraction croît avec elle sauf découplage absolu — dématérialisation de la valeur ajoutée, gains de qualité, essor des services [S12] —, dont L1.C03 examine la portée empirique et conclut qu'elle n'est pas observée globalement [S2]. Le crédit vert déplace la couleur du prélèvement ; il n'en commande pas le volume. (*Image : on a peint en vert une partie de la pompe ; la pompe débite davantage.*)

Cette formulation est plus étroite que celle du texte source, et elle est falsifiable : elle prédit que le découplage absolu apparaît localement et qu'il n'apparaît pas globalement tant que l'encours mondial croît et que les capacités anciennes restent solvables. Elle ne prédit pas qu'un euro de plus soit un kilogramme de plus.

## 4. Le cas allemand, relu

L'Allemagne est souvent citée comme démonstration, dans un sens ou dans l'autre. Il faut la lire avec les données.

Côté sectoriel, la réussite est nette : 6,3 % de renouvelables dans la consommation brute d'électricité en 2000, 51,8 % en 2023 [S5]. Côté carbone, les émissions comptées selon la consommation reculent — 1 037 millions de tonnes en 2008, 768 en 2023 [S10] —, ce qui contredit l'idée d'une décarbonation intérieure compensée par des émissions importées ; le solde net importé reste positif, mais l'empreinte totale décroît. Côté matières, la consommation de matières premières par habitant, importations comprises, est restée à peu près stable — 15,6 tonnes en 2008, 15,8 en 2022, 14,3 en 2023 [S1]. Le texte dont ce chapitre est issu affirmait qu'elle avait augmenté ; ce n'est pas ce que dit Eurostat.

::hypothese:: Ce que le cas montre est donc plus précis, et plus utile à la thèse : un découplage sectoriel spectaculaire et une décarbonation réelle n'ont pas fait baisser l'empreinte matérielle nationale, stabilisée à un niveau supérieur à la moyenne mondiale par habitant [S2] ; et l'Allemagne, comme tout autre pays, n'a pas cessé d'exiger la croissance de son activité, parce que sortir de cette exigence dans le régime actuel provoquerait une contraction financière qu'aucun gouvernement ne choisit. Le cas ne réfute pas la finance verte ; il montre sa limite : elle transforme la composition de l'activité, non l'exigence de son volume.

## 5. Pourquoi la malédiction se verrouille

::hypothese:: Quatre verrous tiennent la deuxième malédiction fermée, et ils sont tous des conséquences de la première.

**La masse monétaire est la contrepartie des dettes.** Chaque unité en circulation est une dette portée par quelqu'un (L1.C08). Réduire délibérément l'encours, c'est exiger des remboursements nets, donc une contraction — celle que la Grèce a subie (L1.C08 § 4). Aucun gouvernement ne la choisit.

**La vitesse de circulation ne se pilote pas.** Elle a chuté de moitié en vingt-cinq ans aux États-Unis [S3] sans qu'aucune politique l'ait décidé ; elle dépend, selon l'analyse standard, de la confiance, des habitudes, des techniques de paiement et de la répartition de la monnaie entre agents qui dépensent et agents qui accumulent (L1.C08 § 2).

**La stabilité des prix ferme la voie de l'érosion.** L1.C08 § 2 range l'inflation parmi les mécanismes qui absorbent la charge d'un encours croissant : elle en érode la valeur réelle. Le mandat des banques centrales est précisément d'empêcher cette érosion ; lorsque l'expansion du crédit menace les prix, elles relèvent leurs taux et restreignent le crédit. Cette issue-là étant fermée, il ne reste, pour servir un encours croissant, que la croissance réelle des revenus — ou le défaut, que le même régime traite comme un accident à prévenir. Le régime ne « traduit » pas le crédit en volumes ; il interdit les deux façons de ne pas le faire.

**L'alternative est peu présente dans le champ politique.** Sortir de l'exigence de croissance de l'encours sans contraction suppose un autre régime d'émission et de reflux (L1.C08 § 5, L1.C11 § 4) ; il est abondamment discuté dans la littérature (L1.C09, L1.C10) et peu porté par les partis de gouvernement et les institutions multilatérales.

::hypothese:: Ces verrous expliquent pourquoi la finance verte a été adoptée sans résistance par les institutions orthodoxes : elle ne remet pas en cause l'exigence de croissance de l'encours, elle en colore la sortie. Elle rassure, et elle occupe le débat sans le déplacer.

## 6. Portée

Le chapitre a établi que verdir le crédit produit des découplages réels — sectoriels, nationaux, y compris importations comprises — et ne produit pas de découplage mondial absolu, parce que le crédit vert contribue à l'expansion nette que le régime exige et finance des capacités nouvelles sans que les anciennes soient retirées au même rythme, leur retrait étant ce que le régime protège. Il a écarté l'argument quantitatif — plus de monnaie, plus d'extraction — que les séries monétaires réfutent, et donné à la deuxième malédiction une formulation falsifiable.

Deux malédictions sont posées. Aucune ne se résout par ajustement des règles en aval ; toutes deux tiennent au régime d'émission et de reflux. Il en reste une, qui ne concerne plus seulement les banques et les entreprises mais les États : elle noue la dette financière et la dette écologique en un piège dont aucun des deux termes ne se défait sans l'autre. C'est l'objet du chapitre suivant.
