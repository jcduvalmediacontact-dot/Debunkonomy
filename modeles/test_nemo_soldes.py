#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DU MODÈLE DE COMPENSATION, version 2.

CE QU'IL PROUVE : que les identités tiennent, que les cinq corrections de
l'auteur sont effectivement en place, et que les conclusions publiées sont
celles que la sortie montre — non celles qu'on voudrait qu'elle montre.

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


def taux_essentiel(e, pays="PAU"):
    v = e.essentiel_voulu[pays]
    return 100.0 * e.essentiel_recu[pays] / v if v else 100.0


# =====================================================================
print("A. IDENTITÉS — correction (2) de l'auteur")
# =====================================================================
for sc in m.SCENARIOS:
    e, journal, anomalies = m.jouer(sc)
    exiger(not codes(anomalies, "[C1]"),
           "%s : la somme des soldes, institution comprise, reste nulle" % sc.cle)
    exiger(not codes(anomalies, "[C5]"),
           "%s : la variation de masse égale EXACTEMENT le flux NEMO converti "
           "à la parité — l'identité stock-flux tient période par période"
           % sc.cle)

e, _, _ = m.jouer(par_cle("S2"))
contraction, expansion, ecart = m.reconciliation(e)
exiger(abs(ecart) > 1e-6,
       "et les masses NATIONALES ne se bouclent pas (écart %+.0f) : c'est un "
       "EFFET DE PARITÉ, et il prouve qu'elles ne sont pas sommables entre "
       "pays" % ecart)


# =====================================================================
print("")
print("B. HORIZON — correction (1)")
# =====================================================================
exiger(m.PERIODES > 3 * m.DUREE_FACILITE,
       "l'horizon (%d) dépasse largement la maturité (%d)"
       % (m.PERIODES, m.DUREE_FACILITE))
for sc in m.SCENARIOS:
    _, _, anomalies = m.jouer(sc)
    exiger(not codes(anomalies, "[C7]"),
           "%s : aucun tirage ne subsiste à la fin — rien n'est reporté hors "
           "horizon" % sc.cle)


# =====================================================================
print("")
print("C. LES ÉCHANGES RÉPONDENT — correction (4), la plus dure")
# =====================================================================
# Avec des flux exogènes, conclure qu'une charge n'arrête pas l'accumulation
# était tautologique. On le vérifie en annulant l'élasticité.
elast = m.ELASTICITE
try:
    m.ELASTICITE = 0.0
    e_rigide, _, _ = m.jouer(par_cle("S0"))
finally:
    m.ELASTICITE = elast
e_souple, _, _ = m.jouer(par_cle("S0"))

pic = max(e_souple.soldes_par_periode["EXC"])
fin_souple = e_souple.soldes_par_periode["EXC"][-1]
fin_rigide = e_rigide.soldes_par_periode["EXC"][-1]

exiger(fin_souple < pic,
       "avec des échanges élastiques, le solde de l'excédentaire CULMINE à "
       "%.0f puis REDESCEND à %.0f" % (pic, fin_souple))
exiger(fin_rigide > fin_souple,
       "avec des flux rigides il finit plus haut (%.0f contre %.0f) : LA "
       "CONCLUSION DE LA VERSION 1 ÉTAIT EN PARTIE TAUTOLOGIQUE"
       % (fin_rigide, fin_souple))
exiger(m.ESSENTIEL.get(("EXC", "PAU")) is True,
       "et les postes essentiels restent inélastiques : c'est ce qui les "
       "définit")


# =====================================================================
print("")
print("D. LES DEUX GUICHETS — la décision posée par l'auteur")
# =====================================================================
sc = par_cle("S2")          # choc STRUCTUREL
e_fac, _, _ = m.jouer(sc, allocation_active=False)
e_deux, _, _ = m.jouer(sc, allocation_active=True)

exiger(taux_essentiel(e_deux) > taux_essentiel(e_fac),
       "sur un choc STRUCTUREL, l'allocation non remboursable sert %.0f %% des "
       "besoins essentiels contre %.0f %% pour la facilité seule"
       % (taux_essentiel(e_deux), taux_essentiel(e_fac)))
