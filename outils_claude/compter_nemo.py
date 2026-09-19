# -*- coding: utf-8 -*-
# Compte les formes de la famille NEMO dans TOUT le corpus, en separant :
#   - EN-TETE (metadonnees, entrees de source, verifications) et CORPS
#   - DANS UNE CITATION (entre guillemets) et EN VOIX PROPRE
# Aucun verdict : releve pour lecture humaine. Les chapitres sont nommes.
import io, os, re, sys, glob, collections
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
R = r"C:\Users\jcduv\Documents\GitHub\debunkonomy"

FORMES = [
    "NGSRD", "NGSDR", "NGDTS", "NGA",
    "NEMO Green Allocation", "NEMO Green SDR", "NEMO Green DTS",
    "NEMO IMS", "NEMO Exchange Standard", "NEMO SWIFT", "NEMO Clearing",
    "GAIA Economic Symposium", "GA\u00cfA Economic Symposium", "GES",
    "droit de tirage sp\u00e9cial", "droits de tirage sp\u00e9ciaux", "DTS", "SDR",
]
CITATION = re.compile(r"\u00ab[^\u00bb]{0,6000}\u00bb|\u201c[^\u201d]{0,6000}\u201d")

res = {f: {"tete": 0, "corps_cit": 0, "corps_propre": 0,
           "ch_corps": set(), "ch_propre": set(), "ch_tete": set()} for f in FORMES}
n = 0
for F in sorted(glob.glob(os.path.join(R, "corpus", "livre-*", "c*.md"))):
    t = io.open(F, encoding="utf-8").read()
    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    if not m:
        continue
    n += 1
    ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
    tete, corps = t[:m.end()], t[m.end():]
    masque = bytearray(len(corps))
    for c in CITATION.finditer(corps):
        for i in range(c.start(), c.end()):
            masque[i] = 1
    for f in FORMES:
        rx = re.compile(r"\b" + re.escape(f) + r"\b")
        k = len(rx.findall(tete))
        if k:
            res[f]["tete"] += k
            res[f]["ch_tete"].add(ch)
        for s in rx.finditer(corps):
            res[f]["ch_corps"].add(ch)
            if masque[s.start()]:
                res[f]["corps_cit"] += 1
            else:
                res[f]["corps_propre"] += 1
                res[f]["ch_propre"].add(ch)

out.write("%d chapitres balay\u00e9s\n\n" % n)
out.write("%-26s %6s %8s %9s %10s  %s\n"
          % ("forme", "en-t\u00eate", "corps/cit", "corps/VOIX", "ch. voix", "chapitres en voix propre"))
for f in FORMES:
    r = res[f]
    if not (r["tete"] or r["corps_cit"] or r["corps_propre"]):
        continue
    chs = sorted(r["ch_propre"])
    out.write("%-26s %6d %8d %9d %10d  %s\n"
              % (f, r["tete"], r["corps_cit"], r["corps_propre"], len(chs),
                 ", ".join(chs[:8]) + (" ..." if len(chs) > 8 else "")))
out.write("\nFORMES SANS AUCUNE OCCURRENCE : %s\n"
          % ", ".join(f for f in FORMES
                      if not (res[f]["tete"] or res[f]["corps_cit"] or res[f]["corps_propre"])))
out.flush()
