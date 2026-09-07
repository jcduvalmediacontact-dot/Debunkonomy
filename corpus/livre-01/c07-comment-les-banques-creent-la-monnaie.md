---
chapitre: L1.C07
titre: "Comment les banques créent vraiment la monnaie"
livre: 1
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-07
autorite: preparatoire
citable: false
regime: hybride
sources_primaires:
  - ref: S1
    nature: theorie
    reference: "M. McLeay, A. Radia, R. Thomas, « Money creation in the modern economy », Bank of England Quarterly Bulletin, Q1 2014"
    url: "https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy"
    date_verification: 2026-09-03
  - ref: S2
    nature: theorie
    reference: "H. Withers, The Meaning of Money, Smith, Elder & Co., Londres, première édition ; rééditions successives"
    date_verification: 2026-09-03
  - ref: S3
    nature: theorie
    reference: "J. A. Schumpeter, History of Economic Analysis, Oxford University Press, publication posthume 1954"
    date_verification: 2026-09-03
verifications_en_attente:
  # — Corrections critiques identifiées à la conversion —
  - "CRITIQUE — date de première édition de Withers, The Meaning of Money : le texte source retient 1901, plusieurs catalogues de bibliothèque donnent 1909. Vérifier la date exacte et l'éditeur avant citation en chapitre vérifié."
  - "CRITIQUE — attribution de la formule « loans make deposits » à Withers plutôt qu'à Schumpeter : retrouver la formulation exacte chez Withers, documenter l'origine de la confusion avec Schumpeter (History of Economic Analysis, 1954), et vérifier qu'aucun antérieur du XIXe siècle ne la formule déjà."
  - "CRITIQUE — « environ 92 % de la monnaie en circulation en Europe en 2024 est de la monnaie commerciale » : chiffre repris sans source. Le même chiffre est déjà signalé comme non sourcé en L1.C05. Retrouver l'agrégat (M1, M2, M3), la zone (euro, UE, monde), l'année et la méthode ; aligner les deux chapitres ou retirer."
  - "CRITIQUE — « quatre-vingt-dix pour cent des manuels d'économie continuent d'enseigner l'ancien modèle » : affirmation quantitative sur le contenu des cursus, à étayer par un relevé de manuels ou à retirer."
  # — Références à établir —
  - "Théorie de la monnaie endogène : citer les travaux de Nicholas Kaldor, Basil Moore, Marc Lavoie et l'école post-keynésienne. Sourcer notamment Moore (Horizontalists and Verticalists, 1988) et Lavoie (Post-Keynesian Economics, 2014)."
  - "Représentations du multiplicateur monétaire dans les manuels standards : relever deux ou trois manuels de référence et citer le passage — vérification déjà ouverte en L1.C01."
  - "Rapport de la Banque d'Angleterre 2014 : citer le passage exact reproduit dans le chapitre et vérifier la traduction française retenue."
  - "Article compagnon du même Quarterly Bulletin Q1 2014 de la Banque d'Angleterre : « Money in the modern economy: an introduction » (McLeay, Radia, Thomas) — à ajouter en source si utilisé."
  # — Cohérence interne —
  - "COHÉRENCE — la formule « les crédits font les dépôts » et la création ex nihilo doivent se rattacher explicitement à la définition de la monnaie comme registre posée en L1.C05. Vérifier l'alignement."
  - "COHÉRENCE — L1.C06 annonce ce chapitre comme celui qui démontre le mécanisme de création monétaire. Vérifier que la démonstration porte bien ce que L1.C06 en attend."
  - "COHÉRENCE — la non-neutralité affirmée en L1.C01, L1.C02, L1.C05 porte sur l'orientation sectorielle du crédit. Vérifier que ce chapitre en fournit la démonstration mécanique attendue."
  # — Renvois —
  - "Renvoi à ajouter vers le chapitre consacré à la première malédiction monétaire quand il existera"
resume: "Le mécanisme de création monétaire enseigné par les manuels standards — la Banque centrale émet la monnaie de base, les banques commerciales collectent l'épargne et la reprêtent — inverse la chronologie réelle des opérations. Ce chapitre expose le mécanisme comptable effectif : une banque commerciale qui accorde un crédit inscrit simultanément une créance à son actif et un dépôt de même montant au passif, sans transfert d'aucune monnaie préalablement existante. Cette description, formulée dès le début du XXe siècle par Hartley Withers, a été publiquement reconnue par la Banque d'Angleterre en 2014. Le chapitre en tire quatre conséquences pour la suite du corpus : la masse monétaire est intrinsèquement une dette, l'orientation des crédits décide de l'orientation de l'économie, un pouvoir monétaire privé s'exerce sans mandat démocratique explicite, et la politique monétaire au sens usuel ne porte que sur une fraction de ce pouvoir."
concepts: [creation_monetaire, monnaie_comme_registre, monnaie_endogene, solvabilite_anticipee, systeme_monetaire_et_financier, neutralite_monetaire]
renvois: [L1.C05, L1.C06, L1.C08]
---

