# Ordre 7 — le déploiement, préparé

**Rien n'est appliqué.** Le diff est soumis ; le suivi de
`outils/construire_site.py` attend l'accord de l'auteur.

**Le fichier a été lu en entier** — 88 lignes — avant d'être proposé au suivi.
Un fichier qu'on verse au dépôt public est un fichier qu'on a lu.

---

## Ce que le script fait

`python outils/construire_site.py` assemble une prévisualisation locale dans
`build/`, jamais versionnée. Dans l'ordre : il lance `corpus/controle.py` et
s'arrête si le contrôle échoue ; il copie la racine du site dans un dossier
temporaire en écartant les sources et les notes privées ; il appelle
`corpus/generer.py --sortie … --base /corpus` ; il déplace la sortie sous
`/corpus` ; il fusionne les sitemaps **sans réécrire les URL déjà servies** ;
puis il renomme le temporaire en `build/`.

**Ce qu'il écarte** : `.git`, `.claude`, `build`, `corpus`, `coordination`,
`protocoles`, `outils`, `outils_claude`, `Codex`, `tmp`, `__pycache__`, et
**tous les `.md`**. Les sources du corpus ne sont jamais copiées : seul
`generer.py` émet sous `/corpus`, et il n'émet que ce que la convention
autorise — aujourd'hui quatorze chapitres.

---

## Deux écarts trouvés, et le second est celui que « vérifier » devait attraper

**`build/` est bien ignoré** (`.gitignore` l. 51), ainsi que `.build-env/`
(l. 52). **Mais le script ne travaille pas dans ces dossiers-là.** Il utilise
`.build-en-cours`, qui **n'est pas ignoré** :

```python
TEMPORAIRE = RACINE / ".build-en-cours"   # ligne 22
```

Une exécution interrompue entre la copie et le renommage final laisse donc
**une copie complète du site, non suivie, à la racine du dépôt**. Le commentaire
ajouté ce matin à `.gitignore` annonçait couvrir la sortie du script ; il
nommait le mauvais dossier.

**`.build-env/` serait copié dans la construction.** Il est à la racine, il
n'est pas dans `EXCLUS`, et `ignorer()` ne rejette que les noms de cette liste
et les `.md`. Un environnement virtuel Python entrerait donc dans `build/`.
Même remarque pour `PLAN-DIRECTEUR-2026-09-04.pdf`, qui est à la racine.

**Je ne corrige pas le script** : l'ordre 7 demande de le suivre et de le
documenter, pas de le modifier. Les deux points sont signalés pour décision.

---

## Diff soumis — `.gitignore`

```diff
 # Construction locale du site et du corpus. Cette sortie est reconstruite par
 # outils/construire_site.py ; elle n'est jamais une source à versionner.
 build/
+.build-en-cours/
 .build-env/
```

Une ligne. Sans elle, le dossier de travail du script apparaît dans
`git status` dès qu'une exécution est interrompue.

---

## Diff soumis — `CLAUDE.md`, § « Écarts connus », à la suite du bloc du générateur

```diff
+- **La construction locale du site existe : `outils/construire_site.py`.**
+  Elle assemble dans `build/` — jamais versionné — le site statique de la
+  racine et la sortie de `corpus/generer.py` servie sous `/corpus`, puis
+  fusionne les deux `sitemap.xml` **sans réécrire les URL déjà servies**. Le
+  contrôle structurel doit passer d'abord, et les chapitres non publiables ne
+  sont pas une erreur : le générateur les écarte lui-même selon la convention.
+
+  ```bash
+  python outils/construire_site.py          # assemble dans build/
+  ```
+
+  **Ce qui reste ouvert.** La construction n'est ni déployée ni poussée vers
+  `main` : elle produit une prévisualisation locale, et rien d'autre. Le choix
+  de l'emplacement de la sortie dans l'arbre servi, et le lien corpus ↔ site
+  décrit ci-dessous, restent à trancher. Deux défauts sont connus et non
+  corrigés : le dossier temporaire `.build-en-cours` n'était pas ignoré avant
+  le 2026-09-23, et `.build-env/` n'est pas dans la liste d'exclusion du
+  script, donc serait copié dans la sortie.
```

---

## Ce que ce lot ne fait pas

Aucune génération publiée, aucune poussée vers `main`, aucune modification du
script. Le suivi de `outils/construire_site.py` — 88 lignes, un seul fichier —
attend votre accord, et entrerait avec les deux diffs ci-dessus.
