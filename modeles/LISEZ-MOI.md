# `modeles/` — les pièces exécutables du corpus

Ce répertoire est **hors `corpus/`**, et c'est délibéré. Un script n'est pas un
chapitre : il ne doit ni compter dans le nombre de chapitres, ni passer sous le
contrôle de `corpus/convention.md`, ni recevoir un en-tête YAML. Ce qu'il produit
est lu par un chapitre, qui lui porte la convention.

Dépendance : aucune. Python 3, bibliothèque standard seule.

## Avertissement, et il est le plus important de ce fichier

**DEUX versions de cette matrice ont été écrites et réfutées le même jour, le
2026-09-09.** La première rendait un verdict unique par branche et **traitait une
insuffisance d'actifs comme une inexistence de passif** : c'est faux, une dette
reste une dette quand son débiteur ne peut pas l'honorer. La seconde écrivait
encore « reconnu comme passif » alors qu'elle vérifiait seulement que des
étiquettes étaient renseignées ; elle figeait un créancier unique pour un
instrument transférable ; et elle concluait que le collecteur d'un prélèvement
décidait de l'extinction. **Les tests passaient dans les deux cas — ils
établissaient que le programme appliquait ses règles, non que les règles étaient
fondées.**

**Un programme qui applique fidèlement une hypothèse fausse produit des résultats
faux avec une régularité parfaite.** C'est pourquoi la version courante sépare
ce qui relève des identités comptables, qui ne se discutent pas, de ce qui relève
d'une **lecture de la norme**, qui se discute et doit être soumise à un
contradicteur humain.

## `a35b_bilans.py` — matrice comptable de l'arbre A35b

Sept secteurs, quatorze branches, **six résultats séparés par branche, et ils
ne se commandent pas** :

| | |
|---|---|
| **R1a cohérence arithmétique** | équilibres, miroirs, somme des situations nettes, et l'identité *total des passifs représentatifs de l'unité, quel qu'en soit le porteur = total des avoirs chez les détenteurs*, contrôlée **à chaque étape**. **Vérifiée mécaniquement SELON LES ÉCRITURES POSÉES** — le programme ne juge pas la validité de la représentation qu'on lui donne, et des écritures fausses peuvent s'équilibrer parfaitement. |
| **R1b qualification comptable** | **PROPOSÉE, jamais établie.** Le programme n'écrit nulle part « reconnu comme passif » : il constate que des éléments sont renseignés, et suspend sa proposition quand l'un manque. |
| **R2 liquidité** | la demande maximale exigible à **chaque** étape. **Calculée, au pic** — et **par scénarios séparés** quand l'instrument est servi par d'autres participants. **Mais CONDITIONNELLE** : le facteur du plafond est juridiquement sourcé pour les droits de tirage spéciaux, mais **sa transposition à NEMO reste un choix de conception non arbitré**, et les autres repères ne sont calibrés sur rien. Changer un seul change le résultat. |
| **R3 solvabilité intertemporelle** | **non évaluable** : un cycle, sans intérêt ni horizon. |
| **R4a conception juridique** | **à produire.** Une institution prospective écrit son droit constitutif : droits, obligations, gouvernance, retrait, liquidation, immunités, différends. Aucun texte n'existe. |
| **R4b compatibilité juridique** | **à évaluer, non évaluée.** Elle devra pourtant être reconnue dans des ordres qui existent : traités, droits nationaux et régionaux, normes comptables. |

```bash
python modeles/a35b_bilans.py
```

**Un plafond de désignation est une CAPACITÉ d'acceptation, jamais une demande.** La règle dit ce qu'un participant peut être tenu d'accepter ; elle ne crée pas les devises qu'il faudrait remettre. La capacité effective est le minimum du plafond de règle et des devises encore détenues.

La formule est celle de l'**article XIX § 4(a)** des Statuts du Fonds, lu dans le texte le 2026-09-09 : c'est **l'excédent sur l'allocation** qui est borné à deux allocations, de sorte que le plafond total des avoirs vaut **trois** allocations.

```
limite_excedent   = 2 x allocation
plafond_total     = allocation + limite_excedent
capacite_restante = max(0, plafond_total - avoirs)
```

Une version antérieure écrivait `2 x allocation - avoirs` et sous-estimait la capacité d'une allocation entière. **L'erreur était masquée par le scénario**, la ressource étant nulle de toute façon : `capacite_designation` est donc une fonction pure, éprouvée hors de tout scénario. Le § 4(b) ajoute qu'un participant **peut** fournir au-delà — la limite borne l'obligation, jamais la possibilité.

**Une branche peut être comptablement cohérente et illiquide.** C'est le cas
normal d'un émetteur qui promet plus qu'il ne détient, et ce n'est pas une
anomalie d'écriture : c'est un risque, et le programme le nomme au lieu de
rejeter la branche.

