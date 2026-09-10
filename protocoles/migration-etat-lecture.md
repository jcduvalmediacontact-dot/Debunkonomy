# Migration `etat_lecture` — proposition, non appliquée

**État : proposition, 2026-09-10, révisée quatre fois le même jour — après la
correction de l'auteur sur E-L6 ; après ses corrections sur le commit source,
l'état enregistré et la voie hors ligne ; après l'audit du fichier d'état, qui
ouvre un préalable distinct (§ 9) ; enfin après la validation par l'auteur des
douze changements de fond et de la restauration des vingt-sept dates. La
proposition elle-même ne modifie rien ; les commits préparatoires qu'elle
décrit sont énumérés au § 7.1, et chacun est limité à son objet.** Ni la convention, ni `controle.py`, ni
aucun chapitre, ni aucune date. **Aucune source n'est promue, aucun manifeste
n'est créé.**

**Place dans la séquence des sept jours** : étape 1 — migration documentaire et
contrôle reproductible. Aucune autre étape ne s'ouvre avant celle-ci.

---

## 1. Ce que l'audit établit, et ce qu'il n'établit pas

**Le défaut est réel et il est systémique.** `date_verification` est obligatoire
pour toute source primaire — convention § 4, et `CHAMPS_SOURCE_OBLIGATOIRES`
dans `controle.py`. Son sens est fixé au § 12 : *« date de contrôle de la source
pour `mode: date`, date de dernière revue pour `mode: revue` »*. **Ni « date
d'inscription », ni « DOI confirmé », ni « référence localisée ».** Le champ est
donc exigé à l'instant même où, pour une référence candidate, il n'a rien à
attester.

**La formulation exacte de ce que l'audit démontre.**

> **Pour une grande partie des sources existantes, les métadonnées ne permettent
> pas d'établir si la date correspond à la lecture du texte pertinent, à la
> localisation de la référence ou à une saisie par lots.**

**Une absence de preuve d'ouverture n'est pas une preuve de non-ouverture**, et
l'audit le montre lui-même : **185 sources portent une trace forte d'ouverture**
— l'union dédupliquée de T1, T2 et T7 —, dont **173 le marqueur explicite
`OUVERT PAR TÉLÉCHARGEMENT DIRECT`**, institué par le protocole lui-même.

**Le regroupement des dates est un indice, non une démonstration.** 401 sources
sur 1 161 portent une date **égale au jour de création de leur chapitre**, et les
dates se concentrent sur sept journées — 316 au 7 septembre, 289 au 6, 200 au 4.
**C'est un indice fort de saisie par lots. Il ne démontre pas à lui seul que les
textes n'ont pas été lus** : un chapitre peut être écrit le jour où ses sources
sont ouvertes, et c'est même le cas favorable.

**Et la reconstruction ne dépend pas d'un témoignage.** Sept familles de preuves
sont mobilisables avant de classer une source :

| trace | ce qu'elle vaut exactement | relevée |
|---|---|---|
| **T1** marqueur `OUVERT PAR TÉLÉCHARGEMENT DIRECT` | **la plus forte, parce qu'elle vient d'un marqueur institué par le protocole.** Mais elle atteste une **ouverture DÉCLARÉE** : elle reste à rapprocher de l'édition et du passage mobilisé | **173** |
| **T2** la liste en attente **affirme** l'ouverture, en nommant la référence | **affirmation interne, utile et non décisive.** Elle n'est **pas automatiquement plus fiable que les métadonnées qu'on cherche précisément à réparer** — c'est la même main qui a écrit les deux | **14** |
| **T3** la liste en attente **nie** l'ouverture, en nommant la référence | forte, en sens inverse | **136** |
| **T4** citation littérale attribuée à la référence dans le corps | **indicatif** — une citation peut venir d'une source seconde | **279** |
| **T5** la même référence porte T1 ou T2 dans un autre chapitre | **indicatif** — l'ouverture ne se transporte pas : édition et passage restent à contrôler | **12** |
| **T6** date de vérification **postérieure** à la création du fichier | **indice de passe dédiée, et rien de plus.** La comparaison est faussée par les versements postérieurs à l'écriture (§ 5). **Sans aucun rôle dans le contrôle** : ni la date de création du chapitre ni l'ancienne date ne décident plus de rien | **18** |
| **T7** dette bibliographique supposant une lecture — *« l'OCR ne porte pas les folios »* | **indice contextuel fort, NON preuve suffisante.** Il établit qu'un document ou son OCR a été consulté ; **il n'établit pas que l'édition a été identifiée ni que le passage pertinent a été lu** | **4** |

**AUCUNE DE CES TRACES N'EST UNE PREUVE D'`ouverte`.** Elles orientent un examen,
elles ne le remplacent pas.

**Deux gisements de preuves ne sont pas encore exploités** : l'historique Git
d'une part — la comparaison date / création de fichier est faussée, plusieurs
chapitres portant des dates **antérieures** à leur premier commit, signe que
l'écriture a précédé le versement — et **`Documents/Codex/`** d'autre part,
**19 répertoires datés d'acquisitions** dont aucun n'est encore rapproché des
références.

---

## 2. Le champ proposé

```yaml
etat_lecture: ouverte        # candidate | ouverte | a_requalifier
date_verification: 2026-09-03
```

| valeur | signification |
|---|---|
| `candidate` | source **explicitement sélectionnée**, mais **texte pertinent non lu** |
| `ouverte` | **édition identifiée et passage pertinent effectivement lu** |
| `a_requalifier` | **état historique incertain**, en attente de reconstruction ou de nouvelle ouverture |

**Les règles proposées.**

1. `date_verification` **obligatoire et autorisée seulement** pour `ouverte`.
2. `date_verification` **absente** pour `candidate`.
3. Pour `a_requalifier`, **l'ancienne date est conservée dans le manifeste et
   le rapport de migration, hors du chapitre. Elle ne vaut plus preuve, et elle
   ne sert à aucun calcul.**
4. Un chapitre **ne peut pas passer à `verifie`** si l'une de ses sources reste
   `candidate` ou `a_requalifier`.
5. `verifications_en_attente` **continue de porter** les problèmes de citation,
   de portée et d'adéquation entre la source et l'énoncé. **Le nouvel état ne
   les absorbe pas** : une source peut être `ouverte` et l'énoncé qu'elle
   appuie rester contesté.
6. Le contrôle **autorise** les sources `candidate` dans un brouillon, **mais
   les signale — de façon AGRÉGÉE par chapitre**, jamais une alerte par source.
7. La **génération publique les exclut mécaniquement**.

**`a_requalifier` EST RÉSERVÉ AUX SOURCES HÉRITÉES DE LA MIGRATION.** Une
source ajoutée **après** celle-ci est **soit `candidate`, soit `ouverte`** — il
n'y a pas de troisième possibilité pour un travail neuf, puisque celui qui
inscrit la référence sait s'il a lu le texte. **Sans cette réserve,
`a_requalifier` deviendrait un état d'attente permanent permettant de repousser
indéfiniment la décision éditoriale**, et le corpus aurait remplacé une date
qui affirme trop par un état qui n'affirme rien.

**Le contrôle peut le vérifier — mais pas par la date de création du chapitre.**
Une source nouvelle ajoutée après la migration à un chapitre ancien recevrait
`a_requalifier` sans que rien ne le détecte : **la date de création d'un chapitre
ne dit rien de l'ancienneté d'une occurrence de source.** La réserve s'applique
donc par un **manifeste explicite des occurrences historiques** (§ 3.1) :
`a_requalifier` n'est admis que pour une occurrence **inscrite au manifeste, sous
l'empreinte bibliographique qui y est enregistrée** — c'est la règle E-L6 révisée
(§ 3.6).

**Ce que ce champ est, et il faut le dire pour ne pas répéter la faute
précédente.** **`etat_lecture` n'est pas calculable.** C'est une **qualification
documentaire fondée sur des preuves**. Le script peut vérifier sa **cohérence**
— une date sans `ouverte`, un `verifie` avec une `candidate` — **il ne peut pas
vérifier sa vérité**. Le remplacer par un calcul serait promettre exactement ce
que `date_verification` a promis à tort.

---

## 3. Ce que la migration produirait — les livrables

**Aucun n'est produit ici. Aucune source n'est promue automatiquement à
`ouverte`.** Neuf livrables, et chacun a sa section :

1. le **manifeste** des occurrences historiques, lu par le contrôle (§ 3.1.1) ;
2. le **rapport** de conservation, lu par un humain (§ 3.1.2) ;
3. le **script de migration**, qui écrit une fois et uniformément (§ 3.2, § 7) ;
4. le **script de preuve**, qui établit la conservation (§ 8.4) ;
5. les **modifications de la convention** (§ 3.5) ;
6. les **tests bloquants** et les alertes agrégées de `controle.py` (§ 3.6) ;
7. la **définition des deux identités**, locale et documentaire (§ 3.7) ;
8. les **livrables de reproductibilité** du contrôle, voie connectée et voie
   hors ligne (§ 3.8) ;
