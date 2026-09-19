# Organisation des passes — qui produit, qui contrôle

**Arrêtée le 2026-09-19.** Elle remplace le fonctionnement où plusieurs modèles
cherchaient en parallèle. Motif donné par l'auteur : préserver la capacité du
superviseur sur toute la semaine, au lieu de l'épuiser en deux jours.

---

## 1. Les rôles

| | rôle | ce qu'il fait | ce qu'il ne fait pas |
|---|---|---|---|
| **Claude** | moteur | recherche documentaire, acquisition, **ouverture et qualification des sources**, rédaction et réécriture des chapitres, exécution des contrôles | — |
| **Codex** | superviseur indépendant | contrôle d'**attribution**, de **solidité logique**, de **cohérence avec le corpus**, de **régressions**, d'**erreurs mécaniques**. Propose des **corrections ciblées** | **n'engage aucune recherche de sa propre initiative** ; quand une source manque, **il la renvoie au lieu de la chercher** |
| **Gemini** | tiers ponctuel | recherche profonde ou audit alternatif, à la demande | rien n'entre au corpus sur sa seule foi |

**Codex n'intervient qu'aux jalons, et sur des états gelés.** Un état gelé est un
chapitre commité, dont l'arbre de travail est propre. Toute modification
postérieure périme le dossier.

**Ce que Gemini rapporte reste une piste.** La règle du projet ne change pas :
ses résultats sont **vérifiés sur les sources primaires avant toute
intégration**. La supervision de Codex, elle, porte sur un texte et ses sources
déjà ouvertes — c'est un contrôle, non une piste.

---

## 2. Le dossier compact — quatre pièces, et **le chapitre n'en fait pas partie**

**Le chapitre gelé existe déjà dans le dépôt. Le dossier ne le reproduit pas.**
C'est la règle qui décide de tout le reste : un dossier qui recopie le corps
coûte au superviseur ce que l'organisation cherche justement à lui épargner.

Chaque passe reçoit **exactement** :

1. **empreinte et chemin du chapitre** — plus statut, régime, autorité, commit de
   gel et propreté de l'arbre. L'empreinte permet de vérifier qu'on lit le bon
   état ;
2. **le résumé des changements et les extraits strictement touchés** — quelles
   sections ont bougé, de combien le corps a varié, et le diff des seules
   sections modifiées ;
3. **les sources et contrôles concernés** — pas toutes les sources : celles que
   la passe a touchées, plus celles qui restent non ouvertes, qui bloquent ;
4. **les faiblesses et incertitudes soumises expressément.**

**Le superviseur lit le chapitre dans le dépôt si, et seulement si, une faiblesse
ou un extrait le rend nécessaire.**

**La pièce 4 n'est pas facultative et l'outil refuse de produire un dossier sans
elle.** Un dossier muet sur ses faiblesses fait croire au superviseur qu'il n'y
en a pas, ce qui est toujours faux et lui fait perdre son temps à retrouver ce
que le producteur savait déjà.

### L'outil

```bash
python outils_claude/dossier_codex.py L1.C29 --depuis <ref> --faiblesses notes.md --sortie dossier.md
```

Il **rassemble et ne juge pas.** `--depuis` vaut par défaut le dernier commit
ayant touché le chapitre avant `HEAD` ; `--resume` accepte un résumé libre des
changements, que la machine ne sait pas écrire.

**Deux cas, et le second est fréquent.** Si quelques sections ont bougé, le
dossier en donne le diff, chaque extrait plafonné en signes — le corpus écrit des
paragraphes d'un seul tenant, et trois cents lignes peuvent faire soixante mille
signes. **Si la majorité des sections a bougé, le corps a été réécrit et non
retouché** : donner les extraits reviendrait à recopier le chapitre, et le
dossier le dit au lieu de le faire.

### Le test

```bash
python outils_claude/test_dossier_codex.py
```

Dix contrôles, dont ceux qui gardent le contrat : le refus sans faiblesses,
**l'absence du corps du chapitre dans le dossier**, la présence de l'empreinte,
la compacité sous trois mille mots, et **l'encodage**. Ce dernier a un motif
précis : sous Windows, un sous-processus écrit dans l'encodage de la console et
le verdict des contrôles arrive en mojibake. Un verdict illisible dans un dossier
de supervision est pire qu'absent — il se lit comme du bruit et se saute.

---

## 3. Ce que le retour de supervision peut contenir

- **Corrections ciblées** — appliquées après lecture, pas sur confiance.
  Une objection peut être bloquante et fausse : chaque citation d'un retour est
  recontrôlée sur le fichier avant d'être appliquée.
- **Demandes de recherche** — elles reviennent au moteur. C'est la règle, et
  elle préserve exactement la capacité que cette organisation veut préserver.
- **Sources signalées manquantes** — signalées, non cherchées.

**Ce qu'un retour de supervision ne peut pas faire :** ouvrir une source. La
qualification d'une source suppose d'avoir lu la pièce, et la pièce est du côté
qui l'a acquise.

---

## 4. Ce qui ne change pas

- **Aucun commit, aucune poussée, aucun archivage sans validation explicite de
  l'auteur** (`AGENTS.md`).
- **`controle.py` reste l'autorité.** Un dossier de supervision ne s'y substitue
  pas : il le rapporte.
- **Un résumé produit par un modèle ne vaut pas ouverture de source.** Y compris
  un outil qui « récupère » une page en la faisant résumer.
- **La séquence du registre canonique tient** : arbitrage des sept points, mise à
  jour du registre, audit contradictoire, et seulement alors propagation
  (`protocoles/registre-canonique-nemo-ims.md`, § 8).
