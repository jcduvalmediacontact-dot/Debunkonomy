#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DE LA RÈGLE D'ÉMISSION.

CE QU'IL PROUVE : que les trois décisions restent SÉPARÉES — que le veto ne
regarde jamais le mérite, que le calibrage ne refuse jamais au fond, que la
priorité ne classe jamais deux essentiels — et que les résultats publiés par
les sept cas sont ceux que la sortie montre.

CE QU'IL NE PROUVE PAS : que la règle soit bonne. Un test qui applique une
règle prouve qu'elle est appliquée, jamais qu'elle est fondée. Le cas 7 est
d'ailleurs vérifié ICI COMME UN ÉCHEC : le test passe au vert précisément
parce que le mécanisme ne détecte pas la capture.

USAGE :  python modeles/test_nemo_emission.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import nemo_emission as m

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ECHECS = []


def exiger(condition, libelle):
    print(("  ok   " if condition else "  RATÉ ") + libelle)
    if not condition:
        ECHECS.append(libelle)


def clone(p, **kw):
    d = dict(cle=p.cle, libelle=p.libelle, demande=p.demande,
             essentiel=p.essentiel, ressources=p.ressources,
             frontieres=p.frontieres, beneficiaires=p.beneficiaires,
             gravite=p.gravite, rang_depot=p.rang_depot)
    d.update(kw)
    return m.Projet(**d)


# =====================================================================
print("A. LES TROIS DÉCISIONS RESTENT SÉPARÉES")
# =====================================================================
charbon = m.PAR_CLE["charbon"]
merite = clone(charbon, essentiel=True, gravite=3, beneficiaires=10 ** 6)
exiger(m.veto_physique(charbon)[0] is False
       and m.veto_physique(merite)[0] is False,
       "le veto refuse le même projet qu'on le déclare vital ou non : IL NE "
       "REGARDE PAS LE MÉRITE")

eau = m.PAR_CLE["eau"]
indigne = clone(eau, essentiel=False, gravite=0, beneficiaires=0)
exiger(m.veto_physique(eau)[0] is True and m.veto_physique(indigne)[0] is True,
       "et il admet le même projet qu'on le déclare essentiel ou non : IL "
       "N'AUTORISE RIEN, il se borne à ne pas refuser")

trois = [m.PAR_CLE[c] for c in ("eau", "hopital", "logement")]
ech, ecart = m.calibrer(trois, capacite=m.CAPACITE)
servi = sum(sum(e["servi"].values()) for e in ech)
exiger(abs(servi - sum(p.demande for p in trois)) < 1e-6,
       "le calibrage sert INTÉGRALEMENT la demande sur la fenêtre (%.0f sur "
       "%.0f) : il échelonne, il ne refuse pas" % (servi, sum(p.demande for p in trois)))
exiger(len(ech) > 1 and ecart > 0,
       "et il l'échelonne bien quand la capacité manque (%d périodes, écart "
       "de capacité %.0f)" % (len(ech), ecart))

_, indecidable, _ = m.prioriser([m.PAR_CLE["hopital"], m.PAR_CLE["logement"]],
                                400.0)
exiger(indecidable is True,
       "et la priorité REND LA MAIN devant deux essentiels que l'enveloppe ne "
       "couvre pas : le mécanisme ne les classe pas")


# =====================================================================
print("")
print("B. LE VETO A DEUX MOTIFS, ET ILS NE SONT PAS DE MÊME NATURE")
# =====================================================================
hydro, solaire = m.PAR_CLE["hydrogene"], m.PAR_CLE["solaire"]
ok_h, motif_h = m.veto_physique(hydro)
ok_ha, motif_ha = m.veto_physique(hydro, agregation=True)
ok_s, motif_s = m.veto_physique(solaire)
ok_sa, _ = m.veto_physique(solaire, agregation=True)

exiger(ok_h is False and ok_ha is False and "indisponible" in motif_ha,
       "une INDISPONIBILITÉ résiste même au veto agrégé : aucun bilan ne "
       "fabrique du lithium qui n'existe pas")
exiger(ok_s is False and ok_sa is True,
       "un FRANCHISSEMENT, lui, cède au veto agrégé — ce qui prouve que la "
       "variante agrégée PONDÈRE une limite contre une autre")
exiger("franchissement" in motif_s and "biodiversite" in motif_s,
       "et le motif nomme la limite franchie : %s" % motif_s)


# =====================================================================
print("")
print("C. CAS 3 — LES DÉPARTAGES DIVERGENT, DONC LE CHOIX EST POLITIQUE")
# =====================================================================
a, b = m.PAR_CLE["hopital"], m.PAR_CLE["logement"]
gagnants = set(m.departager([a, b], r)[0].cle for r in m.DEPARTAGES)
exiger(len(gagnants) > 1,
       "%d gagnants distincts pour %d départages plausibles : aucune règle "
       "neutre ne départage deux besoins essentiels"
       % (len(gagnants), len(m.DEPARTAGES)))


