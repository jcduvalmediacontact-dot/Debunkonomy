#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A47 — DÉCIDER SOUS INCERTITUDE. Doctrine de précaution proportionnée.
Proposée par l'auteur le 2026-09-09, mise à l'épreuve ici.

CE QUE FAIT CE PROGRAMME : il applique la doctrine en neuf points à des
dossiers fictifs, et cherche où elle décide, où elle ne décide pas, et où le
résultat dépend de quelque chose qu'elle ne règle pas.

CE QU'IL NE FAIT PAS : fixer un seuil. La doctrine n'en arrête aucun — c'est
son propos — et le corpus n'en inventera pas.

LES NEUF POINTS, DANS LES TERMES DE L'AUTEUR

  1. Toute décision distingue GRAVITÉ, ÉTENDUE, RÉVERSIBILITÉ et URGENCE.
  2. L'incertitude ne produit automatiquement ni autorisation ni refus.
  3. Risque plausible de dommage GRAVE ET IRRÉVERSIBLE : le PORTEUR doit
     établir une compatibilité suffisante.
  4. Risque LIMITÉ ET RÉVERSIBLE : autorisation par tranches et sous
     surveillance possible ; l'AUTORITÉ doit motiver tout refus.
  5. BESOIN ESSENTIEL URGENT : la solution réalisable la moins risquée, en
     quantité minimale, avec réexamen rapide.
  6. RESSOURCES RARES : arbitrage au niveau du portefeuille des usages
     concurrents.
  7. Données, méthodes, incertitudes, seuils normatifs et AVIS MINORITAIRES
     sont publics.
  8. Le RECOURS repose sur des examinateurs et des canaux de mesure
     indépendants, qui conservent leurs propres marges d'erreur.
  9. Les seuils propres à chaque domaine sont fixés AVANT l'examen des
     dossiers, publiés et périodiquement révisés.

CE QUE LE PROGRAMME TROUVE, ET DEUX DE SES QUATRE RÉSULTATS SONT DÉFAVORABLES.
La doctrine tient sur les points 6, 7, 8 et 9 — le point 9 mord, et le
programme le montre. Elle laisse en revanche deux trous : la QUALIFICATION du
risque, qui décide de tout et dont elle ne dit pas qui l'opère ; et la ZONE
INTERMÉDIAIRE entre ses points 3 et 4, où la charge de la preuve n'est
attribuée à personne.

USAGE :  python modeles/nemo_a47.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False


# =====================================================================
# POINT 1 — LES QUATRE DIMENSIONS, ET ELLES NE SE MÉLANGENT PAS
# =====================================================================
class Dossier(object):
    def __init__(self, cle, libelle, gravite, etendue, reversible,
                 plausibilite, urgence=False, essentiel=False):
        self.cle = cle
        self.libelle = libelle
        self.gravite = gravite          # 0 à 3
        self.etendue = etendue          # 0 à 3
        self.reversible = reversible    # déclaré, et c'est tout le problème
        self.plausibilite = plausibilite
        self.urgence = urgence
        self.essentiel = essentiel


DOSSIERS = [
    Dossier("renovation", "Rénovation thermique", 1, 1, True, 0.20),
    Dossier("stockage-geo", "Stockage géologique de CO2", 2, 2, False, 0.50),
    Dossier("barrage", "Grand barrage en zone habitée", 3, 3, False, 0.70),
    Dossier("pesticide", "Pesticide à large spectre", 2, 3, True, 0.60),
    Dossier("mine-lithium", "Mine de lithium", 2, 1, False, 0.30),
    Dossier("medicament", "Traitement essentiel en épidémie", 3, 0, False,
            0.55, urgence=True, essentiel=True),
]

SEUIL_PLAUSIBILITE = 0.50   # NON CALIBRÉ. Publié d'avance — point 9.
GRAVITE_SERIEUSE = 2
ETENDUE_LIMITEE = 2


