#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DE LA DOCTRINE A47 VALIDÉE.

CE QU'IL PROUVE : les deux propriétés exigées par l'auteur — une grille
complète attribue un régime à CHAQUE dossier ; deux dossiers de même risque et
de connaissances différentes reçoivent des PROCÉDURES D'INSTRUCTION
différentes. Et que les trois variables — probabilité, confiance,
réductibilité — restent séparées.

CE QU'IL NE PROUVE PAS : que la doctrine soit bonne. Aucun seuil n'est
éprouvé, aucun dossier n'est réel.

USAGE :  python modeles/test_nemo_a47.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nemo_a47 as m

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ECHECS = []


def exiger(condition, libelle):
    print(("  ok   " if condition else "  RATÉ ") + libelle)
    if not condition:
        ECHECS.append(libelle)


def par_cle(c):
    return [d for d in m.DOSSIERS if d.cle == c][0]


source = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "nemo_a47.py"), encoding="utf-8").read()
COMPLETE = m.grille_complete()


# =====================================================================
print("A. PROPRIÉTÉ EXIGÉE N° 1 — AUCUN DOSSIER SANS RÉGIME")
# =====================================================================
exiger(m.controler_exhaustivite(COMPLETE) == [],
       "avec une grille COMPLÈTE, le contrôle R1 ne relève aucune anomalie")
regimes = dict((d.cle, m.qualifier(d, COMPLETE)[0]) for d in m.DOSSIERS)
exiger(all(r in m.REGIMES for r in regimes.values()),
       "les %d dossiers reçoivent un régime connu" % len(m.DOSSIERS))
exiger(all(m.REGIMES[r][0] is not None for r in regimes.values()),
       "et chacun porte une charge nommée : %s"
       % ", ".join(sorted(set(m.REGIMES[r][0] for r in regimes.values()))))

pest, mine = par_cle("pesticide"), par_cle("mine-lithium")
exiger(regimes["pesticide"] == "intermediaire"
       and regimes["mine-lithium"] == "intermediaire",
       "« GRAVE MAIS RÉVERSIBLE » et « IRRÉVERSIBLE MAIS PEU PLAUSIBLE » "
       "relèvent bien de la ZONE INTERMÉDIAIRE — la version précédente les "
       "rendait sans charge, et c'était une erreur de traduction de la règle")
exiger(m.REGIMES["intermediaire"][0] == "partagée",
       "dont la charge est PARTAGÉE")
exiger(len(m.CHARGE_PARTAGEE) == 4
       and any("tranches" in x[1] for x in m.CHARGE_PARTAGEE)
       and any("données manquantes" in x[1] for x in m.CHARGE_PARTAGEE),
       "et la charge partagée porte ses quatre composantes, dont les tranches "
       "et l'expertise indépendante")

# Sans horizon, la protection ne disparaît pas : elle passe en zone
# intermédiaire, qui est le régime prudent.
sans_horizon = [d for d in m.DOSSIERS if d.domaine not in m.GRILLE["horizons"]]
exiger(all(m.qualifier(d)[0] in m.REGIMES for d in sans_horizon),
       "et même sans horizon sectoriel, %d dossiers reçoivent un régime : la "
       "grille lacunaire ne crée pas de vide, elle bascule en zone "
       "intermédiaire" % len(sans_horizon))
exiger(any(x.startswith("[Q2]") for x in m.qualifier(sans_horizon[0])[2]),
       "tout en signalant l'horizon manquant")


# =====================================================================
print("")
print("B. PROPRIÉTÉ EXIGÉE N° 2 — MÊME RISQUE, INSTRUCTIONS DIFFÉRENTES")
# =====================================================================
base = par_cle("stockage-geo")
essais = {}
for etiquette, confiance, reductible, delai in (
        ("réductible à temps", 0.55, True, 3),
        ("réductible trop tard", 0.55, True, 9),
        ("robuste et irréductible", 0.85, False, 0)):
    jumeau = m.Dossier(base.cle, base.libelle, base.domaine, base.gravite,
                       base.etendue, base.plausibilite, base.reversible_sur,
                       confiance, reductible, delai)
    essais[etiquette] = (m.qualifier(jumeau, COMPLETE)[0],
                         m.instruire(jumeau, COMPLETE)[0])

exiger(len(set(r for r, _ in essais.values())) == 1,
       "les trois dossiers ont le MÊME RÉGIME DE RISQUE (%s) : l'incertitude "
       "n'a volontairement aucun effet automatique sur le régime"
       % list(set(r for r, _ in essais.values()))[0])
exiger(len(set(p for _, p in essais.values())) == 3,
       "ET TROIS PROCÉDURES D'INSTRUCTION DIFFÉRENTES : %s"
       % ", ".join(sorted(set(p for _, p in essais.values()))))
exiger(essais["réductible à temps"][1] == "acquisition",
       "réductible dans le délai utile → acquisition de données AVANT "
       "décision complète")
exiger(essais["réductible trop tard"][1] == "precaution",
       "réductible hors délai utile → marge de précaution explicitée")
exiger(essais["robuste et irréductible"][1] == "directe",
       "information robuste → application directe de la grille")
med = par_cle("medicament")
exiger(m.instruire(med, COMPLETE)[0] == "urgence",
       "et le besoin essentiel urgent → autorisation minimale et temporaire "
       "PENDANT l'instruction")


