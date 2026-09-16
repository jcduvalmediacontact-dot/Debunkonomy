# Architecture de reprise de L1.C15 — « L'essentiel insolvable »

Date : 2026-09-13  
État : proposition d'architecture, soumise à validation de l'auteur  
Chapitre examiné : `L1.C15`, SHA-256
`BC83F150E6A11FB2800C60A41867049E68DA8902F59DEC82AADF3747BC83945D`

Le chapitre n'est pas modifié par cette passe. La présente note confronte son
texte à la cartographie validée du Livre 1, au protocole
`validation-essentiel-insolvable.md`, aux décisions déjà inscrites dans le
registre et aux corrections acquises par L1.C07, L1.C08 et L1.C31.

## 1. Verdict d'ensemble

La forme logique du concept est correcte :

```text
Solvable             = M ∧ C ∧ T ∧ A
Essentiel insolvable = E ∧ (¬M ∨ ¬C ∨ ¬T ∨ ¬A)
```

Une seule condition financière qui échoue suffit. Le chapitre actuel ne commet
pas l'erreur inverse dans cette formule.

En revanche, il transforme à plusieurs endroits une **catégorie analytique
prospective** en résultat général déjà établi. Il ne définit pas `E`, le
caractère essentiel, indépendamment de NEMO ; il ne démontre ni la fréquence
des cas, ni leur volume, ni leur déficit de financement. Il confond aussi le
filtre proposé par le corpus avec le sens bancaire ou juridique ordinaire de la
solvabilité.

La thèse et le titre peuvent être conservés, mais le chapitre demande une
réécriture substantielle de sa portée. Il ne peut pas passer directement à
l'audit factuel dans son état actuel.

## 2. Quatre objets aujourd'hui confondus

Le texte réécrit doit séparer quatre propositions.

1. **Définition.** Le corpus propose d'appeler « essentiel insolvable » une
   activité ou un besoin qui satisfait un critère indépendant d'essentialité
   et échoue à au moins une des quatre conditions financières.
2. **Applicabilité.** Des tiers doivent pouvoir appliquer cette définition aux
   mêmes cas avec une concordance suffisante. Ce résultat n'existe pas encore.
3. **Ampleur.** La fréquence, les volumes et le déficit de financement doivent
   être mesurés après stabilisation de la définition. Ils sont inconnus.
4. **Portée pour NEMO.** Même un ensemble réel et important ne démontre pas
   l'apport propre de NEMO. Il faut encore comparer NEMO aux portefeuilles
   concurrents selon L1.C31 et F10.

Le chapitre peut être `verifie` en exposant honnêtement ces quatre niveaux. Il
ne peut pas présenter les trois derniers comme acquis.

## 3. Écarts conceptuels à corriger

### 3.1 Le critère `E` manque

Le texte décrit successivement comme essentiels le maintien des conditions de
la vie, le soin donné, la transmission, la recherche fondamentale et la
préservation des communs. Aucun critère commun n'est défini. Le protocole
d'opérationnalisation dit pourtant que la non-circularité n'est tenue qu'à
moitié : les quatre conditions financières sont indépendantes de NEMO, mais le
périmètre `E` ne l'est pas encore.

La réécriture doit exposer cette lacune au lieu de la remplir implicitement.
Tant que `E` n'est pas arrêté, les exemples sont des cas candidats, jamais une
classe démontrée.

### 3.2 « Solvabilité » est employé dans deux sens

Le § 1 présente les quatre conditions comme le « vocabulaire bancaire ». C'est
trop fort. Une banque peut prêter sur la base des revenus généraux de
l'emprunteur, d'une garantie, d'un collatéral, d'un garant public ou d'autres
éléments que la recette propre de l'activité. Le corpus construit ici un test
de **finançabilité autonome par les flux attendus de l'activité** ; il ne donne
pas la définition exhaustive de la solvabilité d'une personne ou d'un État.

La réécriture doit donc distinguer :

- la solvabilité juridique ou comptable du débiteur ;
- la bancabilité d'un projet dans une architecture donnée ;
- le filtre analytique à quatre conditions proposé par le corpus.

Le terme « essentiel insolvable » peut rester le nom du concept, à condition
que cette convention soit déclarée.

### 3.3 La dette souveraine est décrite trop mécaniquement

