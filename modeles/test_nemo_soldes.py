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


# =====================================================================
print("")
print("G. A43 (3) SCINDÉ — PARITÉS ADMINISTRÉES CONTRE STRICTEMENT FIXES")
# =====================================================================
declare = m.PAS_PARITE
jeux = {}
for s in m.SCENARIOS:
    jeux[s.cle] = (m.jouer_a_parites(s, declare), m.jouer_a_parites(s, 0.0))
exiger(m.PAS_PARITE == declare,
       "le pas de révision déclaré (%.2f) est rendu après chaque passe" % declare)

for cle in ("S0", "S1", "S2", "S3"):
    (e_adm, _, _), (e_fix, _, _) = jeux[cle]
    exiger(e_fix.contraction["DEF"] > e_adm.contraction["DEF"],
           "%s : figer les parités accroît la contraction du déficitaire "
           "(%.0f contre %.0f)" % (cle, e_fix.contraction["DEF"],
                                  e_adm.contraction["DEF"]))
    exiger(e_fix.soldes_par_periode["EXC"][-1]
           > e_adm.soldes_par_periode["EXC"][-1],
           "%s : et le solde final de l'excédentaire (%.0f contre %.0f)"
           % (cle, e_fix.soldes_par_periode["EXC"][-1],
              e_adm.soldes_par_periode["EXC"][-1]))

for s in m.SCENARIOS:
    (e_adm, _, _), (e_fix, _, _) = jeux[s.cle]
    exiger(abs(taux_essentiel(e_fix) - 100.0) < 1e-9
           and e_fix.alloc["PAU"] >= e_adm.alloc["PAU"],
           "%s : à parités fixes le pays pauvre reste servi en totalité, et le "
           "guichet d'allocation verse au moins autant (%.0f contre %.0f)"
           % (s.cle, e_fix.alloc["PAU"], e_adm.alloc["PAU"]))

e_sans, j_sans, _ = m.jouer_a_parites(par_cle("S2"), 0.0, allocation_active=False)
bloque_sans = sum(j["bloque"][c] for j in j_sans for c in m.CODES)
exiger(bloque_sans > 0 and taux_essentiel(e_sans) < 100.0,
       "S2 à parités fixes SANS allocation : l'essentiel est bloqué (%.0f, "
       "%.1f %% servi)" % (bloque_sans, taux_essentiel(e_sans)))

(_, _, _), (e_fix2, _, _) = jeux["S2"]
e_del, _, a_del = m.jouer_a_parites(par_cle("S2"), 0.0,
                                    symetrie_contraignante=False)
exiger(codes(a_del, "[C6]") and e_del.soldes_par_periode["EXC"][-1]
       > e_fix2.soldes_par_periode["EXC"][-1],
       "S2 à parités fixes sous obligation DÉLIBÉRATIVE : l'excédent crève le "
       "plafond (%d dépassements, solde %.0f contre %.0f)"
       % (len(codes(a_del, "[C6]")), e_del.soldes_par_periode["EXC"][-1],
          e_fix2.soldes_par_periode["EXC"][-1]))

(_, _, a_adm4), (_, _, a_fix4) = jeux["S4"]
exiger(codes(a_adm4, "[C6]") and codes(a_fix4, "[C6]"),
       "S4 : AUCUN des deux régimes ne tient le plafond dur (%d et %d "
       "dépassements) — la perte durable d'un débouché ne relève pas du change"
       % (len(codes(a_adm4, "[C6]")), len(codes(a_fix4, "[C6]"))))
exiger(m.PAS_PARITE == declare,
       "et le pas de révision déclaré est toujours rendu à la fin")


# =====================================================================
print("")
print("H. A43 (3b), CONDITION (1) — LA RÈGLE DE RÉVISION DE L'AUTEUR")
# =====================================================================
OPTIONS = ({}, {"symetrie_contraignante": False}, {"allocation_active": False},
           {"procedure": "blocage"}, {"procedure": "conversion"})
ecarts = 0
for s in m.SCENARIOS:
    for opt in OPTIONS:
        _, j1, a1 = m.jouer(s, **opt)
        _, j2, a2 = m.jouer(s, regle=m.regle_mecanique, **opt)
        ecarts += a1 != a2
        for p1, p2 in zip(j1, j2):
            for champ in ("solde", "masse", "parite", "fac", "alloc", "bloque"):
                ecarts += sum(abs(p1[champ][k] - p2[champ][k]) > 1e-9
                              for k in p1[champ])