# Comment les banques créent vraiment la monnaie

Ce chapitre établit deux propositions et en tire quatre conséquences. La première proposition est descriptive : dans le système bancaire moderne, l'essentiel de la monnaie en circulation n'est pas émis par la Banque centrale mais créé par les banques commerciales, à l'occasion de chaque crédit qu'elles accordent, par une double écriture comptable sans transfert d'aucune monnaie préexistante. La seconde est historique : cette description n'est pas récente ni marginale — elle est formulée dès le début du XXe siècle et a été publiquement reconnue par la Banque d'Angleterre en 2014 [S1].

Ces deux propositions ne sont pas discutées dans la littérature contemporaine spécialisée. Elles le restent dans le débat public et dans une part des manuels — un écart qui appelle une explication distincte, examinée en § 4.

## 1. Le modèle du multiplicateur

La représentation communément enseignée du crédit bancaire tient en trois étapes. La Banque centrale émet la monnaie de base. Les agents économiques déposent cette monnaie dans les banques commerciales. Les banques commerciales, tenues à un ratio de réserves, prêtent la fraction non réservée à d'autres agents, dont les dépôts alimentent à leur tour de nouveaux crédits — chaîne qui définit le multiplicateur monétaire.

Dans ce modèle, la banque commerciale joue un rôle d'intermédiation passive : elle collecte l'épargne, la redistribue sous forme de crédit, prélève une marge d'intérêt. Elle transfère de la monnaie qu'elle ne crée pas. Le pouvoir d'émission appartient à la Banque centrale ; les banques commerciales n'en démultiplient que l'effet.

Cette représentation est intuitive : elle correspond à ce que suggère l'expérience courante du dépôt et de l'emprunt. Elle sous-tend une part importante du débat public sur l'épargne, la dette publique, la politique monétaire. Elle est enseignée du lycée aux écoles de commerce.

::hypothese:: Elle est fondamentalement erronée dans son principe, non seulement dans certains cas particuliers. Elle inverse l'ordre chronologique des opérations : ce ne sont pas les dépôts qui rendent possibles les crédits, ce sont les crédits qui produisent les dépôts. Le multiplicateur est un dispositif pédagogique, non une description du secteur bancaire réel.

## 2. Le mécanisme comptable réel

Un agent sollicite un crédit auprès de sa banque — par exemple, trois cent mille euros pour l'achat d'un logement. La banque examine le dossier selon ses critères propres — capacité de remboursement, garanties, exposition au risque. Si elle accorde le crédit, deux écritures comptables suivent, sans transfert monétaire préalable ni prélèvement sur un autre compte.

::etat:: **Première écriture** : la banque inscrit à son actif une créance de trois cent mille euros sur son nouveau client — la promesse contractuelle de remboursement, comptabilisée comme telle. **Seconde écriture** : la banque inscrit à son passif un dépôt de trois cent mille euros au crédit du compte courant du client — une dette exigible à vue, puisque le client peut retirer la somme à tout moment.

Aucune monnaie préexistante n'a été mobilisée. La banque n'a ouvert aucun coffre, n'a rien retiré d'un compte tiers, n'a rien sollicité de la Banque centrale au moment de l'opération. La double écriture, symétrique et simultanée, fait apparaître une somme monétaire qui n'existait pas une seconde plus tôt. Le vocabulaire économique désigne cette opération par l'expression *ex nihilo*, entendue au sens comptable strict — sans contrepartie monétaire préalable — et non métaphorique.

Symétriquement, chaque remboursement de capital efface la monnaie créée. La somme remboursée n'entre pas dans les fonds propres de la banque : elle disparaît du bilan, comme s'annule une écriture. La masse monétaire d'une économie augmente donc de la différence entre créations et remboursements de crédits, et se contracte lorsque cette différence devient négative.

Il en résulte une définition opératoire à retenir pour la suite : la monnaie moderne est faite de dettes. Elle naît par le crédit. Elle disparaît par le remboursement. Cette définition prolonge, sur le versant du mécanisme, la caractérisation de la monnaie comme registre posée en L1.C05.

