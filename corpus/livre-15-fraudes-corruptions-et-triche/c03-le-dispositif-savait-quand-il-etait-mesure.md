---
chapitre: L15.C03
titre: "Le dispositif savait quand il était mesuré"
livre: 15
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
    reference: "**S. R. H. Barrett et al., « Impact of the Volkswagen emissions control defeat device on US public health », *Environmental Research Letters*, vol. 10, n° 114005, 2015, 11 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depuis le dépôt institutionnel du MIT, par son interface de programmation, **après refus du site de l'éditeur (captcha Radware — mur anti-robot déclaré et non franchi).** Lu dans le texte. **DROITS, LUS DANS LE DOCUMENT : « *Content from this work may be used under the terms of the Creative Commons Attribution 3.0 licence* » — régime `libre`, sous condition d'attribution à l'auteur, au titre, à la revue et au DOI.** **C'ÉTAIT L'ACQUISITION DE RANG 1 INSCRITE DEUX FOIS PAR CE LIVRE : la fraude MÉTROLOGIQUE, celle que son motif de registre nomme.**"
    date_verification: 2026-09-08
verifications_en_attente:
  - "**LE CORPUS N'A PAS OUVERT LA DÉCOUVERTE, IL EN A OUVERT LA CONSÉQUENCE.**
     Cette source quantifie les effets sanitaires ; **elle n'est pas l'étude qui a
     mis au jour le dispositif de contournement.** Celle-ci est citée en
     bibliographie — des essais sur route conduits pour un organisme indépendant.
     **ACQUISITION DE RANG 1 : l'étude de détection elle-même**, car c'est elle qui
     porte le seul enseignement directement transposable — **comment on a trouvé.**"
  - "**LE TRANSFERT AU DISPOSITIF EST UNE ANALOGIE DE FORME, ET LE CORPUS NE LA
     POUSSE PAS.** Un moteur est un objet manufacturé dont le comportement est
     programmable ; **un écosystème ne l'est pas.** **On ne programme pas une
     forêt pour qu'elle se comporte autrement pendant un relevé.** **Ce qui se
     transporte n'est donc pas le dispositif de contournement, c'est LA STRUCTURE
     DE L'INCITATION : quand le contrôle est identifiable, il devient une
     situation à part, et ce qui est optimisé est la situation, non l'état.**"
  - "**LES CHIFFRES SANITAIRES SONT DES ESTIMATIONS DE MODÈLE À LARGE INTERVALLE.**
     Cinquante-neuf décès prématurés, avec un intervalle de confiance à 95 % allant
     de 10 à 150 — **soit un facteur quinze entre les bornes.** **Le corpus
     rapporte l'ordre de grandeur et l'intervalle ensemble, jamais le point seul.**"
  - "**AUCUNE SOURCE SUR LA CAPTURE DE CERTIFICATEUR.** Le livre tient désormais
     trois architectures — ligne de base, fiscalité du transfert, mesure — **et
     toujours rien sur le troisième terme de son motif de registre : la capture du
     régulateur.** **C'est le seul point où L1.C18 § 5 déclare une limite que le
     corpus n'a documentée d'aucune manière.**"
resume: "Ce chapitre ouvre la troisième architecture de fraude du livre, et c'est celle que son motif de registre nommait sans que le corpus en eût aucune source, à savoir la falsification de la mesure elle-même. Un constructeur automobile a installé dans ses véhicules un logiciel qui détectait que le véhicule subissait un essai d'émissions et modifiait alors le fonctionnement du système de dépollution, de sorte que les émissions réelles d'oxydes d'azote se sont révélées supérieures d'un facteur de dix à quarante à la norme, sur des millésimes couvrant six années. Le chapitre retient que la falsification n'a porté ni sur un registre, ni sur un document, ni sur un scénario de référence, mais sur le comportement de l'objet mesuré pendant la mesure, et que l'essai de certification a été passé avec succès. Il établit que ce qui se transporte au dispositif examiné par ce corpus n'est pas le mécanisme, puisqu'on ne programme pas un écosystème, mais la structure de l'incitation, car dès lors qu'un contrôle est identifiable il devient une situation particulière et c'est cette situation qui est optimisée plutôt que l'état à mesurer. Il tire de la manière dont la fraude a été découverte un principe de conception, à savoir que le contrôle doit être pour partie indiscernable du fonctionnement ordinaire, la découverte étant venue de mesures conduites hors du protocole et non d'un protocole amélioré. Il relève enfin que ce principe entre en collision avec le coût du contrôle établi par le premier chapitre de ce livre, un contrôle inopiné coûtant davantage et non moins, et que le livre ne dispose toujours d'aucune source sur la capture du certificateur."
concepts: [additionnalite, qualification_regenerative, bareme, regle_contre_discretion, robustesse]
renvois: [L1.C18, L11.C13, L11.C30, L15.C01, L15.C02, L18.C15, L26.C12]
---

