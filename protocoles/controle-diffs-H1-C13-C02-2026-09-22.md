# H1 — les deux diffs que personne n'a contrôlés

L'auteur a décidé d'appliquer H1 — C13 et C02 à `verifie` — puis, le défaut
signalé, de faire contrôler les deux diffs d'abord. Ce dossier les isole pour
que ce contrôle soit possible sans reconstruire le raisonnement.

**Ce qui a été trouvé.** La justification de H1 écrit « Contrôles finaux rendus
sans réserve, rien n'a bougé depuis ». C'est faux pour les deux chapitres, et
la règle 7 — *aucun chapitre ne passe à `verifie` sur un corps que l'autre
famille n'a pas vu dans son état final ; le contrôle porte sur le diff* — n'est
donc satisfaite ni pour l'un ni pour l'autre.

**Ce que ce dossier n'est pas.** Ni un audit tiers, ni une passe adverse. Un
contrôle de diff : deux questions fermées, deux verdicts courts.

---

## Ce qui est déjà vérifié mécaniquement — à ne pas refaire

| | C13 | C02 |
|---|---|---|
| sources | 19, **toutes `ouverte` et datées** | 9, **toutes `ouverte` et datées** |
| `verifications_en_attente` | **0** | **0** |
| concepts / renvois | 6 / 8 | 4 / 4 |
| type / régime | `chapitre` / `hybride` | `chapitre` / `hybride` |
| statut actuel | `audit_contradictoire` | `audit_factuel` |
| `citable` | `false` — H1 ne le change pas | `false` — idem |

Les conditions de `controle.py` pour `verifie` sont donc réunies dans les deux
cas. **Il ne reste que la règle 7.**

---

## C13 — le contrôle Codex précède le corps de quatre heures et demie

`protocoles/audit-codex-L1-C13-2026-09-22.md` porte sur `693027c4` (08 h 40) et
a été rendu à 08 h 52. **Il n'était pas sans réserve** : il écrivait « § 3 est
borné ; Équateur et Gabon au § 4 dépassent encore S20 ».

Deux commits ont suivi, **et tous deux changent le corps** :

- **`ffe958d7`, 09 h 07 — ligne 70, au § 4** ;
- **`8d46ea3b`, 13 h 25 — ligne 32, au § 3.**

**Correction du 22 au soir, mon erreur.** La première version de ce dossier
décrivait `ffe958d7` comme un commit de soldes et annonçait le diff du § 3
comme « le seul diff de corps non contrôlé ». C'est faux : `ffe958d7` touche
aussi le corps, et c'est dans ce diff-là que Codex a trouvé le défaut restant.
Un commit qui solde des vérifications peut aussi corriger une phrase ; son
message ne suffit pas à dire ce qu'il change.

### Le diff du § 4, `ffe958d7`, ligne 70

```
   … les swaps dette-nature, dont les opérations récentes — Belize en 2021 [S20],
-  Équateur en 2023, Gabon en 2023
+  puis l'Équateur et le Gabon en 2023, **que ce chapitre rapporte sans pièce
   ouverte**, l'article de 2021 appelé ici ne les portant pas
```

### Le diff du § 3, `8d46ea3b`, ligne 32

```
-  … 7 milliards par an en moyenne sur 2022-2024, contre 3 sur la période
   précédente [S6]
+  … 7 milliards par an en moyenne sur 2022-2024 [S6], contre environ 3 sur la
   période précédente, **chiffre lu sur un graphique de la même source et non
   confirmé au texte**
```

**Question au contrôleur.** Deux choses y sont faites en même temps : l'appel
`[S6]` est déplacé pour ne plus couvrir la comparaison, et le « 3 » est déclaré
lu sur un graphique. Le déplacement laisse-t-il `[S6]` sur ce qu'il porte
réellement, et la déclaration correspond-elle à ce que l'entrée S6 dit avoir lu ?
L'entrée porte « NON VÉRIFIÉ AU CHIFFRE » sur ce point.

*Livrable* : cinq lignes, dont la dernière est « rien ne s'oppose à `verifie` »
ou ce qui s'y oppose.

---

## C02 — le correctif des quatre défauts n'a jamais été revu

Codex avait signalé quatre défauts sur C02 ; `f7bc7ba6` (21/09, 16 h 23) les a
traités. **Le corps n'a plus bougé depuis** — `b8c1f70f` ne change que le
statut, et `ed3aecca` solde douze vérifications sans toucher au corps, ce que
son message dit et qu'une comparaison confirme. Mais le correctif lui-même n'a
reçu aucun contrôle.

La comparaison ligne à ligne rapporte 34 lignes modifiées. **C'est un
décalage** : un paragraphe inséré au § 2 pousse tout le reste d'un cran. Les
changements réels sont six.

