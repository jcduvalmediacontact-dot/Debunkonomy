# Relevé de génération pour Codex — 2026-09-25

**Le nom de ce fichier dit « seize » ; le générateur en émet dix-sept.** Il garde
le nom que l'ordre du jour lui donne, pour que Codex le trouve ; le compte
ci-dessous est celui du jour.

**Tous les nombres de ce relevé sont calculés à l'écriture**, aucun n'est recopié
d'une sortie lue à l'œil.

---

## Ce que le générateur émet

| | |
|---|---|
| chapitres publiables, comptés sur les en-têtes | **17** |
| chapitres écartés | **318** |
| fichiers émis, suivis par git sous `corpus/` | **43** |
| fichiers de la construction `build/` | **545**, 45.9 Mo |

Les publiables : L1.C01, L1.C02, L1.C03, L1.C04, L1.C05, L1.C06, L1.C07, L1.C08, L1.C09, L1.C10, L1.C11, L1.C12, L1.C13, L1.C14, L1.C15, L1.C16, L1.C31.

Motifs d'écart, comptés :

- statut brouillon : **318**

## Les sitemaps

| | |
|---|---|
| URL du `sitemap.xml` de la racine | **225** |
| URL du sitemap fusionné dans `build/` | **245** |
| dont sous `/corpus/` | **20** |
| URL en double | **0** |

Racine `urlset` dans l'espace officiel `http://www.sitemaps.org/schemas/sitemap/0.9`,
sans préfixe. Il y avait 774 préfixes `ns0:`/`ns1:` le 2026-09-24.

## Le diff contre `main`

`main` porte **494** fichiers, `dev` **1030**. Une PR ajouterait
**536** fichiers et en retirerait **0**.

- `corpus` : **407**
- `protocoles` : **95**
- `outils_claude` : **18**
- `modeles` : **10**
- `(racine)` : **4**
- `outils` : **2**

**Dont 43 fichiers générés** — ceux que le site doit servir sous
`/corpus/`. Le reste de `corpus/` est constitué des **364 fichiers
sources**, qui seront servis aussi : l'auteur l'a tranché le 2026-09-25 après
mesure, sachant que `debunkonomy.org/AGENTS.md` répond 200 et que `main` sert
donc tout ce qu'il reçoit.

**Fichiers du site existant modifiés par ce diff : 21.** Et la
distinction compte, parce que **le critère de l'ordre 1 ne peut pas être rempli
tel qu'il est écrit** — il attend « aucun fichier du site existant modifié hors
`sitemap.xml` et `llms.txt` ».

**20 divergeaient déjà avant aujourd'hui**, accumulés sur `dev` depuis
`5d2b3a46`, l'ancêtre commun du 2 septembre : `AGENTS.md`, `articles/auteur/SMI-4/index.html`, `articles/auteur/a-quoi-doit-servir-une-monnaie-au-xxie-siecle/index.html`, `articles/auteur/creation-monetaire-dette/index.html`, `articles/auteur/essentiel-insolvable-comment-le-financer/index.html`, `articles/auteur/neobanques-vertes-impasse-monnaie-dette/index.html` et 14 autres.

**Un seul relève du travail du jour** : `sitemap.xml`.

Autrement dit : la PR emporterait 20 fichiers du site édités entre le 2
et le 24 septembre, que personne n'a relus dans ce fil. Ce n'est pas un effet du
corpus, et un relevé qui donnerait « 21 » sans cette distinction le lui
ferait imputer. Le `llms.txt` de la racine, lui, **n'est pas modifié** — le
générateur produit le sien à côté.

---

## Ce que Codex doit pouvoir vérifier

1. **Espace officiel partout** — la fusion refuse désormais trois cas : espaces
   différents entre les deux fichiers, espace hors norme, entrée sans `<loc>`.
   Les trois refus sont éprouvés sur cas fabriqués.
2. **245 URL uniques**, 20 sous `/corpus/`.
3. **17 pages de chapitre sous `/corpus/livre-1/`.**
4. **Aucun fichier du site existant modifié hors ceux listés ci-dessus.**
5. **Ni `corpus/` source, ni `protocoles/`, ni `coordination/` dans la sortie
   `build/`** — vérifié par contrôle négatif : aucun `.md` hors corpus, aucun
   `.git`, aucun `.build-env`.

## Ce que ce relevé n'établit pas

**Que la PR soit sans conséquence.** Elle sert 364 fichiers sources à des
URL stables du domaine, dont les 318 chapitres que la convention refuse de
publier. C'est une décision d'auteur, prise après mesure, et non un effet de
bord — mais elle ne se lit nulle part dans les nombres ci-dessus.

**Que les pages soient justes.** Le générateur n'émet que ce que la convention
autorise ; il ne relit pas ce qu'il émet.