# =====================================================================
# POINTS 3, 4 ET 5 — LE RÉGIME, ET LA CHARGE DE LA PREUVE
# =====================================================================
REGIMES = {
    "grave_irreversible": ("porteur",
                           "établir une compatibilité suffisante"),
    "limite_reversible": ("autorité",
                          "motiver tout refus ; tranches et surveillance"),
    "urgence_essentielle": ("décision provisoire",
                            "solution réalisable la moins risquée, quantité "
                            "minimale, réexamen rapide"),
    "intermediaire": (None, None),
}


def regime(d, seuil=None):
    """Rend la clé de régime. LE POINT 5 PREND LE PAS quand il s'applique —
    mais le programme relève plus bas que la doctrine ne le dit nulle part."""
    seuil = SEUIL_PLAUSIBILITE if seuil is None else seuil
    if d.urgence and d.essentiel:
        return "urgence_essentielle"
    if (d.plausibilite >= seuil and d.gravite >= GRAVITE_SERIEUSE
            and not d.reversible):
        return "grave_irreversible"
    if (d.reversible and d.gravite <= GRAVITE_SERIEUSE
            and d.etendue <= ETENDUE_LIMITEE):
        return "limite_reversible"
    return "intermediaire"


def point_3_applique(d, seuil=None):
    seuil = SEUIL_PLAUSIBILITE if seuil is None else seuil
    return (d.plausibilite >= seuil and d.gravite >= GRAVITE_SERIEUSE
            and not d.reversible)


# =====================================================================
# POINT 7 — CE QUE TOUTE DÉCISION DOIT PUBLIER
# =====================================================================
PUBLICATION = ("donnees", "methodes", "incertitudes", "seuil_normatif",
               "avis_minoritaires")


def controler_publication(decision):
    """P1 — la publicité n'est pas un supplément : sans elle, ni le recours du
    point 8 ni la révision du point 9 ne sont exerçables."""
    return ["[P1] %s : « %s » n'est pas publié" % (decision.get("cle"), champ)
            for champ in PUBLICATION if not decision.get(champ)]


# =====================================================================
def titre(libelle):
    print("")
    print("=" * 78)
    print(libelle)
    print("=" * 78)


# =====================================================================
def tableau():
    titre("LA DOCTRINE APPLIQUÉE — POINTS 1, 3, 4 ET 5")
    print("  Seuil de plausibilité PUBLIÉ D'AVANCE : %.2f. Non calibré."
          % SEUIL_PLAUSIBILITE)
    print("")
    print("  %-14s %3s %3s %6s %6s  %-22s %s"
          % ("dossier", "gra", "éte", "révers", "plaus", "régime", "charge"))
    compte = {}
    for d in DOSSIERS:
        r = regime(d)
        charge = REGIMES[r][0] or "NON ATTRIBUÉE"
        compte[r] = compte.get(r, 0) + 1
        print("  %-14s %3d %3d %6s %6.2f  %-22s %s"
              % (d.cle, d.gravite, d.etendue,
                 "oui" if d.reversible else "non", d.plausibilite, r, charge))
    print("")
    print("  LE POINT 2 EST TENU, ET C'EST DÉJÀ QUELQUE CHOSE. L'incertitude")
    print("  ne produit ici ni autorisation ni refus automatiques : elle")
    print("  DÉPLACE LA CHARGE DE LA PREUVE. C'est une règle de procédure, et")
    print("  c'est ce qui la rend applicable sans seuil numérique.")
    return compte


