# Convention de production du corpus

**Révision 7 — 3 septembre 2026.** Journal des révisions en fin de document.

Ce fichier est déposé à la racine du corpus. Il fait autorité.

**Il n'existe pas de résumé de ce document.** Un aide-mémoire rédigé séparément
divergerait de la convention sans qu'aucun mécanisme ne le détecte — c'est le
problème que `verifiee_le` résout pour le livre 0, et qu'on ne saurait pas
résoudre ici. En cas de doute sur une règle, la réponse est dans ce fichier ou
n'existe pas.

Toute modification de la convention engage une migration scriptée des chapitres
déjà écrits, et l'incrément de la révision ci-dessus. Ne pas modifier sans les
deux.

---

## 1. Principe

Le Markdown est le format pivot. Tout le reste — pages HTML, index JSON,
`llms.txt`, glossaire, tables des matières, diagnostic — est généré par script
depuis les fichiers sources.

Règle absolue : **rien de ce qui peut être calculé n'est écrit à la main.**
L'auteur déclare les exceptions et les changements de sens. Le script calcule
tout le reste.

### Cible du lecteur

**Ce corpus est écrit pour un lecteur adulte, attentif, francophone, qui
accepte l'effort.** La convention protège la qualité du fragment extractible ;
elle ne protège pas la fluidité d'une lecture facile. Les IA qui restituent le
corpus à un lecteur donné sont libres d'ajuster leur registre à ce lecteur ;
les fichiers eux-mêmes s'adressent au premier public.

### Ce que le système garantit, et ce qu'il ne garantit pas

Trois plans distincts, à ne jamais confondre :

| Plan | Vérifiable par | Porté par |
|---|---|---|
| **Validité structurelle** | le script, entièrement | contrôle bloquant |
| **Fraîcheur documentaire** | le script, partiellement | alertes datées |
| **Justesse intellectuelle** | l'auteur seul | aucun champ |

Aucun champ de ce schéma n'atteste la justesse d'un chapitre. Un chapitre
`verifie` a des sources contrôlées et une structure cohérente. Rien de plus.

---

## 2. Arborescence

```
corpus/
  livres.yaml
  vocabulaire.yaml
  livre-00-<libellé>/
    c01-....md
  livre-01-monnaie-finance-limites-planetaires/
    c01-....md
  livre-06-droits-de-la-nature-et-des-ecosystemes/
    c05-environnement-sous-condition.md
```

Un fichier par chapitre. L'éclatement en plusieurs fichiers reste possible (§ 6)
mais n'est pas le cas normal.

**Nom du dossier de livre — forme arrêtée le 2026-09-07 (r10).** `livre-NN-<libellé>`,
où `NN` est **le matricule sur deux chiffres** et `<libellé>` un raccourci du titre
en minuscules sans accents. **Le matricule reste en tête et seul il identifie** :
le libellé n'est qu'une aide de lecture et **peut être corrigé si le titre change**,
la règle du § 3 ne portant que sur le numéro. **Le contrôle ne lit que le champ
`chapitre:` des en-têtes et globe `livre-*/`** : aucun outil ne dépend du libellé.

**Tous les matricules déclarés ont un dossier, et tout dossier a un chapitre —
arrêté le 2026-09-07 (r11).** Y compris les livres dont rien n'est écrit :
l'arborescence porte la collection entière. **Git ne suit pas les dossiers
vides**, et un marqueur en `.md` dépourvu de champ `chapitre:` **bloquerait le
contrôle**, qui globe `livre-*/*.md`. Chaque dossier sans chapitre reçoit donc
un **CHAPITRE D'AMORCE**, valide au regard du schéma.

