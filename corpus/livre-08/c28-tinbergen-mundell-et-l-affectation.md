---
chapitre: L8.C28
titre: "Tinbergen, Mundell et l'affectation des instruments"
livre: 8
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-06
autorite: preparatoire
citable: false
regime: descriptif
sources_primaires:
  - ref: S1
    nature: theorie
    reference: "J. Tinbergen, On the Theory of Economic Policy, North-Holland, Amsterdam, 1952 — OUVERT INTÉGRALEMENT le 2026-09-06. Retenu ici : la RÈGLE DU COMPTE et ses trois cas (ch. IV) ; les DIRECTIVES, équations qui « indicate how the political parameters have to be varied in relation to the changing data » ; les CONDITIONS du ch. II, grandeurs « not in themselves elements of well-being but rather technical expressions of a “sound policy” » ; les BOUNDARY CONDITIONS du ch. V, qui « represent all the protests of reality against the supposed linearity » et « only become “active” [...] if their fulfilment is threatened » ; la CLASSIFICATION EN CINQ GROUPES (ch. IX) et l'aveu qui l'accompagne — « empirical research into each of the points (b) — (e) is still almost completely lacking »"
    date_verification: 2026-09-06
  - ref: S2
    nature: theorie
    reference: "R. Mundell, « Capital Mobility and Stabilization Policy under Fixed and Flexible Exchange Rates », Canadian Journal of Economics and Political Science, 29(4), novembre 1963, p. 475-485 — OUVERT INTÉGRALEMENT le 2026-09-05. Retenu ici : sous parité fixe et mobilité parfaite des capitaux, « the central bank has no power over the money supply either (except in transitory positions of disequilibrium) » ; « the budget deficit is entirely at the expense of reserves » ; et la portée du raisonnement, « the world is still a closed economy »"
    date_verification: 2026-09-05
verifications_en_attente:
  # ── Méthode ────────────────────────────────────────────────────────────────
  # CHAPITRE À SOURCES OUVERTES. Les deux textes qui le portent ont été lus
  # intégralement et dépouillés dans le Livre 11 : c'est pourquoi il est écrit
  # en premier de la partie, avant les chapitres qui exigeraient des
  # acquisitions.
  #
  # PASSE 1 ASSUMÉE. Le chapitre ne prétend pas rendre compte de la synthèse
  # néoclassique ni de la macroéconomie de l'après-guerre : il traite les deux
  # résultats que le corpus emploie, dit ce qu'ils apportent au dispositif, ce
  # qu'ils lui opposent, et ce que le dispositif cherche chez eux sans l'y
  # trouver. Les passes suivantes élargiront.
  #
  - "MUNDELL 1962 — « The Appropriate Use of Monetary and Fiscal Policy for
     Internal and External Stability », IMF Staff Papers 9(1) — N'EST PAS
     OUVERT, et ne figure donc pas au bloc des sources. Le § 4 traite le
     principe d'affectation, dont le corpus ne tient que la formulation
     courante. **Aucune citation de l'auteur n'y figure et le § le dit** ;
     porté en acquisition avec Fleming 1962, dont l'absence est signalée depuis
     L11.C04."
  - "LA RÉSERVE DE TINBERGEN SUR L'AFFECTATION UN À UN N'A PAS ÉTÉ RECOUPÉE.
     Le § 4 s'appuie sur la mention d'« a very special structure » ; **le corpus
     ne l'a pas confrontée à la littérature ultérieure sur l'assignment
     problem**, qui a discuté cette condition pendant vingt ans."
  - "LE STATUT DISCIPLINAIRE ANNONCÉ EST UN JUGEMENT DU CORPUS. Le § 6 classe
     la règle du compte en « acquis » et l'affectation un à un en « opérant ».
     **Aucune enquête bibliométrique ne l'appuie** : c'est une appréciation de
     lecture, contestable, et elle est donnée comme telle."
