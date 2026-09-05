# CLAUDE.md — repères de travail pour Claude Code

Ce fichier oriente une session Claude qui ouvre le dépôt. Il ne se substitue
à aucun document existant : il pointe vers eux et signale les écarts entre ce
que la convention décrit et ce que le dépôt implémente aujourd'hui.

## Documents faisant autorité

Lire dans cet ordre avant toute modification :

1. [corpus/convention.md](corpus/convention.md) — schéma, statuts, empreintes,
   contrôle. **Autorité sur tout ce qui touche au corpus.** Aucun résumé
   n'existe et ne doit être écrit : cf. son préambule. Révision courante : r9
   (licence CC-BY-SA-4.0 obligatoire, cible du lecteur explicite, patron des
   métaphores restituables `(*Image : ...*)`, registre des livres `livres.yaml`
   et règle du matricule en § 3).
2. [AGENTS.md](AGENTS.md) — routine de publication. **Ne jamais commiter,
   pousser ni archiver sans validation explicite de l'utilisateur.**
3. Pour le site hors corpus : [GUIDE-PUBLIER-CONTENU.md](GUIDE-PUBLIER-CONTENU.md),
   [INTEGRATION-ASSISTANT.md](INTEGRATION-ASSISTANT.md),
   [KNOWLEDGE-BASE.md](KNOWLEDGE-BASE.md).
4. [protocoles/](protocoles/) — textes à coller pour les modèles tiers :
   `audit-contradictoire.md` (Gemini normal / ChatGPT, jamais Claude seul) et
   `sourcage-deep-research.md` (Gemini Deep Research sur les
   `verifications_en_attente`). Ce qu'ils rapportent est une piste, jamais une
   vérification : un humain ouvre la source avant toute `date_verification`.
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

Dépendance unique : `PyYAML` (`pip install pyyaml`).

**Contrôle et état** — `controle.py` est l'autorité, refuse la publication en cas
de blocage :

```bash
python corpus/controle.py                    # contrôle structurel seul
python corpus/controle.py --publier          # ajoute les règles de publication
python corpus/controle.py --maj-etat         # enregistre l'état après arbitrage
python corpus/controle.py --maj-etat --fond      # changement substantiel, même jour
python corpus/controle.py --maj-etat --editorial # changement non substantiel
```

Le fichier `corpus/.etat-corpus.json` est écrit par le script — ne jamais
l'éditer à la main.

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
- Ne fait pas passer un chapitre à `verifie` sans que les sources soient
  effectivement vérifiées et datées (§ 11 de la convention, étape 4 : goulot
  d'étranglement volontaire).
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

## Écarts connus entre convention et dépôt

Signaler ces points à l'utilisateur avant d'agir dessus, plutôt que d'y toucher
en passant :

- **Le générateur du § 13 n'est pas implémenté.** `controle.py` ne produit
  que le rapport de diagnostic sur `stdout` ; les pages HTML du corpus, les
  index par livre, le `llms.txt` propre au corpus, le glossaire, les `.md`
  servis à côté des pages n'existent pas encore. Les deux empreintes du § 5
  sont bien calculées et stockées dans `.etat-corpus.json` (voir
  `controler_empreintes` dans `controle.py`).
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
