#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A47 — DÉCIDER SOUS INCERTITUDE. VERSION 2, VALIDÉE PAR L'AUTEUR LE 2026-09-09.

CE QUE LA VERSION 2 CHANGE, ET C'EST UNE RÉPONSE AU PREMIER TROU. La version 1
répartissait la charge de la preuve après une qualification dont elle ne disait
ni l'auteur ni la procédure. LA VERSION 2 LE DIT :

  — les SEUILS NORMATIFS sont fixés À L'AVANCE par l'AUTORITÉ DÉMOCRATIQUE,
    APRÈS EXPERTISE PLURALISTE ;
  — la QUALIFICATION est MOTIVÉE SELON CETTE GRILLE GÉNÉRALE.

La qualification cesse donc d'être un jugement libre : elle applique une grille
publiée d'avance, et elle se motive. Le pouvoir de fixer la grille et celui de
l'appliquer sont séparés, conformément à A46.

LA DOCTRINE ADOPTÉE, DANS LES TERMES DE L'AUTEUR

  1. Évaluation SÉPARÉE de la gravité, de l'étendue, de la PLAUSIBILITÉ, de la
     réversibilité et des INCERTITUDES.
  2. Seuils normatifs fixés à l'avance par l'autorité démocratique après
     expertise pluraliste.
  3. Qualification MOTIVÉE selon cette grille générale.
  4. Charge de la preuve ADAPTÉE À LA NATURE DU RISQUE.
  5. Autorisation PROGRESSIVE pour les risques limités et réversibles.
  6. PROTECTION PARTICULIÈRE des besoins essentiels urgents.
  7. Arbitrage AU NIVEAU DU PORTEFEUILLE pour les ressources rares.
  8. Procédure PUBLIQUE pour la révision des seuils.
  9. Recours mobilisant des examinateurs et des CANAUX DE MESURE INDÉPENDANTS.

RESTENT OUVERTS, ET L'AUTEUR LES NOMME : les seuils numériques, LES HORIZONS
SECTORIELS et leurs méthodes de calibration.

CE QUE CE PROGRAMME MESURE. Jusqu'où la grille détermine effectivement la
qualification — et ce qui se passe là où elle se tait. DEUX RÉSULTATS
DÉFAVORABLES SUBSISTENT, et ils sont chiffrés : la grille ne couvre que deux
domaines sur six, et l'incertitude est évaluée sans qu'aucune règle ne dise ce
qu'elle emporte.

AUCUN SEUIL N'EST CALIBRÉ. Les dossiers sont fictifs, et un programme qui
applique une règle ne la valide jamais.

USAGE :  python modeles/nemo_a47.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False


# =====================================================================
# POINT 1 — CINQ DIMENSIONS ÉVALUÉES SÉPARÉMENT
# =====================================================================
DIMENSIONS = ("gravite", "etendue", "plausibilite", "reversibilite",
              "incertitude")


class Dossier(object):
    """LA RÉVERSIBILITÉ N'EST PAS UN BOOLÉEN : elle dépend de l'horizon, et
    l'horizon est un choix normatif que la grille doit fixer."""

    def __init__(self, cle, libelle, domaine, gravite, etendue, plausibilite,
                 reversible_sur, incertitude, urgence=False, essentiel=False):
        self.cle = cle
        self.libelle = libelle
        self.domaine = domaine
        self.gravite = gravite            # 0 à 3
        self.etendue = etendue            # 0 à 3
        self.plausibilite = plausibilite  # 0 à 1 : le dommage est-il probable
        self.reversible_sur = dict(reversible_sur)   # horizon → booléen
        self.incertitude = incertitude    # 0 à 1 : que sait-on, au juste
        self.urgence = urgence
        self.essentiel = essentiel


HORIZONS = ("cinquante ans", "échelle humaine")