**Régime du chapitre d'amorce.** Il porte toujours le matricule `C01` et le titre
« Ce que ce livre doit établir ». Il **rapporte** l'entrée du registre — titre,
collection, statut, fonction, motifs, architecture proposée — et **n'instruit
rien** : `regime: descriptif`, `concepts: []`, `renvois: []`, et ses
`verifications_en_attente` déclarent qu'aucune source n'est ouverte. **Il ne verse
aucun résultat au corpus et AUCUN AUTRE CHAPITRE NE DOIT LE CITER.** Son corps
s'ouvre sur la mention `**AMORCE.`, qui permet aux outils de le distinguer d'un
chapitre instruit.

**Il est REMPLACÉ, non complété.** Tous les livres ouverts commencent par un
chapitre « Ce que ce livre doit établir » qui instruit la fonction, la confronte
aux acquis des autres livres et fixe la grille du livre. **Ouvrir un livre, c'est
écrire ce chapitre-là à la place de l'amorce**, et `chapitres_acquis` reste à
zéro tant que l'amorce n'a pas été remplacée.

---

## 3. Identifiants et URL

L'identifiant de chapitre est **stable et définitif**. Il porte l'URL publique.

```
identifiant : L6.C05
URL         : /corpus/livre-6/c05-environnement-sous-condition/
```

Le nom de fichier peut changer, l'identifiant et l'URL non. Un identifiant n'est
jamais réattribué, même après suppression du chapitre.

### Le numéro de livre est un matricule

La collection de livres n'est pas close : elle se complète avec le temps. Le
numéro qui ouvre l'identifiant (`L7.C03`) est donc un **matricule**, non un rang.

- Il est attribué dans l'ordre de création, définitif, jamais réattribué.
- On ajoute toujours à la fin ; **on n'insère jamais, on ne renumérote jamais.**
  Renuméroter casserait toutes les URL publiées et tous les `renvois`.
- Un matricule **peut** être réservé pour un livre envisagé, à une condition
  stricte : **un matricule réservé est brûlé même si le livre n'est jamais
  écrit.** Il n'est pas rendu au stock et n'est jamais réattribué à un autre
  livre. Un livre abandonné laisse un trou dans la numérotation ; c'est le
  prix, et il est nul. Ce qu'interdit la règle, c'est l'insertion et la
  réutilisation, non la réservation.

Le numéro ne porte donc **ni ordre de lecture ni sens**. Ceux-ci vivent dans
`livres.yaml`, dans deux champs qui ne portent aucune URL et se réorganisent
librement à chaque passe : `collection` — la manière d'écrire, une par livre —
et `motifs` — pourquoi le livre existe, plusieurs par livre, de trois types
(`rouage`, `discipline`, `objection`). Un `motif` de type `objection` référence
une promesse du registre des promesses : une promesse non soldée qui ne figure
dans les motifs d'aucun livre est une promesse que personne n'a prise en charge.

`livres.yaml` joue pour le champ `livre` le rôle que `vocabulaire.yaml` joue
pour `concepts` : **un `livre` absent du registre bloque la publication.** Le
contrôle s'arrête là. Collections, motifs et statuts ne sont pas contrôlés :
ce sont des arbitrages éditoriaux, appelés à bouger d'une passe à l'autre, et
un script n'a pas à les figer.

### Le numéro de chapitre l'est aussi

La même règle vaut à l'intérieur d'un livre, et pour le même motif : le nombre
de chapitres n'est pas figé non plus.

- Un chapitre nouveau prend le numéro suivant. **On n'insère jamais un chapitre
  entre deux existants**, quand bien même la logique de lecture l'appellerait :
  la place d'un chapitre dans le raisonnement se dit par `renvois`, jamais par
  son numéro.
- Un chapitre abandonné laisse son numéro vacant. Il n'est pas réattribué.
- Le champ `chapitres_annonces` de `livres.yaml` est donc une **estimation
  courante, jamais une cible**. Un livre qui en compte plus que prévu n'est pas
  en défaut ; le registre est corrigé, et rien d'autre ne bouge.

Il en résulte que ni le nombre de livres ni le nombre de chapitres n'ont à être
arrêtés pour que le corpus soit publiable. C'est la propriété que l'ensemble du
dispositif d'identifiants existe pour garantir.

