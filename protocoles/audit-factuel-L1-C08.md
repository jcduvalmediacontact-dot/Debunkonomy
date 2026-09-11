# Audit factuel de L1.C08 — « Quand la dette crée une contrainte de croissance »

**Quatre passes, conduites par Claude à la demande de l'auteur, dans l'arbre
local, sans commit.** La première (2026-09-10) a audité les onze sources de
« Pourquoi la dette change tout » contre ses affirmations d'alors. La deuxième
(2026-09-11, matin) a refondu la structure en huit sections sous le nouveau
titre. La troisième (2026-09-11, après la note actualisée issue de l'échange
vocal) a corrigé les affirmations signalées, ouvert la version accessible de
Jackson et Victor, recherché le texte de Cahen-Fourot et Lavoie et réduit les
précédents partiels. La quatrième (2026-09-11, soir) reconstruit le chapitre
sur les cinq niveaux de l'architecture conceptuelle validée par l'auteur
(`protocoles/architecture-L1-C08.md`), ouvre dans le texte les quatre sources
qu'il a fournies — Jackson et Victor 2012, les thèses de Cottin-Euziol,
Sersiron et Deyris —, crée l'arbitrage `REGIME-NEGATIF`, requalifie les deux
entrées correspondantes de L1.C23, réancre les promesses P2 et P9 et renomme
le fichier. Une cinquième étape, le même soir, applique l'audit contradictoire
rendu par un modèle tiers et arbitré par l'auteur, passe le statut à
`audit_factuel` et enregistre l'état (§ 4 et § 6). Ce document décrit l'état
final.

