# Architecture d'alignement — tranche 3 : L1.C17 à L1.C30

**Proposée le 2026-09-17 par Claude, non validée par l'auteur. Ce document ne décide rien, et aucune ligne des chapitres n'est modifiée.** Régime : METHODE-REECRITURES, METHODE-PERIMETRE, METHODE-PARALLELISME et METHODE-AUDITS (`coordination/DECISIONS_AUTEUR.md`). La règle qui commande tout le reste est la première : les chapitres « réécrire substantiellement » sont alignés sur les arbitrages ; les énoncés faux sont retirés, les branches ouvertes exposées, et seules les sources que le texte aligné cite sont ouvertes.

---

## 0. Ce qui a été fait, et ce que cela garantit

**Le périmètre n'est pas uniforme.** Onze chapitres de la seconde partie sont « réécrire substantiellement » : L1.C17, C18, C19, C20, C21, C22, C24, C26, C27, C28 et C29. L1.C30 reste brouillon, « déclaré récit » (METHODE-PERIMETRE). L1.C23 et L1.C25 sont « conserver » et gelés pour une passe adverse externe depuis le 2026-09-16 : ils ne reçoivent ici qu'un relevé de ce qui sera à propager **après** l'audit.

**La méthode.** Sept sous-agents ont reçu une consigne commune : lire le chapitre entier, la cartographie de refonte, le registre, `passe-2.md`, L1.C31 et les falsifieurs ; donner à chaque énoncé touché par un arbitrage un sort — **K** conserver, **C** corriger sous un arbitrage nommé, **R** retirer, **O** exposer ouvert, **N** ajouter — ; appuyer chaque sort sur une citation verbatim étiquetée par son fichier. Aucun n'a écrit dans le dépôt ; leurs brouillons ne valaient que piste. Sept se sont arrêtés sur une limite d'API ; deux ont été repris sur leur transcription, sans refaire leurs lectures.

**Ce que la session principale a vérifié.** Chaque citation, par script : **2275 citations, 0 introuvable, 0 ligne annoncée démentie**. Le vérificateur a d'abord été éprouvé sur un faux brouillon (vraies citations, coupes, guillemets imbriqués, paraphrase, coupe inventée, citation attribuée au mauvais fichier) : il a accepté les vraies et refusé les trois fausses. Les onze échecs du premier passage étaient huit en-têtes de colonne de gabarit et trois citations du vocabulaire contrôlé, que le vérificateur ne consultait pas encore. Puis la relecture a porté sur chaque énoncé **R, N et O** et sur chaque question ; les points qui décident ont été contrôlés sur pièce : la lettre de D76 et de D78, la section A19 de `passe-2.md`, la fiche de spécification de l'unité, le vocabulaire du reflux, les entrées tronquées, les empreintes des quatre gels.

**Ce que cela ne garantit pas.** Une citation retrouvée prouve que le texte existe, non que le sort qui s'en réclame est juste. Les énoncés **C** et **K** ont été relus par échantillon, non un par un.

**Les architectures par chapitre** sont versées à côté de ce document : `protocoles/architecture-L1-C17.md` à `protocoles/architecture-L1-C30.md`, et `protocoles/releve-apres-gel-L1-C23-C25.md`.

---

## 1. Mesures

| chapitre | mots du corps | sources ouvertes / à requalifier | vérifications en attente | énoncés | K | C | R | O | N | dont sorts qualifiés ou composés | questions |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L1.C17 | 2885 | 6 / 8 | 19 | 52 | 18 | 23 | 2 | 4 | 5 | 2 | 3 |
| L1.C18 | 6150 | 11 / 11 | 33 | 94 | 37 | 37 | 5 | 10 | 0 | 58 | 6 |
| L1.C19 | 3903 | 5 / 4 | 20 | 61 | 12 | 30 | 2 | 7 | 10 | 0 | 4 |
| L1.C20 | 4371 | 4 / 6 | 24 | 49 | 12 | 21 | 1 | 11 | 4 | 0 | 7 |
| L1.C21 | 5520 | 5 / 10 | 24 | 61 | 20 | 27 | 4 | 3 | 7 | 16 | 5 |
| L1.C22 | 5499 | 6 / 8 | 13 | 46 | 9 | 26 | 2 | 9 | 0 | 5 | 4 |
| L1.C24 | 3945 | 4 / 8 | 9 | 48 | 22 | 18 | 2 | 4 | 2 | 0 | 4 |
| L1.C26 | 4318 | 4 / 5 | 8 | 52 | 13 | 27 | 4 | 1 | 7 | 0 | 4 |
| L1.C27 | 3730 | 5 / 4 | 6 | 47 | 15 | 16 | 2 | 12 | 2 | 8 | 4 |
| L1.C28 | 2610 | 3 / 4 | 7 | 39 | 15 | 19 | 2 | 0 | 3 | 10 | 3 |
| L1.C29 | 4488 | 2 / 4 | 7 | 65 | 12 | 32 | 4 | 10 | 7 | 0 | 7 |
| L1.C30 | 2020 | 1 / 1 | 5 | 30 | 9 | 15 | 0 | 3 | 3 | 3 | 7 |

