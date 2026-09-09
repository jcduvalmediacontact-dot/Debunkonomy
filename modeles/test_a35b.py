#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DU PROGRAMME — et de lui seul.

CE QUE CE FICHIER PROUVE, ET IL FAUT LE DIRE AVANT TOUT LE RESTE.

Il prouve que `a35b_bilans.py` applique correctement les règles qu'on lui a
données. **Il ne prouve PAS que ces règles sont comptablement fondées.** C'est
une distinction que la version 1 avait perdue : ses tests passaient tous, et
deux de ses règles de rejet étaient fausses. Un programme qui applique
fidèlement une hypothèse erronée produit des résultats erronés avec une
régularité parfaite.

CE QUE LES TESTS COUVRENT.

  A. Les IDENTITÉS COMPTABLES — équilibre par secteur, motifs des variations de
     situation nette, miroirs des encours croisés, somme des situations nettes.
     Celles-ci ne sont pas des hypothèses : ce sont des identités, et les
     sabotages vérifient qu'elles sont bien appliquées.

  B. La RECONNAISSANCE — obligation, débiteur, créancier, créance
     correspondante. **C'est une HYPOTHÈSE DE LECTURE** du § 4.101 et du
     § 4.103 du SNA 2025, et les tests ne la valident pas : ils vérifient que
     le programme la met en œuvre comme elle est écrite.

  C. La LIQUIDITÉ — contrôlée au PIC. Le test vérifie que le programme regarde
     bien CHAQUE étape, et non le bilan final : c'est précisément la faute que
     la version 1 commettait, et elle lui faisait manquer une tension de
     quarante.

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


def code(anomalies, n):
    return [a for a in anomalies if a.startswith("[%d]" % n)]


def par_cle(c):
    return [b for b in m.BRANCHES if b.cle == c][0]


B2, B7, B9, B11 = par_cle("B2"), par_cle("B7"), par_cle("B9"), par_cle("B11")


# =====================================================================
print("A. IDENTITÉS COMPTABLES — ce ne sont pas des hypothèses")
# =====================================================================
def s_desequilibre(b):
    E = VRAIE(b)
    E[0].postes = [p for p in E[0].postes
                   if not (p[0] == "BCN" and p[2] == m.SN)]
    return E


a = arith(B2, s_desequilibre)
exiger(code(a, 1), "une écriture qui ne se ferme pas est vue")
exiger(code(a, 2), "et le bilan final correspondant l'est aussi")


def s_sans_motif(b):
    E = VRAIE(b)
    E[0].motifs = {}
    return E


exiger(code(arith(B2, s_sans_motif), 3),
       "une variation de situation nette sans motif est vue")


def s_richesse(b):
    E = VRAIE(b)
    E[2].postes = [p for p in E[2].postes
                   if not (p[0] == "ETAT" and p[2] == m.SN)]
    E[2].postes += [("ETAT", "dépôt à la banque centrale", m.ACTIF, +m.M)]
    return E


exiger(code(arith(B2, s_richesse), 6),
       "une richesse nette apparue de rien est vue")


def s_miroir(b):
    E = VRAIE(b)
    E[2].postes += [("BQ", "réserves à la banque centrale", m.ACTIF, +7),
                    ("BQ", "dépôts des bénéficiaires", m.PASSIF, +7)]
    return E


exiger(code(arith(B2, s_miroir), 5),
       "un encours dont le miroir manque est vu")
exiger(not arith(B2), "et la branche intacte ne déclenche aucune identité")


# =====================================================================
print("")
print("B. RECONNAISSANCE — hypothèse de lecture, non validée par ces tests")
# =====================================================================
_, chrono_B2, _ = m.passer(B2)
exiger(not m.reconnaissance(B2, chrono_B2),
       "une branche dotée des quatre éléments est reconnue")

sans_obligation = copy.copy(B2)
sans_obligation.obligation = None
exiger(m.reconnaissance(sans_obligation, chrono_B2),
       "l'absence d'obligation est vue")

sans_creancier = copy.copy(B2)
sans_creancier.creancier = None
exiger(m.reconnaissance(sans_creancier, chrono_B2),
       "l'absence de créancier est vue")

creance_absente = copy.copy(B2)
creance_absente.creance = ("BCN", "créance qui n'existe pas", m.ACTIF)
exiger(m.reconnaissance(creance_absente, chrono_B2),
       "une créance que le créancier ne détient à aucune étape est vue")

