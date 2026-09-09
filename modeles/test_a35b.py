#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DU PROGRAMME — et de lui seul.

CE QUE CE FICHIER PROUVE. Que `a35b_bilans.py` applique correctement les règles
qu'on lui a données.

CE QU'IL NE PROUVE PAS, ET IL FAUT LE LIRE AVANT LE RESTE. **Que ces règles
soient comptablement fondées.** Une première version passait tous ses tests et
deux de ses règles de rejet étaient fausses. **Un programme qui applique
fidèlement une hypothèse fausse produit des résultats faux avec une régularité
parfaite.**

D'où la séparation en sections :

  A. IDENTITÉS — ce ne sont pas des hypothèses. Un bilan s'équilibre, un encours
     a sa contrepartie, et le passif total égale la somme des avoirs de tous les
     détenteurs À CHAQUE ÉTAPE. Les sabotages vérifient qu'elles s'appliquent.

  B. CRÉANCIER DYNAMIQUE — un instrument transférable change de créancier avec
     son détenteur. Vérifié sur les branches où l'unité passe de main en main.

  C. QUALIFICATION — **PROPOSÉE, jamais établie.** Les tests vérifient que le
     programme suspend sa proposition quand un élément manque. Ils ne valident
     pas la lecture de la norme.

  D. LIQUIDITÉ — au pic, et par scénario séparé. Le stress à cent pour cent
     n'est jamais présenté comme l'état ordinaire.

  E. A36 — deux mécanismes distincts, et le collecteur ne décide que de la
     PREMIÈRE DESTINATION des unités : l'emploi ultérieur décide de l'encours.

USAGE :  python modeles/test_a35b.py
"""

import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import a35b_bilans as m

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ECHECS = []
VRAIE = m.sequence


def exiger(condition, libelle):
    print(("  ok   " if condition else "  RATÉ ") + libelle)
    if not condition:
        ECHECS.append(libelle)


def arith(branche, sabotage=None):
    if sabotage:
        m.sequence = sabotage
    try:
        return m.passer(branche)[2]
    finally:
        m.sequence = VRAIE


def par_cle(c):
    return [b for b in m.BRANCHES if b.cle == c][0]


B2 = par_cle("B2")
B10, B11, B12 = par_cle("B10"), par_cle("B11"), par_cle("B12")


# =====================================================================
print("A. IDENTITÉS — ce ne sont pas des hypothèses")
# =====================================================================
def s_desequilibre(b):
    E = VRAIE(b)
    E[0].postes = [p for p in E[0].postes if not (p[0] == "BCN" and p[2] == m.SN)]
    return E


exiger(arith(B2, s_desequilibre), "une écriture qui ne se ferme pas est vue")


def s_sans_motif(b):
    E = VRAIE(b)
    E[0].motifs = {}
    return E


exiger([a for a in arith(B2, s_sans_motif) if "motif" in a],
       "une variation de situation nette sans motif est vue")


def s_richesse(b):
    E = VRAIE(b)
    E[2].postes = [p for p in E[2].postes if not (p[0] == "ETAT" and p[2] == m.SN)]
    E[2].postes += [("ETAT", "dépôt à la banque centrale", m.ACTIF, +m.M)]
    return E


exiger([a for a in arith(B2, s_richesse) if "situations nettes" in a],
       "une richesse nette apparue de rien est vue")


def s_avoirs_orphelins(b):
    """Des avoirs chez un détenteur, sans passif en face chez l'émetteur."""
    E = VRAIE(b)
    E[0].postes += [("RDM", m.AVOIRS, m.ACTIF, +9),
                    ("RDM", "report à nouveau", m.SN, +9)]
    E[0].motifs["RDM"] = "sabotage"
    return E


exiger([a for a in arith(B2, s_avoirs_orphelins) if "identité créancier" in a],
       "des avoirs sans passif en face rompent l'identité, ET ELLE EST "
       "CONTRÔLÉE À CHAQUE ÉTAPE")
exiger(not arith(B2), "la branche intacte ne rompt aucune identité")


# =====================================================================
print("")
print("B. CRÉANCIER DYNAMIQUE — il migre avec l'instrument")
# =====================================================================
_, chrono10, _ = m.passer(B10)
fin10 = chrono10[-1][1]
det10 = m.detenteurs(fin10)
exiger(len(det10) == 2,
       "B10 : deux banques centrales détiennent l'unité à la fin (%s)"
       % ", ".join("%s %d" % x for x in det10))
exiger(m.passif_total(B10, fin10) == sum(v for _, v in det10),
       "et le passif de l'émetteur égale la SOMME de leurs encours, non celui "
       "d'un créancier désigné")

vus = set()
for _, inst in chrono10:
    vus.update(s for s, _ in m.detenteurs(inst))
exiger(vus == {"BCN", "BCN2"},
       "la qualité de créancier a bien migré au cours du circuit")

_, chrono11, _ = m.passer(B11)
det11 = m.detenteurs(chrono11[-1][1])
exiger(len(det11) == 2 and dict(det11)["BCN2"] > dict(det11)["BCN"],
       "B11 : après échange, le participant contributeur détient plus que son "
       "allocation, et le bénéficiaire moins")


