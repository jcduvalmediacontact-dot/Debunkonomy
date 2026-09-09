# Calibration d'A47 sur dossiers réels — protocole à deux équipes

Ce protocole éprouve si A47 est **transférable** : si des personnes différentes,
appliquant la même grille aux mêmes dossiers réels, parviennent à des
classements convergents — ou savent dire précisément où et pourquoi elles
divergent.

**Ce qui a été établi jusqu'ici, et c'est étroit.** Le corpus a montré que la
règle **ne laisse aucun vide logique** : tout dossier évalué reçoit un régime,
la lacune de grille n'ouvre aucun droit, et l'incertitude agit sur la procédure
d'instruction. **Il reste à établir qu'elle peut être appliquée par des tiers à
des situations réelles.** Une règle cohérente que deux praticiens appliquent
différemment n'est pas une règle : c'est un vocabulaire.

**Ce protocole n'est pas exécuté.** Les trois dossiers sont nommés, les champs
sont posés, l'instrument de comparaison existe et fonctionne. **Les données
réelles ne sont pas acquises, et le corpus n'en inventera aucune.**

## Les trois dossiers, et pourquoi ceux-là

Ils sont choisis pour couvrir trois régimes de connaissance différents, non pour
leur intérêt propre.

**1. EAU POTABLE.** Seuils scientifiques et sanitaires relativement documentés,
horizons courts, réversibilité généralement établie. **C'est le cas favorable** :
si deux équipes divergent ici, A47 n'est pas transférable du tout.

**2. LITHIUM ET BATTERIES.** Ressource rare exigeant un **arbitrage de
portefeuille** entre usages concurrents — point 7 de la doctrine. La difficulté
n'est pas l'incertitude mais la **concurrence des usages**, et le classement
d'un dossier dépend de ce qu'on retient dans le portefeuille.

**3. STOCKAGE GÉOLOGIQUE DU CO₂.** Horizons longs, incertitudes importantes,
dommages potentiellement irréversibles. **C'est le cas défavorable**, et c'est
là que l'horizon sectoriel — cinquante ans ou échelle humaine — décide de la
charge de la preuve.

## Ce que chaque équipe documente, dossier par dossier

Aucun champ n'est facultatif. **Un champ non documenté n'est pas une valeur par
défaut : il rend la qualification incomplète**, et c'est un résultat en soi.

| champ | ce qu'il porte |
|---|---|
| `donnees` | sources utilisées, avec date d'accès et édition — **pas de résumé** |
| `horizon` | horizon de réversibilité retenu, et **pourquoi celui-là** |
| `gravite` | 0 à 3, avec le motif |
| `etendue` | 0 à 3, avec le motif |
| `plausibilite` | probabilité estimée du dommage, 0 à 1 |
| `confiance` | crédit accordé à cette estimation, 0 à 1 |
| `reductible` | l'incertitude peut-elle être réduite, oui ou non |
| `delai_acquisition` | en combien de temps, si réductible |
| `delai_utile` | délai au-delà duquel l'acquisition n'arrive pas à temps |
| `regime` | le régime obtenu en appliquant la grille |
| `charge` | à qui incombe la preuve |
| `procedure` | la procédure d'instruction obtenue |
| `motif` | la motivation, en toutes lettres |

**La plausibilité, la confiance et la réductibilité sont trois champs distincts,
et le rester est une condition du protocole.** Une probabilité de 0,30 bien
établie n'est pas une probabilité de 0,30 tirée de rien.

## Comment les deux équipes travaillent

**Même grille, fixée et publiée avant l'examen.** Les deux équipes reçoivent la
même grille sectorielle — seuils, horizons, délai utile. Si la grille ne couvre
pas un domaine, **les deux équipes doivent aboutir à « qualification
incomplète »**, et une divergence sur ce point est déjà un échec de
transférabilité.

**Indépendance.** Les équipes ne se consultent pas avant remise. Elles ne voient
pas les remises l'une de l'autre.

**Mêmes sources accessibles, sources propres autorisées.** Chaque équipe reçoit
le même dossier documentaire de départ et peut en ouvrir d'autres, **à condition
de les déclarer**. Une divergence due à une source que l'une seule a ouverte est
une information, pas un bruit.

**Motivation obligatoire.** Une valeur sans motif ne compte pas. C'est le point 3
de la doctrine, et c'est aussi ce qui rend les divergences analysables.

## Ce qu'on mesure, et ce qui compte vraiment

L'instrument est `modeles/calibration_a47.py`. Il compare deux remises et
distingue **quatre choses** :

**ACCORD DE RÉGIME.** Les deux équipes classent-elles le dossier dans le même
régime ? C'est la mesure principale.

**ACCORD DE PROCÉDURE.** Même procédure d'instruction ? Un même régime peut
recevoir des procédures différentes si les équipes divergent sur la
réductibilité ou le délai.

**DIVERGENCES SANS EFFET.** Deux équipes peuvent évaluer la gravité à 2 et 3 sans
que le régime change. **Ces divergences-là ne comptent pas comme des échecs** :
elles montrent seulement que la grille est robuste à cet endroit.

**DIVERGENCES DÉCISIVES.** Une divergence sur une seule dimension qui **fait
basculer le régime ou la charge de la preuve**. Ce sont celles-là qui décident
de la transférabilité, et l'instrument les isole en rejouant la qualification
avec la valeur de l'autre équipe, une dimension à la fois.

## Ce qui vaudra succès, et ce qui vaudra échec

**Le corpus ne fixe pas de seuil d'accord, et il ne doit pas en fixer avant
l'épreuve** — ce serait exactement la faute que le point 9 de la doctrine
interdit à propos des seuils sectoriels : les choisir après avoir vu les
dossiers, ou les choisir pour obtenir le résultat voulu.

**Ce qui est arrêté d'avance, en revanche, c'est la forme du verdict.**

- **A47 est transférable** si les divergences décisives sont **nommées et
  expliquées par la divergence d'une dimension identifiée**, chaque équipe
  pouvant dire quelle valeur elle a retenue et pourquoi.
- **A47 n'est pas transférable** si deux équipes aboutissent à des charges de la
  preuve opposées **sans pouvoir localiser la dimension responsable**, ou si
  elles divergent sur le cas favorable — l'eau potable.
- **Un résultat intermédiaire est possible et attendu** : transférable sur les
  dossiers documentés, non transférable sur ceux où l'horizon est en jeu. **Ce
  serait déjà une réponse**, et elle renverrait à la pièce ouverte des seuils
  sectoriels.

## Ce que ce protocole ne fera pas

**Il ne validera pas A47.** Deux équipes qui convergent peuvent converger sur une
erreur commune — c'est le défaut connu de tout accord inter-juges, et il est
d'autant plus fort que les deux équipes partagent une formation. **L'accord
mesure la transférabilité, jamais la justesse.**

**Il ne remplacera pas les seuils sectoriels.** Il les éclairera : une divergence
décisive concentrée sur l'horizon du stockage géologique dirait exactement quel
seuil doit être fixé en premier.

**Et il exige des sources ouvertes, non des résumés.** La règle du corpus vaut
ici comme ailleurs : un résumé produit par un modèle ne vaut pas ouverture, et
les acquisitions ne sont pas versées au dépôt.

## État

**Protocole écrit le 2026-09-09. Instrument construit et vérifié sur données
synthétiques — lesquelles ne disent rien d'A47 et servent uniquement à prouver
que l'instrument discrimine.**

**Les trois dossiers ne sont pas documentés. Les équipes ne sont pas
constituées.** Ce sont les deux conditions de l'exécution, et elles relèvent de
l'auteur.