exiger(e_deux.contraction["PAU"] < e_fac.contraction["PAU"],
       "et la contraction du pays pauvre tombe de %.0f à %.0f"
       % (e_fac.contraction["PAU"], e_deux.contraction["PAU"]))
exiger(e_fac.fac["PAU"] > 0 and e_deux.fac["PAU"] == 0,
       "la facilité seule laisse une dette de %.0f à la fin ; les deux "
       "guichets n'en laissent aucune" % e_fac.fac["PAU"])

# ET SUR UN CHOC TEMPORAIRE, LA FACILITÉ SUFFIT — sans quoi l'allocation
# serait une réponse à tout, donc à rien.
e_t, _, _ = m.jouer(par_cle("S1"), allocation_active=False)
exiger(taux_essentiel(e_t) > 95.0,
       "sur un choc TEMPORAIRE, la facilité seule suffit (%.0f %%) : "
       "l'allocation n'est pas une réponse à tout" % taux_essentiel(e_t))


# =====================================================================
print("")
print("E. UN PLAFOND EST UNE PROCÉDURE — correction (5)")
# =====================================================================
garde = m.PLAFOND_SOLDE
try:
    m.PLAFOND_SOLDE = 0.30
    res = {}
    for proc in m.PROCEDURES:
        e, journal, anomalies = m.jouer(sc, procedure=proc)
        res[proc] = (e, len(codes(anomalies, "[C6]")))
finally:
    m.PLAFOND_SOLDE = garde

exiger(res["blocage"][1] == m.PERIODES,
       "le « blocage » est dépassé à CHAQUE période (%d sur %d) : un plafond "
       "sans procédure est un nombre, pas un mécanisme"
       % (res["blocage"][1], m.PERIODES))
exiger(res["recyclage"][1] < res["blocage"][1],
       "le recyclage réduit les dépassements (%d contre %d)"
       % (res["recyclage"][1], res["blocage"][1]))
exiger(res["conversion"][0].soldes_par_periode["EXC"][-1]
       < res["blocage"][0].soldes_par_periode["EXC"][-1],
       "et la conversion ramène le solde (%.0f contre %.0f)"
       % (res["conversion"][0].soldes_par_periode["EXC"][-1],
          res["blocage"][0].soldes_par_periode["EXC"][-1]))

# LE RISQUE SIGNALÉ PAR L'AUTEUR — un plafond qui bloque l'essentiel — ne se
# matérialise que si le guichet d'allocation est retiré.
try:
    m.PLAFOND_SOLDE = 0.10
    _, j_avec, _ = m.jouer(sc, procedure="blocage", allocation_active=True)
    _, j_sans, _ = m.jouer(sc, procedure="blocage", allocation_active=False)
finally:
    m.PLAFOND_SOLDE = garde
avec = sum(j["bloque"][c] for j in j_avec for c in m.CODES)
sans = sum(j["bloque"][c] for j in j_sans for c in m.CODES)
exiger(sans >= avec,
       "à plafond serré, retirer l'allocation ne réduit jamais le blocage des "
       "importations essentielles (%.0f sans, %.0f avec)" % (sans, avec))


# =====================================================================
print("")
print("F. CE QUI N'EST PAS PUBLIÉ, ET NE DOIT PAS L'ÊTRE — correction (3)")
# =====================================================================
e, _, _ = m.jouer(sc)
exiger(not hasattr(e, "effort"),
       "aucun registre « effort » n'existe : une variation de masse monétaire "
       "n'est pas une perte réelle")
for registre in ("contraction", "expansion", "production", "essentiel_recu",
                 "transfert_reel"):
    exiger(hasattr(e, registre),
           "le registre « %s » est publié séparément" % registre)
exiger(m.SEUILS_CALIBRES is False,
       "et aucun seuil n'est déclaré calibré")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas ses règles :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("Les cinq corrections sont en place et les conclusions publiées sont")
print("celles que la sortie montre. CELA NE VALIDE NI LE MÉCANISME NI SES")
print("PARAMÈTRES, et l'inflation n'est toujours pas modélisée : les prix ne")
print("sont pas endogènes.")
sys.exit(0)