9. le **préalable d'état** — réparer le mécanisme, auditer son retard, établir
   la référence (§ 9).

### 3.1 Deux livrables de conservation : le manifeste, et le rapport

**Le manifeste est lu par la machine ; le rapport est lu par un humain. Les deux
sortent du même relevé, au même instant, et le manifeste fait foi** : le rapport
en est la projection lisible, jamais une source concurrente.

#### 3.1.1 Le manifeste des occurrences historiques — `corpus/manifeste-etat-lecture.json`

**Ce qu'il est.** La liste close des occurrences de source qui existaient au
moment de la migration — **et la seule autorisation possible de l'état
`a_requalifier`**. Écrit **une fois**, par le script de migration, à l'étape 3 ;
**jamais édité à la main ; jamais réécrit par `controle.py`**, qui le lit
seulement. Format JSON — bibliothèque standard, aucune dépendance nouvelle —,
UTF-8, clés triées, indentation de deux espaces, pour que tout écart apparaisse
dans un diff.

**Ce que porte chaque occurrence** — le minimum, et rien de ce que la migration
produit n'entre dans l'empreinte :

| champ | contenu |
|---|---|
| `id` | **identifiant local** `chapitre/ref`, par exemple `L1.C08/S11` — unique, et contrôlé unique |
| `chapitre`, `ref` | les deux composantes, redondantes à dessein pour la lecture |
| `empreinte_bibliographique` | sha256 des **métadonnées bibliographiques d'origine** — règle ci-dessous |
| `ancienne_date_verification` | la date que portait l'occurrence avant la migration — **indice, jamais point de départ** |
| `date_migration` | la date à laquelle l'occurrence est passée en requalification — **le seul point de départ de A-L2** |
| `traces` | les traces T1 à T7 détectées, chacune avec son **emplacement** et sa **citation d'appui** |
| `file`, `orientation` | la file d'examen A, B, C ou D et son libellé — **proposée, jamais appliquée** |
| `etat_initial` | **toujours** `a_requalifier` ; le contrôle refuse toute autre valeur |

**La règle de l'empreinte bibliographique.** Elle se calcule sur les champs de
l'occurrence **à l'exclusion** de `etat_lecture`, de `date_verification` et de
tout ce que la migration produit ; à l'exclusion aussi de `ref` — déjà dans
l'identifiant — et de `horizon` / `motif_horizon`, qui sont des données de
contrôle, non de bibliographie, et qu'aucune occurrence ne porte aujourd'hui.
Restent **`nature`, `reference` et `url`** — `url` sur 169 occurrences. Forme
canonique : les blancs normalisés comme le fait `normalise()` dans `controle.py`,
les clés absentes omises, la sérialisation `json.dumps(sort_keys=True,
ensure_ascii=False, separators=(",", ":"))`, puis sha256 en hexadécimal complet.
**Deux outils qui n'appliqueraient pas la même règle produiraient deux
empreintes pour une même occurrence** : la règle est écrite dans l'en-tête du
manifeste, et `controle.py` l'implémente par une seule fonction, partagée avec
le script de migration.

**La forme, sur une occurrence réelle** — L1.C08/S11, traces contradictoires :

```json
{
  "schema": "manifeste-etat-lecture/1",
  "migration": {
    "date": "AAAA-MM-JJ",
    "commit_source": "<HEAD immédiatement antérieur à la migration>",
    "revision_convention": 12,
    "python": "3.14.5",
    "pyyaml": "6.0.3",
    "nombre_occurrences": 1161,
    "regle_empreinte": "sha256(json.dumps({nature, reference, url} normalisés, sort_keys=True, ensure_ascii=False, separators=(',', ':')))"
  },
  "occurrences": [
    {
      "id": "L1.C08/S11",
      "chapitre": "L1.C08",
      "ref": "S11",
      "empreinte_bibliographique": "<64 caractères hexadécimaux>",
      "ancienne_date_verification": "2026-09-03",
      "date_migration": "AAAA-MM-JJ",
      "traces": [
        {"code": "T2", "emplacement": "verifications_en_attente", "appui": "« … »"},
        {"code": "T3", "emplacement": "verifications_en_attente", "appui": "« … »"}
      ],
      "file": "B",
      "orientation": "traces contradictoires",
      "etat_initial": "a_requalifier"
    }
  ]
}
```

**Une liste, non un dictionnaire indexé par identifiant** : un objet JSON à clés
dupliquées se charge silencieusement en n'en gardant qu'une. La liste laisse le
doublon visible, et E-M1 le refuse.

**`commit_source` désigne le commit dont les occurrences ont été relevées** — le
HEAD propre immédiatement antérieur à la migration (§ 7.1). **Il ne désigne
jamais le commit qui contient le manifeste** : cet identifiant n'existe pas
quand le fichier est écrit, et l'y inscrire serait une autoréférence
impossible. Le commit de migration est rapporté après sa création, ailleurs.

**Ce qu'il ne porte pas, et pourquoi.** Ni le texte de la référence — il se relit
dans `commit_source` et dans le rapport —, ni l'identité documentaire (§ 3.7),
qui ne l'indexe jamais, ni aucun fichier acquis.

#### 3.1.2 Le rapport de conservation — `protocoles/rapport-migration-etat-lecture.md`

**Pour un lecteur humain, généré par le même script que le manifeste**, donc
incapable de s'en écarter. Il porte : l'en-tête de migration — date, commit
source, révision, versions, décomptes ; l'identifiant du commit de migration ne
peut y être ajouté que par un commit ultérieur, § 7.1 — ; les quatre files et
leurs effectifs ; **un
tableau par chapitre** ; et **une ligne par occurrence** avec l'identifiant,
l'ancienne date, les traces et leur citation d'appui, la file proposée. Il porte
enfin **la sortie de la preuve de conservation** (§ 8.4). Hors du schéma du
corpus : c'est un document de migration, comme les autres textes de
`protocoles/`.

### 3.2 La migration initiale — UNIFORME, et c'est la règle

**TOUTES les sources historiques reçoivent `a_requalifier`. Les 1 161, sans
exception.**

**Aucune trace ne modifie automatiquement l'état inscrit dans un chapitre.** T1
à T7 alimentent le rapport et **proposent une orientation d'examen** ; elles ne
promeuvent rien. Le passage vers `ouverte` ou `candidate` intervient **ensuite,
après examen de la source concernée**.

**Pourquoi l'uniformité plutôt que le classement automatique.** Une migration qui
promeut sur trace refait exactement la faute qu'elle répare : elle inscrit dans
le chapitre une qualification que personne n'a vérifiée. **L'état inscrit doit
toujours résulter d'un examen, jamais d'un motif reconnu par un script.**

**Le manifeste est l'entrée de l'étape 3, non son sous-produit.** Le script de
migration parcourt les identifiants du manifeste et n'écrit que sur eux : une
occurrence hors manifeste n'est pas touchée, et une occurrence du manifeste ne
peut pas être oubliée — la preuve de conservation (§ 8.4) le vérifie dans les
deux sens.

### 3.3 L'orientation d'examen — dans le rapport, jamais dans le chapitre

Le rapport classe les 1 161 sources en **quatre files d'examen**, et **les
quatre décomptes se bouclent**.

| file | définition reproductible | nombre |
|---|---|---|
| **orientation vers `ouverte`** | **union dédupliquée de T1, T2 et T7**, **sans** démenti T3 | **175** |
| **traces contradictoires** | union dédupliquée de T1, T2, T7 **avec** démenti T3 | **10** |
| **orientation vers `candidate`** | **T3 seul**, sans aucune trace forte contraire | **126** |
| **sans orientation** | aucune trace forte, dans un sens ni dans l'autre | **850** |
| **total** | | **1 161** |

**L'union dédupliquée T1 ∪ T2 ∪ T7 compte 185 sources** — 175 sans démenti,
10 avec. Le décompte est reproductible : il ne dépend d'aucun ordre de priorité
entre traces, seulement de l'appartenance à l'union et de la présence de T3.

**Répartition par livre des 175** : L20 : 37 · L18 : 31 · L26 : 13 · L8 : 12 ·
L19 : 11 · L2 : 10 · L7 : 10 · L1 : 6 · L10 : 6 · L17 : 5 · L24 : 5 · L6 : 5 ·
L12 : 4 · L15 : 4 · L23 : 4 · L11 : 3 · L16 : 3 · L21 : 3 · L22 : 2 · L13 : 1

**T4, T5 et T6 n'entrent dans aucune file.** Ils sont **indicatifs** : 279
citations littérales, 12 références ouvertes ailleurs et 18 dates postérieures à
la création du fichier enrichissent le dossier d'examen d'une source **sans en
orienter le classement**.

### 3.4 Les traces contradictoires

**10 sources** portent un démenti **et** une affirmation — S11 dans C08 en est
le cas type. **Elles n'ont pas d'orientation** : une contradiction n'est pas un
constat, et elle appelle l'examen le plus attentif, non le plus expéditif.