resume: "Ce chapitre traite les deux résultats de théorie de la politique économique sur lesquels tout le Livre 11 est construit, et il est écrit en premier de sa partie parce que ses deux sources ont été lues intégralement. Il établit ce que Tinbergen apporte au dispositif : une règle de comptage qui transforme une intuition en contrainte vérifiable, une catégorie pour les grandeurs qui ne sont pas des objectifs mais des conditions techniques, un statut pour les inégalités qui ne mordent que sous tension, et surtout une forme pour ce qu'un barème doit être — non une table de nombres mais une directive, fonction des données observées. Il établit ce que Mundell lui oppose : sous parité fixe et capitaux mobiles, la banque centrale nationale perd le contrôle de la quantité de monnaie, résultat que le dispositif affirme neutraliser sans mécanisme. Il énonce ce que le dispositif cherche chez ces deux auteurs et n'y trouve pas — une méthode pour compter des objectifs qui ne sont pas des grandeurs monétaires, et un traitement du cas où l'instrument et l'objectif appartiennent à des ordres différents. Il montre que la question des limites physiques est chez eux compatible mais silencieuse : rien n'interdit d'y faire entrer une contrainte biophysique, rien ne l'appelle non plus. Il relève enfin que Tinbergen classe lui-même les propositions de changement de structure monétaire dans une catégorie où il déclare la connaissance empirique presque absente, ce qui vaut au dispositif une qualification et non une dispense."
concepts: [affectation_des_instruments, regle_contre_discretion, referentiel_de_change, bareme]
renvois: [L1.C21, L1.C26, L8.C01, L11.C03, L11.C04, L11.C12, L11.C15, L11.C17]
---

# Tinbergen, Mundell et l'affectation des instruments

::etat:: Ce chapitre traite les deux résultats sur lesquels le Livre 11 est construit. Il est écrit en premier de sa partie **parce que ses deux sources ont été lues intégralement** — ce qui n'est le cas que de cinq chapitres du livre.

## 1. La controverse : combien d'instruments pour combien d'objectifs

::etat:: **La question que ces travaux tranchent est celle de la faisabilité d'une politique, non de son contenu.** Elle se pose dès qu'une autorité poursuit plusieurs buts avec un nombre fini de leviers, et elle avait été traitée jusque-là par le jugement politique. **Tinbergen la rend arithmétique.**

::etat:: La règle est une équivalence entre systèmes d'équations, et Tinbergen en distingue **trois cas** [S1]. Autant d'instruments que d'objectifs : le problème a une solution, et elle est unique. Plus d'instruments que d'objectifs : le problème est sous-déterminé, il reste des degrés de liberté à employer. **Moins d'instruments que d'objectifs : il n'y a pas de solution qui atteigne tout, et un arbitrage se fait — écrit ou non.**

::hypothese:: **Le troisième cas est celui qui compte, et sa force tient à ce qu'il n'est pas normatif.** Il ne dit pas quel objectif sacrifier : il dit qu'un sacrifice a lieu. **Une politique en sous-nombre d'instruments n'échoue pas bruyamment — elle atteint certains buts et pas d'autres, sans que personne ait décidé lesquels.**

## 2. POUR — quatre apports au dispositif, et le quatrième est le plus grand

::hypothese:: **La règle du compte.** L11.C03 l'applique au dispositif et trouve six objectifs pour trois instruments dans la même main. Le résultat n'est pas une opinion sur le dispositif : c'est un décompte, et il est contestable ligne par ligne — ce qui est exactement ce que le corpus recherche.

::hypothese:: **La catégorie des conditions.** Tinbergen range à part les grandeurs introduites « in the form of **conditions** [...] since they are **not in themselves elements of well-being but rather technical expressions of a “sound policy”** », son exemple étant le solde de la balance des paiements [S1]. **Cela donne un statut au bouclage volumétrique du dispositif** — que le reflux couvre l'émission n'est pas un élément du bien-être, c'est une condition de solidité. L11.C03 s'en sert pour reclasser un objectif que le corpus comptait à tort comme les autres.

