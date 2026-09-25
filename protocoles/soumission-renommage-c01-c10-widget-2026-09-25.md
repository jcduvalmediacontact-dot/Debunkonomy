# Soumission — six ancrages de renommage, le widget, et un verrou dans l'outil

**Rien n'est appliqué.** Ni le registre des ancrages, ni le widget. Les commandes
et les diffs sont ci-dessous ; l'approbation des ancrages est par ancrage, et
elle est à l'auteur.

---

## 1. Le verrou — TRANCHÉ ET LEVÉ LE 2026-09-25, issue (a)

**L'auteur a accordé l'admission partielle, et elle est appliquée dans l'outil.**
Une passe écrit les ancrages admis et eux seuls ; les autres restent non
déclarés, le contrôle continue de les signaler, le code de sortie reste 1. Le
plafond de quatre est intact, et aucune occurrence ne reçoit un motif qu'on ne lui
a pas donné. Dix sabotages nouveaux dans `test_controle_renommage.py`.

Ce qui suit est le constat tel qu'il a été soumis, et n'est pas réécrit.

### Le constat d'origine

`controle_renommage.py` porte deux règles qui s'excluent au-delà de quatre
occurrences neuves :

- `PLAFOND = 4` — quatre ancrages au plus par admission, « pour qu'un motif
  partagé reste un acte » ;
- toute occurrence neuve **non admise** fait échouer le lot entier
  (`refuses` → `sys.exit(1)`), avant toute écriture.

**Il y a six occurrences neuves.** Admettre quatre laisse deux refusées, donc
échoue ; admettre six dépasse le plafond, donc échoue. **`--generer-ancrages` ne
peut pas aboutir.**

Éprouvé, et non déduit : l'admission des quatre appariés a été lancée pour de
vrai, l'outil a refusé en nommant les deux restantes, et **le registre n'a pas
bougé** — empreinte `efc5304029…` avant et après. Le refus précède l'écriture.

**Le message de l'outil décrit une séquence que son code interdit** : « … puis
les N suivant(s), SÉPARÉMENT : le plafond est de 4 ancrages par admission ». Une
seconde passe séparée est impossible, puisque la première n'écrit rien.

**Trois issues, une recommandation.**

| | issue | effet |
|---|---|---|
| **a** | **admission partielle** : écrire les ancrages admis, et re-signaler les autres comme neuves | **recommandé.** Rend possible la séquence que le message promet déjà, sans toucher au plafond : chaque admission reste ≤ 4 et séparément motivée |
| b | relever `PLAFOND` à 6 | un motif partagé par six redevient un tampon, ce que le plafond existe pour empêcher |
| c | faire disparaître deux occurrences pour repasser sous le plafond | **à écarter** : ce serait réécrire un texte vrai pour contourner un contrôle. Les deux en cause doivent rester (§ 3) |

---

## 2. Les quatre déclarations à retirer — la même occurrence, déplacée

Aucune n'a disparu du texte : chacune a changé d'empreinte parce que son contexte
a bougé. **Trois par le soldage du 2026-09-22** : une vérification soldée devient
`# - "…"`, ce que l'expression `^  - "(.*?)"$` de l'outil ne reconnaît plus, donc
la zone passe de `notes` à `tete` et le `#` entre dans la fenêtre d'empreinte.
**Une par réécriture du corps.**

| disparu | remplacé par | zone | cause |
|---|---|---|---|
| `10ebf8b2e1b1a65d` L1.C01 | `a2679b1be9457cbb` | `notes` → `tete` | soldage du 2026-09-22 |
| `57f7dba231eb1394` L1.C01 | `67d6a94eb6bdf89b` | `notes` → `tete` | soldage du 2026-09-22 |
| `7ffd6c054d158705` L1.C10 | `7453a766dcb9be3e` | `notes` → `tete` | soldage du 2026-09-22 |
| `9d7fa3c20a5b59fd` L1.C10 | `f1e9bb43b2e2638d` | `corps` → `corps` | phrase réécrite autour |

Elles se retirent d'elles-mêmes : `--generer-ancrages` réécrit le fichier depuis
le relevé vivant. Aucune commande propre.

---

## 3. Les six ancrages à admettre, et le motif de chacun

Trois admissions, chacune sous le plafond, chacune un acte.

### Admission A — L1.C01, deux ancrages

```
python outils_claude/controle_renommage.py --generer-ancrages \
  --admettre a2679b1be9457cbb,67d6a94eb6bdf89b \
  --motif "notes seules — passées en commentaire par le soldage du 2026-09-22, texte inchangé"
```

Ce sont les deux occurrences que le registre déclarait déjà sous « notes
seules ». Le texte n'a pas changé d'un caractère ; seul le `#` du soldage s'est
inséré devant la ligne. Le motif d'origine tient, et le dit.

### Admission B — L1.C01, un ancrage : le procès-verbal du renommage

```
python outils_claude/controle_renommage.py --generer-ancrages \
  --admettre 59288f1159add83f \
  --motif "procès-verbal du renommage : mentionne « sans dette » pour constater qu'il est sorti du corps"
```

Ligne 17 du chapitre, dans un bloc soldé :

> `# SOLDÉE le 2026-09-22 (lot C01) — close par sa lettre, ET VÉRIFIÉE APPLIQUÉE :`
> `« contrepartie collective » figure au corps, « régénérative » cinq fois, et`
> `« sans dette » en est sorti. Texte d'origine :`

**C'est l'occurrence la plus légitime qui puisse exister** : elle emploie l'ancien
terme uniquement pour attester qu'il a quitté le corps. La retirer effacerait la
preuve que le renommage a été fait. Et la ligne ouvre un `Texte d'origine :`,
qu'on ne réécrit jamais.