### 3.5 Les modifications de la convention

| section | modification |
|---|---|
| **en-tête**, ligne 3 | porter **la révision courante et sa date** — voir l'incohérence relevée ci-dessous |
| **§ 2**, arborescence | déclarer `manifeste-etat-lecture.json` et `requirements.txt` à côté de `livres.yaml` et `vocabulaire.yaml`, et le dossier `migrations/` des scripts à exécution unique |
| **§ 4**, table des champs de source | ajouter `etat_lecture`, **obligatoire** ; rendre `date_verification` **conditionnel — obligatoire si et seulement si `etat_lecture: ouverte`** |
| **§ 4**, listes vides et brouillon | dire qu'un brouillon peut porter des sources `candidate` |
| **§ 11**, boucle de production | l'étape 4 devient : *ouvrir le texte, porter `etat_lecture: ouverte` et la date* |
| **§ 12**, contrôle | **remplacer** la ligne bloquante *« source primaire sans `date_verification` ou sans `nature` »* par sa forme conditionnelle, et ajouter E-L1 à E-L6, E-M1 et les alertes agrégées A-L1 à A-L3 |
| **§ 15**, journal | incrémenter la révision, et **décrire la migration, le manifeste et la preuve de conservation** |

**Incohérence relevée, à corriger dans la même migration — et pas avant.**
L'en-tête de la convention annonce *« Révision 7 — 3 septembre 2026 »* alors que
son journal atteint la **révision 11 du 7 septembre 2026** ; `CLAUDE.md` annonce
de son côté *« Révision courante : r9 »*. **Trois numéros pour un même
document.** La migration, qui crée la révision suivante — la 12, si aucune ne
s'intercale —, porte l'en-tête à cette révision et à sa date, et corrige
`CLAUDE.md` dans le même commit. **Rien de cela n'est touché par la présente
proposition.**

### 3.6 Les tests bloquants

| code | condition de blocage |
|---|---|
| **E-L1** | `date_verification` présente sur une source qui n'est pas `ouverte` |
| **E-L2** | `date_verification` absente sur une source `ouverte` |
| **E-L3** | `etat_lecture` absent, ou valeur hors des trois admises |
| **E-L4** | chapitre `verifie` portant une source `candidate` ou `a_requalifier` |
| **E-L5** | génération publique demandée pour un chapitre portant une source non `ouverte` |
| **E-L6** | `a_requalifier` sur une occurrence **qui n'est pas inscrite au manifeste** — soit son identifiant `chapitre/ref` en est absent, soit il y figure **mais l'empreinte bibliographique courante diffère de l'empreinte enregistrée**. Dans les deux cas l'occurrence est neuve : **une source ajoutée après la migration, y compris dans un chapitre ancien, est `candidate` ou `ouverte`** ; **une référence historique remplacée par une autre édition ou un autre document n'hérite pas de l'état historique** |
| **E-M1** | manifeste **absent, illisible ou incohérent** — identifiant en doublon, `etat_initial` autre que `a_requalifier`, `date_migration` absente, mal formée ou différente de celle de l'en-tête, nombre déclaré différent du nombre d'entrées. **Le contrôle s'arrête** : E-L6 n'est pas évaluable |
| **A-L1** *(alerte AGRÉGÉE)* | **bilan par chapitre** : « n sources `candidate` sur m » — **une ligne par chapitre, jamais une par source** |
| **A-L2** *(alerte AGRÉGÉE)* | **bilan par chapitre** des sources `a_requalifier`, avec leur ancienneté **comptée depuis la `date_migration` du manifeste — jamais depuis l'ancienne `date_verification`** |
| **A-L3** *(alerte AGRÉGÉE)* | **bilan par chapitre** des entrées du manifeste **sans occurrence correspondante** dans le corpus — source retirée ou `ref` renommée. Informative : retirer une source est un acte éditorial légitime, et le manifeste n'a pas à l'interdire |

**LE BRUIT EST UN DÉFAUT DE CONTRÔLE, PAS UN DÉTAIL D'AFFICHAGE.** Des sources
`candidate` dans un brouillon sont **normales** : c'est même l'état attendu d'un
chapitre en cours. **Une alerte par source produirait plusieurs centaines de
lignes permanentes et rendrait le diagnostic inutilisable** — donc ignoré, donc
inopérant. **Le contrôle agrège par chapitre.**

**Les blocages individuels, eux, restent justifiés, et ils sont de deux
sortes.** E-L1, E-L2, E-L3 et E-L6 sont **structurels** : ils s'évaluent à chaque
contrôle, comme le champ inconnu du § 12, et ils sont rares par construction —
un corpus bien tenu n'en déclenche aucun. E-L4 et E-L5 ne se déclenchent qu'aux
**deux moments qui comptent** : le passage à `verifie`, et l'entrée dans la
génération publique.

**Le point de départ de A-L2 est tranché : la `date_migration` du manifeste.**
L'ancienneté d'une source `a_requalifier` se compte depuis le jour où elle a été
mise en requalification, et depuis lui seul. **L'ancienne `date_verification` ne
sert jamais à ce calcul** : c'est précisément elle qui est mise en doute, et elle
n'est d'ailleurs plus dans le chapitre — le manifeste la porte à titre d'indice
de datation, non de point de départ. La date vit dans le manifeste et non dans
le chapitre, parce qu'elle qualifie la procédure et non la source : l'inscrire
dans le chapitre créerait un second champ non calculable pour surveiller le
premier.

**Et deux tests de non-régression, qui valent pour le script lui-même** : une
source `candidate` **doit** faire échouer E-L4 sur un chapitre `verifie`, et une
source `a_requalifier` **hors manifeste** — ou sous une empreinte différente —
**doit** faire échouer E-L6. Un contrôle qui ne se déclenche jamais est
décoratif — le corpus l'a établi ailleurs.

### 3.7 Deux identités, strictement séparées

**L'identité locale d'une occurrence est `chapitre/ref`.** C'est elle que la
migration inscrit au manifeste et que le contrôle lit. Elle est **unique dans le
corpus de ce jour** — 1 161 identifiants pour 1 161 occurrences, aucun doublon —
et le contrôle la maintient unique. Elle ne change pas quand l'occurrence est
examinée : une occurrence sort de `a_requalifier`, elle ne sort pas du manifeste.

**L'identité documentaire d'une source est un sextuplet**, et elle ne sert qu'à
une chose : **rapprocher les acquisitions** de `Documents/Codex/`, et reconnaître
qu'un même document est cité dans plusieurs chapitres.

| composante | rôle |
|---|---|
| **auteurs** | liste ordonnée, noms normalisés |
| **titre** | casse, accents, ponctuation et sous-titre réduits à une forme canonique |
| **édition** | **la composante décisive** — c'est elle que le titre seul écrase |
| **année** | de l'édition mobilisée, non de la première parution |
| **DOI ou URL** | identifiant stable quand il existe |
| **empreinte du fichier** | **si un fichier existe** — la seule composante qui ne se discute pas |

**Un rapprochement par titre seul attribuerait l'ouverture d'une édition au
passage d'une autre.** C'est le risque propre aux dix-neuf répertoires
d'acquisition, et il faut le fermer avant de les exploiter. **Deux sources
partageant titre, auteurs et année mais non l'édition sont deux sources.** Le
corpus l'a déjà rencontré : S11 est ouverte dans L16.C01 sans que cette
ouverture vaille pour C08, faute d'édition et de passage vérifiés.

**Aucun rapprochement documentaire, exact ou approximatif, ne change
`etat_lecture`.** Un rapprochement produit une **proposition**, versée au rapport
avec son degré de concordance — composantes égales, absentes, divergentes — et
**examinée à l'étape 5 comme n'importe quelle trace**. L'identité documentaire
n'est jamais une clé du manifeste : elle l'annote, elle ne l'indexe pas. T5 en
est l'illustration : la même référence ouverte ailleurs est un indice, pas un
transport d'ouverture.

**Ce qui entre au dépôt public, et ce qui n'y entre jamais.** Les fichiers
acquis **restent dans les espaces d'acquisition autorisés**. La migration ne
verse au dépôt **que les métadonnées et les empreintes** — jamais les fichiers
eux-mêmes sans droit de publication. **Un PDF sous droits ne devient pas
publiable parce qu'il sert de preuve.**

### 3.8 La reproductibilité du contrôle — voie connectée, voie hors ligne, non implémentées

**Un contrôle qui n'est vert que sur la machine de l'auteur n'est pas un
contrôle.** Le dépôt ne déclare aujourd'hui aucune version de sa dépendance
unique : `CLAUDE.md` dit *« pip install pyyaml »*, sans numéro. Relevé ce jour
sur la machine de travail — **la seule plateforme testée** :