---

## 4. En-tête d'un chapitre

```yaml
---
# Identité — ne change jamais
chapitre: L6.C05
titre: "L'environnement sous condition"
livre: 6
langue: fr
licence: CC-BY-SA-4.0
type: chapitre              # chapitre | synthese

# État
statut: audit_factuel       # brouillon | audit_contradictoire
                            # | audit_factuel | verifie
revision_de_fond: 2026-09-02
autorite: canonique         # canonique | preparatoire
citable: true               # false pour tout document préparatoire

# Régime documentaire par défaut
regime: descriptif          # descriptif | hybride | conception

# Sourcing
sources_primaires:
  - ref: S1
    nature: jurisprudence   # normatif | jurisprudence | donnees
                            # | actualite | theorie
    reference: "WT/DS639/R"
    url: "https://www.wto.org/..."
    date_verification: 2026-08-28
  - ref: S2
    nature: donnees
    reference: "Eurostat env_ac_ainah_r2"
    url: "https://ec.europa.eu/..."
    date_verification: 2026-08-28
    horizon: 3m             # dérogation à l'horizon par défaut
    motif_horizon: "Série révisée trimestriellement"
verifications_en_attente:
  - "Dates DS639 (distribution, appel)"

# Restitution
resume: "Deux à quatre phrases énonçant ce que le chapitre établit."
concepts: [article_XX_GATT, PPM, MACF]
renvois: [L6.C06, L3.C02]
---
```

**Aucun numéro de version.** Le script calcule les empreintes (§ 5) et détecte
seul toute modification.

### Champs

Tout champ absent de cette table est un champ inconnu, et bloque (§ 12).

| Champ | Statut | Portée |
|---|---|---|
| `chapitre` | obligatoire | identifiant stable, porte l'URL |
| `titre` | obligatoire | |
| `livre` | obligatoire | entier |
| `langue` | obligatoire | code de langue |
| `licence` | obligatoire | identifiant de licence (défaut du corpus : `CC-BY-SA-4.0`) |
| `type` | obligatoire | `chapitre` \| `synthese` |
| `statut` | obligatoire | voir table des statuts |
| `revision_de_fond` | obligatoire | date, jugement éditorial |
| `autorite` | obligatoire | `canonique` \| `preparatoire` |
| `citable` | obligatoire | booléen |
| `regime` | obligatoire | régime par défaut du chapitre |
| `resume` | obligatoire | 2 à 4 phrases |
| `sources_primaires` | obligatoire | liste, vide admise en `brouillon` |
| `verifications_en_attente` | obligatoire | liste, vide admise |
| `concepts` | obligatoire | liste, vide admise en `brouillon` |
| `renvois` | obligatoire | liste, vide admise |
| `partie` | conditionnel | chapitre éclaté seulement (§ 7) |
| `chapitres_sources` | conditionnel | `type: synthese` seulement (§ 6) |
| `verifiee_le` | conditionnel | `type: synthese` seulement (§ 6) |

Champs d'une source primaire :

| Champ | Statut | Portée |
|---|---|---|
| `ref` | obligatoire | référence courte citée dans le texte : `[S1]` |
| `nature` | obligatoire | `normatif` \| `jurisprudence` \| `donnees` \| `actualite` \| `theorie` |
| `reference` | obligatoire | référence bibliographique ou juridique |
| `url` | optionnel | absent pour une source non disponible en ligne |
| `date_verification` | obligatoire | voir § 12 pour son double sens |
| `horizon` | optionnel | dérogation à l'horizon de la nature |
| `motif_horizon` | conditionnel | **obligatoire si `horizon` est présent** |

Listes vides et `brouillon` : un chapitre en brouillon peut avoir
`sources_primaires: []` et `concepts: []`. Le passage à `verifie` exige que les
deux soient renseignés — sans quoi le contrôle ne mordrait sur rien.

