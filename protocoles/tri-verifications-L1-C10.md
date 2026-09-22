# Tri des dix-neuf vérifications de L1.C10

**Préparé le 2026-09-22. Rien n'est appliqué.** Ordre 2 du jour, décisions E3 et
E4 de l'auteur.

**État du chapitre** : `audit_contradictoire`, 21 sources, **toutes `ouverte`**
depuis la réduction de ce matin. E-L4 ne bloque plus.

---

## Réponse à E4, et elle est nette

**Les chiffres Deep Research des § 1 et § 2 sont déjà traités.** Le relevé
mécanique ne trouve **aucun énoncé chiffré sans appel** dans tout le chapitre.
Le détail, vérifié phrase par phrase :

| Piste de la vérification n° 5 | État dans le corps |
|---|---|
| 4 300 habitants | « environ quatre mille habitants » — arrondi, non chiffré au détail |
| 350 chômeurs, 200 sans indemnité | « plusieurs centaines », « une part sans aucune indemnité » — **dé-chiffré** |
| chômage −25 % contre +19 % national | « environ un quart », et **déclaré sans appui vérifié** |
| 32 000 schillings, tiers en circulation | au corps, **sourcé [S2]** (Fisher) |
| vitesse 10-15×, arriérés d'impôts | **déclarés non portés** par le corpus |

**E4 est donc confirmé sans réécriture** : ces chiffres suivent déjà E3, par
retrait, par arrondi, par sourçage ou par déclaration explicite.

**MAIS LE CONTRÔLE EN TROUVE UN AUTRE, ET IL N'EST DANS AUCUNE VÉRIFICATION.**

> …et de trente à cinquante emplois permanents créés parmi **les quinze cents
> chômeurs de la commune** [S2].

La vérification n° 5 attribue les **1 500 au district**, et 350 à la commune. Le
corps les attribue à la **commune**, qui compte environ quatre mille habitants —
un chômeur pour moins de trois habitants, nourrissons compris. **L'un des deux
se trompe**, et l'appel [S2] ne tranche pas : il faut lire Fisher.

Ce n'est **pas une acquisition** — [S2] est ouverte. C'est une confirmation sur
pièce tenue, à faire avec `lire_piece.py`.

---

## Le tri

| Colonne | Lignes | Compte |
|---|---|---|
| **A. À confirmer sur pièce tenue, ou acquisition** | 5, 6, 7, 8, 9, 10, 11 | **7** |
| **B. Close par son texte, ou périmée** | 1, 3, 4, 12, 18, 19 | **6** |
| **C. Pas une tâche factuelle** | 2, 13, 14, 15, 16, 17 | **6** |

**Une ligne est PÉRIMÉE : la n° 12.** Elle écrit « S2, S7, S9, S10, S11, S12, S14,
S22 : **à ouvrir par un humain** ». Les vingt et une entrées sont aujourd'hui
`ouverte`, et la règle « un humain ouvre » a été levée par l'auteur le
2026-09-06. Double péremption, comme la n° 10 de L1.C13.

**DEUX LIGNES APPELLENT UNE SOURCE QUI N'EXISTE PLUS**, et c'est **une dette
que notre réduction de ce matin a créée** : les n° 2 et n° 5 appellent `[S16]`,
retirée au commit `693027c4`. Le corps est propre — une garde le vérifiait —
mais elle **ne balayait que le corps**. Les deux entrées doivent perdre cet
appel, ou le déclarer retiré.

---

## Colonne A — sept lignes, dont zéro réécriture du corps

**Aucune de ces sept ne demande de réécrire une phrase.** Toutes demandent de
**confirmer** qu'une source ouverte porte bien ce que le corps lui fait dire :

- **n° 5, Wörgl [S2]** — confirmer les 1 500 chômeurs, voir ci-dessus. *Pièce
  tenue.*
- **n° 6, WIR [S4] [S5]** — confirmer les effectifs, volumes et taux. *Pièces
  tenues.*
- **n° 7, Bristol Pound [S20]** — « Ouvrir [S20] et confirmer ». **S20 est
  ouverte** : la ligne est à reformuler en confirmation.
- **n° 8, MLCC France [S21]** — idem ; elle note déjà que les chiffres Deep
  Research (5,0 M€, 40 000 utilisateurs) **ne sont pas retenus**.
- **n° 9, Eurosystème [S18]** — « l'API BCE était indisponible (503) ; ouvrir la
  série et confirmer ». **SEULE VRAIE ACQUISITION DU LOT.** E3 s'applique :
  réécrire sans les montants, ou écarter. Les montants sont appelés en [S18] au
  corps ; il faut donc lire [S18] avant de décider.
- **n° 10, euro numérique** — « vérifier la décision prise à l'issue » de la
  phase close le 31 octobre 2025. **Acquisition d'actualité.** E3 s'applique :
  le corps ne doit pas promettre un état qu'il ne tient pas à jour.
- **n° 11, Bancor [S6]** — confirmer deux paragraphes du Livre blanc Cmd. 6437.
  *Pièce tenue.*

---

## Colonne B — closes ou périmées

- **n° 1, renommage** : « CE CHAPITRE N'EST PAS RENOMMÉ, ET C'EST DÉLIBÉRÉ » —
  décision motivée, close.
- **n° 3, citation de Soddy** : « ÉCARTÉ », absente de l'OCR de l'édition 1926.
- **n° 4, Marshall & O'Neill** : « ÉCARTÉ », introuvable sur Crossref, remplacée
  par [S20].
- **n° 12** : périmée deux fois, voir ci-dessus.
- **n° 18 et n° 19** : la source ET la réponse à l'objection de fuite sont
  ouvertes depuis le 2026-09-08 par L16.C01 et L16.C02. Ce qui reste — le prix
  de cette réponse, la suppression de la propriété foncière — est un **arbitrage
  d'auteur**, pas une tâche documentaire.

---

## Colonne C — pas des tâches factuelles

- **n° 2, discordance September** : relevée sur une **pièce secondaire**, non
  arbitrée. Sa place est le registre.
- **n° 13, 14, 15** : trois limites — ancre fiscale, fuite devant la monnaie
  fondante, risque inflationniste. **Toutes trois mentionnées au corps** (§ 2,
  § 1, § 4), et les lignes le disent elles-mêmes.
- **n° 16, n° 17** : constats de cohérence avec L1.C05, L1.C08 et L1.C20.

---

## Ce que ce tri produit, si l'auteur le retient

| | avant | après |
|---|---|---|
| Vérifications actives | 19 | **2 à 4** |
| Phrases du corps réécrites | — | **0**, sauf décision sur n° 9 et n° 10 |
| Acquisitions | 7 annoncées | **2 réelles** — n° 9 et n° 10 |
| Appels orphelins en en-tête | **2** | 0 |

**Cinq des sept lignes de la colonne A n'étaient des acquisitions que par leur
formulation** : elles disent « ouvrir » des pièces que le corpus tient déjà
ouvertes. Les requalifier en confirmations ne coûte rien et ne demande aucune
décision.

Les deux vraies acquisitions — la série BCE et l'état de l'euro numérique —
tombent sous E3. Et un défaut de contenu, les 1 500 chômeurs, n'était dans
aucune vérification.