| composante | constaté le 2026-09-10 |
|---|---|
| système | Windows 11 |
| Python | 3.14.5 |
| PyYAML | **6.0.3** |
| liaisons libyaml | présentes, **et sans effet** : `yaml.safe_load` emploie le chargeur pur Python, la version épinglée n'en dépend donc pas |
| autre dépendance | aucune — bibliothèque standard seule |

**Deux voies, et elles ne promettent pas la même chose.**

**La voie connectée** rend la dépendance **déclarée et reproductible quand
l'accès à l'index des paquets fonctionne** — et seulement alors.

| livrable | forme proposée |
|---|---|
| **déclaration de version** | `corpus/requirements.txt`, trois lignes : un commentaire datant le relevé et la version de Python constatée, puis `PyYAML==6.0.3`. **Épinglage exact**, pas de borne inférieure |
| **commande d'installation** | `python -m pip install -r corpus/requirements.txt` — la seule documentée ; `CLAUDE.md` renvoie vers elle dans la même migration |
| **commande unique de contrôle** | `python corpus/controle.py` — inchangée ; `--publier` et `--maj-etat` restent des options, non des commandes distinctes |
| **test en environnement propre** | `corpus/test_environnement_propre.py` : crée un environnement virtuel **dans un répertoire temporaire hors du dépôt**, y installe la dépendance par la voie connectée ou, à défaut, par la voie hors ligne, vérifie que `yaml.__version__` vaut exactement la version déclarée, exécute la commande unique de contrôle et exige **le code de sortie 0 et un bilan identique** à celui de l'environnement de travail sur le même commit, puis rejoue la preuve de conservation (§ 8.4) |

**Le test distingue trois issues, et il ne les confond jamais :**

| issue | code de sortie | ce qu'elle signifie |
|---|---|---|
| contrôle passé | 0 | le corpus est contrôlable depuis un environnement neuf |
| **contrôle en échec** | 1 | **un défaut du corpus** — blocage, bilan différent, invariant faux |
| **dépendance indisponible** | 2 | **ni index accessible, ni cache local, ni voie hors ligne instruite. Ce n'est pas un défaut du corpus**, et le test le dit en toutes lettres |

**Ce que `requirements.txt` ne résout pas.** Le cas déjà rencontré : **Python
présent, PyYAML absent, accès réseau bloqué.** Dans cet environnement, le
fichier épinglé ne sert à rien, et le test en environnement propre **dépend
aujourd'hui d'un accès réseau ou d'un cache local de `pip`**. Son échec faute de
réseau **n'est pas un défaut du corpus**, et ne doit jamais être rapporté comme
tel.

**La voie hors ligne — livrable de mise en service, à instruire.** L'une des
deux formes :

- **une roue PyYAML compatible**, conservée **avec son empreinte et sa licence**
  — une roue est propre à une version de Python et à une plateforme, et celle
  qui serait conservée ne vaut que pour la plateforme testée ;
- **une autre distribution autonome documentée** — par exemple le paquet
  `yaml` pur Python de PyYAML, versé avec sa licence et chargé en repli par le
  contrôle quand l'installation standard manque.

**La solution exacte est choisie à l'implémentation.** Ce que le protocole
fixe, c'est la portée : **aucune portabilité n'est revendiquée sur une
plateforme qui n'a pas été testée**, et **un `requirements.txt` ne suffit pas
dans un environnement sans réseau**.

Les commandes de la voie connectée, telles qu'un relecteur les exécute à la
main — **non exécutées dans le cadre de cette proposition** ; PowerShell sur la
plateforme testée, puis POSIX, **non testé** :

```
python -m venv $env:TEMP\controle-propre
& $env:TEMP\controle-propre\Scripts\python -m pip install -r corpus\requirements.txt
& $env:TEMP\controle-propre\Scripts\python corpus\controle.py
```

```
python3 -m venv /tmp/controle-propre
/tmp/controle-propre/bin/python -m pip install -r corpus/requirements.txt
/tmp/controle-propre/bin/python corpus/controle.py
```

**Ce que ces livrables ne garantissent pas.** La version de `pip` n'est pas
épinglée ; la version de Python est constatée, non exigée — le test la relève
et la compare, il ne l'impose pas ; et la voie hors ligne n'existe pas tant
qu'elle n'est pas instruite. **Le corpus n'a pas à promettre une portabilité
qu'il n'a pas mesurée.**

---

## 4. C08 — la file d'examen

**Les onze sources reçoivent `a_requalifier` à la migration, comme toutes les
autres.** Ce qui suit n'est **pas un classement** : c'est **l'ordre dans lequel
les examiner**, et ce que chacun devra établir.

| priorité | réf | ce que l'examen doit établir |
|---|---|---|
| **1** | **S6** Jackson & Victor | **la lecture de la conclusion centrale** — *« une économie à encours stable et intérêts redépensés peut honorer ses dettes sans croissance »*. **Priorité élevée : ce résultat est central et sans trace suffisante** |
| **1** | **S7** Cahen-Fourot & Lavoie | même conclusion, même priorité, même absence de trace |
| **2** | **S11** Gesell | **traces contradictoires** — niée dans C08, ouverte le 8 septembre par L16.C01. Vérifier **l'édition ET le passage effectivement utilisés dans C08** |
| **3** | **S2** Soddy | **forte présomption de lecture, passage retrouvé.** Reste la **dette de folio** à résoudre |
| **4** | **S1** BoE 2014 | **reconstruction nécessaire** — Git, Codex, ou l'emploi de la même source dans L1.C07 et L19 |
| **4** | **S3** IIF | reconstruction nécessaire ; chiffres précis employés |
| **4** | **S4** Eurostat | reconstruction nécessaire ; une trace partielle existe — l'extraction 15-74 ans a été tentée |
| **5** | **S5** Lavoie | **présomption de candidature à confirmer** — chapitre exact à établir |
| **5** | **S8** S&P Global | présomption à confirmer ; **accès bloqué**, et le corpus ne contourne pas |
| **5** | **S9** BMJ Open | présomption à confirmer |
| **5** | **S10** Moore | présomption à confirmer |

**S6 et S7 commandent la file**, et ils ne figuraient dans aucune liste de
démentis : **le silence les avait rendus invisibles**. Ils portent le résultat
qui fonde la forme conditionnelle de la contrainte de croissance — celle que
toute la refonte du Livre 1 propage.

**Gesell reste hors de C08.** C08 écrit que Wörgl *« relève d'un autre principe »*
et *« illustre moins l'émission sans dette que l'accélération de la
circulation »*. **Il n'invoque pas Gesell comme précédent direct de NEMO.**
**AUCUN APPORT SUR GESELL N'EST AJOUTÉ À C08 TANT QUE LA VÉRIFICATION DE
L'ÉDITION ET DU PASSAGE N'EST PAS FAITE**, et la conclusion sur la règle de prix
demeure dans L16.C01.

---

## 5. Les limites de cet instrument

**Il donne un plancher, jamais un compte.** Il reconnaît des tournures ; un
démenti ou une affirmation formulés autrement lui échappent — **T7 n'a trouvé que
4 cas, ce qui est invraisemblablement bas.**

**Il ne détecte pas l'ouverture silencieuse.** Une source réellement lue dont la
liste ne dit rien tombe en `a_requalifier`. **C'est voulu** : l'état nomme
l'incertitude documentaire, il n'accuse personne.

**La trace Git est actuellement inexploitable telle quelle.** Plusieurs chapitres
portent des dates de vérification **antérieures** à leur premier commit — L1.C08
est daté du 3 septembre et versé le 7. L'écriture précède le versement, et la
comparaison naïve ne dit rien. **Il faudra suivre les renommages** et lire les
diffs d'en-tête, non les dates de création.

**Et `Documents/Codex/` n'est pas rapproché.** 19 répertoires d'acquisitions
datés attendent d'être appariés aux références. **C'est le gisement de preuves le
plus prometteur et le seul entièrement inexploité.**

**Et le manifeste est strict par construction, ce qui a un coût.** Corriger une
coquille dans la `reference` d'une occurrence encore `a_requalifier` change son
empreinte bibliographique et déclenche E-L6 : l'occurrence doit alors être
qualifiée `candidate` ou `ouverte`. **C'est accepté** : celui qui corrige une
référence sait s'il a lu le texte, et la règle vaut mieux qu'une procédure de
rectification du manifeste qui rouvrirait la porte à l'héritage automatique. Si
ce coût se révélait excessif à l'usage, la seule issue admissible serait une
rectification **datée, motivée et inscrite dans le manifeste** — jamais une
tolérance du contrôle.

**Et l'état enregistré n'est pas surveillé.** Un chapitre sans entrée dans
`.etat-corpus.json` ne déclenche rien : le contrôle compare à l'état enregistré
quand il existe, il ne signale ni son absence ni son retard. Relevé du
2026-09-10, en lecture seule : **268 entrées pour 335 chapitres, 67 chapitres
sans entrée, 12 empreintes éditoriales et 39 empreintes de métadonnées
différentes de celles qu'on recalcule** — le dernier enregistrement date du
7 septembre. **Le § 9 en fait un préalable distinct** : réparer le mécanisme —
P6 à P8 rendent la surveillance permanente —, auditer son retard, puis établir
l'état de référence, **avant que `commit_source` soit fixé.**