# Le dispositif savait quand il était mesuré

::etat:: **Ce livre a inscrit deux fois, en rang 1, la fraude MÉTROLOGIQUE** — celle que son motif de registre nomme et dont il n'avait aucune source. **Elle est ouverte** [S1]. **Et elle prend une forme plus radicale que « falsification des relevés » : la falsification était DANS L'OBJET MESURÉ, et elle ne fonctionnait QUE PENDANT LA MESURE.**

## 1. Le mécanisme, en une phrase

::etat:: **Le logiciel** *« **detected if the vehicle was undergoing emissions testing and modified operation of the emission control system** »* [S1].

::etat:: **L'écart** : *« On-road emissions testing suggests that **in-use NOx emissions for these vehicles are a factor of 10 to 40 above the EPA standard** »*, sur les millésimes **2009 à 2015**. **Le constructeur a admis l'inclusion de ces dispositifs.**

::hypothese:: **Rien n'a été falsifié au sens ordinaire.** **Aucun registre, aucune pièce justificative, aucun scénario de référence.** **L'essai de certification a été passé, et il a été passé honnêtement : l'appareil respectait la norme PENDANT L'ESSAI.** **Ce qui a été truqué est la relation entre l'état mesuré et l'état ordinaire.**

## 2. Ce que cela coûte, et le corpus donne l'intervalle avec le point

::etat:: **Sur la période de vente 2008-2015** [S1] : *« we estimate that the excess emissions will cause **59 (95% CI: 10 to 150) early deaths** in the US »*, pour un coût social d'environ **450 millions de dollars**. **Et un retour à la conformité de tous les véhicules concernés avant fin 2016 éviterait environ 130 décès prématurés et 840 millions de dollars de coûts sociaux.**

::etat:: **L'intervalle va de 10 à 150 — un facteur quinze entre les bornes.** **Le corpus rapporte l'ordre de grandeur et l'intervalle ensemble, jamais le point seul** — c'est la même discipline que A39 impose au rendement énergétique.

## 3. Ce qui se transporte au dispositif, et ce qui ne se transporte pas

::etat:: **CE QUI NE SE TRANSPORTE PAS, ET IL FAUT LE DIRE D'ABORD.** Un moteur est un objet manufacturé dont le comportement est **programmable**. **Un écosystème ne l'est pas.** **On ne programme pas une forêt pour qu'elle se comporte autrement pendant un relevé.**

::hypothese:: **CE QUI SE TRANSPORTE EST LA STRUCTURE DE L'INCITATION, ET ELLE EST INDÉPENDANTE DU SUPPORT.** **Dès qu'un contrôle est IDENTIFIABLE — parce qu'il est annoncé, périodique, ou reconnaissable à ses instruments — il cesse d'être un échantillon de l'état ordinaire et devient UNE SITUATION PARTICULIÈRE.** **Et ce qui est optimisé est alors la situation, non l'état.**

::hypothese:: **Le régime probatoire de L1.C18 est exposé à cela par construction, et de deux manières.** **Les relevés de terrain sont des visites : elles ont une date, un lieu et des opérateurs.** **Et la rente de maintien est conditionnée à un constat périodique** — donc à des rendez-vous. **Une parcelle qu'on sait visitée au printemps n'est pas dans le même état qu'une parcelle qu'on ne sait pas visitée.**

::etat:: **Le corpus ne prétend pas que cela se produirait.** **Il établit que la forme de l'incitation est présente, et qu'aucun chapitre du corpus ne la traite.**

## 4. Comment on a trouvé, et c'est le seul enseignement de conception