### `revision_de_fond` : un jugement, pas un calcul

Ce champ ne se modifie que lorsque le sens change : thèse révisée, conclusion
inversée, argument retiré. Jamais pour une coquille, une reformulation ou un
ajout de source.

C'est **le seul jugement éditorial que le système ne peut pas vérifier**.
L'empreinte prouve qu'un texte a changé ; elle ne peut pas prouver que le
changement est substantiel. Le diagnostic traite donc toute empreinte modifiée
sans qualification comme une **décision en attente**, pas comme un avertissement
mineur. Deux réponses possibles, aucune n'est de laisser en l'état : soit
`revision_de_fond` est mis à jour, soit le changement est déclaré éditorial.

### Statuts

| Statut | Signification |
|---|---|
| `brouillon` | en cours d'écriture, non publiable |
| `audit_contradictoire` | thèse et argumentation confrontées aux objections adverses ; les sources ne sont pas encore contrôlées |
| `audit_factuel` | audit contradictoire passé ; vérification des sources en cours |
| `verifie` | sources contrôlées et datées, structure cohérente — publiable |

`verifie` ne dit rien de la justesse du raisonnement. Le mot est choisi pour ne
pas suggérer davantage.

---

## 5. Empreintes

Le script calcule et stocke **deux empreintes distinctes** par chapitre. Aucune
ne s'écrit à la main.

**Empreinte éditoriale** — le texte du chapitre et son `resume`, normalisés.
C'est elle qui déclenche la question de la révision de fond et qui périme les
entrées du livre 0.

**Empreinte des métadonnées** — le reste de l'en-tête. Sa modification ne périme
rien : corriger une URL de source ou ajouter un renvoi ne change pas la thèse.

Sans cette séparation, toute correction de métadonnée déclencherait une alerte
de synthèse périmée, et les alertes deviendraient du bruit.

---

## 6. Entrée du livre 0

Même en-tête, avec trois différences.

```yaml
type: synthese
chapitres_sources: [L6.C05, L3.C02]
verifiee_le: 2026-09-02
```

`chapitres_sources` liste les chapitres résumés — une entrée transversale peut en
croiser plusieurs. Le nom est distinct de `sources_primaires`, qui désigne les
sources documentaires : ce ne sont pas les mêmes objets.

`verifiee_le` est la date à laquelle l'entrée a été confrontée à ses chapitres.
Le script la compare au `revision_de_fond` de chacun : si l'un est postérieur,
l'entrée est signalée comme périmée.

**Le livre 0 est une couche de réponse, pas une table des matières.** Chaque
entrée répond brièvement à une question, puis renvoie au chapitre qui démontre.
Elle doit tenir debout seule : c'est le seul endroit du corpus où la vue
d'ensemble est elle-même un passage extractible.

**Il s'écrit au fil de l'eau.** Dès qu'un livre est vérifié, ses entrées de
livre 0 sont rédigées dans la foulée. Ni avant — ce serait une promesse — ni à la
fin — ce serait une reconstitution de mémoire.

---

## 7. Chapitre éclaté (cas exceptionnel)

La première partie porte l'en-tête complet. Les suivantes un en-tête minimal :

```yaml
---
chapitre: L6.C05
partie: 2
---
```

Tout ce qui décrit le chapitre n'est déclaré qu'une fois, sur la partie 1. Le
script assemble dans l'ordre et signale toute partie orpheline.

---

## 8. Balises de régime

Le régime déclaré en en-tête est le régime par défaut. **On ne balise que les
paragraphes qui s'en écartent.**

```markdown
Le règlement MACF entre en application progressive à partir de 2026. [S1]

::hypothese:: Dans une architecture NEMO, ce mécanisme deviendrait inutile, la
contrainte étant portée par l'unité de compte elle-même.

::norme:: Il faudrait subordonner l'accord commercial à la comptabilité
biophysique, et non l'inverse.

::etat:: Retour au descriptif après une série de paragraphes marqués.
```

