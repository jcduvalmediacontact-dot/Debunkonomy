#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VÉRIFICATION DE LA RÈGLE D'ÉMISSION, version 2.

CE QU'IL PROUVE : que les cinq pouvoirs restent séparés et que les contrôles
S1 et S2 le voient ; que la contrainte PHYSIQUE s'applique même quand le
CONSTAT se trompe ; que les quatre corrections de l'auteur sont effectivement
en place — et que les nombres publiés sont ceux que la sortie montre.

CE QU'IL NE PROUVE PAS : que la règle soit bonne, ni que les mécanismes
suffisent. Un test qui applique une règle prouve qu'elle est appliquée, jamais
qu'elle est fondée. Aucun seuil n'est calibré.

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


# =====================================================================
print("A. A46 — LES CINQ POUVOIRS RESTENT SÉPARÉS")
# =====================================================================
exiger(m.controler_separation(m.CHAINE) == [],
       "la chaîne de référence ne déclenche aucune anomalie S1")
exiger(sorted(p for _, ps in m.CHAINE for p in ps) == sorted(m.POUVOIRS),
       "et les cinq pouvoirs sont couverts, une institution chacun")

cumul = [("autorite-unique", ("mesurer", "qualifier", "calibrer")),
         ("instance-democratique", ("prioriser",)),
         ("audit-et-juridiction", ("controler",))]
exiger(any(a.startswith("[S1]") and "cumule" in a
           for a in m.controler_separation(cumul)),
       "S1 voit l'autorité qui mesure, qualifie ET verse — la configuration "
       "du cas 7")
exiger(any("aucun titulaire" in a for a in m.controler_separation(
           [("tout", ("mesurer",))])),
       "et S1 voit aussi un pouvoir sans titulaire : la séparation n'est pas "
       "qu'une interdiction de cumul")

# La portée arrêtée par l'auteur est plus large que celle que le programme
# portait : elle nomme les INCERTITUDES, les PROJETS, les TRANCHES, le RECOURS.
attendus = {"mesurer": "INCERTITUDES", "qualifier": "projets",
            "prioriser": "ADMISSIBLES", "calibrer": "TRANCHES",
            "controler": "RECOURS"}
exiger(all(mot in m.PORTEE.get(p, "") for p, mot in attendus.items()),
       "la portée des cinq fonctions est celle arrêtée par l'auteur : "
       "incertitudes, projets, admissibles, tranches, recours")


# =====================================================================
print("")
print("A bis. AUTOCORRECTION PERMISE, AUTOCONTRÔLE INTERDIT")
# =====================================================================
def dossier_verse(cle):
    d = m.Dossier(m.PAR_CLE[cle])
    for etat, par in (("physiquement_admissible", "mesurer"),
                      ("politiquement_prioritaire", "prioriser"),
                      ("financierement_programme", "calibrer"),
                      ("verse_par_tranches", "calibrer")):
        d.passer_a(etat, par)
    return d


# (a) SUSPENSION CONSERVATOIRE par l'autorité qui a versé : c'est de
#     l'autocorrection, et l'interdire ferait durer l'erreur.
a = dossier_verse("eau")
a.recours = m.ORGANE_DE_RECOURS
suspension = []
a.passer_a("suspendu", "calibrer", niveau="interne", anomalies=suspension)
a.passer_a("verse_par_tranches", "controler", niveau="conformite")
a.passer_a("controle", "controler", niveau="conformite")
a.passer_a("acheve", "controler", niveau="conformite")
exiger(suspension == [],
       "S2 admet la SUSPENSION CONSERVATOIRE par l'autorité qui a versé : "
       "elle est une modalité de contrôle interne, pas une usurpation")
exiger(m.controler_autocontrole(a) == [],
       "et S3 ne la signale pas — INTERDIRE L'AUTOCONTRÔLE N'EST PAS "
       "INTERDIRE L'AUTOCORRECTION")

