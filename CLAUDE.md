# CLAUDE.md — repères de travail pour Claude Code

Ce fichier oriente une session Claude qui ouvre le dépôt. Il ne se substitue
à aucun document existant : il pointe vers eux et signale les écarts entre ce
que la convention décrit et ce que le dépôt implémente aujourd'hui.

## Documents faisant autorité

**Travail en cours — depuis le 2026-09-21, le seul fichier qui distribue les
tâches est `coordination/ORDRE_DU_JOUR.md`** (dépôt privé, exclu de celui-ci) :
lire son « Point d'entrée », chercher son propre nom, exécuter ses ordres et rien
d'autre, rendre compte en bas. `coordination/FILE_DE_TRAVAIL.yaml`,
`ETAT_DU_CORPUS.md`, `JOURNAL_DES_RELAIS.md` et `veille-nuit.md` sont des
archives. Un état se lit dans le fichier du chapitre et dans `git log`, jamais
dans une note.

Lire dans cet ordre avant toute modification :

1. [corpus/convention.md](corpus/convention.md) — schéma, statuts, empreintes,
   contrôle. **Autorité sur tout ce qui touche au corpus.** Aucun résumé
   n'existe et ne doit être écrit : cf. son préambule. Révision courante : r14
   (l'URL publique ne dérive que de l'identifiant, `/corpus/livre-6/c05/` — § 3 ;
   r13 : vérification des exemplaires par un outil séparé et facultatif,
   `corpus/verifier-exemplaires.py`, hors du chemin de publication — § 12 ;
   r12 : champ `etat_lecture` sur chaque source — `candidate`, `ouverte`,
   `a_requalifier` —, `date_verification` conditionnel, manifeste des
   occurrences historiques `corpus/manifeste-etat-lecture.json` lu par le
   contrôle, état enregistré conservateur ; r9 : licence CC-BY-SA-4.0
   obligatoire, cible du lecteur explicite, patron des métaphores restituables
   `(*Image : ...*)`, registre des livres `livres.yaml` et règle du matricule
   en § 3).
2. [AGENTS.md](AGENTS.md) — routine de publication. **Ne jamais commiter,
   pousser ni archiver sans validation explicite de l'utilisateur.**
3. Pour le site hors corpus : [GUIDE-PUBLIER-CONTENU.md](GUIDE-PUBLIER-CONTENU.md),
   [INTEGRATION-ASSISTANT.md](INTEGRATION-ASSISTANT.md),
   [KNOWLEDGE-BASE.md](KNOWLEDGE-BASE.md).
4. [protocoles/](protocoles/) — textes à coller pour les modèles tiers :
   `audit-contradictoire.md` (Gemini normal / ChatGPT, jamais Claude seul) et
   `sourcage-deep-research.md` (Gemini Deep Research sur les
   `verifications_en_attente`). **Ce qu'ils rapportent est une piste, jamais une
   vérification** — cela vaut pour tout résumé produit par un modèle, y compris
   un outil qui « récupère » une page en la faisant résumer. **MODIFIÉ le
   2026-09-06 par l'auteur** : Claude peut désormais télécharger une source,
   l'ouvrir, juger son édition et la porter lui-même à `etat_lecture: ouverte`
   avec sa `date_verification`, à condition de lire le TEXTE et non un résumé.
   L'entrée de source porte alors `OUVERT PAR TÉLÉCHARGEMENT DIRECT` avec
   l'URL. Un scan sans couche de texte reste non ouvert, et une source
   sélectionnée mais non lue reste `candidate`, sans date. `a_requalifier` est
   réservé aux occurrences historiques du manifeste : jamais pour une source
   nouvelle. Voir la section « Tenue de cette liste » de
   `sources-a-ouvrir.md`.
   `registre-des-promesses.md` tient les objections que la première partie du
   Livre 1 renvoie à la seconde ; à solder en passe 2, une ligne par promesse.
   `falsification.md` tient les conditions explicites sous lesquelles la thèse
   échoue — posées avant que les réponses arrivent, parce que l'auteur attend de
   ce corpus un verdict qui peut être négatif. Ne jamais présenter une objection
   déplacée comme résolue.
   `passe-2.md` tient ce qui a été délibérément reporté — décisions prises à ne
   pas rouvrir, corrections à propager, tensions entre le corpus et le livre.
   **Le livre fait autorité sur les fichiers d'adaptation** : ceux-ci contiennent
   des états antérieurs de la pensée. Lire le chapitre du livre avant de
   convertir un texte source.

