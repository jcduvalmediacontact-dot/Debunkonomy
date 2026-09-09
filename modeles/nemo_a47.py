#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A47 — DÉCIDER SOUS INCERTITUDE. DOCTRINE VALIDÉE PAR L'AUTEUR, 2026-09-09.

DEUX DES TROIS « RESTES » QUE CE PROGRAMME PUBLIAIT ÉTAIENT DES LECTURES
FAUTIVES DE LA RÈGLE, NON DES LACUNES DE LA RÈGLE. L'auteur les a redressées
le même jour, et la correction porte sur l'implémentation.

  (A) LA ZONE INTERMÉDIAIRE EST COUVERTE. « Zone intermédiaire : charge
      partagée, autorisation limitée par tranches, surveillance et capacité
      d'arrêt. » — clause explicitée par l'auteur le 2026-09-09. « Grave mais
      réversible » et « irréversible mais peu plausible » y appartiennent
      précisément. Le programme les rendait « sans charge attribuée » : c'était
      un défaut de traduction de la règle. AUCUN DOSSIER NE DOIT RESTER SANS
      RÉGIME, et un contrôle le vérifie désormais.

  (B) L'INCERTITUDE N'A VOLONTAIREMENT PAS D'EFFET AUTOMATIQUE SUR LE RÉGIME.
      Deux dossiers peuvent recevoir le même régime de risque avec des états de
      connaissance différents — c'est voulu. CE QUI DOIT DIFFÉRER EST LEUR
      PROCÉDURE D'INSTRUCTION. Le programme concluait « l'incertitude n'emporte
      rien » : il regardait le régime, là où la règle agit sur la procédure.

  (C) ET IL FAUT SÉPARER TROIS VARIABLES QUE CE PROGRAMME CONFONDAIT ENCORE
      DANS UN SEUL NOMBRE : la PROBABILITÉ estimée du dommage, la CONFIANCE
      accordée à cette estimation, et la POSSIBILITÉ DE RÉDUIRE l'incertitude
      dans un délai utile. Une probabilité de 0,10 fondée sur de bonnes données
      n'est pas une probabilité de 0,10 très incertaine.

RESTE OUVERT, ET C'EST LA SEULE PIÈCE : les horizons et seuils sectoriels, à
fixer par domaine selon la procédure d'A47, sans rouvrir son principe.

CE QUE LE PROGRAMME VÉRIFIE DÉSORMAIS, ET C'EST LA COMMANDE DE L'AUTEUR :
  — une grille complète attribue un régime à CHAQUE dossier ;
  — deux dossiers de MÊME RISQUE mais de qualités de connaissance différentes
    reçoivent, si nécessaire, des PROCÉDURES D'INSTRUCTION différentes.

AUCUN SEUIL N'EST CALIBRÉ. Les dossiers sont fictifs, et un programme qui
applique une règle ne la valide jamais.

USAGE :  python modeles/nemo_a47.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False


# =====================================================================
# LES DIMENSIONS — ET TROIS D'ENTRE ELLES NE SE CONFONDENT PAS
# =====================================================================
DIMENSIONS = ("gravite", "etendue", "plausibilite", "reversibilite",
              "confiance", "reductibilite", "delai_acquisition")


class Dossier(object):
    """TROIS VARIABLES DISTINCTES, ET C'EST LA CORRECTION DE L'AUTEUR.

    « plausibilite » est la PROBABILITÉ ESTIMÉE du dommage.
    « confiance » est le CRÉDIT accordé à cette estimation.
    « reductible » et « delai_acquisition » disent si l'incertitude peut être
    réduite, ET DANS QUEL DÉLAI.

    Une probabilité de 0,10 très bien établie et une probabilité de 0,10 tirée
    de rien ne sont pas la même chose. UN SEUL NOMBRE ENTRE 0 ET 1 NE PEUT PAS
    PORTER LES TROIS.
    """

    def __init__(self, cle, libelle, domaine, gravite, etendue, plausibilite,
                 reversible_sur, confiance, reductible, delai_acquisition,
                 urgence=False, essentiel=False, impossible=False):
        self.cle = cle
        self.libelle = libelle
        self.domaine = domaine
        self.gravite = gravite
        self.etendue = etendue
        self.plausibilite = plausibilite
        self.reversible_sur = dict(reversible_sur)
        self.confiance = confiance
        self.reductible = reductible
        self.delai_acquisition = delai_acquisition
        self.urgence = urgence
        self.essentiel = essentiel
        self.impossible = impossible


HORIZONS = ("cinquante ans", "échelle humaine")