---

## 6. Ce que cette proposition ne fait pas

**Elle ne modifie rien.** Ni la convention, ni `controle.py`, ni un chapitre, ni
une date, ni un état. **Aucune source n'est promue à `ouverte`.**

**Elle ne crée pas le manifeste.** Aucun relevé n'est clos, aucun fichier JSON
n'existe, aucune empreinte bibliographique n'est calculée pour de bon : le format
est proposé, et lui seul.

**Elle ne répare pas le mécanisme d'état et n'exécute pas `--maj-etat`.** Le § 9
prescrit la réparation, l'audit et l'état de référence ; il ne les fait pas, et
`.etat-corpus.json` n'a pas bougé.

**Elle ne referme pas la question du champ.** L'option retenue à titre provisoire
est la deuxième des trois examinées ; **un état saisi à la main reste aussi
faillible que la date qu'il remplace**. Ce qu'il apporte n'est pas
l'infaillibilité, c'est que **l'incertitude devienne dicible** — `a_requalifier`
n'existe que pour cela.

**Et elle ne remplace pas le tri.** 1 161 qualifications à porter ne sont pas une
migration scriptée : c'est **le goulot d'étranglement volontaire du § 11**, et il
ne s'élargit pas avec l'outillage.

---

## 7. La règle de migration — enchaînement reproductible

**Aucune étape n'est exécutée. L'enchaînement est donné pour pouvoir être
rejoué, contesté et corrigé avant d'être lancé.**

```
ÉTAPE 0 — FIXER LE COMMIT SOURCE
    préalables commités, chacun dans son commit (§ 7.1) :
        le protocole validé ; la réparation du mécanisme d'état et l'état de
        référence (§ 9) ; les dépendances — requirements.txt, voie hors ligne
        si instruite
    arbre de travail propre — git status vide
    contrôle vert en environnement propre, ou « dépendance indisponible » motivée
    → ce HEAD propre est commit_source : le commit dont les occurrences sont relevées
    → sans point de départ daté ET reproductible, la migration n'est pas rejouable

ÉTAPE 1 — RELEVER, SANS RIEN ÉCRIRE DANS LE CORPUS
    lecture de l'état antérieur par git show <commit_source>:<fichier>
    pour chaque occurrence datée de commit_source (1 161 au commit 98713a0, ce jour) :
        identifiant chapitre/ref, empreinte bibliographique, ancienne date
        traces T1..T7, chacune avec son emplacement et sa citation d'appui
    → MANIFESTE PROVISOIRE (JSON) et RAPPORT (Markdown), issus du même relevé
    → contrôle : identifiants uniques, nombre = nombre d'occurrences datées

ÉTAPE 2 — ORIENTER, SANS RIEN ÉCRIRE DANS LE CORPUS
    file A  union(T1,T2,T7) sans T3        → orientation « ouverte »
    file B  union(T1,T2,T7) avec T3        → traces contradictoires
    file C  T3 seul                         → orientation « candidate »
    file D  aucune trace forte              → sans orientation
    contrôle : |A|+|B|+|C|+|D| = nombre d'occurrences, sinon la migration s'arrête
    → T4, T5 et T6 enrichissent le dossier, n'orientent aucune file
    → la file entre au manifeste ; elle n'entre dans aucun chapitre

ÉTAPE 3 — ÉCRIRE, UNE SEULE FOIS ET UNIFORMÉMENT
    pour CHAQUE identifiant du manifeste, et pour lui seul :
        etat_lecture: a_requalifier
        retirer la ligne date_verification du chapitre
    en-têtes modifiés ligne à ligne, JAMAIS re-sérialisés
    inscrire date_migration dans chaque entrée, puis CLORE le manifeste
    → aucune promotion, aucune exception, aucune trace consultée ici
    → l'ancienne date ne survit que dans le manifeste et le rapport

ÉTAPE 3 bis — PROUVER LA CONSERVATION
    invariants I1..I6 (§ 8.4), vérifiés par script
    un seul invariant faux → retour à l'étape 0, rien n'est commité
    → la sortie de la preuve est jointe au rapport et au message du commit

ÉTAPE 4 — OUVRIR LE SCHÉMA AU NOUVEL ÉTAT, ET ENREGISTRER L'ÉTAT
    convention : en-tête (révision courante), § 2, § 4, § 11, § 12, § 15
    controle.py : lecture du manifeste, E-L1..E-L6, E-M1, A-L1..A-L3 agrégées
    tests bloquants, dont deux tests de non-régression :
        un « verifie » gardant une source non ouverte → E-L4 doit échouer
        une source a_requalifier hors manifeste       → E-L6 doit échouer
    contrôle complet sur le corpus migré : python corpus/controle.py, vert
    enregistrement officiel du nouvel état : --maj-etat, forme déterminée en test
    invariant I7 (§ 8.4) : .etat-corpus.json cohérent avec l'état migré
    → les étapes 3, 3 bis et 4 — chapitres, manifeste, rapport, convention,
      controle.py, .etat-corpus.json — forment UN SEUL commit (§ 7.1)

ÉTAPE 5 — EXAMINER, OCCURRENCE PAR OCCURRENCE
    dans l'ordre A, B, C, D
    chaque examen établit : édition identifiée ? passage lu ?
    puis écrit etat_lecture: ouverte + date, OU candidate sans date
    → le manifeste ne bouge pas : l'occurrence quitte a_requalifier,
      elle ne quitte pas le manifeste
    → c'est le goulot d'étranglement du § 11, et il ne s'élargit pas

ÉTAPE 6 — RAPPROCHER LES ACQUISITIONS
    identité documentaire (§ 3.7), définie AVANT d'apparier
    tout rapprochement est une PROPOSITION versée au rapport, examinée à l'étape 5
    aucun rapprochement, exact ou approximatif, ne change etat_lecture
    n'importer au dépôt que métadonnées et empreintes
    → jamais un fichier sous droits
```

### 7.1 L'enchaînement des commits — et ce que `commit_source` désigne

1. **Protocole validé et commité seul.**
2. **Réparation de `controle.py` et tests de conservation de l'état** (§ 9.2,
   § 9.3) — un commit, examinable seul.
3. **Restauration des 27 dates de fond déplacées par des métadonnées seules**
   (§ 9.5) — un commit de **réparation de provenance**, qui ne touche ni corps
   ni résumé.
4. **Inscription tardive des douze changements de fond validés par l'auteur**
   (§ 9.1) — dans l'état, avec la date réelle de `revision_de_fond` que chaque
   chapitre porte.
5. **Initialisation tardive des 67 chapitres jamais enregistrés** (§ 9.2, P5).
6. **Établissement et commit de l'état de référence complet** (§ 9.4) — les
   points 4 et 5 sont deux effets d'un même enregistrement et forment avec lui
   un seul commit, **distinct du commit de migration**.
7. **Contrôle reproductible et arbre propre** (§ 3.8).
8. **Fixation de `commit_source`** : ce HEAD propre.
9. **Migration atomique `etat_lecture`** — manifeste, rapport, convention,
   contrôle, chapitres et `.etat-corpus.json`, en un seul commit.

L'audit en lecture seule du fichier d'état (§ 9.1) précède le point 2 ; il a
été fait le 2026-09-10 et **est à rejouer au moment de l'exécution**.

**La migration lit l'état antérieur avec `git show <commit_source>:<fichier>`**
— jamais dans l'arbre de travail, qu'elle est en train de modifier. **Et le
commit de migration est rapporté après sa création** — à l'auteur, et au dépôt
s'il le faut par un commit ultérieur — **mais n'est pas inscrit dans son propre
manifeste** : son identifiant n'existe pas quand le fichier est écrit, et l'y
inscrire serait une autoréférence impossible. **Le « commit préparatoire
d'état » n'est jamais une simple exécution de la commande actuelle** : celle-ci
détruirait les 268 qualifications qu'elle devrait conserver (§ 9.1).

**Quatre propriétés de cet enchaînement, et elles sont ce qui le rend
défendable.** **L'étape 3 ne consulte aucune trace** — elle est donc rejouable à
l'identique par quiconque, sans jugement. **Les étapes 1 et 2 n'écrivent rien
dans le corpus** — elles peuvent être rejouées, contestées et corrigées sans le
toucher. **Les étapes 3, 3 bis et 4 sont un seul commit** — chapitres migrés,
manifeste, rapport, convention, `controle.py` et `.etat-corpus.json` — : entre
l'écriture de `etat_lecture` et l'ouverture du schéma, le contrôle refuse le
corpus pour champ inconnu sur 1 161 occurrences, et **cet état intermédiaire ne
doit jamais être commité** — c'est la règle du § 12, *« une migration scriptée
sur l'ensemble du corpus, en une fois »*. Et **`commit_source` n'est jamais le
commit de migration** : il lui est antérieur, et c'est ce qui rend la preuve
rejouable.