::hypothese:: **Les conditions-limites.** Elles « represent all the protests of reality against the supposed linearity », elles comptent comme des objectifs, et surtout **elles ne mordent pas toujours** : « In principle, boundary conditions are **inequalities** [...] **As long as they are satisfied they need not to be introduced** [...] **They only become “active” [...] if their fulfilment is threatened** » [S1]. **Le compte d'une politique n'est donc pas un nombre mais une fonction de l'état du monde** — et L11.C03 en tire que le compte du dispositif est au plus mauvais quand il est le plus sollicité.

::hypothese:: **Et la forme d'un barème, qui est le plus grand des quatre apports.** Une fois les cibles fixées, les valeurs des instruments restent fonctions des données, qui changent : « **In this form we shall call these equations “directives for economic policy” since they indicate how the political parameters have to be varied in relation to the changing data** » [S1]. **Un barème réglé n'est donc pas une table de taux : c'est une directive**, de forme *taux = f(données observées)*. L11.C12 en fait la réponse commune aux trois barèmes du dispositif, et L11.C17 vérifie qu'elle passe l'épreuve des trois.

## 3. CONTRE — Mundell, et le sommet que le dispositif ne peut pas garder

::etat:: **Mundell 1963 oppose au dispositif le résultat le plus dur du dossier, et il l'oppose sur une phrase que le livre écrit sans mécanisme.** Le livre affirme que le dispositif « neutralise les dilemmes exposés par le triangle d'incompatibilité de Mundell » tout en conservant l'autonomie monétaire nationale et la libre circulation des capitaux (L1.C26, promesse bloquante P49).

::etat:: **Le texte dit l'inverse, et sans réserve.** Sous parité fixe et mobilité parfaite des capitaux, « **the central bank has no power over the money supply either (except in transitory positions of disequilibrium)** », et la tentative de stériliser les flux « will ultimately lead to the breakdown of the fixed exchange system » [S2]. Sur le budget : « **the budget deficit is entirely at the expense of reserves** ».

::hypothese:: **Le dispositif obtient bien les changes fixes, et mieux qu'un ancrage classique** — aucune parité n'y est attaquable faute de marché où l'attaquer (L1.C26). **Ce qu'il ne peut pas obtenir, c'est les trois sommets.** L11.C04 a tiré du texte deux choses que le corpus n'avait pas : une **seconde fuite** par le compte financier, et le fait que la contrainte est fonction de ce qui demeure **hors** du système — elle s'annule à couverture complète, se restreint par le contrôle des capitaux, et **un barème modulé nationalement la recrée**.

::hypothese:: **Ce dernier point retourne Mundell en faveur du dispositif sur un point précis**, et le corpus le porte au même titre : il fournit un argument structurel pour l'uniformité des barèmes, donc pour la branche centralisée de l'arbitrage A4. **Le même auteur soutient une objection bloquante et une exigence de conception.**

## 4. Le principe d'affectation, et la réserve que Tinbergen y met

::etat:: **Le corpus doit ici marquer une limite de sa propre documentation.** Le principe d'affectation — associer chaque instrument à l'objectif sur lequel il a l'avantage relatif — est attribué à **Mundell 1962, que le corpus n'a pas ouvert** — raison pour laquelle ce texte ne figure pas au bloc des sources, la convention exigeant une vérification datée. Aucun mot de l'auteur n'est cité dans ce paragraphe, et rien n'en doit sortir avant lecture.

::hypothese:: **Ce que le corpus tient de première main, en revanche, c'est la réserve de Tinbergen.** L'affectation un à un — un instrument, un objectif — ne vaut que sous « a very special structure » du système [S1]. **Elle n'est donc pas la forme générale de la solution, mais un cas particulier**, ce que la présentation courante omet souvent.

::hypothese:: **Cela porte sur le dispositif de façon directe.** L11.C17 a établi que ses barèmes sont interdépendants — la structure de la valorisation ne se règle qu'avec le taux de reflux, l'égalité de bouclage les liant — et Tinbergen le dit d'avance : « the values of the instrument variables are dependent, generally speaking, **on all the targets set and cannot be considered in isolation** » [S1]. **Un dispositif dont on règle les tables séparément suppose la structure très spéciale, sans l'avoir montrée.**

