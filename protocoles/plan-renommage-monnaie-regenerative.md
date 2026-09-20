# Plan d'application — « monnaie régénérative à contrepartie collective »

**Décision d'auteur du 2026-09-20.** Nom canonique :

> **monnaie régénérative à contrepartie collective**

Définition de travail à stabiliser :

> Monnaie émise pour financer ou rémunérer une prestation régénérative, inscrite
> au passif de l'émetteur, dont la contrepartie et le reflux sont organisés
> collectivement plutôt que par une créance individualisée contre son
> bénéficiaire.

**Rien n'est écrit.** Ce document est le plan demandé avant toute écriture. La
cartographie est faite ; les lots sont dimensionnés ; **quatre décisions bloquent
le lot 1**, et une cinquième porte sur une fenêtre qui se referme.

Cartographie produite par `outils_claude/cartographie_sans_dette.py` — il relève
et ne juge pas.

---

## 0. Ce que la cartographie a trouvé

| | |
|---|---|
| occurrences de « sans dette », tout le dépôt | **287** |
| dont **voix propre, hors archive** — à relire à l'œil | **199** |
| dont dans les **corps de chapitres** | **54**, dans **23 chapitres** |
| entrée de vocabulaire pour le concept | **aucune** — il faut la créer, non la remplacer |

**Les formes ne se valent pas, et c'est le premier problème.**

| forme | occurrences | ce que le nouveau nom en fait |
|---|---|---|
| « émission sans dette » | **112** | **rien** — voir D1 |
| « monnaie sans dette » | 27 | remplacée directement |
| « monnaie émise sans dette » | 13 | remplacée directement |
| « argent sans dette » | 7 | remplacée directement |
| « création monétaire sans dette » | 5 | **rien** — voir D1 |

**Densité par chapitre** (corps, voix propre) : L1.C20 **13** · L11.C01 5 ·
L1.C18 4 · L1.C19 3 · L1.C22 3 · L8.C06 3 · L1.C08 2 · L1.C29 2 · L8.C24 2 ·
L8.C38 2 · L10.C07 2 · L18.C05 2 · puis onze chapitres à une occurrence.

---

## 1. Les cinq décisions qui précèdent toute écriture

### D1 — Que devient « émission sans dette » ? **C'est la forme dominante, et le nouveau nom ne la couvre pas.**

Le nom arrêté désigne **la monnaie**. « Émission sans dette » désigne **l'acte**,
et il compte **112 occurrences** — quatre fois plus que « monnaie sans dette ».

Trois branches, et le corpus ne doit pas en inventer une quatrième en silence :

- **(a)** « émission de monnaie régénérative à contrepartie collective » —
  exact, lourd, et impraticable en usage courant ;
- **(b)** une forme courte à arrêter, du type « émission à contrepartie
  collective » — **elle serait neuve et n'existe dans aucune source** ;
- **(c)** « émission sans dette » **conservée** comme nom de l'acte, le nouveau
  nom ne portant que la monnaie. Cohérent si l'on tient que « sans dette »
  décrivait mal la monnaie mais décrit bien l'acte — l'émission ne crée
  effectivement aucune créance bilatérale.

**Sans D1, les lots 1 à 3 ne peuvent pas commencer** : 112 des 287 occurrences en
dépendent, et le chapitre porteur en dépend d'abord.

### D2 — Le **Livre 19 porte l'ancien nom dans son intitulé**

Son dossier est `livre-19-comptabilite-monetaire-de-l-emission-sans-dette`, et
son titre au registre est « Comptabilité monétaire de l'émission sans dette ».
Dix chapitres.

**Le coût est plus faible qu'il n'y paraît, et il faut le dire :** le générateur
construit les URL sur `livre-{numéro}/{slug-du-chapitre}/` — **le nom du dossier
n'entre dans aucune URL**. Le renommer est une opération interne, sans effet
public. Reste le **titre** au registre, qui est un acte éditorial.

D2 dépend de D1 : si « émission sans dette » est conservée (branche c), le titre
du Livre 19 ne bouge pas.

### D3 — Les **pages publiées du site** portent le terme

`articles/auteur/essentiel-insolvable-comment-le-financer/index.html` (6
occurrences) et `articles/auteur/SMI-4/index.html` (4), plus quelques autres.

**Ce n'est pas le corpus.** Modifier une page publiée est un acte public et
daté, pas une correction éditoriale interne. Trois branches : les laisser ; les
corriger avec une note de mise à jour ; les corriger silencieusement — **la
troisième est écartée d'office**, elle réécrirait un état public sans trace.

### D4 — **L1.C29 est verrouillé et attend une seconde passe de supervision**

Le point de rendez-vous de la veille porte `chapitre_verrouille: L1.C29` et
`prochain_acteur: Codex`. Or **L1.C29 figure dans la liste de propagation**.

Réécrire C29 maintenant briserait la règle « un seul acteur modifie un chapitre à
la fois » et **périmerait la passe demandée**, qui porte sur un état gelé.
Deux branches : solder la passe d'abord, puis propager ; ou retirer C29 du verrou
et annuler la seconde passe.

### D5 — **Une fenêtre se referme, et elle est étroite**

Le générateur n'émet que les chapitres `verifie`, `citable: true` et à sources
toutes ouvertes. **Huit chapitres seulement sont dans ce cas** : L1.C07, C08,
C09, C11, C12, C15, C16, C31.