---

## 8. Les décomptes proposés

### 8.1 Immédiatement après l'étape 3

| état | sources | part |
|---|---|---|
| `a_requalifier` | **1 161** | **100 %** |
| `ouverte` | 0 | — |
| `candidate` | 0 | — |

**Aucune source n'est ouverte au sortir de la migration, et c'est le résultat
attendu.** L'état du corpus devient **honnête plutôt que présumé** : il ne dit
plus que 1 161 sources sont vérifiées, il dit que 1 161 restent à qualifier.

**Effet mécanique sur le corpus** : **aucun chapitre ne peut passer à `verifie`**
tant qu'aucune de ses sources n'est examinée. Le corpus comptant **zéro chapitre
`verifie`**, cet effet ne retire rien — **il rend seulement visible ce qui était
déjà vrai**.

### 8.2 Les quatre files d'examen — orientation, non état

| file | définition | sources | chapitres |
|---|---|---|---|
| **A** — orientation `ouverte` | union(T1,T2,T7) **sans** T3 | **175** | 20 livres |
| **B** — traces contradictoires | union(T1,T2,T7) **avec** T3 | **10** | dont L1.C08 |
| **C** — orientation `candidate` | T3 seul | **126** | 35 chapitres |
| **D** — sans orientation | aucune trace forte | **850** | le reste |
| **total** | | **1 161** | **323** |

**La file D est la vraie mesure du travail**, et elle représente **73 %** des
sources. Ce n'est pas une accusation : c'est le nombre de sources dont **rien,
dans le corpus, ne dit si elles ont été lues**.

### 8.3 Ce que le manifeste doit porter, et que les décomptes ne disent pas

**La date de migration, par occurrence**, sans laquelle A-L2 n'est pas
calculable — et depuis laquelle seule elle l'est. **L'ancienne date de chaque
occurrence**, qui ne vaut plus preuve et ne sert à aucun calcul, mais reste un
indice de datation. **L'empreinte bibliographique d'origine**, sans laquelle
E-L6 ne distinguerait pas une occurrence historique d'une occurrence qui l'a
remplacée. **Et la citation d'appui de chaque trace**, faute de quoi
l'orientation serait aussi invérifiable que la date qu'elle remplace.

### 8.4 La preuve de conservation — huit invariants, vérifiés par script

**« La migration conserve exactement 1 161 occurrences » n'est pas une
affirmation, c'est le résultat d'un programme.** Le nombre lui-même n'est pas
inscrit d'avance : il est relevé sur `commit_source` — **1 161 au commit
`98713a0`, constaté le 2026-09-10 ; `commit_source` lui sera postérieur, et le
relevé y est refait** — et c'est ce relevé, non le chiffre, que la preuve
compare.

**Le relevé de ce jour, sur lequel les invariants sont calibrés :**

| mesure | valeur |
|---|---|
| chapitres | 335 |
| chapitres portant au moins une occurrence | 323 |
| occurrences de source | 1 161 |
| occurrences portant `date_verification` | 1 161 — toutes |
| occurrences sans `ref` | 0 |
| identifiants `chapitre/ref` distincts | 1 161 — aucun doublon |
| lignes `date_verification:` dans les en-têtes | 1 161 — une par occurrence, chacune sur sa propre ligne |
| `reference` ou `url` en scalaire de bloc | 0 |

Les deux dernières lignes établissent que **l'étape 3 peut modifier les en-têtes
ligne à ligne**, sans jamais re-sérialiser le YAML — la re-sérialisation
reformaterait les 335 en-têtes et pourrait altérer les blancs des références,
donc leurs empreintes. **Le corpus a déjà payé cette faute une fois** : un
correctif qui supposait des scalaires de bloc a écrasé F10.

**Les huit invariants** — l'état « avant » se lit dans `commit_source`, par
`git show <commit_source>:<fichier>`, et l'état « après » dans l'arbre de
travail :

| invariant | ce qui doit être vrai |
|---|---|
| **I1** identifiants | l'ensemble des `chapitre/ref` portant `a_requalifier` **après** = l'ensemble des `chapitre/ref` portant `date_verification` **avant** = l'ensemble des identifiants du manifeste. **Égalité de trois ensembles, dans les deux sens** — pas un simple décompte |
| **I2** vidage | après l'étape 3, **zéro** `date_verification`, **zéro** `ouverte`, **zéro** `candidate` dans le corpus |
| **I3** effectifs | le nombre d'occurrences **de chaque chapitre** est identique avant et après — un vecteur de 335 comptes, non un total |
| **I4** empreintes bibliographiques | pour chaque occurrence, l'empreinte calculée **après** = l'empreinte calculée **avant** = l'empreinte du manifeste |
| **I5** corps | l'empreinte éditoriale — corps et résumé, celle de `controler_empreintes` — est identique avant et après pour **les 335 chapitres** ; l'empreinte de métadonnées change pour **exactement les 323 chapitres** qui portent une occurrence, et pour aucun des 12 autres |
| **I6** manifeste | identifiants uniques ; `nombre_occurrences` égal au nombre d'entrées ; `etat_initial` = `a_requalifier` partout ; `date_migration` identique partout et égale à celle de l'en-tête |
| **I7** état enregistré | pour les 335 chapitres, les empreintes `editoriale` et `metadonnees` enregistrées dans `.etat-corpus.json` après l'enregistrement de l'étape 4 sont égales aux empreintes recalculées sur les chapitres migrés ; et les 335 `editoriale` sont égales à celles recalculées sur les chapitres de `commit_source` — donc à celles que le `.etat-corpus.json` de `commit_source` enregistre, puisque le § 9 l'a établi à jour avant que `commit_source` soit fixé |
| **I8** qualifications | l'invariant Q (§ 9.3) tient sur le commit de migration : les 335 qualifications de `commit_source` se retrouvent après l'enregistrement, à l'identique, la migration ne demandant aucune requalification |

**La commande d'enregistrement, à la lecture du code — la forme exacte est
déterminée en test.** Avec le script actuel, `--maj-etat` refuse d'écrire s'il
reste un blocage ou une décision en attente ; une décision n'est levée que par
une empreinte éditoriale modifiée à `revision_de_fond` inchangée ; un changement
de métadonnées seul n'en lève aucune — **mais l'enregistrement reconstruit le
fichier entier et perd toute qualification, et `--editorial` ou `--fond`
estampillent les 335 entrées**, y compris les 12 chapitres que la migration ne
touche pas. C'est le défaut que le § 9 répare **avant** la migration. **Avec le
script réparé, `--maj-etat` sans option est la forme attendue** : les empreintes
des 323 chapitres migrés changent, les 335 qualifications sont conservées (P1,
P2), et l'invariant I8 le vérifie. Si le test montre une décision en attente,
c'est que l'étape 3 a touché un corps, **et c'est I5 qui a échoué, non la
commande**.

**Le script de preuve** — `corpus/migrations/etat-lecture/prouver.py`, à écrire,
à côté du script de migration `migrer.py` — imprime les huit lignes avec les
valeurs mesurées et **sort en erreur au premier invariant faux** ; sa sortie est
jointe au rapport de conservation et au message du commit. **La preuve est
rejouable par quiconque** : `commit_source`, le manifeste et le script
suffisent, aujourd'hui comme dans un an.

---

## 9. Le préalable d'état — réparer le mécanisme, auditer son retard, puis établir la référence

**Ce préalable est distinct de la migration, et il la précède.** Il est terminé
et commité **avant que `commit_source` soit fixé** (§ 7.1). Il répond à un autre
défaut que celui de `date_verification` : **un dispositif de surveillance
aveugle sur 67 chapitres, et une commande d'enregistrement qui détruit ce
qu'elle devrait conserver.** Le corpus ne peut se dire opérationnel ni avec
l'un ni avec l'autre.

### 9.1 Ce que l'audit du 2026-09-10 établit — lecture seule, rien n'est écrit

| constat | valeur |
|---|---|
| chapitres | 335 |
| entrées de `.etat-corpus.json` | 268 — dernier enregistrement `292d490`, 7 septembre |
| commits depuis ce dernier enregistrement | 121 |
| chapitres sans entrée | **67**, créés du 7 au 9 septembre ; **aucun n'a jamais figuré dans aucune version historique du fichier** |
| entrées sans chapitre | 0 |
| empreintes éditoriales divergentes | **12** — 8 amorces de livres remplacées par le chapitre réel, et 4 chapitres des Livres 1 et 10 modifiés dans leur corps |
| empreintes de métadonnées divergentes | **39**, dont les 12 ci-dessus ; **27 n'ont changé que d'en-tête** — `renvois`, `verifications_en_attente`, `revision_de_fond` |
| champs `qualification` | **268 sur 268**, tous « fond, déclarée le 2026-09-07 » |
| ce qu'une exécution actuelle de `--maj-etat` en ferait | **sans option : les 268 sont perdus** ; avec `--editorial` ou `--fond` : **les 268 sont écrasés par la qualification du jour, et les 67 nouveaux la reçoivent aussi**, comme si une décision éditoriale avait été prise à leur création |