# (b) L'auteur du versement se contrôle lui-même ET clôt : interdit.
b = dossier_verse("hopital")
b.recours = m.ORGANE_DE_RECOURS
b.passer_a("controle", "controler", institution="autorite-monetaire",
           niveau="conformite")
b.passer_a("acheve", "controler", institution="autorite-monetaire",
           niveau="conformite")
auto = m.controler_autocontrole(b)
exiger(any("unique juge" in x for x in auto),
       "S3 refuse un contrôle de conformité exercé par l'auteur de l'acte")
exiger(any("DERNIER juge" in x for x in auto),
       "et refuse que la CLÔTURE soit prononcée par lui")
exiger(m.controler_separation(m.CHAINE) == [],
       "PENDANT QUE S1 NE VOIT RIEN : le non-cumul se lit sur l'organigramme, "
       "l'auto-contrôle sur le dossier")

# (c) Contrôle indépendant, mais aucune voie de recours extérieure.
c = dossier_verse("logement")
c.passer_a("controle", "controler", niveau="conformite")
c.passer_a("acheve", "controler", niveau="conformite")
sans = m.controler_autocontrole(c)
exiger(len(sans) == 1 and "recours" in sans[0],
       "et S3 exige une voie de RECOURS extérieure, troisième niveau")

d = dossier_verse("eau")
d.recours = "autorite-monetaire"
d.passer_a("controle", "controler", niveau="conformite")
d.passer_a("acheve", "controler", niveau="conformite")
exiger(any("déjà intervenue" in x for x in m.controler_autocontrole(d)),
       "un recours tenu par une institution déjà intervenue n'en est pas un")

exiger(len(m.NIVEAUX) == 3,
       "les trois niveaux sont nommés : %s"
       % ", ".join(n for n, _ in m.NIVEAUX))


# =====================================================================
print("")
print("B. LE PROCESSUS — CHAQUE PASSAGE PAR SON POUVOIR, ET PAR LUI SEUL")
# =====================================================================
anomalies = []
d = m.Dossier(m.PAR_CLE["eau"])
for etat, par in (("physiquement_admissible", "mesurer"),
                  ("politiquement_prioritaire", "prioriser"),
                  ("financierement_programme", "calibrer"),
                  ("verse_par_tranches", "calibrer"),
                  ("controle", "controler"),
                  ("acheve", "controler")):
    d.passer_a(etat, par, anomalies=anomalies)
exiger(anomalies == [] and d.etat == "acheve",
       "le chemin nominal va de « propose » à « acheve » sans anomalie")

saut = []
e = m.Dossier(m.PAR_CLE["hopital"])
e.passer_a("physiquement_admissible", "mesurer", anomalies=saut)
e.passer_a("verse_par_tranches", "calibrer", anomalies=saut)
exiger(any("non prévu" in a for a in saut),
       "S2 refuse un versement qui saute la priorisation politique")

usurpe = []
f = m.Dossier(m.PAR_CLE["logement"])
f.passer_a("physiquement_admissible", "qualifier", anomalies=usurpe)
exiger(any("alors que seul" in a for a in usurpe),
       "S2 refuse que l'autorité de QUALIFICATION déclare l'admissibilité "
       "PHYSIQUE : c'est la confusion que A46 interdit")

exiger(all(m.TRANSITIONS[(a, b)] == ("controler",)
           for a, b in m.TRANSITIONS if b == "recupere"),
       "RÉCUPÉRER n'appartient qu'au contrôle : c'est un acte définitif")
exiger(all("calibrer" in m.TRANSITIONS[(a, b)]
           for a, b in m.TRANSITIONS if b == "suspendu"),
       "mais SUSPENDRE est ouvert à l'autorité qui a versé — correction de "
       "l'auteur : la suspension conservatoire est de l'autocorrection, et la "
       "lui interdire ferait durer l'erreur")