DOSSIERS = [
    Dossier("renovation", "Rénovation thermique", "batiment", 1, 1, 0.20,
            {"cinquante ans": True, "échelle humaine": True}, 0.20),
    Dossier("stockage-geo", "Stockage géologique de CO2", "energie", 2, 2,
            0.50, {"cinquante ans": True, "échelle humaine": False}, 0.60),
    Dossier("barrage", "Grand barrage en zone habitée", "eau", 3, 3, 0.70,
            {"cinquante ans": False, "échelle humaine": False}, 0.30),
    Dossier("pesticide", "Pesticide à large spectre", "agriculture", 2, 3,
            0.60, {"cinquante ans": True, "échelle humaine": True}, 0.50),
    Dossier("mine-lithium", "Mine de lithium", "mines", 2, 1, 0.30,
            {"cinquante ans": False, "échelle humaine": False}, 0.40),
    Dossier("medicament", "Traitement essentiel en épidémie", "sante", 3, 0,
            0.55, {"cinquante ans": False, "échelle humaine": False}, 0.80,
            urgence=True, essentiel=True),
]


# =====================================================================
# POINTS 2 ET 3 — LA GRILLE, FIXÉE D'AVANCE, ET LA QUALIFICATION MOTIVÉE
# =====================================================================
GRILLE = {
    "fixee_par": "instance-democratique",
    "apres": "expertise pluraliste",
    "publiee": "avant l'examen des dossiers",
    "seuil_plausibilite": 0.50,
    "gravite_serieuse": 2,
    "etendue_limitee": 2,
    # LES HORIZONS SECTORIELS — pièce de conception OUVERTE, et la grille de
    # référence n'en couvre que deux. C'est délibéré : le programme mesure ce
    # que coûte une grille incomplète.
    "horizons": {"energie": "échelle humaine",
                 "agriculture": "cinquante ans"},
    # CE QUE L'INCERTITUDE EMPORTE — non fixé. La doctrine l'évalue et la
    # publie ; elle ne dit pas ce qu'on en fait.
    "usage_des_incertitudes": None,
}

def grille_complete(horizon="échelle humaine"):
    """La même grille, mais dont les horizons couvrent TOUS les domaines.

    SANS CETTE COMPARAISON, le programme imputerait à la doctrine ce qui vient
    du scénario : la grille de référence est délibérément incomplète, et son
    incomplétude est un PARAMÈTRE, non un résultat.
    """
    g = dict(GRILLE)
    g["horizons"] = dict((d.domaine, horizon) for d in DOSSIERS)
    return g


REGIMES = {
    "grave_irreversible": ("porteur",
                           "établir une compatibilité suffisante"),
    "limite_reversible": ("autorité",
                          "motiver tout refus ; autorisation progressive"),
    "urgence_essentielle": ("décision provisoire",
                            "protection particulière : solution la moins "
                            "risquée, quantité minimale, réexamen rapide"),
    "non_determine": (None, "la grille ne détermine pas ce dossier"),
}


def qualifier(d, grille=None):
    """Rend (regime, motivation, anomalies). LA QUALIFICATION APPLIQUE LA
    GRILLE ET SE MOTIVE — elle ne juge pas librement."""
    g = GRILLE if grille is None else grille
    anomalies = []

    if d.urgence and d.essentiel:
        return ("urgence_essentielle",
                "besoin essentiel urgent — protection particulière",
                anomalies)

    horizon = g["horizons"].get(d.domaine)
    if horizon is None:
        anomalies.append(
            "[Q2] %s : la grille ne fixe aucun HORIZON pour le domaine « %s » "
            "— la réversibilité n'est pas déterminée (%s)"
            % (d.cle, d.domaine,
               " / ".join("%s : %s" % (h, "réversible" if v else "irréversible")
                          for h, v in sorted(d.reversible_sur.items()))))
        return ("non_determine", "horizon sectoriel non fixé", anomalies)

    reversible = d.reversible_sur[horizon]
    if (d.plausibilite >= g["seuil_plausibilite"]
            and d.gravite >= g["gravite_serieuse"] and not reversible):
        return ("grave_irreversible",
                "plausibilité %.2f ≥ %.2f, gravité %d ≥ %d, irréversible à "
                "l'horizon « %s »" % (d.plausibilite, g["seuil_plausibilite"],
                                      d.gravite, g["gravite_serieuse"],
                                      horizon),
                anomalies)
    if (reversible and d.gravite <= g["gravite_serieuse"]
            and d.etendue <= g["etendue_limitee"]):
        return ("limite_reversible",
                "réversible à l'horizon « %s », gravité %d ≤ %d, étendue %d ≤ "
                "%d" % (horizon, d.gravite, g["gravite_serieuse"], d.etendue,
                        g["etendue_limitee"]),
                anomalies)
    return ("non_determine",
            "hors des deux pôles : gravité %d, étendue %d, %s à l'horizon "
            "« %s », plausibilité %.2f"
            % (d.gravite, d.etendue,
               "réversible" if reversible else "irréversible", horizon,
               d.plausibilite),
            anomalies)


