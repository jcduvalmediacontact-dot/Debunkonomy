# -*- coding: utf-8 -*-
"""Contrôle des compteurs du registre recopiés à la main dans les corps.

CE QUE CE CONTRÔLE ÉTABLIT. Un chapitre qui écrit « dix-huit arbitrages
arbitrés » fige un nombre que le registre fait bouger sans prévenir. Le contrôle
relève ces nombres et les compare à ceux du registre vivant.

IL NE RECALCULE RIEN. Les chiffres de référence sont lus dans la sortie de
`corpus/controle.py`, qui reste l'autorité : réimplémenter son décompte
reviendrait à créer une seconde vérité, exactement le défaut qu'on cherche.

Il ne touche à rien. Code de sortie : 0 si aucun écart, 1 sinon, 2 si le
contrôle de référence n'a pas pu être lu.

    python outils_claude/controle_compteurs.py
    python outils_claude/controle_compteurs.py --livre 1
"""
import argparse
import io
import os
import re
import subprocess
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

UNITS = {"zéro": 0, "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4,
         "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10,
         "onze": 11, "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15,
         "seize": 16, "vingt": 20, "trente": 30, "quarante": 40,
         "cinquante": 50, "soixante": 60, "cent": 100}
# « dix-sept », « quarante-huit », « vingt et un »
COMPOSE = re.compile(r"\b(dix|vingt|trente|quarante|cinquante|soixante)"
                     r"(?:[- ]et[- ]|[- ])(un|une|deux|trois|quatre|cinq|six|"
                     r"sept|huit|neuf)\b", re.I)
# CONSTRUCTION DE DÉNOMBREMENT, et rien d'autre.
# Relevé le 2026-09-20 : une première version cherchait un nombre AU VOISINAGE
# du vocabulaire du registre. Elle a rendu six candidats sur le Livre 1, et les
# six étaient faux — « dix-huit pays classés IDA », « dix à quinze fois »,
# « IPSAS 47 § 19 », « 15 % des importations ». « arbitrage » est un mot
# français ordinaire : sa présence dans une phrase ne signifie rien.
# Il faut que le nombre COMPTE des entrées, c'est-à-dire qu'il soit accolé au
# nom compté. Deux formes seulement :
#     « dix-huit arbitrages arbitrés »   (nombre, nom, qualification)
#     « arbitrages ouverts : quarante-sept »
# « un » et « une » sont ÉCARTÉS : ce sont des articles avant d'être des
# nombres, et « un arbitrage ouvert » n'est pas un dénombrement. Constaté sur
# L1.C27 et L1.C30, seuls restants après le premier resserrement.
COMPOSES = (r"(?:dix|vingt|trente|quarante|cinquante|soixante)"
            r"(?:[- ]et[- ]|[- ])(?:une?|deux|trois|quatre|cinq|six|sept|huit|neuf)")
NOMBRE = (COMPOSES + r"|\d{1,3}|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|"
          r"onze|douze|treize|quatorze|quinze|seize|vingt|trente|quarante|"
          r"cinquante|soixante|cent")
QUALIF = r"arbitr[ée]e?s?|ouvert(?:e|s|es)?|orient[ée]e?s?"
DENOMBREMENT = [
    # « dix-huit sont arbitrées », « quarante-sept sont ouvertes ou orientées »
    # — la forme que L1.C29 § 6 emploie, et que la première version manquait
    # parce qu'elle attendait le nom compté juste après le nombre.
    re.compile(r"\b(%s)\s+(?:sont|est|restent|demeurent)\s+(?:%s)" % (NOMBRE, QUALIF), re.I),
    re.compile(r"\b(%s)\s+(?:arbitrages?|entrées?)\s+(?:%s)" % (NOMBRE, QUALIF), re.I),
    re.compile(r"(?:arbitrages?|entrées?)\s+(?:%s)\s*[:—-]?\s*(%s)\b" % (QUALIF, NOMBRE), re.I),
    re.compile(r"\b(%s)\s+(?:%s)\s+(?:au\s+)?registre" % (NOMBRE, QUALIF), re.I),
]
# Le gras du corpus s'interpose entre le nombre et son verbe : on le retire
# avant de chercher, sinon « **dix-huit sont arbitrées** » échappe au motif.
MARKDOWN = re.compile(r"\*{1,3}|`")


