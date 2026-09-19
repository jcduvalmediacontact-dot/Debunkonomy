# -*- coding: utf-8 -*-
"""Verifie un rapport d'audit tiers CONTRE LE CHAPITRE qu'il pretend citer.

Regle appliquee : un audit se verifie avant de s'appliquer. Une objection peut etre
bloquante ET fausse. Le verificateur n'arbitre rien : il dit seulement, pour chaque
passage que le rapport donne entre guillemets, s'il figure ou non dans le fichier.

Il extrait les citations tout seul (texte entre guillemets francais), de sorte que
rien ne depende de ce que le lecteur a bien voulu recopier.

DEUX GARDE-FOUS, sans lesquels un resultat ne vaut rien :
  - CONTROLE POSITIF : une phrase certainement presente doit etre retrouvee ;
  - CONTROLE NEGATIF : une phrase certainement absente ne doit pas l'etre.
Si l'un des deux echoue, le script s'arrete : le defaut est dans l'outil, pas dans
le rapport. Sans cela, un motif casse produit "tout est absent" et ment.

Quand une citation ne se retrouve pas, le script cherche separement des fragments
de la citation, pour distinguer une PARAPHRASE (le chapitre porte l'idee sous
d'autres mots) d'une INVENTION (rien d'approchant).

Usage :
    python outils_claude/verifier_audit.py --chapitre L1.C23
    python outils_claude/verifier_audit.py --chapitre L1.C23 --rapport <chemin> --min 40
"""
import argparse
import glob
import io
import os
import re
import sys
import unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Tout ce qu'une recopie deforme sans changer le texte : blancs, les deux apostrophes,
# les guillemets, les tirets de toute longueur, le tiret conditionnel, le gras Markdown.
IGNORES = r"[\s­'’‘“”\"«»‐-―*_`—–-]+"


def norm(s):
    """Normalise pour comparer un texte recopie a un texte source."""
    return re.sub(IGNORES, "", unicodedata.normalize("NFKC", s)).lower()


def corps_du_chapitre(chemin):
    """Rend le corps seul : l'en-tete YAML porte les verifications, pas le texte audite."""
    t = io.open(chemin, encoding="utf-8").read()
    i = t.index("\n---\n", t.index("resume:"))
    return t, t[i + 5:]


def citations_du_rapport(texte, minimum):
    """Extrait les passages entre guillemets francais, dedupliques, ordre conserve."""
    brutes = re.findall(r"«\s*(.+?)\s*»", texte, re.S)
    vues, gardees = set(), []
    for c in brutes:
        c = re.sub(r"\s+", " ", c).strip()
        if len(c) < minimum:          # trop court = mot isole, non opposable
            continue
        if norm(c) in vues:
            continue
        vues.add(norm(c))
        gardees.append(c)
    return gardees


