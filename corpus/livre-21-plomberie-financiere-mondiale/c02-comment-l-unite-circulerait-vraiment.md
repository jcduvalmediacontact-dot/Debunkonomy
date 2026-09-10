---
chapitre: L21.C02
titre: "Comment l'unité circulerait vraiment, et ce que chaque étape exige"
livre: 21
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
    nature: normatif
    reference: "**PFMI, avril 2012 — PRINCIPE 12, SYSTÈMES DE RÈGLEMENT D'ÉCHANGE DE VALEUR.** L'infrastructure « should **eliminate principal risk** by ensuring that **the final settlement of one obligation occurs IF AND ONLY IF the final settlement of the linked obligation also occurs**, regardless of whether the FMI settles on a gross or net basis ». **PRINCIPE 7, RISQUE DE LIQUIDITÉ** : l'infrastructure « should maintain **sufficient liquid resources IN ALL RELEVANT CURRENCIES** to effect **same-day** and, where appropriate, **intraday and multiday** settlement of payment obligations with a high degree of confidence under a wide range of potential stress scenarios », incluant « **the default of the participant and its affiliates that would generate the largest aggregate liquidity obligation** ». **PRINCIPE 20, LIENS ENTRE INFRASTRUCTURES** : un lien « should have **a well-founded legal basis, IN ALL RELEVANT JURISDICTIONS**, that supports its design and provides adequate protection to the FMIs »"
    etat_lecture: a_requalifier
  - ref: S2
    nature: normatif
    reference: "**Même source — CE QUE LE CORPUS TENAIT DÉJÀ ET QUI S'ENCHAÎNE ICI.** **PRINCIPE 8, CARACTÈRE DÉFINITIF** : « clear and certain **final settlement, at a minimum by the end of the value date** ». **PRINCIPE 9, RÈGLEMENT EN MONNAIE** : « in **central bank money** where practical and available » ; à défaut, un actif de règlement présentant « **little or no credit or liquidity risk** ». **PRINCIPE 1** : base juridique opposable « **in all relevant jurisdictions** ». **PRINCIPE 19** : participation en paliers, directs et indirects. **PRINCIPE 13, DÉFAILLANCE D'UN PARTICIPANT** : des règles permettant « to take timely action to **contain losses and liquidity pressures** and **continue to meet its obligations** »"
    etat_lecture: a_requalifier
  - ref: S3
    nature: theorie
    reference: "**Le corpus lui-même.** **L3.C05** : « une monnaie doit être acceptée pour valoir, **un rail doit seulement être joignable** », et « un rail parfait sur lequel circulerait de la monnaie de crédit **laisserait le filtre exactement où il est** ». **L3.C09** : le dispositif **s'ajoute** au système existant, son unité **ne règle pas**. **L5.C02** : le principe 9 force un choix — « ou bien le rail règle en monnaie de banque centrale [...] **on entre et on n'a rien changé** ; ou bien l'unité est l'actif de règlement », question de fait sur sa contrepartie. **L21.C01** : le principe 15 exige des fonds propres, **et la séparation de l'émetteur et de l'infrastructure rend celle-ci indifférente à l'unité qu'elle transporte**"
    etat_lecture: a_requalifier
verifications_en_attente:
  - "LE CORPUS N'A JAMAIS DÉCRIT UNE SEULE OPÉRATION DE BOUT EN BOUT. Ni le
     nombre de bilans traversés, ni les écritures à chaque étape, ni le moment
     du caractère définitif, ni ce qui se passe si une étape échoue. **Ce
     chapitre pose les exigences ; il ne décrit pas le trajet**, et la revue
     contradictoire du 2026-09-07 avait précisément demandé **trois jeux
     d'écritures complets et séparés par entité.**"
  - "AUCUN SYSTÈME DE RÈGLEMENT EXISTANT N'EST OUVERT — ni CLS pour les
     opérations de change, ni un système à règlement brut en temps réel, ni une
     chambre de compensation. **Le corpus raisonne sur la norme et sur aucune
     mise en œuvre.**"
  - "LE BESOIN DE LIQUIDITÉ N'EST PAS CHIFFRÉ, et il ne peut pas l'être sans
     volume ni devise de référence. **Le principe 7 exige des ressources dans
     TOUTES les monnaies pertinentes**, et le corpus ne sait ni lesquelles, ni
     combien."
