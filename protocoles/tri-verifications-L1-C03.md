# Ouverture du lot L1.C03 — tri des vingt-deux vérifications

**Préparé le 2026-09-22. Rien n'est appliqué.** Aucune acquisition n'est
engagée ; aucun statut n'est changé.

**État** : `audit_contradictoire`, `revision_de_fond: 2026-09-20`, régime
`hybride`, **11 sources toutes `ouverte`** — E-L4 ne bloque pas —, 4 concepts,
99 lignes de corps, 6 sections.

---

## Ce que ce chapitre fait mieux que les autres

Il faut le dire avant les défauts. **Le § 1 déclare lui-même que trois de ses
chiffres ne sont pas portés** :

> la progression depuis 1990 […] — 22,7 puis 38,6 gigatonnes, soit une hausse de
> 70 % — **ne figure pas dans l'article** mais dans la série de données qu'il
> nomme, **et cette série n'a pas été acquise**. Aucune conclusion de ce
> chapitre ne repose sur cette progression.

Et le § 3 écarte trois exemples d'un coup :

> Les exemples habituellement cités — éclairage, motorisation automobile,
> transport aérien — appellent chacun une vérification distincte […]. **Ils ne
> sont pas repris ici tant qu'ils ne sont pas établis.**

**CONSÉQUENCE POUR L'OUTIL** : `controle_chiffres` signale « 22,7 », « 38,6 » et
« 70 » comme énoncés chiffrés sans appel. **Ce sont des faux positifs.** L'outil
ne distingue pas un chiffre non sourcé d'un chiffre explicitement déclaré non
sourcé. C'est son troisième angle mort connu, après l'insuffisance de portée
d'un appel.

---

## Le tri

| Colonne | Lignes | Compte |
|---|---|---|
| **A. Tâche ouverte réelle** | 10, 11, 12 | **3** |
| **A′. Arbitrage d'auteur, non tâche** | 2, 3, 4 | **3** |
| **B. Close ou traitée par le corps** | 1, 5, 6, 9, 13, 14, 15, 18, 19, 21, 22 | **11** |
| **C. Sans objet — l'énoncé n'est pas au corps** | 7, 8, 16, 17, 20 | **5** |

---

## Le défaut central, et il n'est dans aucune vérification

### Le § 2 fait porter à [S10] trois énoncés que ses passages lus ne portent pas

> Le charbon n'a pas mis fin à l'usage du bois, **dont la consommation mondiale
> a continué de croître**. Le pétrole n'a pas mis fin au charbon, **dont la
> consommation atteindrait son maximum historique deux siècles plus tard**. Le
> gaz n'a pas fait reculer le pétrole **[S10]**. […] Et l'essor récent du
> solaire et de l'éolien s'accompagne de **niveaux records de consommation de
> pétrole, de gaz et de charbon** [S10].

**[S10] est York & Bell 2019, quatre pages.** Ses passages lus sont trois :

- « a transition to natural gas is currently in progress […] even as consumption
  of the newly introduced energy source grew explosively, consumption of the
  older energy source continued to grow as well » (page PDF 2) ;
- « wind and solar combined provided only about 2% » (page PDF 2) ;
- « energy additions rather than transitions » (page PDF 2).

Ils portent **le principe général** des additions et **le cas du gaz**. Ils ne
portent ni la croissance du bois, ni le maximum historique du charbon, ni des
« niveaux records ». L'entrée dit d'ailleurs explicitement ce qu'elle ne porte
pas — le nucléaire — sans mentionner ces trois-là.

**C'EST LA TROISIÈME OCCURRENCE DU MÊME DÉFAUT EN UNE JOURNÉE** : le § 6 de
L1.C13 (Belize–Équateur–Gabon), le § 3 de L1.C05 (Jevons et les registres
distribués), et celui-ci. Un appel placé en fin de série paraît couvrir toute la
série ; `controle_chiffres` ne le voit pas, la phrase portant un appel.

**Les vérifications n° 10, n° 11 et n° 12 sont donc des tâches ouvertes
réelles** — et elles demandent des sources que le chapitre n'a pas.

**Deux voies, et E3 les couvre** : borner le § 2 à ce que [S10] porte — le gaz
et le principe —, ou déclarer les trois autres rapportés sans pièce ouverte, sur
le patron déjà employé au § 1 pour les trois chiffres.

---

## Colonne A — les quatre autres

- **n° 2** : le critère « productions qui n'apportent pas de bien-être »,
  employé alors que L1.C16 le construit **et le déclare inapplicable**. Le § 1
  porte déjà une précaution sur le statut du renvoi ; ce qui reste est un
  arbitrage.
- **n° 3, S2 Georgescu-Roegen** : **à trancher par l'auteur**, un exemplaire
  ayant été fourni le 2026-09-14. Arbitrage, non tâche.
- **n° 4, S9** : ouverte sur un **manuscrit accepté**, non sur la version
  publiée, dont le titre diffère. La réserve est tenue dans l'entrée ; reste à
  décider si elle suffit.
- **n° 18, Fressoz — CORRECTION DE CE DOSSIER, faite à l'application.** Elle
  demandait de remplacer « a démontré » par « défend la thèse que ». **Le corps
  l'écrit déjà** : « L'historien Jean-Baptiste Fressoz **défend** […] la thèse
  suivante ». Ce n'était pas une tâche. Ce qui reste — rechercher les
  discussions critiques de l'ouvrage — est un programme de recherche.

## Colonne C — cinq lignes sans objet

Kansas City, les « 160 ans » de l'effet Jevons, Raworth et le donut ne sont pas
au corps — vérifié. Les n° 16 et 17 demandent de rassembler des travaux et de
mesurer une part : ce sont des programmes de recherche, non des vérifications.

---

## Une dette déjà inscrite

`protocoles/passe-2.md` porte depuis ce jour le renvoi manquant : **L1.C03 ne
renvoie pas à L1.C07**, zéro occurrence dans son corps, absent de ses `renvois`.
Relevé refait ce jour. Ce lot est l'occasion de le corriger, si l'auteur le veut.

---

## Ce que le lot demanderait

| | Décision | Coût |
|---|---|---|
| **§ 2 / [S10]** | borner ou déclarer, trois énoncés | une à trois phrases |
| **renvoi C07** | ajouter le renvoi et l'ancre | une phrase, et `renvois` |
| **n° 2, 3, 4** | arbitrages d'auteur | — |
| **Solde** | les vingt-deux lignes | mécanique |

**Aucune acquisition n'est nécessaire** si le § 2 est borné plutôt que sourcé.
