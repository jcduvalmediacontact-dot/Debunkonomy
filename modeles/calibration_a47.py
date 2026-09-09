#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CALIBRATION D'A47 SUR DOSSIERS RÉELS — INSTRUMENT DE COMPARAISON.

CE QU'IL FAIT : il compare les remises de DEUX ÉQUIPES INDÉPENDANTES appliquant
la même grille aux mêmes dossiers, et il sépare quatre choses — accord de
régime, accord de procédure, DIVERGENCES SANS EFFET et DIVERGENCES DÉCISIVES.

LA DISTINCTION QUI COMPTE EST LA DERNIÈRE. Deux équipes peuvent évaluer une
gravité à 2 et à 3 sans que le régime bouge : cela dit que la grille est robuste
à cet endroit, non qu'elles se sont trompées. Une divergence est DÉCISIVE quand
elle fait basculer, à elle seule, le régime ou la charge de la preuve — et
l'instrument l'isole en rejouant la qualification une dimension à la fois.

CE QU'IL NE FAIT PAS, ET C'EST DÉLIBÉRÉ : il n'invente aucune donnée. Les trois
dossiers réels — eau potable, lithium et batteries, stockage géologique du CO2 —
ne sont PAS documentés. Tant qu'ils ne le sont pas, le programme le dit et
s'arrête.

CE QU'IL NE PROUVERA JAMAIS : que A47 soit juste. Deux équipes qui convergent
peuvent converger sur une erreur commune, d'autant plus qu'elles partagent une
formation. L'ACCORD MESURE LA TRANSFÉRABILITÉ, JAMAIS LA JUSTESSE.

Protocole : protocoles/calibration-a47.md

USAGE :  python modeles/calibration_a47.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nemo_a47 as a47

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False
SEUIL_D_ACCORD_FIXE = False   # délibérément : le fixer avant l'épreuve serait
                              # la faute que le point 9 de A47 interdit


# =====================================================================
# LES TROIS DOSSIERS RÉELS — NOMMÉS, NON DOCUMENTÉS
# =====================================================================
NON_DOCUMENTE = "À DOCUMENTER"

DOSSIERS_REELS = [
    {"cle": "eau-potable",
     "libelle": "Eau potable — seuils sanitaires",
     "role": "CAS FAVORABLE : seuils scientifiques et sanitaires relativement "
             "documentés. Si deux équipes divergent ici, A47 n'est pas "
             "transférable du tout.",
     "donnees": NON_DOCUMENTE},
    {"cle": "lithium",
     "libelle": "Lithium et batteries — usages concurrents",
     "role": "RESSOURCE RARE : la difficulté n'est pas l'incertitude mais la "
             "CONCURRENCE DES USAGES, et le classement dépend du portefeuille "
             "retenu.",
     "donnees": NON_DOCUMENTE},
    {"cle": "stockage-co2",
     "libelle": "Stockage géologique du CO2 — horizons longs",
     "role": "CAS DÉFAVORABLE : horizons longs, incertitudes importantes, "
             "dommages potentiellement irréversibles. C'est là que l'horizon "
             "sectoriel décide de la charge.",
     "donnees": NON_DOCUMENTE},
]

CHAMPS_EXIGES = ("donnees", "horizon", "gravite", "etendue", "plausibilite",
                 "confiance", "reductible", "delai_acquisition", "delai_utile",
                 "regime", "charge", "procedure", "motif")

DIMENSIONS_COMPAREES = ("gravite", "etendue", "plausibilite", "confiance",
                        "reductible", "delai_acquisition", "horizon")


def documente(remise):
    """Une remise n'est complète que si AUCUN champ ne porte encore la marque.
    Un champ absent n'est pas une valeur par défaut."""
    manquants = [c for c in CHAMPS_EXIGES
                 if remise.get(c) in (None, NON_DOCUMENTE, "")]
    return manquants


# =====================================================================
# LA COMPARAISON
# =====================================================================
def dossier_depuis(remise, cle, domaine="calibration"):
    """Reconstruit un Dossier A47 à partir d'une remise d'équipe."""
    horizon = remise["horizon"]
    return a47.Dossier(
        cle, remise.get("libelle", cle), domaine,
        remise["gravite"], remise["etendue"], remise["plausibilite"],
        {horizon: remise["reversible_a_l_horizon"]},
        remise["confiance"], remise["reductible"],
        remise["delai_acquisition"],
        urgence=remise.get("urgence", False),
        essentiel=remise.get("essentiel", False))


def grille_pour(remise):
    g = dict(a47.GRILLE)
    g["horizons"] = {"calibration": remise["horizon"]}
    g["delai_utile"] = remise["delai_utile"]
    return g


def qualifier_remise(remise, cle):
    d = dossier_depuis(remise, cle)
    g = grille_pour(remise)
    regime = a47.qualifier(d, g)[0]
    procedure = a47.instruire(d, g)[0]
    return regime, procedure, a47.REGIMES[regime][0]


