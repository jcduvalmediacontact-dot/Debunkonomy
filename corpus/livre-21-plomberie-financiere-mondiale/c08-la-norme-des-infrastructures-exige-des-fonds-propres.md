---
chapitre: L21.C08
titre: "La norme des infrastructures exige des fonds propres"
livre: 21
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
    nature: normatif
    reference: "**Committee on Payment and Settlement Systems et Technical Committee of the International Organization of Securities Commissions, *Principles for financial market infrastructures*, avril 2012, ISBN 92-9131-108-1.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte le 2026-09-08 ; pièce du dossier NEMO constitué par l'auteur le 2026-09-07. **DROITS : « © Bank for International Settlements and International Organization of Securities Commissions 2012. All rights reserved. BRIEF EXCERPTS MAY BE REPRODUCED OR TRANSLATED PROVIDED THE SOURCE IS [cité] » — mention lue dans le document. RÉGIME : `citation_seule`**, la mention autorisant expressément la citation courte avec attribution. **C'est la norme internationale qui régit les infrastructures de marchés financiers**, et elle a été rendue par deux comités internationaux."
    date_verification: 2026-09-08
verifications_en_attente:
  - "**L'APPLICABILITÉ DE CETTE NORME AU DISPOSITIF N'EST PAS ÉTABLIE, ET CE
     CHAPITRE NE L'ÉTABLIT PAS.** La norme vise les **systèmes de paiement
     d'importance systémique**, les dépositaires centraux, les systèmes de
     règlement-livraison, les contreparties centrales et les référentiels
     centraux. **Savoir si la couche de règlement du dispositif entre dans la
     première catégorie est une question de fait et de qualification, non de
     lecture** — et personne ne l'a tranchée. **Le chapitre instruit donc ce qui
     s'appliquerait SI elle y entrait.**"
  - "**LE TEXTE OUVERT DATE DE 2012, ET LE CORPUS N'A OUVERT AUCUNE MISE À JOUR.**
     Les travaux postérieurs sur les infrastructures transfrontalières, sur les
     monnaies numériques de banque centrale et sur la cyber-résilience existent
     et ne sont pas tenus. **ACQUISITION DE RANG 1**, d'autant que la question
     transfrontalière est celle du dispositif."
  - "**AUCUNE CRITIQUE DE CETTE NORME N'EST OUVERTE.** Le corpus tient le texte
     de deux comités internationaux sur les infrastructures qu'ils régulent.
     **Même défaut que celui déjà déclaré trois fois : une norme sans son
     adversaire.**"
resume: "Ce chapitre ouvre la norme internationale qui régit les infrastructures de marchés financiers et la confronte à ce que le corpus a établi de la couche de règlement du dispositif. Il commence par borner sa propre portée, puisque la norme vise les systèmes de paiement d'importance systémique et que personne n'a établi que le dispositif en soit un, de sorte que le chapitre instruit ce qui s'appliquerait dans cette hypothèse. Il relève d'abord un point favorable, la norme demandant que les règlements en monnaie s'effectuent en monnaie de banque centrale lorsque cela est praticable, ce que l'architecture du dispositif satisfait puisque son allocation ne circule qu'entre l'émetteur et les banques centrales nationales. Il établit ensuite trois exigences que le dispositif ne satisfait pas en l'état. La première est celle d'une base juridique solide, claire, transparente et opposable dans toutes les juridictions concernées, alors que la forme juridique de l'émetteur reste indécise et qu'un arbitrage en attente en dépend. La deuxième, et c'est la plus dure, est l'obligation de détenir des actifs liquides nets financés par des fonds propres, suffisants pour absorber des pertes d'exploitation et pour permettre un redressement ou une liquidation ordonnée, alors que le dix-neuvième livre a établi que l'émetteur pourrait présenter des fonds propres négatifs selon la branche retenue du même arbitrage. La troisième est celle d'un règlement définitif clair et certain, dont le corpus n'a jamais fixé le moment. Le chapitre conclut que ces exigences font de l'arbitrage sur la forme juridique de l'émetteur un point qui décide désormais d'une cinquième chose."
concepts: [contrepartie_comptable, robustesse, hierarchie_monetaire]
renvois: [L16.C04, L19.C01, L19.C03, L19.C06, L19.C07, L21.C03, L21.C05, L21.C07]
---