_, chrono_B11, _ = m.passer(B11)
manques = m.reconnaissance(B11, chrono_B11)
exiger(manques and "collectif" in " ".join(manques),
       "un débiteur collectif est signalé comme non conforme au § 4.101")

print("")
print("  RAPPEL — CE QUI N'EST PAS TESTÉ ICI, ET NE PEUT PAS L'ÊTRE.")
print("  Que ces quatre éléments soient LA bonne lecture de la norme est une")
print("  hypothèse du corpus. Aucun test de programme ne peut la valider :")
print("  seuls un comptable national ou un contradicteur humain le peuvent.")


# =====================================================================
print("")
print("C. LIQUIDITÉ — contrôlée au PIC, jamais sur le bilan final")
# =====================================================================
_, chrono_B9, _ = m.passer(B9)
liq = m.liquidite(B9, chrono_B9)
exiger(liq["objet"] and liq["pire"] is not None,
       "B9 est ILLIQUIDE malgré une souscription égale à l'encours FINAL")

pics = [ex for _, ex, _ in liq["lignes"]]
exiger(max(pics) == m.M,
       "le pic d'exigible vaut l'émission entière (%d), non l'encours final "
       "(%d)" % (m.M, m.M - m.PRELEVEMENT - m.DEMURRAGE))

dernier_ex, dernier_co = liq["lignes"][-1][1], liq["lignes"][-1][2]
exiger(dernier_ex == dernier_co,
       "et le bilan FINAL seul aurait conclu à la couverture (%d contre %d) — "
       "c'est la faute de la version 1" % (dernier_ex, dernier_co))

couvert = copy.copy(B9)
couvert.souscription = m.M
_, chrono_c, _ = m.passer(couvert)
exiger(m.liquidite(couvert, chrono_c)["pire"] is None,
       "une souscription égale à l'ÉMISSION, et non à l'encours final, la rend "
       "servable à chaque étape")

liq11 = m.liquidite(B11, chrono_B11)
exiger(liq11["objet"] and liq11["pire"] is not None,
       "B11 : la liquidité d'un avoir de type DTS dépend des AUTRES "
       "participants, et elle est bornée par leurs devises")

exiger(m.liquidite(B7, m.passer(B7)[1])["objet"] is False,
       "une obligation d'acceptation n'appelle aucun décaissement : sans objet")


# =====================================================================
print("")
print("D. A36 — le démurrage et le prélèvement sont DEUX mécanismes")
# =====================================================================
exiger(m.PRELEVEMENT != m.DEMURRAGE,
       "deux montants distincts (%d et %d)" % (m.PRELEVEMENT, m.DEMURRAGE))
exiger(m.ASSIETTE_DEMURRAGE != m.D,
       "deux assiettes distinctes : la transaction (%d) et l'encaisse (%d)"
       % (m.D, m.ASSIETTE_DEMURRAGE))

libelles = [e.libelle for e in m.sequence(B7)]
exiger(sum(1 for x in libelles if "Prélèvement" in x) == 2
       and sum(1 for x in libelles if "Démurrage" in x) == 2,
       "quatre opérations distinctes : deux faits générateurs, deux règlements")

bil_inst, _, _ = m.passer(par_cle("B2"))
bil_etat, _, _ = m.passer(par_cle("B3"))
e_inst = bil_inst["INST"].get((m.EMISES, m.PASSIF), 0)
e_etat = bil_etat["INST"].get((m.EMISES, m.PASSIF), 0)
exiger(e_etat == e_inst + m.PRELEVEMENT,
       "le collecteur décide de ce qui s'éteint : encours %d si l'émetteur "
       "perçoit, %d si l'État perçoit" % (e_inst, e_etat))
exiger(bil_etat["ETAT"].get((m.AVOIRS, m.ACTIF), 0) == m.PRELEVEMENT,
       "et l'État détient alors les unités qu'il a perçues, sans les éteindre")


# =====================================================================
print("")
if ECHECS:
    print("SABOTAGE NON DÉTECTÉ — le programme n'applique pas ses règles :")
    for e in ECHECS:
        print("  " + e)
    sys.exit(1)
print("Le programme applique ses règles. CELA NE VALIDE AUCUNE DE SES")
print("HYPOTHÈSES COMPTABLES : la reconnaissance retenue est une lecture, et")
print("elle doit être soumise à un contradicteur humain.")
sys.exit(0)