### Admission C — L1.C10, trois ancrages : le vocabulaire de [S9]

```
python outils_claude/controle_renommage.py --generer-ancrages \
  --admettre 7453a766dcb9be3e,f1e9bb43b2e2638d,7334bb7693069aa2 \
  --motif "mots de Grandjean et Dufrêne, cités dans [S9] et décrits — y compris la case de grille du 2026-09-24"
```

Les deux premiers sont les occurrences déjà déclarées sous ce motif, déplacées.
Le troisième est **nouveau et de même nature** : une case de la grille du § 4,
ligne 342 —

> `| création monétaire écologique | non établi | [S9] émission sans dette pour la transition | non établi | non établi |`

La case rapporte le vocabulaire de la pièce **tel que la pièce l'emploie**. Le
renommer serait prêter à `[S9]` des mots qu'elle n'écrit pas — exactement la
faute que le corpus traque ailleurs.

**Aucun des six n'est une occurrence à renommer.** Quatre sont des déplacements,
et les deux nouveaux sont l'un un constat du renommage, l'autre une citation.

---

## 4. Le widget de l'assistant — oublié par la passe du 2026-09-20

`assets/widgets/debunkonomy-assistant-widget.html` : **trois occurrences de
« sans dette » à l'indicatif, zéro « monnaie régénérative à contrepartie
collective », zéro « émission à contrepartie collective », et pas de note
terminologique.**

**Il est déjà sur `main`, et inchangé depuis le 2 septembre** : la PR ne le
dégrade pas. Mais elle publie le glossaire qui fixe le nom canonique, ce qui rend
la contradiction citable là où elle passait inaperçue.

**Il se réécrit, il ne s'annote pas.** Les dix-huit pages ont reçu une note parce
qu'elles disent ce qui a été publié à leur date. Un widget d'assistant n'a pas de
date : il répond au présent. Une note datée y serait un contresens.

### Les trois remplacements proposés

**1 — prose HTML, offset 7903.** Le terme est employé pour l'acte.

> avant : « NEMO IMS propose que la monnaie soit créée **sans dette** en
> contrepartie d'activités régénératives — reforester, dépolluer… »
> après : « NEMO IMS propose une **émission à contrepartie collective** : la
> monnaie est créée pour des activités régénératives — reforester, dépolluer… »

La reprise de « en contrepartie » disparaît, sinon le mot figurerait deux fois en
huit mots.

**2 — réponse de l'assistant, offset 13178.** Le terme désigne l'unité.

> avant : « comment éviter l'inflation si on crée de la monnaie **sans dette** ? »
> après : « comment éviter l'inflation si on émet une **monnaie régénérative à
> contrepartie collective** ? »

**3 — réponse de l'assistant, offset 20905.** Deux corrections dans la même
phrase.

> avant : « création monétaire **sans dette**, **destroyée** selon l'impact
> écologique. »
> après : « **émission à contrepartie collective**, **détruite** selon l'impact
> écologique. »

**« destroyée » n'est pas un mot français** — un anglicisme resté en place, servi
en production. Il est dans la phrase même que le renommage touche : le corriger
là est moins risqué que de le laisser pour un lot qui n'existe pas encore.

---

## 5. Le widget n'est pas le trou : c'en est la pointe française

Le contrôle négatif a été étendu aux six versions linguistiques, avec le terme
**dans chaque langue** et non le terme français. La passe du 2026-09-20 n'a
couvert que le site français.

| version | fichiers portant l'ancien terme, **sans note** |
|---|---|
| `de/` | **14** |
| `en/` | **18** |
| `es/` | **12** |
| `it/` | **13** |
| `pt/` | **12** |
| **total** | **69** |

Aucun ne porte de note terminologique, et **aucun n'a changé depuis le
2 septembre** : la PR ne les touche pas, ils sont déjà sur `main`. Mais elle
publie le glossaire qui fixe le nom canonique, et **69 pages en cinq
langues le contrediront** — dont les cinq glossaires traduits eux-mêmes
(`de/nemo-ims/glossary/`, `en/…`, `es/…`, `it/…`, `pt/…`), qui définissent encore
l'ancien nom comme s'il était le bon.

**C'est la différence avec le widget** : le widget est un oubli, ceci est un
périmètre jamais ouvert. CLAUDE.md signale d'ailleurs que la « politique
multilingue n'est pas tranchée » — mais pour le corpus, pas pour le renommage du
site.

**L'ARABE N'EST PAS VÉRIFIÉ, et le dire est le seul résultat honnête.** Mon
premier balayage a rendu zéro pour `ar/` ; c'était un artefact de terme, pas un
résultat — `ar/` porte bien le mot « dette ». Surface : **58 fichiers
`.html`, dont 42 contiennent le mot**. Le rendu de « sans dette » en
arabe demande quelqu'un qui lit l'arabe ; je ne le devine pas, et deux fichiers
portant à la fois « dette » et « sans » ne font pas un verdict.

**Ce lot ne propose rien pour les cinq langues.** Réécrire 69 pages traduites, ou
leur poser une note traduite, est une décision de périmètre — pas une retouche.
Elle demande cinq notes à traduire, et les cinq glossaires à reprendre.

---

## Ce que cette soumission ne fait pas

- **Le balayage a été fait, et c'est le § 5.** Tous les fichiers suivis hors
  `corpus/` et `protocoles/` ont été balayés, avec le terme propre à chaque
  langue. **Sauf l'arabe, non vérifié**, pour la raison dite au § 5.
- **Elle ne juge pas le reste du widget.** Seules les trois occurrences du terme
  et l'anglicisme qui les accompagne ont été lus, sur 24 249 caractères.
