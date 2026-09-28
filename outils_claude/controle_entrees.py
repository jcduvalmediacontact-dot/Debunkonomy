# -*- coding: utf-8 -*-
"""Contrôle d'une entrée de source contre elle-même.

CE QUE CE CONTRÔLE ÉTABLIT. Le 2026-09-28, trois entrées sur vingt de L1.C23 —
S6, S9, S14 — citaient en tête un passage entre guillemets, puis déclaraient
plus bas qu'il n'est pas dans la pièce, en ajoutant « le corps est aligné ». Le
corps avait été corrigé à chaque fois, l'entrée jamais. Aucun contrôle ne
compare une entrée à elle-même : `controle.py` vérifie l'état de lecture,
`controle_appels.py` les appels, `lire_piece.py` la pièce.

Il signale toute entrée qui porte À LA FOIS une citation entre guillemets et
une déclaration d'absence, et donne les deux, pour qu'un lecteur tranche.

CE QU'IL N'ÉTABLIT PAS. Qu'une entrée signalée se contredise : une entrée
saine peut citer ce que la pièce porte et dire ce qu'elle ne porte pas — c'est
même ce que la règle du 2026-09-20 demande (« ce que la pièce dit contre
l'usage qui en est fait »). Le signal dit OÙ LIRE, non ce que la lecture
trouvera. Il ne voit pas non plus une contradiction écrite sans les tournures
qu'il connaît.

DEUX CLASSES, pour que le bruit ne noie pas le défaut.

    corps_aligne       l'entrée cite, déclare une absence, ET dit que le corps
                       a été aligné. C'est la signature relevée le 28 : sur
                       l'état de L1.C23 antérieur à sa correction, cette
                       classe rend S6, S9 et S14, et elles seules. Elle ne
                       distingue pas une entrée corrigée d'une entrée qui ne
                       l'est pas : l'entrée corrigée garde la phrase.
    a_lire             citation et déclaration d'absence coexistent, sans
                       mention d'alignement. À lire ; souvent sain.

UNE PREMIÈRE VERSION CLASSAIT PAR « CITATION REPRISE AU MOT PRÈS DE LA
DÉCLARATION D'ABSENCE ». Éprouvée sur le même état de L1.C23, elle manquait
les trois entrées fautives et signalait S9 une fois corrigée : elle est
retirée. Un classement qui n'a pas été éprouvé sur le défaut qu'il vise ne
vaut rien.

AVERTISSEMENTS, JAMAIS BLOCAGES. Hors du chemin de publication ; `controle.py`
reste l'autorité. Code de sortie : 0 si aucune `corps_aligne`, 1 sinon.

    python outils_claude/controle_entrees.py
    python outils_claude/controle_entrees.py --livre 1
    python outils_claude/controle_entrees.py --livre 1 --chapitres 17-30
    python outils_claude/controle_entrees.py --livre 1 --tout   # les deux classes
"""
import argparse
import glob
import io
import os
import re
import sys

import yaml

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

CITATION = re.compile(r"«\s*([^«»]{12,}?)\s*»")

# Tournures relevées dans les entrées du Livre 1. La liste est ouverte : une
# tournure absente d'ici est un défaut que l'outil ne voit pas.
ABSENCE = re.compile(
    r"n'y figure pas|ne figure pas|n'y figurent pas|ne figurent pas"
    r"|ne contient pas|ne la contient pas|ne le contient pas|ne les contient pas"
    r"|n'est pas dans (?:la|cette|l[ae]) |ne sont pas dans (?:la|cette) "
    r"|absente? de (?:la|cette|l'|tout)|absents de "
    r"|ne porte pas|ne le porte pas|ne la porte pas|ne les portent? pas|ne portent pas"
    r"|n'emploie pas|n'emploient pas|ne mentionne pas|ne mentionnent pas"
    r"|ne nomme pas|introuvable|zéro occurrence|aucune occurrence"
    r"|est retirée? le|EST RETIRÉE? LE",
    re.I,
)

ALIGNEMENT = re.compile(r"\balign", re.I)


def examiner(reference):
    """Rend (classe, absences, citations) ou None."""
    texte = " ".join(str(reference).split())
    citations = [m.group(1) for m in CITATION.finditer(texte)]
    absences = [m.group(0) for m in ABSENCE.finditer(texte)]
    if not citations or not absences:
        return None
    classe = "corps_aligne" if ALIGNEMENT.search(texte) else "a_lire"
    return classe, absences, citations


def chapitres(livre, plage):
    motif = "livre-%02d-*" % livre if livre is not None else "livre-*"
    for f in sorted(glob.glob(os.path.join(CORPUS, motif, "c*.md"))):
        m = re.match(r"c(\d+)", os.path.basename(f))
        if not m:
            continue
        n = int(m.group(1))
        if plage and not (plage[0] <= n <= plage[1]):
            continue
        yield f


def lire_entete(chemin):
    t = io.open(chemin, encoding="utf-8").read()
    p = t.split("---", 2)
    if len(p) < 3:
        return None
    return yaml.safe_load(p[1])


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--livre", type=int)
    ap.add_argument("--chapitres", help="plage, par exemple 17-30")
    ap.add_argument("--tout", action="store_true", help="afficher aussi la classe a_lire")
    a = ap.parse_args(argv)
    plage = None
    if a.chapitres:
        d, f = a.chapitres.split("-")
        plage = (int(d), int(f))
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    n_aligne = n_lire = n_entrees = 0
    for chemin in chapitres(a.livre, plage):
        h = lire_entete(chemin)
        if not h:
            continue
        ident = h.get("chapitre") or os.path.basename(chemin)
        for s in h.get("sources_primaires") or []:
            n_entrees += 1
            r = examiner(s.get("reference", ""))
            if not r:
                continue
            classe, absences, citations = r
            if classe == "corps_aligne":
                n_aligne += 1
            else:
                n_lire += 1
                if not a.tout:
                    continue
            print("%-8s %-4s %-13s %-14s %d citation(s), absence : %s"
                  % (ident, s.get("ref"), classe, s.get("etat_lecture"),
                     len(citations), " / ".join(sorted(set(x.lower() for x in absences)))[:70]))
    print()
    print("%d entrée(s) examinée(s) ; %d corps_aligne ; %d a_lire%s"
          % (n_entrees, n_aligne, n_lire, "" if a.tout else " (non affichées : --tout)"))
    return 1 if n_aligne else 0


if __name__ == "__main__":
    sys.exit(main())
