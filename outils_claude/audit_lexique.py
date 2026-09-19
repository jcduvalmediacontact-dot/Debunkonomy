# -*- coding: utf-8 -*-
# Audit lexical du corpus, deuxieme tranche : les formes concurrentes des composants du
# dispositif. Separe en-tete / corps et citation / voix propre. Aucun verdict.
import io, os, re, sys, glob
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
R = r"C:\Users\jcduv\Documents\GitHub\debunkonomy"

GROUPES = {
    "Gouvernance du Symposium": [
        "quatre chambres", "cinq coll\u00e8ges", "cinq chambres", "quatre coll\u00e8ges",
        "coll\u00e8ges", "Assembl\u00e9e des Communs", "cinq fonctions",
        "cinq centres de responsabilit\u00e9", "Office",
    ],
    "Les deux circuits": [
        "circuit Yin", "circuit Yang", "Yin et le Yang", "deux circuits",
        "deux orientations", "deux portes",
    ],
    "Instruments de reflux": [
        "fontes diff\u00e9renci\u00e9es", "fonte diff\u00e9renci\u00e9e", "d\u00e9murrage", "demurrage",
        "reflux transactionnel", "reflux collectif", "reflux structurel",
        "monnaie fondante",
    ],
    "Contrepartie et qualification": [
        "certificat de qualification r\u00e9g\u00e9n\u00e9rative", "certificat de qualification",
        "qualification r\u00e9g\u00e9n\u00e9rative", "cr\u00e9ance sur les fontes futures",
        "cr\u00e9ance sur reflux futurs", "activit\u00e9 r\u00e9g\u00e9n\u00e9rative", "essentiel insolvable",
        "d\u00e9g\u00e9n\u00e9ratif",
    ],
    "Mesure": [
        "tableau de bord multidimensionnel", "tableau de bord", "six familles",
        "bar\u00e8me", "limites plan\u00e9taires",
    ],
}
CITATION = re.compile(r"\u00ab[^\u00bb]{0,6000}\u00bb|\u201c[^\u201d]{0,6000}\u201d")

FICH = sorted(glob.glob(os.path.join(R, "corpus", "livre-*", "c*.md")))
donnees = {}
for grp, formes in GROUPES.items():
    for f in formes:
        donnees[f] = {"tete": 0, "cit": 0, "propre": 0, "ch": set(), "livres": set()}

for F in FICH:
    t = io.open(F, encoding="utf-8").read()
    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    if not m:
        continue
    ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
    livre = ch.split(".")[0]
    tete, corps = t[:m.end()], t[m.end():]
    masque = bytearray(len(corps))
    for c in CITATION.finditer(corps):
        for i in range(c.start(), c.end()):
            masque[i] = 1
    for f in donnees:
        rx = re.compile(re.escape(f), re.I)
        donnees[f]["tete"] += len(rx.findall(tete))
        for s in rx.finditer(corps):
            if masque[s.start()]:
                donnees[f]["cit"] += 1
            else:
                donnees[f]["propre"] += 1
                donnees[f]["ch"].add(ch)
                donnees[f]["livres"].add(livre)

for grp, formes in GROUPES.items():
    out.write("\n=== %s ===\n" % grp)
    out.write("%-40s %6s %5s %7s %5s  %s\n"
              % ("forme", "t\u00eate", "cit", "VOIX", "ch.", "livres"))
    for f in formes:
        d = donnees[f]
        if not (d["tete"] or d["cit"] or d["propre"]):
            out.write("%-40s %6s %5s %7s %5s  \u2014 AUCUNE OCCURRENCE\n" % (f, "", "", "", ""))
            continue
        lv = sorted(d["livres"], key=lambda x: (len(x), x))
        out.write("%-40s %6d %5d %7d %5d  %s\n"
                  % (f, d["tete"], d["cit"], d["propre"], len(d["ch"]), ", ".join(lv[:10])))
out.flush()