## 3. Une thèse ancienne

Cette description du crédit bancaire n'est ni récente ni marginale. Le journaliste financier britannique Hartley Withers la formule dès le début du XXe siècle dans *The Meaning of Money* [S2], sous la forme rendue célèbre par la formule anglaise *loans make deposits* — les crédits font les dépôts. La formule tient en trois mots ; elle inverse l'ordre habituel de l'exposition.

Une précision d'attribution est utile, parce qu'elle a longtemps été erronée dans la littérature francophone. La paternité de la formule appartient à Withers, non à Joseph Schumpeter, à qui elle est parfois attribuée sur la foi de son *Histoire de l'analyse économique* [S3], publiée à titre posthume plus d'un demi-siècle après l'ouvrage de Withers. Schumpeter y décrit le mécanisme avec précision, mais en s'appuyant explicitement sur les travaux antérieurs — dont ceux de Withers.

Une école de pensée s'est développée à partir de cette description, aujourd'hui désignée par le terme de théorie de la monnaie endogène. Ses représentants — Nicholas Kaldor, Basil Moore, Marc Lavoie, et plus largement l'école post-keynésienne — ont raffiné et étayé empiriquement la description initiale. Selon cette théorie, la monnaie ne descend pas de la Banque centrale vers l'économie : elle émerge de l'économie à travers les décisions de crédit des banques commerciales, la Banque centrale intervenant en aval pour réguler cette création par les taux et par la fourniture de liquidité de règlement interbancaire.

Cette théorie a longtemps été considérée comme hétérodoxe et n'était pas enseignée dans le canon des grandes écoles. Elle est restée controversée dans le débat académique jusqu'à ce que la Banque d'Angleterre en reconnaisse publiquement la substance en 2014.

## 4. La reconnaissance publique de 2014, et le silence qui l'a suivie

En mars 2014, la Banque d'Angleterre publie dans son *Quarterly Bulletin* un article de Michael McLeay, Amar Radia et Ryland Thomas intitulé « Money creation in the modern economy » [S1]. Le texte, signé par trois économistes de l'institution, décrit le mécanisme de création monétaire par les banques commerciales dans les termes rappelés en § 2, et écarte explicitement le modèle du multiplicateur comme description du fonctionnement réel du système bancaire.

La portée de cette publication tient moins à ce qu'elle affirme — la thèse est antérieure — qu'à l'institution qui la porte. Une banque centrale nationale, reconnue et non identifiée à un courant hétérodoxe, valide publiquement une description que ses propres services expertisent. L'argument d'autorité qui maintenait le modèle du multiplicateur dans les manuels perd son fondement.

::hypothese:: Onze années après cette publication, la description héritée continue pourtant d'être enseignée dans une part importante des manuels d'économie généralistes, et le débat public sur la monnaie continue majoritairement de se conduire dans les termes qu'elle impose. Trois hypothèses distinctes rendent compte de ce décalage, sans que le corpus tranche entre elles à ce stade.

**Inertie pédagogique.** La transmission d'une génération de manuels à la suivante procède par mise à jour incrémentale plutôt que par refonte. Réviser le chapitre sur la création monétaire suppose de rouvrir l'architecture d'ensemble d'un cours d'économie monétaire, coût que peu d'éditeurs assument tant qu'aucune pression externe ne l'exige.

**Charge politique.** La description exacte fait apparaître qu'un pouvoir d'émission monétaire est exercé, à l'échelle des masses, par des acteurs privés selon un critère de rentabilité. Cette description ouvre une question de mandat démocratique que la description standard n'appelle pas.

**Coût cognitif partagé.** Reprendre les débats publics — sur la dette souveraine, la politique de la Banque centrale, le financement de la transition écologique — dans le cadre exact suppose de reformuler des raisonnements installés. Le maintien du cadre hérité économise cette reformulation.

Le partage entre ces hypothèses n'est pas l'objet du chapitre. Ce qui l'est, c'est le constat : un fait reconnu par l'autorité compétente reste, plus d'une décennie après cette reconnaissance, largement absent du cadre dans lequel se conduit le débat sur la monnaie.

## 5. Quatre conséquences

De la description du § 2 découlent, sans étapes supplémentaires, quatre conséquences pour la suite du corpus.