DOSSIERS = [
    Dossier("renovation", "Rénovation thermique", "batiment", 1, 1, 0.20,
            {"cinquante ans": True, "échelle humaine": True},
            confiance=0.85, reductible=False, delai_acquisition=0),
    Dossier("stockage-geo", "Stockage géologique de CO2", "energie", 2, 2,
            0.50, {"cinquante ans": True, "échelle humaine": False},
            confiance=0.55, reductible=True, delai_acquisition=3),
    Dossier("barrage", "Grand barrage en zone habitée", "eau", 3, 3, 0.70,
            {"cinquante ans": False, "échelle humaine": False},
            confiance=0.80, reductible=False, delai_acquisition=0),
    Dossier("pesticide", "Pesticide à large spectre", "agriculture", 2, 3,
            0.60, {"cinquante ans": True, "échelle humaine": True},
            confiance=0.70, reductible=True, delai_acquisition=8),
    Dossier("mine-lithium", "Mine de lithium", "mines", 2, 1, 0.30,
            {"cinquante ans": False, "échelle humaine": False},
            confiance=0.60, reductible=True, delai_acquisition=6),
    Dossier("capteur", "Réseau de capteurs urbains", "numerique", 1, 1, 0.30,
            {"cinquante ans": True, "échelle humaine": True},
            confiance=0.60, reductible=True, delai_acquisition=9),
    Dossier("medicament", "Traitement essentiel en épidémie", "sante", 3, 0,
            0.55, {"cinquante ans": False, "échelle humaine": False},
            confiance=0.45, reductible=True, delai_acquisition=2,
            urgence=True, essentiel=True),
]


# =====================================================================
# LA GRILLE — FIXÉE D'AVANCE, PAR UNE AUTRE AUTORITÉ QUE CELLE QUI L'APPLIQUE
# =====================================================================
GRILLE = {
    "fixee_par": "instance-democratique",
    "apres": "expertise pluraliste",
    "publiee": "avant l'examen des dossiers",
    "seuil_plausibilite": 0.50,
    "gravite_serieuse": 2,
    "etendue_limitee": 2,
    "seuil_confiance": 0.75,      # au-delà, l'information est dite robuste
    "delai_utile": 4,             # au-delà, l'acquisition n'arrive pas à temps
    # LES HORIZONS SECTORIELS — LA SEULE PIÈCE RÉELLEMENT OUVERTE. La grille de
    # référence est délibérément incomplète : le programme mesure ce que coûte
    # une grille lacunaire, et c'est un PARAMÈTRE, non un résultat.
    "horizons": {"energie": "échelle humaine",
                 "agriculture": "cinquante ans"},
}


def grille_complete(horizon="échelle humaine"):
    g = dict(GRILLE)
    g["horizons"] = dict((d.domaine, horizon) for d in DOSSIERS)
    return g


# =====================================================================
# LES RÉGIMES — ET ILS COUVRENT TOUT L'ESPACE
# =====================================================================
CHARGE_PARTAGEE = (
    ("porteur", "documente les risques, les alternatives et les mesures de "
                "réduction"),
    ("autorité", "apporte ses propres éléments et justifie la "
                 "proportionnalité de toute restriction"),
    ("expertise indépendante", "recherche les données manquantes"),
    ("autorisation", "limitée par tranches, surveillée et révocable"),
)

# LE RÉGIME PAR DÉFAUT — une grille lacunaire n'ouvre AUCUN droit nouveau.
# Sans cela, une autorité éviterait les règles en ne construisant jamais la
# grille : le dossier passerait en zone intermédiaire et obtiendrait
# l'autorisation par tranches. LA LACUNE NE DOIT PROFITER À PERSONNE.
INTERDIT_SI_INCOMPLETE = (
    "toute ÉMISSION COMPLÈTE",
    "toute ACTION IRRÉVERSIBLE",
)
AUTORISE_SI_INCOMPLETE = (
    "le financement des ÉTUDES et des MESURES nécessaires",
    "les OPÉRATIONS PRÉPARATOIRES RÉVERSIBLES",
    "pour un besoin essentiel urgent, l'INTERVENTION MINIMALE ET TEMPORAIRE",
)
OBLIGE_SI_INCOMPLETE = (
    "compléter la grille dans un DÉLAI PUBLIC",
    "CONTRÔLE INDÉPENDANT en cas de retard",
)