exiger(ecarts == 0,
       "une règle fournie passe par le même chemin que la règle par défaut : "
       "la règle mécanique écrite comme règle reproduit le modèle à l'identique "
       "(%d écart sur %d jeux)" % (ecarts, len(m.SCENARIOS) * len(OPTIONS)))

jeux_regles = {}
for s in m.SCENARIOS:
    jeux_regles[s.cle] = (
        m.jouer(s, regle=m.regle_mecanique),
        m.jouer(s, regle=m.regle_de_revision_auteur),
        m.jouer(s, regle=m.regle_de_revision_auteur, symetrie_contraignante=False))

hors_butee, pas_hors_regle = 0, 0
for s in m.SCENARIOS:
    _, (_, j_a, _), _ = jeux_regles[s.cle]
    prec = dict((c, 1.0) for c in m.CODES)
    for p in j_a:
        for c in m.CODES:
            q = p["parite"][c]
            hors_butee += abs(q - 1.0) > m.BUTEE_AUTEUR + 1e-12
            if abs(q - prec[c]) > 1e-12 and \
                    abs(abs(q / prec[c] - 1.0) - m.PAS_GLISSEMENT_AUTEUR) > 1e-9:
                pas_hors_regle += 1
            prec[c] = q
exiger(hors_butee == 0,
       "aucune parité ne s'écarte de plus de %.0f %% de sa valeur de départ"
       % (100 * m.BUTEE_AUTEUR))
exiger(pas_hors_regle == 0,
       "chaque révision est exactement un pas de %.1f %%, dans un sens ou dans "
       "l'autre" % (100 * m.PAS_GLISSEMENT_AUTEUR))

for cle in ("S0", "S1", "S2", "S3"):
    (e_m, _, _), (e_a, _, _), _ = jeux_regles[cle]
    exiger(e_a.contraction["DEF"] < e_m.contraction["DEF"],
           "%s : la règle de l'auteur réduit un peu la contraction du déficitaire "
           "(%.0f contre %.0f)" % (cle, e_a.contraction["DEF"],
                                   e_m.contraction["DEF"]))

(e_m4, _, _), (e_a4, _, _), _ = jeux_regles["S4"]
exiger(e_a4.parite["DEF"] < e_m4.parite["DEF"],
       "S4 : la butée borne la dérive de la parité du déficitaire (%.2f contre "
       "%.2f)" % (e_a4.parite["DEF"], e_m4.parite["DEF"]))
exiger(e_a4.contraction["DEF"] >= e_m4.contraction["DEF"],
       "S4 : SANS y réduire la contraction (%.0f contre %.0f) — la perte durable "
       "d'un débouché passe à la procédure structurelle"
       % (e_a4.contraction["DEF"], e_m4.contraction["DEF"]))

depass_contraignante = sum(len(codes(jeux_regles[s.cle][1][2], "[C6]"))
                           for s in m.SCENARIOS)
depass_deliberative = sum(len(codes(jeux_regles[s.cle][2][2], "[C6]"))
                          for s in m.SCENARIOS)
exiger(depass_deliberative > depass_contraignante,
       "sous la règle de l'auteur, retirer l'obligation contraignante des "
       "excédentaires fait passer les dépassements de %d à %d : aucune règle de "
       "révision ne la remplace" % (depass_contraignante, depass_deliberative))
exiger(all(abs(taux_essentiel(jeux_regles[s.cle][1][0]) - 100.0) < 1e-9
           for s in m.SCENARIOS),
       "et le pays pauvre reste servi en totalité dans les cinq scénarios")

synthese = dict((libelle, m.mesurer_regle(regle))
                for libelle, regle in m.REGLES_MESUREES)
mecanique = synthese["mécanique, par défaut"]
exiger(synthese["auteur : glissement + butée"]["contraction"]
       < mecanique["contraction"],
       "synthèse : la règle de l'auteur réduit la contraction cumulée de S0 à S3 "
       "(%.0f contre %.0f)" % (synthese["auteur : glissement + butée"]["contraction"],
                               mecanique["contraction"]))
for libelle in ("créancier d'abord", "glissement lent (1 %)"):
    exiger(synthese[libelle]["contraction"] > mecanique["contraction"],
           "synthèse : « %s » fait pire que la règle par défaut (%.0f contre %.0f)"
           % (libelle, synthese[libelle]["contraction"], mecanique["contraction"]))
exiger(synthese["proportionnelle bornée"]["pas_max"]
       > synthese["auteur : glissement + butée"]["pas_max"],
       "synthèse : la proportionnelle bornée révise par sauts plus grands que la "
       "règle de l'auteur (%.1f %% contre %.1f %%)"
       % (100 * synthese["proportionnelle bornée"]["pas_max"],
          100 * synthese["auteur : glissement + butée"]["pas_max"]))
