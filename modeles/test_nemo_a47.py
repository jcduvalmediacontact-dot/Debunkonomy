#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DE LA DOCTRINE A47.

CE QU'IL PROUVE : que la doctrine est appliquée telle qu'elle est écrite, et
que les deux trous relevés sont dans la sortie, non dans le commentaire.

CE QU'IL NE PROUVE PAS : que la doctrine soit bonne. Deux de ses résultats
sont défavorables, et le test les vérifie COMME DÉFAUTS — il passe au vert
parce que le défaut est bien là.

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


# =====================================================================
print("A. POINT 2 — L'INCERTITUDE NE TRANCHE PAS SEULE")
# =====================================================================
regimes = dict((d.cle, m.regime(d)) for d in m.DOSSIERS)
exiger(len(set(regimes.values())) > 2,
       "la doctrine produit %d régimes distincts sur %d dossiers : elle ne "
       "répond ni « oui » ni « non » uniformément"
       % (len(set(regimes.values())), len(m.DOSSIERS)))
exiger(all(m.REGIMES[r][0] is not None
           for r in ("grave_irreversible", "limite_reversible")),
       "et chacun des deux pôles attribue une charge de la preuve nommée")


# =====================================================================
print("")
print("B. TROU 1 — LA QUALIFICATION DÉCIDE DE L'ISSUE")
# =====================================================================
d = par_cle("stockage-geo")
lectures = {}
for reversible in (True, False):
    copie = m.Dossier(d.cle, d.libelle, d.gravite, d.etendue, reversible,
                      d.plausibilite)
    lectures[reversible] = m.REGIMES[m.regime(copie)][0]
exiger(lectures[True] != lectures[False],
       "deux lectures également défendables de la RÉVERSIBILITÉ font basculer "
       "la charge de « %s » à « %s »" % (lectures[True], lectures[False]))
exiger(lectures[True] == "autorité" and lectures[False] == "porteur",
       "et le basculement va bien du refus motivé exigé de l'autorité à la "
       "preuve exigée du porteur : c'est l'issue du dossier qui change")


# =====================================================================
print("")
print("C. TROU 2 — LA ZONE INTERMÉDIAIRE N'ATTRIBUE AUCUNE CHARGE")
# =====================================================================
intermediaires = [c for c, r in regimes.items() if r == "intermediaire"]
exiger(len(intermediaires) > 0,
       "%d dossiers sur %d ne relèvent NI du point 3 NI du point 4 : %s"
       % (len(intermediaires), len(m.DOSSIERS), ", ".join(intermediaires)))
exiger(m.REGIMES["intermediaire"][0] is None,
       "et la doctrine n'y attribue la charge à personne — le programme "
       "n'invente pas la règle manquante")

pest = par_cle("pesticide")
mine = par_cle("mine-lithium")
exiger(pest.gravite >= m.GRAVITE_SERIEUSE and pest.reversible,
       "le premier cas est ordinaire : grave MAIS réversible")
exiger(not mine.reversible and mine.plausibilite < m.SEUIL_PLAUSIBILITE,
       "le second aussi : irréversible MAIS peu plausible")


# =====================================================================
print("")
print("D. LA CONTRADICTION ENTRE LES POINTS 3 ET 5")
# =====================================================================
med = par_cle("medicament")
exiger(m.point_3_applique(med) and med.urgence and med.essentiel,
       "sur le dossier urgent, les points 3 ET 5 s'appliquent ensemble")
exiger(m.regime(med) == "urgence_essentielle",
       "le programme applique le point 5 — CHOIX D'IMPLÉMENTATION, non "
       "lecture du texte, et la sortie le signale comme tel")
source = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "nemo_a47.py"), encoding="utf-8").read()
exiger("CHOIX D'IMPLÉMENTATION" in source,
       "et il ne le fait pas silencieusement")


# =====================================================================
print("")
print("E. POINT 9 — LE SEUIL FIXÉ D'AVANCE MORD")
# =====================================================================
plaus = sorted(x.plausibilite for x in m.DOSSIERS)
avant = len([x for x in m.DOSSIERS
             if m.regime(x, m.SEUIL_PLAUSIBILITE) == "grave_irreversible"])
tout_admettre = len([x for x in m.DOSSIERS
                     if m.regime(x, max(plaus) + 0.01)
                     == "grave_irreversible"])
tout_refuser = len([x for x in m.DOSSIERS
                    if m.regime(x, min(plaus) - 0.01)
                    == "grave_irreversible"])
exiger(tout_admettre < avant < tout_refuser,
       "un seuil choisi après coup produit l'issue voulue : %d, %d ou %d "
       "dossiers à la charge du porteur selon le moment de la fixation"
       % (tout_admettre, avant, tout_refuser))
exiger(min(plaus) - 0.01 < m.SEUIL_PLAUSIBILITE < max(plaus) + 0.01,
       "et les trois seuils sont dans la même plage de valeurs plausibles : "
       "RIEN DANS LE DOSSIER NE DISTINGUE UN SEUIL DE PRINCIPE D'UN SEUIL "
       "TAILLÉ SUR MESURE")


# =====================================================================
print("")
print("F. POINT 7 — LA PUBLICITÉ EST CONTRÔLÉE, NON DÉCLARÉE")
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


# =====================================================================
print("")
print("G. CE QUE LA DOCTRINE NE FIXE PAS, ET NE DOIT PAS FIXER")
# =====================================================================
exiger(m.SEUILS_CALIBRES is False,
       "aucun seuil n'est déclaré calibré")
exiger("NON CALIBRÉ" in source,
       "et le seuil de plausibilité porte la mention dans le code même")
exiger("ne la valide jamais" in source and "aucun dossier n'est réel" in source,
       "et le programme redit ce qu'il ne prouve pas : dossiers fictifs, "
       "seuils non éprouvés, et appliquer une règle ne la valide jamais")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas la doctrine telle qu'écrite :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("La doctrine est appliquée telle qu'elle est écrite. ELLE TIENT SUR")
print("CINQ DE SES NEUF POINTS et laisse DEUX TROUS que la sortie montre : la")
print("qualification du risque, qui décide de l'issue sans que la doctrine")
print("dise qui l'opère ; et la zone intermédiaire, où la charge de la preuve")
print("n'est attribuée à personne. CE TEST PASSE PARCE QUE LES DÉFAUTS SONT")
print("BIEN LÀ — il ne valide rien.")
sys.exit(0)
