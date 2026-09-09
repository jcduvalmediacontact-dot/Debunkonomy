#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DU MODÈLE DE COMPENSATION — et de lui seul.

CE QU'IL PROUVE : que `nemo_soldes.py` applique ses règles, que ses identités
tiennent, et que ses trois manquements sont SENSIBLES AUX PARAMÈTRES plutôt que
structurels — ce qui est une information utile, puisqu'elle dit ce qu'il
faudrait changer.

CE QU'IL NE PROUVE PAS : que le mécanisme soit viable, ni que les repères
retenus soient raisonnables. Aucun n'est calibré.

USAGE :  python modeles/test_nemo_soldes.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nemo_soldes as m

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ECHECS = []


def exiger(condition, libelle):
    print(("  ok   " if condition else "  RATÉ ") + libelle)
    if not condition:
        ECHECS.append(libelle)


def par_cle(c):
    return [s for s in m.SCENARIOS if s.cle == c][0]


def codes(anomalies, prefixe):
    return [a for a in anomalies if a.startswith(prefixe)]


# =====================================================================
print("A. IDENTITÉS — ce ne sont pas des hypothèses")
# =====================================================================
for sc in m.SCENARIOS:
    for lien in (True, False):
        _, _, anomalies = m.jouer(sc, lien)
        exiger(not codes(anomalies, "[C1]"),
               "%s (%s) : la somme des soldes reste nulle à chaque période"
               % (sc.cle, "contraignante" if lien else "délibérative"))
        exiger(not codes(anomalies, "[C2]"),
               "%s (%s) : la liquidité reste dans ses bornes"
               % (sc.cle, "contraignante" if lien else "délibérative"))


_, journal0, _ = m.jouer(par_cle("S0"), True)
somme = sum(journal0[-1]["solde"][c] for c in m.COMPTES)
exiger(abs(somme) < 1e-6,
       "et la clôture finale vaut zéro (%.6f) : une compensation qui ne se "
       "boucle pas n'en est pas une" % somme)


# =====================================================================
print("")
print("B. LA PROTECTION DES IMPORTATIONS ESSENTIELLES")
# =====================================================================
_, _, a_s1 = m.jouer(par_cle("S1"), True)
exiger(codes(a_s1, "[C3]"),
       "S1 : la règle est ENFREINTE — le choc dure plus longtemps que la "
       "facilité")

# LE MOTIF EST LE REMBOURSEMENT, ET ON LE PROUVE EN ALLONGEANT LA DURÉE.
duree = m.DUREE_LIQUIDITE
try:
    m.DUREE_LIQUIDITE = m.PERIODES + 1
    _, _, a_long = m.jouer(par_cle("S1"), True)
    exiger(not codes(a_long, "[C3]"),
           "et elle cesse de l'être si la facilité couvre tout l'horizon : "
           "LA CAUSE EST LE REMBOURSEMENT À ÉCHÉANCE, non le plafond")
finally:
    m.DUREE_LIQUIDITE = duree

plafond = dict(m.PLAFOND_LIQUIDITE)
try:
    m.PLAFOND_LIQUIDITE = dict((c, 0) for c in m.CODES)
    _, _, a_sans = m.jouer(par_cle("S1"), True)
    exiger(len(codes(a_sans, "[C3]")) > len(codes(a_s1, "[C3]")),
           "sans facilité du tout, la règle est enfreinte davantage (%d contre "
           "%d) : la facilité sert, elle ne suffit pas"
           % (len(codes(a_sans, "[C3]")), len(codes(a_s1, "[C3]"))))
finally:
    m.PLAFOND_LIQUIDITE = plafond


# =====================================================================
print("")
print("C. L'ACCUMULATION INDÉFINIE")
# =====================================================================
for sc in m.SCENARIOS:
    _, _, a = m.jouer(sc, True)
    exiger(codes(a, "[C4]"),
           "%s : le corridor NE BORNE PAS — il tarife le dépassement sans "
           "l'empêcher" % sc.cle)