exiger(all(r["depass_delib"] > r["depass"] for r in synthese.values()),
       "synthèse : sous obligation délibérative, CHACUNE des cinq règles dépasse "
       "davantage le plafond — le modèle départage mal les règles et très bien "
       "les conditions")


# =====================================================================
print("")
print("I. A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES")
# =====================================================================
def memes_trajectoires(opts_a, opts_b):
    n = 0
    for s in m.SCENARIOS:
        _, ja, aa = m.jouer(s, **opts_a)
        _, jb, ab = m.jouer(s, **opts_b)
        n += aa != ab
        for pa, pb in zip(ja, jb):
            for champ in ("solde", "masse", "parite", "alloc", "bloque"):
                n += sum(abs(pa[champ][k] - pb[champ][k]) > 1e-9 for k in pa[champ])
    return n

exiger(memes_trajectoires({}, {"obligations_creancier": m.OBLIGATIONS_CREANCIER,
                               "delai_creancier": 0, "charge_debiteur": True}) == 0,
       "les nouveaux paramètres, laissés à leur valeur par défaut, ne changent rien")
exiger(memes_trajectoires({"symetrie_contraignante": False},
                          {"obligations_creancier": ()}) == 0,
       "« aucune obligation tenue » est exactement l'obligation délibérative")

R_AUTEUR = {"regle": m.regle_de_revision_auteur}
aucune = m.mesurer_configuration(obligations_creancier=(), **R_AUTEUR)
charge_seule = m.mesurer_configuration(obligations_creancier=("charge",), **R_AUTEUR)
parite_seule = m.mesurer_configuration(obligations_creancier=("parite",), **R_AUTEUR)
les_trois = m.mesurer_configuration(**R_AUTEUR)
exiger(abs(charge_seule["contraction"] - aucune["contraction"]) < 1e-6
       and charge_seule["solde_exc"] < aucune["solde_exc"],
       "la charge seule réduit l'excédent (%.0f contre %.0f) sans soulager le "
       "déficitaire (%.0f dans les deux cas)" % (charge_seule["solde_exc"],
                                               aucune["solde_exc"], aucune["contraction"]))
exiger(parite_seule["contraction"] < 0.7 * aucune["contraction"]
       and les_trois["contraction"] <= parite_seule["contraction"] + 1e-6,
       "la réévaluation de l'excédentaire fait l'essentiel du soulagement "
       "(%.0f contre %.0f sans obligation)" % (parite_seule["contraction"],
                                             aucune["contraction"]))

delais = [m.mesurer_configuration(delai_creancier=d, **R_AUTEUR)["contraction"]
          for d in (0, 2, 4, 8, m.PERIODES)]
exiger(all(b >= a - 1e-6 for a, b in zip(delais, delais[1:]))
       and abs(delais[-1] - aucune["contraction"]) < 1e-6,
       "chaque période d'attente avant activation retire du soulagement, et une "
       "attente égale à l'horizon revient à l'obligation délibérative (%s)"
       % " → ".join("%.0f" % x for x in delais))

deux_cotes = m.mesurer_configuration(**R_AUTEUR)
excedents_seuls = m.mesurer_configuration(charge_debiteur=False, **R_AUTEUR)
auteur_c2 = m.mesurer_configuration(**m.OPTIONS_AUTEUR)
conversion = m.mesurer_configuration(**dict(m.OPTIONS_AUTEUR, procedure="conversion"))
exiger(excedents_seuls["contraction"] < deux_cotes["contraction"]
       and excedents_seuls["contraction_s4"] < deux_cotes["contraction_s4"],
       "la charge sur les débiteurs les enfonce (S4 : %.0f avec, %.0f sans)"
       % (deux_cotes["contraction_s4"], excedents_seuls["contraction_s4"]))
exiger(auteur_c2["contraction_s4"] < excedents_seuls["contraction_s4"]
       and auteur_c2["depass"] == 0 and excedents_seuls["depass"] > 0,
       "la charge sur les excédents détourne ce que le recyclage aurait prêté : "
       "sans elle, S4 tombe à %.0f et plus aucun plafond n'est dépassé"
       % auteur_c2["contraction_s4"])
exiger(conversion["contraction_s4"] > auteur_c2["contraction_s4"],
       "la conversion ne soulage pas le déficitaire en S4 comme le recyclage "
       "(%.0f contre %.0f)" % (conversion["contraction_s4"], auteur_c2["contraction_s4"]))