def trou_de_la_qualification():
    titre("PREMIER TROU — LA QUALIFICATION DÉCIDE, ET NUL NE SAIT QUI LA FAIT")
    d = [x for x in DOSSIERS if x.cle == "stockage-geo"][0]
    print("  %s. Gravité %d, étendue %d, plausibilité %.2f."
          % (d.libelle, d.gravite, d.etendue, d.plausibilite))
    print("  La RÉVERSIBILITÉ est contestée : réversible sur cinquante ans")
    print("  selon un organisme, irréversible à l'échelle humaine selon un")
    print("  autre. AUCUN DES DEUX N'A TORT — ils ne parlent pas du même")
    print("  horizon.")
    print("")
    print("  %-16s %-22s %-14s %s"
          % ("lecture", "régime", "charge", "conséquence probable"))
    resultats = {}
    for reversible, lecture in ((True, "réversible"), (False, "irréversible")):
        copie = Dossier(d.cle, d.libelle, d.gravite, d.etendue, reversible,
                        d.plausibilite)
        r = regime(copie)
        charge = REGIMES[r][0] or "NON ATTRIBUÉE"
        resultats[lecture] = (r, charge)
        print("  %-16s %-22s %-14s %s"
              % (lecture, r, charge,
                 "autorisé par tranches sauf refus motivé"
                 if charge == "autorité" else
                 "refusé tant que le porteur n'a pas établi la compatibilité"))
    print("")
    print("  LA CHARGE DE LA PREUVE BASCULE ENTIÈREMENT, ET AVEC ELLE L'ISSUE")
    print("  PROBABLE DU DOSSIER — sur la seule qualification d'une dimension.")
    print("  LA DOCTRINE RÉPARTIT LA CHARGE APRÈS UNE CLASSIFICATION DONT ELLE")
    print("  NE DIT NI QUI L'OPÈRE NI SELON QUELLE PROCÉDURE.")
    print("")
    print("  ET CE N'EST PAS UN DÉTAIL DE RÉDACTION. Si l'autorité qui")
    print("  qualifie classe elle-même, on retrouve la capture du cas 7 de la")
    print("  règle d'émission, déplacée d'un cran. Si l'organisme de mesure")
    print("  classe, on lui donne la souveraineté que A46 lui refuse : la")
    print("  réversibilité À QUEL HORIZON est un choix normatif, non une")
    print("  mesure. LA QUALIFICATION DU RISQUE EST UNE PIÈCE MANQUANTE.")
    return resultats


def conflit_3_et_5():
    titre("SECOND TROU — LES POINTS 3 ET 5 SE CONTREDISENT, ET RIEN NE TRANCHE")
    d = [x for x in DOSSIERS if x.cle == "medicament"][0]
    print("  %s. Gravité %d, irréversible, plausibilité %.2f, URGENT et"
          % (d.libelle, d.gravite, d.plausibilite))
    print("  ESSENTIEL.")
    print("")
    print("  LE POINT 3 S'APPLIQUE : %s" % ("oui" if point_3_applique(d)
                                            else "non"))
    print("    → le porteur doit établir une compatibilité suffisante, ce")
    print("      qu'une incertitude non levée lui interdit par construction.")
    print("  LE POINT 5 S'APPLIQUE AUSSI : oui")
    print("    → la solution réalisable la moins risquée est accordée")
    print("      provisoirement, en quantité minimale.")
    print("")
    print("  LES DEUX INSTRUCTIONS SONT CONTRAIRES : l'une refuse tant que la")
    print("  preuve manque, l'autre accorde parce que le besoin n'attend pas.")
    print("  LA DOCTRINE NE LES ORDONNE PAS. Le programme applique le point 5")
    print("  — c'est un CHOIX D'IMPLÉMENTATION, pas une lecture du texte, et")
    print("  il doit être signalé comme tel.")
    print("")
    print("  LA VERSION ANTÉRIEURE DE LA RÈGLE PORTAIT L'EXCEPTION : « sauf")
    print("  impossibilité physique ou risque catastrophique suffisamment")
    print("  établi ». La rédaction du 2026-09-09 ne la reprend pas. IL FAUT")
    print("  DIRE SI ELLE EST MAINTENUE — sans elle, le point 5 autorise")
    print("  provisoirement ce que le point 3 refuse.")

    print("")
    print("  ET « LA MOINS RISQUÉE » SUPPOSE UN ORDRE. Trois solutions")
    print("  réalisables, trois profils incomparables :")
    options = [("A", 3, 0, False, "grave, étroit, irréversible"),
               ("B", 1, 3, True, "léger, très large, réversible"),
               ("C", 2, 1, False, "moyen, étroit, irréversible")]
    print("")
    print("  %-8s %3s %3s %8s  %s" % ("option", "gra", "éte", "révers",
                                      "profil"))
    for cle, g, e, rev, note in options:
        print("  %-8s %3d %3d %8s  %s"
              % (cle, g, e, "oui" if rev else "non", note))
    ordres = {
        "gravité d'abord": min(options, key=lambda o: (o[1], o[2]))[0],
        "étendue d'abord": min(options, key=lambda o: (o[2], o[1]))[0],
        "réversibilité d'abord": min(options,
                                     key=lambda o: (0 if o[3] else 1,
                                                    o[1] + o[2]))[0],
        "produit gravité × étendue": min(options,
                                         key=lambda o: o[1] * o[2])[0],
    }
    print("")
    for regle, gagnant in sorted(ordres.items()):
        print("    %-28s → option %s" % (regle, gagnant))
    distincts = sorted(set(ordres.values()))
    print("")
    print("  %d gagnants pour %d ordres plausibles. « LA MOINS RISQUÉE » N'EST"
          % (len(distincts), len(ordres)))
    print("  PAS UNE DONNÉE : c'est le résultat d'une pondération entre")
    print("  dimensions incommensurables, exactement comme au cas 2 de la")
    print("  règle d'émission. La doctrine ne peut pas la fournir, et elle ne")
    print("  doit pas prétendre le faire.")
    return {"conflit": point_3_applique(d), "ordres": len(distincts)}