Mots, sources et vérifications sont lus dans les chapitres par script ; énoncés, sorts et questions sont comptés dans les tableaux des architectures. Un sort qualifié ou composé — « K et N », « R, sauf source », « N (O) »… — est compté à son premier sigle, et la colonne dédiée en donne le nombre ; une ligne sans sigle initial (« à sourcer ou à décider ») n'est comptée que parmi les énoncés.

---

## 2. Constats transversaux

**T1 — La cartographie de refonte est périmée sur plusieurs fiches, et le registre fait foi.** Elle date du 2026-09-10. Depuis : les « obligations graduées » qu'elle prête à la compensation symétrique ont été retirées par D71 ; A43 a été scindé puis jugé de D68 à D91 ; le reflux est « retenu, non annulé » depuis A2 bis. Les architectures s'alignent sur le registre, non sur les fiches.

**T2 — Le résultat le plus lourd de L1.C27 reposait sur la parité fixe.** Le chapitre tire de deux mécanismes du livre que « le barème voté au centre détermine la balance des paiements de chaque pays », et l'un des deux est « la parité fixe qui ferme le canal du change ». Or les parités strictement fixes sont jugées non applicables sans transferts permanents (A43 (3a)), et sous les parités administrées la parité glisse par règle (D69). **Le résultat ne suit plus tel qu'il est écrit** ; une concentration de pouvoir demeure, dont le siège est à exposer.

**T3 — La « contradiction interne » que la refonte jugeait rédhibitoire dans L1.C28 est levée pour le dispositif arbitré.** Le livre nommait la croissance du produit parmi les critères possibles de révision des parités. La règle arrêtée lit une position de compensation au regard d'un corridor (D69, D85), sur des quotas proportionnels aux importations (D83), et la position nette depuis D88 : aucune grandeur de production n'y entre, dans le texte comme dans le modèle.

**T4 — La forme de l'unité traverse six chapitres, et la pièce qui la trancherait n'a jamais été écrite.** L1.C19, C20, C22, C24, C26 et C29 raisonnent sur l'unité du livre — nominative, non cessible, détruite à la conversion, jamais détenue —, alors que la priorité de modélisation arrêtée est une unité de réserve tenue par les banques centrales (A37), et que la compensation de (3b) fait tenir aux banques centrales des positions débitrices et créditrices qui se remboursent ou s'annulent. Selon la branche, des résultats du Livre 1 changent de portée : le test « ni principal ni intérêt » (C22), « strictement en deçà du DTS » (C24), « jamais détenu » (C26), les quatre propriétés qui fondent le nom (C20). **Le corpus s'est lui-même réclamé la pièce qui départagerait** — une fiche de spécification de l'unité : droits du détenteur, obligations de l'émetteur, règle de conversion, extinction, détenteurs autorisés, sort en cas de sortie d'un membre — et il dit ne l'avoir pas produite (L10.C06 ; L20.C02 : aucune conclusion sur l'article 123 avant elle). Question D92.

**T5 — Le vocabulaire contrôlé se contredit sur le reflux.** Une entrée le définit comme « destruction de la monnaie après sa création » ; l'entrée du reflux transactionnel porte l'arbitrage du 2026-09-05 : « La monnaie quitte donc la circulation sans être détruite. » L1.C17, C18, C19 et C21 emploient l'un ou l'autre. Question D94.

