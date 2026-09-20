# -*- coding: utf-8 -*-
"""Contrôle final du renommage « sans dette » → nom canonique.

**Ce qu'il compte, et rien d'autre** : les occurrences de l'ancien terme dans les
**corps, titres et métadonnées** des chapitres, **en voix propre**.

**Ce qu'il exclut, et c'est ce qui le rend utilisable** :
  - les **citations** — entre guillemets français ou anglais, ou en bloc `> ` ;
  - les **archives** et les fichiers portant un **erratum** daté ;
  - les **analyses de l'ancien terme** — les entrées de vérification qui portent
    le marqueur du renommage, et qui nomment l'ancien nom pour dire qu'il l'est.

Le décompte brut du dépôt a cessé d'être une mesure : les notes et errata citent
eux-mêmes l'ancien terme pour l'abandonner, de sorte que le total MONTE quand le
travail avance. Ce contrôle mesure ce qui reste à faire, pas ce qui est écrit.

Sortie : la liste des survivances, chacune devant être justifiée, et un code de
sortie non nul si une survivance n'est pas dans la table des exceptions.

    python outils_claude/controle_renommage.py [--liste]
"""
import io
import os
import re
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
LISTE = "--liste" in sys.argv

TERME = re.compile(r"sans dette", re.I)
CITATION = re.compile(r"«[^»]{0,6000}»|“[^”]{0,6000}”")
MARQUEUR = "RENOMMAGE CANONIQUE DU 2026-09-20"

# Les douze survivances justifiees, arretees le 2026-09-20. Chacune porte son motif.
EXCEPTIONS = {
    "L11.C01": (3, "analyse de l'ancien nom : le chapitre établit que la lecture B en "
                   "coûte l'appellation « au sens fort »"),
    "L1.C08": (2, "chapitre canonique et citable — lot public distinct"),
    "L1.C11": (1, "chapitre canonique et citable — lot public distinct"),
    "L1.C29": (2, "verrouillé jusqu'à la seconde passe de supervision"),
    "L10.C07": (2, "trace d'une affirmation retirée : on ne retire pas sous un nom jamais "
                   "porté"),
    "L1.C10": (1, "mots de Grandjean et Dufrêne, cités dans [S9]"),
    "L11.C02": (1, "l'alternative mise en balance : « sans dette ou financée par "
                   "prélèvement »"),
}


def masque_citations(txt):
    m = bytearray(len(txt))
    for c in CITATION.finditer(txt):
        for i in range(c.start(), c.end()):
            m[i] = 1
    pos = 0
    for l in txt.split("\n"):
        if l.lstrip().startswith(">"):
            for i in range(pos, min(pos + len(l), len(m))):
                m[i] = 1
        pos += len(l) + 1
    return m


def zones_de_note(tete):
    """Positions couvertes par une entrée de vérification portant le marqueur."""
    zones = []
    for m in re.finditer(r'(?ms)^  - "(.*?)"$', tete):
        if MARQUEUR in m.group(1):
            zones.append((m.start(), m.end()))
    return zones


survivances = {}
for F in sorted(glob.glob(os.path.join(RACINE, "corpus", "livre-*", "c*.md"))):
    t = io.open(F, encoding="utf-8").read()
    if "ERRATUM TERMINOLOGIQUE DU" in t or "NOTE TERMINOLOGIQUE DU" in t:
        continue
    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    if not m:
        continue
    ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
    tete, corps = t[:m.end()], t[m.end():]
    notes = zones_de_note(tete)
    compte, contextes = 0, []
    for zone, txt, decalage in (("en-tête", tete, 0), ("corps", corps, 0)):
        masq = masque_citations(txt)
        for s in TERME.finditer(txt):
            if masq[s.start()]:
                continue
            if zone == "en-tête" and any(a <= s.start() < b for a, b in notes):
                continue
            compte += 1
            contextes.append((zone, re.sub(r"\s+", " ",
                                           txt[max(0, s.start() - 90):s.start() + 60])))
    if compte:
        survivances[ch] = (compte, contextes)

out.write("CONTRÔLE FINAL DU RENOMMAGE — corps, titres et métadonnées, voix propre\n")
out.write("=" * 78 + "\n")
out.write("Exclus : citations, archives, errata, et analyses de l'ancien terme.\n\n")

total = sum(n for n, _ in survivances.values())
out.write("%d survivance(s) dans %d chapitre(s).\n\n" % (total, len(survivances)))

echecs = []
out.write("%-9s %5s  %s\n" % ("chapitre", "n", "motif"))
for ch in sorted(survivances, key=lambda c: -survivances[c][0]):
    n, ctx = survivances[ch]
    if ch in EXCEPTIONS and EXCEPTIONS[ch][0] == n:
        out.write("%-9s %5d  %s\n" % (ch, n, EXCEPTIONS[ch][1]))
    elif ch in EXCEPTIONS:
        out.write("%-9s %5d  **ÉCART** : %d attendue(s) — %s\n"
                  % (ch, n, EXCEPTIONS[ch][0], EXCEPTIONS[ch][1]))
        echecs.append(ch)
    else:
        out.write("%-9s %5d  **NON JUSTIFIÉE**\n" % (ch, n))
        echecs.append(ch)
    if LISTE:
        for zone, c in ctx:
            out.write("            [%s] …%s…\n" % (zone, c))

attendu = sum(n for n, _ in EXCEPTIONS.values())
out.write("\nAttendu : %d survivance(s) justifiée(s) dans %d chapitre(s).\n"
          % (attendu, len(EXCEPTIONS)))
manquants = [c for c in EXCEPTIONS if c not in survivances]
if manquants:
    out.write("Chapitres attendus et absents du relevé : %s\n" % ", ".join(sorted(manquants)))

if echecs:
    out.write("\nÉCHEC : %d chapitre(s) hors table — %s\n" % (len(echecs), ", ".join(echecs)))
else:
    out.write("\nCONTRÔLE PASSÉ : toute survivance est justifiée.\n")
out.flush()
sys.exit(1 if echecs else 0)