exiger(auteur_c2["institution"] < excedents_seuls["institution"] < deux_cotes["institution"]
       and auteur_c2["charges_exc"] == 0 and auteur_c2["charges_def"] == 0,
       "ET LE PRIX DU CHOIX DE L'AUTEUR : sans charge, l'institution ne perçoit rien "
       "et cumule le solde le plus négatif (%.0f contre %.0f et %.0f)"
       % (auteur_c2["institution"], excedents_seuls["institution"], deux_cotes["institution"]))
exiger(abs(auteur_c2["essentiel_min"] - 100.0) < 1e-9,
       "et le pays pauvre reste servi en totalité sous la configuration de l'auteur")
exiger(auteur_c2["masse_negative"] > 0,
       "CORRECTION DU 2026-09-17 : sous cette même configuration, le drain extérieur "
       "du déficitaire dépasse sa masse initiale en S4 (%d périodes) — « plus aucun "
       "plafond dépassé » ne disait pas cela" % auteur_c2["masse_negative"])


# =====================================================================
print("")
print("J. A43 (3b), CONDITION (5) — LA PERTE DURABLE D'UN DÉBOUCHÉ")
# =====================================================================
exiger(memes_trajectoires({}, {"procedure_structurelle": None, "recyclage_pret": False}) == 0,
       "sans procédure et sans prêt explicites, le modèle est inchangé")

r_def = m.mesurer_s4(m.PERIODES)
r_c2 = m.mesurer_s4(m.PERIODES, **m.OPTIONS_AUTEUR)
exiger(r_def["premiere_negative"] is not None and r_c2["premiere_negative"] == 13,
       "le contrôle C8 signale la masse négative du déficitaire en S4 : période %s "
       "par défaut, période %s sous les conditions (1) et (2) de l'auteur"
       % (r_def["premiere_negative"], r_c2["premiere_negative"]))

ouvertures = []
for s in m.SCENARIOS:
    e, _, _ = m.jouer(s, **m.OPTIONS_AUTEUR_COMPLETES)
    ouvertures += [(s.cle, c) for c, v in e.procedure_ouverte.items() if v is not None]
exiger(ouvertures == [("S4", "DEF")],
       "la procédure ne s'ouvre qu'en S4, pour le déficitaire : un déficit persistant "
       "sans débouché perdu n'ouvre rien (%s)" % ouvertures)

sans_reussite = m.mesurer_s4(40, **m.OPTIONS_AUTEUR_COMPLETES)
exiger(sans_reussite["masse_min"] > 0 and sans_reussite["negatifs"] == 0
       and sans_reussite["identite"] == 0,
       "réussite non supposée : le financement garde la masse du déficitaire positive "
       "sur 40 périodes (minimum %.0f), et l'identité stock-flux tient avec le prêt"
       % sans_reussite["masse_min"])
exiger(abs(sans_reussite["creee"] - sans_reussite["remboursee"] - sans_reussite["annulee"]
           - sans_reussite["dette"]) < 1e-6,
       "la dette de recyclage se boucle : créée %.0f = remboursée %.0f + annulée %.0f "
       "+ due %.0f" % (sans_reussite["creee"], sans_reussite["remboursee"],
                       sans_reussite["annulee"], sans_reussite["dette"]))
exiger(sans_reussite["close"] == sans_reussite["ouverte"] + m.PROCEDURE_AUTEUR["duree"]
       and abs(sans_reussite["institution"] - m.mesurer_s4(60, **m.OPTIONS_AUTEUR_COMPLETES)["institution"]) < 1e-6,
       "la procédure se clôt à l'échéance (période %s) et l'institution ne verse "
       "qu'une fois : même coût à 40 et à 60 périodes (%.0f)"
       % (sans_reussite["close"], sans_reussite["institution"]))

def s4_avec_reussite(part, horizon=40):
    proc = dict(m.PROCEDURE_AUTEUR, reconversion=dict(m.PROCEDURE_AUTEUR["reconversion"], part=part))
    return m.mesurer_s4(horizon, **dict(m.OPTIONS_AUTEUR_COMPLETES, procedure_structurelle=proc))
r0, r25, r50 = s4_avec_reussite(0.0), s4_avec_reussite(0.25), s4_avec_reussite(0.5)
exiger(abs(r0["masse_min"] - r50["masse_min"]) < 1e-6 and r50["dette"] < r25["dette"] < r0["dette"],
       "sous recyclage, la réussite de la reconversion ne change pas la monnaie du "
       "déficitaire (%.0f dans tous les cas) : elle réduit sa dette (%.0f, %.0f, %.0f)"
       % (r0["masse_min"], r0["dette"], r25["dette"], r50["dette"]))