Le programme imprime la **chronologie des bilans après chaque opération**. Ce
n'est pas un confort d'affichage : une obligation stipulée « à tout moment » ne
se contrôle pas sur le bilan final, et c'est exactement la faute que la version 1
commettait.

**Aucun comportement économique n'y est modélisé** — ni prix, ni salaire, ni
profit, ni élasticité, ni capacité productive, ni transfert international, ni
intérêt. En particulier, **la matrice n'établit aucune incidence économique** :
elle impose par paramètre qui est redevable, puis retrouve ce qu'elle a imposé.

`A36` est respecté : le **démurrage** (assiette : l'encaisse détenue) et le
**prélèvement transactionnel** (assiette : la transaction) sont deux mécanismes,
avec deux redevables et deux règlements. Et le **collecteur du prélèvement est un
paramètre**, parce que A36 n'a pas arrêté l'architecture juridique. Mais **le
collecteur ne décide que de la PREMIÈRE DESTINATION** des unités perçues : à
circuit ultérieur inchangé, son choix modifie l'encours immédiatement après
perception, et **l'encours final dépend ensuite de l'emploi des unités
collectées** — trois sous-branches l'établissent.

Le résultat est lu par **L19.C10**, et le raisonnement vit dans
`protocoles/passe-2.md`.

## `test_a35b.py` — vérification du programme, et de lui seul

```bash
python modeles/test_a35b.py
```

Six sections, et la troisième porte un avertissement en toutes lettres :

- **A. identités comptables** — sabotées une par une ; ce ne sont pas des
  hypothèses, ce sont des identités.
- **B. créancier dynamique** — vérifie que la qualité de créancier MIGRE avec
  l'instrument, et que le passif égale la somme des encours de tous les
  détenteurs.
- **C. qualification** — vérifie que le programme SUSPEND sa proposition quand un
  élément manque. **Il ne valide pas la lecture de la norme.**
- **D. liquidité** — vérifie que le pic est contrôlé, que le bilan final seul
  aurait conclu à tort à la couverture, et que les trois scénarios sont publiés
  séparément.
- **E. R4** — vérifie que la conception à produire et la compatibilité à évaluer
  restent deux listes disjointes.
- **F. A36** — vérifie que les deux mécanismes restent distincts, et que
  l'EMPLOI des unités perçues, non le collecteur seul, décide de l'encours.

## Comment ajouter une branche

**Une branche qui n'est pas écrite n'est pas rejetée : elle est absente.** Le
résultat de L19.C10 est conditionnel à l'énumération, et un contradicteur qui
produirait une quinzième branche déplacerait ses conclusions.

**Le jalon suivant est humain** : `protocoles/revue-comptable-a35b.md` pose huit
questions, dont sept à un comptable national ou à un spécialiste des bilans de
banque centrale, et une — la sixième — à un juriste en droit monétaire
international. **Aucun modèle macroéconomique avant cette revue.**

Pour l'écrire : ajouter une `Branche(...)` à la liste `BRANCHES`, en renseignant
ses axes — `circulation`, `inscription`, `allocation`, `beneficiaire`, plus
`souscription`, `collecteur`, `emploi_collecte` et `contrib_detenteur` s'il y a
lieu — et sa fiche : l'obligation, le secteur chez qui le passif est inscrit, le
droit attaché, qui sert l'obligation, l'exigibilité, l'extinction, le porteur du
risque, et les exigences juridiques que la branche appellerait. **Le créancier
n'est pas un champ : il est DÉRIVÉ des écritures, et il migre avec
l'instrument.** Les écritures s'en déduisent.


## `nemo_soldes.py` — compensation symétrique des déséquilibres courants

Trois pays, huit périodes, quatre scénarios. Une union de compensation :
comptes des banques centrales auprès de l'institution, corridor toléré des deux
côtés, obligations graduées, facilité temporaire de liquidité, parités
administrées.

```bash
python modeles/nemo_soldes.py
python modeles/test_nemo_soldes.py
```

**VERSION 2, après cinq corrections de l'auteur** : horizon au-delà de toutes
les maturités, identité stock-flux vérifiée par pays et par période, registres
publiés séparément au lieu d'un « effort » agrégé, **échanges élastiques à la
parité** — sans quoi conclure qu'une charge n'arrête pas une accumulation est
tautologique — et **un plafond qui est une PROCÉDURE, pas un nombre**.

**Deux guichets** : facilité remboursable pour un choc temporaire, allocation
solidaire **non remboursable** pour un besoin essentiel structurel. Le programme
compare les deux, et les trois procédures de plafond.

**La symétrie est un PARAMÈTRE, jamais une hypothèse.** Chaque scénario est joué
sous obligation excédentaire contraignante puis délibérative, parce que le
corpus a établi sur pièces que c'est exactement la disposition qui saute [F6].

**Aucun seuil n'est calibré**, et le drapeau `SEUILS_CALIBRES` doit rester à
`False` tant qu'une source ne fonde pas chaque seuil.

**A43 (3) SCINDÉ LE 2026-09-16 — parités administrées contre strictement fixes.**
`comparer_parites` joue chaque scénario deux fois, révision des parités active
puis coupée ; `jouer_a_parites` rend toujours le pas déclaré. **Dans ce modèle,
la parité est le seul canal qui agit sur les volumes : le sens de l'effet est
presque acquis d'avance.** Ce que la comparaison apporte est l'ordre de grandeur
de ce que charges, recyclage et guichets doivent porter à sa place. La section G
du test vérifie que chaque conclusion imprimée est celle que la sortie montre.

**RÈGLE DE RÉVISION DE L'AUTEUR, 2026-09-16 — condition (1) d'A43 (3b).**
`jouer(..., regle=...)` accepte une règle de révision ; laissée vide, le modèle
suit son chemin d'origine, et la section H du test vérifie qu'une règle fournie ne
change rien d'autre. `regle_de_revision_auteur` : glissement de 2,5 % par période
hors corridor, dans les deux sens, et butée cumulée de 30 % au-delà de laquelle la
révision s'arrête. Les trois candidates écartées restent versées pour que le choix
se rejoue. **Le modèle départage mal les règles et très bien les conditions.**

**OBLIGATIONS DES EXCÉDENTAIRES, 2026-09-17 — condition (2) d'A43 (3b).**
`jouer` décompose les obligations de l'excédentaire (`obligations_creancier` :
charge, plafond, parité), retarde leur activation (`delai_creancier`) et peut
supprimer la charge sur les débiteurs (`charge_debiteur`) ; par défaut, rien ne
change. `OPTIONS_AUTEUR` porte les choix de l'auteur : obligations automatiques
par réévaluation et recyclage, aucune charge. `comparer_obligations` publie leur
effet ET leur prix — l'institution ne perçoit plus rien —, vérifiés par la section I.