Trois marqueurs, pas davantage. Le script les convertit en attribut sur le
paragraphe et les retire du texte affiché — le régime voyage donc avec le
passage lorsqu'une IA l'extrait isolément.

Ne pas enrichir cette liste : des catégories aux frontières floues produisent des
marquages incohérents en quelques mois.

---

## 9. Vocabulaire

`vocabulaire.yaml`, à la racine. Une entrée par concept.

```yaml
- terme: article_XX_GATT
  libelle: "Article XX du GATT"
  definition: "Clause d'exception générale permettant de déroger aux règles
               commerciales pour des motifs limitativement énumérés."
  premiere_occurrence: L6.C05
```

Vocabulaire fermé, ouvert à l'ajout. Un concept employé sans figurer ici
**bloque** la publication. Le déblocage passe par l'écriture de l'entrée,
définition comprise.

Cette friction est volontaire : c'est en rédigeant la définition qu'on s'aperçoit
qu'on vient de rebaptiser un concept existant.

Ce fichier sert aussi de glossaire publié.

---

## 10. Habitudes de rédaction

Ni vérifiables ni rattrapables par script. Les seules choses que le système ne
peut pas faire à votre place.

**Chaque chapitre s'ouvre sur ce qu'il établit**, en deux ou trois phrases. Pas
d'accroche, pas de suspense rhétorique. Même logique par paragraphe.

**Chaque sigle est redéfini à sa première occurrence dans le chapitre**, sans
supposer les chapitres précédents lus. « Comme nous l'avons vu » ne veut rien
dire pour un passage extrait isolément.

**Chaque concept garde le même nom partout**, celui du fichier de vocabulaire.

**Chaque métaphore utile va entre parenthèses en italique, préfixée `Image :`**,
immédiatement après le passage qu'elle illustre. Le corps reste dans le registre
académique. L'IA qui restitue le corpus à un lecteur novice peut s'appuyer sur
l'image ; celle qui répond à un expert peut l'ignorer. Sans ce marqueur, une
image extraite isolément serait lue comme un argument.

```markdown
La finance a acquis une capacité d'orientation qui excède son mandat historique
de facilitation des échanges. (*Image : elle est devenue une reine, non plus
une servante.*)
```

Raison commune : une IA ne lit jamais le corpus entier. Elle en extrait trois ou
quatre passages et répond à partir d'eux. Chaque passage doit tenir debout seul.

---

## 11. Boucle de production

1. **Rédiger** le chapitre, en-tête compris, `statut: brouillon`.
2. **Ajouter au vocabulaire** tout concept nouveau, au moment où il apparaît.
3. **Audit contradictoire** — confronter la thèse aux objections adverses.
   Passer à `audit_contradictoire`.
4. **Vérifier les sources** une par une, renseigner `date_verification`.
   Passer à `audit_factuel` pendant, `verifie` après. C'est le goulot
   d'étranglement du corpus, et il ne s'élargit pas avec l'outillage : une
   référence plausible n'est pas une référence vérifiée.
5. **Rédiger les entrées de livre 0** correspondantes, dans la foulée.
6. **Contrôle structurel.** Corriger tout ce qui bloque.
7. **Génération locale** — pages, index, diagnostic, en aperçu.
8. **Revue humaine** du rendu et du diagnostic. Traiter les décisions en
   attente, arbitrer les alertes.
9. **Publier.**

La génération n'est pas la dernière étape : elle fournit la matière de la
dernière vérification humaine.

**Revue périodique.** Indépendamment de l'écriture, traiter les revues dues
signalées au diagnostic : rouvrir la source, constater son état, mettre à jour
`date_verification` — y compris, et surtout, quand rien n'a changé.

Le corpus est alimenté au fil de l'eau — l'application est lancée avec les
premiers livres et s'enrichit à chaque ajout. Le script régénère intégralement
les index à chaque exécution ; ajouter un livre ne demande aucune modification de
code.