a60 = m.mesurer_s4(60, **m.OPTIONS_AUTEUR_COMPLETES)
exiger(a60["dette"] > m.QUOTA["DEF"] and a60["annulee"] < 0.05 * a60["dette"],
       "LE PRIX DU CHOIX DE L'AUTEUR : reconversion ratée, 60 périodes, la procédure "
       "close laisse une dette de %.0f, au-delà du quota (%d) ; le créancier ne perd "
       "que %.0f" % (a60["dette"], m.QUOTA["DEF"], a60["annulee"]))
prol = m.mesurer_s4(60, **dict(m.OPTIONS_AUTEUR_COMPLETES,
                               procedure_structurelle=dict(m.PROCEDURE_AUTEUR, revue="prolongation")))
plaf = m.mesurer_s4(60, **dict(m.OPTIONS_AUTEUR_COMPLETES, procedure_structurelle=dict(
    m.PROCEDURE_AUTEUR, revue="prolongation", plafond_annulation=float(m.QUOTA["DEF"]))))
def rupture_puis_reprise(t, volumes, prix):
    """Scénario réservé au test : le débouché se perd, puis revient en force.
    C'est le seul qui fasse rembourser la dette de recyclage."""
    if 4 <= t < 24:
        volumes = dict(volumes)
        volumes[("DEF", "EXC")] = 10
    elif t >= 26:
        volumes = dict(volumes)
        volumes[("DEF", "EXC")] = 260
    return volumes, prix

reprise = m.Scenario("ST", "Rupture puis reprise", rupture_puis_reprise, "test du remboursement")
e_rp, j_rp, a_rp = m.jouer_a_horizon(reprise, 50, **m.OPTIONS_AUTEUR_COMPLETES)
exiger(e_rp.rembourse_pret["DEF"] > 0 and j_rp[-1]["dette"]["DEF"] < 1e-6
       and not codes(a_rp, "[C5]")
       and abs(e_rp.dette_creee["DEF"] - e_rp.rembourse_pret["DEF"]
               - e_rp.dette_annulee["DEF"]) < 1e-6,
       "le remboursement sur les excédents futurs circule sans rompre l'identité "
       "stock-flux : créée %.0f = remboursée %.0f + annulée %.0f, plus rien de dû"
       % (e_rp.dette_creee["DEF"], e_rp.rembourse_pret["DEF"], e_rp.dette_annulee["DEF"]))

exiger(a60["dette"] > plaf["dette"] > prol["dette"]
       and prol["annulee"] > plaf["annulee"] > a60["annulee"]
       and abs(plaf["annulee"] - m.QUOTA["DEF"]) < 1e-6,
       "le choix posé : la clôture charge le débiteur, la prolongation le créancier, et "
       "le plafond partage au quota (dettes %.0f, %.0f, %.0f ; annulations %.0f, %.0f, %.0f)"
       % (a60["dette"], plaf["dette"], prol["dette"], a60["annulee"], plaf["annulee"], prol["annulee"]))


# =====================================================================
print("")
print("K. A43 (3b), CONDITION (4) — QUI FINANCE LES GUICHETS ET LA RECONVERSION")
# =====================================================================
# CE QUE CETTE SECTION NE PROUVE PAS : la taille du reflux. Il n'est pas modélisé,
# et le repère est tiré des besoins eux-mêmes. Elle vérifie ce que le registre du
# découvert compte, et que les conclusions publiées sont celles de la sortie.
# La configuration AU MOMENT DE D75 : la conversion du reliquat (D77) a sa section.
O = m.OPTIONS_AVANT_D77
exiger(memes_trajectoires({}, {"reflux_apurement": 11.0}) == 0
       and memes_trajectoires(dict(O), dict(O, reflux_apurement=40.0)) == 0,
       "le registre du découvert ne change aucune trajectoire, avec ou sans apurement")

pire, bouclage = 0.0, 0.0
for s in m.SCENARIOS:
    _, j, _ = m.jouer_a_horizon(s, 40, **O)
    pire = max([pire] + [abs(p["decouvert"] + p["solde"][m.INST] + sum(p["fac"].values()))
                         for p in j])
    e, _, _ = m.jouer_a_horizon(s, 40, **dict(O, reflux_apurement=11.0))
    bouclage = max(bouclage, abs(e.verse_guichets - e.decouvert - e.apure))
exiger(pire < 1e-9 and bouclage < 1e-9,
       "sans charge, le découvert égale à chaque période le solde négatif de "
       "l'institution moins les facilités en cours ; et versé = découvert + apuré")

BESOINS = m.besoins_des_guichets(40, **O)
REPERE = m.besoin_moyen(BESOINS)
def apurement(cle, multiple):
    return m.mesurer_apurement(par_cle(cle), 40, multiple * REPERE, **O)