Le chapitre affirme qu'une banque qui souscrit une obligation souveraine crée
un dépôt « exactement comme pour un crédit ordinaire ». Le résultat dépend du
circuit de règlement, du vendeur et de l'institution qui tient son compte. La
formule ne peut pas être universalisée depuis L1.C07.

Il affirme ensuite que la capacité de l'État est gagée sur une base d'activité
que le crédit privé aurait préalablement jugée solvable. Cette chaîne est une
hypothèse forte. Les capacités fiscales, la monnaie d'émission, le régime de
change, la banque centrale, le droit applicable, l'inflation, la contrainte
extérieure et la demande de titres interviennent aussi.

Le passage doit être ramené à une proposition plus étroite : un financement
public peut contourner la bancabilité du projet, mais il déplace la charge et
les contraintes vers une institution publique. La nature et l'intensité de ces
contraintes varient selon le régime monétaire et juridique.

Les ratios français de 2023 et 2025 ne démontrent pas ce mécanisme. Ils doivent
recevoir une source primaire et une fonction précise, ou être retirés.

### 3.4 L'universalité alléguée n'est pas démontrée

Les formulations suivantes dépassent le dossier :

- « il n'existe aucun canal de création monétaire » sans promesse de
  remboursement gagée sur une activité solvable ;
- « tout ce qui relève » de l'entretien, du soin, de la transmission et de la
  recherche fondamentale échoue au filtre ;
- les activités concernées échouent « presque toujours » sur plusieurs
  conditions ;
- les six voies existantes se heurtent toutes « au même filtre ».

Ces phrases doivent devenir des hypothèses soumises à l'épreuve, ou être
retirées. L'impôt, la subvention, le don, le bénévolat et la gouvernance
collective ne réfutent pas le concept, mais ils ne sont pas non plus de simples
reproductions du crédit. Ils compensent ou contournent certaines conditions au
prix de contraintes qui leur sont propres.

### 3.5 La section thermodynamique ne fonde pas le concept

La section 3 peut rester comme hypothèse secondaire sur la sélection des
activités, mais elle ne doit plus porter la définition de l'essentiel
insolvable.

Trois phrases doivent être retirées ou profondément réduites : « transformer,
c'est dégrader » sans frontière ni grandeur ; « l'entretien ne liquide rien » ;
« un effondrement évité ne produit aucune recette et n'apparaît dans aucun
compte ». L'entretien consomme lui-même des ressources, certains dommages
évités modifient coûts, risques ou valeurs d'actifs, et L18.C10 a précisément
établi que l'amélioration peut entrer au compte d'actif sans devenir un revenu
de la période.

Le résultat conservable est plus étroit : l'exploitation de certains stocks
naturels produit des biens vendables tandis que certains bénéfices de
préservation restent diffus, tardifs ou non captables par celui qui les
finance. L'ampleur de cette asymétrie reste à mesurer.

### 3.6 Les exemples stylisés doivent rester manifestement fictifs

Marie, Jean et Claire sont déclarés idéaux-types, mais leur âge, leur histoire
et l'affirmation selon laquelle ils n'ont pas obtenu de crédit ressemblent à
des faits biographiques. Les remplacer par trois dossiers abstraits ou les
écrire au conditionnel évite de faire entrer des faits inventés dans un dépôt
public.

### 3.7 Le vocabulaire de NEMO doit être aligné

La conclusion parle encore d'une émission « adossée à la régénération ». Ce
mot a été retiré pour NEMO : il suggère une convertibilité ou un droit sur un
actif. La formulation arrêtée est « monnaie affectée à la préservation et à la
régénération des communs », avec une émission conditionnée par la qualification
d'activités essentielles.

L1.C15 ne doit pas annoncer cette solution comme conséquence de sa définition.
Il doit renvoyer au test de L1.C31.

## 4. Matrice affirmation–preuve

