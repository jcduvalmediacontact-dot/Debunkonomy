#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DE LA DOCTRINE A47, VERSION 2.

CE QU'IL PROUVE : que la doctrine validée par l'auteur est appliquée telle
qu'elle est écrite ; que la grille est bien fixée d'avance par une autorité
DISTINCTE de celle qui l'applique ; et que les trois restes publiés sont dans
la sortie, chacun avec sa nature — un paramètre du programme d'un côté, deux
propriétés de la doctrine de l'autre.

CE QU'IL NE PROUVE PAS : que la doctrine soit bonne. Ce test passe au vert
parce que les défauts sont bien là où le programme les annonce.

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


# =====================================================================
print("A. POINT 1 — CINQ DIMENSIONS, ÉVALUÉES SÉPARÉMENT")
# =====================================================================
exiger(len(m.DIMENSIONS) == 5 and "incertitude" in m.DIMENSIONS
       and "plausibilite" in m.DIMENSIONS,
       "les cinq dimensions sont nommées, et l'INCERTITUDE est distincte de "
       "la PLAUSIBILITÉ : %s" % ", ".join(m.DIMENSIONS))
d = par_cle("stockage-geo")
exiger(isinstance(d.reversible_sur, dict) and len(d.reversible_sur) > 1,
       "LA RÉVERSIBILITÉ N'EST PAS UN BOOLÉEN : elle est déclarée par horizon "
       "(%s)" % ", ".join(sorted(d.reversible_sur)))


# =====================================================================
print("")
print("B. POINTS 2 ET 3 — LA GRILLE EST FIXÉE D'AVANCE, ET AILLEURS")
# =====================================================================
exiger(m.GRILLE["publiee"] == "avant l'examen des dossiers",
       "la grille est publiée AVANT l'examen des dossiers")
exiger(m.GRILLE["fixee_par"] == "instance-democratique",
       "elle est fixée par l'autorité démocratique")
exiger(m.GRILLE["apres"] == "expertise pluraliste",
       "après expertise pluraliste — la compétence technique informe, elle ne "
       "décide pas")
exiger(m.GRILLE["fixee_par"] != "autorite-de-qualification",
       "ET CELUI QUI FIXE LA GRILLE N'EST PAS CELUI QUI L'APPLIQUE : c'est "
       "A46, et c'est ce qui ferme le premier trou de la version 1")
mauvaise = dict(m.GRILLE, fixee_par="autorite-de-qualification")
exiger(any(x.startswith("[Q4]") for x in m.controler_grille(mauvaise)),
       "et le contrôle Q4 le vérifie : une grille fixée par qui l'applique "
       "est signalée")

for d in m.DOSSIERS:
    regime, motif, _ = m.qualifier(d)
    if regime == "non_determine":
        continue
    exiger(bool(motif) and len(motif) > 20,
           "%s : la qualification est MOTIVÉE — « %s »"
           % (d.cle, motif[:58] + ("…" if len(motif) > 58 else "")))


# =====================================================================
print("")
print("C. CE QUE LA VERSION 2 FERME — L'HORIZON EST DANS LA GRILLE")
# =====================================================================
d = par_cle("stockage-geo")
issues = {}
for horizon in m.HORIZONS:
    g = dict(m.GRILLE)
    g["horizons"] = dict(m.GRILLE["horizons"])
    g["horizons"][d.domaine] = horizon
    issues[horizon] = m.REGIMES[m.qualifier(d, g)[0]][0]
exiger(len(set(issues.values())) > 1,
       "l'horizon décide encore de la charge (%s)"
       % " / ".join("%s → %s" % (h, c) for h, c in sorted(issues.items())))
exiger(d.domaine in m.GRILLE["horizons"],
       "MAIS CE CHOIX EST DÉSORMAIS DANS LA GRILLE, publiée d'avance et fixée "
       "par une autre autorité : il devient une décision attaquable au lieu "
       "d'un arbitrage de dossier")


# =====================================================================
print("")
print("D. RESTE 1 — UN PARAMÈTRE DU PROGRAMME, ET IL EST DIT COMME TEL")
# =====================================================================
ref = len([x for x in m.DOSSIERS if m.qualifier(x)[0] != "non_determine"])
complet = len([x for x in m.DOSSIERS
               if m.qualifier(x, m.grille_complete())[0] != "non_determine"])
exiger(complet > ref,
       "une grille complète détermine %d dossiers contre %d : la "
       "détermination vaut la complétude de la grille" % (complet, ref))
exiger("UN PARAMÈTRE DE CE PROGRAMME" in source,
       "ET LE PROGRAMME DIT QUE L'INCOMPLÉTUDE EST SON PROPRE CHOIX, non un "
       "défaut de la doctrine")
exiger(any(x.startswith("[Q2]") for x in m.controler_grille()),
       "le contrôle Q2 signale les domaines sans horizon")
exiger(m.controler_grille(m.grille_complete()) and not any(
       x.startswith("[Q2]") for x in m.controler_grille(m.grille_complete())),
       "et il se tait quand la grille est complète : le contrôle discrimine")