au_repere = dict((k, apurement(k, 1.0)) for k in ("S0", "S1", "S2", "S3", "S4"))
exiger(au_repere["S0"]["apure_en"] == 0
       and all(au_repere[k]["apure_en"] is not None and au_repere[k]["pic"] > 0
               for k in ("S1", "S3", "S4"))
       and au_repere["S2"]["apure_en"] is None and au_repere["S2"]["reste"] > 0,
       "au repère (%.2f), les chocs passagers sont apurés dans l'horizon — pics %.0f, "
       "%.0f, %.0f en %s, %s, %s périodes — et le choc structurel ne l'est pas (reste %.0f)"
       % (REPERE, au_repere["S1"]["pic"], au_repere["S3"]["pic"], au_repere["S4"]["pic"],
          au_repere["S1"]["apure_en"], au_repere["S3"]["apure_en"], au_repere["S4"]["apure_en"],
          au_repere["S2"]["reste"]))

moitie = dict((k, apurement(k, 0.5)) for k in ("S1", "S3", "S4"))
double = dict((k, apurement(k, 2.0)) for k in ("S1", "S3", "S4"))
exiger(all(double[k]["apure_en"] < au_repere[k]["apure_en"] < moitie[k]["apure_en"]
           for k in ("S1", "S3")) and moitie["S4"]["apure_en"] is None,
       "moins le reflux est grand, plus le découvert dure ; à la moitié du repère, la "
       "perte d'un débouché n'est plus apurée dans l'horizon (reste %.0f)"
       % moitie["S4"]["reste"])
s2_double, s2_quadruple = apurement("S2", 2.0), apurement("S2", 4.0)
flux_s2 = m.calendrier_reflux_seul(BESOINS["S2"], REPERE)["flux_propre"]
exiger(s2_double["apure_en"] is None and s2_quadruple["apure_en"] is not None
       and 2.0 * REPERE < flux_s2 < 4.0 * REPERE,
       "le choc structurel n'est apuré que si le reflux dépasse le flux de son propre "
       "besoin (%.1f par période) : reste %.0f au double du repère, apuré au quadruple"
       % (flux_s2, s2_double["reste"]))

calendriers = dict((k, m.calendrier_reflux_seul(BESOINS[k], REPERE)) for k in BESOINS)
exiger(all(calendriers[k]["manque"] > 0 for k in ("S1", "S3", "S4"))
       and all(calendriers[k]["flux_minimal"] >= 3.0 * calendriers[k]["flux_propre"]
               and calendriers[k]["fonds_prealable"] >= 0.5 * sum(BESOINS[k])
               for k in ("S0", "S1", "S3", "S4")),
       "LE REFLUX SEUL MANQUE AU MOMENT DES CHOCS : %.0f, %.0f et %.0f en S1, S3, S4 au "
       "repère ; il faudrait un flux d'au moins trois fois le besoin moyen de chaque "
       "scénario passager, ou un fonds d'avance de plus de la moitié du besoin total"
       % (calendriers["S1"]["manque"], calendriers["S3"]["manque"], calendriers["S4"]["manque"]))

sans40 = m.mesurer_incidence_allocation(40, False, **O)
avec40 = m.mesurer_incidence_allocation(40, True, **O)
sans80 = m.mesurer_incidence_allocation(80, False, **O)
avec80 = m.mesurer_incidence_allocation(80, True, **O)
exiger(avec40["essentiel"] > 99.99 > sans40["essentiel"]
       and avec40["contraction_pau"] < sans40["contraction_pau"]
       and abs(avec40["parite_pau"] - 1.0) < 1e-12 < sans40["parite_pau"] - 1.0
       and avec40["exportations_pau"] < sans40["exportations_pau"],
       "S2 : l'allocation sert tout l'essentiel et épargne la monnaie du pays pauvre "
       "(contraction %.0f contre %.0f), qui n'ajuste plus par le change (parité %.2f "
       "contre %.2f)" % (avec40["contraction_pau"], sans40["contraction_pau"],
                          avec40["parite_pau"], sans40["parite_pau"]))
a_la_butee = (avec40["parite_exc"] * (1.0 - m.PAS_GLISSEMENT_AUTEUR)
              < 1.0 - m.BUTEE_AUTEUR <= avec40["parite_exc"])