def controler_grille(grille=None):
    """Q1, Q3, Q4 — ce que la grille doit dire, et ce qu'elle ne dit pas."""
    g = GRILLE if grille is None else grille
    anomalies = []
    if g.get("publiee") != "avant l'examen des dossiers":
        anomalies.append("[Q1] la grille n'est pas publiée avant l'examen")
    if g.get("usage_des_incertitudes") is None:
        anomalies.append(
            "[Q3] l'INCERTITUDE est évaluée et publiée, mais aucune règle ne "
            "dit ce qu'elle emporte")
    if g.get("fixee_par") == "autorite-de-qualification":
        anomalies.append(
            "[Q4] la grille est fixée par l'autorité qui l'applique — A46")
    manquants = [d.domaine for d in DOSSIERS
                 if d.domaine not in g.get("horizons", {})]
    if manquants:
        anomalies.append(
            "[Q2] aucun horizon sectoriel pour %d domaine(s) sur %d : %s"
            % (len(set(manquants)), len(set(d.domaine for d in DOSSIERS)),
               ", ".join(sorted(set(manquants)))))
    return anomalies


# =====================================================================
# POINT 8 — CE QUE TOUTE DÉCISION PUBLIE
# =====================================================================
PUBLICATION = ("donnees", "methodes", "incertitudes", "seuil_normatif",
               "avis_minoritaires")


def controler_publication(decision):
    return ["[P1] %s : « %s » n'est pas publié" % (decision.get("cle"), champ)
            for champ in PUBLICATION if not decision.get(champ)]


# =====================================================================
def titre(libelle):
    print("")
    print("=" * 78)
    print(libelle)
    print("=" * 78)


def la_grille():
    titre("POINTS 2 ET 3 — LA GRILLE FIXÉE D'AVANCE, ET CE QU'ELLE COUVRE")
    print("  fixée par        %s" % GRILLE["fixee_par"])
    print("  après            %s" % GRILLE["apres"])
    print("  publiée          %s" % GRILLE["publiee"])
    print("  seuils           plausibilité %.2f, gravité sérieuse %d, "
          "étendue limitée %d"
          % (GRILLE["seuil_plausibilite"], GRILLE["gravite_serieuse"],
             GRILLE["etendue_limitee"]))
    print("  horizons         %s"
          % ", ".join("%s : %s" % (k, v)
                      for k, v in sorted(GRILLE["horizons"].items())))
    print("")
    print("  CE QUE LA VERSION 2 RÈGLE, ET C'ÉTAIT LE PREMIER TROU. La")
    print("  qualification n'est plus un jugement libre : elle APPLIQUE une")
    print("  grille PUBLIÉE D'AVANCE, fixée par l'autorité démocratique après")
    print("  expertise pluraliste, et elle SE MOTIVE. Le pouvoir de fixer la")
    print("  grille et celui de l'appliquer sont séparés — c'est A46.")
    print("")
    anomalies = controler_grille()
    for a in anomalies:
        print("    %s" % a)
    return anomalies