**T6 — Le gel de L1.C25 est rompu, sur l'en-tête seulement ; ceux de L1.C13, C14 et C23 tiennent.** Empreintes recalculées : les trois fichiers sont identiques à l'état gelé que donne leur dossier d'audit ; L1.C25 ne l'est plus. Deux commits du 2026-09-16 au soir ont touché son en-tête — empreintes d'exemplaire de S2 et S3, S9 rebasée et ouverte par D63 — ; le corps et le résumé sont intacts (empreinte éditoriale inchangée). **Le dossier d'audit de L1.C25 annonce S9 fermée alors qu'elle est ouverte.** Question D101.

**T7 — Deux phrases de METHODE-PERIMETRE ne tiennent pas ensemble.** « Terminé » signifie les trente et un chapitres vérifiés, et « C30 reste brouillon, déclaré récit ». Si C30 reste brouillon, trente et un chapitres `verifie` n'arrivent jamais ; C30 n'est pourtant pas techniquement exclu de `verifie`. Question D100.

**T8 — Défauts mécaniques relevés, à corriger à la réécriture sans décision.** Sources déclarées jamais appelées dans le corps : L1.C21 S6 et S8, L1.C29 S5. Entrées de `verifications_en_attente` tronquées à leurs premières lettres : quatre dans L1.C21, une dans L1.C27, deux dans L1.C28. Annexes de balayage et historiques de correction encore dans le corps de plusieurs chapitres.

**T9 — La table fonctions d'A46 ↔ chambres, que la refonte déclarait à conduire, est faite ; elle ne conclut ni à cinq chambres, ni à quatre sans conditions** (`protocoles/architecture-L1-C18.md`, § 3 bis). Le cumul complet que la lettre d'A46 nomme — mesurer, qualifier, verser et se contrôler — n'est dans aucune chambre du livre tel que le chapitre le décrit. Mais l'Office de certification réunit trois fonctions sans séparation écrite : la mesure, la qualification par le label, le contrôle des bénéficiaires. La priorité entre projets admissibles, la suspension, la correction et la récupération, et le contrôle indépendant de conformité n'ont pas de titulaire ; les nominations et les budgets par centre ne sont pas décrits. **Quatre chambres suffisent si ces séparations sont écrites.** Deux absences — le rythme, la suspension — sont peut-être des omissions du chapitre et non du livre : l'exemplaire du livre est à relire avant d'écrire « absent du livre ». Et les fonctions arbitrées depuis — l'exécution de la compensation, les guichets d'A45, les procédures structurelles — ne sont attribuées à aucun centre. Questions D102 et D103.

**T10 — Deux appuis de L1.C18, que d'autres textes tiennent pour acquis, sont à vérifier sur pièce.** La marge d'incertitude de 20 à 50 % sur les indices synthétiques d'état, que F2 tient pour établie en citant ce chapitre et que L15.C01 reprend, n'a pas été retrouvée par le sous-agent dans le passage du cadre statistique qui porte les catégories. Et l'étude invoquée pour valider « fortement » l'abandon de l'additionnalité contrefactuelle estimerait elle-même des contrefactuels. **Ce sont des relevés de sous-agent sur des pièces que la session principale n'a pas relues : rien n'est propagé avant lecture.** Questions D104 et D105.

---

## 3. Feuille de décisions

Les questions sont numérotées à la suite de l'index des décisions. **Chacune renvoie à l'architecture du chapitre, où se lisent les options complètes, leurs conséquences et les citations.** Recommandation en première position.

### 3.1 Ce qui demande une décision de l'auteur

**D92 — La forme de l'unité (T4 ; C19 O4, C20 Q1-Q2, C22 Q1, C24 Q3, C26 Q1, C29 A).** (a) **Exposer dans chaque chapitre les trois branches — unité du livre, unité de réserve d'A37, positions de compensation de (3b) — sans conclure, et faire de la fiche de spécification de l'unité le prochain chantier du passif** ; (b) prendre l'unité de réserve comme référence du Livre 1, ce qui tranche de fait la priorité de modélisation d'A37 ; (c) garder l'unité du livre comme référence, A37 restant une commodité de modélisation. *Recommandation : (a)* : A35b est ouvert, A37 seulement orienté, et la fiche est la pièce que le corpus s'est réclamée.