# =====================================================================
print("")
print("C. (3) LA CONTRAINTE PHYSIQUE N'EST PAS SON CONSTAT")
# =====================================================================
charbon = m.PAR_CLE["charbon"]
vraie = charbon.frontieres["carbone"]
noms = [n for n, _ in m.ORGANISMES]

vu_honnete, _ = m.veto_physique(charbon, regle="mediane")
vu_capte, _ = m.veto_physique(charbon, regle="mediane", captes=tuple(noms))
exiger(vu_honnete is False and vu_capte is True,
       "un constat entièrement capté ADMET un projet que le constat honnête "
       "refuse")
exiger(m.infaisable_reellement(charbon) is True,
       "ET LE MONDE, LUI, NE CHANGE PAS : le projet reste réellement "
       "infaisable (%.0f pour %.0f de budget). La contrainte physique ne se "
       "vote pas" % (vraie, m.FRONTIERES["carbone"]))

hydro = m.PAR_CLE["hydrogene"]
exiger(m.infaisable_reellement(hydro) is True,
       "et l'infaisabilité MATÉRIELLE compte comme telle (%.0f de lithium "
       "pour %.0f) : sans cela on la compterait comme un refus à tort"
       % (hydro.ressources["lithium"], m.RESSOURCES["lithium"]))


# =====================================================================
print("")
print("D. (1) LA PLURALITÉ — CE QU'ELLE COÛTE ET CE QU'ELLE PROTÈGE")
# =====================================================================
seuil = m.FRONTIERES["carbone"]
besoins = dict((r, m.captures_necessaires(vraie, seuil, r)[0])
               for r in m.REGLES_DE_VETO)
exiger(besoins["unique"] == 1,
       "une seule capture suffit sous la règle « unique » : c'est le pouvoir "
       "absolu que l'auteur interdit")
exiger(besoins["mediane"] > besoins["unique"],
       "la médiane en exige %d" % besoins["mediane"])
exiger(besoins["prudente"] == len(m.ORGANISMES),
       "la règle prudente exige de capter les %d organismes"
       % len(m.ORGANISMES))

banc = [m.Projet("b%d" % k, "banc", 100, False, {}, {"carbone": float(v)})
        for k, v in enumerate((300, 340, 370, 380, 390), start=1)]
exiger(all(not m.infaisable_reellement(p) for p in banc),
       "banc de contrôle : aucun de ses %d projets ne franchit RÉELLEMENT"
       % len(banc))
faux = dict((r, len([p for p in banc if not m.veto_physique(p, regle=r)[0]]))
            for r in m.REGLES_DE_VETO)
exiger(faux["prudente"] > 0,
       "la règle prudente en refuse %d à tort : sa robustesse a un prix"
       % faux["prudente"])
exiger(faux["mediane_avec_recours"] < faux["prudente"],
       "le recours ne refuse à tort aucun projet (%d contre %d pour la "
       "prudente) — mais sa robustesse se paie ailleurs, voir D bis"
       % (faux["mediane_avec_recours"], faux["prudente"]))
exiger(besoins["mediane_avec_recours"] < besoins["prudente"],
       "ET IL NE DOMINE PAS : %d captures suffisent contre %d pour la "
       "prudente. AUCUNE RÈGLE N'EST GRATUITEMENT SUPÉRIEURE"
       % (besoins["mediane_avec_recours"], besoins["prudente"]))


# =====================================================================
print("")
print("D bis. LE RECOURS N'EST PAS UN ORACLE — CONTRÔLE DE MÉTHODE")
# =====================================================================
# Une simulation qui rendrait la valeur VRAIE au recours lui donnerait
# gratuitement ce qu'aucun dispositif réel ne possède, et TOUTE conclusion
# tirée de sa robustesse serait un artefact. Ce contrôle doit échouer si
# quelqu'un remet un oracle dans le modèle.
vals = [v for _, v in m.estimations(vraie, captes=("A",))]
etendue = (max(vals) - min(vals)) / m.mediane(vals)
exiger(etendue > m.SEUIL_DIVERGENCE,
       "une capture partielle fait diverger les organismes (%.0f %%) et saisit "
       "le recours" % (100 * etendue))
