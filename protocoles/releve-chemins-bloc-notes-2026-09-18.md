# Relevé des chemins de bloc-notes cités par les entrées de source

**Ouvert le 2026-09-18 par Claude. Aucune entrée de source n'est modifiée ici, et rien n'est commité.** Ce fichier répond à une commande qui partait d'une prémisse fausse, et il commence par le dire.

## Le constat qui renverse la commande

La commande posait que les 28 chemins d'acquisition cités « [n'existent] plus sur le disque ». **Ils existent tous.** Ils sont relatifs à `C:/Users/jcduv/Documents/Codex/`, et non à la racine du dépôt. Cette racine est déjà écrite dans le dépôt : `protocoles/constats-tranche-3.md` nomme le dossier `Documents/Codex/2026-09-15/` en tête de son tableau.

Une recherche lancée à l'intérieur du dépôt ne trouve rien, et ce vide ne dit rien des fichiers — c'est le même artefact que celui déjà porté au catalogue pour les extractions : **un « non retrouvé » produit par un script n'est pas un verdict tant que la racine n'a pas été vérifiée.**

Il n'y a donc **aucune réacquisition à faire, aucune URL à déduire, et aucune entrée à corriger** au titre de ce signalement.

## Ce qui a été vérifié, et comment

Le contrôle ne s'est pas arrêté à l'existence des fichiers. Pour chaque chemin cité dans un en-tête de chapitre, le script a apparié le chemin à l'empreinte SHA-256 que l'entrée inscrit **immédiatement après lui**, a lu le fichier sur le disque et a recalculé son empreinte.

| | |
|---|---|
| Occurrences de chemins datés en en-tête | **221** |
| dont retenues par le `grep` de la commande | **28** |
| dont le `grep` ne voit pas | **193** |
| Empreinte recalculée **concordante** | **202** |
| Empreinte **discordante** | **0** |
| Fichier absent | **0** |
| Chemins cités sans empreinte inscrite (fichier présent) | **18** |

**Zéro discordance sur 202 empreintes recalculées.** Les exemplaires versés au dossier sont, à l'octet près, ceux que les entrées déclarent avoir lus.

### Pourquoi le `grep` de la commande ne voyait que 28 sur 221

Deux raisons, et la seconde est la plus coûteuse.

1. Le motif `[^\s,)\"]*` est une classe de caractères POSIX : `\s` n'y est pas la classe « espace », mais les deux caractères `\` et `s`. **Le nom de fichier est donc tronqué à la première lettre `s`** — d'où les `C18-S5-`, `C22-S5-o`, `bretton-wood` du relevé initial. Le motif localise, il ne lit pas.
2. Il n'accepte que le segment littéral `acquisitions`. Or les exemplaires vivent aussi sous `courses-c17-c30/`, `empreintes-completees/`, `audit-C08/`, `je-x20/`, `c02/` … `c25/`. **Le sous-ensemble de 28 est arbitraire** : il ne recouvre ni un livre, ni une séance, ni une classe de risque.

### Ce que le sous-ensemble de 28 laissait hors champ

Les 28 sont tous des chapitres `brouillon`. Les 193 que le motif manque touchent **41 chapitres dans 5 livres**, dont **5 chapitres `verifie`** — L1.C07, L1.C08, L1.C09, L1.C15, L1.C31 — et 4 en `audit_contradictoire`. Si la prémisse avait été vraie, c'est là que le dommage aurait porté, et non sur les 28.

## Réponses aux quatre points de la commande

**1. La liste exhaustive des 28.** En annexe, une ligne par occurrence, avec le chapitre, le champ, le nom de fichier, la présence d'une URL, l'`etat_lecture` et le résultat du recalcul d'empreinte.

**2. Les URL canoniques des 15 sans rattrapage.** Le décompte de la commande est exact : **13 entrées portent une URL, 15 n'en portent pas.** Mais la déduction demandée est sans objet, les fichiers étant présents et vérifiés. Et pour 7 des 13 entrées de source concernées, **il n'y aurait rien à déduire** : l'URL est déjà écrite dans le corpus, attachée au fichier de même empreinte.