::etat:: **La fraude n'a pas été trouvée en améliorant l'essai.** **Elle a été trouvée par des mesures EN CONDITIONS RÉELLES, conduites hors du protocole de certification** — *« on-road emissions testing »* [S1].

::hypothese:: **Le principe de conception qui en sort est simple et le corpus le formule pour la première fois : UN CONTRÔLE DOIT ÊTRE, AU MOINS EN PARTIE, INDISCERNABLE DU FONCTIONNEMENT ORDINAIRE.** **Ce n'est pas la rigueur du protocole qui protège, c'est son imprévisibilité.** **Un protocole plus sévère mais annoncé reste optimisable ; un protocole plus léger mais inopiné ne l'est pas.**

::hypothese:: **Appliqué au dispositif, cela donne deux exigences concrètes.** **Les relevés de terrain doivent comporter une part INOPINÉE**, et la proportion doit être publiée sans que les dates le soient. **Et la télédétection continue, que L1.C18 tient pour un moyen de mesure, doit aussi être tenue pour un moyen de CONTRÔLE DE LA MESURE** — c'est le seul instrument dont l'observé ne connaît pas le calendrier.

## 5. Et le principe entre en collision avec le coût

::etat:: **L15.C01 a établi que le coût du contrôle est un paramètre de fraude**, et que les relevés que le satellite ne fournit pas absorbent jusqu'à **25 % de l'annuité** [L1.C18].

::hypothese:: **Un contrôle inopiné coûte PLUS, non moins.** Il interdit de grouper les déplacements, d'optimiser les tournées, de prévenir pour préparer l'accès. **Le principe de conception que ce chapitre dégage aggrave donc le paramètre que le chapitre précédent a identifié comme critique.**

::hypothese:: **C'est une tension réelle et le livre ne la résout pas. Il la pose dans sa forme exacte : la propriété qui rend un contrôle efficace est celle qui le rend cher, et le coût du contrôle est ce qui pousse à l'alléger.** **Un dispositif qui ne budgète pas explicitement le surcoût de l'imprévisibilité fera, par simple gestion, le choix du contrôle annonçable.**

## 6. Ce que le livre tient maintenant, et ce qui manque encore

::etat:: **Trois architectures, et elles n'ont rien en commun.** **L15.C01** : la ligne de base — une fausse qualification **sans tricheur**. **L15.C02** : la fiscalité du transfert — des tricheurs qui **ne touchent pas à l'objet protégé**. **L15.C03** : la mesure — **l'objet mesuré se comporte autrement pendant la mesure**.

::hypothese:: **Le modèle d'adversaire que L15.C01 réclamait commence donc à prendre forme, et il a une propriété que le corpus n'attendait pas : DANS AUCUN DES TROIS CAS L'ADVERSAIRE N'ATTAQUE LA GRANDEUR ÉCOLOGIQUE ELLE-MÊME.** Il attaque **le cadre qui la compare**, **la fiscalité qui la transfère**, ou **le moment où on la regarde**. **Le corpus protégeait la mesure ; les trois fraudes documentées passent à côté d'elle.**

::etat:: **ET IL MANQUE TOUJOURS LE TROISIÈME TERME DU MOTIF DE REGISTRE : LA CAPTURE DU RÉGULATEUR.** **C'est le seul point où L1.C18 § 5 déclare une limite — l'État audité et bénéficiaire — que le corpus n'a documentée d'aucune manière.**

## 7. Ce que ce chapitre n'établit pas

::etat:: **Il a ouvert la CONSÉQUENCE, non la DÉCOUVERTE.** Cette source quantifie les effets sanitaires ; **l'étude qui a mis le dispositif au jour est citée en bibliographie et n'est pas ouverte.** **Or c'est elle qui porte l'enseignement transposable — comment on a trouvé. Acquisition de rang 1.**

::etat:: **Il ne prétend à aucune fréquence.** Un cas documenté n'établit pas qu'une architecture soit répandue, et le corpus n'a rien sur la prévalence.

::etat:: **Et le transfert au dispositif est une analogie de FORME**, explicitement bornée en section 3. **Le corpus n'affirme pas qu'un bénéficiaire se comporterait ainsi : il affirme que la structure d'incitation qui l'a produit ailleurs est présente ici, et non traitée.**