resume: "Ce chapitre instruit trois principes supplémentaires du standard des infrastructures de marché et il en tire ce que chaque étape de la circulation exigerait de l'unité. Le premier impose que le règlement définitif d'une obligation n'intervienne que si le règlement de l'obligation liée intervient aussi, afin d'éliminer le risque en principal, et le chapitre établit que cette exigence frappe précisément le point où l'unité rencontre une monnaie nationale, c'est-à-dire l'endroit où le dispositif est le plus vulnérable puisque son unité ne règle pas. Le deuxième impose de détenir des ressources liquides dans toutes les monnaies pertinentes pour régler le jour même, ce qui fait apparaître une conséquence que le corpus n'avait pas tirée, à savoir qu'une infrastructure transportant une unité non convertible immédiatement devrait détenir des liquidités dans les monnaies de ses participants, donc constituer des réserves dans les monnaies mêmes que le dispositif entend concurrencer. Le troisième impose que tout lien entre infrastructures repose sur une base juridique solide dans toutes les juridictions concernées, ce qui reproduit à chaque connexion l'exigence que le corpus avait rencontrée pour l'établissement d'une seule infrastructure, et transforme une contrainte ponctuelle en contrainte multiplicative. Le chapitre conclut que ces trois exigences ne portent pas sur la conception de l'unité mais sur les conditions de sa circulation, et que le corpus n'a jamais décrit une seule opération de bout en bout."
concepts: [monnaie_comme_registre, hierarchie_monetaire, contrepartie_comptable, devise_cle, seuil_d_activation]
renvois: [L1.C24, L3.C05, L3.C09, L5.C02, L5.C09, L10.C01, L11.C02, L21.C01]
---

# Comment l'unité circulerait vraiment, et ce que chaque étape exige

::etat:: **L21.C01 a instruit les principes qui portent sur LE BILAN de l'infrastructure.** **Ce chapitre instruit ceux qui portent sur LA CIRCULATION** — trois de plus, portant le total à quatorze sur vingt-quatre.

## 1. Le règlement d'échange de valeur, et il frappe le point faible

::etat:: **Principe 12** [S1] : une infrastructure qui règle des échanges de valeur « should **eliminate principal risk** by ensuring that **the final settlement of one obligation occurs IF AND ONLY IF the final settlement of the linked obligation also occurs** ».

::hypothese:: **Le corpus enregistre que ce principe frappe exactement l'endroit où le dispositif est le plus vulnérable.** **L3.C09 a établi que l'unité NE RÈGLE PAS et que le dispositif S'AJOUTE au système existant** [S3]. **Toute opération utile suppose donc, à un moment, un échange entre l'unité et une monnaie qui règle.**

::hypothese:: **Et le principe 12 exige que cet échange soit CONDITIONNEL DANS LES DEUX SENS.** **Livrer l'unité sans recevoir la monnaie, ou l'inverse, expose au risque en principal — c'est-à-dire à la perte du montant entier, non d'une variation.** **Le lien doit donc être technique et simultané, pas contractuel et séquentiel.**

::hypothese:: **La conséquence est que le dispositif ne peut pas se contenter d'un rail qui transporte son unité : il lui faut un mécanisme de règlement CONTRE une autre valeur.** **C'est un objet distinct, et le corpus ne l'a jamais nommé.** **L5.C02 avait posé l'alternative du principe 9 ; le principe 12 ajoute que l'articulation entre les deux jambes doit être garantie, quelle que soit la branche retenue.**

## 2. La liquidité, et elle impose des réserves dans les monnaies concurrentes

::etat:: **Principe 7** [S1] : l'infrastructure doit maintenir « **sufficient liquid resources IN ALL RELEVANT CURRENCIES** » pour régler **le jour même**, et le cas échéant en cours de journée et sur plusieurs jours, **sous des scénarios de tension incluant la défaillance du participant générant la plus forte obligation de liquidité**.

::hypothese:: **Le corpus enregistre une conséquence qu'il n'avait pas tirée, et elle est ironique.** **Une infrastructure qui transporte une unité non immédiatement convertible devrait détenir des liquidités DANS LES MONNAIES DE SES PARTICIPANTS** pour honorer ses obligations en cas de tension. **Elle constituerait donc des réserves dans les monnaies mêmes que le dispositif entend concurrencer.**

::hypothese:: **Et l'exigence est cumulative, non alternative** : « in ALL relevant currencies ». **Plus le dispositif s'étend, plus la liste des monnaies pertinentes s'allonge, et plus les réserves à immobiliser croissent.** **L'extension du réseau augmente son coût de liquidité au lieu de le diluer** — l'inverse de ce qu'on attend d'une infrastructure.

::etat:: **Le corpus ne peut pas chiffrer ce besoin** : il ne tient ni volume, ni devise de référence, ni scénario de tension. **Il constate l'exigence et son sens.**