**D93 — Le financement régénératif est-il encore un canal de rééquilibrage extérieur ? (T2 ; C27 Q1).** (a) **L'exposer dans L1.C27 sans trancher, en disant que seule la branche « par les guichets d'A45 » est décrite par des pièces arbitrées** ; (b) non : le rééquilibrage relève du seul Exchange Standard (3b) ; (c) oui, en complément de (3b) ; (d) seulement par les guichets d'A45. *Recommandation : (a)*, parce que le modèle n'a jamais joué ce canal. Mais c'est la thèse du livre sur le rééquilibrage : l'auteur peut vouloir la trancher avant la réécriture de L1.C26.

**D94 — Le reflux : retrait ou destruction (T5 ; C17 Q2, C19 Q4, C21).** (a) **Écrire « retrait de la circulation », renvoyer le sort du reflux à EXCEDENT-DU-SYMPOSIUM, et corriger l'entrée du vocabulaire qui dit « destruction »** ; (b) distinguer deux étages : destruction de dépôts à la perception nationale, rétention au Symposium ; (c) garder « destruction » jusqu'à l'adoption de la formule d'affectation. *Recommandation : (a)*, seule option qui n'affirme rien au-delà d'A2 bis ; (b) est plus exacte mais décrit un circuit que `passe-2.md` déclare à préciser.

**D95 — Quel démurrage les chapitres examinent-ils ? (C21 Q1).** (a) **La conception du livre — encaisses des agents au-delà d'un seuil —, en disant que la forme expérimentable le restreint aux soldes institutionnels en unités (D76, D78)** ; (b) la seule forme expérimentable ; (c) déclarer abandonné le démurrage des ménages. *Recommandation : (a)* : rien dans D76, D78 ni la conclusion du 2026-09-09 n'abandonne la conception du livre, et les objections du chapitre sont des résultats sur elle. (c) serait un changement de doctrine.

**D96 — Les coûts réels comprennent-ils le coût d'opportunité de la préservation ? (C27 Q2 ; CRITERE-L25).** (a) **L'exposer en attendant une décision, en disant que la force du premier levier de L1.C27 en dépend** ; (b) oui : le renoncement à exploiter est rémunéré ; (c) non : seules les actions sont financées ; (d) le laisser à la priorité sociale et territoriale. *Recommandation : (a)*, mais c'est un choix que le texte de F13 ne permet pas d'inférer, et que l'auteur devra faire.

**D97 — « PT = MV transformé » (C21 Q2).** (a) **Appliquer l'arbitrage de l'auteur du 2026-09-04 : cadre de conception, non preuve ; deux phrases dans L1.C21, le détail au Livre 2** ; (b) suivre la cartographie de refonte, qui classe la reformulation « abandonnée ». *Recommandation : (a)*, parce qu'une cartographie ne vaut pas arbitrage.

**D98 — Les infrastructures critiques dans le périmètre financé (C22 Q3 ; C30 B3).** (a) **Les inclure sous le test de l'apport propre, contre la tarification régulée et l'investissement public, et inscrire A5 au registre, qui ne le porte pas** ; (b) les exclure ; (c) les inclure sans condition. *Recommandation : (a)*, qui applique un test déjà arbitré.

**D99 — Les titres (C24 Q1, C17 Q1, C27 Q3).** L1.C24 réfute son titre : quatre propositions dans son architecture, **sans recommandation sur le choix**, et une recommandation de procédure — ne pas renommer le fichier, dont l'adresse dérive. L1.C17 et L1.C27 bornent leur titre sans le réfuter : *garder les titres du plan directeur et ouvrir sur la réponse restreinte*. **Les intitulés viennent du plan directeur de l'auteur, qui tranche.**

