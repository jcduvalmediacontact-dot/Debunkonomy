---
chapitre: L2.C10
titre: "De la stabilité à la robustesse"
livre: 2
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-06
autorite: preparatoire
citable: false
regime: conception
sources_primaires:
  - ref: S1
    nature: theorie
    reference: "*Cahier Technique*, **épisode 2**, section 2 — la filiation revendiquée : « Le concept de robustesse a une histoire scientifique distincte, qui vient principalement de l'écologie des systèmes complexes. Sa première formulation moderne remonte à l'écologue canadien Crawford Stanley Holling [...] qui publie en 1973 un article devenu classique dans les *Annual Reviews of Ecology and Systematics*, intitulé *Resilience and Stability of Ecological Systems*. Holling y distingue explicitement deux propriétés qui, jusque-là, étaient confondues. LA STABILITÉ — capacité d'un système à revenir rapidement à un état d'équilibre après une perturbation. LA RÉSILIENCE — capacité d'un système à absorber les perturbations et à se réorganiser tout en conservant ses fonctions essentielles [...] Ces deux propriétés [...] PEUVENT ÊTRE INVERSEMENT CORRÉLÉES. » Prolongements cités : Levin, Walker et Salt (*Resilience Thinking*, 2006). **OUVERT le 2026-09-06**"
    date_verification: 2026-09-06
  - ref: S2
    nature: theorie
    reference: "Même source, section 5, tableau de correspondance — « CONCEPT OPÉRATIONNEL CENTRAL. Orthodoxie : stabilité — retour rapide à l'équilibre après perturbation. NEMO IMS : robustesse — maintien des fonctions essentielles à travers LES PERTURBATIONS IMPRÉVUES. » Et « FILIATION THÉORIQUE. Orthodoxie : théorie des marchés efficients, économie néokeynésienne, macroéconomie DSGE. NEMO IMS : écologie des systèmes complexes (Holling), théorie de la résilience (Walker, Salt), économie écologique (Daly, Raworth). »"
    date_verification: 2026-09-06
  - ref: S3
    nature: theorie
    reference: "C. Borio, BIS Working Papers n° 128, 2003 — la thèse séparatrice : « A microprudentialist would argue that for a financial system to be sound IT IS NECESSARY AND SUFFICIENT THAT EACH INDIVIDUAL INSTITUTION IS SOUND. A macroprudentialist would take issue with this. » Et l'exemple : le resserrement défensif simultané de toutes les firmes, rationnel individuellement, aggrave le risque agrégé — « RISK WOULD THEREBY INCREASE ». Modèle du risque : « IN PART ENDOGENOUS with respect to the behaviour of the financial system ». **OUVERT le 2026-09-06**"
    date_verification: 2026-09-06
  - ref: S4
    nature: theorie
    reference: "Le corpus lui-même — `corpus/vocabulaire.yaml`, entrées `resilience` (première occurrence L1.C23) et `robustesse` (L1.C04). La première porte déjà la distinction de Holling : « À distinguer de la stabilité, qui désigne la vitesse de retour à un état d'équilibre : les deux propriétés PEUVENT ÊTRE INVERSEMENT CORRÉLÉES [...] LA ROBUSTESSE AJOUTE À LA RÉSILIENCE L'ABSORPTION DE PERTURBATIONS NON ANTICIPÉES. »"
    date_verification: 2026-09-06
verifications_en_attente:
  - "HOLLING 1973 N'EST PAS OUVERT. C'est la source du deuxième déplacement et
     **la seule référence scientifique nommée du Cahier hors économie.** Le
     corpus en tient la restitution par le Cahier et rien d'autre — alors que
     l'article est classique, court, et largement disponible."
  - "WALKER ET SALT 2006, LEVIN, DALY, RAWORTH : AUCUN N'EST OUVERT. Le
     tableau de filiation de l'épisode 2 nomme SIX auteurs pour le compte de
     NEMO IMS ; **le corpus n'en a lu aucun.** L8.C34 avait déjà déclaré ce
     manque pour l'économie écologique."
  - "LA FILIATION ATTRIBUÉE À L'ORTHODOXIE N'EST PAS VÉRIFIÉE. Le Cahier lui
     assigne « théorie des marchés efficients, économie néokeynésienne,
     macroéconomie DSGE ». **Le corpus ne tient aucun texte DSGE ni
     néokeynésien**, et il verra en revanche que la macroprudence pose le
     risque comme ENDOGÈNE, ce qui est incompatible avec l'efficience."
