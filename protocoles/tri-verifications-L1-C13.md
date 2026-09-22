# Tri des quatorze vérifications de L1.C13

**Préparé le 2026-09-22. Rien n'est appliqué.** Ordre 2 du jour, décisions E3 et
E4 de l'auteur : toute vérification qui est une acquisition suit la règle des
ressources gratuites — réécrire la phrase ou écarter.

**État du chapitre** : `audit_contradictoire`, 19 sources, **toutes `ouverte`**
depuis la réduction de ce matin. E-L4 ne bloque plus.

---

## Le tri

| Colonne | Lignes | Compte |
|---|---|---|
| **A. Acquisition ou énoncé non porté** — relève d'E3 | 1, 4, 5, 7, 9 | **5** |
| **B. Close par son texte, ou périmée** | 2, 6, 10, 11, 13, 14 | **6** |
| **C. Pas une tâche factuelle** | 3, 8, 12 | **3** |

**Une ligne est PÉRIMÉE et il faut le dire : la n° 10.** Elle écrit « S7, S10,
S11, S12, S13, S14, S16 : ouvrages et articles non ouverts ». Les dix-neuf
entrées du chapitre sont aujourd'hui `ouverte`. C'est le même défaut que la
n° 12 de L1.C14, soldée le 2026-09-20 comme « périmée sur deux plans ».

---

## Colonne A — les cinq phrases, avant et après

### A-1 — Équateur 2023 et Gabon 2023, § 6 (vérification n° 1)

> les swaps dette-nature, dont les opérations récentes — Belize en 2021 **[S20]**,
> **Équateur en 2023, Gabon en 2023** — ont changé d'échelle.

**L'appel ne couvre que Belize.** La pièce acquise le 2026-09-19 est de 2022 et
ne porte ni l'Équateur ni le Gabon. `controle_chiffres` ne le voit pas : la
phrase porte un appel, et l'outil s'arrête là. **C'est un angle mort de l'outil,
noté ici.**

**Après, voie « écarter »** — la plus simple :

> les swaps dette-nature, dont l'opération du Belize en 2021 [S20] a marqué un
> changement d'échelle.

**Après, voie « réécrire »** — garde le fait en le déclarant :

> les swaps dette-nature, dont les opérations récentes — Belize en 2021 [S20],
> puis l'Équateur et le Gabon en 2023, que ce chapitre rapporte sans pièce
> ouverte — ont changé d'échelle.

**Ce qui est perdu, voie 1** : deux opérations sur trois, et l'idée de
changement d'échelle qu'elles portaient à elles trois.

---

### A-2 — Sinistres climatiques assurés, § 5 (vérifications n° 4 et n° 7)

> sinistres climatiques assurés de **5 à 7 milliards d'euros par an [S6]**, en
> hausse tendancielle

La vérification n° 4 note que 2024 est consolidé à **5,0 Md€**, l'estimation
provisoire ayant été de 3,9 Md€ ; la n° 7 demande d'ouvrir les communiqués
France Assureurs de mars 2025 et mars 2026. **C'est une acquisition.**

**Après, voie « écarter l'acquisition et garder la fourchette »** : ne rien
changer au corps, et solder n° 7 comme acquisition écartée par E3. La fourchette
est déjà appelée en [S6].

**Motif** : le corps n'avance pas le chiffre consolidé ; il donne une fourchette
sourcée. L'acquisition n'ajouterait de la précision qu'à une phrase qui n'en
demande pas.

---

### A-3 — Pages du PDNA pakistanais, § 5 (vérification n° 5)

> le bilan officiel des dommages est de 14,9 milliards de dollars, celui des
> pertes de 15,2 milliards, et les besoins de reconstruction résiliente d'au
> moins 16,3 milliards **[S5]**

**Ce n'est PAS une acquisition** : [S5] est ouverte. La vérification dit
« p. 16 **selon Deep Research** » — c'est la *localisation* qui vient d'une
piste, non le chiffre. Travail de confirmation sur pièce déjà tenue, à faire
avec `lire_piece.py`, sans rien acquérir.

**Après** : aucune réécriture. L'entrée doit dire ce qui reste — confirmer la
page — et cesser d'annoncer une acquisition.

---

### A-4 — Cumul mondial des swaps, § 6 (vérification n° 9)

> leur cumul mondial se compte en quelques milliards de dollars — **2,6 milliards
> de dette traitée et 1,2 milliard effectivement versé à la conservation selon le
> relevé que le Fonds reprend du PNUD [S20]**

**La vérification est largement périmée.** Elle demande de sourcer « environ
2,5 Md$ et 1,2 Md$ … d'après reprises (Reuters, NAP Global Network) ». Le corps
écrit **2,6** et **1,2**, sourcés sur [S20] avec sa chaîne de reprise explicite.
Seuls les montants par opération — 364 M$, 1,6 Md$, 500 M$ — restent non
sourcés, **et ils ne sont pas au corps**.

**Après** : aucune réécriture. Solder comme périmée, en notant que les montants
par opération restent hors du corps.

---

### A-5 — Typologie des issues de l'État endetté, § 2 (vérification n° 3)

La ligne propose d'étoffer les « trois options » par la typologie de
Reinhart-Sbrancia **[S11], qui est ouverte**. Ce n'est ni une acquisition ni un
défaut : c'est une **proposition d'enrichissement éditorial**.

**Après** : aucune réécriture. Sa place est `passe-2.md`, non cette liste — elle
demanderait d'élargir le chapitre, ce que l'ordre exclut.

---

## Colonne B — closes par leur texte, ou périmées

- **n° 2, Skouriès** : « LE CHIFFRE EST SORTI DU CORPS LE 2026-09-16 ». Vérifié :
  « 340 hectares » est absent du corps.
- **n° 6, S15 scindée** : ouverte au texte des lois 4628/2019 et 4631/2019. Son
  renvoi au « cadre de 2010-2011 qui reste candidat » est **périmé depuis ce
  matin** : S19 est retirée, et le § 5 dit désormais « le chapitre ne le porte
  donc pas en source ».
- **n° 10** : périmée, voir ci-dessus.
- **n° 11, n° 13** : constats de cohérence, faits et concordants.
- **n° 14, `noeud_gordien`** : « ÉTAT VÉRIFIÉ LE 2026-09-19, CONFORME » ; ce qui
  reste est un arbitrage de passe 2.

---

## Colonne C — pas des tâches factuelles

- **n° 3** : proposition éditoriale, voir A-5.
- **n° 8, Gran Chaco** : le chiffre de 1,14 million d'hectares **n'est pas au
  corps** — vérifié. La ligne dit elle-même « non sourcé, **non repris** ». Elle
  est sans objet tant qu'il n'y entre pas.
- **n° 12, cohérence avec L1.C12** : le contrôle est fait, et il trouve **une
  contradiction interne à L1.C12**. La tâche n'appartient pas à ce chapitre-ci ;
  sa place est le registre, à l'arbitrage de l'auteur.

---

## Ce que ce tri produit, si l'auteur le retient

| | avant | après |
|---|---|---|
| Vérifications actives | 14 | **0 ou 1** |
| Phrases du corps réécrites | — | **une seule** (A-1) |
| Acquisitions | 2 | **0**, écartées par E3 |

**Une seule phrase du corps est en cause**, celle des swaps. Tout le reste est
soit clos, soit périmé, soit hors de cette liste. La décision qui compte est
donc unique : **écarter l'Équateur et le Gabon, ou les garder en les déclarant
non sourcés.**
