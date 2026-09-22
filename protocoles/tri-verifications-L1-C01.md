# Ouverture du lot L1.C01 — tri des vingt-sept vérifications

**Préparé le 2026-09-22. Rien n'est appliqué.** Aucune acquisition ; aucun
statut changé.

**État** : `brouillon`, `type: chapitre`, `revision_de_fond: 2026-09-20`, régime
`hybride`, **ZÉRO source**, `renvois` **vide**, 4 concepts, 192 lignes — le plus
long de la première partie.

---

## Ce chapitre n'est pas de la même nature que les autres

**Il le dit lui-même, dès sa seconde phrase** :

> Ces trois propositions sont ici énoncées et argumentées ; **elles ne sont pas
> démontrées**. Leur démonstration occupe les chapitres suivants.

**Et le relevé le confirme** : 11 `::hypothese::`, 11 `::etat::`, 2 `::norme::`,
**zéro appel `[Sn]`**, et **aucune grandeur chiffrée** — ni en chiffres, ni en
lettres, contrôlé sur les deux formes. C'est une ouverture programmatique, pas
un chapitre empirique.

---

## Le blocage est structurel, et il ne se lève pas par un tri

`controle.py`, ligne 598 : un chapitre dont le `type` n'est pas `synthese` et
dont `sources_primaires` est vide **ne peut pas atteindre `verifie`**.

L1.C01 est `type: chapitre` avec zéro source. **Solder ses vingt-sept
vérifications ne changerait rien à cela.** Trois voies s'ouvrent, et elles
appartiennent à l'auteur :

| | Voie | Ce qu'elle coûte |
|---|---|---|
| **1** | verser au moins une source | une acquisition, ou un versement depuis un autre chapitre |
| **2** | passer en `type: synthese` | change la nature déclarée du chapitre ; ses sources deviennent des chapitres |
| **3** | assumer que C01 reste hors `verifie` | le chapitre d'ouverture n'est jamais citable |

La voie 2 mérite un examen : une synthèse « n'a pas de sources documentaires :
ses sources sont des chapitres », dit le commentaire de `controle.py`. C'est
exactement ce que C01 est — un chapitre qui annonce ce que les suivants
démontrent. Mais ce serait un changement de nature déclarée, non un tri.

---

## Le tri

| Colonne | Lignes | Compte |
|---|---|---|
| **A. Affirmation qualitative sans source, au corps** | 7, 8, 15 | **3** |
| **B. Close ou vérifiée appliquée** | 1 | **1** |
| **C. Sans objet — aucun chiffre au corps** | 2-6, 9-14, 18-27 | **21** |
| **D. En attente d'un acte futur** | 16, 17 | **2** |

### C — vingt et une lignes sans objet, et le contrôle qui l'établit

Elles demandent toutes de **sourcer des grandeurs** : séries longues de
production et d'émissions, volumes de dispositifs, part des émissions couvertes
par un prix du carbone, fourchettes du coût social, durées d'engagement,
seuil du HANPP. **Le corps ne porte aucune grandeur.** Contrôlé sur les nombres
écrits en chiffres et sur ceux écrits en lettres — zéro dans les deux cas.

Les objets dont elles parlent sont bien au corps — polycrise, manuels, horizon
des investisseurs, peuplement forestier, paiements pour services
environnementaux, prix du carbone, dioxyde de soufre, additionnalité — **mais
qualitativement, sans mesure**. HANPP, lui, n'y est pas du tout.

**Sous E3, ces vingt et une acquisitions tombent**, et leurs lignes de solde
doivent dire qu'elles redeviennent actives si une grandeur entre au corps.

### A — trois affirmations qui demandent un appui, chiffres ou non

- **n° 7, « polycrise »** : le corps écrit « Le terme de "polycrise" a été forgé
  pour décrire cet empilement » — **une affirmation de paternité, sans auteur ni
  date**. Elle ne demande pas un chiffre mais une référence.
- **n° 8, les manuels** : le corps parle du traitement de la monnaie dans les
  manuels. **Affirmation sur un corpus de textes, sans citation.** L1.C05 a
  résolu le même problème avec [S6] et [S7] — un cours de première année et des
  manuels — **qui sont ouverts**.
- **n° 15, la condition d'accumulation de L1.C08** : le mot « accumul » est
  **absent du corps**, alors que l'audit du 2026-09-03 demandait d'ajouter cette
  condition à la chaîne causale. À vérifier : soit la condition est exprimée
  autrement, soit elle manque.

### D — deux lignes qui attendent un identifiant

Les n° 16 et 17 demandent d'ajouter des renvois « quand le chapitre aura son
identifiant » — Livre 3 sur la coordination internationale, et le chapitre du
régime de preuve. **Une note qui renvoie à un acte futur doit nommer un acte qui
existe** : tant que ces identifiants n'existent pas, ces lignes ne sont pas des
tâches mais des rappels. Leur place est `passe-2.md`.

---

## Une correction de ce dossier, faite pendant sa rédaction

La n° 1 déclare le renommage canonique « appliqué ici ». Mon premier contrôle
cherchait l'expression exacte « régénérative à contrepartie » et rendait
**absent du corps**. **C'était un faux négatif** : « contrepartie collective »
figure une fois au corps, « régénérative » cinq fois, et « sans dette » a
disparu du corps tout en restant en en-tête. La ligne dit vrai.

C'est le troisième faux négatif du même type aujourd'hui — une chaîne de
recherche trop longue, qu'une coupure de ligne ou une variante de formulation
suffit à faire échouer.

---

## Ce que le lot demanderait

| | Décision | Coût |
|---|---|---|
| **Voie pour `verifie`** | source, `synthese`, ou hors `verifie` | **décision d'auteur** |
| **n° 7** | sourcer « polycrise » ou déclarer le terme repris sans paternité | une phrase |
| **n° 8** | verser [S6]/[S7] depuis L1.C05, ou borner | un versement |
| **n° 15** | vérifier si la condition d'accumulation est au corps | lecture |
| **Solde** | vingt et une lignes sans objet, deux en `passe-2.md` | mécanique |

**La décision qui commande est la première**, et elle n'est pas documentaire.