# =====================================================================
print("")
print("C. QUALIFICATION — proposée, jamais établie")
# =====================================================================
obs11, res11 = m.qualification(B11, chrono11)
exiger(not res11,
       "B11 n'est PLUS écartée : son débiteur est déterminé — chaque membre "
       "pour sa propre allocation")
exiger(any("architecture concurrente" in o for o in obs11),
       "et elle est signalée comme architecture CONCURRENTE d'A35a, non comme "
       "un défaut")

_, chrono12, _ = m.passer(B12)
obs12, res12 = m.qualification(B12, chrono12)
exiger(any("possibilité future" in r for r in res12),
       "B12, sans obligation présente du détenteur, voit sa qualification "
       "SUSPENDUE : le droit ne porte sur rien")

_, chrono2, _ = m.passer(B2)
exiger(not m.qualification(B2, chrono2)[1],
       "B2, avec contribution modélisée et son fait générateur, n'appelle "
       "aucune réserve")

sans_obl = copy.copy(B2)
sans_obl.obligation = None
exiger(m.qualification(sans_obl, chrono2)[1],
       "l'absence d'obligation déclarée suspend la proposition")

print("")
print("  RAPPEL — CE QUI NE PEUT PAS ÊTRE TESTÉ ICI.")
print("  Que les quatre éléments retenus soient LA bonne lecture des § 4.101")
print("  et 4.103 est une hypothèse du corpus. Aucun test de programme ne peut")
print("  la valider, et le programme n'écrit jamais « reconnu comme passif ».")


# =====================================================================
print("")
print("D. LIQUIDITÉ — au pic, et par scénario séparé")
# =====================================================================
B9 = par_cle("B9")
_, chrono9, _ = m.passer(B9)
liq9 = m.liquidite(B9, chrono9)
exiger(liq9["pire"] is not None,
       "B9 est illiquide malgré une souscription égale à l'encours FINAL")
exiger(max(ex for _, ex, _ in liq9["lignes"]) == m.M,
       "le pic d'exigible vaut l'émission entière (%d)" % m.M)
dernier = liq9["lignes"][-1]
exiger(dernier[1] <= dernier[2],
       "et le bilan FINAL seul aurait conclu à la couverture — c'est la faute "
       "de la version 1")

liq11 = m.liquidite(B11, chrono11)
exiger(liq11["type"] == "participants" and len(liq11["scenarios"]) == 3,
       "B11 publie TROIS scénarios séparés, et non une mesure unique")
normal, plafond, stress = liq11["scenarios"]
exiger(normal[1] <= normal[3],
       "en fonctionnement normal, la demande courante est servie (%d contre %d)"
       % (normal[1], normal[3]))
exiger(stress[1] > normal[1],
       "la ruée demande davantage (%d) que le fonctionnement normal (%d), et "
       "elle est étiquetée comme un STRESS" % (stress[1], normal[1]))
exiger(plafond[2] is not None,
       "le plafond statutaire est publié à part, avec sa règle")
exiger(m.PLAFOND_DESIGNATION_SOURCE is False,
       "et le facteur du plafond est déclaré NON SOURCÉ, faute d'avoir pu "
       "ouvrir les documents du Fonds")

exiger(m.liquidite(B2, chrono2)["type"] == "sans_objet",
       "une obligation d'acceptation n'appelle aucun décaissement")


# =====================================================================
print("")
print("E. A36 — deux mécanismes, et l'emploi décide de l'encours")
# =====================================================================
exiger(m.PRELEVEMENT != m.DEMURRAGE and m.ASSIETTE_DEMURRAGE != m.D,
       "deux assiettes et deux montants distincts : transaction %d/%d, "
       "encaisse %d/%d" % (m.PRELEVEMENT, m.D, m.DEMURRAGE,
                           m.ASSIETTE_DEMURRAGE))

encours = {}
for c in ("B2", "B3a", "B3b", "B3c"):
    b = par_cle(c)
    bil, _, _ = m.passer(b)
    encours[c] = m.passif_total(b, bil)

exiger(encours["B3a"] == encours["B3b"],
       "conserver ou remettre en circulation laisse le MÊME encours (%d) : "
       "l'unité reste en circulation dans les deux cas" % encours["B3a"])
exiger(encours["B3c"] == encours["B2"],
       "transférer à l'émetteur ramène l'encours à celui du cas où l'émetteur "
       "percevait lui-même (%d)" % encours["B2"])
exiger(encours["B3a"] != encours["B3c"],
       "L'EMPLOI DÉCIDE, ET LE COLLECTEUR NE DÉCIDE QUE DE LA PREMIÈRE "
       "DESTINATION : %d si l'État conserve, %d s'il reverse"
       % (encours["B3a"], encours["B3c"]))


# =====================================================================
print("")
if ECHECS:
    print("SABOTAGE NON DÉTECTÉ — le programme n'applique pas ses règles :")
    for e in ECHECS:
        print("  " + e)
    sys.exit(1)
print("Le programme applique ses règles. CELA NE VALIDE AUCUNE DE SES")
print("HYPOTHÈSES COMPTABLES. La qualification est une PROPOSITION, et elle")
print("attend un comptable national ou un spécialiste des bilans de banque")
print("centrale : voir protocoles/revue-comptable-a35b.md.")
sys.exit(0)
