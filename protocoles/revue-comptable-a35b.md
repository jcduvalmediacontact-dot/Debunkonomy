# Note de revue — qualification comptable d'une unité monétaire émise sans dette

**Destinataire : un comptable national, ou un spécialiste des bilans de banque
centrale.**
**Objet : valider ou infirmer une lecture de la norme, non commenter un projet.**
**Date : 2026-09-09. Pièce jointe : `modeles/a35b_bilans.py` et
`modeles/test_a35b.py`, exécutables, sans dépendance.**

---

## 1. Ce qui vous est demandé, en une phrase

Un programme écrit les bilans de sept secteurs pour quatorze architectures
possibles d'un même instrument. Il calcule des identités comptables, et il
**propose** une qualification. **Nous vous demandons si cette proposition tient,
et à quelles conditions.** Nous ne vous demandons pas si le dispositif est
souhaitable.

## 2. Ce que le programme calcule, et ce qu'il ne fait que proposer

| | |
|---|---|
| **R1a — cohérence arithmétique** | **Vérifiée mécaniquement, selon les écritures posées.** Équilibre par secteur à chaque opération ; miroirs des encours croisés ; somme des variations de situation nette nulle à chaque flux ; et l'identité *total des passifs représentatifs de l'unité, quel qu'en soit le porteur = total des avoirs chez les détenteurs*, contrôlée **à chaque étape**. **Le programme ne juge pas la validité de la représentation : des écritures fausses peuvent s'équilibrer parfaitement.** |
| **R1b — qualification comptable** | **Proposée, non calculée.** Le programme constate que des éléments sont renseignés et que la créance suit son détenteur. Il n'écrit jamais qu'un élément « est » un passif. |
| **R2 — liquidité** | **Calculée**, au pic et par scénario séparé — **mais conditionnelle** : aucun des paramètres n'est calibré, et changer un seul change le résultat. |
| **R3 — solvabilité intertemporelle** | **Non évaluable** : un seul cycle, sans intérêt ni horizon. |
| **R4a — conception juridique** | **À produire.** Une institution prospective écrit son droit constitutif : droits, obligations, gouvernance, retrait, liquidation, immunités, différends. Aucun texte n'existe. |
| **R4b — compatibilité juridique** | **À évaluer, non évaluée.** Traités, droits nationaux et régionaux, normes comptables. |

## 3. L'hypothèse de lecture que nous vous demandons de juger

Nous retenons qu'un élément peut être proposé comme passif lorsque **quatre**
éléments sont réunis, tirés de l'édition 2025 du système de comptabilité
nationale, lue dans le texte :

1. une **obligation** — « *Liabilities are defined as obligations where one unit
   (the debtor) is obliged, under specific circumstances, to provide funds or
   other economic resources to another unit (the creditor)* » (§ 4.101) ;
2. un **débiteur déterminé** ;
3. un ou plusieurs **créanciers** ;
4. la **créance correspondante** effectivement inscrite chez ces créanciers —
   « *Whenever a liability exists, there is a corresponding financial claim that
   the creditor has against the debtor [...] Like the liabilities, the claims are
   unconditional* » (§ 4.103).

**Question 1. Cette lecture est-elle correcte, ou incomplète ?** En particulier,
le § 4.102 admet des passifs *constructifs*, nés de la coutume et d'une attente
légitime de paiement, sans contrat. **Notre modèle ne les représente pas.**

## 4. Les quatre points sur lesquels votre jugement décide du résultat

**QUESTION 2 — LE CRÉANCIER D'UN INSTRUMENT TRANSFÉRABLE.** Nous traitons le
créancier comme **dynamique** : à chaque étape, les créanciers sont les
détenteurs du moment, et la créance de chacun vaut son encours. Une version
antérieure figeait un créancier unique dans une fiche, ce qui était faux dès que
l'instrument change de mains. **Est-ce le bon traitement ?**

**QUESTION 3 — UNE OBLIGATION D'ACCEPTATION SANS DETTE EN FACE.** L'instrument
donne à son détenteur le droit de le remettre à l'émetteur en règlement de ce
qu'il lui doit. **Si aucune dette de ce genre n'existe chez un détenteur, ce
droit reste-t-il une obligation présente de l'émetteur, ou une simple
possibilité future ?** Le programme distingue les deux cas et suspend sa
proposition dans le second (branches B2 et B12, à comparer).

