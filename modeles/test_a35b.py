#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SABOTAGE DE LA MATRICE A35b — chaque contrôle doit pouvoir échouer.

Un contrôle qui n'a jamais rejeté quoi que ce soit ne prouve rien : il peut
être mort sans que personne le sache. Ce fichier casse délibérément chaque
règle, une par une, et exige que le contrôle correspondant la voie. Si un
sabotage passe inaperçu, le test échoue et la matrice est déclarée sans valeur
sur ce point.

USAGE :  python modeles/test_a35b.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import a35b_bilans as m

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ECHECS = []


def exiger(condition, libelle):
    print(("  ok   " if condition else "  RATÉ ") + libelle)
    if not condition:
        ECHECS.append(libelle)


def anomalies_de(branche, sabotage=None):
    """Passe une branche, en remplaçant éventuellement sa séquence."""
    vraie = m.sequence
    if sabotage:
        m.sequence = sabotage
    try:
        return m.passer(branche)[1]
    finally:
        m.sequence = vraie


def code(anomalies, n):
    return [a for a in anomalies if a.startswith("[%d" % n)]


B3 = [b for b in m.BRANCHES if b.cle == "B3"][0]
vraie_sequence = m.sequence


print("SABOTAGE 1 — une écriture déséquilibrée doit être vue")
def s1(b):
    E = vraie_sequence(b)
    # on supprime la contrepartie au passif de la banque centrale
    E[1].postes = [p for p in E[1].postes
                   if not (p[0] == "BCN" and p[1] == "dépôt du guichet national")]
    return E

a = anomalies_de(B3, s1)
exiger(code(a, 1), "le contrôle 1 rejette une écriture qui ne se ferme pas")
exiger(code(a, 2), "le contrôle 2 rejette le bilan final correspondant")


print("")
print("SABOTAGE 2 — une variation de situation nette sans motif doit être vue")
def s2(b):
    E = vraie_sequence(b)
    E[0].motifs = {}          # on retire les motifs de l'écriture d'émission
    return E

a = anomalies_de(B3, s2)
exiger(code(a, 3), "le contrôle 3 rejette une richesse qui bouge sans motif")


print("")
print("SABOTAGE 3 — une richesse créée globalement doit être vue")
def s3(b):
    E = vraie_sequence(b)
    # le bénéficiaire s'enrichit sans que personne ne s'appauvrisse
    E[2].postes = [p for p in E[2].postes
                   if not (p[0] == "ETAT" and p[2] == m.SN)]
    E[2].postes += [("ETAT", "dépôt à la banque centrale", m.ACTIF, +m.M)]
    return E

a = anomalies_de(B3, s3)
exiger(code(a, 6), "le contrôle 6 rejette une richesse nette apparue de rien")


print("")
print("SABOTAGE 4 — un encours sans contrepartie doit être vu")
def s4(b):
    E = vraie_sequence(b)
    # les banques inscrivent des réserves que la banque centrale ne doit pas
    E[2].postes += [("BQ", "réserves à la banque centrale", m.ACTIF, +7),
                    ("BQ", "dépôts des bénéficiaires", m.PASSIF, +7)]
    return E

a = anomalies_de(B3, s4)
exiger(code(a, 5), "le contrôle 5 rejette un encours dont le miroir manque")


print("")
print("SABOTAGE 5 — un passif sans obligation doit être vu")
sans_obligation = m.Branche(
    "X", "témoin", circulation="unite_directe",
    inscription="situation_nette", allocation=None,
    beneficiaire="subvention", obligation=None, obligation_envers=None,
    obligation_type=None, droit="", extinction="", pertes="")
a = anomalies_de(sans_obligation)
exiger(code(a, 4), "le contrôle 4 rejette un passif sans obligation présente")
exiger([x for x in a if x.startswith("[4a]")],
       "et il le rejette bien au titre de 4a")


print("")
print("TÉMOINS — ce que les branches intactes doivent donner")
B7 = [b for b in m.BRANCHES if b.cle == "B7"][0]
exiger(not anomalies_de(B7), "B7 passe les sept contrôles sans anomalie")

a = anomalies_de(B3)
exiger(len(a) == 1 and a[0].startswith("[4b]"),
       "B3 ne tombe que sur 4b : ses écritures se ferment, mais son "
       "obligation ne court vers aucun détenteur")
a = anomalies_de([b for b in m.BRANCHES if b.cle == "B2"][0])
exiger(len(a) == 1 and a[0].startswith("[4c]"),
       "B2 ne tombe que sur 4c : sa promesse de conversion n'a pour gage "
       "qu'une créance sur le détenteur lui-même")


print("")
print("SEUIL DE LA CONVERSION — le capital souscrit doit couvrir TOUT l'encours")
import copy
B9 = [b for b in m.BRANCHES if b.cle == "B9"][0]
juste = copy.copy(B9)
juste.souscription = m.M - m.R - 1
a = anomalies_de(juste)
exiger([x for x in a if x.startswith("[4c]")],
       "une souscription de %d, inférieure d'une unité à l'encours de %d, "
       "fait tomber la promesse de conversion" % (m.M - m.R - 1, m.M - m.R))
exiger(not anomalies_de(B9),
       "une souscription égale à l'encours de %d la fait tenir : le seuil "
       "est exactement l'encours restant" % (m.M - m.R))


print("")
print("INVARIANTS DES BRANCHES QUI SE FERMENT")
for b in m.BRANCHES:
    bilans, anomalies = m.passer(b)
    if anomalies:
        continue
    somme = sum(m.totaux(bilans, s)[2] for s, _ in m.SECTEURS)
    depart = sum(v for (_, _, co, v) in m.ouverture(b) if co == m.SN)
    exiger(somme == depart,
           "%s : la richesse finale (%+d) est exactement celle du départ "
           "(%+d) — la matrice n'en a créé aucune" % (b.cle, somme, depart))
    emis = bilans["INST"].get(("unités NEMO émises", m.PASSIF), 0)
    exiger(emis == m.M - m.R,
           "%s : l'encours d'unités restant est de %d, soit l'émission moins "
           "le reflux" % (b.cle, m.M - m.R))


print("")
if ECHECS:
    print("SABOTAGE NON DÉTECTÉ — la matrice est sans valeur sur ces points :")
    for e in ECHECS:
        print("  " + e)
    sys.exit(1)
print("Les sept contrôles rejettent ce qu'ils doivent rejeter, et acceptent le "
      "témoin.")
sys.exit(0)