## Deux sous-systèmes distincts

- **`corpus/`** — Markdown à en-tête YAML, sous convention stricte, contrôlé
  par script. Toutes les règles sont dans `corpus/convention.md`. La collection
  de livres est ouverte : `corpus/livres.yaml` déclare les matricules existants
  et les livres candidats, sans numéro.
- **Reste du dépôt** — site statique historique : `index.html`, `livre/`,
  `manifeste/`, `articles/`, `articles.json`, `news.json`, `feed.xml`,
  `sitemap.xml`, versions linguistiques `ar/ de/ en/ es/ it/ pt/`. Le corpus
  n'y est pas encore relié.

## Commandes du corpus

Dépendance unique : `PyYAML`, épinglée dans `corpus/requirements.txt`
(6.0.3, constatée le 2026-09-10 sur Windows 11, Python 3.14.5 — la seule
plateforme testée).

```bash
python -m pip install -r corpus/requirements.txt                                   # voie connectée
python -m pip install --no-index --find-links corpus/hors-ligne -r corpus/requirements.txt  # voie hors ligne
python corpus/test_environnement_propre.py                                          # test en environnement propre
```

La voie hors ligne repose sur l'artefact de `corpus/hors-ligne/` — roue,
empreinte SHA-256 dans `SHA256SUMS` et vérifiée mécaniquement avant toute
installation, licence MIT et notice dans `NOTICE.md` — qui ne couvre que
l'étiquette `cp314-cp314-win_amd64`. Le test distingue quatre issues par son
code de sortie : 0 installé et contrôle réussi, 1 contrôle du corpus en échec,
2 dépendance indisponible — ce n'est pas un défaut du corpus —, 3 plateforme non
couverte par l'artefact hors ligne.

**Contrôle et état** — `controle.py` est l'autorité, refuse la publication en cas
de blocage :

```bash
python corpus/controle.py                    # contrôle structurel seul
python corpus/controle.py --publier          # ajoute les règles de publication
python corpus/controle.py --maj-etat         # enregistre l'état après arbitrage
python corpus/controle.py --maj-etat --fond      # changement substantiel, même jour
python corpus/controle.py --maj-etat --editorial # changement non substantiel
python corpus/controle.py --maj-etat --initialiser-tardif=L1.C31   # initialisation tardive, après audit seulement
python corpus/controle.py --maj-etat --purger-orphelins            # retire les entrées d'état sans chapitre
python corpus/test_etat.py                       # conservation de l'état enregistré, sur copies
python corpus/test_lecture.py                    # sabotages E-L1 à E-L6, E-M1, sur copies
```

Le fichier `corpus/.etat-corpus.json` est écrit par le script — ne jamais
l'éditer à la main. L'enregistrement **conserve** les qualifications
existantes : une entrée inchangée ou à métadonnées seules modifiées garde la
sienne, `--fond` et `--editorial` ne qualifient que les entrées dont le corps a
changé, une entrée nouvelle est une initialisation neutre, et « tardive » n'est
jamais déduit d'une date. Le fichier `corpus/manifeste-etat-lecture.json`, écrit
une fois par la migration `etat_lecture`, est la seule autorisation possible de
l'état `a_requalifier` (E-L6) : ne jamais l'éditer non plus.

**Exemplaires — facultatif, hors du chemin de publication.** Les entrées de
source inscrivent l'empreinte SHA-256 de la pièce qu'elles déclarent avoir lue.
`verifier-exemplaires.py` la recalcule : pièce encore là, même octet pour octet,
et pièce nommée sous un nom qu'elle n'a pas. Il ne bloque rien, `controle.py`
restant l'autorité, et il ne dit RIEN de ce que la pièce porte (§ 12).

```bash
python corpus/verifier-exemplaires.py --dossier <racine>   # ou DEBUNKONOMY_EXEMPLAIRES
python corpus/test_verifier_exemplaires.py                 # neuf sabotages, sur fixtures
```

**Migration `etat_lecture`** — outils à exécution unique, dans
`corpus/migrations/etat-lecture/` : `migrer.py --commit-source <sha>` écrit une
fois et uniformément depuis le commit source qu'il reçoit explicitement, et
refuse tout arbre sale non attendu, tout commit inexistant, tout écart entre
son relevé et l'arbre ; `prouver.py --commit-source <sha>` rejoue huit
invariants indépendamment. Le protocole complet est
`protocoles/migration-etat-lecture.md`.