def nombres_en_lettres(txt):
    """Rend [(valeur, position, forme)] pour les nombres écrits en toutes lettres."""
    vus = []
    for m in COMPOSE.finditer(txt):
        d, u = m.group(1).lower(), m.group(2).lower()
        vus.append((UNITS[d] + UNITS[u], m.start(), m.group(0)))
    pris = {p for _, p, f in vus for p in range(p, p + len(f))}
    for mot, val in UNITS.items():
        for m in re.finditer(r"\b%s\b" % mot, txt, re.I):
            if m.start() not in pris:
                vus.append((val, m.start(), m.group(0)))
    return vus


def reference():
    """Les compteurs vivants, LUS DANS LA SORTIE DE controle.py."""
    r = subprocess.run([sys.executable, os.path.join(CORPUS, "controle.py")],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=RACINE)
    sortie = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+)\s+arbitré\(s\).{0,120}?(\d+)\s+ouvert\(s\)", sortie, re.S)
    if not m:
        return None, sortie
    return {"arbitres": int(m.group(1)), "ouverts": int(m.group(2))}, sortie


def corps(chemin):
    lignes = io.open(chemin, encoding="utf-8").read().split("\n")
    b = [i for i, l in enumerate(lignes) if l.strip() == "---"]
    return "\n".join(lignes[b[1] + 1:]) if len(b) > 1 else "\n".join(lignes)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--livre", type=int)
    a = p.parse_args()
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)

    ref, brut = reference()
    if ref is None:
        out.write("Le décompte n'a pas pu être lu dans la sortie de controle.py.\n"
                  "Le contrôle s'arrête : il ne recalcule jamais de son côté.\n")
        out.flush()
        return 2
    out.write("Référence, lue dans controle.py : %d arbitré(s), %d ouvert(s) ou "
              "orienté(s).\n\n" % (ref["arbitres"], ref["ouverts"]))

    motif = os.path.join(CORPUS, "livre-%s*" % ("%02d" % a.livre if a.livre else ""),
                         "c*.md")
    ecarts, examines, candidats = [], 0, 0
    for f in sorted(glob.glob(motif)):
        txt = MARKDOWN.sub("", corps(f))
        cid = re.search(r"c(\d+)-", os.path.basename(f))
        examines += 1
        for phrase in re.split(r"(?<=[.!?])\s+", txt):
            for motif in DENOMBREMENT:
                for m in motif.finditer(phrase):
                    forme = m.group(1)
                    val = (int(forme) if forme.isdigit()
                           else dict((f.lower(), v) for v, _, f
                                     in nombres_en_lettres(forme)).get(forme.lower()))
                    if val is None:
                        vus = nombres_en_lettres(forme)
                        val = vus[0][0] if vus else None
                    if val is None:
                        continue
                    candidats += 1
                    attendus = (("arbitré(s)", ref["arbitres"]),
                                ("ouvert(s) ou orienté(s)", ref["ouverts"]))
                    proche = [(n, a) for n, a in attendus if a != val]
                    if all(a != val for _, a in attendus):
                        n, a = min(proche, key=lambda x: abs(x[1] - val))
                        ecarts.append((os.path.basename(f), forme, val, n, a,
                                       re.sub(r"\s+", " ", phrase)[:190]))
    out.write("%d chapitre(s) balayé(s), %d nombre(s) au voisinage du vocabulaire "
              "du registre.\n\n" % (examines, candidats))

    if ecarts:
        out.write("ÉCARTS — un nombre proche d'un compteur vivant, mais différent :\n")
        for fic, forme, val, nom, att, ctx in ecarts:
            out.write("\n  %s\n      « %s » = %d, quand le registre rend %d %s\n"
                      "      … %s …\n" % (fic, forme, val, att, nom, ctx))
        out.write("\n%d écart(s). Un compteur ne se recopie pas : il se calcule.\n"
                  % len(ecarts))
    else:
        out.write("CONTRÔLE PASSÉ : aucun nombre du voisinage ne diverge d'un\n"
                  "compteur vivant. Le contrôle ne voit QUE les nombres proches\n"
                  "des compteurs ; un chiffre recopié qui se trouve encore juste\n"
                  "passe, et restera invisible jusqu'à ce qu'il dérive.\n")
    out.flush()
    return 1 if ecarts else 0


if __name__ == "__main__":
    sys.exit(main())