resume: "Ce chapitre traite le deuxième déplacement, qui substitue la robustesse à la stabilité comme objectif macroprudentiel ultime, et il établit que la substitution est juste mais que sa présentation en rupture est fausse deux fois. Il restitue d'abord la filiation revendiquée, qui remonte à l'article de Holling de 1973 distinguant la stabilité, vitesse de retour à l'équilibre, de la résilience, capacité d'absorber et de se réorganiser en conservant ses fonctions, et posant que les deux propriétés peuvent être inversement corrélées. Il relève que le corpus porte déjà cette distinction dans son vocabulaire contrôlé depuis son premier livre, et qu'il y ajoute la nuance que le Cahier omet, à savoir que la robustesse n'est pas la résilience mais lui ajoute l'absorption des perturbations non anticipées. Il établit ensuite le résultat principal. La thèse séparatrice de la macroprudence, formulée en 2003, est que la solidité de chaque institution prise isolément n'est ni nécessaire ni suffisante à la solidité du système, et que le resserrement défensif simultané de toutes les firmes, rationnel pour chacune, augmente le risque agrégé. C'est exactement la distinction de Holling, importée dans la finance vingt ans avant le Cahier. La filiation attribuée à l'orthodoxie est donc fausse sur son point central, puisqu'un cadre qui pose le risque comme endogène au comportement du système est incompatible avec la théorie des marchés efficients qu'on lui prête."
concepts: [robustesse, resilience, limites_planetaires, plafond_ecologique, sisyphe_economique]
renvois: [L1.C04, L1.C23, L2.C02, L2.C04, L2.C09, L2.C15, L8.C34, L11.C23]
---

# De la stabilité à la robustesse

::etat:: Ce chapitre traite **le deuxième déplacement**, qui substitue la robustesse à la stabilité comme objectif macroprudentiel ultime. **La substitution est juste ; sa présentation en rupture est fausse deux fois.**

## 1. La filiation revendiquée

::etat:: **Holling, 1973** [S1] : *Resilience and Stability of Ecological Systems*. L'article distingue **la stabilité** — vitesse de retour à un état d'équilibre après perturbation — de **la résilience** — capacité d'absorber la perturbation et de se réorganiser en conservant fonctions, structure et identité. **Et il pose que les deux propriétés peuvent être inversement corrélées** : un système optimisé pour un état revient vite à cet état **et se brise devant une perturbation qu'il n'a pas prévue.**

::etat:: **Le Cahier en tire son objectif** [S2] : « robustesse — maintien des fonctions essentielles à travers **les perturbations imprévues** ».

## 2. Le corpus porte déjà cette distinction, et il la porte mieux

::etat:: **`vocabulaire.yaml` la contient depuis L1.C23** [S4], avec la corrélation inverse explicitement notée — **et avec une nuance que le Cahier omet** : « **la robustesse ajoute à la résilience l'absorption de perturbations non anticipées** ».

::hypothese:: **La nuance n'est pas cosmétique.** La résilience de Holling suppose **un répertoire de perturbations** : on absorbe et on se réorganise face à ce dont on a la mémoire ou le modèle. **La robustesse porte sur ce qui n'était pas au répertoire.** Un système résilient a des marges dimensionnées ; **un système robuste a des marges qu'il ne sait pas justifier.**

::hypothese:: **Le corpus enregistre ce que cela coûte, parce que c'est le vrai obstacle de ce déplacement.** Une marge dimensionnée pour un choc identifié se calibre et se défend devant un actionnaire ou un régulateur. **Une marge dimensionnée pour l'inconnu ne se calibre pas** — et se fait retirer à la première revue de coûts. **Le Cahier revendique la robustesse et n'a aucune règle de dimensionnement pour elle.** C'est le même problème que L11.C23 a rencontré sur la contracyclicité, et il n'est pas résolu.

## 3. Le résultat principal : la distinction est déjà dans la finance depuis 2003

::etat:: **La thèse séparatrice de la macroprudence** [S3] : « for a financial system to be sound **it is necessary and sufficient that each individual institution is sound** » — **c'est ce que le macroprudentialiste conteste.**