**Un.** La masse monétaire est intrinsèquement une dette. À chaque unité monétaire en circulation correspond, à un point du système, une créance bancaire d'égal montant portée par un débiteur — ménage, entreprise, État. Le remboursement de l'ensemble des dettes contracterait la masse monétaire à zéro. Cette symétrie n'est pas une figure ; c'est le corollaire mécanique de la double écriture.

**Deux.** L'orientation des crédits décide de l'orientation de l'économie. Puisque toute nouvelle monnaie procède d'une décision de crédit prise par une banque commerciale, ces décisions déterminent, dans l'agrégat, quelles activités sont financées et lesquelles ne le sont pas. Le critère d'attribution est la solvabilité anticipée du débiteur — ce qui, en pratique, revient à financer ce qui produit une recette monétaire suffisante pour porter le service de la dette. Ce partage n'est pas neutre par rapport à la distinction établie en L1.C01 entre activités dont la régénération s'accompagne d'un produit vendable et celles où elle constitue le bénéfice principal sans recette attachée.

**Trois.** Un pouvoir monétaire privé s'exerce à côté du pouvoir monétaire public. La part de la monnaie en circulation émise par les banques commerciales est très supérieure à celle émise par la Banque centrale sous forme fiduciaire — l'ordre de grandeur retenu ici demande vérification (voir `verifications_en_attente`), mais aucun agrégat n'invalide la disproportion. Ce pouvoir ne s'exerce dans le cadre d'aucun mandat démocratique explicite pour cette fonction, distincte du mandat de crédit à l'économie qui fonde l'existence même du secteur bancaire.

**Quatre.** La politique monétaire, au sens du débat public, ne porte que sur une fraction du pouvoir monétaire réel. Les taux directeurs, les opérations d'*open market*, l'assouplissement quantitatif, la politique de bilan de la Banque centrale modifient les conditions d'accès à la liquidité et le coût du crédit — donc influent, indirectement, sur les décisions de crédit des banques commerciales. Ils ne décident pas de la composition sectorielle du crédit accordé. Le débat public sur la monnaie porte ainsi sur les paramètres généraux d'un pouvoir dont l'exercice sectoriel reste hors du débat.

Ces quatre conséquences ne démontrent pas qu'une modification du régime d'émission monétaire soit possible, souhaitable ou suffisante. Elles délimitent ce que toute proposition sérieuse en matière d'orientation de l'économie doit prendre en compte : le levier monétaire principal est aujourd'hui hors du champ de la décision publique, non pour des raisons techniques, mais par l'effet direct de la manière dont la monnaie est créée. Les chapitres suivants examinent ce que cette contrainte engendre — à commencer par l'effet de la dette sur les trajectoires économiques — et ce que différents dispositifs modifieraient s'ils étaient introduits.

---

## BALAYAGE DU LIVRE 6 — 2026-09-07

::etat:: **Annotation portée à la clôture de la passe 1 du Livre 6.** Ce que ce chapitre reçoit n'a pas été instruit ici et **ne modifie pas ce qui précède** : il est versé pour que la passe 2 le trouve.

::hypothese:: **Le créancier ne décide pas seulement de ce qui se finance : il décide de ce qui peut être PROTÉGÉ** [L6.C07]. L'obligation réelle environnementale du droit français — article L. 132-3 du code de l'environnement, charge écologique attachée au bien jusqu'à quatre-vingt-dix-neuf ans — **est subordonnée en pratique à l'accord du créancier hypothécaire, qui n'a pas intérêt à consentir puisque la charge déprécie l'assiette de sa sûreté.**

::hypothese:: **Le mécanisme est propre et sans mauvaise foi** : la sûreté est un droit acquis, la dépréciation est réelle, le refus est rationnel. **La solvabilité anticipée qu'établit ce chapitre a donc une portée que ce chapitre n'énonce pas** — elle filtre non seulement les projets, mais les engagements de conservation.

::etat:: **RÉSERVE PORTÉE PAR LE REGISTRE DU LIVRE 6** : ce verrou est une **pratique notariale, non une règle légale explicite**, et aucune décision judiciaire ne l'a tranché.

::hypothese:: **ET UNE SORTIE EXISTE, versée en L6.C06 après lecture de l'arrêt italien n° 119 de 2023.** Les usages civiques italiens ne se heurtent pas au créancier : leur opposabilité « opera a prescindere dal rispetto di oneri pubblicitari » et survit à la vente forcée. **La différence est de nature : une charge inscrite vient après le créancier et lui demande permission ; une charge inhérente au fonds était là avant et ne la demande pas.** **Le corpus ne peut pas obtenir par convention ce que l'antériorité donne.**