def fragments(citation, taille=34):
    """Decoupe une citation en morceaux discriminants, sur la ponctuation d'abord.

    La virgule ne coupe PAS entre deux chiffres : en francais elle est un separateur
    decimal, et couper "0,8 mois" en "0" et "8 mois" fabrique un faux absent. Ce
    defaut a ete constate le 2026-09-18 sur le rapport de L1.C13.
    """
    morceaux = [m.strip() for m in re.split(r"[;:—–]|(?<!\d),(?!\d)|\.\s", citation)]
    return [m for m in morceaux if len(m) >= taille]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--chapitre", required=True, help="identifiant, par exemple L1.C23")
    p.add_argument("--rapport", help="par defaut protocoles/rapport-audit-<id>-tiers.md")
    p.add_argument("--min", type=int, default=30, help="longueur minimale d'une citation opposable")
    a = p.parse_args()

    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    m = re.match(r"^L(\d+)\.C(\d+)$", a.chapitre)
    if not m:
        sys.exit("identifiant attendu de la forme L1.C23")
    livre, chap = int(m.group(1)), m.group(2)

    motif = os.path.join(RACINE, "corpus", "livre-%02d-*" % livre, "c%s-*.md" % chap)
    trouves = glob.glob(motif)
    if len(trouves) != 1:
        sys.exit("chapitre introuvable ou ambigu : %s" % motif)
    fichier = trouves[0]
    rapport = a.rapport or os.path.join(
        RACINE, "protocoles", "rapport-audit-L%d-C%s-tiers.md" % (livre, chap))
    if not os.path.exists(rapport):
        sys.exit("rapport introuvable : %s" % rapport)

    entier, corps = corps_du_chapitre(fichier)
    nc = norm(corps)
    texte_rapport = io.open(rapport, encoding="utf-8").read()

    # --- garde-fous : l'outil prouve d'abord qu'il sait trouver ---------------
    temoin = [l for l in corps.split("\n") if len(l.strip()) > 80][0][:70]
    if norm(temoin) not in nc:
        sys.exit("CONTROLE POSITIF EN ECHEC : l'outil ne retrouve pas une phrase du fichier.")
    if norm("phrase temoin absente du corpus xyzzy plugh") in nc:
        sys.exit("CONTROLE NEGATIF EN ECHEC : l'outil retrouve n'importe quoi.")
    out.write("controle positif et negatif : franchis\n")

    cits = citations_du_rapport(texte_rapport, a.min)
    if not cits:
        sys.exit("AUCUNE citation reperee dans le rapport : verifier le motif "
                 "avant de conclure quoi que ce soit.")
    out.write("%s : %d citations opposables (>= %d caracteres)\n\n"
              % (a.chapitre, len(cits), a.min))

    exactes, partielles, absentes = [], [], []
    for c in cits:
        if norm(c) in nc:
            exactes.append(c)
            etat = "EXACTE"
        else:
            frs = fragments(c)
            retrouves = [f for f in frs if norm(f) in nc]
            if retrouves:
                partielles.append((c, retrouves, [f for f in frs if f not in retrouves]))
                etat = "PARTIELLE (%d/%d fragments)" % (len(retrouves), len(frs))
            else:
                absentes.append(c)
                etat = "ABSENTE"
        out.write("[%-24s] %s\n" % (etat, c[:96]))

    out.write("\n%-12s %d\n%-12s %d\n%-12s %d\n"
              % ("exactes :", len(exactes), "partielles :", len(partielles),
                 "absentes :", len(absentes)))

    if partielles:
        out.write("\nDETAIL DES CITATIONS PARTIELLES "
                  "(le chapitre porte une partie, le rapport a recrit le reste)\n")
        for c, oui, non in partielles:
            out.write("  citation : %s\n" % c[:150])
            for f in oui:
                out.write("     present  : %s\n" % f[:110])
            for f in non:
                out.write("     ABSENT   : %s\n" % f[:110])

    # --- titres de section : un rapport qui se trompe de plan n'a pas lu -------
    titres = re.findall(r"(?m)^## (.+)$", corps)
    out.write("\nTITRES REELS DU CHAPITRE (%d sections)\n" % len(titres))
    for t in titres:
        out.write("  %s\n" % t)

    # --- etats de lecture, pour les objections qui portent sur une source ------
    etats = re.findall(r"(?ms)^  - ref: (S\d+)\n.*?etat_lecture: (\w+)", entier)
    fermees = [r for r, e in etats if e != "ouverte"]
    out.write("\nsources : %d declarees, %d non ouvertes%s\n"
              % (len(etats), len(fermees), (" (%s)" % ", ".join(fermees)) if fermees else ""))
    out.write("\nRAPPEL : ce script ne dit PAS si une objection est fondee. Il dit si le\n"
              "passage cite figure dans le fichier. Une citation exacte peut porter une\n"
              "objection fausse ; une citation absente peut viser un defaut reel.\n")
    out.flush()


if __name__ == "__main__":
    main()
