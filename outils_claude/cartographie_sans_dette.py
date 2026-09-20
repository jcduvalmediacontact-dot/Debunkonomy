# -*- coding: utf-8 -*-
"""Cartographie des occurrences de « sans dette » dans tout le dépôt.

Prépare le renommage canonique vers « monnaie régénérative à contrepartie
collective ». NE REND AUCUN VERDICT et NE MODIFIE RIEN : il relève.

Trois séparations, et la troisième est la seule que la machine ne sait pas faire :

  - PÉRIMÈTRE   : corpus / protocoles / coordination / site — et dans le corpus,
                  en-tête (métadonnées, sources, vérifications) ou corps ;
  - CITATION    : entre guillemets français ou anglais, ou dans un bloc `> ` ;
  - EMPLOI vs MENTION : indétectable mécaniquement. Une occurrence qui ANALYSE le
                  terme n'est pas une occurrence qui l'EMPLOIE. Le relevé les
                  compte ensemble et signale les fichiers à relire à l'œil.

    python outils_claude/cartographie_sans_dette.py [--detail]
"""
import io
import os
import re
import sys
import glob
import collections

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
DETAIL = "--detail" in sys.argv

FORMES = [
    "monnaie sans dette",
    "argent sans dette",
    "émission sans dette",
    "création monétaire sans dette",
    "monnaie émise sans dette",
    "sans dette",          # le plus large : contient les precedents
]
CITATION = re.compile(r"«[^»]{0,6000}»|“[^”]{0,6000}”")
# fichiers d'archive : on n'y touche pas, on y ajoute au plus un erratum
ARCHIVE = re.compile(r"(rapport-audit|dossier-audit|verification-audit|audit-codex|"
                     r"passe-2|BILAN|ARCHIVE)", re.I)


def perimetre(chemin):
    r = os.path.relpath(chemin, RACINE).replace("\\", "/")
    if r.startswith("corpus/"):
        return "corpus"
    if r.startswith("protocoles/"):
        return "protocoles"
    if r.startswith("coordination/"):
        return "coordination"
    if r.startswith("outils_claude/"):
        return "outils"
    return "site"


def fichiers():
    vus = set()
    for motif in ("corpus/**/*.md", "corpus/*.yaml", "protocoles/**/*.md",
                  "coordination/**/*.md", "*.md", "*.html", "*.json",
                  "livre/**/*.html", "articles/**/*.html", "manifeste/**/*.html"):
        for f in glob.glob(os.path.join(RACINE, motif), recursive=True):
            if os.path.isfile(f) and f not in vus:
                vus.add(f)
                yield f


par_perimetre = collections.Counter()
par_forme = collections.Counter()
fichiers_touches = collections.defaultdict(lambda: collections.Counter())
a_relire = []
slugs = []
titres = []

for F in sorted(fichiers()):
    try:
        t = io.open(F, encoding="utf-8").read()
    except Exception:
        continue
    rel = os.path.relpath(F, RACINE).replace("\\", "/")
    if "sans dette" not in t.lower() and "sans-dette" not in rel.lower():
        continue
    p = perimetre(F)
    arch = bool(ARCHIVE.search(rel))

    if "sans-dette" in rel.lower():
        slugs.append(rel)

    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    zones = [("en-tête", t[:m.end()]), ("corps", t[m.end():])] if m else [("fichier", t)]

    for zone, txt in zones:
        masque = bytearray(len(txt))
        for c in CITATION.finditer(txt):
            for i in range(c.start(), c.end()):
                masque[i] = 1
        for i, l in enumerate(txt.split("\n")):
            pass
        # les lignes de citation en bloc `> ` comptent aussi comme citation
        pos = 0
        for l in txt.split("\n"):
            if l.lstrip().startswith(">"):
                for i in range(pos, min(pos + len(l), len(masque))):
                    masque[i] = 1
            pos += len(l) + 1

        for s in re.finditer(r"sans dette", txt, re.I):
            cite = bool(masque[s.start()])
            cle = (p, zone, "citation" if cite else "voix propre",
                   "archive" if arch else "vivant")
            par_perimetre[cle] += 1
            fichiers_touches[rel][cle] += 1
            if not cite and not arch:
                a_relire.append((rel, zone, re.sub(r"\s+", " ",
                                                   txt[max(0, s.start() - 90):s.start() + 70])))
    for f in FORMES[:-1]:
        par_forme[f] += len(re.findall(re.escape(f), t, re.I))
    for mm in re.finditer(r"(?m)^(titre|#)\s*:?\s*(.*sans dette.*)$", t, re.I):
        titres.append((rel, mm.group(2).strip()[:70]))

out.write("CARTOGRAPHIE « sans dette » — préparation du renommage canonique\n")
out.write("=" * 78 + "\n\n")

out.write("1. PAR FORME (toutes zones, tous périmètres)\n")
for f in FORMES[:-1]:
    out.write("   %-34s %4d\n" % ("« %s »" % f, par_forme[f]))
out.write("   %-34s %4d\n" % ("« sans dette », total",
                              sum(par_perimetre.values())))
out.write("\n2. PAR PÉRIMÈTRE, ZONE, ET NATURE\n")
out.write("   %-13s %-9s %-13s %-9s %5s\n"
          % ("périmètre", "zone", "voix/citation", "état", "n"))
for cle in sorted(par_perimetre, key=lambda k: (-par_perimetre[k], k)):
    p, zone, voix, etat = cle
    out.write("   %-13s %-9s %-13s %-9s %5d\n" % (p, zone, voix, etat, par_perimetre[cle]))

out.write("\n3. FICHIERS, par nombre d'occurrences\n")
rangs = sorted(fichiers_touches.items(), key=lambda kv: -sum(kv[1].values()))
for rel, c in rangs[:28]:
    vivantes = sum(v for k, v in c.items() if k[2] == "voix propre" and k[3] == "vivant")
    out.write("   %-72s %3d  dont %2d en voix propre vivante\n"
              % (rel[:72], sum(c.values()), vivantes))
if len(rangs) > 28:
    out.write("   … et %d autre(s) fichier(s)\n" % (len(rangs) - 28))

out.write("\n4. SLUGS ET CHEMINS contenant « sans-dette »\n")
for s in slugs or ["   (aucun)"]:
    out.write("   %s\n" % s)

out.write("\n5. TITRES contenant « sans dette »\n")
for rel, ti in titres or [("   (aucun)", "")]:
    out.write("   %-64s %s\n" % (rel[:64], ti))

out.write("\n6. À RELIRE À L'ŒIL — voix propre, hors archive : %d occurrence(s)\n"
          % len(a_relire))
out.write("   La machine ne distingue pas l'EMPLOI de la MENTION. Chacune de ces\n")
out.write("   occurrences doit être lue avant d'être touchée.\n")
if DETAIL:
    for rel, zone, ctx in a_relire:
        out.write("\n   --- %s (%s)\n   …%s…\n" % (rel, zone, ctx))
else:
    out.write("   (relancer avec --detail pour le contexte de chacune)\n")
out.flush()