## 3. Les liens, et la contrainte devient multiplicative

::etat:: **Principe 20** [S1] : un lien entre infrastructures « should have **a well-founded legal basis, IN ALL RELEVANT JURISDICTIONS**, that supports its design and provides adequate protection to the FMIs », et les risques du lien doivent être identifiés et gérés avant l'établissement **et de façon continue**.

::hypothese:: **Le corpus enregistre que c'est la même exigence que le principe 1, reproduite à chaque connexion.** **L5.C02 avait établi que « la géographie de l'entrée est celle des droits, non celle des intérêts ».** **Le principe 20 ajoute que cette géographie se refait ENTIÈREMENT à chaque lien.**

::hypothese:: **Et cela change la nature du coût d'extension.** **Le principe 19 avait donné au corpus un mécanisme de croissance encourageant — la participation en paliers, où le premier entrant gagne une position d'intermédiaire.** **Le principe 20 en donne le revers : atteindre un participant par un LIEN entre infrastructures, plutôt que par un palier, exige une base juridique nouvelle dans toutes les juridictions du lien.** **Croître par paliers est bon marché ; croître par liens ne l'est pas.**

## 4. Ce que ces trois principes ne disent pas

::hypothese:: **Le corpus relève que ces exigences ne portent pas sur la conception de l'unité mais sur LES CONDITIONS DE SA CIRCULATION, et que cette distinction lui est favorable sur un point.** **Aucun des trois ne demande ce que l'unité vaut ni ce qui la gage.** **Ils demandent que le règlement soit conditionnel, que la liquidité existe, et que le lien soit fondé en droit.**

::hypothese:: **Ce sont des exigences d'exploitation, et elles s'achètent.** **À la différence du principe 15, qui exige des fonds propres que l'émetteur n'a pas, et du principe 9, qui pose une question de fait sur la contrepartie, ces trois-là se satisfont par de l'organisation et du capital de roulement.** **Le corpus doit les compter comme un COÛT, non comme un obstacle.**

::etat:: **Mais il n'a chiffré aucun de ces coûts, et L5.C02 avait déjà relevé qu'il « soutient qu'une infrastructure est une première marche sans savoir ce qu'elle coûte à gravir ».**

## 5. Portée

::etat:: **Trois principes de plus sont instruits — 7, 12 et 20 — portant le total à quatorze sur vingt-quatre.**

::hypothese:: **Le principe 12 frappe le point faible du dispositif.** Il exige que le règlement définitif d'une obligation intervienne **« si et seulement si »** celui de l'obligation liée intervient aussi. **Or L3.C09 a établi que l'unité NE RÈGLE PAS** : toute opération utile suppose un échange contre une monnaie qui règle, **et cet échange doit être conditionnel dans les deux sens, techniquement et simultanément.** **Le dispositif a besoin d'un mécanisme de règlement CONTRE une autre valeur, objet distinct qu'il n'a jamais nommé.**

::hypothese:: **Le principe 7 impose des ressources liquides « in ALL relevant currencies » pour régler le jour même.** **Conséquence non tirée jusqu'ici, et elle est ironique : une infrastructure transportant une unité non immédiatement convertible devrait constituer des réserves DANS LES MONNAIES MÊMES QUE LE DISPOSITIF ENTEND CONCURRENCER.** **Et l'exigence est cumulative : plus le réseau s'étend, plus les réserves à immobiliser croissent** — **l'extension augmente le coût de liquidité au lieu de le diluer.**

::hypothese:: **Le principe 20 rend la contrainte juridique multiplicative.** Tout lien exige **une base juridique solide dans TOUTES les juridictions concernées** — c'est le principe 1 reproduit à chaque connexion. **Le principe 19 rendait la croissance par PALIERS bon marché ; le principe 20 rend la croissance par LIENS coûteuse.**

::hypothese:: **Ces trois exigences portent sur les CONDITIONS DE CIRCULATION, non sur la conception de l'unité, et cela est favorable sur un point** : **aucune ne demande ce que l'unité vaut ni ce qui la gage.** **Ce sont des exigences d'exploitation, et elles s'achètent** — à la différence du principe 15, qui exige des fonds propres que l'émetteur n'a pas. **Le corpus doit les compter comme un COÛT, non comme un obstacle.**

::etat:: **Mais il n'a chiffré aucun de ces coûts**, et **il n'a jamais décrit une seule opération de bout en bout** — ni les bilans traversés, ni les écritures à chaque étape, ni le moment du caractère définitif, ni ce qui advient si une étape échoue. **La revue contradictoire du 2026-09-07 avait précisément demandé trois jeux d'écritures complets et séparés par entité.**