| Affirmation actuelle | Nature réelle | Appui actuel | Décision proposée |
|---|---|---|---|
| Quatre conditions cumulatives de solvabilité | définition du corpus | S1, S2 sont des textes de l'auteur | conserver comme `::norme::`, pas comme vocabulaire bancaire établi |
| Les activités essentielles en manquent presque toujours plusieurs | hypothèse empirique | aucune mesure | réduire ; renvoyer au protocole d'épreuve |
| Les deux premières conditions recouvrent les biens publics | comparaison conceptuelle partielle | S3 | confronter aussi externalités, biens tutélaires, soin, missions publiques et projets non bancables |
| L'emprunt public déplace le filtre vers l'État | interprétation conditionnelle | renvois internes | distinguer les régimes et supprimer la mécanique unique |
| Aucun canal monétaire n'échappe au remboursement | affirmation universelle | aucun appui suffisant | retirer |
| Tout entretien du vivant échoue au maillage | généralisation | aucun cas réel classé | retirer ou poser comme hypothèse à tester |
| Dissipation des stocks et flux monétaires sont structurellement couplés | hypothèse physique et économique | S6-S8 ne mesurent pas ce couplage | réduire et dissocier du concept |
| Programme costaricien : surfaces, montants, bénéficiaires | données | S9 agrège plusieurs reprises non ouvertes | ouvrir les sources primaires et séparer les séries |
| Additionnalité inférieure à 1 % | résultat empirique délimité | attribution incertaine entre les textes de S13 | ouvrir chaque étude, préciser période, métrique et périmètre |
| Les six remèdes rencontrent le même filtre | conclusion du corpus | les sources documentent des mécanismes distincts | remplacer par une comparaison des contournements et de leurs limites propres |
| Le concept justifie une émission sans remboursement | conclusion sur NEMO | F10 et les portefeuilles restent ouverts | retirer ; renvoyer à L1.C31 |

## 5. Audit des quinze sources inscrites

Toutes les sources sont actuellement `a_requalifier`. S15 n'est jamais appelée
dans le corps.

| Source | État de la mobilisation | Action documentaire |
|---|---|---|
| S1 — article de J.-C. Duval | source de provenance du concept et de la formule | ouvrir la version publiée, dater, citer les passages ; ne pas l'employer comme validation externe |
| S2 — livre fondateur | source de provenance | identifier l'édition et les pages ; distinguer ce qui vient du livre et de l'article |
| S3 — Samuelson 1954 | attribution possiblement anachronique de la paire non-rivalité/non-excluabilité | ouvrir le texte ; établir ce qu'il formule réellement ; compléter par une source de taxonomie si nécessaire |
| S4 — Ostrom 1990 | huertas et zanjeras, travail, mutualisation et cotisations | ouvrir l'édition et les chapitres précis ; ne pas généraliser au-delà des cas |
| S5 — Carney 2015 | « tragédie des horizons » | réutilisable après vérification du passage déjà ouvert pour L1.C09 |
| S6 — Georgescu-Roegen 1971 | thermodynamique du processus économique | ouvrir les passages exacts ; ne pas lui attribuer le couplage monétaire propre au corpus |
| S7 — Soddy 1926 | richesse réelle et richesse virtuelle | texte signalé ouvert ailleurs ; vérifier édition, chapitre et formulation exacte |
| S8 — Daly 1977/1991 | propositions d'économie stationnaire | ouvrir l'édition effectivement utilisée ; préciser la proposition mobilisée |
| S9 — FONAFIFO | loi, financement, surfaces, versements, familles | scinder loi, rapports FONAFIFO et reprises institutionnelles ; ne conserver que les chiffres remontés à leur source |
| S10 — Costanza et al. 2014 | évaluation distincte de marchandisation et privatisation | ouvrir le texte et vérifier que la phrase est bien celle des auteurs |
| S11 — Stern, Nordhaus, Quinet | trois signatures regroupées dans une seule entrée | scinder ; ne garder que les textes effectivement cités ; Quinet concerne le renvoi L1.C09 plutôt que le corps de C15 |
| S12 — Weber | définition de l'idéal-type | supprimer si les personnages deviennent de simples cas stylisés ; sinon ouvrir l'édition et le passage |
| S13 — Pattanayak et al. 2010 ; Arriagada et al. 2012 | additionnalité du programme costaricien | scinder les deux études ; ajouter la source réellement porteuse du « moins de 1 % » si différente |
| S14 — Pigou 1920 ; Goulder 1995 | subvention des externalités positives | scinder les auteurs ; retirer Goulder si aucun énoncé ne l'appelle |
| S15 — Wray 2012 ; Kelton 2020 | MMT | source inutilisée ; retirer ou appeler précisément, sans faire parler deux auteurs d'une seule voix |