## 5. MANQUEMENT — ce que le dispositif cherche là et n'y trouve pas

::hypothese:: **Deux manques, et ils sont du même ordre.**

::hypothese:: **Le premier : compter des objectifs qui ne sont pas des grandeurs monétaires.** La règle suppose des cibles exprimées dans un même espace de variables, reliées par des équations estimées. Le dispositif poursuit un état biosphérique et un état social ; L11.C14 a établi que la moitié des familles de son tableau de bord sont des objectifs et non des données. **Rien chez Tinbergen ne dit comment une cible écologique entre dans le décompte**, et le corpus a fait entrer les siennes par assimilation, faute de mieux.

::hypothese:: **Le second : le cas où l'instrument et l'objectif appartiennent à des ordres différents.** Un taux de reflux est un prix ; l'abondance des produits essentiels est une quantité physique. La règle les compte comme deux objectifs sans dire que le lien entre eux passe par des capacités matérielles que la monnaie ne crée pas. **C'est la promesse P35, et elle n'a pas de traitement ici.**

## 6. LIMITES et STATUT

::hypothese:: **Sur la limite physique, ces travaux sont compatibles mais silencieux.** Rien n'interdit d'introduire une contrainte biophysique parmi les conditions-limites — le vocabulaire de Tinbergen l'accueille sans se défaire, et L11.C03 l'a fait pour douze d'entre elles. **Mais rien ne l'appelle non plus** : les exemples de l'auteur sont des bornes d'évasion fiscale, de proportionnalité des sacrifices, de situations financières. **La limite peut y entrer ; elle n'y est pas.**

::hypothese:: **Statut disciplinaire, et c'est un jugement du corpus, non une enquête.** La règle du compte est **acquise** : enseignée partout, non contestée dans son principe. L'affectation un à un est **opérante** : elle sert à décider, mais elle est datée, et Tinbergen lui-même en borne la validité. Le résultat de Mundell est **acquis** dans son mécanisme et **disputé** dans sa portée contemporaine, la littérature ultérieure ayant soutenu que l'autonomie monétaire est déjà perdue sous changes flottants — ce que le corpus a versé au dossier sans l'ouvrir.

::hypothese:: **Et Tinbergen classe lui-même le dispositif.** Il range les propositions de **changement de la structure du système monétaire** dans une catégorie propre, la classe (d), et écrit que « the scientific treatment of problems of qualitative policy **meets with great difficulties** » pour ces classes, parce que « our empirical quantitative knowledge of human behaviour under different structural conditions is **so restricted** » — concluant que « **empirical research into each of the points (b) — (e) is still almost completely lacking** » [S1].

## 7. Portée

::etat:: **Le dispositif tient sa colonne vertébrale théorique de deux textes, et ils ne disent pas la même chose de lui.** Tinbergen lui donne une règle de comptage, une catégorie pour ses conditions, un statut pour ses bornes, et **la forme même de ce qu'un barème doit être**. Mundell lui oppose la perte de l'autonomie monétaire sous parité fixe — et lui fournit dans le même mouvement l'argument qui impose l'uniformité de ses barèmes.

::hypothese:: **Ce que le dispositif cherche et ne trouve pas est du même ordre dans les deux cas** : une méthode pour faire entrer dans le décompte des objectifs qui ne sont pas des grandeurs monétaires, et un traitement du cas où l'instrument est un prix et l'objectif une quantité physique.

::hypothese:: **La qualification que Tinbergen apporte au dispositif n'est ni une absolution ni une condamnation.** Le cadre du comptage est construit pour des politiques quantitatives à structure donnée ; le dispositif est un changement de structure, classe (d). **Le compte garde donc sa valeur de constat interne et perd sa valeur de verdict** — mais Tinbergen appelle le manque empirique « an urgent need », non une dispense, **et un dispositif qui invoquerait la classe (d) pour se soustraire au chiffrage invoquerait à son profit un aveu d'ignorance.**