**L1.C20 n'en fait pas partie.** Son fichier `c20-de-l-argent-sans-dette.md`
n'a donc **aucune URL publique aujourd'hui**. Le renommer est gratuit.

**Il ne le sera plus.** La convention § 3 pose que « le nom de fichier peut
changer, l'identifiant et l'URL non » — mais le générateur dérive le slug d'URL
**du nom de fichier**. Une fois C20 publié, renommer son fichier changerait son
URL, ce que la convention interdit.

**Ce défaut est signalé et non corrigé** : la convention et le générateur se
contredisent sur ce point, et l'arbitrage n'appartient pas à ce plan.

---

## 2. Les lots, une fois les décisions rendues

Chaque lot est **isolé et commitable**, avec ses contrôles. Aucun ne commence
avant que le précédent ne passe.

### Lot 1 — le noyau canonique *(dépend de D1)*

- **Créer** l'entrée de `corpus/vocabulaire.yaml` sous un identifiant stable —
  proposition : `monnaie_regenerative_contrepartie_collective`, avec la
  définition de travail et `premiere_occurrence: L1.C20`.
- **L1.C20** : titre, chapeau, définition initiale, métadonnées. **13
  occurrences dans le corps.** Le fichier n'est **pas** renommé dans ce lot.
- Contrôles : `controle.py`, `--maj-etat --fond`, les trois tests.

### Lot 2 — la propagation argumentative *(dépend de D1 et D4)*

Les chapitres qui portent le concept **comme thèse**, par densité : L11.C01,
L1.C18, L1.C19, L1.C22, L1.C08, L1.C29, L1.C21, L1.C10, L1.C11, L1.C01.

**La règle d'écriture, et elle vaut correction de fond.** Toute formule absolue
du type « aucune dette » se décompose en **trois plans distincts** :

1. **passif de l'émetteur** — l'unité y est inscrite ;
2. **absence de créance bilatérale individualisée** contre le bénéficiaire ;
3. **contrepartie et reflux collectifs**.

**La réserve est conservée explicitement** : les écritures précises et la
répartition institutionnelle du prélèvement restent à spécifier avant
déploiement. **Ce n'est pas un blocage conceptuel**, et le corpus ne doit pas le
présenter comme tel.

### Lot 3 — les chapitres qui mentionnent sans thèse

L8.C06, L8.C24, L8.C38, L10.C07, L18.C05, L2.C19, L11.C02, L11.C03, L11.C26,
L17.C01, L20.C02, L21.C03. Une à trois occurrences chacun, souvent un renvoi.

**Deux d'entre eux ANALYSENT le terme et ne doivent pas être renommés** :
L20.C25 titre une section « Mais cela ne sauve pas l'“émission sans dette” », et
L19.C05 écrit « “sans intérêt” tombe, comme “sans dette” ». **Renommer là
détruirait l'analyse.**

### Lot 4 — registre, protocoles et coordination

- Inscrire la décision de renommage et sa définition dans le registre adéquat —
  **`protocoles/registre-canonique-nemo-ims.md`**, dont c'est exactement l'objet,
  et **non** `corpus/vocabulaire.yaml`, qui porte les concepts. La séparation a
  été arrêtée le 2026-09-19 et ce lot la respecte.
- `corpus/livres.yaml` (9 occurrences), `protocoles/falsification.md` (15),
  `protocoles/registre-des-promesses.md` (9), les architectures.
- **`protocoles/falsification.md` demande une attention propre** : un falsifieur
  énonce une condition d'échec. En changer les mots change ce qui est testé.

### Lot 5 — archives : **erratum, jamais réécriture**

`passe-2.md`, les rapports d'audit, `BILAN_*`, `JOURNAL_DES_RELAIS.md`.
**24 occurrences en archive.** Une note datée en tête suffit ; réécrire
falsifierait l'historique.

### Lot 6 — renommages de chemins *(dépend de D2 et D5, irréversible)*

- `c20-de-l-argent-sans-dette.md` → nouveau slug, **si D5 conclut à saisir la
  fenêtre**.
- Dossier du Livre 19, **si D2 le décide**.
- **Avant tout renommage** : recenser les liens internes qui dépendent du chemin,
  puis les vérifier après.

### Lot 7 — site *(dépend de D3)*

Séparé de tout le reste, parce qu'il est public.

---

## 3. Contrôles, et le dossier de gel

À chaque lot : `controle.py`, `--maj-etat` en dernier des écritures mais **avant**
les tests, puis `test_etat`, `test_lecture`, `test_generer`. Après tout
renommage, vérifier les liens.

**Contrôle final propre à ce chantier** : relancer
`cartographie_sans_dette.py` et vérifier qu'aucune occurrence **canonique** ne
subsiste hors citation, archive, ou section qui analyse explicitement le terme
comme ancien.

Puis geler un dossier compact pour la supervision —
`outils_claude/dossier_codex.py` — avec le diff, la définition, la liste des
occurrences traitées, les contrôles et les faiblesses restantes.

**Ni poussée ni archive.**

---

## 4. Ce que ce plan ne fait pas

Il ne tranche aucune des cinq décisions. Il ne réécrit aucune citation. Il ne
touche à aucun document historique. Il ne renomme rien avant D2 et D5. Et il
**n'invente pas la forme courte de D1(b)** : si cette branche est retenue, la
formule vient de l'auteur.
