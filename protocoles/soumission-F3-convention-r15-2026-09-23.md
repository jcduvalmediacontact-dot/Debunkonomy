# F3 — les deux diffs, soumis avant application

**Rien n'est appliqué.** Ordre 8 : préparer l'amendement de la convention et la
renumérotation du § 4 de C01, et soumettre.

**Mais un fait trouvé en préparant change ce qui est à décider**, et il est en
tête parce qu'il commande le reste.

---

## Ce que `chapitres_sources` déclare, et ce que le corps fait

C01 déclare huit chapitres sources. **Son corps en cite deux.**

| | |
|---|---|
| déclarés | L1.C07, L1.C08, L1.C09, L1.C11, L1.C12, L1.C14, L1.C15, L1.C16 |
| cités au corps | **L1.C05, L1.C08** |
| déclarés **et** cités | **L1.C08**, seul |
| déclarés et non cités | sept |
| cité et non déclaré | **L1.C05** |

Ce champ a été posé le 2026-09-22 comme un jugement éditorial assumé — le
chapitre articule ces huit chapitres sans les nommer. **Le relevé montre que
l'écart est plus large que cette formule ne le laissait croire** : un sur huit.

Le contrôle ne le voit pas. `controler_synthese` vérifie que
`chapitres_sources` est non vide et que `verifiee_le` est postérieur aux
`revision_de_fond` — jamais que le corps s'appuie sur ce qu'il déclare. C'est
la troisième occurrence aujourd'hui du même défaut : **deux enregistrements de
la même chose, que rien ne compare.**

**Conséquence pour F3.** Amender la convention pour admettre `synthese` hors du
livre 0 est défendable. Amender pour légitimer un `chapitres_sources` qui ne
correspond pas au corps ne l'est pas : la convention validerait un champ qui dit
autre chose que le texte.

---

## Diff 1 — convention, § 6 et journal r15

### `corpus/convention.md`, § 6, à la suite du dernier paragraphe

```diff
 **Il s'écrit au fil de l'eau.** Dès qu'un livre est vérifié, ses entrées de
 livre 0 sont rédigées dans la foulée. Ni avant — ce serait une promesse — ni à la
 fin — ce serait une reconstitution de mémoire.
+
+**Le type `synthese` n'est pas réservé au livre 0.** Un chapitre qui articule
+d'autres chapitres au lieu d'établir sur des pièces le porte aussi : il ouvre un
+livre, ou en referme une partie, et son travail est de dire ce que les chapitres
+qu'il nomme ont établi. Les deux champs restent obligatoires et le contrôle est
+le même.
+
+**Ce que le type dispense, et ce qu'il ne dispense pas.** Il dispense de
+`sources_primaires` : une synthèse n'ouvre pas de pièce, elle renvoie à ceux qui
+l'ont fait. Il ne dispense de rien d'autre — ni des concepts, ni des
+vérifications soldées, ni des balises de régime.
+
+**`chapitres_sources` n'est pas une liste de lectures : c'est ce sur quoi le
+corps s'appuie.** Un chapitre déclaré et jamais employé n'y a pas sa place, et
+un chapitre employé sans être déclaré doit y entrer. L'écart entre les deux est
+un défaut, non un jugement éditorial — mais **aucun script ne le contrôle**, et
+la convention le dit plutôt que de le laisser croire.
```

### `corpus/convention.md`, § 15, en tête du journal

```diff
 ## 15. Journal des révisions
+
+**Révision 15 — 23 septembre 2026.** Le type `synthese` cesse d'être réservé
+aux entrées du livre 0 (§ 6). Motif : L1.C01 ouvre le Livre 1 en articulant les
+chapitres qui démontrent, sans ouvrir de pièce ; il ne pouvait être ni
+`chapitre` — le statut `verifie` exige alors des `sources_primaires` — ni
+`synthese`, le § 6 réservant ce type au livre 0. **Aucun des deux types ne le
+décrivait**, et le blocage était structurel, non documentaire.
+
+Cette révision **n'ajoute aucun champ au schéma et ne touche aucun chapitre** —
+d'où l'absence de migration. Elle ajoute en revanche une exigence qui n'était
+écrite nulle part : `chapitres_sources` déclare ce sur quoi le corps s'appuie,
+et l'écart avec ce que le corps cite est un défaut. **Cette exigence n'est
+contrôlée par aucun script**, et la convention le déclare : c'est une règle de
+rédaction, pas un blocage.
+
+**Un écart connu au jour de la révision** : L1.C01 déclare huit
+`chapitres_sources` et son corps en cite deux, dont un seul figure parmi les
+huit. La révision rend cet écart nommable ; elle ne le corrige pas.
```

### `CLAUDE.md`, ligne « Révision courante »

```diff
-   contrôle. **Autorité sur tout ce qui touche au corpus.** Aucun résumé
-   n'existe et ne doit être écrit : cf. son préambule. Révision courante : r14
-   (l'URL publique ne dérive que de l'identifiant, `/corpus/livre-6/c05/` — § 3 ;
+   contrôle. **Autorité sur tout ce qui touche au corpus.** Aucun résumé
+   n'existe et ne doit être écrit : cf. son préambule. Révision courante : r15
+   (le type `synthese` n'est plus réservé au livre 0, et `chapitres_sources`
+   déclare ce sur quoi le corps s'appuie — § 6 ; r14 : l'URL publique ne dérive
+   que de l'identifiant, `/corpus/livre-6/c05/` — § 3 ;
```

---

## Diff 2 — renumérotation du § 4 de C01, `--editorial`

Le § 4 contient **quatre `##` au même niveau que les sections numérotées**. Le
chapitre paraît donc avoir onze sections là où il en a six, et la table des
matières produite par le générateur les mettrait au même rang.

```diff
-## Ce que l'objection soutient          (ligne 54)
+### Ce que l'objection soutient
-## Ce que ces instruments obtiennent    (ligne 78)
+### Ce que ces instruments obtiennent
-## Où l'instrument rencontre ses limites (ligne 91)
+### Où l'instrument rencontre ses limites
-## Le point exact du désaccord          (ligne 121)
+### Le point exact du désaccord
```

Quatre lignes, aucun mot changé. `--editorial` : la structure d'affichage
change, le propos non.

---

## Ce qui reste à décider

**Le diff 2 est prêt et ne dépend de rien.** Il peut être appliqué seul.

**Le diff 1 pose une question que l'ordre 8 ne posait pas.** Sa dernière clause
— `chapitres_sources` déclare ce sur quoi le corps s'appuie — rend l'écart de
C01 nommable et le laisse entier. Trois suites sont possibles :

| | |
|---|---|
| **a** | amender tel quel, et inscrire l'écart de C01 comme une dette à solder |
| **b** | amender, puis ramener `chapitres_sources` aux deux chapitres que le corps emploie — L1.C05 et L1.C08 — ce qui est exact mais laisse un chapitre d'ouverture qui ne synthétise presque rien |
| **c** | amender, puis écrire au corps l'articulation que le champ annonce — sept chapitres à nommer là où ils portent. C'est de la rédaction, non un lot |

**Sans la dernière clause**, le diff 1 passe sans question : il admet `synthese`
hors du livre 0 et ne dit rien de ce que le champ doit contenir. Ce serait
amender la convention pour lever un blocage en laissant intact ce qui l'a causé.