Le premier gain documentaire ne viendra donc pas de l'ouverture indistincte de
quinze références. Il faut d'abord réécrire les affirmations : plusieurs
sources deviendront inutiles, et les sources restantes auront chacune une
fonction contrôlable.

## 6. Structure proposée

### 1. Une catégorie prospective

Dire ce que le concept propose, ce qu'il ne démontre pas, et séparer `E` du
filtre financier. Donner la formule logique complète.

### 2. Les quatre conditions et leur domaine

Définir M, C, T et A comme grille analytique de finançabilité autonome. Les
distinguer de la solvabilité juridique du débiteur et de la bancabilité
effective d'un projet avec garanties ou soutien public.

### 3. Cas positifs, négatifs et limites

Présenter des dossiers stylisés sans biographie inventée. Montrer des cas
candidats dedans, dehors et à la frontière. Ne pas conclure avant le classement
indépendant prévu par le protocole.

### 4. Ce que les autres mécanismes financent déjà

Examiner séparément impôt, subvention, dette publique, don, bénévolat,
gouvernance collective et finance privée. Dire quelles conditions chacun
contourne et quelles contraintes propres il rencontre.

### 5. Non-redondance et thermodynamique

Comparer le concept aux catégories voisines. Garder la dissipation des stocks
comme hypothèse explicative partielle, si ses sources et sa frontière sont
établies, sans en faire la définition.

### 6. Protocole d'épreuve

Reprendre les cinq critères et les cinq étapes de
`validation-essentiel-insolvable.md`. Énoncer les quatre conditions de vacuité.

### 7. Ce que cela permet de dire sur NEMO

Une catégorie cohérente peut désigner un phénomène trop petit ou déjà mieux
traité par d'autres instruments. L1.C31 et F10 décident de l'apport propre.
L1.C15 ne conclut ni à la nécessité, ni à la supériorité, ni à l'applicabilité
de NEMO.

## 7. Décisions demandées à l'auteur

1. Conserver « essentiel insolvable » comme nom d'une catégorie analytique
   prospective, en déclarant que « solvabilité » y a un sens conventionnel.
2. Maintenir les quatre conditions M, C, T et A comme définition du filtre.
3. Laisser `E` explicitement ouvert jusqu'à une définition indépendante, plutôt
   que le déduire des activités que NEMO entend financer.
4. Retirer la proposition universelle selon laquelle aucun canal de création
   monétaire n'échappe à une promesse de remboursement gagée sur une activité
   solvable.
5. Réduire la dette publique à un déplacement conditionnel des contraintes
   vers l'institution publique, variable selon le régime.
6. Sortir la « signature thermodynamique » du fondement du concept et la garder
   comme hypothèse explicative secondaire.
7. Traiter les six remèdes comme des mécanismes concurrents ou compensateurs,
   avec leurs limites propres, plutôt que comme six formes du même filtre.
8. Remplacer les trois biographies par des cas stylisés explicites.
9. Retirer « adossée à la régénération » et appliquer le vocabulaire déjà
   arrêté pour NEMO.
10. Faire de l'ampleur empirique et de la comparaison avec les portefeuilles
    concurrents des résultats ouverts, sans empêcher la vérification
    documentaire du chapitre.

## 8. Séquence après validation

1. Réécrire la structure conceptuelle, sans ouvrir de nouvelles sources.
2. Établir la matrice définitive des affirmations conservées.
3. Retirer les sources devenues sans fonction et scinder les entrées qui
   confondent plusieurs signatures.
4. Ouvrir les sources restantes, une par une, pour leur seul passage utile.
5. Produire un nouvel audit contradictoire sur le texte réécrit ; l'audit du
   3 septembre portait sur un autre état et ne peut pas suffire.
6. Traiter les objections, puis conduire l'audit factuel.
7. Passer à `verifie` si toutes les sources sont ouvertes et datées, si aucune
   vérification documentaire ne reste et si les inconnues empiriques sont
   exposées comme telles.

Le chapitre reste `audit_contradictoire`, `citable: false` jusqu'à cette
séquence. Aucun résultat de la présente note ne ferme
`OPERATIONNALISATION-INSOLVABLE`, F10 ou `PORTEFEUILLE-COMPARAISON`.