# ET C'EST UNE QUESTION DE BARÈME, NON DE STRUCTURE.
t1, t2 = m.TAUX_CHARGE_1, m.TAUX_CHARGE_2
try:
    m.TAUX_CHARGE_1, m.TAUX_CHARGE_2 = 0.60, 1.20
    e_fort, _, _ = m.jouer(par_cle("S0"), True)
    e_faible = None
finally:
    m.TAUX_CHARGE_1, m.TAUX_CHARGE_2 = t1, t2
e_faible, _, _ = m.jouer(par_cle("S0"), True)


def dernier_increment(e):
    serie = e.soldes_par_periode["EXC"]
    return serie[-1] - serie[-2]


exiger(dernier_increment(e_fort) < 0.5 * dernier_increment(e_faible),
       "une charge forte FREINE l'accumulation : dernier incrément %.1f contre "
       "%.1f au barème déclaré"
       % (dernier_increment(e_fort), dernier_increment(e_faible)))
exiger(dernier_increment(e_fort) > 0,
       "MAIS ELLE NE LA BORNE PAS DANS L'HORIZON : l'excédent croît encore de "
       "%.1f à la dernière période. Un taux fait converger vers corridor plus "
       "flux divisé par taux ; il ne pose aucun plafond."
       % dernier_increment(e_fort))

# CE QUE CELA ÉTABLIT, ET C'EST PLUS FIN QUE « C'EST UN PROBLÈME DE BARÈME ».
# Un taux appliqué au dépassement fait converger le solde vers
#     corridor + flux / taux
# — donc il BORNE asymptotiquement, mais il ne POSE AUCUN PLAFOND, et la
# convergence peut être plus lente que le choc. Empêcher l'accumulation
# demande un plafond DUR, ou une charge croissant plus vite que le solde.


# =====================================================================
print("")
print("D. F6 — LA SYMÉTRIE EST UN PARAMÈTRE, ET L'ÉCART SE MESURE")
# =====================================================================
for sc in m.SCENARIOS:
    ec, _, _ = m.jouer(sc, True)
    ed, _, _ = m.jouer(sc, False)
    part_c = m.effort(ec)["EXC"]["total"]
    part_d = m.effort(ed)["EXC"]["total"]
    exiger(part_d == 0.0,
           "%s : sous obligation DÉLIBÉRATIVE, l'excédentaire ne porte RIEN "
           "(%.1f) — c'est la configuration historiquement adoptée"
           % (sc.cle, part_d))
    exiger(part_c > part_d,
           "%s : sous obligation contraignante il porte %.1f, et l'écart est "
           "ce que F6 met en jeu" % (sc.cle, part_c))

ec, _, _ = m.jouer(par_cle("S1"), True)
eff = m.effort(ec)
total = sum(eff[c]["total"] for c in m.CODES)
part = 100.0 * eff["EXC"]["total"] / total
exiger(part < 20.0,
       "et même contraignante, la symétrie reste NOMINALE : l'excédentaire "
       "porte %.1f %% de l'effort en S1" % part)
exiger(eff["EXC"]["expansion"] > eff["DEF"]["contraction"] * 0.5,
       "alors que son expansion monétaire (%.0f) est du même ordre que la "
       "contraction du déficitaire (%.0f) — miroir non compté"
       % (eff["EXC"]["expansion"], eff["DEF"]["contraction"]))


# =====================================================================
print("")
print("E. AUCUN SEUIL N'EST DÉCLARÉ CALIBRÉ")
# =====================================================================
exiger(m.SEUILS_CALIBRES is False,
       "le drapeau de calibrage est à False, et il doit y rester tant qu'une "
       "source ne fonde pas chaque seuil")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas ses règles :")
    for e in ECHECS:
        print("  " + e)
    sys.exit(1)
print("Le modèle applique ses règles, et ses trois manquements sont de")
print("CALIBRAGE ou de DURÉE, non de structure. CELA NE VALIDE NI LE MÉCANISME")
print("NI SES PARAMÈTRES : aucun n'est calibré, et la symétrie reste la")
print("disposition dont le corpus a établi qu'elle est celle qui saute [F6].")
sys.exit(0)
