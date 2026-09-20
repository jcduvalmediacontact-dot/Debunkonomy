# -*- coding: utf-8 -*-
"""Contrôle final du renommage « sans dette » → nom canonique.

**Version par ancrage, du 2026-09-20**, seconde demande de la passe adverse.

La version précédente comptait par **chapitre et zone**. Elle avait un trou, que
la passe a nommé : *si une ancienne occurrence disparaît et qu'une autre apparaît
ailleurs dans le même corps, avec le même total, le contrôle passe.* Une
substitution à total constant n'était pas détectée.

Chaque occurrence déclarée porte donc désormais un **ancrage stable** : l'empreinte
d'un contexte normalisé — casse, espaces, apostrophes et guillemets écrasés —
pris autour du terme. Le contrôle compare les **multi-ensembles d'ancrages**, pas les
nombres. Une occurrence déplacée, une phrase réécrite autour d'elle, une phrase
neuve : les trois changent l'ancrage et font échouer le contrôle.

**Contrepartie assumée** : toute retouche éditoriale au voisinage d'une occurrence
déclarée casse son ancrage. C'est voulu — la remise à jour est alors un acte
délibéré, et non un silence.

    python outils_claude/controle_renommage.py [--liste]
    python outils_claude/controle_renommage.py --generer-ancrages   # après arbitrage
"""
import hashlib
import io
import json
import os
import re
import sys
import glob
import unicodedata
from collections import Counter

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANCRAGES = os.path.join(RACINE, "outils_claude", "ancrages-renommage.json")
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
LISTE = "--liste" in sys.argv
GENERER = "--generer-ancrages" in sys.argv
MARQUEUR = "RENOMMAGE CANONIQUE DU 2026-09-20"
LARGEUR = 70      # signes de contexte de part et d'autre du terme

# Motifs par chapitre. L'ancrage dit OÙ ; le motif dit POURQUOI.
MOTIFS = {
    "L1.C01": "notes seules",
    "L1.C08": "canonique et citable — lot public distinct",
    "L1.C10": "mots de Grandjean et Dufrêne, cités dans [S9] et décrits",
    "L1.C11": "canonique et citable — lot public distinct",
    "L1.C18": "notes seules",
    "L1.C19": "notes seules",
    "L1.C20": "notes seules — le chapitre porteur analyse l'ancien nom",
    "L1.C21": "notes seules",
    "L1.C29": "verrouillé jusqu'à la seconde passe de supervision",
    "L7.C11": "trace d'un arbitrage daté, attribuée",
    "L8.C02": "entrée `a_requalifier` — dette inscrite, E-L6 (P4)",
    "L8.C06": "entrée `a_requalifier` — dette inscrite, E-L6 (P18)",
    "L8.C38": "entrée `a_requalifier` — dette inscrite, E-L6 (P18)",
    "L10.C07": "trace d'une affirmation retirée",
    "L11.C01": "analyse de l'ancien nom — le chapitre établit ce qu'il coûte",
    "L11.C02": "l'alternative mise en balance",
    "L17.C01": "citation au mot de la promesse P9 — à migrer avec elle",
    "L17.C03": "citation au mot de la promesse P9 — à migrer avec elle",
    "L19.C01": "analyse historique : pourquoi le terme échoue",
    "L19.C03": "analyse historique : pourquoi le terme échoue",
    "L19.C07": "analyse historique : pourquoi le terme échoue",
    "L20.C25": "titre de section : analyse du terme — le renommer le détruirait",
    "L25.C03": "entrée `a_requalifier` — dette inscrite, E-L6",
}
IGNORES = re.compile("[\\s'’‘“”\"«»*_`—–-]+")


def empreinte(txt, i):
    """Empreinte d'un contexte normalisé : casse, espaces et ponctuation écrasés."""
    ctx = txt[max(0, i - LARGEUR):i + LARGEUR]
    n = IGNORES.sub("", unicodedata.normalize("NFKC", ctx)).lower()
    return hashlib.sha256(n.encode("utf-8")).hexdigest()[:16]