**PERTE DURABLE D'UN DÉBOUCHÉ, 2026-09-17 — condition (5) d'A43 (3b).**
Le contrôle C8 signale désormais une masse monétaire négative : il manquait, et une
conclusion publiée sur S4 en dépendait. `recyclage_pret` fait du recyclage un prêt,
avec remboursement et annulation ; `procedure_structurelle` ouvre une procédure
sur perte mesurée de débouché — restriction, reconversion, transfert, revue.
`OPTIONS_AUTEUR_COMPLETES` porte les choix de l'auteur, et `comparer_procedure_structurelle`
publie leur effet, sans supposer la réussite de la reconversion, et leur prix.

**QUI FINANCE LES GUICHETS, 2026-09-17 — condition (4) d'A43 (3b).**
`jouer` tient un registre du DÉCOUVERT : ce que l'institution verse sans
remboursement, et ce qu'un flux `reflux_apurement` en retire. Il ne change aucune
trajectoire, et la section K du test le vérifie. Le reflux n'est pas modélisé :
`comparer_financement_guichets` exprime son flux en multiples du besoin moyen des
guichets, que le modèle calcule (`MULTIPLES_REFLUX`), publie ce que le reflux seul
laisserait manquer au moment des chocs, et montre où aboutit l'émission en S2 —
chez l'exportateur des biens essentiels. **Le registre n'est pas le solde de
l'institution : il compte ce que le reflux aurait à retirer, il ne le retire pas.**

**L'ACCUMULATION DE L'EXPORTATEUR, 2026-09-17 — D77 à D79.**
`jouer` porte deux instruments, inactifs par défaut : `demurrage_soldes`, démurrage sur les
soldes positifs de compensation, et `reliquat_plafond`, « conversion » ou « placement » de ce
qui reste au-delà du plafond après recyclage. `OPTIONS_AUTEUR_COMPLETES` porte la conversion
(D77) ; `OPTIONS_AVANT_D77` reproduit la configuration des sections antérieures, dont les
chiffres publiés restent exacts. `comparer_accumulation_exportateur` publie les remèdes
mesurés, le démurrage écarté (D78), la baisse de dépendance SUPPOSÉE qui motive D79, et le
cas d'un retournement, vérifiés par la section L du test.

**LA DÉPENDANCE DURABLE À UNE IMPORTATION ESSENTIELLE, 2026-09-17 — D79 à D82.**
`jouer` porte `procedure_importateur`, absente par défaut : ouverture sur la persistance
d'un déficit essentiel et le surcoût mesuré de la facture essentielle, financement non
remboursable, baisse des importations essentielles SUPPOSÉE (`part`), revue par clôture,
prolongation ou jalons. `PROCEDURE_IMPORTATEUR_AUTEUR` porte D80 à D82 dans
`OPTIONS_AUTEUR_COMPLETES` ; `OPTIONS_AVANT_D77` et `OPTIONS_AVANT_D80` figent les
configurations des sections antérieures, dont la sortie reste identique.
`comparer_procedure_importateur` publie l'ouverture, l'intensité du choc, le financement, la
revue, la baisse nécessaire et la configuration de l'auteur, vérifiés par la section M.