exiger(avec40["solde_exc"] > sans40["solde_exc"] and avec40["plafond_exc"] > 0
       and avec40["recycle_exc"] == 0 and a_la_butee
       and avec80["plafond_exc"] == 80 - avec40["premier_plafond_exc"] + 1
       and avec80["solde_exc"] > 2.5 * m.QUOTA["EXC"] and sans80["plafond_exc"] == 0,
       "L'ÉMISSION PERMANENTE DEVIENT L'ACCUMULATION PERMANENTE DE L'EXPORTATEUR : "
       "solde %.0f contre %.0f à 40 périodes, %.0f à 80 ; plafond dépassé dès la période "
       "%s puis à chaque période, réévaluation à la butée, recyclage sans destinataire à 40"
       % (avec40["solde_exc"], sans40["solde_exc"], avec80["solde_exc"],
          avec40["premier_plafond_exc"]))
exiger(sans40["plafond_pau"] > 0 and avec40["plafond_pau"] == 0,
       "sans allocation, c'est le pays pauvre qui passe sous son plancher (%d fois à 40 "
       "périodes)" % sans40["plafond_pau"])

e_s1, j_s1, _ = m.jouer_a_horizon(par_cle("S1"), 40, **dict(O, reflux_apurement=REPERE))
exiger(j_s1[-1]["decouvert"] < 1e-9 and e_s1.solde[m.INST] < -100,
       "LE REGISTRE N'EST PAS LE SOLDE : en S1, le découvert est apuré et l'institution "
       "reste à %.0f — le modèle compte ce que le reflux aurait à retirer, il ne le "
       "retire pas" % e_s1.solde[m.INST])


# =====================================================================
print("")
print("L. A43 (3b) — L'ACCUMULATION DE L'EXPORTATEUR SOUS CHOC STRUCTUREL")
# =====================================================================
# CE QUE CETTE SECTION NE PROUVE PAS : qu'un exportateur accepte d'avance
# l'annulation (F6), ni qu'une reconversion de l'importateur réussisse — la baisse
# de dépendance est SUPPOSÉE dans les jeux qui la mesurent.
O77 = m.OPTIONS_AUTEUR_COMPLETES
exiger(memes_trajectoires({}, {"demurrage_soldes": 0.0, "reliquat_plafond": None,
                               "persistance_reliquat": 0}) == 0,
       "les instruments ajoutés, laissés à leur valeur par défaut, ne changent rien")
exiger(O77.get("reliquat_plafond") == "conversion" and not O77.get("demurrage_soldes")
       and dict(O77, reliquat_plafond=None) == m.OPTIONS_AVANT_D77,
       "la configuration de l'auteur porte la conversion du reliquat (D77) et aucun "
       "démurrage sur la compensation (D78)")

S2 = par_cle("S2")
def remede(h, **extra):
    return m.mesurer_accumulation(S2, h, **dict(O77, **extra))
acc80, acc120 = remede(80, reliquat_plafond=None), remede(120, reliquat_plafond=None)
conv = dict((h, remede(h)) for h in (40, 80, 120))
exiger(acc120["solde_exc"] > 3 * m.QUOTA["EXC"] and acc120["au_dela_exc"] > 80
       and acc120["recycle_exc"] > 5 * conv[120]["recycle_exc"],
       "SANS REMÈDE, l'exportateur atteint %.0f à 120 périodes, au-delà du plafond %d "
       "fois, et le recyclage d'un excès accumulé déraille (%.0f recyclés contre %.0f)"
       % (acc120["solde_exc"], acc120["au_dela_exc"], acc120["recycle_exc"],
          conv[120]["recycle_exc"]))
plafond_exc = m.PLAFOND_SOLDE * m.QUOTA["EXC"]
exiger(all(conv[h]["au_dela_exc"] == 0 and conv[h]["solde_exc"] <= plafond_exc + 1e-6
           and conv[h]["negatives"] == 0 and conv[h]["identite"] == 0 for h in conv)
       and abs(conv[80]["institution"] - conv[120]["institution"]) < 1e-6,
       "D77 : la conversion tient l'exportateur au plafond à 40, 80 et 120 périodes, et le "
       "solde de l'institution ne bouge plus entre 80 et 120 (%.0f)" % conv[120]["institution"])

ailleurs = 0
for sc in m.SCENARIOS:
    if sc.cle == "S2":
        continue
    for h in (40, 80, 120):
        _, j0, a0 = m.jouer_a_horizon(sc, h, **m.OPTIONS_AVANT_D77)
        _, j1, a1 = m.jouer_a_horizon(sc, h, **O77)
        ailleurs += int(a0 != a1) + sum(abs(p0["solde"][c] - p1["solde"][c]) > 1e-9
                                        for p0, p1 in zip(j0, j1) for c in m.COMPTES)
exiger(ailleurs == 0, "la conversion ne change aucune trajectoire de S0, S1, S3 et S4")