REGIMES = {
    "impossible": ("—", "refus : impossibilité matérielle"),
    "qualification_incomplete": (
        "instruction suspendue",
        "ni émission complète ni action irréversible ; études, mesures et "
        "préparatoires réversibles admises ; délai public et contrôle du "
        "retard"),
    "grave_irreversible": ("porteur",
                           "établir une compatibilité suffisante"),
    "limite_reversible": ("autorité",
                          "motiver tout refus ; autorisation progressive"),
    "intermediaire": ("partagée",
                      "charge partagée ; autorisation limitée par tranches, "
                      "surveillance et capacité d'arrêt"),
    "urgence_essentielle": ("décision provisoire",
                            "protection particulière : solution la moins "
                            "risquée, quantité minimale, réexamen rapide"),
}


def qualifier(d, grille=None):
    """Rend (regime, motivation, anomalies).

    L'ORDRE DES TESTS EST CELUI DE LA RÈGLE, et le dernier est un RÉSIDU
    EXHAUSTIF : tout dossier qui ne relève ni de l'impossibilité, ni du risque
    plausible grave et irréversible, ni du risque limité et réversible entre
    dans la ZONE INTERMÉDIAIRE. AUCUN DOSSIER NE RESTE SANS RÉGIME.
    """
    g = GRILLE if grille is None else grille
    anomalies = []

    if d.impossible:
        return "impossible", "impossibilité matérielle", anomalies
    if d.urgence and d.essentiel:
        return ("urgence_essentielle",
                "besoin essentiel urgent — protection particulière", anomalies)

    horizon = g["horizons"].get(d.domaine)
    if horizon is None:
        anomalies.append(
            "[Q2] %s : la grille ne fixe aucun HORIZON pour le domaine « %s » "
            "— la réversibilité n'est pas qualifiable (%s)"
            % (d.cle, d.domaine,
               " / ".join("%s : %s" % (h, "réversible" if v else "irréversible")
                          for h, v in sorted(d.reversible_sur.items()))))
        # UNE GRILLE LACUNAIRE N'EST PAS UN RISQUE INTERMÉDIAIRE. Le risque
        # intermédiaire suppose un dossier ÉVALUÉ ; ici la qualification n'a
        # pas pu être achevée. Les confondre ouvrirait une échappatoire :
        # ne jamais construire la grille pour obtenir l'autorisation par
        # tranches.
        return ("qualification_incomplete",
                "horizon sectoriel non fixé : la qualification n'est pas "
                "achevée, elle n'est pas intermédiaire",
                anomalies)

    reversible = d.reversible_sur[horizon]
    if (d.plausibilite >= g["seuil_plausibilite"]
            and d.gravite >= g["gravite_serieuse"] and not reversible):
        return ("grave_irreversible",
                "plausibilité %.2f ≥ %.2f, gravité %d ≥ %d, irréversible à "
                "l'horizon « %s »" % (d.plausibilite, g["seuil_plausibilite"],
                                      d.gravite, g["gravite_serieuse"],
                                      horizon), anomalies)
    if (reversible and d.gravite <= g["gravite_serieuse"]
            and d.etendue <= g["etendue_limitee"]):
        return ("limite_reversible",
                "réversible à l'horizon « %s », gravité %d ≤ %d, étendue %d ≤ "
                "%d" % (horizon, d.gravite, g["gravite_serieuse"], d.etendue,
                        g["etendue_limitee"]), anomalies)
    return ("intermediaire",
            "ni impossible, ni grave et irréversible, ni limité et "
            "réversible : gravité %d, étendue %d, %s à l'horizon « %s », "
            "plausibilité %.2f"
            % (d.gravite, d.etendue,
               "réversible" if reversible else "irréversible", horizon,
               d.plausibilite), anomalies)


# =====================================================================
# LA PROCÉDURE D'INSTRUCTION — C'EST LÀ QUE L'INCERTITUDE AGIT
# =====================================================================
INSTRUCTIONS = {
    "acquisition": "acquisition de données AVANT décision complète",
    "precaution": "décision avec MARGE DE PRÉCAUTION explicitée, réexamen "
                  "ouvert dès que les connaissances arrivent",
    "urgence": "autorisation minimale et temporaire PENDANT l'instruction",
    "directe": "application directe de la grille",
    "residuelle": "application de la grille, la confiance étant publiée avec "
                  "la décision",
}