---

## 12. Contrôle

Le script est l'autorité. Il s'exécute en ligne de commande et **refuse la
publication** en cas d'erreur bloquante. La page de diagnostic n'est que sa
sortie lisible.

### Bloquant — validité structurelle

- identifiant de chapitre dupliqué
- renvoi vers un chapitre inexistant
- concept absent du vocabulaire
- source primaire sans `date_verification` ou sans `nature`
- partie orpheline (`partie: 2` sans partie 1)
- en-tête incomplet, ou **champ inconnu**
- statut `verifie` avec `verifications_en_attente` non vide
- `citable: true` sur un chapitre dont le statut n'est pas `verifie`
- **génération publique demandée pour un chapitre dont le statut n'est pas
  `verifie`, ou dont `citable` est `false`** — les marqueurs d'état n'ont de
  valeur que s'ils ont un effet mécanique

Le blocage sur champ inconnu est délibéré : un champ toléré parce qu'inconnu est
une dérive silencieuse. Toute évolution du schéma passe par une migration
scriptée sur l'ensemble du corpus, en une fois.

### Décisions en attente — à trancher, pas à ignorer

- empreinte éditoriale modifiée sans que `revision_de_fond` ait bougé :
  qualifier en révision de fond, ou déclarer le changement éditorial

Tant qu'une décision est en attente, `--maj-etat` **refuse d'enregistrer l'état**.
Sans ce refus, enregistrer l'empreinte ferait disparaître la décision sans qu'elle
ait été tranchée : le geste censé consigner un arbitrage permettrait de s'en
dispenser. Deux réponses sont possibles, et le silence n'en est pas une.

| Situation | Réponse |
|---|---|
| Changement de sens, à une date postérieure à `revision_de_fond` | mettre à jour `revision_de_fond`, puis `--maj-etat` |
| Changement de sens, le même jour que `revision_de_fond` | `--maj-etat --fond` |
| Changement éditorial | `--maj-etat --editorial` |

Le cas du même jour existe parce que `revision_de_fond` a une granularité
journalière : une seconde révision substantielle survenue le jour même ne peut pas
s'y inscrire. `--fond` la déclare explicitement et l'inscrit dans l'état, avec sa
date. Les deux drapeaux s'excluent.

`--editorial` est une déclaration explicite, portée par la personne qui la fait.
Le script ne peut pas distinguer une coquille corrigée d'une thèse révisée ; il peut
seulement exiger que quelqu'un le dise.

### Alertes — fraîcheur documentaire

Les horizons de revérification ne sont pas inscrits dans cette convention : ils
vivent dans `horizons.yaml`, à la racine du corpus, et se révisent sans migration.

```yaml
# Valeurs par défaut. À ajuster à mesure que l'expérience s'accumule.
# mode: date  → le script constate l'âge de la source
# mode: revue → le script constate l'ancienneté de la dernière revue humaine
normatif:
  mode: revue
  horizon: 1a
  motif: "Vérifier que le texte est toujours en vigueur, non sa date."
jurisprudence:
  mode: revue
  horizon: 1a
  motif: "Vérifier l'absence d'appel, de révision ou de renversement."
donnees:
  mode: date
  horizon: 1a
  motif: "Séries révisées ; horizon à déroger source par source."
actualite:
  mode: date
  horizon: 9m
  motif: "Fait rapporté durable, mais état de la situation vite périmé."
theorie:
  mode: date
  horizon: aucun
  motif: "Travaux stabilisés ; revérifier sur controverse signalée."
```

`date_verification` porte les deux sens selon le mode : date de contrôle de la
source pour `mode: date`, date de dernière revue pour `mode: revue`. C'est le
même geste, et il n'appelle pas un second champ.