def le_point_9_mord():
    titre("CE QUI TIENT — LE POINT 9 N'EST PAS DÉCORATIF")
    print("  Le point 9 exige que les seuils soient fixés AVANT l'examen des")
    print("  dossiers. Voici ce que coûte de ne pas le faire.")
    print("")
    plausibilites = sorted(d.plausibilite for d in DOSSIERS)
    print("  Plausibilités des six dossiers : %s"
          % ", ".join("%.2f" % p for p in plausibilites))
    print("")
    print("  %-34s %8s %10s %10s"
          % ("seuil", "valeur", "au porteur", "à l'autorité"))
    resultats = {}
    for etiquette, seuil in (
            ("publié d'avance", SEUIL_PLAUSIBILITE),
            ("choisi après, pour tout admettre", max(plausibilites) + 0.01),
            ("choisi après, pour tout refuser", min(plausibilites) - 0.01)):
        porteur = len([d for d in DOSSIERS
                       if regime(d, seuil) == "grave_irreversible"])
        autorite = len([d for d in DOSSIERS
                        if regime(d, seuil) == "limite_reversible"])
        resultats[etiquette] = (porteur, autorite)
        print("  %-34s %8.2f %10d %10d"
              % (etiquette, seuil, porteur, autorite))
    print("")
    print("  UN SEUIL CHOISI APRÈS COUP PRODUIT L'ISSUE QU'ON VEUT, ET RIEN")
    print("  DANS LE DOSSIER NE LE DISTINGUE D'UN SEUIL DE PRINCIPE : les deux")
    print("  sont des nombres compris dans la plage des valeurs plausibles.")
    print("  FIXER LE SEUIL D'AVANCE EST CE QUI EN FAIT UNE CONTRAINTE PLUTÔT")
    print("  QU'UNE DESCRIPTION. C'est le point 9, et il mord.")
    print("")
    print("  MAIS IL NE SE SUFFIT PAS : « périodiquement révisés » rouvre la")
    print("  main à chaque révision. Ce qui protège n'est pas la fixation")
    print("  seule, c'est la fixation PLUS la publication PLUS le fait que la")
    print("  révision ne s'applique pas au dossier en cours. Le point 9 dit")
    print("  les deux premières ; LA TROISIÈME MANQUE.")
    return resultats