def instruire(d, grille=None):
    """Rend (instruction, motivation). LE RÉGIME DIT QUI PORTE LA CHARGE ; LA
    PROCÉDURE DIT COMMENT ON INSTRUIT. Les deux sont séparés, et c'est
    précisément par la seconde que l'incertitude agit.

    UNE LECTURE EST FAITE ICI, ET ELLE EST SIGNALÉE, dans la formulation
    arrêtée par l'auteur : une incertitude réductible hors du délai utile est
    traitée comme NON RÉDUCTIBLE POUR LA DÉCISION PRÉSENTE, SANS ÊTRE DÉCLARÉE
    DÉFINITIVEMENT IRRÉDUCTIBLE. La nuance n'est pas verbale : elle laisse le
    RÉEXAMEN ouvert dès que les connaissances deviennent disponibles, là où
    « irréductible » aurait clos la question. Le qualificatif « dans un délai
    utile » n'aurait sinon aucun effet — un délai de 99 périodes vaudrait un
    délai de 1. Ce n'est pas une règle ajoutée, c'est la lecture de celle qui
    existe, et elle est écrite ici pour pouvoir être contestée.
    """
    g = GRILLE if grille is None else grille
    if d.urgence and d.essentiel:
        return "urgence", "besoin essentiel urgent"
    if d.reductible and d.delai_acquisition <= g["delai_utile"]:
        return ("acquisition",
                "incertitude RÉDUCTIBLE dans le délai utile (%d ≤ %d)"
                % (d.delai_acquisition, g["delai_utile"]))
    if d.confiance >= g["seuil_confiance"]:
        return ("directe", "information robuste : confiance %.2f ≥ %.2f"
                % (d.confiance, g["seuil_confiance"]))
    if d.gravite >= g["gravite_serieuse"]:
        return ("precaution",
                "incertitude NON RÉDUCTIBLE POUR LA DÉCISION PRÉSENTE (%s), "
                "sans être définitivement irréductible — RÉEXAMEN OUVERT ; "
                "dommage potentiellement grave (gravité %d)"
                % ("non réductible" if not d.reductible
                   else "délai %d > %d" % (d.delai_acquisition,
                                           g["delai_utile"]), d.gravite))
    return ("residuelle",
            "ni réductible à temps, ni robuste, ni potentiellement grave : "
            "confiance %.2f publiée avec la décision" % d.confiance)


# =====================================================================
# LES CONTRÔLES
# =====================================================================
PUBLICATION = ("donnees", "methodes", "incertitudes", "seuil_normatif",
               "avis_minoritaires")


def controler_publication(decision):
    return ["[P1] %s : « %s » n'est pas publié" % (decision.get("cle"), champ)
            for champ in PUBLICATION if not decision.get(champ)]


def controler_exhaustivite(grille=None):
    """R1 — AUCUN DOSSIER SANS RÉGIME, et R2 — AUCUNE LACUNE PROFITABLE.

    R1 vérifie que tout dossier reçoit un régime. R2 vérifie qu'un dossier dont
    la qualification n'a PAS pu être achevée ne reçoit PAS le régime des
    dossiers évalués : sans quoi ne jamais construire la grille deviendrait un
    moyen d'obtenir l'autorisation par tranches.
    """
    anomalies = []
    for d in DOSSIERS:
        regime, _, _ = qualifier(d, grille)
        if regime not in REGIMES:
            anomalies.append("[R1] %s : régime « %s » inconnu"
                             % (d.cle, regime))
            continue
        if REGIMES[regime][0] is None:
            anomalies.append("[R1] %s : aucun régime attribué" % d.cle)
        g = GRILLE if grille is None else grille
        if d.domaine not in g.get("horizons", {}) \
                and regime not in ("qualification_incomplete", "impossible",
                                   "urgence_essentielle"):
            anomalies.append(
                "[R2] %s : horizon absent et pourtant qualifié « %s » — la "
                "lacune de grille ne doit ouvrir aucun droit" % (d.cle, regime))
    return anomalies


def controler_grille(grille=None):
    g = GRILLE if grille is None else grille
    anomalies = []
    if g.get("publiee") != "avant l'examen des dossiers":
        anomalies.append("[Q1] la grille n'est pas publiée avant l'examen")
    if g.get("fixee_par") == "autorite-de-qualification":
        anomalies.append(
            "[Q4] la grille est fixée par l'autorité qui l'applique — A46")
    manquants = sorted(set(d.domaine for d in DOSSIERS
                           if d.domaine not in g.get("horizons", {})))
    if manquants:
        anomalies.append(
            "[Q2] aucun horizon sectoriel pour %d domaine(s) sur %d : %s"
            % (len(manquants), len(set(d.domaine for d in DOSSIERS)),
               ", ".join(manquants)))
    return anomalies


# =====================================================================
def titre(libelle):
    print("")
    print("=" * 78)
    print(libelle)
    print("=" * 78)