**Règles appliquées.** Seul le texte de l'auteur, obtenu et lu directement,
vaut ouverture ; aucun résumé, aucun rapport tiers n'a été compté comme
lecture. Le manifeste des occurrences historiques a servi de piste, jamais de
verdict. Aucune détection de robot n'a été contournée : une réponse 403, 406 ou
une page « Making sure you're not a bot » clôt la tentative. Aucune source n'est
versée dans le dépôt : les fichiers acquis sont dans
`Documents/Codex/2026-09-10/audit-C08/` et `Documents/Codex/2026-09-11/audit-C08/`
(et, pour S1, S14 et S15, dans les dossiers d'acquisition du 2026-09-07) ; seuls
leurs empreintes SHA-256 et leurs métadonnées figurent ici. Les quatre sources
fournies par l'auteur ne sont pas des téléchargements : leur entrée porte la
mention « OUVERTE SUR LE FICHIER FOURNI PAR L'AUTEUR », avec la date et
l'empreinte, et aucune URL publique n'a été inventée pour elles. Pour chaque
citation, la page imprimée a été calculée par script à partir des folios du
texte extrait (Cottin-Euziol : page PDF − 10 ; Sersiron : − 12 ; Deyris : − 2),
et toutes les citations du chapitre ont été retrouvées mécaniquement dans les
textes acquis, en tolérant les césures et les sauts de page.
`corpus/.etat-corpus.json` a été mis à jour par le script le 2026-09-11, sur
décision de l'auteur (§ 6). Chaque source ne vaut que pour
l'énoncé précis qu'elle établit ; sa compétence est déclarée dans l'entrée de
source et dans le tableau ci-dessous.

## 1. La directive de reconstruction, point par point

| Point de la directive | Ce que le chapitre fait |
|---|---|
| Conclusion centrale (trois phrases) | reprise mot pour mot dans l'introduction ; la première phrase est fondée au § 2 (circulation, modèle S6, distinction intérêt / capital de S19), la deuxième au § 3 et au § 4 (S18, S19, S20, S3, S15, S16, S17), la troisième au § 5 (S14, S18) |
| Conséquence révélée par Deyris | reprise mot pour mot au § 7 comme décision de l'auteur (`::norme::`), précédée de ce que la thèse établit (`::etat::`, S21) et suivie de l'extension déclarée (carbone → incompatible écologique ; banques centrales → dispositif d'émission) et de la règle du corpus (reflux lourd, A44, arbitrage `REGIME-NEGATIF`) |
| Jackson et Victor ne sont plus des contradicteurs | § 2 : le modèle de 2015 « réfute seulement la nécessité arithmétique que produiraient les seuls intérêts » ; le texte de 2012 « dit ce que les mécanismes font ensemble » ; « les deux textes se complètent sans se contredire » |
| Cinq niveaux | § 1 (création et destruction) ; § 2 (absence d'impossibilité arithmétique) ; § 3 et § 4 (dynamiques cumulatives, finances publiques comprises) ; § 5 (transmission conditionnelle, empreintes importées) ; § 6 et § 7 (essentiel insolvable, réponse prospective de NEMO IMS) |
| Fonctions des sources | S18 : dépendance structurelle et dilemme (§ 3), service de la dette en récession (§ 4), découplage et taux d'intérêt / extraction (§ 5) ; S6 : contre-exemple à la nécessité des seuls intérêts (§ 2) ; S19 : destruction et fuite (§ 1), intérêt / capital (§ 2), renouvellement du crédit (§ 3), monnaie permanente (§ 7) ; S20 : encastrement contingent (§ 1, § 7), contrainte de solvabilité et report (§ 3), investissement vert sans recettes (§ 6), émission hors de tout rapport d'endettement (§ 7) ; S21 : phase-in / phase-out, limites du prudentiel et de l'informationnel, neutralité de marché, cohérence, légitimité démocratique (§ 7) ; S14 : faits biophysiques (§ 5) |
| Qualifier chaque affirmation | chaque paragraphe porte sa balise et dit s'il tient d'un fait, d'un modèle, d'une lecture institutionnelle, d'un énoncé raisonné, d'une déduction, d'une hypothèse ou d'une décision ; le § 8 récapitule |
| Signaler les affirmations sans preuve | § 3 : part des revenus absorbée par le service et accumulation des revenus financiers déclarées hypothèses ; `verifications_en_attente` les inscrit ; § 7 : l'instrument du régime négatif n'est pas fixé |
| Vérifier la règle limitant les financements dégénératifs | vérification faite (architecture § 6) : régime par le prix et engagement sur le canal propre existants, aucune règle sur les autres circuits ; l'auteur a choisi l'option 2 : arbitrage `REGIME-NEGATIF` créé, option 3 conservée en repli |
| Ne rien committer | rien n'a été commité avant la validation finale ; le 2026-09-11 au soir, l'auteur a autorisé des commits séparés (renommage, chapitre, architecture, audit, L1.C23, arbitrages, registre, état), sans aucun push |

## 2. Tableau de preuve S1 à S22

Colonnes : affirmation à établir ; passage exact ; édition ou version examinée
et preuve locale ; compétence ; hypothèses et limites ; rôle ; verdict.

| Réf | Affirmation à établir | Passage exact lu | Édition examinée, preuve locale (SHA-256) | Compétence | Hypothèses et limites | Rôle | Verdict |
|---|---|---|---|---|---|---|---|
| S1 | § 1 : le prêt crée un dépôt, la majorité de la monnaie naît ainsi, le remboursement la détruit, les achats d'actifs par les banques créent aussi des dépôts, prix des réserves et limite ultime. § 4 : un titre public n'entre dans la création de dépôts que si une banque l'achète. § 6 : les banques décident d'abord combien prêter selon les occasions rentables | p. 14 : « the majority of money in the modern economy is created by commercial banks making loans » ; « Whenever a bank makes a loan, it simultaneously creates a matching deposit in the borrower's bank account, thereby creating new money » ; « In normal times, the central bank does not fix the amount of money in circulation » ; « Monetary policy acts as the ultimate limit on money creation ». p. 15 : « setting the price of reserves — that is, interest rates » ; « supplied on demand by the Bank of England » ; « Banks first decide how much to lend depending on the profitable lending opportunities available to them ». p. 16 : « Just as taking out a new loan creates money, the repayment of bank loans destroys money ». p. 17 : « Banks buying and selling government bonds is one particularly important way in which the purchase or sale of existing assets by banks creates and destroys money » ; « When banks purchase government bonds from the non-bank private sector they credit the sellers with bank deposits » ; « The ultimate constraint on money creation is monetary policy » (pages 16 devenues 17 pour les deux citations sur les titres publics, correction du 2026-09-11 après relecture pour L1.C07) | *BoE Quarterly Bulletin* 2014 Q1, p. 14-27 ; `BoE-Money-creation-2014.pdf` `cfc4a626…992b62b2` ; texte `BoE-2014.txt` `43c2823c…831fbabf` | écritures et mécanismes de la monnaie bancaire | Royaume-Uni « en temps normal » ; rien sur les effets physiques ni sur la dette publique au-delà de l'achat de titres par les banques | indispensable | **ouverte**, 2026-09-11 |
| S2 | § 5 : formulation historique de l'écart entre lois mathématiques et physiques | p. 70 : « Debts are subject to the laws of mathematics rather than physics. […] On the contrary, they grow at so much per cent per annum, by the well-known mathematical laws of simple and compound interest. » | Allen & Unwin 1926, ch. IV, nouvelle impression 1983 ; `soddy-1926-djvu.txt` `f3229ee9…dfe00b83` ; `soddy-djvu.xml` `a1cc28a1…6dbb891a` ; `soddy-page_numbers.json` `9ae91f9d…205684bf` | formulation d'un principe | aucune mesure ; « Soddy fournit la formulation, non la mesure » | remplaçable | **ouverte**, 2026-09-10 |
| S3 | § 3 : l'encours nominal mondial croît (315 100 Mds $ au T1 2024 ; plus de 350 000 Mds $ au T1 2026) | p. 1 : « reaching a new record high of over $315 trillion — 333% of GDP » ; tableau 1 : 59,1 / 94,1 / 91,4 / 70,4 / 315,1 ; iif.com : « a record $348 trillion » ; « nearly $353T », « 305% » ; « over $350 trillion » | GDM 7 mai 2024 + textes publics 2026 ; `iif-gdm-may2024.pdf` `54beedd8…4c51f380` ; `iif-gdm-page.html` `58ee57d6…eb2a0b56` ; `iif-6581.html` `bb7ecb85…e13c81d8` | encours nominaux agrégés | rien sur la part des revenus absorbée par le service ; ratio 2026 non mobilisé | remplaçable | **ouverte**, 2026-09-10 |
| S4 | § 4 : concomitance grecque | valeurs de l'API : 247 275,7 ; 180 522,1 ; 181 479,1 ; 27,8 | jeux mis à jour le 2026-09-08 et le 2026-06-11 ; `eurostat-nama_10_gdp-EL.json` `10e11fd6…df1b0bac` ; `eurostat-une_rt_a-EL.json` `7df66109…8d5e7344` | niveaux macroéconomiques | aucune causalité | remplaçable | **ouverte**, 2026-09-10 |
| S6 | § 2 : un modèle stock-flux conclut que ni la création de crédit ni l'intérêt ne créent par eux-mêmes un impératif de croissance, sous des hypothèses énoncées ; d'autres incitations à la croissance existent ; ce résultat réfute seulement la nécessité arithmétique des seuls intérêts | p. 1 : « Contrary to claims in the literature, we find that neither credit creation nor the charging of interest on debt create a 'growth imperative' in and of themselves » ; p. 5 : « we assume balanced trade in this version of FALSTAFF » ; p. 7 : profits bancaires « distributed to household as dividends » ; p. 29 : « we found no evidence of a growth imperative arising from the existence of a debt-based money system per se » ; « we assumed a 'closed' economy, in which net trade was zero throughout. In addition, prices were excluded from the model » ; « Taxation is set so that government debt does not accumulate. Firms financing behaviour is determined in such a way as not to accumulate capital assets beyond those deemed necessary to satisfy expected demand » ; « there exists a number of other incentives towards growth within the architecture of the capitalist economy » ; p. 30 : « But this logic does not entail that interest-bearing money, in and of itself, creates a growth imperative » | PASSAGE Working Paper 15/01, 2015, ISSN 2056-6255, 31 p., dépôt Open Research de Surrey, « may be reproduced as long as the reference source is cited » ; `jackson-victor-wp-surrey.pdf` `c0d5da27…9a3531ef` ; rapport à la version publiée : même étude, titre différent, même phrase de résumé à un mot près ; la version publiée n'est pas lue | résultat d'existence dans un modèle déterminé | économie fermée, sans prix, dette publique non accumulée, capital non accumulé, sans logement ; rien sur les économies réelles | indispensable au § 2 | **ouverte**, 2026-09-11 |
| S7 (retirée le 2026-09-11) | anciennement § 2 : conclusion de Cahen-Fourot et Lavoie 2016 rapportée d'après le résumé | résumé seulement (reproduction tierce) : « We argue that interest rates set to zero is an unnecessary condition to reach a steady-state economy » | *Ecological Economics* 126, 2016 ; `degrowth-cfl.html` `8fa92d5c…e838ce2f`. Toutes les voies publiques essayées : éditeur 403 ; HAL sans fichier, lien ISTEX déclaré par HAL renvoyant à une connexion institutionnelle ; RePEc sans fichier ; thèse tel-02301843 derrière la page anti-robot, non contournée ; Semantic Scholar « CLOSED » ; portail de recherche de Roskilde sans fichier ; page du programme de Leipzig 2014 retrouvée dans l'archive du Web, mais les pages des communications n'y sont pas archivées ; deux textes de Lavoie fournis par l'auteur sans rapport avec le sujet | critique post-keynésienne du taux nul | résumé seulement ; le § 2 porte déjà l'objection de l'accommodation sans elle | supprimable | retrait, décision de l'auteur |
| S9 | § 4 : hausse des suicides concomitante, causalité non établie | « The mean suicide rate overall rose by 35% between 2010 and 2012 » ; « It is never possible, with an observational study, to establish causality » ; « The passage of new austerity measures in June 2011 marked the beginning of significant, abrupt and sustained increases in total suicides (+35.7%, p<0.001) » | BMJ Open 5, e007295 et e005619, versions Europe PMC ; `PMC4386238.xml` `029b5c45…903932cb` ; `PMC4316557.xml` `5b645052…eb2f4bad` | épidémiologie descriptive | les auteurs excluent la causalité | remplaçable | **ouverte**, 2026-09-10 |
| S14 | § 5 : pas de découplage absolu mondial ; empreinte matérielle vs consommation intérieure ; déplacement des impacts par le commerce | p. xiv : « There has so far been no evidence of widespread absolute decoupling at the global level » ; « Through global trade, high-income countries displace environmental impacts to all other income country groups » ; p. 4 : « between 2015 (reference year of the 2019 edition) and 2023 there was no absolute decoupling of any environmental impact on the global scale, and all impacts increased in absolute terms with only a few temporary exceptions » ; p. 24, tableau 2.1 : définitions de MF et DMC | GRO 2024, ISBN 978-92-807-4128-5 ; `PNUE-Global-Resources-Outlook-2024.pdf` `0f1e7d53…49994d48` | pressions physiques mondiales | rien sur la monnaie ; « 106.6 billion tonnes in 2024 » non repris | indispensable | **ouverte**, 2026-09-11 |
| S15 | § 4 : les États s'abstiennent de la sobriété par dépendance revendiquée à la croissance fiscale | p. 34 : « recent research suggests that states have so far refrained from strategies of sufficiency as these may contradict their claimed structural dependence on economic growth for the generation of tax revenue, employment and consumption-based political legitimacy » ; p. 30 : « although many articles conclude that absolute decoupling is empirically rarely found, the recommendations to a large extent stick to a green growth repertoire » | Haberl et al., *ERL* 15, 065003, 2020, version publiée CC BY 4.0 ; `L26-04_Haberl_Decoupling_Review_Part_II_2020.pdf` `ede22f83…4164ddb9` | synthèse de 835 articles | rapporte « recent research » ; le chapitre l'appelle « hypothèse appuyée » | indispensable au § 4 | **ouverte**, 2026-09-11 |
| S16 | § 4 : titres refinancés ; charge de la dette dépense du budget général | p. 24 : « Pour 2026. Le besoin de financement est principalement constitué d'un déficit à financer de 124,4 Md€ et d'amortissements de titres à moyen/long terme qui devraient atteindre 175,8 Md€ » ; « Ce besoin de financement sera principalement couvert par un volume d'émissions de dette à moyen/long terme de 310,0 Md€ » ; p. 30 : « 58,0 Md€, soit 7,2 Md€ de plus que la charge aujourd'hui prévue pour 2025 » ; p. 31 : « un effet volume de +4,1 Md€ » | PAP « Engagements financiers de l'État », PLF 2026 ; `pap-2026-engagements-financiers.pdf` `2715898f…76314e34` | tableau de financement et charge de la dette, France, 2026 | un pays, un exercice, des prévisions | indispensable au § 4 | **ouverte**, 2026-09-11 |
| S17 | § 4 : deuxième poste de dépenses en 2026, premier à terme | « deuxième poste de dépenses du budget de l'État en crédits de paiement (CP) après la mission « Enseignement scolaire » » ; « devrait devenir à terme le premier poste de dépenses » ; « atteindre la barre des 100 milliards d'euros » | Sénat, rapport général n° 139 (2025-2026), tome III, annexe 12 ; `senat-l25-139-312.html` `daaf0336…c74990b7` | rang de la charge ; projection parlementaire | projection « à politique budgétaire inchangée » | remplaçable | **ouverte**, 2026-09-11 |
| S18 (nouvelle) | § 3 : besoin structurel de croissance, mécanisme productivité-emploi, croissance facteur structurel de la stabilité, dilemme stabilité / viabilité ; § 4 : service de la dette en récession ; § 5 : découplage jugé peu crédible, taux d'intérêt et extraction, consumérisme stimulé par la dette | p. 2 : « Pour développer une macroéconomie écologique crédible, le principal défi à relever vient du besoin structurel de croissance économique, implicite dans les économies modernes. » ; « La stabilité économique repose sur une croissance économique perpétuelle alors que la viabilité écologique est déjà mise à mal par les niveaux d'activité économique. » ; « dès que cela n'est plus le cas, la hausse de productivité se traduira par une baisse de la demande de main-d'œuvre » ; « Les revenus finissent par chuter. L'investissement recule. Le chômage augmente davantage et l'économie entre alors dans une spirale de récession » ; « Le service de la dette dans une économie en déclin est au mieux problématique car le seul remboursement des intérêts occupe une proportion relativement grande du revenu national. » ; p. 3 : « Pour résumer, les économies modernes sont inévitablement poussées vers toujours plus de croissance. » ; « Dans une économie de la croissance, celle-ci constitue un facteur structurel de la stabilité. » ; « résister à la croissance s'apparente à courir le risque d'un effondrement économique et social, la poursuivre sans fin c'est mettre en danger les écosystèmes dont nous dépendons pour notre survie à long terme. » ; « Tout indique pourtant que cette hypothèse est loin d'être crédible. » ; p. 6 : « une augmentation du taux d'intérêt sur ce type de dépôts constituera une incitation à extraire les ressources à un rythme accru afin de générer des profits élevés. L'inverse est vrai quand le taux d'intérêt diminue. » ; « Une macroéconomie qui reposerait sur une expansion continue d'un consumérisme matérialiste, stimulé par la dette, est écologiquement intenable. » ; p. 10 : « La stabilité du système financier exige-t-elle une croissance de l'économie “réelle” ? » | P. Victor et T. Jackson, « Pour une macroéconomie écologique », « les notes Veblen » de l'Institut Veblen (publications hors commerce), octobre 2012, 12 p., « Publié sous Creative Commons » ; communication pour la conférence de l'INET, Berlin, avril 2012 ; trad. Valérie Denot ; deux sections « légèrement adaptées de Jackson (2011) et Jackson (2009) » ; fichier fourni par l'auteur, copie sur son Drive ; `jackson-victor-2012-pour-une-macroeconomie-ecologique.pdf` `2640ff9b…eaeae459` ; URL publique vérifiée le 2026-09-11 par téléchargement direct depuis veblen-institute.org, `jackson-victor-2012-veblen.pdf` d'empreinte identique | énoncé raisonné de la dépendance structurelle et du dilemme ; principe d'économie des ressources | aucune mesure ; chiffres de découplage repris de Jackson 2009 ; question de la stabilité financière laissée ouverte par les auteurs ; le chapitre l'emploie comme hypothèse appuyée, jamais comme fait | indispensable au § 3 | **ouverte**, 2026-09-11 |
| S19 (nouvelle) | § 1 : le remboursement est une fuite hors du circuit, la monnaie étant détruite ; § 2 : l'intérêt reflue, le capital remboursé fuit ; salaires et intérêts n'entrent pas dans la détermination des profits globaux ; § 3 : investissements toujours plus importants, taux de croissance requis des investissements croissant, crédits toujours plus importants relativement à la production, probabilité de crise croissante, appel à des études empiriques ; § 7 : monnaie permanente, monétisation d'une part des dépenses publiques à montant décidé à l'avance | p. 92 : « Les salaires et les intérêts payés sur les crédits bancaires représentent à la fois un coût de production pour les entreprises et une source de revenus, ils n'entrent donc pas dans la détermination des profits globaux » ; p. 93 : « Ces remboursements constituent clairement une fuite hors du circuit puisque la monnaie correspondante est détruite et ne peut donc pas refluer vers les entreprises » ; p. 104 : « Le remboursement d'un crédit bancaire représente une dépense pour l'entreprise, mais ne génère pas de revenus dans l'économie, la monnaie correspondante étant détruite » ; p. 140 : « Des investissements toujours plus importants devront être émis pour permettre aux revenus générés par la production d'égaliser la valeur de la production » ; p. 186 : « Le paiement des intérêts représente un flux des entreprises vers les banques, qui dépenseront à leur tour cet argent, augmentant les recettes des entreprises. Cela ne modifie donc pas le principe du multiplicateur. Le remboursement du capital, au contraire, constitue une fuite hors du circuit économique » ; p. 195 : « Le principal résultat que nous obtenons est alors que le taux de croissance requis des investissements doit progressivement s'élever au cours d'une phase de croissance » ; p. 202 : « La manière dont la monnaie est créée et détruite apparaît alors avoir une influence décisive, et particulièrement déstabilisante, sur la dynamique des économies » ; p. 207 : « une monnaie que l'on pourrait qualifier de permanente, par opposition à la monnaie bancaire qui a une durée de vie temporaire » ; p. 220-221 : « l'émission de crédits bancaires toujours plus importants, relativement à la valeur de la production, était nécessaire pour éviter qu'une crise ne se développe » ; « la probabilité d'occurrence d'une crise augmente dans nos modèles à mesure que la phase de croissance de l'économie considérée se prolonge » ; p. 221 : « conduire des études empiriques afin de confirmer ou infirmer les résultats obtenus » ; p. 222 : « consisterait en la monétisation d'une partie des dépenses publiques » ; « décidé à l'avance et peu susceptible de varier » | thèse, Université de Limoges, LAPE, soutenue le 24 septembre 2013, dir. A. Sauviat, rapporteurs L.-P. Rochon et M. Seccareccia ; PDF intégral fourni par l'auteur, 252 pages, couche de texte complète, pagination imprimée = page PDF − 10 ; `cottin-euziol-these.pdf` `42876dcc…eaf25168` | résultats de deux modèles théoriques d'une économie monétaire de production | aucune épreuve empirique, ce que l'auteur dit lui-même ; le chapitre les emploie comme résultats de modèle | indispensable aux § 1 à § 3 | **ouverte**, 2026-09-11 |
| S20 (nouvelle) | § 1 et § 7 : l'encastrement de la création monétaire dans le crédit est contingent, on peut s'en défaire, émission hors de tout rapport d'endettement ; § 3 : contrainte de solvabilité, endettement toujours accru, report par la baisse continue des taux jusqu'au plancher, croissance reposant sur une dégradation de la solvabilité ; § 6 : investissement vert sans recettes finançable seulement par subvention | résumé : « redéfinie comme encastrement de la création monétaire dans le marché du crédit, est au contraire une construction sociale contingente et instable » ; « toute création monétaire implique un alourdissement du fardeau de la dette, jusqu'à buter sur la contrainte de solvabilité des agents » ; « nous proposons à la suite de Fisher (100% Money) un régime d'émission exogène, brisant l'encastrement de l'institution monétaire dans le marché de la dette » ; p. 5 : « ne passera pas par une modélisation mathématique » ; p. 9-10 : « Le fardeau de la dette des agents s'alourdit progressivement, mais leur contrainte de solvabilité est sans cesse repoussée par une baisse continue des taux » ; « les taux nuls constituent par convention un plancher que les Banques centrales ne peuvent pas percer sans remettre en cause l'encastrement de la monnaie dans la dette » ; « permet d'enjamber la contrainte de solvabilité des agents en injectant l'argent dans l'économie sans contrepartie, en dehors de tout rapport d'endettement » ; p. 28 : « les pousse à ne pas s'endetter assez par rapport aux conditions de la stabilité macroéconomique » ; p. 57 : « Les agents économiques doivent s'endetter toujours davantage pour permettre l'accroissement de la masse monétaire au fil de la croissance, or leur contrainte de solvabilité s'avère toujours plus difficile à surmonter au fil du temps. » ; p. 98 : « La création monétaire par le crédit n'est donc pas selon nous une nécessité logique première, une nécessité fonctionnelle de toute économie monétaire de production, comme le pensent circuitistes et postkeynésiens (on y reviendra), mais un état de fait historique contingent. » ; p. 99 : « on peut donc s'en défaire » ; p. 296 : « la principale réponse à la contrainte de solvabilité » ; p. 305 : « la croissance repose sur une dégradation progressive de la solvabilité des agents, donc une érosion de la confiance » ; p. 388 : « La création monétaire se ferait en dehors du marché et en dehors de tout rapport d'endettement. » ; p. 405-406 : « Prenons le cas d'un investissement vert qui ne génère pas, ou peu, de recettes supplémentaires » ; « l'investissement ne peut alors se faire, sauf s'il est subventionné » | thèse, Université Paris 1 Panthéon-Sorbonne, soutenue le 3 février 2021, codir. J. Lallement et A. Orléan ; jury J. Couppey-Soubeyran, L. Desmedt, G. Giraud, J.-F. Ponsot ; PDF intégral fourni par l'auteur, 448 pages, pagination imprimée = page PDF − 12 ; `sersiron-these.pdf` `cad0d623…00b9e042` | lecture institutionnelle et historique, épistémologie de la Régulation | aucune mesure, la thèse le dit elle-même ; le chapitre l'emploie comme lecture institutionnelle | indispensable aux § 3 et § 7 | **ouverte**, 2026-09-11 |
| S21 (nouvelle) | § 7 : les politiques promotionnelles se concentrent sur le phase-in et jamais sur le phase-out ; le prudentiel est compatible avec la poursuite des financements carbonés ; l'Europe n'a employé que l'information, insuffisante ; la neutralité de marché est un mythe et un choix de fait pour le polluant ; trois familles d'instruments ; phase-out accéléré, mesures sur les financements nouveaux, cohérence entre tous les acteurs, décision démocratique | p. 36 : « even more attention should be paid to closing the tap of polluting financial flows » ; p. 39 : « all focus on the development of green financial flows (the phase-in), and never tackle the problem of curtailing dirty financial flows (the phase-out) » ; « the development of a green financial niche must not distract from the need to discourage carbon-based investments, whose termination is the only relevant criteria for climate stabilization » ; p. 40 : « The prudential approach is perfectly compatible with a continuation - or even with an acceleration - of carbon-intensive funding, as long as it is provided by institutions that are strong enough to bear the losses in the event of a transition shock. » ; p. 41 : « Halt new funding of dirty assets as fast as possible » ; p. 63 : « direct controls on credit allocation (quantity-based) » ; p. 71 : « In Europe, informational instruments have been the only tools used by political and delegated authorities » ; p. 81 : « The de jure principle of not choosing leads to a de facto choice in favour of polluting activities. » ; p. 82 : « Such decisions need strong democratic legitimacy and are a matter for governments and parliaments » ; p. 84 : « are unlikely to either fully capture inherently uncertain climate-related risks or to push financial resources towards sustainable activities with the sufficient strength » ; p. 188 : « this neutrality is a myth (van 't Klooster & Fontan, 2020) » ; p. 195 : « current interventions are in fact credit policy without democratic control » ; p. 228-229 : « data and informational policies are a necessary tool, but a non-sufficient one » ; « the current misconception that promotional policies can focus solely on supporting the development of green activities must be challenged » ; « repressive promotional policies can and should be much stricter, for example by requiring that all new funding for fossil fuel extraction projects be financed without any leverage, by limiting their number or by banning certain types of project financing altogether » ; « What is needed is accelerated phase-out » ; « these repressive promotional interventions can only be effective if they are deployed as a coherent set, targeted at all types of financial actors to avoid regulatory arbitrage » ; p. 231 : « This choice can only be made democratically, and one cannot expect everything from central banks. » | thèse en anglais, Université Paris Nanterre, EconomiX, soutenue le 10 juillet 2023, dir. L. Scialom ; jury C. Couharde, L. Le Maux, J.-F. Ponsot, J. Couppey-Soubeyran ; chapitre II issu de Baer, Campiglio et Deyris (Ecological Economics, 2021), chapitre III publié dans New Political Economy (2023) ; PDF intégral fourni par l'auteur, 297 pages, pagination imprimée = page PDF − 2 ; `deyris-these-2023.pdf` `ca17b188…78f355c7` | économie politique des banques centrales, climat, Europe ; principes et cas | aucune mesure d'efficacité des encadrements cités ; l'extension du carbone à l'incompatible écologique et des banques centrales à un dispositif d'émission est déclarée comme extension du corpus | indispensable au § 7 | **ouverte**, 2026-09-11 |
| S22 (nouvelle) | § 2 : dans un modèle minskyen, croissance et croissance nulle peuvent chacune connaître des régimes stables ou instables selon la conduite de l'endettement des entreprises ; § 8 | p. 1 : « We confirm that, with or without growth, there can be both stable and unstable scenarios. To maintain stability, firms must not change their debt levels or target debt levels too quickly. » ; p. 2 : « is capable of producing both stable and unstable scenarios, depending on firms' behaviour in relation to debt » ; p. 4 : « designed to model 'normal times', and the onset of a crisis, but not the behaviour of the economy after crisis onset » ; p. 14 : « given a level of productivity growth, it is debt behaviour that determines the stability of the model economy » ; « Although the model is very simple » ; « We have held other variables constant, notably the interest rate, and (implicitly) prices » ; « in the many stable scenarios plotted, the profit share (defined as output minus wages minus interest) is positive, and thus firms are (at the aggregate macro level) able to keep up with interest payments to prevent an exponential growth of debt » ; p. 15 : « there is no mathematical reason to expect a demarcation in behaviour between scenarios in which the productivity growth parameter is zero and in which it takes a small positive value » ; « no stable zero growth scenario for the original Keen (1995) model, on which investment decisions are based purely on profit » | A. B. Barrett, prépublication arXiv:1704.08161v3 [q-fin.EC], 7 novembre 2017, 23 p., University of Sussex ; version de travail de l'article d'Ecological Economics, 146, 2018, p. 228-239, non lue ; `barrett-2017-arxiv-v3.pdf` `5d365bbf…08129ccd` | résultat de stabilité dynamique dans un modèle minskyen simple | quatre variables, taux d'intérêt et prix constants, consommation résiduelle ; l'auteur fixe l'usage : ce modèle seul, aucune généralisation | complémentaire de S6 au § 2 | **ouverte**, 2026-09-11 |
| S5, S8, S10 (retirées le 2026-09-10) | — | non lues ou inaccessibles | Lavoie 2014 ; S&P 2024 ; Moore 1988 | — | — | supprimables | retrait |
| S11, S12 (retirées le 2026-09-11) | anciennement § 7 : mécanisme de fonte, chiffres de Wörgl | transcriptions lues, non confrontées à une édition originale | `Gesell-NaturalEconomicOrder.pdf` `8f83ef1d…c2ca76c9` ; `fisher/stamp4.html` `1a7b2f42…cf193932` | analogue d'un composant périphérique | le détail est renvoyé au Livre 16 | supprimables | retrait |
| S13 (retirée le 2026-09-11) | anciennement § 7 : greenbacks | scan govinfo lu | `legal-tender-act-1862-govinfo.pdf` `0842c70c…89d4e24e` | texte d'une émission publique | plus aucune affirmation ne le mobilise | supprimable | retrait |

Acquis mais non mobilisés : `senat-l25-139-217.html` `a7c0c96f…b1f7f059` (répète le
tableau de financement du PAP) ; `soas-wp159.pdf` (le lien RePEc de la note
pointe vers un document de travail sans rapport : Warren-Rodríguez, *An
exploration of factors shaping technology-upgrading efforts in Mozambican
manufacturing firms*, SOAS n° 159) ; Légifrance (LFI 2026, LOLF), Agence France
Trésor et theses.hal.science refusent la requête automatique ; `lavoie-psl.pdf`
`d45751ab…ffc3e203` (fourni par l'auteur le 2026-09-11 pour S7 : M. Lavoie,
« Post-Keynesian economics 50 years after the Eichner and Kregel paradigm
article: Coherence or incoherence? », PSL Quarterly Review, 79 (316), mars
2026, p. 3-20, CC BY-NC-ND ; texte extrait en entier, première page lue,
corps interrogé par mots-clés ; ni économie écologique, ni état
stationnaire, ni taux nul, ni citation de Cahen-Fourot et Lavoie 2016 : sans
usage pour S7) ; `ojs-96-374.pdf` `dd5e7bc9…11bae382` (fourni par l'auteur le
2026-09-11 pour S7 : M. Lavoie, « Rethinking monetary theory in light of Keynes
and the crisis », Brazilian Keynesian Review, 2 (2), 2016, p. 174-188 ; texte
extrait en entier, première page lue, corps interrogé par mots-clés : aucune
occurrence d'économie écologique, d'état stationnaire ou de taux nul ; sans
usage pour S7).

Empreintes complètes des fichiers cités :

```
cfc4a6262631e7b5582a427aec1215c1568f240c45d54696bb9a2093992b62b2  BoE-Money-creation-2014.pdf
43c2823ccde52f804d3c5b15ebcf9aa661746ab03816d68336e9f8cb831fbabf  BoE-2014.txt
f3229ee989372d5769f87f878cf19ac25cfb077d99f38656c4354244dfe00b83  soddy-1926-djvu.txt
a1cc28a169ae89ca77f56d9c7d9855a10dd56b682eb11b87ff5ac7f26dbb891a  soddy-djvu.xml
9ae91f9d912eb86b4648f609e20f7fdda1b1428ebccf38ac7c1966ec205684bf  soddy-page_numbers.json
54beedd833851ec7eb70c48f36b8938617de5197a4c5c8106c5d35e44c51f380  iif-gdm-may2024.pdf
58ee57d6261aca435db72053c97f3971830f1ed61dc5f71db05aabadeb2a0b56  iif-gdm-page.html
bb7ecb85f621453348238f41a0f94d98ececa14bcf2adfdf8425fd2ae13c81d8  iif-6581.html
10e11fd6f840ad91b7d24585ba2353c1868ca53dd84986f22e9e3377df1b0bac  eurostat-nama_10_gdp-EL.json
7df661096a853a50e793b84fd5d4f8bddb4849097506ae7ff7dd29088d5e7344  eurostat-une_rt_a-EL.json
b351c3c155c82229d85ae7c7eff77e5c5d9de1c5bc20573ca1ba79895bd6b58d  spglobal.html
029b5c45779b7bdd6a447baebd49635e9dda82374da2108e1ef49be1903932cb  PMC4386238.xml
5b645052c902f9d44f7ce6dc43214e12f33b59f7441652bd9e28d36aeb2f4bad  PMC4316557.xml
8f83ef1de716a9bbc3f05b056ac1642108395a032f628764fc8825f5c2ca76c9  Gesell-NaturalEconomicOrder.pdf
1a7b2f4233c76f013b07069d3f36e1b644d7b4a9622dbd48e157ef81cf193932  fisher/stamp4.html
0842c70c49eeba32b8ff49fec351f2113b7e3e6c5e997a67600f730d89d4e24e  legal-tender-act-1862-govinfo.pdf
0f1e7d5366e7e3d18209184fd35bd1e31011641a1cd9b33034b4537049994d48  PNUE-Global-Resources-Outlook-2024.pdf
ede22f8315b6e41cd74ca9d58be2bc54ccf04d999055c80da3318cfe4164ddb9  L26-04_Haberl_Decoupling_Review_Part_II_2020.pdf
2715898f5466cd9089dad97d99b0ad0365a54eea9b3bdb2cdfb3f3bb76314e34  pap-2026-engagements-financiers.pdf
daaf03364bfd092a0c68ad4197c11a158d28813d09de4b1cfc129281c74990b7  senat-l25-139-312.html
a7c0c96f74062302e51e25ef26a8ba01cd5a8b04ea215151fe52be12b1f7f059  senat-l25-139-217.html
c0d5da276c26c7a7a2c003f10a519d7391e94bb8871cba65ab2a72479a3531ef  jackson-victor-wp-surrey.pdf
8fa92d5c1af8835cb44546c1f143d0aab66403f3abab0c817943dec8e838ce2f  degrowth-cfl.html
2640ff9b1d201f084405b27a91df548026cdf4ffecad8aca18643e17eaeae459  jackson-victor-2012-pour-une-macroeconomie-ecologique.pdf
42876dcca806ed61c92cdb436a5804fdbe8820dc8ade316914482f28eaf25168  cottin-euziol-these.pdf
cad0d62353650e6e04fbc883234b0ef633491a25311e0faf4168a3db00b9e042  sersiron-these.pdf
ca17b1884ae59034df3dcb741ee40ef0972f88efa130506f91cc605078f355c7  deyris-these-2023.pdf
d45751abf78ac37e637beafddb54f6d791fd001d1f8172497ebdfd19ffc3e203  lavoie-psl.pdf
dd5e7bc9114b1c087b546665b1f6bf0efa630950ab879bcc2e2758da11bae382  ojs-96-374.pdf
5d365bbf1d8da7dc068a7d1a4acb1f20aa26f8d0231057b47fc4a1ff08129ccd  barrett-2017-arxiv-v3.pdf
```

## 3. Table des affirmations centrales et de leur appui

Nature : **F** fait sourcé (source et passage) ; **M** résultat de modèle lu ;
**L** lecture institutionnelle lue ; **E** énoncé raisonné d'une source lue ;
**D** déduction explicitée ; **H** hypothèse conditionnelle du corpus ; **N**
décision de l'auteur ; **P** proposition prospective à soumettre à réfutation.

| § | Affirmation centrale | Nature | Appui |
|---|---|---|---|
| intro | La dette à intérêt ne crée pas, par une identité comptable isolée, une obligation universelle de croissance | D + M | circulation (§ 2) ; S6 ; S19 p. 186 et 92 |
| intro, § 3 | Intégrée aux mécanismes d'emploi, de rentabilité, d'investissement, de refinancement et de stabilité budgétaire, elle contribue à une dépendance structurelle à la croissance | H appuyée (E + M + L + F) | S18 p. 2-3 ; S19 p. 140, 195, 202, 220-221 ; S20 résumé, p. 9-10, 57, 296, 305 ; S3 ; S15 ; S16 ; S17 |
| intro, § 5 | Sans découplage absolu mondial suffisamment rapide et étendu, cette dépendance entretient les pressions matérielles et écologiques | H | S14 pour la condition ; S18 p. 3 et 6 comme énoncé ; le maillon lui-même est une hypothèse |
| § 1 | Un prêt crée généralement un dépôt et une créance ; la majorité de la monnaie naît ainsi ; le remboursement la détruit | F | S1, p. 14 et 16 |
| § 1 | Le remboursement est une fuite hors du circuit, la monnaie étant détruite | M | S19, p. 93 et 104 |
| § 1 | Les dépôts naissent aussi d'achats d'actifs ; toutes les monnaies n'ont pas pour contrepartie une dette privée portant intérêt | F | S1, p. 17 |
| § 1 | La Banque centrale fixe le prix des réserves, non la quantité ; limite ultime | F | S1, p. 14, 15, 17 |
| § 1 | Le régime de crédit est un état de fait historique contingent, non une nécessité logique | L | S20, p. 98 |
| § 1 | Le reflux du régime de crédit est particulier ; le corpus lui oppose un reflux collectif | N, P | vocabulaire ; L1.C21 ; Livre 2 |
| § 2 | Une même unité acquitte plusieurs charges d'intérêt si elle circule ; l'impossibilité arithmétique est fausse | D | raisonnement explicité |
| § 2 | L'intérêt reflue et ne modifie pas le multiplicateur ; le capital remboursé fuit ; salaires et intérêts n'entrent pas dans la détermination des profits globaux | M | S19, p. 186 et 92 |
| § 2 | La circulation ne démontre pas un équilibre stationnaire complet ; cela exige un modèle | D | énoncé de l'auteur |
| § 2 | Un modèle stock-flux exhibe des états quasi stationnaires avec dette et intérêts, sous hypothèses énoncées ; d'autres incitations existent | M | S6, p. 1, 5, 7, 29, 30 |
| § 2 | Ce résultat réfute seulement la nécessité arithmétique des seuls intérêts ; 2012 et 2015 se complètent | D | S6, p. 29-30 ; S18 ; directive de l'auteur |
| § 2 | Cahen-Fourot et Lavoie concluent qu'un taux nul n'est pas nécessaire | rapporté | S7 candidate, résumé seulement, dit dans le texte |
| § 2 | Le débat est réellement controversé | H | formulation de l'auteur ; L1.C23 comme carte, non comme preuve |
| § 3 | Besoin structurel de croissance ; mécanisme productivité-emploi ; croissance facteur structurel de la stabilité ; dilemme | E | S18, p. 2-3 |
| § 3 | Le taux de croissance requis des investissements s'élève au cours d'une phase de croissance ; crédits toujours plus importants ; probabilité de crise croissante | M | S19, p. 140, 195, 202, 220-221 |
| § 3 | Contrainte de solvabilité, endettement toujours accru, report par la baisse des taux jusqu'au plancher, croissance reposant sur une dégradation de la solvabilité | L | S20, résumé, p. 9-10, 57, 296, 305 |
| § 3 | L'encours nominal mondial croît | F | S3 |
| § 3 | Un encours net croissant engage des revenus futurs croissants | D | déduction explicitée ; L1.C12 |
| § 3 | Le service de la dette absorbe une part croissante des revenus | H | aucune source ouverte ; `verifications_en_attente` |
| § 3 | Une partie des revenus financiers s'accumule | H | aucune source ouverte ; L1.C23 non probant |
| § 3 | Là où ces mécanismes sont réunis, la croissance est une condition de fonctionnement du régime d'émission | H appuyée | assemblage des lignes précédentes ; le chapitre le dit hypothèse |
| § 4 | La dette publique est dans le même système monétaire mais n'est pas un crédit bancaire ; un titre public crée des dépôts si une banque l'achète | F, D | S1, p. 17 |
| § 4 | Les États refinancent les titres à échéance (France 2026 : 175,8 / 310,0 / 124,4 Md€) | F | S16, p. 24 |
| § 4 | La charge d'intérêts est une dépense du budget général (58,0 Md€, +7,2), deuxième poste, premier à terme | F | S16, p. 30-31 ; S17 |
| § 4 | Déterminants de la contrainte d'un État ; croissance souvent la réponse politiquement privilégiée ; autres solutions | H | formulation de l'auteur ; L1.C13 |
| § 4 | En récession, le service de la dette absorbe une part relativement grande du revenu national ; les États empruntent davantage | E | S18, p. 2 |
| § 4 | Les États s'abstiennent de la sobriété par dépendance revendiquée à la croissance fiscale | F (synthèse) + H | S15, p. 34 |
| § 4 | Grèce : concomitance contraction, chômage, suicides ; pas de causalité | F | S4 ; S9 |
| § 5 | Trois voies de croissance nominale ; une charge d'intérêts n'est pas en soi un prélèvement physique | D | déduction explicitée |
| § 5 | Pas de découplage absolu mondial ; aucun entre 2015 et 2023 | F | S14, p. xiv, 4 ; L1.C03 |
| § 5 | Le découplage comme solution est jugé peu crédible | E | S18, p. 3 |
| § 5 | Empreinte matérielle vs consommation intérieure ; déplacement des impacts par le commerce | F | S14, p. 24, xiv |
| § 5 | Publier les trois niveaux ; un projet n'est pas régénératif par déplacement ; limite de la promesse | N | décision de l'auteur |
| § 5 | Le taux d'intérêt influence le taux d'extraction ; consumérisme stimulé par la dette écologiquement intenable | E | S18, p. 6 |
| § 5 | Soddy : formulation, non mesure | F | S2, p. 70 |
| § 6 | Solvabilité conventionnelle = M ∧ C ∧ T ∧ A ; essentiel insolvable = E ∧ (¬M ∨ ¬C ∨ ¬T ∨ ¬A) | N (définition) | note de l'auteur ; L1.C15 ; L1.C06 |
| § 6 | Les banques décident d'abord combien prêter selon les occasions rentables | F | S1, p. 15 |
| § 6 | Un investissement vert sans recettes n'est finançable que par subvention (forme ¬M) | L | S20, p. 405-406 |
| § 6 | Autres financements possibles ; le concept n'est pas vidé ; l'avantage comparatif peut l'être (F10) ; ampleur inconnue | H | arbitrage OPERATIONNALISATION-INSOLVABLE ; F10 |
| § 7 | Définition de NEMO IMS ; inversion de polarité | N | formulation adoptée par l'auteur |
| § 7 | Pour les activités qualifiées, pas de prêt remboursable ; reflux collectif ; régime de crédit maintenu | P | L1.C20, L1.C21, L1.C17, Livre 2 |
| § 7 | L'émission sans dette est institutionnellement concevable et a des formes proposées (émission exogène ; monnaie permanente) | L + M | S20, résumé, p. 99, 388 ; S19, p. 207, 222 |
| § 7 | Le dispositif ne lève pas la contrainte physique ; inflation et P9 non soldées ; volet international contesté | H | L1.C31 ; registre des promesses ; protocole de falsification |
| § 7 | Financer le régénératif ne suffit pas sans limitation des autres circuits ; canal positif et régime négatif | N | formulation de l'auteur, reprise mot pour mot |
| § 7 | Phase-in sans phase-out ; prudentiel compatible avec les financements carbonés ; information seule insuffisante ; neutralité mythe ; phase-out accéléré, flux nouveaux, cohérence, décision démocratique | F (énoncés d'une thèse dans son domaine) | S21, p. 36-41, 63, 71, 81-84, 188, 195, 228-231 |
| § 7 | Extension du carbone à l'incompatible écologique et des banques centrales à un dispositif d'émission | N (déclarée) | choix du corpus, dit tel |
| § 7 | Le corpus avait un régime par le prix et un engagement sur le canal propre, aucune règle sur les autres circuits ; l'arbitrage fixe principe et grille, non l'instrument | F (corpus) + N | L1.C21 ; L11.C03 ; A44 ; L2.C06, L2.C13, L2.C20 ; `REGIME-NEGATIF` |
| § 7 | Gesell et Wörgl : composant périphérique ; aucun système historique complet ; antériorités du mécanisme monétaire seul | H | Livre 16 ; F5 ; S19, S20 |
| § 8 | Huit conditions de réfutation, une par maillon | P | mesures renvoyées à L1.C23, L1.C13, L1.C03, L1.C31, Livre 2, `REGIME-NEGATIF` |

## 4. Ce que la quatrième passe change

- **Introduction** : la conclusion provisoire en trois phrases ouvre le
  chapitre ; les cinq niveaux sont annoncés avec leurs sections ; NEMO IMS est
  défini à sa première occurrence.
- **§ 1** : ajout de la fuite hors du circuit (S19) et de la contingence du
  régime de crédit (S20).
- **§ 2** : ajout de la distinction intérêt / capital et de la neutralité des
  intérêts dans les profits globaux (S19) ; délimitation du résultat de 2015 ;
  complémentarité avec 2012 ; mention de la requalification de L1.C23.
- **§ 3, refondu** : les trois conditions deviennent des composants d'une
  dépendance structurelle — énoncé raisonné (S18), résultat de modèle (S19),
  lecture institutionnelle (S20), fait (S3) —, chacun avec sa qualification ;
  les conditions 2 et 3 restent hypothèses et sont regroupées sous « Ce que le
  chapitre n'établit pas » ; synthèse « Ce que les niveaux réunis établissent »
  comme hypothèse appuyée.
- **§ 4** : ajout du service de la dette en récession (S18, p. 2).
- **§ 5** : ajout du jugement sur le découplage, du principe taux d'intérêt /
  extraction et du consumérisme stimulé par la dette (S18), tous comme énoncés.
- **§ 6** : ajout de l'investissement vert sans recettes (S20) comme forme ¬M.
- **§ 7, refondu** : antériorités de l'émission sans dette (S20, S19) ;
  conséquence de Deyris mot pour mot ; ce que la thèse établit (S21) ;
  extension déclarée ; règle du corpus et arbitrage `REGIME-NEGATIF` ;
  précédents réduits conservés.
- **§ 8** : régime des sources à sept catégories (ajout de la source
  d'économie politique) ; huit conditions de réfutation (ajout de l'épreuve
  empirique du modèle de circuit et de la démonstration qu'un canal positif
  suffirait).
- **En-tête** : S18 à S21 ajoutées, `ouverte` au 2026-09-11 ; aucune source
  retirée ; concepts `degeneratif` et `reflux_transactionnel` ajoutés ;
  renvois L1.C20, L2.C06, L2.C13, L2.C20, L11.C03 ajoutés ; quatre
  `verifications_en_attente` ; résumé réécrit ; `statut`, `citable`,
  `revision_de_fond` inchangés.
- **Audit contradictoire du 2026-09-11** (modèle tiers, dossier
  `audit-contradictoire-L1-C08-a-coller.md`), arbitré par l'auteur le jour
  même : cinq objections corrigées dans le texte (déduction sur le service de
  la dette conditionnée aux taux ; mécanisme productivité-emploi dit réel et
  non monétaire ; définition M ∧ C ∧ T ∧ A marquée `::norme::` ; Grèce et
  France dites États de la zone euro sans souveraineté monétaire ; voies de
  croissance nominale réécrites en décomposition comptable marquée
  `::hypothese::`), trois acceptées comme limites et écrites (amortissement
  contre fuite, au § 3 ; répression financière, au § 7 ; accommodation
  post-keynésienne, au § 2). Une relecture avant l'audit avait déjà corrigé
  l'attribution à S18 d'un mécanisme « par la rentabilité », que le texte ne
  porte pas. Statut passé à `audit_factuel`.
- **S7 retirée** le 2026-09-11, sur décision de l'auteur, après épuisement
  des voies publiques (tableau du § 2) : l'entrée, la phrase du § 2 qui la
  rapportait d'après son résumé et l'entrée correspondante des vérifications
  en attente sont supprimées ; le § 2 conserve l'objection post-keynésienne de
  l'accommodation, portée sans elle. Le chapitre compte quatorze sources,
  toutes `ouverte`.
- **Sixième étape, le 2026-09-11 au soir**, sur validation par l'auteur des
  deux fiches et de la matrice (architecture § 11 à § 14) : le paragraphe du
  § 3 sur les deux conditions est réécrit — les sources « documentent deux
  mécanismes conditionnels, principalement au moyen de modèles », sans mesure
  générale (S19 p. 138-139, 153 ; S18 p. 2 ; S20 ; S6 p. 2-3 rapportant
  Binswanger 2009) ; la synthèse du § 3 dit la dépendance comme combinaison
  sans nœud unique ; le § 5 écrit l'appui double de la clause écologique (S18
  pour l'argument structurel, S14 et S15 pour l'état empirique) ; S22
  (Barrett 2017, arXiv) est acquise par téléchargement direct et employée au
  § 2 pour le seul résultat de stabilité, sans généralisation ; l'en-tête
  applique la règle de l'auteur sur les limites : les trois objections
  acceptées comme limites et la limite de conception du régime négatif sont
  portées dans le corps et le résumé et consignées en commentaire, la liste
  des vérifications ne gardant que la tâche factuelle du § 3.
- **Septième étape, le 2026-09-11 au soir**, sur validation de la passe
  précédente : contrôle textuel qu'aucune formulation ne présente comme
  observés, généralisés, dominants ou quantitativement importants la
  croissance de la part des revenus absorbée par le service, l'accumulation
  durable des paiements d'intérêts ou le renouvellement croissant du crédit
  (aucun dépassement : chaque occurrence est une citation attribuée à un
  modèle, une déduction conditionnelle ou une négation) ; la dernière tâche
  factuelle est requalifiée en limite du chapitre, écrite au § 3 et dans le
  résumé (« Le chapitre établit l'existence théorique de plusieurs mécanismes
  par lesquels l'endettement peut contribuer à la dépendance à la croissance.
  Il ne mesure ni leur ampleur dans les économies observées, ni leur poids
  relatif parmi les autres mécanismes de cette dépendance. ») ; la liste
  `verifications_en_attente` est vidée ; statut `verifie` ; état enregistré
  (`--maj-etat --fond`).
- **Commit correctif du 2026-09-11**, sur décision de l'auteur : URL publique
  de S18 ajoutée après vérification par empreinte ; l'énoncé général « aucun
  découplage absolu n'est observé à l'échelle mondiale » remplacé, au § 5 et
  au § 8, par « le PNUE ne relève aucune preuve d'un découplage absolu
  généralisé à l'échelle mondiale et, entre 2015 et 2023, aucun découplage
  absolu des pressions environnementales examinées à cette échelle » ; § 7
  aligné sur l'arbitrage `REGIME-NEGATIF` (principe validé, instruments non
  tranchés, objet distinct du compte de capital).
- **Hors C08** : L1.C23 [S18] et [S19] requalifiées `ouverte` (2026-09-11)
  après vérification de tous leurs passages, et une citation du corps corrigée
  (« ne serait alors pas à rechercher ») ; `corpus/arbitrages.yaml` :
  `REGIME-NEGATIF` créé, lien réciproque ajouté à A44 ; registre des
  promesses : P2 réancrée en L1.C08 § 7, P9 en L1.C08 § 3, P39 annotée ;
  fichier renommé `c08-quand-la-dette-cree-une-contrainte-de-croissance.md`
  (identifiant et URL inchangés) ; architecture § 8 mise à jour.

## 5. Réserves et jugements à trancher par l'auteur

1. **S6 en version de travail.** La version publiée (Ecological Economics 120)
   reste fermée ; le chapitre le dit.
2. **S7 retirée.** Toutes les voies publiques ont été essayées (tableau du
   § 2) ; l'auteur a décidé de s'en passer. Si le texte de 2016 ou sa version
   de conférence de 2014 est un jour obtenu, il pourra revenir au § 2 comme
   source lue, non comme résumé.
3. **Conditions 2 et 3 du § 3 sans source.** Aucune des quatre sources
   nouvelles ne mesure la part des revenus absorbée par le service ni
   l'accumulation des revenus financiers ; déclarées hypothèses, inscrites en
   `verifications_en_attente`.
4. **L'assemblage du § 3.** La dépendance structurelle est portée par un
   énoncé raisonné, deux modèles théoriques et une lecture institutionnelle,
   plus un fait d'encours ; le chapitre la qualifie d'hypothèse appuyée. C'est
   le point que l'audit contradictoire doit attaquer en premier.
5. **L'extension de Deyris.** Le passage du carbone à l'incompatible
   écologique et des banques centrales à un dispositif d'émission est déclaré
   comme choix du corpus ; l'audit contradictoire doit dire si la thèse le
   supporte.
6. **L'instrument du régime négatif** n'est pas fixé ; la divergence de
   L2.C13 sur l'encadrement quantitatif demeure ; l'arbitrage l'enregistre.
7. **passe-2.md** dit encore de Cottin-Euziol « PARTIELLEMENT LUE, à rouvrir »
   avec une extraction arrêtée au chapitre 2 ; le fichier fourni est intégral
   et lu. Le protocole n'a pas été modifié : correction à faire par l'auteur.
8. **L1.C23** : le changement (requalification de deux sources, un mot rétabli
   dans une citation) a été enregistré comme éditorial le 2026-09-11 par
   `--maj-etat --editorial`, sur décision de l'auteur.
9. **Renommage et historique.** `git mv` a enregistré le renommage dans
   l'index avec l'ancien contenu ; pour que l'historique suive le fichier, il
   faut commiter d'abord ce seul renommage (`git commit` sans `-a`), puis le
   nouveau contenu. Un commit unique peut passer sous le seuil de similarité
   de git et apparaître comme suppression et création.
10. **URL des sources fournies.** S18 à S21 n'ont pas d'URL : aucune n'a été
    vérifiée, et le corpus n'en invente pas. L'auteur peut en ajouter une
    (dépôt de thèses, HAL, Institut Veblen) s'il la vérifie.
11. **P2 reformulée** : « techniquement possible » est devenu
    « institutionnellement possible », ce que les deux thèses établissent ; à
    confirmer par l'auteur.
12. **Statut.** `verifie` depuis le 2026-09-11 au soir, sur décision de
    l'auteur, après l'audit contradictoire arbitré, les deux fiches et la
    requalification de la dernière tâche factuelle en limite. Ce statut atteste
    des sources contrôlées, toutes ouvertes et datées, et une structure
    cohérente ; il ne signifie pas que l'importance empirique des mécanismes
    du § 3 ait été démontrée, ce que le chapitre dit lui-même. `citable` reste
    `false` et `autorite` reste `preparatoire` : la publication relève d'une
    décision distincte de l'auteur.
13. **Ce que l'audit n'a pas vu.** Le mot « rentabilité » dans la conclusion
    n'est appuyé qu'indirectement (autres incitations nommées par S6, équation
    des profits de S19) ; formulation de l'auteur, conservée.

## 6. Statut et blocages

**Statut : `verifie`, `citable: false`, `autorite: preparatoire`,
`revision_de_fond: 2026-09-11`.** Quinze sources depuis l'ajout de S22, toutes
`ouverte` et datées, aucune `candidate` ni `a_requalifier`. Les deux
affirmations qui restaient à établir, réduire ou requalifier l'ont été comme
mécanismes conditionnels documentés par des modèles ; leur mesure, dernière
tâche factuelle, a été requalifiée en limite du chapitre par l'auteur, sans
nouvelle collecte, et la liste `verifications_en_attente` est vide. L'en-tête
consigne en commentaire l'audit contradictoire du 2026-09-11 (cinq objections
traitées), les trois objections acceptées comme limites, la limite de
conception du régime négatif et la limite de mesure, toutes portées dans le
corps et le résumé. **`verifie` ne signifie pas que l'importance empirique des
mécanismes ait été démontrée** : le chapitre établit l'existence théorique de
plusieurs mécanismes et ne mesure ni leur ampleur ni leur poids relatif.

**Contrôle.** `python corpus/controle.py` : contrôle structurel passé, aucun
blocage ; une décision en attente, sur L1.C23 (réserve 8). Pour C08 : A-L1,
1 candidate sur 15 ; A-L3, quatre entrées du manifeste sans occurrence (S5, S8,
S10, S11, retirées). `--publier` refuse C08 sur son statut et sur S7 seulement.
Le registre d'arbitrages compte 41 entrées ouvertes ou orientées après
l'ajout de `REGIME-NEGATIF`. Vérification mécanique des citations : 135 sur
135 citations du chapitre (en-tête et corps) retrouvées dans les textes
acquis ; pour les passages que L1.C23 et l'architecture attribuent aux thèses,
71 sur 72, la seule absence étant la citation tronquée du corps de L1.C23,
corrigée par cette passe.

**État enregistré.** Le 2026-09-11, sur décision de l'auteur, en deux temps :
`python corpus/controle.py --maj-etat --editorial` après l'audit contradictoire
(C08 qualifié « fond » d'après sa `revision_de_fond`, L1.C23 requalifié
« editorial » par l'option), puis `--maj-etat --fond` après le retrait de S7
(C08 requalifié « fond, déclarée le 2026-09-11 ») ; 335 entrées, aucune
qualification perdue, aucune décision en attente ; puis, après validation de
la sixième et de la septième étapes, une troisième inscription par
`--maj-etat --fond` (C08 requalifié « fond, déclarée le 2026-09-11 »). Contrôle
complet après cette inscription : structurel passé, aucun blocage, aucune
décision en attente ; en mode publication, C08 n'est refusé que pour
`citable: false`. Le bilan A-L3 de C08 compte
désormais cinq entrées du manifeste sans occurrence (S5, S7, S8, S10, S11),
toutes retirées ; c'est une alerte, non un blocage.

## 7. À propager hors de C08 (décision de l'auteur)

- **L1.C01** : ajouter la condition de non-accumulation des revenus d'intérêts
  aux conditions de la contrainte de croissance.
- **L1.C07** : le sourçage de Moore 1988 et Lavoie 2014 y reste en attente.
- **L1.C23** : [S18] et [S19] sont requalifiées ; les dix-sept autres entrées
  `a_requalifier` restent à ouvrir chapitre par chapitre ; S6 y est lisible en
  version de travail.
- **passe-2.md** : corriger la ligne Cottin-Euziol (réserve 7).
- **L1.C12 § 3** : la déduction « le service d'un encours croissant exige une
  expansion nette du crédit » appelle la même condition sur les taux et les
  échéances que l'objection 1 de l'audit ; à conditionner en passe suivante.
- **Registre, P39** : l'objection 5 de l'audit (amortissement contre fuite) y
  est ajoutée le 2026-09-11 ; à instruire avec la promesse.
- **Livre 2 (L2.C13, L2.C20)** : l'arbitrage `REGIME-NEGATIF` leur renvoie le
  choix de l'instrument ; la divergence enregistrée doit être reprise là.
- **L16.C01, L16.C03** : reçoivent le détail de Gesell et de Wörgl que C08 ne
  porte plus ; les transcriptions lues le 2026-09-10 restent disponibles pour
  eux, sans promotion automatique.
- **L1.C03, L17.C01, L26** : S14 et S15 sont lues dans des éditions
  identifiées ; leurs entrées `a_requalifier` peuvent en bénéficier, chapitre
  par chapitre.