**Conversion d'un texte source en squelette de chapitre** — `convertir.py`
prend un `.odt`, `.md` ou `.txt` et produit un chapitre à en-tête minimal
valide, corps inséré. L'auteur complète ensuite le `resume`, les
`sources_primaires`, les `concepts` et les `renvois`.

```bash
python corpus/convertir.py --source ep08.odt \
    --chapitre L1.C08 \
    --titre "Pourquoi la dette change tout"
```

Le convertisseur ne remplit délibérément que le mécanique — jugements
éditoriaux exclus, par respect de la convention § 1. Le squelette contient des
`À COMPLÉTER` explicites dans `verifications_en_attente` et `resume`.

## Ce que Claude ne fait pas

- Ne calcule ni n'écrit d'empreinte à la main : c'est le script qui les stocke
  dans `.etat-corpus.json`.
- Ne fait pas passer un chapitre à `verifie` sans que toutes ses sources
  soient `ouverte` — texte lu, édition identifiée — et datées (§ 11 de la
  convention, étape 4 : goulot d'étranglement volontaire). Une source
  `candidate` ou `a_requalifier` bloque ce passage (E-L4).
- Ne modifie pas `revision_de_fond` pour une coquille ou une reformulation
  (§ 4 de la convention).
- N'ajoute pas de champ au schéma sans migration scriptée sur tout le corpus
  et incrément du journal des révisions (§ 15).
- **Ne réattribue, n'insère et ne renumérote jamais un matricule de livre**
  (§ 3). Un matricule réservé est brûlé même si le livre n'est jamais écrit.
  Le sens et l'ordre se changent dans `collection` et `motifs`, qui ne portent
  aucune URL. `corpus/livres.yaml` est la projection du **plan directeur** de
  l'auteur (Drive) : en cas d'écart, le plan tranche et le registre est
  corrigé — jamais l'inverse.
- N'enrichit pas la liste des balises de régime ni des `nature` de source
  (§ 8, § 4).
- Ne rédige pas de résumé de la convention (interdiction explicite en tête
  du fichier).
- Ne commite, ne pousse ni n'archive sans accord explicite (AGENTS.md).

## Méthode — règles arrêtées le 2026-09-20

Elles complètent ce qui précède et ne le remplacent pas. Chacune vient d'un
défaut constaté, nommé entre parenthèses.

**Ouvrir une source, c'est lire la pièce, non y localiser une phrase.**

- Pièce de moins de trente pages : lecture intégrale. Au-delà : les sections
  nommées, et l'entrée dit lesquelles ne sont pas lues. (Une pièce de douze
  pages a été déclarée `ouverte` deux fois sans que sa note décisive, sa
  condition d'application ni l'absence du terme qu'on lui attribuait soient
  vues.)
- Pour chaque énoncé du corps qu'elle appuie, l'entrée de source donne le
  passage et la page qui le portent — ni un titre, ni un mot du résumé.
- L'entrée porte une ligne « ce que la pièce dit contre l'usage qui en est
  fait ». « Rien » s'y écrit en toutes lettres.
- Extraction par `pdftotext` ou `pypdf`, contrôle positif et négatif avant tout
  verdict d'absence (`outils_claude/lire_piece.py`). Si un site refuse le
  téléchargement, l'auteur télécharge depuis son navigateur ; ne jamais lui
  donner une adresse inventée.

**Pistes, chiffres et signatures.**

- Un chiffre issu d'une recherche assistée est une piste. Il n'entre au corps à
  l'indicatif qu'avec un appel `[Sn]` vers une pièce lue qui le porte. Un énoncé
  chiffré sans appel est invisible pour E-L4.
- Un récapitulatif ne répète pas l'appel : lorsqu'un paragraphe reprend sans
  ajout des chiffres sourcés juste au-dessus, y remettre `[Sn]` alourdit le
  texte et laisse croire que l'appel couvre une conclusion nouvelle.
- Une entrée de source, une signature. Pas d'entrée composite ; pas d'appel
  double où une source non ouverte accompagne une source ouverte.
- Une école n'est pas portée par le texte d'un seul de ses membres.
- Si aucune pièce ne tranche, l'énoncé redescend en `::hypothese::` ou en
  question ouverte. Aucune relecture par un modèle ne tient lieu de la revue
  humaine qu'un arbitrage attend.

**Renvois et compteurs.**