def comparer(cle, a, b):
    """Rend le détail de la comparaison entre deux remises sur un dossier.

    LES DIVERGENCES DÉCISIVES SONT ISOLÉES EN REJOUANT LA QUALIFICATION UNE
    DIMENSION À LA FOIS : on part de la remise A, on y substitue la SEULE valeur
    de B pour une dimension, et l'on regarde si le régime ou la charge bouge.
    C'est ce qui distingue un désaccord qui compte d'un désaccord qui n'a aucun
    effet sur la décision.
    """
    ra, pa, ca = qualifier_remise(a, cle)
    rb, pb, cb = qualifier_remise(b, cle)

    ecarts, decisives, sans_effet, procedurales = [], [], [], []
    for dim in DIMENSIONS_COMPAREES:
        if a.get(dim) == b.get(dim):
            continue
        ecarts.append((dim, a.get(dim), b.get(dim)))
        melange = dict(a)
        melange[dim] = b[dim]
        if dim == "horizon":
            melange["reversible_a_l_horizon"] = b["reversible_a_l_horizon"]
        rm, pm, cm = qualifier_remise(melange, cle)
        if (rm, cm) != (ra, ca):
            decisives.append((dim, a.get(dim), b.get(dim), ra, rm))
        elif pm != pa:
            # NI SANS EFFET NI DECISIVE : elle ne touche pas la charge de la
            # preuve mais change LA MANIERE D'INSTRUIRE. Les confondre avec les
            # divergences inertes masquerait ce que A47 fait de l'incertitude.
            procedurales.append((dim, a.get(dim), b.get(dim), pa, pm))
        else:
            sans_effet.append((dim, a.get(dim), b.get(dim)))

    return {"regime_a": ra, "regime_b": rb, "accord_regime": ra == rb,
            "procedure_a": pa, "procedure_b": pb, "accord_procedure": pa == pb,
            "charge_a": ca, "charge_b": cb,
            "ecarts": ecarts, "decisives": decisives,
            "sans_effet": sans_effet, "procedurales": procedurales}


def rendre(cle, r):
    print("")
    print("  DOSSIER « %s »" % cle)
    print("    régime      A %-24s B %-24s %s"
          % (r["regime_a"], r["regime_b"],
             "ACCORD" if r["accord_regime"] else "DÉSACCORD"))
    print("    charge      A %-24s B %-24s" % (r["charge_a"], r["charge_b"]))
    print("    procédure   A %-24s B %-24s %s"
          % (r["procedure_a"], r["procedure_b"],
             "ACCORD" if r["accord_procedure"] else "DÉSACCORD"))
    if r["sans_effet"]:
        print("    DIVERGENCES SANS EFFET — la grille est robuste ici :")
        for dim, va, vb in r["sans_effet"]:
            print("      %-20s A=%s  B=%s" % (dim, va, vb))
    if r["procedurales"]:
        print("    DIVERGENCES DE PROCÉDURE — même charge, autre instruction :")
        for dim, va, vb, avant, apres in r["procedurales"]:
            print("      %-20s A=%s  B=%s   %s → %s"
                  % (dim, va, vb, avant, apres))
    if r["decisives"]:
        print("    DIVERGENCES DÉCISIVES — elles font basculer à elles seules :")
        for dim, va, vb, avant, apres in r["decisives"]:
            print("      %-20s A=%s  B=%s   %s → %s"
                  % (dim, va, vb, avant, apres))
    if not r["ecarts"]:
        print("    aucune divergence sur les dimensions comparées")


# =====================================================================
def etat_des_dossiers():
    print("=" * 78)
    print("CALIBRATION D'A47 SUR DOSSIERS RÉELS")
    print("=" * 78)
    print("Le corpus a établi que la règle ne laisse AUCUN VIDE LOGIQUE. Il")
    print("reste à établir qu'elle peut être APPLIQUÉE PAR DES TIERS à des")
    print("situations réelles. C'est ce que ce protocole éprouve.")
    print("")
    print("LES TROIS DOSSIERS")
    for d in DOSSIERS_REELS:
        print("")
        print("  %-14s %s" % (d["cle"], d["libelle"]))
        print("                 %s" % d["role"])
        print("                 données : %s" % d["donnees"])

    manquants = [d["cle"] for d in DOSSIERS_REELS
                 if d["donnees"] == NON_DOCUMENTE]
    print("")
    print("  %d dossiers sur %d ne sont PAS documentés." % (len(manquants),
                                                            len(DOSSIERS_REELS)))
    print("")
    print("  LE PROGRAMME N'INVENTE AUCUNE DONNÉE, et c'est la seule conduite")
    print("  possible : des valeurs fabriquées produiraient un accord ou un")
    print("  désaccord qui ne dirait rien d'A47, tout en en ayant l'apparence.")
    print("  Il faut des SOURCES OUVERTES — un résumé ne vaut pas ouverture —")
    print("  et DEUX ÉQUIPES CONSTITUÉES. Les deux relèvent de l'auteur.")
    return manquants