**Une revue qui ne constate aucun changement met tout de même la date à jour.**
C'est la seule règle qui fait tenir le mécanisme : si la date ne bouge qu'en cas
de changement, elle cesse de mesurer la surveillance pour ne mesurer que les
modifications, et le diagnostic finit par signaler comme non surveillées des
sources revues la semaine précédente.

Le message du diagnostic diffère en revanche, parce que l'action attendue
diffère : **« contenu potentiellement périmé »** en mode date, **« revue due,
sans changement connu »** en mode revue. La seconde ne prétend rien sur l'état
de la source — elle constate que personne ne l'a regardée depuis l'horizon fixé.
C'est la séparation entre ce que le système sait et ce qu'il demande seulement
d'aller voir.

Aucune source n'échappe donc au contrôle. L'incapacité à vérifier
automatiquement est elle-même devenue une donnée surveillée.

Une source peut déroger à l'horizon de sa nature via `horizon` et
`motif_horizon` (§ 4). Le motif est obligatoire : une dérogation sans
justification est un horizon arbitraire de plus.

**Le diagnostic affiche toujours l'horizon appliqué et son motif**, jamais un
simple « source ancienne ». Un délai dont on ne voit pas la raison devient un
dogme caché, appliqué par habitude et jamais révisé.

Autres alertes :

- entrée de synthèse dont un chapitre source a été révisé sur le fond depuis
  `verifiee_le`
- chapitre en brouillon depuis plus de trois mois
- concept déclaré au vocabulaire et employé nulle part
- `verifications_en_attente` non vide sur un chapitre non `verifie`

Ne jamais déclasser une règle bloquante en alerte pour se débloquer. Une alerte
ignorée est une alerte inutile, et un système qui continue de fonctionner en
donnant une fausse impression de rigueur est pire qu'un système qui s'arrête.

---

## 13. Ce que le script génère

Aucun de ces fichiers ne s'écrit ni ne se modifie à la main.

- les pages HTML du corpus, avec hiérarchie de titres et JSON-LD
- le fichier `.md` servi à côté de chaque page
- les index de recherche, **un par livre** (un index unique deviendra trop lourd)
- l'index global léger : identifiants, titres, résumés, concepts
- les tables des matières par livre
- le `sitemap.xml`, avec les équivalences de langue
- les entrées du `llms.txt`
- le glossaire, depuis `vocabulaire.yaml`
- les deux empreintes de chaque chapitre
- la page de diagnostic, en trois sections distinctes : blocages, décisions en
  attente, alertes de fraîcheur — chaque alerte de fraîcheur portant l'horizon
  appliqué, son motif, et son origine (défaut de nature ou dérogation)

---

## 14. Publication et pérennité

Le corpus est publié en section non listée dans la navigation. Ce n'est pas
indexable en soi : l'indexation suppose que les URL figurent au `sitemap.xml`,
qu'au moins un lien y mène, et qu'aucune règle du `robots.txt` ni balise
`noindex` ne bloque le répertoire. À vérifier explicitement, les trois.

**Licence.** Le corpus est publié sous **Creative Commons Attribution — Partage
dans les Mêmes Conditions 4.0 International (CC-BY-SA 4.0)**. Chaque chapitre
porte le champ `licence` dans son en-tête (§ 4). Cette licence est irrévocable
pour les versions déjà publiées : elle protège le corpus contre l'enclosure
sans en restreindre la circulation. La clause « Share-Alike » impose à tout
dérivé d'être publié sous la même licence — la propagation du commun se fait
par le mécanisme même de la licence, sans surveillance.

Points ouverts, à trancher hors routine :

- dépôt d'archive avec identifiant permanent, miroirs, dépôt légal
- successeur désigné par écrit, détenant droits, domaine et accès
- renouvellement du nom de domaine — la cause de disparition la plus probable,
  et la plus banale

---

## 15. Journal des révisions