**D100 — L1.C30 (T7 ; C30 Q1 à Q3).** Trois choix : la forme de la déclaration « récit » sans modifier le schéma (en prose, mention d'ouverture définie par la convention, ou hors du chapitre) ; le sens de « terminé » (trente et un chapitres, ou trente et C30 déclaré récit) ; aligner C30 ou le laisser en l'état. *Pas de recommandation sur le fond, par consigne ; recommandation de procédure : que l'auteur énonce la clause « C30 reste brouillon, déclaré récit » dans un texte de référence. Aujourd'hui, seuls l'index des décisions et le bilan du 2026-09-16 la portent ; le billet du journal que l'index cite comme autorité ne la contient pas.*

**D101 — Le dossier d'audit de L1.C25 (T6 ; relevé après gel, G1).** (a) **S'il n'est pas encore soumis, le régénérer sur l'état actuel, sous la nouvelle empreinte, sans toucher au chapitre** ; (b) s'il l'est, tenir l'audit pour valide sur le corps et le résumé, inchangés, et traiter comme dépassée toute objection sur S2, S3 ou S9. *Recommandation : (a) si le dossier n'est pas parti, (b) sinon.*

**D102 — Où vivent les cinq centres de l'institution (T9 ; C18 7.1).** (a) **L1.C18 expose la table de correspondance, les conditions de conformité et les organisations possibles — quatre chambres et séparations internes, une chambre de plus, une liste de pouvoirs non délégables —, et le choix va au chapitre de gouvernance A46-A47 que prévoit la refonte** ; (b) garder quatre chambres et écrire les séparations comme conditions ; (c) ajouter une chambre, de mesure ou de contrôle de conformité ; (d) une organisation dotée d'une liste de pouvoirs non délégables. *Recommandation : (a), en présentant (b) comme la branche la plus proche du livre* : A46 laisse l'organisation ouverte.

**D103 — La fixation des seuils (A47) et la priorité démocratique (A46) relèvent-elles du même centre ? (C18 7.2).** (a) Un seul centre, l'Assemblée des Communs, qui fixe d'avance les seuils et la grille de priorité, appliqués par un tiers ; (b) deux centres : les normes à l'Assemblée, la priorité à un centre distinct, territorial par exemple ; (c) les seuils dans l'acte fondateur, la priorité à l'Assemblée. *Pas de recommandation sur le fond* : la lettre des deux arbitrages ne le dit pas, et la table du § 3 bis en dépend. D'ici là, L1.C18 expose sans choisir.

**D104 — Le fondement de l'abandon de l'additionnalité contrefactuelle (T10 ; C18 7.3).** (a) **Après lecture de la pièce (S18, sous D66) : garder l'abandon au niveau du paiement, le fonder sur la manipulation des scénarios de référence déclarés et sur la déformation par l'annonce (F2), attribuer « invérifiable » au livre, et dire que l'additionnalité en ressources demeure au niveau de l'instrument (L1.C31)** ; (b) la même chose, sans la phrase sur L1.C31 ; (c) garder « fiction invérifiable » et « valide fortement ». *Recommandation : (a)*, seule option qui ne contredirait ni la pièce citée ni un chapitre vérifié. La définition `additionnalite` du vocabulaire, qui cite ce passage, serait à revoir hors du chapitre.

**D105 — La marge d'incertitude de 20 à 50 % (T10 ; C18 7.5 ; F2).** (a) **La chercher d'abord sur la pièce ; si elle n'y est pas, corriger L1.C18 sur les catégories que porte le cadre statistique, écrire la condition de F2 sans chiffre, et propager à F2 et à L15.C01** ; (b) chercher et ouvrir une autre source de la marge ; (c) retirer la phrase. *Recommandation : (a)*, parce qu'une condition de falsification ne peut pas s'illustrer d'un chiffre sans source.

### 3.2 Ce que les architectures recommandent d'exposer sans trancher — une validation en bloc

METHODE-REECRITURES prescrit déjà d'exposer les branches ouvertes ; **ces points ne demandent une décision que si l'auteur veut les trancher maintenant**. Les architectures recommandent de les exposer : la fonction « reflux sur les dettes des flux Yang », comme hypothèse à instruire (C19 Q1, C21 Q4) ; l'assiette financière du prélèvement, en lecture de travail conciliatrice (C21 Q3) ; le mode de fixation des niveaux de taux de reflux, P48 (C21 Q5) ; l'objet de la clé de répartition, pays ou projets, à trancher avec l'autorité de CRITERE-L25 (C22 Q2) ; la réponse de F13 appliquée au tableau de bord, A18 (C28 Q2) ; la parité de départ, à exposer en L1.C26 (C28 Q3) ; les monnaies membres face aux non-membres, « non instruit » (C26 Q2) ; la clause de neutralité anticoloniale, renvoyée au chantier du barème aux frontières (C27 Q4).

**D106 — Valider en bloc l'exposition de ces points**, ou désigner ceux que l'auteur veut trancher.

### 3.3 Choix d'édition et de périmètre — une validation en bloc

Ils ne touchent pas la doctrine ; chacun a sa recommandation dans l'architecture du chapitre. Portée documentaire des §§ 2 et 3 de C17 (Q3) ; portée du § 6 de C19 et place de la dominance budgétaire (Q2, Q3) ; attribution au livre, faits zimbabwéens, positionnement face aux propositions voisines, financement des guichets, partage Livre 1 / Livre 2 dans C20 (Q3 à Q7) ; passages empiriques sans source et lieu de l'analyse de la règle de vote dans C18 (7.4, 7.6) ; rétractations dans le corps de C22 (Q4) ; annexes datées et notes de Mehrling dans C24 (Q2, Q4) ; niveau de détail chiffré, étalon-or et nuance de Rey dans C26 (Q3, Q4) ; attribution des propriétés de la robustesse dans C28 (Q1) ; chemin critique, voie du démurrage, annexes, vérification v1, prix de l'issue, nombre de promesses dans C29 (Q1, Q3 à Q7) ; et, si C30 est aligné (D100), l'universel du récit, « rendrait finançable », les jalons du § 5 et la vérification de la l. 24 (C30 Q4 à Q7) ; et, pour après l'audit de C23 et C25, le lieu de la chaîne A43, le § 6 de C25 et le taux que vise l'objection des zones monétaires (G2 à G4).

**D107 — Valider en bloc les recommandations d'édition et de périmètre**, ou désigner les exceptions.

### 3.4 Déterminé par les règles existantes — aucune décision

Exposer une branche sans préférence quand l'objet est ouvert (index des décisions : un agent ne choisit pas une branche au nom de l'auteur ; C20, C29) ; sortir du corps l'historique des corrections (règle éditoriale du 2026-09-08 ; C22, C27) et les annexes de balayage (précédent de l'auteur du 2026-09-14 pour L1.C09 et L1.C11 ; C21, C24, C29) ; calculer les décomptes par script (convention ; C29) ; appeler ou retirer les sources déclarées jamais appelées, et réparer les entrées tronquées (T8) ; vérifier sur l'exemplaire du livre toute attribution au livre que l'en-tête donne au script d'adaptation (C20).

