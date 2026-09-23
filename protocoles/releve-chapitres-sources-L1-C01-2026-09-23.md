# L1.C01 — sur quoi le corps s'appuie, proposition par proposition

**Ordre 6. Rien n'est appliqué** : l'en-tête de C01 n'est pas modifié avant J3.

Depuis r15, `chapitres_sources` déclare **ce sur quoi le corps s'appuie**. Le
relevé ci-dessous cherche, pour chaque énoncé que C01 affirme sans le démontrer
lui-même, le chapitre qui le porte, sa section, et son état.

**Ce que C01 dit de lui-même, et qui commande tout le relevé** : « Ces trois
propositions sont ici énoncées et argumentées ; elles ne sont pas démontrées.
Leur démonstration occupe les chapitres suivants. » Un chapitre d'ouverture qui
annonce sa propre non-démonstration s'appuie donc moins qu'il n'annonce. **La
liste doit porter ce sur quoi il s'appuie, non le programme du livre.**

---

## Ce que le corps nomme explicitement — trois chapitres

| ligne | ce que le corps écrit | chapitre | état |
|---|---|---|---|
| 18 | « **L1.C08 établit**, sur un modèle à cohérence stock-flux, que ni la création de crédit ni la perception d'intérêts ne produisent à elles seules un impératif de croissance » | **L1.C08** | `verifie`, citable |
| 24 | « **L1.C05 § 5** le porte sur deux pièces ouvertes, un cours de première année et un manuel » | **L1.C05** | **`audit_factuel`** |
| 83 | « Le protocole de Montréal, **examiné au chapitre quatre** » | **L1.C04** | `verifie`, citable |

**L1.C04 est nommé en toutes lettres et ne figure pas dans la liste déclarée.**
Un renvoi écrit « au chapitre quatre » plutôt que « L1.C04 » échappe à tout
relevé mécanique — c'est ainsi qu'il a été manqué.

---

## Ce sur quoi le corps s'appuie sans le nommer — trois chapitres

| ligne | ce que le corps affirme | chapitre qui le porte | état |
|---|---|---|---|
| 14 | « Un **enchaînement causal** relie pourtant ces éléments » — extraction, production, croissance, rentabilité, dette | **L1.C02** | `verifie`, citable |
| 16 | « Plusieurs économies avancées présentent une consommation matérielle stabilisée ou en recul alors que leur produit croît […] leur portée dépend du traitement des flux incorporés dans les importations » | **L1.C03** | `verifie`, citable |
| 36-39 | le partage entre ce qui se vend et ce qui ne se vend pas, et les trois cas — sylviculture, tourbière, milieu marin | **L1.C15** | `verifie`, citable |

**Une tension à signaler sur L1.C02, et elle n'est pas de forme.** C01 § 1
écrit « un enchaînement **causal** relie pourtant ces éléments ». C02 écrit
l'inverse de ce que cette phrase suppose : « Ce qui précède décrit une
progression conjointe, **non une causalité**. Le mot de corrélation lui-même
serait prématuré. » **Le chapitre qui porte le constat refuse d'en tirer la
causalité que C01 énonce.** C01 se rattrape au § 1 en marquant sa conclusion
`::hypothese::`, mais la phrase de la ligne 14 est à l'indicatif.

---

## Ce qui est déclaré et que le corps n'emploie pas — cinq chapitres

| chapitre | titre | ce que C01 en dit |
|---|---|---|
| **L1.C07** | Comment les banques créent la monnaie | rien. Et son résumé **borne** C01 : « cela ne signifie ni que chaque crédit finance une activité productive rentable, ni que toute création bancaire impose à elle seule la croissance » |
| **L1.C09** | L'architecture invisible | rien. Les quatre règles n'apparaissent pas dans C01 |
| **L1.C11** | La première malédiction monétaire | rien |
| **L1.C12** | La deuxième malédiction monétaire | rien |
| **L1.C14** | La dette, un mythe de Sisyphe | rien. Le § 1 mentionne « rembourser des dettes », sans s'appuyer sur ce chapitre |
| **L1.C16** | La bullshitnovation | rien |

Six en réalité. Ces chapitres **démontrent ce que C01 annonce** — c'est le
programme du livre —, mais C01 ne s'appuie pas sur eux : il les précède.

---

## La liste que ce relevé justifie

```yaml
chapitres_sources: [L1.C02, L1.C03, L1.C04, L1.C05, L1.C08, L1.C15]
```

**Six, dont trois nommés au corps et trois à nommer.** Contre huit déclarés
aujourd'hui, dont **un seul** — L1.C08 — figure dans cette liste.

| | aujourd'hui | après relevé |
|---|---|---|
| entrent | — | **L1.C02, L1.C03, L1.C04, L1.C15** |
| restent | L1.C08 | L1.C08, **L1.C05** |
| sortent | L1.C07, L1.C09, L1.C11, L1.C12, L1.C14, L1.C16 | — |

---

## Ce que cette liste entraîne, et qu'il faut savoir avant de la poser

**C01 attend C05.** L1.C05 est `audit_factuel`, non `verifie`. Le corps le
nomme explicitement au § 2 et s'appuie sur ce qu'il porte. Tant que C05 n'est
pas vérifié, **C01 ne peut pas l'être** — J1 commande donc deux chapitres.

**Trois renvois seraient à écrire au corps**, ou la liste resterait déclarative.
L1.C02, L1.C03 et L1.C15 portent des énoncés que C01 fait sans les nommer ;
les nommer coûte trois incises, et rend la liste vérifiable par un lecteur.

**Une décision d'auteur reste entière** : la phrase « un enchaînement causal
relie pourtant ces éléments » (l. 14), quand L1.C02 tient que la causalité
n'est pas établie. Soit C01 la marque comme hypothèse, soit L1.C02 n'est pas ce
sur quoi elle s'appuie — et il faut dire sur quoi elle s'appuie.

**Enfin, `verifiee_le` devra bouger.** Il porte le 2026-09-22 et sera comparé
aux `revision_de_fond` des six chapitres retenus, non des huit actuels.