def application():
    titre("LA GRILLE APPLIQUÉE — ET CE QU'ELLE DÉTERMINE VRAIMENT")
    print("  %-14s %-12s %3s %3s %5s %5s  %-20s %s"
          % ("dossier", "domaine", "gra", "éte", "plaus", "incer", "régime",
             "charge"))
    regimes, motivations, alertes = {}, {}, []
    for d in DOSSIERS:
        r, motif, anomalies = qualifier(d)
        regimes[d.cle] = r
        motivations[d.cle] = motif
        alertes += anomalies
        print("  %-14s %-12s %3d %3d %5.2f %5.2f  %-20s %s"
              % (d.cle, d.domaine, d.gravite, d.etendue, d.plausibilite,
                 d.incertitude, r, REGIMES[r][0] or "—"))
    print("")
    print("  ET CHAQUE QUALIFICATION EST MOTIVÉE — point 3 :")
    for cle in ("stockage-geo", "pesticide", "barrage"):
        print("    %-14s %s" % (cle, motivations[cle]))
    determines = len([r for r in regimes.values() if r != "non_determine"])
    print("")
    print("  DÉTERMINÉS PAR LA GRILLE : %d dossiers sur %d."
          % (determines, len(DOSSIERS)))
    return regimes, motivations, alertes


def ce_que_l_horizon_decide():
    titre("CE QUI RESTE — L'HORIZON SECTORIEL DÉCIDE, ET LA GRILLE SE TAIT")
    d = [x for x in DOSSIERS if x.cle == "stockage-geo"][0]
    print("  %s, domaine « %s ». Réversible à cinquante ans, irréversible à"
          % (d.libelle, d.domaine))
    print("  l'échelle humaine. LA GRILLE TRANCHE : horizon « %s »."
          % GRILLE["horizons"][d.domaine])
    print("")
    print("  %-22s %-22s %s" % ("horizon retenu", "régime", "charge"))
    for horizon in HORIZONS:
        g = dict(GRILLE)
        g["horizons"] = dict(GRILLE["horizons"])
        g["horizons"][d.domaine] = horizon
        r, _, _ = qualifier(d, g)
        print("  %-22s %-22s %s" % (horizon, r, REGIMES[r][0] or "—"))
    print("")
    print("  LA VERSION 1 LAISSAIT CE CHOIX À QUI QUALIFIAIT — c'était le trou.")
    print("  LA VERSION 2 LE PORTE DANS LA GRILLE, fixée d'avance et par une")
    print("  autre autorité. LE TROU EST DÉPLACÉ, ET C'EST UN PROGRÈS RÉEL :")
    print("  il devient une décision publique, motivée et attaquable, au lieu")
    print("  d'un arbitrage de dossier.")
    print("")
    manquants = sorted(set(x.domaine for x in DOSSIERS
                           if x.domaine not in GRILLE["horizons"]))
    print("  MAIS IL NE DISPARAÎT PAS TANT QUE LA GRILLE EST INCOMPLÈTE. La")
    print("  grille de référence couvre %d domaines sur %d, et %d dossiers"
          % (len(GRILLE["horizons"]), len(set(x.domaine for x in DOSSIERS)),
             len([x for x in DOSSIERS
                  if x.domaine not in GRILLE["horizons"]])))
    print("  restent non déterminés faute d'horizon : %s."
          % ", ".join(manquants))
    print("")
    print("  ET CE CHIFFRE EST UN PARAMÈTRE, NON UN RÉSULTAT. C'est moi qui ai")
    print("  choisi une grille incomplète, pour mesurer ce qu'elle coûte. La")
    print("  doctrine n'impose aucune incomplétude — elle exige au contraire")
    print("  que les horizons soient fixés. CE QUE LE PROGRAMME ÉTABLIT EST")
    print("  PLUS ÉTROIT : la détermination de la qualification vaut")
    print("  exactement la complétude de la grille, ni plus ni moins.")
    print("")
    print("  L'AUTEUR NOMME PRÉCISÉMENT CETTE PIÈCE : « les horizons")
    print("  sectoriels et leurs méthodes de calibration » restent ouverts.")
    return manquants


