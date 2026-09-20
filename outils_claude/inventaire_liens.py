# -*- coding: utf-8 -*-
"""Inventaire des liens qui dépendent d'un chemin, AVANT de le renommer.

Cherche dans TOUT le dépôt — pas seulement dans `corpus/` — les mentions d'un
fragment de chemin : protocoles, outils, site, manifestes, index, générateur,
documentation, coordination. Ne modifie rien.

    python outils_claude/inventaire_liens.py c20-de-l-argent-sans-dette [autre-fragment…]

Le décompte est par fichier et par périmètre, avec le contexte de chaque
occurrence : un renommage se prépare sur des lignes, pas sur un total.
"""
import io
import os
import re
import sys
import collections

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)

IGNORE_DOSSIERS = {".git", "node_modules", "genere", "__pycache__", ".claude"}
EXTENSIONS = {".md", ".yaml", ".yml", ".json", ".html", ".xml", ".py", ".txt", ".css", ".js"}


def perimetre(rel):
    tete = rel.split("/")[0]
    if tete in ("corpus", "protocoles", "outils_claude", "coordination"):
        return tete
    return "site"


def fichiers():
    for racine, dossiers, noms in os.walk(RACINE):
        dossiers[:] = [d for d in dossiers if d not in IGNORE_DOSSIERS]
        for n in noms:
            if os.path.splitext(n)[1].lower() in EXTENSIONS:
                yield os.path.join(racine, n)


fragments = sys.argv[1:]
if not fragments:
    sys.exit("usage : inventaire_liens.py <fragment-de-chemin> [autre…]")

par_frag = {f: collections.defaultdict(list) for f in fragments}
for F in sorted(fichiers()):
    rel = os.path.relpath(F, RACINE).replace("\\", "/")
    try:
        t = io.open(F, encoding="utf-8").read()
    except Exception:
        continue
    for frag in fragments:
        if frag in rel:
            par_frag[frag][rel].append(("(le chemin du fichier lui-même)", 0))
        for m in re.finditer(re.escape(frag), t):
            ligne = t.count("\n", 0, m.start()) + 1
            ctx = re.sub(r"\s+", " ", t[max(0, m.start() - 70):m.start() + len(frag) + 40])
            par_frag[frag][rel].append((ctx, ligne))

for frag in fragments:
    liens = par_frag[frag]
    total = sum(len(v) for v in liens.values())
    out.write("\n%s\n" % ("=" * 78))
    out.write("FRAGMENT : %s\n" % frag)
    out.write("%s\n" % ("=" * 78))
    if not liens:
        out.write("  AUCUN LIEN. Le renommage est sans conséquence.\n")
        continue
    par_per = collections.Counter()
    for rel, occ in liens.items():
        par_per[perimetre(rel)] += len(occ)
    out.write("  %d occurrence(s) dans %d fichier(s)\n" % (total, len(liens)))
    out.write("  par périmètre : %s\n\n"
              % ", ".join("%s %d" % (k, v) for k, v in par_per.most_common()))
    for rel in sorted(liens):
        out.write("  --- %s (%d)\n" % (rel, len(liens[rel])))
        for ctx, ligne in liens[rel][:6]:
            out.write("      l.%-5s …%s…\n" % (ligne or "-", ctx))
        if len(liens[rel]) > 6:
            out.write("      … et %d autre(s)\n" % (len(liens[rel]) - 6))
out.flush()