| fichier | entrées sans URL | l'URL existe déjà | preuve |
|---|---|---|---|
| Ostrom, WPS 5095 | L1.C27 [S9], L8.C29 [S2], L8.C33 [S2], L11.C16 [S2], L11.C21 [S3], L11.C25 [S3] | oui, en **L1.C22 [S5]** | même SHA-256 `EE38A92C…15F7` |
| Hardin 1968 | L8.C33 [S3] | oui, en **L1.C22 [S6]** | même SHA-256 `823D0549…F664` |
| Statuts du FMI, UNTS vol. 2 | L3.C02 [S3], L3.C07 [S1–S4], L3.C08 [S3] | **non, nulle part** | SHA-256 `DABCC422…CF5F`, cité par ces 6 entrées seulement |

Seule la troisième ligne appellerait une URL nouvelle. Candidate, **et c'est une inférence tirée de la mention d'édition, non une vérification** : `https://treaties.un.org/doc/Publication/UNTS/Volume%202/v2.pdf`. L'adresse répond et sert bien un PDF (constaté le 2026-09-18) ; **je ne l'ai pas téléchargée et n'ai donc pas établi qu'il s'agit du même fichier de 352 pages.**

**3. Le risque E-L6.** Il ne se présente pas. **Aucune des 28 occurrences n'est `a_requalifier`** : 26 sont `ouverte` et datées, 2 sont des notes de `verifications_en_attente` sans état. Sur l'ensemble des 221, on compte 211 `ouverte` et 2 `candidate`, et toujours aucune `a_requalifier`. La règle reste vraie et mérite d'être retenue pour d'autres entrées — l'empreinte d'E-L6 porte sur le triplet `nature` + `reference` + `url`, donc **ajouter une URL suffit à la rompre, autant que réécrire la référence** — mais elle ne mord sur aucune entrée de ce relevé.

**4. Rien n'est commité.** `corpus/convention.md` et `AGENTS.md` ont été lus avant tout geste. Le dépôt n'est pas modifié ; ce fichier est le seul ajout, et il n'est pas suivi par git.

## Les deux seules imperfections trouvées, et elles sont mineures

**L1.C06 [S1] nomme un fichier sous un nom qu'il n'a pas.** L'entrée écrit « le tableur `Global_Carbon_Budget_2025_v1.0.xlsx` … (dossier `Documents/Codex/2026-09-14/c03/`, SHA-256 `A928CF06…64A9`) ». Le dossier existe, mais aucun fichier n'y porte ce nom : l'exemplaire versé s'appelle `gcb-2025-serie.xlsx`. **L'empreinte tranche** — elle correspond exactement à ce fichier, et à lui seul parmi les treize du dossier. L'entrée nomme donc le fichier de l'éditeur, le dossier en garde une copie renommée, et rien n'est perdu. Reste que l'entrée est, à la lettre, inexacte.

**Dix-huit chemins sont cités sans empreinte.** Le fichier est présent dans les dix-huit cas. Ce sont, pour l'essentiel, des exemplaires **écartés** que l'entrée nomme pour justifier de les avoir écartés — le Gesell de 1919 en fraktur, le substitut UNESCO refusé en L1.C22 [S9], le prolongement Stodder-Lietaer 2016 « ni lu ni appelé ». Ne pas leur donner d'empreinte se défend : ils ne portent aucune lecture.

## Un piège rencontré en route, à porter au catalogue

Ma première passe a annoncé **4 empreintes discordantes**. Elles étaient fausses, toutes les quatre. Le script attachait l'unique empreinte d'une entrée à **tous** les chemins qu'elle cite ; or une entrée nomme couramment un exemplaire ouvert, avec son empreinte, **et** des exemplaires écartés, sans la leur. La discordance était dans mon appariement, pas dans le corpus. Le contrôle corrigé n'associe une empreinte à un chemin que si elle le suit dans la même fenêtre de texte, et il trouve zéro discordance.

**La règle qui s'en dégage** : dans une entrée qui cite plusieurs pièces, une empreinte appartient à la pièce qu'elle suit, jamais à l'entrée. Un contrôle qui l'ignore fabrique des défauts.

## Ce que le contrôle ne voit pas

`python corpus/controle.py` **passe** aujourd'hui, et il serait passé de la même façon si les 221 fichiers avaient réellement disparu : il ne résout aucun chemin d'exemplaire et ne recalcule aucune empreinte de pièce. Or le dépôt inscrit déjà 203 empreintes de fichiers, dans des entrées qui affirment « OUVERT PAR TÉLÉCHARGEMENT DIRECT » ou « OUVERTE PAR VERSEMENT ».