**Les douze divergences éditoriales, et ce que chacune est.** Toutes portent une
`revision_de_fond` déplacée ; **aucune ne portait de qualification pour ce
changement** — l'entrée d'état ne qualifiait que l'enregistrement du 7
septembre, et seuls le message de commit et la date déplacée disaient ce qui
s'était passé. **L'auteur les a validées comme changements de fond le
2026-09-10.** L'état les qualifie séparément, chacune sous la forme
`fond, revision_de_fond du <date du chapitre>, enregistrée tardivement le
2026-09-10` : **la date du changement est celle que le chapitre porte, et elle
est conservée ; seule l'inscription dans le fichier d'état est du 10
septembre**, et la qualification le dit.

| chapitre | ce qui a changé | décision de l'auteur, 2026-09-10 |
|---|---|---|
| L1.C15 | la proposition centrale est reformulée — « gagée sur une dissipation de stocks », énoncée en flux et stocks qui se comptent, avec sa condition de réfutation ; l'image passe du second principe à l'irréversibilité (`dc08c405`, 8 sept.) | **fond** — la seule des douze où le changement est une reformulation et non un ajout ; à regarder en premier |
| L1.C17 | l'adoption de la « quatrième loi » est retirée contre une source ouverte, la contrainte physique est déplacée, et l'objection du rebond reçoit son nom et sa littérature (`022ab83f`, `48de1301`, `fc25bd9c`, 8 sept.) | **fond** — une proposition retenue tombe |
| L1.C26 | l'arbitrage A32 est versé : abandon de la libre circulation inconditionnelle des capitaux, et ce qu'il coûte (`040582be`, 9 sept.) | **fond** |
| L10.C06 | l'unité est inscrite au passif de l'émetteur par décision de conception, et cette inscription est dite règle de conception, non qualification validée (`3b910108`, 9 sept.) | **fond** |
| L12.C01, L13.C01, L14.C01, L15.C01, L16.C01, L17.C01, L19.C01, L26.C01 | l'amorce du 7 septembre est remplacée par le chapitre d'ouverture réel — résumé et corps entièrement réécrits, de 1 650 à 3 230 caractères vers 8 700 à 15 100 (8 sept.) | **fond** — remplacement d'amorce, que chaque chapitre déclare lui-même |

**Aucune des douze n'est absorbée sans qualification.** Et un fait de
l'inventaire des métadonnées a été posé à l'auteur : **27 chapitres ont vu
`revision_de_fond` avancer sans que corps ni résumé changent** — renvois,
sources, vérifications en attente, annotations d'en-tête seules. **Tranché le
2026-09-10, par la convention elle-même** : `revision_de_fond` ne se modifie que
lorsque le sens change, jamais pour une reformulation, une coquille ou un ajout
de source. **Les 27 dates sont restaurées** à la dernière date de fond
antérieure au changement de métadonnées, **retrouvée dans la version historique
de chaque chapitre et non déduite de l'empreinte**, dans un commit distinct de
réparation de provenance (§ 9.5).

Les inventaires complets — 67 entrées absentes avec chemin, premier commit,
`revision_de_fond`, statut et empreintes ; 39 divergences de métadonnées avec
champs et commits — ont été remis à l'auteur le 2026-09-10. **Ils sont à
rejouer au moment de l'exécution** (§ 7.1, point 2) : les nombres ci-dessus
valent au commit `98713a0`.

### 9.2 Le comportement imposé à `controle.py` — dix propriétés, sans le modifier ici

| n° | propriété | nature |
|---|---|---|
| **P1** | une entrée existante **inchangée conserve sa `qualification`** | écriture |
| **P2** | une modification de **métadonnées seule** conserve la qualification antérieure | écriture |
| **P3** | `--editorial` ou `--fond` **ne qualifie que les entrées dont l'empreinte éditoriale a effectivement changé** — jamais les 335 | écriture |
| **P4** | une **nouvelle entrée** reçoit une qualification explicite : `initialisation, enregistrée le AAAA-MM-JJ` | écriture |
| **P5** | une initialisation **tardive** est nommée comme telle : `initialisation tardive, état antérieur non enregistré` — tardive quand le chapitre existait avant le jour de son premier enregistrement, ce qu'une `revision_de_fond` antérieure à ce jour établit sans appel à Git | écriture |
| **P6** | une **entrée absente** du fichier d'état apparaît dans le diagnostic — une ligne par chapitre, et le compte en tête | diagnostic |
| **P7** | une **entrée d'état sans chapitre** correspondant apparaît dans le diagnostic | diagnostic |
| **P8** | la publication d'un chapitre `verifie` ou `citable` **sans état enregistré est bloquée** — sous `--publier` | blocage |
| **P9** | une mise à jour d'état **ne peut jamais supprimer silencieusement** une qualification existante : la conservation est le défaut, et toute requalification est demandée explicitement | écriture |
| **P10** | **le test vérifie que seules les entrées visées changent** | test |

**Et une règle dérivée, que les douze imposent.** Une entrée dont l'empreinte
éditoriale a changé **et** dont `revision_de_fond` a été déplacée est un
changement de fond **déjà déclaré par le chapitre** — la convention réserve ce
déplacement au changement de sens. L'enregistrement la qualifie sans option :
`fond, revision_de_fond du <date>, enregistrée le <jour>`, et `enregistrée
tardivement le <jour>` si le jour est postérieur à la date. `--fond` et
`--editorial` ne servent qu'aux entrées dont l'empreinte a changé **à date
inchangée** — les décisions en attente —, et à elles seules (P3).

**Ce que ces propriétés changent au mécanisme.** Aujourd'hui l'enregistrement
**reconstruit le fichier entier** à partir des empreintes recalculées, et la
qualification n'est posée que par une option globale. Demain il **part du
fichier existant**, y reporte les qualifications, ne touche qu'aux entrées
visées, et **nomme ce qu'il initialise**. La différence est celle d'un registre
et d'un instantané.

### 9.3 L'invariant de non-régression, et les tests

**Invariant Q.** *L'ensemble des qualifications présentes avant une mise à jour
se retrouve après celle-ci, à l'identique, sauf pour les seules entrées dont la
requalification a été explicitement demandée.* Il est vérifié **par le script de
test sur des copies**, jamais sur le corpus, et **par le script de preuve sur le
commit de migration** (§ 8.4, invariant I8).

| test | ce qu'il établit |
|---|---|
| **T-Q1** | une entrée inchangée conserve sa qualification après `--maj-etat` (P1) |
| **T-Q2** | une entrée dont seul l'en-tête change la conserve (P2) |
| **T-Q3** | `--fond` sur une copie où un seul chapitre a changé de corps : **une seule** qualification change, les autres sont identiques octet pour octet (P3, P10) |
| **T-Q4** | un chapitre nouveau reçoit `initialisation, enregistrée le <jour>` ; un chapitre à `revision_de_fond` antérieure reçoit `initialisation tardive, état antérieur non enregistré` (P4, P5) |
| **T-Q5** | le diagnostic liste les entrées absentes et les entrées orphelines (P6, P7) |
| **T-Q6** | `--publier` refuse un chapitre `verifie` ou `citable` sans entrée d'état (P8) |
| **T-Q7** | aucune combinaison d'options ne fait disparaître une qualification sans requalification nominative (P9) |
| **T-Q8** | **sur le fichier réel, avant et après le commit de réparation** : 256 qualifications conservées, 12 requalifiées, 67 initialisées tardives — 335 entrées, aucune perdue |

Les tests vivent dans `corpus/test_etat.py`, à écrire, et s'exécutent sur des
copies dans un répertoire temporaire. **Un test qui passerait sur le script
actuel serait un test faux** : T-Q1 et T-Q7 doivent échouer aujourd'hui, et
c'est ainsi qu'on saura qu'ils mordent.

### 9.4 L'état de référence réparé — ce que le commit contient, et ce qu'il ne contient pas

Quatre commits préparatoires, autorisés par l'auteur le 2026-09-10, chacun
limité à son objet, chaque contrôle annoncé effectivement exécuté, et tous
distincts du commit de migration :

1. **le protocole**, seul ;
2. **la réparation de `controle.py` et ses tests**, verts sur copies —
   examinable seule ;
3. **la restauration des 27 `revision_de_fond`** (§ 9.5) — réparation de
   provenance, une ligne d'en-tête par chapitre ;
4. **l'état de référence** : `.etat-corpus.json` réécrit par le script réparé,
   sans option, avec le résultat attendu de T-Q8.

| entrées | qualification après réparation |
|---|---|
| 256 | conservée — « fond, déclarée le 2026-09-07 » ; dont 27 à en-tête modifié seulement, date de fond restaurée |
| 12 | « fond, revision_de_fond du <date du chapitre>, enregistrée tardivement le 2026-09-10 » — validées par l'auteur |
| 67 | « initialisation tardive, état antérieur non enregistré, enregistrée le 2026-09-10 » |
| **335** | **aucune perdue** |