# =====================================================================
print("")
print("E. RESTE 2 — L'INCERTITUDE EST ÉVALUÉE ET N'EMPORTE RIEN")
# =====================================================================
exiger(m.GRILLE["usage_des_incertitudes"] is None,
       "la grille ne dit pas ce que l'incertitude emporte")
exiger(any(x.startswith("[Q3]") for x in m.controler_grille()),
       "et le contrôle Q3 le signale au lieu de le passer sous silence")
regimes = {}
for incertitude in (0.10, 0.90):
    jumeau = m.Dossier(d.cle, d.libelle, d.domaine, d.gravite, d.etendue,
                       d.plausibilite, d.reversible_sur, incertitude)
    regimes[incertitude] = m.qualifier(jumeau)[0]
exiger(regimes[0.10] == regimes[0.90],
       "deux dossiers identiques hormis leur ÉTAT DE CONNAISSANCE (0.10 et "
       "0.90) reçoivent le même régime : évaluer une dimension sans dire ce "
       "qu'elle emporte ne change aucune décision")
exiger("le programme ne la remet pas de lui-même" in source,
       "et le programme ne rétablit pas de lui-même la règle de la version 1 "
       "— légiférer à la place de l'auteur serait la faute symétrique")


# =====================================================================
print("")
print("F. RESTE 3 — UNE PROPRIÉTÉ DE LA DOCTRINE, GRILLE COMPLÈTE COMPRISE")
# =====================================================================
hors = [x.cle for x in m.DOSSIERS
        if m.qualifier(x, m.grille_complete())[0] == "non_determine"]
exiger(len(hors) > 0,
       "MÊME AVEC UNE GRILLE COMPLÈTE, %d dossiers sur %d restent sans charge "
       "attribuée : %s" % (len(hors), len(m.DOSSIERS), ", ".join(hors)))
pest, mine = par_cle("pesticide"), par_cle("mine-lithium")
exiger(pest.gravite >= m.GRILLE["gravite_serieuse"]
       and pest.reversible_sur["échelle humaine"],
       "le premier est ordinaire : GRAVE MAIS RÉVERSIBLE")
exiger(not mine.reversible_sur["échelle humaine"]
       and mine.plausibilite < m.GRILLE["seuil_plausibilite"],
       "le second aussi : IRRÉVERSIBLE MAIS PEU PLAUSIBLE")
exiger(m.REGIMES["non_determine"][0] is None,
       "et le programme n'invente aucune charge là où la doctrine se tait")


# =====================================================================
print("")
print("G. CE QUI TIENT — SEUILS D'AVANCE, PUBLICITÉ, RECOURS")
# =====================================================================
plaus = sorted(x.plausibilite for x in m.DOSSIERS)


def au_porteur(seuil):
    g = dict(m.grille_complete())
    g["seuil_plausibilite"] = seuil
    return len([x for x in m.DOSSIERS
                if m.qualifier(x, g)[0] == "grave_irreversible"])


avant = au_porteur(m.GRILLE["seuil_plausibilite"])
admettre = au_porteur(max(plaus) + 0.01)
refuser = au_porteur(min(plaus) - 0.01)
exiger(admettre < avant < refuser,
       "un seuil choisi après lecture produit l'issue voulue : %d, %d ou %d "
       "dossiers à la charge du porteur" % (admettre, avant, refuser))
exiger(min(plaus) - 0.01 < m.GRILLE["seuil_plausibilite"] < max(plaus) + 0.01,
       "et les trois sont dans la même plage plausible : RIEN NE DISTINGUE UN "
       "SEUIL DE PRINCIPE D'UN SEUIL TAILLÉ SUR MESURE")

complet_pub = dict((c, True) for c in m.PUBLICATION)
complet_pub["cle"] = "essai"
exiger(m.controler_publication(complet_pub) == [],
       "un dossier complet ne déclenche rien")
for champ in m.PUBLICATION:
    partiel = dict(complet_pub)
    partiel[champ] = False
    exiger(any(champ in a for a in m.controler_publication(partiel)),
           "l'absence de « %s » est vue" % champ)
exiger("canal de mesure indépendant" in source.lower()
       or "CANAL DE MESURE" in source,
       "et le recours parle de CANAL DE MESURE INDÉPENDANT, non d'observation "
       "directe de la vérité")


# =====================================================================
print("")
print("H. CE QUE LE PROGRAMME NE PRÉTEND PAS")
# =====================================================================
exiger(m.SEUILS_CALIBRES is False, "aucun seuil n'est déclaré calibré")
exiger("ne la valide jamais" in source and "aucun dossier n'est réel" in source,
       "et le programme redit ce qu'il ne prouve pas")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas la doctrine telle qu'écrite :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("La doctrine validée est appliquée telle qu'elle est écrite. LA VERSION")
print("2 FERME LE PREMIER TROU — la grille est fixée d'avance par une autorité")
print("distincte de celle qui l'applique, et la qualification se motive. TROIS")
print("RESTES SUBSISTENT, de deux natures : les horizons sectoriels sont une")
print("PIÈCE À CONSTRUIRE que l'auteur a nommée ; l'incertitude sans effet et")
print("la zone entre les pôles sont des PROPRIÉTÉS DE LA DOCTRINE, à trancher.")
sys.exit(0)