## `nemo_emission.py` — la règle d'émission et ses sept cas limites

**Le cœur de NEMO IMS : qui crée combien de monnaie, pour quoi, et avec quel
pouvoir d'arrêt.** Trois décisions séparées — **veto physique** qui refuse sans
jamais autoriser, **priorité** qui appartient au politique, **calibrage** qui
échelonne sans jamais refuser au fond — et **trois arrêts dont un seul est
inconditionnel**.

**VERSION 2, après quatre corrections de l'auteur.** Deux conclusions de la
version 1 étaient fausses, et fausses dans le même sens — celui de
l'impuissance : « le cas 7 ne se répare pas » et « une émission sans dette n'a
aucune reprise ». **Un corpus qui cherche les échecs peut aussi en inventer.**

**Cinq fonctions séparées** — mesure scientifique, qualification, priorité
démocratique, calibrage, contrôle et recours — **neuf états**, et trois
contrôles. **S1** voit le cumul des pouvoirs sur l'organigramme ; **S2** voit un
passage exercé par le mauvais ; **S3** voit une institution contrôler, sur un
dossier, un acte qu'elle a elle-même accompli — ce que S1 ne peut pas voir.

**Les sept cas sont rejoués avec leur mécanisme, et les nombres sont ceux de la
sortie.** Le veto projet par projet s'avère **trop permissif** — trois usages
admis isolément demandent 105 de lithium pour 100. Le versement par tranches
sauve **82 %** d'une erreur détectée tôt contre **30 %** détectée tard.

**Sur la capture, le résultat a été corrigé une fois de plus.** Le programme
donnait d'abord au recours la valeur vraie de la simulation, ce qui lui prêtait
une robustesse imaginaire. **Devenu un instrument avec son biais et son propre
risque de capture, il tombe à deux captures** — un organisme, puis l'instrument
saisi — **contre trois pour la simple médiane et cinq pour la règle prudente,
qui refuse en revanche trois projets légitimes sur cinq.** Pluraliser le recours
le remonte à trois. **Aucune règle n'est gratuitement supérieure.**

**Ce qui reste ouvert est dit à chaque cas** : la collusion unanime ne diverge
pas, le plafond d'urgence est un nombre politique, et aucun critère neutre ne
départage deux besoins essentiels.

```bash
python modeles/nemo_emission.py
python modeles/test_nemo_emission.py
```


## `nemo_a47.py` — décider sous incertitude

**La doctrine de précaution proportionnée, en neuf points, mise à l'épreuve sur
six dossiers fictifs.** Elle n'arrête aucun seuil : elle répartit **la charge de
la preuve** et fixe la procédure d'établissement des seuils.

**Version 2, validée par l'auteur.** La grille des seuils est **fixée d'avance
par l'autorité démocratique après expertise pluraliste**, et la qualification
**l'applique en se motivant** — ce qui ferme le premier trou de la version 1 : le
choix d'horizon devient une décision publique et attaquable au lieu d'un
arbitrage rendu dossier par dossier.

**Ce qui tient et se chiffre.** Selon que le seuil est publié d'avance ou choisi
après lecture des dossiers, **0, 2 ou 3 dossiers** sont mis à la charge du
porteur — les trois valeurs étant dans la même plage plausible.

**Deux « restes » que ce programme publiait étaient des lectures fautives de la
règle, et l'auteur les a redressés.** La **zone intermédiaire** était prévue —
charge partagée, tranches, surveillance, capacité d'arrêt — et « grave mais
réversible » comme « irréversible mais peu plausible » y appartiennent ; le
programme les rendait sans charge. Et **l'incertitude agit sur la procédure
d'instruction, non sur le régime** : le programme regardait le régime.

**Deux propriétés sont désormais vérifiées.** Une grille complète attribue un
régime à **chaque** dossier. Et trois dossiers de risque identique, de
connaissances différentes, reçoivent **un régime et trois procédures** :
acquisition de données, marge de précaution, application directe.

**Trois variables sont séparées** — probabilité du dommage, confiance dans
l'estimation, réductibilité et délai — parce qu'un seul nombre entre 0 et 1 ne
peut pas porter les trois.

**Reste une seule pièce ouverte** : les seuils sectoriels — horizon de
réversibilité, seuil de confiance, délai utile — à fixer par domaine selon la
procédure d'A47.

```bash
python modeles/nemo_a47.py
python modeles/test_nemo_a47.py
```