# La norme des infrastructures exige des fonds propres

::etat:: **Le dispositif comporte une couche de règlement, et il existe une norme internationale pour ce type d'objet.** **Ce chapitre l'ouvre et la confronte à ce que le corpus tient.** **Il ne conclut pas que la norme s'applique : il établit ce qu'elle exigerait si elle s'appliquait, et ce que le dispositif satisfait ou non.**

## 1. La portée, et il faut la borner avant de lire

::etat:: **La norme vise cinq objets** [S1] : les **systèmes de paiement d'importance systémique**, les dépositaires centraux de titres, les systèmes de règlement-livraison, les contreparties centrales et les référentiels centraux de données.

::hypothese:: **Savoir si la couche de règlement du dispositif est un système de paiement d'importance systémique est une question de fait et de qualification, et personne ne l'a tranchée.** **Le corpus ne peut donc pas dire que la norme le lie.** **Mais il ne peut pas non plus l'ignorer** : un mécanisme qui règle des soldes entre banques centrales nationales à l'échelle d'une coalition **présente exactement les caractéristiques que ces comités ont décidé d'encadrer.**

::etat:: **Ce chapitre instruit donc une hypothèse conditionnelle et l'écrit ainsi.**

## 2. Un point favorable, et le corpus doit le compter

::etat:: **Principe 9 — règlements en monnaie** [S1] : *« An FMI should conduct its money settlements in CENTRAL BANK MONEY where practical and available. If central bank money is not used, an FMI should minimise and strictly control the credit and liquidity risk arising from the use of commercial bank money. »*

::hypothese:: **L'architecture du dispositif satisfait ce principe par construction.** L11.C01 a établi que **l'allocation ne circule jamais** : elle vit exclusivement entre l'émetteur et les banques centrales nationales, et le prestataire est payé en monnaie nationale. **Le règlement s'effectue donc en monnaie de banque centrale, ce que la norme demande en premier choix.**

::etat:: **C'est le premier point de cette journée où une norme extérieure trouve le dispositif conforme sans réserve**, et le corpus l'enregistre comme tel.

## 3. Première exigence non satisfaite : la base juridique

::etat:: **Principe 1 — base juridique** [S1] : *« An FMI should have a WELL-FOUNDED, CLEAR, TRANSPARENT, AND ENFORCEABLE LEGAL BASIS for each material aspect of its activities IN ALL RELEVANT JURISDICTIONS. »*

::hypothese:: **Le dispositif ne satisfait aucun des cinq termes en l'état.** **La forme juridique de l'émetteur n'est pas décidée** — L19.C07 a établi qu'elle décide de quatre choses à elle seule. **Et l'exigence porte sur TOUTES les juridictions concernées**, ce qui, pour un mécanisme de coalition, désigne autant de juridictions que de membres.

::etat:: **Ce n'est pas une objection nouvelle mais une aggravation d'une objection connue.** L19 avait établi que l'indécision sur la forme juridique laissait quatre questions ouvertes ; **la norme des infrastructures ajoute qu'elle interdit de satisfaire son premier principe**, qui conditionne tous les autres.

## 4. Deuxième exigence, et c'est la plus dure : les fonds propres

::etat:: **Principe 15 — risque d'exploitation général** [S1] : *« An FMI should identify, monitor, and manage its general business risk and HOLD SUFFICIENT LIQUID NET ASSETS FUNDED BY EQUITY to cover potential general business losses so that it can continue operations and services AS A GOING CONCERN if those losses materialise. Further, liquid net assets should at all times be sufficient to ensure a RECOVERY OR ORDERLY WIND-DOWN of critical operations. »*

::etat:: **L19.C06 a établi que l'émetteur peut présenter des FONDS PROPRES NÉGATIFS selon la branche retenue de l'arbitrage sur sa forme juridique.**