Ces empreintes ne servent actuellement à rien de mécanique. Elles pourraient tout : la question de cette séance se serait réglée en une seconde de calcul au lieu d'une session d'inférence, et une pièce silencieusement remplacée ou tronquée dans le dossier serait détectée le jour même.

C'est la seule proposition de fond de ce relevé, et elle est soumise à l'auteur, ci-dessous.

---

## Annexe — les 28 occurrences du périmètre de la commande

| # | chapitre | champ | fichier cité | URL dans l'entrée | état | empreinte |
|---|---|---|---|---|---|---|
| 1 | L1.C17 | `verifications_en_attente` | `C17-S9-bank-charter-act-1844.html` | **non** | — | fichier présent, sans empreinte inscrite |
| 2 | L1.C18 [S3] | `reference` | `C18-S3-corte-constitucional-colombia-t-622-16.html` | oui | ouverte | **concorde** |
| 3 | L1.C18 [S5] | `reference` | `C18-S5-stone-1972-should-trees-have-standing.pdf` | oui | ouverte | **concorde** |
| 4 | L1.C18 [S6] | `reference` | `C18-S6-jensen-meckling-1976-theory-of-the-firm.pdf` | oui | ouverte | **concorde** |
| 5 | L1.C18 [S10] | `reference` | `C18-S10-hayek-1945-use-of-knowledge.html` | oui | ouverte | **concorde** |
| 6 | L1.C18 | `verifications_en_attente` | `C18-S16-onu-seea-ea-comptabilite-ecosystemes.pdf` | **non** | — | fichier présent, sans empreinte inscrite |
| 7 | L1.C20 [S9] | `reference` | `C20-S9-hanke-krus-cato-wp8-hyperinflations.pdf` | oui | ouverte | **concorde** |
| 8 | L1.C21 [S4] | `reference` | `C21-S4-keynes-1936-general-theory.pdf` | oui | ouverte | **concorde** |
| 9 | L1.C22 [S5] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | oui | ouverte | **concorde** |
| 10 | L1.C22 [S6] | `reference` | `C22-S6-hardin-1968-tragedy-of-the-commons.pdf` | oui | ouverte | **concorde** |
| 11 | L1.C22 [S9] | `reference` | `C22-S9-feyzioglu-swaroop-zhu-1998-wber-banque-mondiale.pdf` | oui | ouverte | **concorde** |
| 12 | L1.C22 [S13] | `reference` | `C22-S13-arrow-1962-economic-welfare-invention.pdf` | oui | ouverte | **concorde** |
| 13 | L1.C24 [S9] | `reference` | `C24-S9-gopinath-2020-dominant-currency-paradigm.pdf` | oui | ouverte | **concorde** |
| 14 | L1.C24 [S10] | `reference` | `C24-S10-gourinchas-rey-nber-w11563.pdf` | oui | ouverte | **concorde** |
| 15 | L1.C25 [S9] | `reference` | `C24-S10-gourinchas-rey-nber-w11563.pdf` | oui | ouverte | **concorde** |
| 16 | L1.C27 [S9] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |
| 17 | L3.C02 [S3] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 18 | L3.C07 [S1] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 19 | L3.C07 [S2] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 20 | L3.C07 [S3] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 21 | L3.C07 [S4] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 22 | L3.C08 [S3] | `reference` | `bretton-woods-unts-v2.pdf` | **non** | ouverte | **concorde** |
| 23 | L8.C29 [S2] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |
| 24 | L8.C33 [S2] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |
| 25 | L8.C33 [S3] | `reference` | `C22-S6-hardin-1968-tragedy-of-the-commons.pdf` | **non** | ouverte | **concorde** |
| 26 | L11.C16 [S2] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |
| 27 | L11.C21 [S3] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |
| 28 | L11.C25 [S3] | `reference` | `C22-S5-ostrom-2009-banque-mondiale-wps5095.pdf` | **non** | ouverte | **concorde** |

Total : 28 occurrences.

## Synthèse des 221

| verdict | occurrences |
|---|---|
| CONCORDE | 202 |
| existe, sans empreinte | 18 |
| ABSENT (dossier) | 1 |

Chapitres touchés : 41. Livres touchés : 5.
Fichiers distincts cités : 156.

| statut du chapitre | chapitres |
|---|---|
| `brouillon` | 32 |
| `verifie` | 5 |
| `audit_contradictoire` | 4 |

---

# Question à l'auteur