def l_incertitude_n_emporte_rien():
    titre("CE QUI RESTE — L'INCERTITUDE EST ÉVALUÉE, ET N'EMPORTE RIEN")
    d = [x for x in DOSSIERS if x.cle == "stockage-geo"][0]
    print("  Le point 1 évalue l'incertitude SÉPARÉMENT de la plausibilité, et")
    print("  la distinction est juste : une plausibilité de 0.50 bien établie")
    print("  n'est pas une plausibilité de 0.50 tirée de rien.")
    print("")
    print("  %-28s %6s %6s  %s" % ("dossier", "plaus", "incer", "régime"))
    resultats = {}
    for incertitude, etiquette in ((0.10, "bien étudié"), (0.90, "sans données")):
        jumeau = Dossier(d.cle, d.libelle, d.domaine, d.gravite, d.etendue,
                         d.plausibilite, d.reversible_sur, incertitude)
        r, _, _ = qualifier(jumeau)
        resultats[etiquette] = r
        print("  %-28s %6.2f %6.2f  %s"
              % ("stockage-geo, " + etiquette, d.plausibilite, incertitude, r))
    print("")
    identiques = len(set(resultats.values())) == 1
    if identiques:
        print("  MÊME RÉGIME, MÊME CHARGE DE LA PREUVE. L'incertitude est")
        print("  évaluée, publiée — et sans effet. LA GRILLE NE DIT PAS CE")
        print("  QU'ELLE EMPORTE, et évaluer une dimension sans dire ce qu'elle")
        print("  emporte ne change aucune décision.")
    print("")
    print("  CE QUE LA VERSION 1 PRÉVOYAIT ET QUE LA VERSION 2 NE REPREND PAS :")
    print("  « incertitude importante portant sur un dommage potentiellement")
    print("  irréversible : suspension provisoire et ACQUISITION DE")
    print("  CONNAISSANCES ». C'était la conséquence naturelle de la dimension.")
    print("  IL FAUT DIRE SI ELLE EST MAINTENUE — le programme ne la remet pas")
    print("  de lui-même, parce que légiférer à la place de l'auteur serait la")
    print("  faute symétrique de celle qu'on lui reproche d'avoir corrigée.")
    return identiques


def zone_intermediaire(regimes):
    titre("CE QUI RESTE — DEUX CAUSES DISTINCTES, ET IL FAUT LES SÉPARER")
    print("  La version 2 dit « charge de la preuve ADAPTÉE À LA NATURE DU")
    print("  RISQUE » — plus général que les deux pôles de la version 1, et")
    print("  compatible avec une gradation. MAIS LA GRADATION N'EST PAS DITE.")
    print("")
    complete = grille_complete()
    lignes = []
    for d in DOSSIERS:
        r_ref = qualifier(d)[0]
        r_com, motif, _ = qualifier(d, complete)
        lignes.append((d.cle, r_ref, r_com, motif))
    print("  %-14s %-20s %-20s" % ("dossier", "grille de référence",
                                   "grille COMPLÈTE"))
    for cle, a, b, _ in lignes:
        print("  %-14s %-20s %-20s" % (cle, a, b))

    determines_ref = len([x for x in lignes if x[1] != "non_determine"])
    determines_com = len([x for x in lignes if x[2] != "non_determine"])
    hors = [x for x in lignes if x[2] == "non_determine"]
    print("")
    print("  DÉTERMINÉS : %d sur %d avec la grille de référence, %d sur %d"
          % (determines_ref, len(DOSSIERS), determines_com, len(DOSSIERS)))
    print("  avec une grille complète.")
    print("")
    print("  LES DEUX CAUSES SONT DONC SÉPARÉES, ET C'EST NÉCESSAIRE : la")
    print("  première est un PARAMÈTRE de ce programme — j'ai choisi une")
    print("  grille couvrant deux domaines sur six — et elle ne prouve rien")
    print("  sur la doctrine. LA SECONDE EST UNE PROPRIÉTÉ DE LA DOCTRINE :")
    print("  même avec une grille COMPLÈTE, %d dossiers restent sans charge"
          % len(hors))
    print("  attribuée.")
    print("")
    for cle, _, _, motif in hors:
        print("    %-14s %s" % (cle, motif))
    print("")
    print("  Ce sont les cas ordinaires : GRAVE MAIS RÉVERSIBLE d'un côté,")
    print("  IRRÉVERSIBLE MAIS PEU PLAUSIBLE de l'autre. Les deux pôles de la")
    print("  doctrine ne partitionnent pas l'espace des risques, et « adaptée")
    print("  à la nature du risque » ne dit pas encore comment graduer entre")
    print("  eux.")
    return [x[0] for x in hors]