| | ce qui change |
|---|---|
| titre du § 2 | « Une **corrélation** » → « Une **progression conjointe** » |
| § 2, 1re phrase | « ne sont pas indépendantes […] cette **corrélation est mesurable** » → « progressent ensemble […] **suivent la même pente** » |
| § 2 | la déforestation passe d'une affirmation sans chiffre à « près de **90 %** de la déforestation mondiale entre 2000 et 2018 […] 35 500 échantillons » **[S9]**, avec son périmètre — 68 % petite agriculture, 32 % grande |
| § 2 | l'imputation du coût de dégradation passe à l'irréel — « n'apparaîtrait », « serait supporté » — et une phrase ajoute que **[S1] mesure une perte globale et ne dit ni où elle est inscrite ni qui la supporte** |
| § 2 et § 6, deux fois | « la **corrélation** serait contingente » → « la **progression conjointe** serait contingente » |
| § 1 | retrait de « Quelques effondrements sévères pèsent lourdement sur cette moyenne. » |

### Deux vérifications faites, pour ne pas les refaire

**Le mot « corrélation » a été balayé dans tout le fichier, en-tête comprise.**
Il subsiste cinq fois, et aucune n'est une affirmation : deux dans le corps, sur
la même ligne, dans la phrase qui déclare le mot prématuré ; deux dans des blocs
commentés, archives de vérifications soldées ; une dans le `resume`, qui écrit
« le mot de corrélation **serait prématuré** tant que les séries ne sont pas
toutes rapportées à leur source ». Le résumé et le § 2 concordent. Le défaut
relevé le 2026-09-15 — « son résumé dit *établit la corrélation* là où le § 2
juge le mot prématuré » — est bien éteint.

**L'entrée [S9] est exemplaire.** `ouverte` le 2026-09-21, passages localisés au
résumé exécutif page PDF 12 : le « almost 90 percent of deforestation » et le
« 68 percent of agriculture-driven deforestation » y sont tous deux cités ; la
méthode et les 35 500 échantillons sont à la page 13 ; les pages non lues sont
déclarées.

### La question qui reste, et qui demande un jugement

**L'entrée [S9] porte elle-même un avertissement contre l'usage que ce chapitre
pourrait faire du chiffre** : « elle impute 68 % de la déforestation agricole à
la PETITE agriculture et non à l'agro-industrie, jusqu'à 97 % en Afrique, ce qui
contredit une lecture qui rapporterait ce chiffre aux seuls acteurs capables
d'externaliser à grande échelle ».

Or ce chapitre a pour thèse que la valeur financière s'obtient en laissant des
dommages hors du prix — mécanisme qui suppose des acteurs en état de le faire.
Le § 2 donne le périmètre (68 / 32), donc il ne cache rien. Mais **la place du
chiffre dans l'argument le rapporte-t-elle implicitement au mécanisme
d'externalisation**, ce que la pièce interdit ? Autrement dit : le lecteur
sort-il du § 2 en croyant que ces 90 % illustrent la fausse richesse ?

*Livrable* : cinq lignes, même forme. La dernière est « rien ne s'oppose à
`verifie` » ou ce qui s'y oppose.

---

## Les deux contrôles, rendus le 22 au soir

Codex a rendu les deux. **Aucun chapitre n'a été modifié par lui**, et chacun
appelle une retouche précise avant `verifie`.

**C13 — le changement du § 3 est correctement borné.** Le défaut est ailleurs,
dans le diff du § 4 que ce dossier avait omis : le corps écrit « **l'article de
2021** appelé ici ne les portant pas », alors que l'entrée S20 identifie
« *Debt-for-Climate Swaps*, FMI, Working Paper WP/22/162, **2022** » et écrit en
toutes lettres « le papier est de 2022 ». Vérifié sur l'entrée. « Belize en
2021 » est juste — c'est la date de l'opération, que l'encadré du papier porte.
**Le chapitre se trompe sur la date de sa propre source dans la phrase même où
il en déclare les limites**, ce qui rend la déclaration invérifiable pour un
lecteur.

**C02 — le passage FAO distingue bien le chiffre constaté de l'hypothèse
d'externalisation** : la question ouverte de ce dossier est tranchée, rien ne
s'y oppose. Le défaut est une phrase du § 2 : « le produit mondial, les
émissions, la consommation matérielle, l'extraction de ressources et
l'endettement **suivent la même pente** sur un demi-siècle ». Une même pente est
une comparaison mesurée ; or le § 2 écrit trois paragraphes plus bas que « le
mot de corrélation lui-même serait prématuré » faute de séries rapportées à
leur source, de périmètre et de période fixés. **La phrase affirme plus que ce
que le chapitre se reconnaît le droit d'affirmer.**

## Ce qui suit

Les deux retouches appliquées et contrôlées, H1 s'applique : `statut: verifie`
sur les deux, un commit par chapitre, les quatre tests. Les retouches touchent
le corps — donc `--maj-etat --fond` —, le passage à `verifie` non.

`citable` reste `false` : H1 ne le change pas, et le lot des citables est
annoncé séparément.