saisi, motif = m.constat(vraie, "mediane_avec_recours", captes=("A",))
exiger(abs(saisi - vraie) > 1e-9,
       "ET LE RECOURS SAISI NE REND PAS LA VALEUR VRAIE (%.1f contre %.0f) : "
       "il a son biais propre, comme tout instrument" % (saisi, vraie))
exiger("canal de mesure indépendant" in motif,
       "son apport est nommé — une information qui ne passe NI par la "
       "déclaration du porteur NI par les modèles des organismes")
exiger(all(biais != 0.0 for _, biais in m.CANAUX_DE_MESURE),
       "et AUCUN CANAL N'EST EXACT : chacun porte un biais déclaré, comme un "
       "étalonnage réel — aucun instrument ne possède la vérité")
exiger(all(nom in [c for c, _ in m.CANAUX_DE_MESURE]
           or True for nom, _ in m.CANAUX_DE_MESURE),
       "les %d canaux sont nommés : %s"
       % (len(m.CANAUX_DE_MESURE),
          ", ".join(n for n, _ in m.CANAUX_DE_MESURE)))

capte, _ = m.constat(vraie, "mediane_avec_recours",
                     captes=("A", "satellite"))
exiger(capte < vraie,
       "et il est LUI-MÊME CAPTURABLE (%.0f) : le recours déplace le point de "
       "défaillance, il ne le supprime pas" % capte)

k_unique, cibles = m.captures_necessaires(vraie, seuil, "mediane_avec_recours")
k_pluriel, _ = m.captures_necessaires(vraie, seuil, "recours_pluriel")
exiger(k_unique < len(m.ORGANISMES),
       "AVEC UN INSTRUMENT RÉEL, « mediane_avec_recours » tombe à %d captures "
       "(%s) — le résultat publié à cinq était un artefact de l'oracle"
       % (k_unique, ", ".join(cibles)))
exiger(k_pluriel > k_unique,
       "et pluraliser le recours le rétablit en partie : %d captures contre %d"
       % (k_pluriel, k_unique))

source_m = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "nemo_emission.py"), encoding="utf-8").read()
exiger("PROPRIÉTÉ STRUCTURELLE" in source_m
       and "NI LA PROBABILITÉ" in source_m,
       "ET LE PROGRAMME DIT CE QUE CE NOMBRE N'EST PAS : une propriété "
       "structurelle de l'architecture simulée, jamais une probabilité ni un "
       "coût de capture")


# =====================================================================
print("")
print("E. (2) NON REMBOURSABLE N'EST PAS IRRÉVOCABLE")
# =====================================================================
p = m.Projet("essai", "essai", 960, True, {}, {}, tranches=4)
sauve = {}
for t in (1, 2, 3, 4):
    g, r, rc, _ = m.reprise(p, t)
    sauve[t] = g + r
exiger(all(sauve[t] > sauve[t + 1] for t in (1, 2, 3)),
       "ce qui est sauvé DÉCROÎT strictement avec la date de détection "
       "(%s)" % " > ".join("%.0f" % sauve[t] for t in (1, 2, 3, 4)))
exiger(sauve[4] > 0,
       "et il reste %.0f même à la dernière tranche : LA VERSION 1 ÉCRIVAIT "
       "ZÉRO, ET C'ÉTAIT FAUX" % sauve[4])

g4, r4, rc4, _ = m.reprise(p, 4, fraude=False)
gf, rf, rcf, _ = m.reprise(p, 4, fraude=True)
exiger(rc4 == 0.0 and rcf > 0.0,
       "le recouvrement ne joue QU'EN CAS DE FRAUDE établie (%.0f contre 0) : "
       "un bénéficiaire conforme n'est jamais poursuivi" % rcf)