def la_grille():
    titre("LA GRILLE — FIXÉE D'AVANCE, ET PAR UNE AUTRE AUTORITÉ")
    for champ in ("fixee_par", "apres", "publiee"):
        print("  %-18s %s" % (champ, GRILLE[champ]))
    print("  %-18s plausibilité %.2f, gravité sérieuse %d, étendue limitée %d"
          % ("seuils de risque", GRILLE["seuil_plausibilite"],
             GRILLE["gravite_serieuse"], GRILLE["etendue_limitee"]))
    print("  %-18s confiance robuste %.2f, délai utile %d périodes"
          % ("seuils de savoir", GRILLE["seuil_confiance"],
             GRILLE["delai_utile"]))
    print("  %-18s %s" % ("horizons",
                          ", ".join("%s : %s" % (k, v) for k, v
                                    in sorted(GRILLE["horizons"].items()))))
    print("")
    for a in controler_grille():
        print("    %s" % a)
    print("")
    print("  LA SEULE PIÈCE OUVERTE EST LÀ : les horizons et seuils sectoriels,")
    print("  à fixer par domaine selon la procédure d'A47, sans rouvrir son")
    print("  principe. Le reste de la grille est arrêté.")
    return controler_grille()


def les_trois_variables():
    titre("LA CORRECTION — TROIS VARIABLES, ET NON UN SEUL NOMBRE")
    print("  La version précédente portait la plausibilité ET l'incertitude")
    print("  dans deux nombres entre 0 et 1, ce qui confondait encore la")
    print("  PROBABILITÉ du dommage, la CONFIANCE dans cette estimation et la")
    print("  POSSIBILITÉ DE RÉDUIRE l'incertitude à temps.")
    print("")
    print("  %-14s %6s %6s %11s %7s" % ("dossier", "proba", "confi",
                                        "réductible", "délai"))
    for d in DOSSIERS:
        print("  %-14s %6.2f %6.2f %11s %7s"
              % (d.cle, d.plausibilite, d.confiance,
                 "oui" if d.reductible else "non",
                 d.delai_acquisition if d.reductible else "—"))
    print("")
    print("  UNE PROBABILITÉ DE 0,30 BIEN ÉTABLIE N'EST PAS UNE PROBABILITÉ DE")
    print("  0,30 TIRÉE DE RIEN, et la mine de lithium comme le réseau de")
    print("  capteurs le montrent : même probabilité, même confiance, mais des")
    print("  gravités et des délais différents — donc des instructions")
    print("  différentes.")


def application(grille=None, etiquette="grille de référence"):
    titre("LA DOCTRINE APPLIQUÉE — RÉGIME ET PROCÉDURE, SÉPARÉMENT (%s)"
          % etiquette)
    print("  %-14s %-20s %-12s %s"
          % ("dossier", "régime", "charge", "procédure d'instruction"))
    resultats = {}
    for d in DOSSIERS:
        regime, motif, _ = qualifier(d, grille)
        proc, raison = instruire(d, grille)
        resultats[d.cle] = (regime, proc, motif, raison)
        print("  %-14s %-20s %-12s %s"
              % (d.cle, regime, REGIMES[regime][0], INSTRUCTIONS[proc]))
    return resultats


def exhaustivite():
    titre("PREMIÈRE PROPRIÉTÉ — AUCUN DOSSIER ÉVALUÉ SANS RÉGIME")
    complete = grille_complete()
    anomalies = controler_exhaustivite(complete)
    regimes = {}
    for d in DOSSIERS:
        r, _, _ = qualifier(d, complete)
        regimes[r] = regimes.get(r, 0) + 1
    print("  Avec une grille COMPLÈTE, sur %d dossiers :" % len(DOSSIERS))
    for r in sorted(regimes):
        print("    %-26s %d — charge : %s" % (r, regimes[r], REGIMES[r][0]))
    print("")
    print("  contrôles R1 et R2 : %s" % (anomalies or "aucune anomalie"))
    print("")
    print("  LA ZONE INTERMÉDIAIRE ÉTAIT PRÉVUE PAR LA RÈGLE, et le programme")
    print("  la rendait vide : « grave mais réversible » et « irréversible mais")
    print("  peu plausible » y appartiennent. Corrigé.")
    print("")
    print("  ET LA CHARGE PARTAGÉE N'EST PAS UN MOT :")
    for qui, quoi in CHARGE_PARTAGEE:
        print("    %-24s %s" % (qui, quoi))
    return anomalies, regimes