def releve():
    """Toutes les occurrences vivantes, avec leur ancrage. Aucun jugement."""
    trouve = []
    for F in sorted(glob.glob(os.path.join(RACINE, "corpus", "livre-*", "c*.md"))):
        t = io.open(F, encoding="utf-8").read()
        if "ERRATUM TERMINOLOGIQUE DU" in t or "NOTE TERMINOLOGIQUE DU" in t:
            continue
        m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
        if not m:
            continue
        ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
        tete, corps = t[:m.end()], t[m.end():]
        zones = [(x.start(), x.end()) for x in re.finditer(r'(?ms)^  - "(.*?)"$', tete)
                 if MARQUEUR in x.group(1)]
        for s in re.finditer("sans dette", tete, re.I):
            z = "notes" if any(a <= s.start() < b for a, b in zones) else "tete"
            trouve.append({"chapitre": ch, "zone": z, "ancrage": empreinte(tete, s.start()),
                           "extrait": re.sub(r"\s+", " ",
                                             tete[max(0, s.start() - 55):s.start() + 40])})
        for s in re.finditer("sans dette", corps, re.I):
            trouve.append({"chapitre": ch, "zone": "corps",
                           "ancrage": empreinte(corps, s.start()),
                           "extrait": re.sub(r"\s+", " ",
                                             corps[max(0, s.start() - 55):s.start() + 40])})
    return trouve


vivantes = releve()

if GENERER:
    inconnus = sorted({o["chapitre"] for o in vivantes} - set(MOTIFS))
    if inconnus:
        sys.exit("REFUS : chapitre(s) sans motif déclaré — %s.\n"
                 "        Un ancrage ne se génère pas sans sa raison." % ", ".join(inconnus))
    for o in vivantes:
        o["motif"] = MOTIFS[o["chapitre"]]
    io.open(ANCRAGES, "w", encoding="utf-8", newline="\n").write(
        json.dumps(sorted(vivantes, key=lambda o: (o["chapitre"], o["zone"], o["ancrage"])),
                   ensure_ascii=False, indent=2) + "\n")
    out.write("%d ancrage(s) écrit(s) dans %s\n"
              % (len(vivantes), os.path.relpath(ANCRAGES, RACINE)))
    sys.exit(0)

if not os.path.exists(ANCRAGES):
    sys.exit("fichier d'ancrages absent : lancer --generer-ancrages après arbitrage.")
declarees = json.loads(io.open(ANCRAGES, encoding="utf-8").read())

cle = lambda o: (o["chapitre"], o["zone"], o["ancrage"])
# MULTI-ensemble, et non ensemble : deux occurrences au contexte identique dans la
# même zone comptent pour deux. Sinon la disparition de l'une passerait inaperçue,
# ce qui est le défaut même que cette version corrige.
d_cnt, v_cnt = Counter(map(cle, declarees)), Counter(map(cle, vivantes))
disparues = [o for o in declarees if (d_cnt - v_cnt)[cle(o)]]
neuves = [o for o in vivantes if (v_cnt - d_cnt)[cle(o)]]

out.write("CONTRÔLE FINAL DU RENOMMAGE — par ancrage\n")
out.write("=" * 78 + "\n")
out.write("Chaque occurrence déclarée porte l'empreinte de son contexte normalisé.\n")
out.write("Une substitution à total constant est donc détectée.\n\n")
out.write("%d occurrence(s) déclarée(s), %d vivante(s), dans %d chapitre(s).\n"
          % (len(declarees), len(vivantes), len({o["chapitre"] for o in vivantes})))

if LISTE:
    out.write("\n%-9s %-6s %-18s %s\n" % ("chapitre", "zone", "ancrage", "extrait"))
    for o in sorted(vivantes, key=cle):
        etat = " " if d_cnt[cle(o)] else "+"
        out.write("%s%-8s %-6s %-18s …%s…\n"
                  % (etat, o["chapitre"], o["zone"], o["ancrage"], o["extrait"][:78]))

if disparues:
    out.write("\nDISPARUES — déclarées et introuvables (%d) :\n" % len(disparues))
    for o in disparues:
        out.write("  %-9s %-6s %-18s …%s…\n"
                  % (o["chapitre"], o["zone"], o["ancrage"], o["extrait"][:70]))
if neuves:
    out.write("\nNEUVES — vivantes et non déclarées (%d) :\n" % len(neuves))
    for o in neuves:
        out.write("  %-9s %-6s %-18s …%s…\n"
                  % (o["chapitre"], o["zone"], o["ancrage"], o["extrait"][:70]))

if disparues or neuves:
    out.write("\nÉCHEC. Le jeu d'ancrages a bougé. **Un total inchangé ne suffit plus** :\n")
    out.write("une occurrence déplacée ou une phrase réécrite autour d'elle change son\n")
    out.write("empreinte. Relire, arbitrer, puis relancer --generer-ancrages.\n")
    sys.exit(1)
out.write("\nCONTRÔLE PASSÉ : chaque occurrence vivante est déclarée à sa place exacte.\n")