exiger(conv[80]["converti"] > 0 and conv[80]["masse_exc"] < acc80["masse_exc"]
       and conv[120]["dette_def"] > conv[80]["dette_def"] > 0,
       "LE PRIX DE D77 : l'exportateur perd %.0f de créances à 80 périodes et sa masse reste "
       "à %.0f contre %.0f ; la dette de recyclage du déficitaire croît encore (%.0f puis %.0f)"
       % (conv[80]["converti"], conv[80]["masse_exc"], acc80["masse_exc"],
          conv[80]["dette_def"], conv[120]["dette_def"]))

plac80 = remede(80, reliquat_plafond="placement")
exiger(abs(plac80["solde_exc"] - conv[80]["solde_exc"]) < 1e-6
       and abs(plac80["institution"] - conv[80]["institution"]) < 1e-6
       and abs(plac80["place"] - conv[80]["converti"]) < 1e-6
       and plac80["restitue"] == 0 and plac80["masse_exc"] > conv[80]["masse_exc"],
       "le placement forcé produit les mêmes comptes de compensation, mais garde une "
       "créance de %.0f jamais restituée en S2 : l'accumulation change de registre"
       % plac80["place"])

retour = m.s2_puis_retournement(45)
r_conv = m.mesurer_accumulation(retour, 90, **O77)
r_plac = m.mesurer_accumulation(retour, 90, **dict(O77, reliquat_plafond="placement"))
exiger(r_plac["restitue_exc"] > 0 and r_plac["solde_exc"] >= -1e-9
       and r_conv["solde_exc"] < 0 and r_conv["restitue_exc"] == 0
       and r_plac["identite"] == 0 and r_conv["identite"] == 0,
       "SI LE CHOC SE RETOURNE, le placement rend %.0f à l'exportateur ; sous la "
       "conversion, il n'a plus de réserve et finit à %.0f"
       % (r_plac["restitue_exc"], r_conv["solde_exc"]))

S4 = par_cle("S4")
dem = dict((taux, m.mesurer_accumulation(S4, 40, **dict(O77, demurrage_soldes=taux)))
           for taux in (0.0, 0.005, 0.01))
exiger(dem[0.0]["negatives"] == 0 and dem[0.005]["negatives"] > 0
       and dem[0.01]["depassements"] > 0
       and dem[0.01]["recycle_exc"] < dem[0.005]["recycle_exc"] < dem[0.0]["recycle_exc"],
       "D78 : en S4, le démurrage sur la compensation retire à l'excédentaire ce que le "
       "recyclage aurait prêté — masse du déficitaire négative dès 0,5 %%, %d dépassements "
       "à 1 %%" % dem[0.01]["depassements"])

but80 = remede(80, reliquat_plafond=None, regle=m.regle_sans_butee_creancier)
but120 = remede(120, reliquat_plafond=None, regle=m.regle_sans_butee_creancier)
exiger(abs(but80["allocations"] - but120["allocations"]) < 1e-6
       and but120["parite_min"] < 0.1 and but120["au_dela_exc"] > 0
       and but120["depassements"] > but120["au_dela_exc"],
       "la butée levée arrête l'allocation (%.0f), au prix d'une spirale de réévaluations "
       "(parité minimale %.3f) où chacun passe au-delà du plafond"
       % (but120["allocations"], but120["parite_min"]))

moitie = dict((h, m.mesurer_accumulation(m.s2_avec_substitution(0.5, 11), h, **O77))
              for h in (40, 80))
quart = dict((h, m.mesurer_accumulation(m.s2_avec_substitution(0.25, 11), h,
                                        **m.OPTIONS_AVANT_D77)) for h in (40, 80))
exiger(abs(moitie[40]["allocations"] - moitie[80]["allocations"]) < 1e-6
       and quart[80]["allocations"] > quart[40]["allocations"] and quart[80]["au_dela_exc"] > 0,
       "D79, SUPPOSÉ : une dépendance réduite de moitié arrête l'émission (%.0f à 40 comme "
       "à 80 périodes) ; réduite d'un quart, l'accumulation n'est que retardée"
       % moitie[80]["allocations"])

e77, j77, _ = m.jouer_a_horizon(S2, 80, **O77)
exiger(abs(e77.verse_guichets - e77.decouvert - e77.apure - e77.apure_conversion) < 1e-9
       and max(abs(p["decouvert"] + p["solde"][m.INST] + sum(p["fac"].values()))
               for p in j77) < 1e-9,
       "le reliquat converti apure le découvert : versé = découvert + apuré + converti, "
       "et le découvert reste égal au solde négatif de l'institution hors facilités")


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