def la_lacune_ne_profite_a_personne():
    titre("DEUXIÈME PROPRIÉTÉ — UNE GRILLE LACUNAIRE N'OUVRE AUCUN DROIT")
    print("  UNE GRILLE LACUNAIRE N'EST PAS UN RISQUE INTERMÉDIAIRE, et les")
    print("  confondre ouvrirait une échappatoire : une autorité éviterait les")
    print("  règles EN NE CONSTRUISANT JAMAIS LA GRILLE.")
    print("")
    print("    RISQUE INTERMÉDIAIRE     dossier ÉVALUÉ dont les")
    print("                             caractéristiques se situent entre les")
    print("                             catégories extrêmes")
    print("    QUALIFICATION INCOMPLÈTE horizon, seuil ou donnée indispensable")
    print("                             ABSENT — la qualification n'a pas pu")
    print("                             être achevée")
    print("")
    complete = grille_complete()
    sans = [d for d in DOSSIERS if d.domaine not in GRILLE["horizons"]]
    print("  %d dossiers sur %d n'ont pas d'horizon dans la grille de"
          % (len(sans), len(DOSSIERS)))
    print("  référence. CE QU'ILS OBTIENNENT, SELON QUE LA GRILLE EST FAITE OU")
    print("  NON :")
    print("")
    print("  %-14s %-26s %-26s" % ("dossier", "grille lacunaire",
                                   "grille complète"))
    gagnants = 0
    for d in sans:
        a, _, _ = qualifier(d)
        b, _, _ = qualifier(d, complete)
        if a == b:
            note = ""
        elif a == "qualification_incomplete":
            note = ""
        else:
            note = "  ← la lacune a profité"
            gagnants += 1
        print("  %-14s %-26s %-26s%s" % (d.cle, a, b, note))
    print("")
    print("  CE QUE LE RÉGIME PAR DÉFAUT INTERDIT :")
    for x in INTERDIT_SI_INCOMPLETE:
        print("    — %s" % x)
    print("  CE QU'IL AUTORISE :")
    for x in AUTORISE_SI_INCOMPLETE:
        print("    — %s" % x)
    print("  CE QU'IL OBLIGE :")
    for x in OBLIGE_SI_INCOMPLETE:
        print("    — %s" % x)
    print("")
    print("  LA LACUNE NE PROFITE À PERSONNE, ET C'EST LA PROPRIÉTÉ QUI COMPTE.")
    print("  AU PORTEUR : aucune émission complète, aucune action")
    print("  irréversible — moins que sous tout régime évalué, y compris")
    print("  l'intermédiaire, qui autorise le projet PAR TRANCHES.")
    print("  À L'AUTORITÉ : un délai public pour compléter la grille, et un")
    print("  contrôle indépendant du retard. Ne rien faire lui coûte.")
    print("")
    print("  %d dossier(s) tirent avantage de la lacune : %s"
          % (gagnants, "aucun" if not gagnants else "À CORRIGER"))
    print("")
    print("  ET CE QUI N'EST PAS BLOQUÉ POUR AUTANT : les études et les mesures")
    print("  sont FINANÇABLES — c'est même par elles que la lacune se comble —")
    print("  les opérations préparatoires réversibles sont admises, et un")
    print("  besoin essentiel urgent reçoit l'intervention minimale et")
    print("  temporaire. LE DÉFAUT DE GRILLE SUSPEND L'INSTRUCTION, IL NE")
    print("  SUSPEND NI LA CONNAISSANCE NI LE SECOURS.")
    return gagnants


def procedures_differentes():
    titre("SECONDE PROPRIÉTÉ EXIGÉE — MÊME RISQUE, INSTRUCTIONS DIFFÉRENTES")
    base = [x for x in DOSSIERS if x.cle == "stockage-geo"][0]
    complete = grille_complete()
    print("  Deux dossiers de MÊME RISQUE — mêmes gravité, étendue,")
    print("  probabilité et réversibilité — et d'états de connaissance")
    print("  différents.")
    print("")
    print("  %-26s %6s %11s %7s  %-20s %s"
          % ("dossier", "confi", "réductible", "délai", "régime", "procédure"))
    resultats = {}
    for etiquette, confiance, reductible, delai in (
            ("mal connu, réductible vite", 0.55, True, 3),
            ("mal connu, réductible tard", 0.55, True, 9),
            ("bien connu, irréductible", 0.85, False, 0)):
        jumeau = Dossier(base.cle, base.libelle, base.domaine, base.gravite,
                         base.etendue, base.plausibilite, base.reversible_sur,
                         confiance, reductible, delai)
        regime, _, _ = qualifier(jumeau, complete)
        proc, raison = instruire(jumeau, complete)
        resultats[etiquette] = (regime, proc)
        print("  %-26s %6.2f %11s %7s  %-20s %s"
              % (etiquette, confiance, "oui" if reductible else "non",
                 delai if reductible else "—", regime, proc))
    regimes = set(r for r, _ in resultats.values())
    procedures = set(p for _, p in resultats.values())
    print("")
    print("  %d régime(s) pour %d procédures. C'EST EXACTEMENT CE QUE LA RÈGLE"
          % (len(regimes), len(procedures)))
    print("  VEUT : l'incertitude ne change PAS le régime de risque — elle")
    print("  change LA MANIÈRE D'INSTRUIRE. Acquérir des données quand c'est")
    print("  possible à temps ; expliciter une marge de précaution quand ce ne")
    print("  l'est pas ; appliquer la grille directement quand l'information")
    print("  est robuste.")
    print("")
    print("  LA VERSION PRÉCÉDENTE CONCLUAIT QUE « L'INCERTITUDE N'EMPORTE")
    print("  RIEN » PARCE QU'ELLE NE REGARDAIT QUE LE RÉGIME. Elle regardait au")
    print("  mauvais endroit.")
    return resultats