def publicite():
    titre("CE QUI TIENT AUSSI — LES POINTS 7 ET 8")
    complete = {"cle": "barrage", "donnees": True, "methodes": True,
                "incertitudes": True, "seuil_normatif": True,
                "avis_minoritaires": True}
    partielle = dict(complete, cle="barrage-bis", incertitudes=False,
                     avis_minoritaires=False)
    print("  Le point 7 exige cinq publications : %s." % ", ".join(PUBLICATION))
    print("")
    print("  dossier complet   : %s"
          % (controler_publication(complete) or "aucune anomalie"))
    for a in controler_publication(partielle):
        print("    %s" % a)
    print("")
    print("  CE QUE CES DEUX MANQUES SUPPRIMENT EN PRATIQUE. Sans les")
    print("  INCERTITUDES publiées, le point 3 est inapplicable : on ne peut")
    print("  pas dire qu'un risque est « plausible » sans dire de quoi on est")
    print("  incertain. Sans les AVIS MINORITAIRES, la divergence entre")
    print("  organismes disparaît du dossier — et c'est précisément elle qui,")
    print("  dans la règle d'émission, sert d'alarme.")
    print("")
    print("  LE POINT 8 EST DÉJÀ TENU PAR LE CORPUS, et il a été acquis")
    print("  contre lui-même : la simulation de la règle d'émission donnait au")
    print("  recours la VALEUR VRAIE par construction. Le contrôle de méthode")
    print("  qui l'interdit est en place, et il échoue si un oracle revient.")
    return len(controler_publication(partielle))


def main():
    print("=" * 78)
    print("A47 — DÉCIDER SOUS INCERTITUDE")
    print("=" * 78)
    print("Doctrine de précaution PROPORTIONNÉE, en neuf points. Elle n'arrête")
    print("aucun seuil numérique : elle répartit LA CHARGE DE LA PREUVE et")
    print("définit la procédure par laquelle les seuils seront établis.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ ICI NON PLUS. Les dossiers sont fictifs.")

    compte = tableau()
    qualification = trou_de_la_qualification()
    conflit = conflit_3_et_5()
    seuils = le_point_9_mord()
    manques = publicite()

    titre("CE QUE LA DOCTRINE TIENT, ET LES DEUX TROUS QU'ELLE LAISSE")
    print("  TIENT — le point 2 : l'incertitude déplace la charge au lieu de")
    print("  trancher seule. Le point 6 : l'arbitrage de portefeuille, déjà")
    print("  construit et mesuré. Le point 7 : la publicité, sans laquelle ni")
    print("  le recours ni la révision ne sont exerçables. Le point 8 : le")
    print("  recours instrumenté, acquis contre une faute du corpus. Le point")
    print("  9 : le seuil fixé d'avance, et le programme montre qu'il mord.")
    print("")
    print("  TROU 1 — LA QUALIFICATION. Sur un seul dossier, deux lectures")
    print("  également défendables de la réversibilité font basculer la charge")
    print("  de la preuve du porteur à l'autorité, et l'issue avec elle. LA")
    print("  DOCTRINE RÉPARTIT LA CHARGE APRÈS UNE CLASSIFICATION DONT ELLE NE")
    print("  RÈGLE NI L'AUTEUR NI LA PROCÉDURE. C'est le point le plus")
    print("  exposé : y placer l'autorité qui qualifie ramène la capture, y")
    print("  placer l'organisme de mesure lui donne la souveraineté que A46")
    print("  lui refuse.")
    print("")
    print("  TROU 2 — LA ZONE INTERMÉDIAIRE. %d dossiers sur %d ne relèvent NI"
          % (compte.get("intermediaire", 0), len(DOSSIERS)))
    print("  du point 3 NI du point 4 : graves mais réversibles, ou")
    print("  irréversibles mais peu plausibles. LA CHARGE DE LA PREUVE N'Y EST")
    print("  ATTRIBUÉE À PERSONNE, et ce sont les cas ordinaires.")
    print("")
    print("  ET UNE CONTRADICTION À LEVER — les points 3 et 5 s'appliquent")
    print("  ensemble au dossier urgent, avec des instructions contraires. La")
    print("  rédaction du 2026-09-09 a laissé tomber l'exception « sauf risque")
    print("  catastrophique suffisamment établi » que portait la version")
    print("  précédente. IL FAUT DIRE SI ELLE EST MAINTENUE.")
    print("")
    print("  CE QUE CE PROGRAMME NE DIT PAS. Il ne dit pas que la doctrine est")
    print("  mauvaise : elle tient sur cinq de ses neuf points, et ses deux")
    print("  trous sont des PIÈCES MANQUANTES, non des contradictions")
    print("  internes. Il ne dit pas non plus qu'elle est bonne : aucun de ses")
    print("  seuils n'est éprouvé, aucun dossier n'est réel, et un programme")
    print("  qui applique une règle ne la valide jamais.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