def le_point_des_seuils():
    titre("CE QUI TIENT — LES SEUILS FIXÉS D'AVANCE")
    plaus = sorted(x.plausibilite for x in DOSSIERS)
    print("  Plausibilités des six dossiers : %s"
          % ", ".join("%.2f" % p for p in plaus))
    print("")
    print("  %-36s %8s %12s" % ("seuil", "valeur", "au porteur"))
    resultats = {}
    for etiquette, seuil in (
            ("fixé d'avance par l'instance démocratique",
             GRILLE["seuil_plausibilite"]),
            ("choisi après lecture, pour admettre", max(plaus) + 0.01),
            ("choisi après lecture, pour refuser", min(plaus) - 0.01)):
        g = dict(GRILLE)
        g["seuil_plausibilite"] = seuil
        n = len([x for x in DOSSIERS
                 if qualifier(x, g)[0] == "grave_irreversible"])
        resultats[etiquette] = n
        print("  %-36s %8.2f %12d" % (etiquette, seuil, n))
    print("")
    print("  LES TROIS SEUILS SONT DANS LA MÊME PLAGE DE VALEURS PLAUSIBLES, et")
    print("  rien dans le dossier ne distingue un seuil de principe d'un seuil")
    print("  taillé sur mesure. LE FIXER D'AVANCE EST CE QUI EN FAIT UNE")
    print("  CONTRAINTE PLUTÔT QU'UNE DESCRIPTION.")
    print("")
    print("  ET LA VERSION 2 AJOUTE QUI LE FIXE : l'AUTORITÉ DÉMOCRATIQUE,")
    print("  APRÈS EXPERTISE PLURALISTE. Ce n'est pas un détail — cela répartit")
    print("  la décision normative et la compétence technique conformément à")
    print("  A46, au lieu de les confondre dans un même organe.")
    print("")
    print("  RESTE la révision : « procédure publique » est acquise ; que la")
    print("  révision ne s'applique pas au dossier en cours ne l'est pas.")
    return resultats


def publicite():
    titre("CE QUI TIENT — POINTS 8 ET 9")
    complet = dict((c, True) for c in PUBLICATION)
    complet["cle"] = "barrage"
    partiel = dict(complet, cle="barrage-bis", incertitudes=False,
                   avis_minoritaires=False)
    print("  Cinq publications exigées : %s." % ", ".join(PUBLICATION))
    print("  dossier complet : %s"
          % (controler_publication(complet) or "aucune anomalie"))
    for a in controler_publication(partiel):
        print("    %s" % a)
    print("")
    print("  SANS LES INCERTITUDES PUBLIÉES, le point 1 est décoratif : on")
    print("  évalue une dimension qu'on ne montre pas. SANS LES AVIS")
    print("  MINORITAIRES, la divergence entre experts disparaît du dossier —")
    print("  et c'est elle qui, dans la règle d'émission, sert d'alarme.")
    print("")
    print("  LE POINT 9 EST TENU PAR LE CORPUS, et il a été acquis contre")
    print("  lui-même : la simulation de la règle d'émission donnait au recours")
    print("  la VALEUR VRAIE par construction. Le contrôle de méthode qui")
    print("  l'interdit est en place. Et le mot est corrigé : CANAL DE MESURE")
    print("  INDÉPENDANT, non observation directe de la vérité.")
    return len(controler_publication(partiel))