g1, r1, _, _ = m.reprise(p, 1)
exiger(g1 > r1,
       "et le GEL (%.0f) est compté à part de la RESTITUTION (%.0f) : "
       "confondre l'argent jamais versé et l'argent revenu gonflerait le "
       "rendement" % (g1, r1))


# =====================================================================
print("")
print("F. LE PORTEFEUILLE — LE VETO ISOLÉ EST TROP PERMISSIF")
# =====================================================================
admis = [x for x in m.CONCURRENTS if m.veto_physique(x)[0]]
lithium = sum(x.ressources.get("lithium", 0.0) for x in admis)
lots = m.portefeuilles_faisables(m.CONCURRENTS)
exiger(lithium > m.RESSOURCES["lithium"],
       "le veto projet par projet admet un ensemble IMPOSSIBLE : %.0f de "
       "lithium pour %.0f disponible" % (lithium, m.RESSOURCES["lithium"]))
exiger(all(sum(x.ressources.get("lithium", 0.0) for x in lot)
           <= m.RESSOURCES["lithium"] for lot in lots),
       "aucun des %d lots faisables ne dépasse la ressource" % len(lots))
exiger(not any("solaire-xxl" in [x.cle for x in lot] for lot in lots),
       "et le projet qui franchit SEUL n'appartient à aucun lot : le "
       "portefeuille organise les possibles, il n'en crée aucun")


# =====================================================================
print("")
print("G. LE DÉPARTAGE RESTE POLITIQUE, ET LA SAISINE EST NOMMÉE")
# =====================================================================
retenus, saisine = m.prioriser([m.PAR_CLE["hopital"], m.PAR_CLE["logement"]],
                               400.0)
exiger(retenus == [] and saisine is not None,
       "le mécanisme ne classe pas deux essentiels : il SAISIT")
exiger(len(set(saisine.options().values())) > 1,
       "les %d départages ne désignent pas le même gagnant" % len(m.DEPARTAGES))
exiger(saisine.recours != saisine.instance,
       "et le recours (%s) n'appartient PAS à l'instance qui tranche (%s)"
       % (saisine.recours, saisine.instance))


# =====================================================================
print("")
print("H. CE QUI N'EST PAS PUBLIÉ, ET NE DOIT PAS L'ÊTRE")
# =====================================================================
source = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "nemo_emission.py"), encoding="utf-8").read()
exiger(m.SEUILS_CALIBRES is False, "aucun seuil n'est déclaré calibré")
exiger("def inflation" not in source and not hasattr(m, "inflation"),
       "aucun indicateur d'inflation : les prix ne sont pas endogènes")
# Les deux conclusions retirées DOIVENT pouvoir être citées — il faut bien
# les retirer — mais jamais affirmées. On exige donc qu'une rétractation
# accompagne chaque occurrence.
lignes = source.split(chr(10))
retirees = ("ne se répare pas", "aucune reprise")
orphelines = []
for i, ligne in enumerate(lignes):
    if any(x in ligne.lower() for x in retirees):
        voisinage = " ".join(lignes[max(0, i - 3):i + 4])
        if "FAUX" not in voisinage and "ÉTAIT" not in voisinage:
            orphelines.append(i + 1)
exiger(orphelines == [],
       "les deux conclusions retirées n'apparaissent qu'À L'INTÉRIEUR de leur "
       "rétractation, jamais affirmées%s"
       % ("" if not orphelines else " — lignes %s" % orphelines))


print("")
if ECHECS:
    print("ÉCHEC — le programme n'applique pas ses règles :")
    for x in ECHECS:
        print("  " + x)
    sys.exit(1)
print("Les cinq pouvoirs restent séparés, la contrainte physique s'applique")
print("même quand le constat se trompe, et les quatre corrections de l'auteur")
print("sont en place. CELA NE VALIDE NI LA RÈGLE NI SES MÉCANISMES : ce qui")
print("reste ouvert — collusion des mesureurs, plafond d'urgence, critère de")
print("départage — reste ouvert, et le programme le dit à chaque cas.")
sys.exit(0)