::etat:: **Et l'exemple qui l'illustre est une corrélation inverse au sens de Holling** [S3] : resserrer ses limites de risque face à un risque accru est **rationnel** pour chaque firme — donc stabilisant à son échelle — et **« if all did that, each of them could end up worse off »**, le resserrement précipitant la tension et la baisse des prix, si bien que **« risk would thereby increase »**.

::hypothese:: **C'est la distinction de Holling, importée dans la finance vingt ans avant le Cahier, et sous une forme opératoire.** Un système composé d'unités individuellement stables **peut être collectivement fragile** : c'est la définition même de la perspective macroprudentielle, et non ce qu'elle ignore.

::hypothese:: **Le deuxième déplacement n'est donc pas un déplacement par rapport à la macroprudence : il en est le principe fondateur, étendu d'un cran.** Ce que le Cahier ajoute n'est pas la distinction stabilité/résilience — **c'est le périmètre du système considéré**, qui passe du système financier au trio biosphère-économie-finance. **L'ajout est réel et il est plus étroit que ce qui est annoncé.**

## 4. La filiation attribuée à l'orthodoxie est fausse sur son point central

::etat:: **Le Cahier assigne à l'orthodoxie** [S2] : « théorie des marchés efficients, économie néokeynésienne, macroéconomie DSGE ».

::etat:: **Et la macroprudence pose le risque comme « in part endogenous with respect to the behaviour of the financial system »** [S3].

::hypothese:: **Un risque endogène au comportement du système est incompatible avec l'efficience informationnelle.** Si les prix intégraient correctement l'information, le comportement défensif collectif ne créerait pas le risque qu'il cherche à fuir. **La macroprudence est constituée contre l'hypothèse d'efficience, pas sur elle.**

::hypothese:: **Le corpus relève la conséquence et elle est la même qu'en L2.C04 et L2.C09 : le Cahier confond deux adversaires.** La théorie de l'efficience est bien le fondement de **la microprudence** — risque exogène, calibrage institution par institution, corrélations indifférentes. **Elle n'est pas celui de la macroprudence.** Troisième chapitre consécutif à faire ce constat.

::hypothese:: **Et cela lui retire un allié dont il aurait besoin.** La note de 2022 versée en L2.C06 pose que le déverrouillage exige de « rompre avec le cadre théorique dominant fondé sur la théorie de l'efficience informationnelle et allocationnelle » — **rupture déjà consommée du côté macroprudentiel sur le versant informationnel**, et qui reste entière sur le versant **allocationnel**. **C'est là, et là seulement, que la rupture est à faire.**

## 5. Ce que le corpus ne tient pas

::etat:: **Holling 1973 n'est pas ouvert**, alors que c'est la source du déplacement et **la seule référence scientifique non économique nommée par le Cahier.** Article classique, court, disponible.

::etat:: **Aucun des six auteurs du tableau de filiation n'est ouvert** — Holling, Levin, Walker, Salt, Daly, Raworth. L8.C34 avait déjà déclaré ce manque pour l'économie écologique ; **il est identique un livre plus loin.**

::etat:: **Et aucun texte DSGE ni néokeynésien n'est au dossier**, de sorte que le corpus conteste une attribution de filiation **sans tenir les textes attribués.** Il le fait sur ce qu'il tient — la définition macroprudentielle — et pas au-delà.

## 6. Portée

::etat:: **La substitution est juste** : un système optimisé pour la stabilité de court terme peut être fragile devant l'imprévu, et les deux propriétés peuvent être inversement corrélées.

::hypothese:: **Le corpus porte la distinction depuis L1.C23 et il la porte mieux** — la robustesse **ajoute** à la résilience l'absorption du non anticipé. **Et c'est là que le déplacement coûte** : une marge dimensionnée pour l'inconnu ne se calibre pas, donc se fait retirer. **Le Cahier revendique la robustesse sans règle de dimensionnement.**

::hypothese:: **La distinction est dans la finance depuis 2003**, sous forme opératoire : des institutions individuellement stables peuvent former un système collectivement fragile. **Le deuxième déplacement est donc le principe fondateur de la macroprudence, étendu d'un cran** — l'ajout réel étant le périmètre du système, non la distinction.

::hypothese:: **La filiation attribuée à l'orthodoxie est fausse sur son point central** : un cadre qui pose le risque comme endogène est **constitué contre** l'hypothèse d'efficience. La rupture reste à faire sur le versant **allocationnel** — et là seulement.

::etat:: **Aucun des six auteurs revendiqués n'est ouvert, Holling compris.**