**Une seule décision est demandée, et elle ne porte pas sur les 28.**

## Ce qui est acquis, et n'appelle pas d'arbitrage

Les 221 exemplaires cités par les en-têtes sont présents sous `Documents/Codex/`. Les 202 empreintes recalculées concordent toutes. Aucune entrée n'est à corriger, aucune URL n'est à écrire, E-L6 ne se présente pas. **La commande du 2026-09-18 est sans objet, et je n'ai rien modifié.**

## La décision : faut-il rendre les empreintes opérantes ?

Le dépôt inscrit **203 empreintes SHA-256 de pièces** dans des entrées qui affirment avoir lu ces pièces. Aucune n'est vérifiée par quoi que ce soit. `controle.py` passe aujourd'hui, et il passerait à l'identique si les 221 fichiers avaient disparu, ou si l'un d'eux avait été remplacé par un autre document.

Cette séance en est la démonstration : il a fallu une session entière pour établir par inférence ce qu'un contrôle aurait rendu en une seconde — et l'inférence est passée par une conclusion fausse à 4 discordances avant d'être corrigée.

**Trois voies, et la troisième est celle que je recommande.**

**(a) Ne rien faire.** Les empreintes restent documentaires. Motif défendable : le dossier `Documents/Codex/` est hors du dépôt, il n'est pas public, et faire dépendre le contrôle du corpus d'un dossier local le rendrait **non reproductible pour quiconque clone le dépôt** — y compris pour vous sur une autre machine. C'est l'objection sérieuse à (b) et (c).

**(b) Un contrôle intégré à `controle.py`.** Il résoudrait les chemins et recalculerait les empreintes. Mais il ferait échouer le contrôle chez tout autre porteur du dépôt, ce qui contredit le rôle de `controle.py` comme autorité de publication. **À écarter pour ce motif.**

**(c) Un contrôle séparé, facultatif, hors du chemin de publication.** Un script distinct — `corpus/verifier-exemplaires.py`, prenant la racine du dossier en argument — que vous lancez quand vous le voulez, et dont l'échec ne bloque rien. Il n'ajoute aucun champ au schéma, ne touche pas à `controle.py`, ne change pas la convention, et ne suppose pas que le dossier existe.

Il répondrait mécaniquement à trois questions que le dépôt ne sait pas poser : *l'exemplaire déclaré lu est-il encore là ? est-ce le même octet pour octet ? une entrée nomme-t-elle une pièce sous un nom qu'elle n'a pas ?*

**Question : voulez-vous (c) ?** Et si oui, faut-il l'inscrire à la convention comme outil reconnu, ou le laisser hors convention comme les `remediation-*.md` de `corpus/sources/` — dont le statut est déjà signalé comme à clarifier dans `CLAUDE.md` ?

## Deux points accessoires, à trancher d'un mot

**1. L1.C06 [S1] nomme `Global_Carbon_Budget_2025_v1.0.xlsx` ; le fichier versé s'appelle `gcb-2025-serie.xlsx`.** L'empreinte prouve que c'est le bon fichier. Faut-il corriger le nom dans l'entrée, ou tenir que nommer le fichier de l'éditeur est le bon usage et que l'empreinte suffit à lever l'ambiguïté ? *(Je penche pour le second, et pour ne rien toucher.)*

**2. Treize entrées de source ne portent pas de champ `url` alors que le document est en ligne.** La convention dit `url` « optionnel — absent pour une source non disponible en ligne » : ces treize sont donc, à la lettre, hors usage. Pour sept d'entre elles, l'URL est déjà dans le corpus sous la même empreinte (Ostrom, Hardin, via L1.C22). Pour les six entrées des Statuts du FMI, il faudrait d'abord établir l'adresse du volume 2 du Recueil des Traités — **ce que je n'ai pas fait.**

Faut-il ouvrir ce travail, ou le renvoyer à la passe 2 ? Il ne bloque rien : les six chapitres concernés sont en `brouillon`, et l'exemplaire est au dossier, vérifié.

## Ce que je n'ai pas fait

- Je n'ai **pas téléchargé** le volume 2 du Recueil des Traités, donc je n'ai pas établi que l'URL proposée sert le fichier de 352 pages dont l'empreinte est `DABCC422…CF5F`. L'adresse répond et sert un PDF, rien de plus.
- Je n'ai **pas ouvert** les pièces pour contrôler les citations qu'en tirent les entrées. Ce relevé établit que l'exemplaire est le bon fichier, **pas qu'il porte ce qu'on lui fait dire**. Les deux questions sont distinctes, et seule la première est traitée ici.
- Je n'ai **pas étendu** le contrôle au corps des chapitres : seuls les en-têtes — `reference` et `verifications_en_attente` — ont été balayés.