def une_lecture_signalee():
    titre("UNE LECTURE FAITE ICI, ET ELLE EST SIGNALÉE")
    g = grille_complete()
    print("  La règle dit : « incertitude réductible DANS UN DÉLAI UTILE :")
    print("  acquisition de données avant décision complète ». Elle ne dit pas")
    print("  ce qu'il advient d'une incertitude réductible HORS de ce délai.")
    print("")
    print("  LE PROGRAMME LA TRAITE COMME IRRÉDUCTIBLE POUR LA DÉCISION")
    print("  PRÉSENTE — sans quoi le qualificatif « dans un délai utile »")
    print("  n'aurait aucun effet. C'est une lecture de la règle existante,")
    print("  non une règle ajoutée, et elle est écrite pour être contestée.")
    print("")
    print("  %-14s %11s %7s  %s" % ("dossier", "réductible", "délai",
                                    "procédure"))
    for cle in ("stockage-geo", "pesticide", "capteur"):
        d = [x for x in DOSSIERS if x.cle == cle][0]
        proc, raison = instruire(d, g)
        print("  %-14s %11s %7d  %s"
              % (cle, "oui" if d.reductible else "non", d.delai_acquisition,
                 INSTRUCTIONS[proc]))
    print("")
    print("  Le délai utile vaut %d périodes dans la grille de référence. IL"
          % g["delai_utile"])
    print("  N'EST PAS CALIBRÉ, et il relève de la même pièce ouverte que les")
    print("  horizons : les seuils sectoriels.")


def les_seuils():
    titre("CE QUI TIENT — LE SEUIL FIXÉ D'AVANCE")
    plaus = sorted(x.plausibilite for x in DOSSIERS)
    complete = grille_complete()

    def au_porteur(seuil):
        g = dict(complete)
        g["seuil_plausibilite"] = seuil
        return len([x for x in DOSSIERS
                    if qualifier(x, g)[0] == "grave_irreversible"])

    print("  Probabilités des %d dossiers : %s"
          % (len(DOSSIERS), ", ".join("%.2f" % p for p in plaus)))
    print("")
    print("  %-38s %8s %12s" % ("seuil", "valeur", "au porteur"))
    for etiquette, seuil in (
            ("fixé d'avance par l'instance démocratique",
             GRILLE["seuil_plausibilite"]),
            ("choisi après lecture, pour admettre", max(plaus) + 0.01),
            ("choisi après lecture, pour refuser", min(plaus) - 0.01)):
        print("  %-38s %8.2f %12d" % (etiquette, seuil, au_porteur(seuil)))
    print("")
    print("  LES TROIS SEUILS SONT DANS LA MÊME PLAGE PLAUSIBLE, et rien dans")
    print("  le dossier ne distingue un seuil de principe d'un seuil taillé")
    print("  sur mesure. LE FIXER D'AVANCE EST CE QUI EN FAIT UNE CONTRAINTE.")
    print("")
    print("  ET CE QUI CHANGE AVEC LA ZONE INTERMÉDIAIRE : un dossier qui")
    print("  sort du régime le plus exigeant NE TOMBE PLUS DANS LE VIDE. Il")
    print("  entre en charge partagée, sous tranches et capacité d'arrêt.")