**Révision 11 — 7 septembre 2026.** Tous les matricules déclarés ont un dossier,
et tout dossier a un chapitre (§ 2), sur demande de l'auteur. **Cette révision
CORRIGE la révision 10 du même jour**, qui énonçait l'inverse — « les dossiers de
livres non ouverts n'existent pas tant qu'aucun chapitre n'est écrit ».
**Quatorze dossiers créés, quatorze CHAPITRES D'AMORCE déposés**, dont le régime
est fixé au § 2 : descriptif, sans concept ni renvoi, non citable, **remplacé et
non complété** à l'ouverture du livre. Un marqueur `.md` sans champ `chapitre:`
aurait bloqué le contrôle ; un marqueur non `.md` n'aurait pas fait du dossier un
livre. **Aucun contenu de chapitre existant n'est touché** ; le contrôle passe sur
241 chapitres, dont 14 d'amorce. **`chapitres_acquis` reste à zéro pour ces
quatorze livres** : une amorce n'est pas un acquis.

**Révision 10 — 7 septembre 2026.** Les dossiers de livres portent désormais leur
intitulé après le matricule (§ 2), sur demande de l'auteur, pour la lisibilité de
l'arborescence. **Migration scriptée par `git mv` sur les douze dossiers
existants ; aucun contenu modifié, aucun matricule touché, aucun identifiant de
chapitre changé.** Le contrôle globe `livre-*/` et lit le champ `chapitre:` : il
passe sans modification. **Le matricule demeure seul identifiant** — le libellé
est une aide de lecture, corrigeable, et la règle du § 3 ne porte que sur le
numéro.

| Rév. | Date | Objet | Migration |
|---|---|---|---|
| 1 | 2026-09-02 | Version initiale : schéma, régimes, vocabulaire, contrôle | — |
| 2 | 2026-09-02 | Empreintes calculées en remplacement du numéro de version ; `revision_de_fond` ; `chapitres_sources` ; statut `verifie` ; horizons par nature dans `horizons.yaml` ; séparation des trois plans ; boucle réordonnée | aucun chapitre écrit |
| 3 | 2026-09-02 | Table des champs obligatoires et optionnels ; blocage de la génération publique hors `verifie` ; règle de non-duplication de la convention | L1.C01 uniquement |
| 4 | 2026-09-03 | Blocage de `citable: true` hors statut `verifie` — un marqueur d'état qui peut mentir ne protège rien | L1.C01 uniquement |
| 5 | 2026-09-03 | `--maj-etat` refuse d'enregistrer tant qu'une décision est en attente ; option `--editorial` pour déclarer un changement non substantiel | aucune |
| 6 | 2026-09-03 | Option `--fond` : déclare une révision substantielle survenue le même jour que la `revision_de_fond` en cours, que le champ ne peut pas enregistrer seul | aucune |
| 7 | 2026-09-03 | Champ `licence` obligatoire, `CC-BY-SA-4.0` par défaut ; cible du lecteur explicitée en § 1 ; patron des métaphores restituables ajouté en § 10 (`(*Image : ...*)`) ; § 14 licence traitée | 7 chapitres existants migrés |
| 9 | 2026-09-04 | Règle du matricule étendue aux numéros de chapitre : ni le nombre de livres ni celui de chapitres n'est figé ; on ajoute toujours à la fin, `chapitres_annonces` est une estimation et non une cible | aucun chapitre modifié |
| 8 | 2026-09-04 | Registre des livres `livres.yaml` : le numéro de livre est un matricule, jamais un rang — ni insertion ni renumérotation ni réattribution ; un matricule réservé est brûlé même si le livre n'est pas écrit ; sens et ordre portés par `collection` et `motifs`, non contrôlés ; un `livre` absent du registre bloque la publication ; registre aligné sur le plan directeur de l'auteur, dix-neuf matricules de 0 à 18 | aucun chapitre modifié |

Toute révision ultérieure s'inscrit ici avant d'être appliquée, avec la portée
de la migration qu'elle entraîne. Une révision non journalisée est une dérive
silencieuse, exactement ce que le blocage sur champ inconnu existe pour empêcher.