---

# Clôture — décisions de l'auteur du 2026-09-18 et suites données

Les questions ci-dessus sont tranchées. Ce qui suit est ce qui a été fait le
jour même, et rien n'a été commité.

## Les décisions

| Question | Décision | Suite |
|---|---|---|
| Rendre les empreintes opérantes ? | **oui**, voie (c) : outil séparé | `corpus/verifier-exemplaires.py` + `corpus/test_verifier_exemplaires.py` |
| L'inscrire à la convention ? | **oui** | **révision 13**, § 12 et journal ; `CLAUDE.md` réaligné |
| Corriger le nom de pièce en L1.C06 [S1] ? | **oui** | l'entrée nomme désormais `2026-09-14/c03/gcb-2025-serie.xlsx` |
| Doter les treize entrées d'une `url` ? | **oui** | 13 `url` écrites |
| L'adresse du Recueil des Traités | **vérifier** | vérifiée par empreinte, puis écrite |

## L'adresse du volume 2 n'est plus une inférence

Le relevé ci-dessus proposait `https://treaties.un.org/doc/Publication/UNTS/Volume%202/v2.pdf`
comme **inférence tirée de la mention d'édition**, et disait ne pas l'avoir
établie. Elle l'est désormais, par calcul et non par ressemblance.

| | |
|---|---|
| Fichier téléchargé le 2026-09-18 | `HTTP 200`, `application/pdf`, **5 514 283 octets** |
| SHA-256 obtenu | `DABCC42277BCCA2AE7462DCCCBA24BF169C966061EB732CA87F8C2B47D19CF5F` |
| SHA-256 de l'exemplaire du dossier | **identique** |

L'adresse sert donc **exactement** l'exemplaire sur lequel les six entrées des
Statuts du FMI ont été ouvertes. Le fichier téléchargé a été supprimé après
comparaison ; rien n'a été versé au dossier ni au dépôt.

## Les treize `url`, et d'où elles viennent

Aucune n'est déduite d'un nom de fichier.

| entrées | url | fondement |
|---|---|---|
| L1.C27 [S9], L8.C29 [S2], L8.C33 [S2], L11.C16 [S2], L11.C21 [S3], L11.C25 [S3] | Ostrom, WPS 5095 | déjà portée par **L1.C22 [S5]**, sur un exemplaire de même SHA-256 |
| L8.C33 [S3] | Hardin 1968 | déjà portée par **L1.C22 [S6]**, même SHA-256 |
| L3.C02 [S3], L3.C07 [S1–S4], L3.C08 [S3] | UNTS vol. 2 | **vérifiée par empreinte le 2026-09-18** ; les six entrées portent la mention |

## État après coup

```
controle.py                      Contrôle structurel passé.
test_lecture / test_etat / test_generer / test_verifier_exemplaires   OK
verifier-exemplaires.py          203 CONCORDE, 18 PRESENTE, 0 anomalie
```

Le signalement `RENOMMEE` de L1.C06 a disparu : la correction du nom l'a
converti en concordance. Aucune empreinte ne manque plus à l'appel.

## Ce qui reste, et n'a pas été demandé

Le décompte de « treize entrées sans `url` » ne valait que **dans le périmètre
des 28**. Sur l'ensemble du corpus, **78 entrées de source citent un chemin
d'exemplaire sans porter de champ `url`** — les treize traitées comprises.
Restent donc 65, ainsi réparties :

- **7 portent déjà leur url dans le texte de la `reference`** : la promotion
  vers le champ `url` est mécanique et sans risque.
- **58 n'en portent aucune** : 55 en chapitre `brouillon`, 15 en
  `audit_contradictoire` (L1.C10, L1.C13, L1.C14), et **1 en `verifie`** —
  L1.C15 [S2], qui est un texte inédit de l'auteur, **légitimement sans url**
  au sens de la convention (« absent pour une source non disponible en ligne »).

Rien de tout cela ne bloque : `controle.py` passe, et l'exemplaire de chacune
est au dossier, empreinte vérifiée. **Ce chantier n'a pas été ouvert.**
