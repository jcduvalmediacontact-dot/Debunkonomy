# Réduction de la source fermée de L1.C10

**Préparée le 2026-09-22. Aucune de ces modifications n'est appliquée.** Le
document est soumis à l'auteur ; il attend un accord.

**Décision dont il procède** : accord de principe C4 du 2026-09-21, sur le
précédent de la décision du 2026-09-14 pour L1.C09 — « réduire ce qu'ils
portent ». La décision de fond est attendue sur cette fiche.

**La source.** S16 — A. von Muralt, « The Woergl Experiment with Depreciating
Money », *Annals of Public and Cooperative Economics*, 10(1), p. 48-57, 1934.

**ATTENTION, SON ÉTAT N'EST PAS CELUI DE S19 DANS L1.C13.** S16 porte
`etat_lecture: a_requalifier`, non `candidate`. Cet état n'est autorisé que par
le manifeste des occurrences historiques, et **corriger la référence d'une
source `a_requalifier` lui fait perdre son état (E-L6)**. La réduction proposée
ici **retire l'entrée entière** et ne touche pas à sa référence : c'est la seule
voie qui n'entre pas en conflit avec E-L6.

---

## Ce que la réduction produit

| | avant | après |
|---|---|---|
| Sources déclarées | 22 | **21** |
| Sources `ouverte` | 21 | **21** |
| Sources non ouvertes | 1 | **0** |
| Blocage E-L4 sur `verifie` | oui | **non** |
| Avertissements A-L3 | — | **+1** |

**Le point qui compte.** S16 est la **seule** source non ouverte du chapitre.
Après réduction, les vingt et une entrées restantes sont toutes `ouverte` et
datées, et L1.C10 cesse d'être bloqué par E-L4.

**Le coût mécanique, et il est réel.** Un avertissement A-L3 s'ajoute — entrée
du manifeste sans occurrence — parce que S16 y figure comme occurrence
historique. **Un avertissement n'est pas un blocage**, et le précédent existe :
la réduction de L1.C09 en a produit quatre par la même logique.

---

## Premier appel, § 1

> …plusieurs centaines de chômeurs dans la ville, dont une part sans aucune
> indemnité, davantage encore dans le district, et quarante mille schillings en
> caisse [S1] **[S16]**.

**Devient** — seul le second marqueur disparaît :

> …plusieurs centaines de chômeurs dans la ville, dont une part sans aucune
> indemnité, davantage encore dans le district, et quarante mille schillings en
> caisse [S1].

**Motif, et il vaut indépendamment de la réduction.** C'est un **appel double où
une source non ouverte accompagne une source ouverte**, que la méthode arrêtée
le 2026-09-20 interdit explicitement. [S1] est ouverte et porte le chiffre. Le
retrait ne coûte donc **rien** : la phrase garde son appui intégral.

---

## Second appel, § 2

> Le recul du chômage d'environ un quart en un an, tandis qu'il augmente dans le
> reste de l'Autriche, est rapporté par von Muralt **[S16]**, dont le texte
> n'est pas ouvert : cet énoncé reste sans appui vérifié.

**Devient** — le marqueur disparaît, la phrase gagne un mot :

> Le recul du chômage d'environ un quart en un an, tandis qu'il augmente dans le
> reste de l'Autriche, est rapporté par von Muralt, dont le texte n'est pas
> ouvert **ici** : cet énoncé reste sans appui vérifié.

**Motif.** Comme dans L1.C13, l'appel désignait une pièce que la phrase déclare
dans le même souffle ne pas avoir ouverte. Le mot « ici » précise que la
fermeture vaut pour ce corpus et non pour la littérature.

---

## Ce qui est perdu, et c'est réel

**La référence bibliographique.** Le nom de von Muralt **reste dans le corps**,
mais l'article — revue, volume, pages, année, DOI — sort du chapitre. Un lecteur
qui voudrait vérifier l'énoncé du quart devra retrouver la référence lui-même.

C'est une perte plus lourde que dans L1.C13, où le corps ne nommait pas la loi :
ici, le chapitre continue d'attribuer un chiffre à un auteur nommé **sans
donner où le lire**. L'énoncé reste explicitement déclaré sans appui vérifié,
donc la prétention n'augmente pas — mais l'attribution perd sa piste.

**Une option existe, et elle appartient à l'auteur** : écrire la référence dans
le corps, en toutes lettres et sans appel — « rapporté par von Muralt dans les
*Annals of Public and Cooperative Economics* de 1934, texte non ouvert ici ».
Elle conserve la piste sans rétablir une source. Comme pour L1.C13, cette
option **ajoute** au corps et sort du périmètre d'une réduction : elle demande
une décision distincte.

**Ce qui n'est pas perdu.** Les deux autres chiffres qui circulent sur Wörgl —
la vitesse de circulation et les arriérés d'impôts — étaient déjà déclarés non
portés par le corpus. Le § 2 conserve cette déclaration inchangée.

---

## Effets de bord contrôlés

- **Le manifeste n'est pas touché.** `corpus/manifeste-etat-lecture.json` reste
  tel quel ; c'est lui qui produira l'avertissement A-L3, et il ne doit pas être
  édité pour le faire taire.
- **E-L6 n'est pas déclenché**, la référence de S16 n'étant pas modifiée mais
  l'entrée retirée en entier.
- **Renumérotation exclue.** Seul le bloc S16 est retiré ; S1 à S15 et S17 à S22
  gardent leurs identifiants.
- **Le statut ne change pas** par cette fiche. L1.C10 reste
  `audit_contradictoire` et devient *éligible* à `verifie`, sous la règle du
  2026-09-21 sur l'état final.