---

## 4. Ordre des lots proposé

1. **Lot 1 — le système monétaire international : L1.C24, L1.C26, L1.C27.** Leurs arbitrages sont les derniers rendus et les mieux instruits (A32, A43, D68 à D91) ; ils dépendent de D92 et D93, qu'ils peuvent exposer.
2. **Lot 2 — la proposition : L1.C17, L1.C20, L1.C21.** A44 et A46 arbitrés ; A35b et F1 ouverts, donc des branches ; dépend de D92, D94, D95 et D97.
3. **Lot 3 — l'institution : L1.C18, L1.C19, L1.C22.** Dépend de D102 à D105, de D92 et de D98 ; la table fonctions ↔ chambres de L1.C18 est faite, le choix d'organisation ne l'est pas.
4. **Lot 4 — la mesure et l'état du dossier : L1.C28, L1.C29, L1.C30.** L1.C29 dresse l'état du dossier : il vient après les autres. C30 selon D100.

**L1.C23 et L1.C25 suivent leur propre voie** : audit tiers, puis propagation du relevé après gel.

---

## 5. Ce que ce document ne vérifie pas

Il ne vérifie aucune source externe, et n'en ouvre aucune. Il ne vérifie pas que les réécritures tiendront à l'audit tiers, obligatoire pour ces chapitres de conception. Il ne tranche aucun objet ouvert ; il ne dit pas que les arbitrages sont justes, seulement ce qu'ils commandent. Les énoncés K et C sont relus par échantillon. Et la vérification de conformité des brouillons au registre vaut pour l'état du dépôt au commit `07688307`.