# =====================================================================
print("")
print("D. CAS 7 — LE MÉCANISME NE VOIT PAS LA CAPTURE")
# =====================================================================
capture = []
for p in m.CATALOGUE:
    if p.cle == "charbon":
        capture.append(clone(p, essentiel=True, gravite=3,
                             frontieres={"carbone": m.DECLARATION_CAPTUREE}))
    else:
        capture.append(p)

honnete_p = m.passer(list(m.CATALOGUE), enveloppe=2000.0, capacite=2000.0)
capture_p = m.passer(capture, enveloppe=2000.0, capacite=2000.0)
detourne = capture_p.emis.get("charbon", 0.0)

exiger(honnete_p.emis.get("charbon", 0.0) == 0.0 and detourne > 0,
       "le passage honnête ne finance pas la centrale, le passage capturé lui "
       "verse %.0f" % detourne)
exiger(capture_p.anomalies == [],
       "ET AUCUN CONTRÔLE NE SE DÉCLENCHE — E1 à E5 tous au vert pendant que "
       "%.0f sont détournés" % detourne)
exiger(len(capture_p.anomalies) == len(honnete_p.anomalies),
       "les deux passages produisent des registres de même forme : rien, de "
       "l'intérieur, ne distingue le sain du capturé")

vraie = m.PAR_CLE["charbon"].frontieres["carbone"]
cumul_declare = capture_p.cumuls.get("carbone", 0.0)
cumul_vrai = cumul_declare - m.DECLARATION_CAPTUREE + vraie
exiger(cumul_declare <= m.FRONTIERES["carbone"] < cumul_vrai,
       "le contrôle cumulé E5 MORD (déclaré %.0f, budget %.0f, réel %.0f) et "
       "la capture se contente de déclarer en dessous : UN CONTRÔLE DE PLUS "
       "DÉPLACE LE MENSONGE, IL NE LE VOIT PAS"
       % (cumul_declare, m.FRONTIERES["carbone"], cumul_vrai))

exiger(not any(a["revocable_par"] is None and "déclar" in a["motif"]
               for a in m.ARRETS),
       "et aucun arrêt ne s'exerce sur autre chose qu'une DÉCLARATION : le "
       "pouvoir d'arrêt physique lui-même est aveugle à une fausse mesure")


# =====================================================================
print("")
print("E. LES CONTRÔLES ATTRAPENT CE QU'ILS DOIVENT ATTRAPER")
# =====================================================================
# Sans quoi le vert du cas 7 ne prouverait rien : un contrôle qui ne se
# déclenche jamais est décoratif.
trop = clone(m.PAR_CLE["eau"], cle="trop", frontieres={"carbone": 390})
p_trop = m.passer([m.PAR_CLE["eau"], m.PAR_CLE["hopital"], trop],
                  enveloppe=2000.0, capacite=2000.0)
exiger(any(x.startswith("[E5]") for x in p_trop.anomalies),
       "E5 se déclenche quand trois projets franchissent ENSEMBLE ce "
       "qu'aucun ne franchit seul : %s"
       % ([x for x in p_trop.anomalies if x.startswith("[E5]")] or "—")[0])
exiger(any(x.startswith("[E2]") for x in m.passer(
           [m.PAR_CLE["eau"]], enveloppe=2000.0, capacite=10.0).anomalies)
       is False,
       "E2 ne se déclenche pas à tort : le calibrage n'émet jamais au-delà de "
       "la capacité, il reporte")


# =====================================================================
print("")
print("F. CE QUI N'EST PAS PUBLIÉ, ET NE DOIT PAS L'ÊTRE")
# =====================================================================
source = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "nemo_emission.py"), encoding="utf-8").read()
exiger(m.SEUILS_CALIBRES is False, "aucun seuil n'est déclaré calibré")
exiger(not hasattr(m, "inflation") and "def inflation" not in source,
       "aucun indicateur d'inflation n'est produit : les prix ne sont pas "
       "endogènes, et le cas 1 ne publie qu'un ÉCART DE CAPACITÉ")
exiger("condition NÉCESSAIRE" in source or "condition NÉCESSAIRE" in m.__doc__,
       "et l'écart de capacité est explicitement dit condition nécessaire, "
       "non suffisante")


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas ses règles :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("Les trois décisions restent séparées et les sept cas rendent ce que la")
print("sortie montre. CELA NE VALIDE PAS LA RÈGLE : cinq des sept cas la")
print("mettent en défaut — le programme les compte lui-même — et le septième")
print("la met en défaut SANS QU'ELLE PUISSE LE SAVOIR. C'est le résultat, pas")
print("un incident de parcours.")
sys.exit(0)