::hypothese:: **La collision est frontale et elle se formule en une phrase : une infrastructure doit détenir des actifs liquides FINANCÉS PAR DES FONDS PROPRES, et le corpus a établi que l'émetteur pourrait n'en avoir aucun.** **Ce n'est pas une difficulté de calibrage : c'est une condition d'existence sous cette norme.**

::etat:: **Et l'exigence de liquidation ordonnée est du même ordre.** Le principe demande que les actifs liquides suffisent **à tout moment** à assurer un redressement ou une liquidation ordonnée des opérations critiques. **Le corpus n'a aucun régime de retrait, de liquidation ni de succession** — ce que L21.C07 avait déjà relevé pour d'autres motifs.

::hypothese:: **Cette exigence fait de l'arbitrage sur la forme juridique de l'émetteur un point qui décide désormais d'une CINQUIÈME chose**, après le porteur du passif, la compétence fiscale du reflux, le bilan qui porte le déficit et l'application de l'objection prudentielle.

## 5. Troisième exigence : le moment du règlement définitif

::etat:: **Principe 8 — caractère définitif du règlement** [S1] : *« An FMI should provide CLEAR AND CERTAIN FINAL SETTLEMENT, at a minimum by the end of the value date. Where necessary or preferable, an FMI should provide final settlement intraday or in real time. »*

::hypothese:: **Le corpus n'a jamais fixé le moment où une allocation devient définitive.** **Or ce moment commande deux choses qu'il a instruites ailleurs** : le point à partir duquel une allocation ne peut plus être révoquée en cas de disqualification ultérieure de l'activité, **et le moment que L19.C03 avait identifié comme décidant de la nature du reflux.**

::etat:: **La norme exige donc de trancher une question que le corpus tenait pour secondaire, et qui commande deux résultats déjà acquis.**

## 6. Ce que la norme demande encore, et que le corpus n'a pas instruit

::etat:: **Principe 2 — gouvernance** [S1] : les dispositions doivent être *« clear and transparent »*, promouvoir *« the SAFETY AND EFFICIENCY of the FMI »*, et soutenir *« the stability of the broader financial system, OTHER RELEVANT PUBLIC INTEREST CONSIDERATIONS, and the objectives of relevant stakeholders »*.

::hypothese:: **La finalité régénérative du dispositif entre vraisemblablement dans les « autres considérations d'intérêt public », et le corpus peut le soutenir.** **Mais l'ordre des termes n'est pas indifférent** : la norme place **la sûreté et l'efficacité de l'infrastructure en premier**, et la stabilité du système financier ensuite. **Un dispositif dont l'objectif premier est écologique devrait établir que cet objectif ne prime pas la sûreté du règlement** — question que sa gouvernance n'a jamais posée.

::etat:: **Principe 3 — cadre de gestion des risques** : la norme exige un cadre couvrant les risques **juridiques, de crédit, de liquidité, opérationnels et autres**. **Le corpus n'en tient aucun.**

## 7. Ce que ce chapitre verse

::etat:: **Un point de conformité, réel** : le règlement en monnaie de banque centrale, satisfait par construction.

::etat:: **Trois exigences non satisfaites** : la base juridique opposable dans toutes les juridictions ; **les actifs liquides financés par des fonds propres, qui heurtent de front le résultat de L19.C06** ; et le moment du règlement définitif, jamais fixé.

::etat:: **Une cinquième conséquence attachée à l'arbitrage sur la forme juridique de l'émetteur.**

::hypothese:: **Et une remarque de méthode qui vaut au-delà de ce chapitre.** **Le corpus a instruit ici une norme qui ne le lie peut-être pas**, et il l'a fait parce que le dispositif présente les caractéristiques de ce qu'elle encadre. **C'est la bonne façon de procéder tant que la qualification n'est pas tranchée** — mais **elle ne remplace pas la qualification**, et le corpus doit établir un jour si sa couche de règlement est ou non un système de paiement d'importance systémique. **Tant qu'il ne l'a pas fait, il ne sait pas quelles règles lui sont opposables.**