def publicite():
    titre("CE QUI TIENT — PUBLICITÉ ET RECOURS")
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
    print("  SANS LES INCERTITUDES PUBLIÉES, la procédure d'instruction n'est")
    print("  pas vérifiable : on ne peut pas contester une marge de précaution")
    print("  dont on ignore le motif. SANS LES AVIS MINORITAIRES, la")
    print("  divergence entre experts disparaît du dossier.")
    print("")
    print("  LE RECOURS repose sur des examinateurs et des CANAUX DE MESURE")
    print("  INDÉPENDANTS, qui conservent leurs propres marges d'erreur. Le")
    print("  contrôle de méthode qui interdit à un recours de posséder la")
    print("  valeur vraie est en place dans la règle d'émission.")


def main():
    print("=" * 78)
    print("A47 — DÉCIDER SOUS INCERTITUDE. DOCTRINE VALIDÉE")
    print("=" * 78)
    print("Précaution proportionnée. La doctrine n'arrête AUCUN SEUIL")
    print("NUMÉRIQUE : elle répartit la CHARGE DE LA PREUVE, fixe QUI établit")
    print("les seuils et QUAND, et fait agir l'incertitude SUR LA PROCÉDURE")
    print("D'INSTRUCTION plutôt que sur le régime de risque.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ ICI. Les dossiers sont fictifs.")

    la_grille()
    les_trois_variables()
    application()
    application(grille_complete(), "grille COMPLÈTE")
    anomalies, regimes = exhaustivite()
    gagnants = la_lacune_ne_profite_a_personne()
    procedures = procedures_differentes()
    une_lecture_signalee()
    les_seuils()
    publicite()

    titre("CE QUE CE PROGRAMME ÉTABLIT, ET CE QU'IL A DÛ CORRIGER")
    print("  DEUX DE SES TROIS « RESTES » ÉTAIENT DES LECTURES FAUTIVES.")
    print("")
    print("  LA ZONE INTERMÉDIAIRE était prévue par la règle ; le programme la")
    print("  rendait vide. Corrigé : tout dossier ÉVALUÉ qui ne relève ni de")
    print("  l'impossibilité, ni du risque plausible grave et irréversible, ni")
    print("  du risque limité et réversible y entre AUTOMATIQUEMENT.")
    print("")
    print("  ET UNE GRILLE LACUNAIRE N'Y ENTRE PAS — c'était une échappatoire")
    print("  que la correction précédente avait ouverte. La QUALIFICATION")
    print("  INCOMPLÈTE est un régime distinct : ni émission complète ni action")
    print("  irréversible, études et préparatoires réversibles admises, délai")
    print("  public et contrôle du retard. %d dossier(s) tirent avantage de la"
          % gagnants)
    print("  lacune. Les contrôles R1 et R2 : %s."
          % (anomalies or "aucune anomalie"))
    print("")
    print("  L'INCERTITUDE agit sur la PROCÉDURE, non sur le régime — c'est")
    print("  voulu. Le programme regardait le régime et concluait qu'elle")
    print("  n'emportait rien. Corrigé : trois dossiers de MÊME RISQUE et de")
    print("  connaissances différentes reçoivent %d procédures distinctes."
          % len(set(p for _, p in procedures.values())))
    print("")
    print("  ET LA LECTURE DU DÉLAI UTILE EST REFORMULÉE : une incertitude")
    print("  réductible hors délai est traitée comme NON RÉDUCTIBLE POUR LA")
    print("  DÉCISION PRÉSENTE, SANS ÊTRE DÉCLARÉE DÉFINITIVEMENT")
    print("  IRRÉDUCTIBLE — le réexamen reste ouvert dès que les connaissances")
    print("  arrivent.")
    print("")
    print("  ET TROIS VARIABLES SONT DÉSORMAIS SÉPARÉES : la probabilité")
    print("  estimée du dommage, la confiance accordée à cette estimation, et")
    print("  la possibilité de réduire l'incertitude dans un délai utile.")
    print("  Aucune ne porte plus la charge des deux autres.")
    print("")
    print("  RESTE OUVERT, ET C'EST LA SEULE PIÈCE : les horizons et seuils")
    print("  sectoriels — horizon de réversibilité, seuil de confiance, délai")
    print("  utile — à fixer par domaine selon la procédure d'A47, sans")
    print("  rouvrir son principe.")
    print("")
    print("  CE QUE CE PROGRAMME NE DIT PAS. Que la doctrine soit bonne. Aucun")
    print("  seuil n'est éprouvé, aucun dossier n'est réel, et un programme qui")
    print("  applique une règle ne la valide jamais. IL DIT SEULEMENT QU'ELLE")
    print("  S'APPLIQUE SANS LAISSER DE VIDE, ce que la version précédente")
    print("  affirmait à tort du contraire.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