- Un renvoi qui déplace une attribution vers un autre chapitre donne l'ancre
  exacte, dit que la pièce est portée là-bas, **et donne son état de lecture
  là-bas**. Modèle : L1.C09 § 5.
- Avant d'écrire `Lx.Cy § n`, ouvrir le chapitre cible et vérifier le numéro :
  une réécriture déplace les sections sans prévenir.
- Aucun compteur recopié à la main dans un corps. (Un relevé du registre a
  périmé en quatre heures.)

**Objections et audits.**

- Le rédacteur ne rejette ni ne restreint seul une objection. Chaque rejet
  reçoit une ligne de motif, relue par le superviseur ou par l'auteur.
- Claude ne conduit jamais l'audit tiers d'un chapitre
  (`protocoles/audit-contradictoire.md`). Une passe qu'il ferait malgré tout
  vaut passe adverse, et se déclare telle.
- Un audit confié à un autre modèle reçoit les extraits des pièces en jeu, non
  le seul chapitre.
- « A résisté à N audits » ne s'emploie nulle part comme argument de solidité.

**Charge d'arbitrage de l'auteur.**

- Au plus cinq décisions soumises par jour, classées par impact. Ce qui se
  règle par un contrôle mécanique passe par un script.
- Pas de nouveau registre ni de nouveau tableau de bord. Une note dit en tête ce
  qu'elle tranche, sans gras ni capitales à chaque ligne : le prochain lecteur
  est humain.

## Écarts connus entre convention et dépôt

Signaler ces points à l'utilisateur avant d'agir dessus, plutôt que d'y toucher
en passant :

- **Le générateur du § 13 existe depuis le 2026-09-16 : `corpus/generer.py`.**
  Il produit les pages HTML avec JSON-LD, le `.md` servi à côté de chaque page,
  un index de recherche par livre, l'index global léger, les tables des
  matières, le `sitemap.xml`, les entrées du `llms.txt`, le glossaire tiré de
  `vocabulaire.yaml` et la page de diagnostic en trois sections.
  **Il n'émet que ce que la convention autorise** : statut `verifie`,
  `citable: true`, toutes les sources `ouverte`. Tout le reste est compté, nommé
  dans `diagnostic.html`, et laissé dehors. Il ne réimplémente aucune règle de
  `controle.py`, qui reste l'autorité : la page de diagnostic reproduit sa
  sortie telle quelle. Les deux empreintes du § 5 sont lues dans
  `.etat-corpus.json`, jamais recalculées.

  ```bash
  python corpus/generer.py                     # émet dans corpus/genere/
  python corpus/generer.py --sortie <dossier>  # ailleurs
  python corpus/test_generer.py                # contrôle de la sortie
  ```

  **Ce qui reste ouvert.** La sortie n'est reliée à rien : `corpus/genere/` est
  exclu du dépôt, et le site est servi depuis `main`, qui ne porte aucun fichier
  du corpus. Publier suppose de trancher où la sortie est écrite dans l'arbre du
  site, et de traiter le point ci-dessous sur le lien corpus ↔ site. Le `llms.txt`
  produit est propre au corpus et **n'écrase pas** celui de la racine, qui décrit
  le site et s'écrit à la main.
- **`corpus/sources/` n'est pas dans l'arborescence du § 2.** Le dossier
  contient des fichiers `remediation-*.md` et `sources-*.md` (matière de
  vérification, hors schéma). Statut à clarifier avec l'utilisateur avant
  d'y toucher — soit intégrer dans la convention, soit déplacer.
- **Politique multilingue non tranchée.** `langue` est obligatoire dans
  l'en-tête, mais la convention ne dit rien du sort des versions `ar/de/en/
  es/it/pt` du site. Le corpus est actuellement français seul.
- **Lien corpus ↔ site.** Rien ne relie encore un chapitre du corpus à
  `articles.json`, à la navigation, au `sitemap.xml`, au `feed.xml`. À
  concevoir avant la première publication publique d'un chapitre.

## Style et rédaction

Les trois habitudes du § 10 de la convention s'appliquent à tout ce qui est
écrit dans le corpus, et Claude doit les respecter lorsqu'il rédige ou modifie
un chapitre :

- ouvrir sur ce que le passage établit, sans accroche ;
- redéfinir chaque sigle à sa première occurrence dans le chapitre ;
- garder pour chaque concept le nom du fichier de vocabulaire.

Raison : une IA n'extrait que quelques passages. Chacun doit tenir debout seul.