def verifier_l_instrument():
    """L'instrument est éprouvé sur des remises SYNTHÉTIQUES.

    ELLES NE DISENT RIEN D'A47. Elles servent uniquement à prouver que
    l'instrument discrimine — qu'il voit un accord quand il y en a un, qu'il
    distingue une divergence sans effet d'une divergence décisive. Sans cette
    vérification, on ne saurait pas si un futur « aucune divergence » signifie
    l'accord ou l'aveuglement.
    """
    print("")
    print("=" * 78)
    print("VÉRIFICATION DE L'INSTRUMENT — SUR DONNÉES SYNTHÉTIQUES")
    print("=" * 78)
    print("Ces trois cas sont FABRIQUÉS et ne disent RIEN d'A47. Ils prouvent")
    print("seulement que l'instrument voit ce qu'il doit voir.")

    base = {"libelle": "cas d'épreuve", "donnees": "synthétique",
            "horizon": "échelle humaine", "reversible_a_l_horizon": False,
            "gravite": 2, "etendue": 2, "plausibilite": 0.60,
            "confiance": 0.55, "reductible": True, "delai_acquisition": 3,
            "delai_utile": 4, "regime": "", "charge": "", "procedure": "",
            "motif": "fabriqué"}

    identique = dict(base)
    sans_effet = dict(base, etendue=1)            # ne change pas le régime
    decisive = dict(base, plausibilite=0.30)      # fait tomber sous le seuil
    procedure = dict(base, delai_acquisition=9)   # même régime, autre procédure

    resultats = {}
    for etiquette, autre in (("accord parfait", identique),
                             ("divergence sans effet", sans_effet),
                             ("divergence décisive", decisive),
                             ("même régime, autre procédure", procedure)):
        r = comparer(etiquette, base, autre)
        resultats[etiquette] = r
        rendre(etiquette, r)

    print("")
    print("  CE QUE LA VÉRIFICATION ÉTABLIT :")
    print("    l'accord parfait ne produit aucune divergence      %s"
          % ("oui" if not resultats["accord parfait"]["ecarts"] else "NON"))
    print("    une divergence sans effet est vue ET classée telle %s"
          % ("oui" if resultats["divergence sans effet"]["sans_effet"]
             and not resultats["divergence sans effet"]["decisives"] else "NON"))
    print("    une divergence décisive est isolée                 %s"
          % ("oui" if resultats["divergence décisive"]["decisives"] else "NON"))
    proc = resultats["même régime, autre procédure"]
    print("    un désaccord de PROCÉDURE à régime identique est vu %s"
          % ("oui" if (proc["accord_regime"] and not proc["accord_procedure"]
                       and proc["procedurales"]) else "NON"))
    print("    et il est classé à part des divergences inertes        %s"
          % ("oui" if proc["procedurales"] and not proc["sans_effet"]
             else "NON"))
    return resultats


def main():
    manquants = etat_des_dossiers()
    resultats = verifier_l_instrument()

    print("")
    print("=" * 78)
    print("CE QUE CE PROGRAMME ÉTABLIT AUJOURD'HUI")
    print("=" * 78)
    print("  L'INSTRUMENT EXISTE ET DISCRIMINE. Il sépare l'accord de régime,")
    print("  l'accord de procédure, les divergences sans effet et les")
    print("  divergences décisives — ces dernières isolées en rejouant la")
    print("  qualification UNE DIMENSION À LA FOIS.")
    print("")
    print("  L'ÉPREUVE N'EST PAS EXÉCUTÉE. %d dossiers sur %d ne sont pas"
          % (len(manquants), len(DOSSIERS_REELS)))
    print("  documentés, et aucune équipe n'est constituée.")
    print("")
    print("  AUCUN SEUIL D'ACCORD N'EST FIXÉ, et le fixer maintenant serait la")
    print("  faute que le point 9 d'A47 interdit à propos des seuils")
    print("  sectoriels : choisir le seuil après avoir vu les dossiers. CE QUI")
    print("  EST ARRÊTÉ D'AVANCE EST LA FORME DU VERDICT, écrite au protocole.")
    print("")
    print("  ET CE QUE L'ÉPREUVE NE POURRA PAS FAIRE, quoi qu'elle donne :")
    print("  VALIDER A47. Deux équipes qui convergent peuvent converger sur une")
    print("  erreur commune, d'autant plus qu'elles partagent une formation.")
    print("  L'ACCORD MESURE LA TRANSFÉRABILITÉ, JAMAIS LA JUSTESSE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