def main():
    print("=" * 78)
    print("A47 — DÉCIDER SOUS INCERTITUDE. VERSION 2, VALIDÉE PAR L'AUTEUR")
    print("=" * 78)
    print("Précaution proportionnée. La doctrine n'arrête AUCUN SEUIL")
    print("NUMÉRIQUE : elle répartit la CHARGE DE LA PREUVE et fixe QUI établit")
    print("les seuils, QUAND et SELON QUELLE PROCÉDURE.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ ICI. Les dossiers sont fictifs.")

    grille = la_grille()
    regimes, motivations, alertes = application()
    manquants = ce_que_l_horizon_decide()
    incertitude = l_incertitude_n_emporte_rien()
    hors = zone_intermediaire(regimes)
    seuils = le_point_des_seuils()
    manques = publicite()

    titre("CE QUE LA VERSION 2 FERME, ET CE QU'ELLE LAISSE")
    print("  FERMÉ — LE PREMIER TROU DE LA VERSION 1. « La doctrine répartit la")
    print("  charge après une classification dont elle ne règle ni l'auteur ni")
    print("  la procédure » : la version 2 règle les deux. LA GRILLE EST FIXÉE")
    print("  D'AVANCE PAR L'AUTORITÉ DÉMOCRATIQUE APRÈS EXPERTISE PLURALISTE,")
    print("  ET LA QUALIFICATION L'APPLIQUE EN SE MOTIVANT. Le choix d'horizon")
    print("  devient une décision publique et attaquable au lieu d'un arbitrage")
    print("  de dossier — et c'est un progrès réel, non une reformulation.")
    print("")
    print("  RESTE 1 — À CONSTRUIRE, ET L'AUTEUR L'A NOMMÉ. La détermination")
    print("  de la qualification vaut EXACTEMENT la complétude de la grille :")
    print("  %d dossiers déterminés sur %d avec une grille couvrant %d domaines"
          % (len([r for r in regimes.values() if r != "non_determine"]),
             len(DOSSIERS), len(GRILLE["horizons"])))
    print("  sur %d, %d sur %d avec une grille complète. LE PREMIER CHIFFRE EST"
          % (len(set(d.domaine for d in DOSSIERS)),
             len([d for d in DOSSIERS
                  if qualifier(d, grille_complete())[0] != "non_determine"]),
             len(DOSSIERS)))
    print("  UN PARAMÈTRE DE CE PROGRAMME, non un défaut de la doctrine : les")
    print("  horizons sectoriels et leurs méthodes de calibration sont une")
    print("  pièce à construire, et elle est ouverte.")
    print("")
    print("  RESTE 2 — À TRANCHER. L'INCERTITUDE N'EMPORTE RIEN. Elle est")
    print("  évaluée séparément, publiée, et deux dossiers identiques hormis")
    print("  leur état de connaissance reçoivent LE MÊME RÉGIME. La version 1")
    print("  prévoyait la suspension provisoire et l'acquisition de")
    print("  connaissances ; la version 2 ne la reprend pas. IL FAUT DIRE SI")
    print("  ELLE EST MAINTENUE — le programme ne la remet pas de lui-même.")
    print("")
    print("  RESTE 3 — À TRANCHER AUSSI, ET C'EST UNE PROPRIÉTÉ DE LA")
    print("  DOCTRINE, non un paramètre : MÊME AVEC UNE GRILLE COMPLÈTE, %d"
          % len(hors))
    print("  dossiers sur %d restent sans charge attribuée — grave mais"
          % len(DOSSIERS))
    print("  réversible, irréversible mais peu plausible. « Adaptée à la")
    print("  nature du risque » est compatible avec une gradation, MAIS LA")
    print("  GRADATION N'EST PAS DITE.")
    print("")
    print("  CE QUE CE PROGRAMME NE DIT PAS. Il ne dit pas que la doctrine est")
    print("  bonne : aucun seuil n'est éprouvé, aucun dossier n'est réel, et un")
    print("  programme qui applique une règle ne la valide jamais. Il dit où")
    print("  elle décide et où elle se tait, et c'est tout.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