**QUESTION 4 — INSUFFISANCE D'ACTIFS ET EXISTENCE DU PASSIF.** Nous tenons
désormais qu'un émetteur promettant une conversion à vue sans détenir de quoi la
servir **porte bien un passif**, assorti d'un risque de liquidité. Une version
antérieure concluait à tort que l'écriture n'existait pas. **Confirmez-vous que
l'insuffisance d'actifs ne fait pas disparaître le passif, y compris pour une
institution dont la situation nette devient négative ?**

**QUESTION 5 — DEUX ARCHITECTURES CONCURRENTES.** Le modèle compare deux
placements du passif :

- **chez l'émetteur**, pour la totalité de l'encours ;
- **chez chaque membre receveur**, pour sa propre allocation — traitement que la
  norme retient pour les droits de tirage spéciaux : « *Holdings of SDRs by an
  IMF member are recorded as a financial asset, while the allocation of SDRs is
  recorded as the incurrence of a liability of the member receiving them
  (because of a requirement to repay the allocation in certain circumstances, and
  also because interest accrues). The holdings and allocations should be shown
  gross, rather than net* » (§ 12.49), le droit s'exerçant « *from other IMF
  members* » (§ 25.142).

**Ces deux architectures sont-elles également représentables ? Et le second
traitement suppose-t-il des éléments que notre modèle omet ?**

## 5. Ce que nous savons manquer

- **Ni intérêt ni horizon.** Or le § 12.49 fonde le passif d'allocation sur une
  obligation de remboursement **et** sur le fait qu'un intérêt court. Nous ne
  pouvons éprouver ni ce motif ni la solvabilité intertemporelle.
- **Aucune obligation modélisée n'existe dans un texte de droit.** Ni
  l'obligation d'acceptation, ni l'engagement de conversion, ni le régime des
  contributions réglables en unités.
- **Le plafond de désignation est sourcé depuis le 2026-09-09** — article XIX
  § 4(a) des Statuts du Fonds, lu dans le texte. **Sa lecture a corrigé une
  erreur du modèle** : c'est l'excédent sur l'allocation qui est borné à deux
  allocations, de sorte que le plafond total des avoirs vaut trois allocations.
  **Ce qui reste hors des Statuts, ce sont les accords d'échange volontaire**,
  dont dépend la liquidité en régime ordinaire, et dont nous ne tenons ni la
  liste ni les montants.
- **Aucun comportement économique.** Le modèle **impose par paramètre** qui est
  redevable, puis retrouve ce qu'il a imposé. **Il n'établit donc aucune
  incidence économique**, et rien de ce qu'il affiche ne doit être lu comme telle.
- **Quatorze branches ne sont pas l'espace des branches possibles.** Une branche
  qui n'est pas écrite n'est pas rejetée : elle est absente.

## 6. Deux résultats que nous soumettons, et qui nous surprennent

**LE CONTRÔLE AU PIC.** Une conversion promise « à tout moment » ne se contrôle
pas sur le bilan final. Dans notre branche à capital souscrit, le bilan final
affiche une couverture exacte, **et la chronologie montre un découvert dès la
première étape**, qui persiste jusqu'à la fin du reflux. **Confirmez-vous que le
pic est la bonne mesure ?**

**LE COLLECTEUR ET L'EMPLOI.** Le dispositif reprend des unités par deux
mécanismes distincts : un prélèvement sur les transactions et une charge sur les
encaisses détenues. **Selon que l'émetteur ou l'État perçoit le premier, l'unité
perçue est éteinte ou seulement déplacée** ; et si l'État perçoit, ce qu'il en
fait ensuite — conserver, remettre en circulation, reverser à l'émetteur —
décide de l'encours final. **Le collecteur ne décide que de la première
destination.** Nous ne trouvons pas ce point traité dans la littérature que nous
avons lue, et nous demandons s'il est trivial ou s'il a été manqué.

## 7. Comment vérifier vous-même

```bash
python modeles/a35b_bilans.py    # les quatorze branches, avec leur chronologie
python modeles/test_a35b.py      # sabotage de chaque règle, pour vérifier qu'elle mord
```

Le second fichier **casse délibérément chaque règle** et exige que le contrôle
correspondant la voie. **Il établit que le programme applique ses règles ; il
n'établit pas qu'elles sont fondées** — c'est précisément ce que nous vous
demandons.

Pour ajouter une architecture : une entrée dans la liste `BRANCHES`, avec ses
axes et sa fiche. Les écritures s'en déduisent. **Une contradiction chiffrée nous
sera plus utile qu'un accord.**