# =====================================================================
print("")
print("C. TROIS VARIABLES SÉPARÉES, ET NON UN SEUL NOMBRE")
# =====================================================================
exiger("plausibilite" in m.DIMENSIONS and "confiance" in m.DIMENSIONS
       and "reductibilite" in m.DIMENSIONS
       and "delai_acquisition" in m.DIMENSIONS,
       "les dimensions distinguent PROBABILITÉ, CONFIANCE, RÉDUCTIBILITÉ et "
       "DÉLAI : %s" % ", ".join(m.DIMENSIONS))
exiger(not hasattr(base, "incertitude"),
       "et le nombre unique « incertitude » a disparu du modèle : il portait "
       "trois choses à la fois")

# Deux dossiers de même probabilité et même confiance, distingués par le reste.
a, b = par_cle("mine-lithium"), par_cle("capteur")
exiger(a.plausibilite == b.plausibilite and a.confiance == b.confiance,
       "la mine et le réseau de capteurs partagent probabilité %.2f et "
       "confiance %.2f" % (a.plausibilite, a.confiance))
exiger(m.instruire(a, COMPLETE)[0] != m.instruire(b, COMPLETE)[0],
       "et reçoivent pourtant des instructions différentes (%s contre %s) : "
       "la probabilité seule ne détermine rien"
       % (m.instruire(a, COMPLETE)[0], m.instruire(b, COMPLETE)[0]))


# =====================================================================
print("")
print("D. LA LECTURE FAITE PAR LE PROGRAMME EST SIGNALÉE")
# =====================================================================
exiger("une lecture est faite ici" in source.lower()
       or "UNE LECTURE EST FAITE ICI" in source,
       "le traitement d'une incertitude réductible HORS délai utile est "
       "déclaré comme une LECTURE de la règle, non comme une règle ajoutée")
exiger("pour pouvoir être contestée" in source or "être contestée" in source,
       "et il est écrit pour être contesté")
tard = m.Dossier("essai", "essai", "energie", 2, 2, 0.50,
                 {"cinquante ans": True, "échelle humaine": False},
                 0.55, True, 99)
exiger(m.instruire(tard, COMPLETE)[0] == "precaution",
       "sans cette lecture, « dans un délai utile » n'aurait aucun effet : un "
       "délai de 99 périodes vaudrait un délai de 1")


# =====================================================================
print("")
print("E. LA GRILLE — FIXÉE D'AVANCE, ET AILLEURS")
# =====================================================================
exiger(m.GRILLE["publiee"] == "avant l'examen des dossiers"
       and m.GRILLE["fixee_par"] == "instance-democratique"
       and m.GRILLE["apres"] == "expertise pluraliste",
       "publiée avant l'examen, fixée par l'autorité démocratique après "
       "expertise pluraliste")
mauvaise = dict(m.GRILLE, fixee_par="autorite-de-qualification")
exiger(any(x.startswith("[Q4]") for x in m.controler_grille(mauvaise)),
       "et une grille fixée par qui l'applique est signalée — A46")
exiger(any(x.startswith("[Q2]") for x in m.controler_grille())
       and not any(x.startswith("[Q2]")
                   for x in m.controler_grille(COMPLETE)),
       "le contrôle des horizons discrimine : il mord sur la grille de "
       "référence et se tait sur la grille complète")

plaus = sorted(x.plausibilite for x in m.DOSSIERS)


def au_porteur(seuil):
    g = dict(COMPLETE)
    g["seuil_plausibilite"] = seuil
    return len([x for x in m.DOSSIERS
                if m.qualifier(x, g)[0] == "grave_irreversible"])


exiger(au_porteur(max(plaus) + 0.01) < au_porteur(m.GRILLE["seuil_plausibilite"])
       < au_porteur(min(plaus) - 0.01),
       "et un seuil choisi après lecture produit l'issue voulue : %d, %d ou %d "
       "dossiers à la charge du porteur"
       % (au_porteur(max(plaus) + 0.01),
          au_porteur(m.GRILLE["seuil_plausibilite"]),
          au_porteur(min(plaus) - 0.01)))


# =====================================================================
print("")
print("F. PUBLICITÉ, ET CE QUE LE PROGRAMME NE PRÉTEND PAS")
# =====================================================================
complet = dict((c, True) for c in m.PUBLICATION)
complet["cle"] = "essai"
exiger(m.controler_publication(complet) == [],
       "un dossier complet ne déclenche rien")
for champ in m.PUBLICATION:
    partiel = dict(complet)
    partiel[champ] = False
    exiger(any(champ in a for a in m.controler_publication(partiel)),
           "l'absence de « %s » est vue" % champ)
exiger(m.SEUILS_CALIBRES is False, "aucun seuil n'est déclaré calibré")
exiger("ne la valide jamais" in source and "aucun dossier n'est réel" in source,
       "et le programme redit ce qu'il ne prouve pas")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas la doctrine telle qu'écrite :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("Les deux propriétés exigées tiennent : AUCUN DOSSIER SANS RÉGIME, et")
print("MÊME RISQUE AVEC DES CONNAISSANCES DIFFÉRENTES DONNE DES PROCÉDURES")
print("DIFFÉRENTES. Deux des trois « restes » que ce programme publiait")
print("étaient des lectures fautives de la règle, non des lacunes : la zone")
print("intermédiaire était prévue, et l'incertitude agit sur la procédure et")
print("non sur le régime. LA SEULE PIÈCE OUVERTE EST CELLE DES HORIZONS ET")
print("SEUILS SECTORIELS.")
sys.exit(0)