**Ce que ces commits ne font pas.** Ils ne migrent aucune source et n'écrivent
pas `etat_lecture` ; les seuls chapitres touchés le sont sur une ligne
d'en-tête, par la restauration de provenance du § 9.5. Ils répondent au défaut
de l'état ; la migration répond au défaut des dates. **Les deux doivent pouvoir
être examinés séparément, et c'est pourquoi ils ne partagent pas un commit.**

### 9.5 La restauration des 27 dates de fond — réparation de provenance

**La règle est celle de la convention, § 4** : `revision_de_fond` ne se modifie
que lorsque le sens change. Les 27 chapitres ci-dessous ont vu leur date
avancer par des commits qui n'ont touché que l'en-tête — renvois, sources,
vérifications en attente. **La date n'est pas déduite de l'empreinte** : elle
est lue dans la **version historique** du chapitre, la dernière dont les
métadonnées sont celles que l'état a enregistrées, et **recoupée** avec la date
que portait le chapitre au dernier commit ayant changé son corps ou son résumé.
Les trois sources — version historique, dernier changement du corps, état
enregistré — concordent pour les 27.

| chapitre | fichier | avant (actuelle) | après (restaurée) | version historique | dernier changement du corps | déplacement |
|---|---|---|---|---|---|---|
| L1.C03 | c03-croissance-infinie-planete-finie.md | 2026-09-08 | **2026-09-03** | 5c04bb01 2026-09-07 | 259aa987 2026-09-05, revision alors 2026-09-03 | 022ab83f 2026-09-08 |
| L1.C08 | c08-pourquoi-la-dette-change-tout.md | 2026-09-08 | **2026-09-03** | 5c04bb01 2026-09-07 | 259aa987 2026-09-05, revision alors 2026-09-03 | 4184df67 2026-09-08 |
| L1.C10 | c10-une-monnaie-peut-elle-etre-concue-autrement.md | 2026-09-08 | **2026-09-03** | 5c04bb01 2026-09-07 | 259aa987 2026-09-05, revision alors 2026-09-03 | 4184df67 2026-09-08 |
| L1.C18 | c18-le-gaia-economic-symposium.md | 2026-09-08 | **2026-09-07** | 5c04bb01 2026-09-07 | b303d1f6 2026-09-07, revision alors 2026-09-07 | ecadaede 2026-09-08 |
| L7.C22 | c22-la-portee-du-livre.md | 2026-09-08 | **2026-09-06** | 5c04bb01 2026-09-07 | 93183f74 2026-09-06, revision alors 2026-09-06 | 2e050eab 2026-09-08 |
| L8.C34 | c34-l-economie-ecologique.md | 2026-09-08 | **2026-09-06** | 5c04bb01 2026-09-07 | 0b2140e9 2026-09-06, revision alors 2026-09-06 | fc25bd9c 2026-09-08 |
| L8.C37 | c37-la-macroeconomie-apres-2008.md | 2026-09-08 | **2026-09-06** | 5c04bb01 2026-09-07 | 0b2140e9 2026-09-06, revision alors 2026-09-06 | 563f57b0 2026-09-08 |
| L10.C07 | c07-ce-qu-une-banque-centrale-a-le-droit-d-acheter.md | 2026-09-08 | **2026-09-07** | 6b2534c1 2026-09-07 | 6b2534c1 2026-09-07, revision alors 2026-09-07 | 3f8399c4 2026-09-08 |
| L11.C01 | c01-reflux-ou-destruction.md | 2026-09-08 | **2026-09-07** | dae59a1c 2026-09-07 | dae59a1c 2026-09-07, revision alors 2026-09-07 | a2cd1860 2026-09-08 |
| L11.C02 | c02-le-trajet-complet-de-la-valeur.md | 2026-09-08 | **2026-09-07** | 1bff4337 2026-09-07 | 1bff4337 2026-09-07, revision alors 2026-09-07 | 292ca00e 2026-09-08 |
| L11.C07 | c07-le-demurrage-et-son-noeud.md | 2026-09-08 | **2026-09-07** | 73052fc3 2026-09-07 | 73052fc3 2026-09-07, revision alors 2026-09-07 | a2cd1860 2026-09-08 |
| L11.C09 | c09-l-incidence-qui-paie-le-reflux.md | 2026-09-08 | **2026-09-07** | 715b5742 2026-09-07 | 715b5742 2026-09-07, revision alors 2026-09-07 | 2d6711fe 2026-09-08 |
| L11.C10 | c10-la-trajectoire-de-mise-en-place.md | 2026-09-08 | **2026-09-07** | 5c04bb01 2026-09-07 | fbe618be 2026-09-07, revision alors 2026-09-07 | 9943a448 2026-09-08 |
| L11.C12 | c12-la-directive.md | 2026-09-08 | **2026-09-06** | 5c04bb01 2026-09-07 | 73032db3 2026-09-06, revision alors 2026-09-06 | 3c6df315 2026-09-08 |
| L11.C13 | c13-le-bareme-de-qualification.md | 2026-09-08 | **2026-09-07** | 292d490b 2026-09-07 | 292d490b 2026-09-07, revision alors 2026-09-07 | 113b97ed 2026-09-08 |
| L11.C24 | c24-le-bareme-aux-frontieres.md | 2026-09-08 | **2026-09-07** | 292d490b 2026-09-07 | 292d490b 2026-09-07, revision alors 2026-09-07 | 9943a448 2026-09-08 |
| L11.C27 | c27-l-assiette-de-la-fonte-est-celle-de-la-tva.md | 2026-09-08 | **2026-09-07** | 9d09ba1c 2026-09-07 | 9d09ba1c 2026-09-07, revision alors 2026-09-07 | e3810b91 2026-09-08 |
| L18.C01 | c01-ce-que-ce-livre-doit-etablir.md | 2026-09-08 | **2026-09-07** | e890ee01 2026-09-07 | e890ee01 2026-09-07, revision alors 2026-09-07 | cc4ab378 2026-09-08 |
| L18.C05 | c05-ce-que-la-norme-exclut-et-ce-n-est-pas-le-commun.md | 2026-09-08 | **2026-09-07** | 5c04bb01 2026-09-07 | 8ee9c692 2026-09-07, revision alors 2026-09-07 | f14a9afd 2026-09-08 |
| L18.C09 | c09-l-ordre-de-grandeur-et-le-concurrent-qu-il-designe.md | 2026-09-08 | **2026-09-07** | 70b1455e 2026-09-07 | 70b1455e 2026-09-07, revision alors 2026-09-07 | 113b97ed 2026-09-08 |
| L21.C01 | c01-ce-que-ce-livre-doit-etablir.md | 2026-09-08 | **2026-09-07** | 025c7cd1 2026-09-07 | 025c7cd1 2026-09-07, revision alors 2026-09-07 | 292ca00e 2026-09-08 |
| L21.C03 | c03-une-operation-de-bout-en-bout.md | 2026-09-08 | **2026-09-07** | b979d3d8 2026-09-07 | b979d3d8 2026-09-07, revision alors 2026-09-07 | 3f8399c4 2026-09-08 |
| L21.C07 | c07-portee-de-la-tranche.md | 2026-09-08 | **2026-09-07** | df6657a7 2026-09-07 | df6657a7 2026-09-07, revision alors 2026-09-07 | a35e3111 2026-09-08 |
| L22.C02 | c02-ou-va-la-monnaie-emise.md | 2026-09-08 | **2026-09-07** | 1bff4337 2026-09-07 | 1bff4337 2026-09-07, revision alors 2026-09-07 | 48de1301 2026-09-08 |
| L22.C04 | c04-les-criteres-reels-ne-mesurent-pas.md | 2026-09-08 | **2026-09-07** | 0ba5bb9e 2026-09-07 | 0ba5bb9e 2026-09-07, revision alors 2026-09-07 | 2e302605 2026-09-08 |
| L24.C01 | c01-ce-que-ce-livre-doit-etablir.md | 2026-09-08 | **2026-09-07** | e890ee01 2026-09-07 | e890ee01 2026-09-07, revision alors 2026-09-07 | d5815e8e 2026-09-08 |
| L25.C01 | c01-ce-que-ce-livre-doit-etablir.md | 2026-09-08 | **2026-09-07** | c4d2a269 2026-09-07 | c4d2a269 2026-09-07, revision alors 2026-09-07 | 183f69f1 2026-09-08 |

**La méthode d'écriture** : une seule ligne d'en-tête remplacée par chapitre,
sans re-sérialiser le YAML ; puis vérification que l'empreinte éditoriale de
chacun des 27 est inchangée et que le diff de chaque fichier tient en une ligne
retirée, une ligne ajoutée. **Un commit distinct, décrit comme réparation de
provenance, et il ne modifie ni corps ni résumé.**
