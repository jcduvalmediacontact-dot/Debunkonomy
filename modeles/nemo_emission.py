#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LA RÈGLE D'ÉMISSION DE NEMO IMS — VERSION 2, 2026-09-09.

QUATRE CONCLUSIONS DE LA VERSION 1 ÉTAIENT TROP FORTES. L'auteur les a
corrigées le jour même, et les corrections changent la conception, non la
rédaction.

  (1) « LE CAS 7 NE SE RÉPARE PAS » ÉTAIT FAUX. Un contrôle qui ne porte que
      sur des DÉCLARATIONS ne détecte pas leur falsification — cela reste
      vrai. Mais la capture ne s'élimine jamais avec certitude ET SE DÉTECTE :
      données satellitaires, mesures indépendantes, traçabilité, audits
      aléatoires, PLURALITÉ DES EXPERTS, publication, alerte, recours.

  (2) « L'ABSENCE DE REPRISE EST LA CONTREPARTIE DE L'ABSENCE DE DETTE » ÉTAIT
      FAUX. Non remboursable veut dire qu'un bénéficiaire CONFORME ne
      rembourse pas. Cela n'interdit ni la récupération des sommes
      INUTILISÉES, ni le gel des tranches FUTURES, ni la restitution pour
      ERREUR MANIFESTE, ni le recouvrement pour FRAUDE, ni la responsabilité
      personnelle des dirigeants. A45 protège le bénéficiaire LÉGITIME, il ne
      crée aucune irrévocabilité au profit d'un bénéficiaire INDU.

  (3) LA CONTRAINTE PHYSIQUE N'EST PAS SON CONSTAT INSTITUTIONNEL. Une loi
      physique ne se vote pas ; une estimation de stock ou de pression reste
      incertaine, révisable, contestable. DONNER UN VETO INCONTESTABLE À
      L'ORGANISME QUI ESTIME CRÉERAIT EXACTEMENT LA CAPTURE DU CAS 7. Ce
      programme sépare donc partout la valeur VRAIE de la valeur CONSTATÉE, et
      la première s'applique au monde que la seconde ait vu juste ou non.

  (4) F3 N'EST PAS VALIDÉ EMPIRIQUEMENT. Le cas 7 établit une VULNÉRABILITÉ
      LOGIQUE à la manipulation d'un indicateur déclaré. Pas une observation.

CINQ FONCTIONS SÉPARÉES — A46, VALIDÉ PAR L'AUTEUR LE 2026-09-09, dans sa
formulation : MESURE SCIENTIFIQUE des ressources, pressions physiques, limites
écologiques et INCERTITUDES ; QUALIFICATION des projets et des besoins
essentiels ; PRIORITÉ DÉMOCRATIQUE entre les projets admissibles ; CALIBRAGE du
montant, du rythme et des TRANCHES ; CONTRÔLE, SUSPENSION, CORRECTION,
RÉCUPÉRATION ET RECOURS.

CINQ FONCTIONS NE VEUT PAS DIRE CINQ INSTITUTIONS — correction de l'auteur.
A46 exige CINQ CENTRES DE RESPONSABILITÉ INDÉPENDANTS : mandats, nominations,
budgets et responsabilités séparés. Qu'ils soient cinq personnes juridiques
distinctes ou cinq organes indépendants d'une même organisation est une
MODALITÉ ENCORE OUVERTE, et le programme n'en tranche aucune : il nomme des
centres, pas des sièges.

ET LE PRINCIPE PORTE DEUX EXIGENCES, NON UNE. « Aucune autorité ne cumule la
mesure, la qualification, la priorité, l'émission ET SON PROPRE CONTRÔLE. » Le
NON-CUMUL se lit sur l'organigramme et le contrôle S1 le vérifie. L'INTERDICTION
DE S'AUTO-CONTRÔLER se lit sur le DOSSIER, et elle signifie que NUL N'EST
L'UNIQUE NI LE DERNIER JUGE DE SES PROPRES ACTES. ELLE N'INTERDIT NI LE
CONTRÔLE INTERNE, NI LA CORRECTION SPONTANÉE, NI LA SUSPENSION IMMÉDIATE D'UN
VERSEMENT — c'est le contrôle S3, réécrit sur ce point.

NEUF ÉTATS SUCCESSIFS. proposé, physiquement admissible, politiquement
prioritaire, financièrement programmé, versé par tranches, contrôlé, achevé —
et les deux issues défavorables : suspendu, récupéré. Le contrôle S2 vérifie
que chaque passage est exercé par le POUVOIR COMPÉTENT et par lui seul.

AUCUN SEUIL N'EST CALIBRÉ, les projets sont fictifs, et ce programme ne
modélise pas l'inflation : les prix n'y sont pas endogènes.

USAGE :  python modeles/nemo_emission.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False


# =====================================================================
# LE MONDE — valeurs VRAIES. Elles s'appliquent que le constat soit juste
# ou non : c'est la correction (3) de l'auteur.
# =====================================================================
FRONTIERES = {"carbone": 400.0, "biodiversite": 30.0, "eau": 120.0}
RESSOURCES = {"lithium": 100.0, "cuivre": 400.0, "travail": 1000.0}
CAPACITE = 1000.0


class Projet(object):
    def __init__(self, cle, libelle, demande, essentiel, ressources,
                 frontieres, beneficiaires=0, gravite=0, rang_depot=0,
                 tranches=4):
        self.cle = cle
        self.libelle = libelle
        self.demande = float(demande)
        self.essentiel = bool(essentiel)
        self.ressources = dict(ressources)
        self.frontieres = dict(frontieres)   # pressions VRAIES
        self.beneficiaires = beneficiaires
        self.gravite = gravite
        self.rang_depot = rang_depot
        self.tranches = tranches

    def soulage(self):
        return -sum(v for v in self.frontieres.values() if v < 0)

    def pese(self):
        return sum(v for v in self.frontieres.values() if v > 0)


CATALOGUE = [
    Projet("eau", "Adduction d'eau potable", 300, True,
           {"cuivre": 50, "travail": 150}, {"carbone": 20, "eau": 10},
           beneficiaires=40, gravite=3, rang_depot=1),
    Projet("hopital", "Hôpital de district", 400, True,
           {"cuivre": 60, "travail": 250}, {"carbone": 30},
           beneficiaires=25, gravite=3, rang_depot=2),
    Projet("logement", "Réhabilitation thermique du logement", 400, True,
           {"cuivre": 90, "travail": 300}, {"carbone": -40},
           beneficiaires=60, gravite=2, rang_depot=3),
    Projet("solaire", "Parc solaire et stockage", 600, False,
           {"lithium": 90, "cuivre": 200, "travail": 300},
           {"carbone": -150, "biodiversite": 40},
           beneficiaires=80, gravite=1, rang_depot=4),
    Projet("hydrogene", "Électrolyse à grande échelle", 500, False,
           {"lithium": 130, "cuivre": 120, "travail": 200},
           {"carbone": -90, "eau": 60},
           beneficiaires=30, gravite=1, rang_depot=5),
    Projet("charbon", "Centrale thermique de secours", 500, False,
           {"cuivre": 40, "travail": 120}, {"carbone": 500},
           beneficiaires=50, gravite=0, rang_depot=6),
]
PAR_CLE = dict((p.cle, p) for p in CATALOGUE)


# =====================================================================
# A46 — LES CINQ POUVOIRS, ET LEUR SÉPARATION
# =====================================================================
POUVOIRS = ("mesurer", "qualifier", "prioriser", "calibrer", "controler")

CHAINE = [
    ("organisme-de-mesure", ("mesurer",)),
    ("autorite-de-qualification", ("qualifier",)),
    ("instance-democratique", ("prioriser",)),
    ("autorite-monetaire", ("calibrer",)),
    ("audit-et-juridiction", ("controler",)),
]

# La portée de chaque fonction, dans les termes de l'auteur.
PORTEE = {
    "mesurer": "ressources, pressions physiques, limites écologiques et "
               "INCERTITUDES",
    "qualifier": "les projets ET les besoins essentiels",
    "prioriser": "entre les projets ADMISSIBLES, démocratiquement",
    "calibrer": "le montant, le rythme et les TRANCHES",
    "controler": "contrôle, suspension, correction, récupération et RECOURS",
}

TITULAIRE = dict((p, nom) for nom, pouvoirs in CHAINE for p in pouvoirs)

# La cinquième fonction se déploie sur TROIS NIVEAUX, et le troisième suppose
# un organe distinct de celui qui vérifie la conformité. QUE CE SOIENT DEUX
# PERSONNES JURIDIQUES OU DEUX ORGANES INDÉPENDANTS D'UNE MÊME ORGANISATION
# EST UNE MODALITÉ OUVERTE : le programme exige l'indépendance, pas le siège.
ORGANE_DE_RECOURS = "juridiction-de-recours"
ETATS_DE_CONTROLE = ("controle", "suspendu", "recupere")


def controler_separation(chaine):
    """S1 — aucune institution ne cumule deux pouvoirs, et les cinq sont
    couverts. C'est la décision A46, rendue vérifiable."""
    anomalies = []
    vus = {}
    for nom, pouvoirs in chaine:
        if len(pouvoirs) > 1:
            anomalies.append("[S1] %s cumule %s" % (nom, ", ".join(pouvoirs)))
        for p in pouvoirs:
            if p in vus:
                anomalies.append("[S1] le pouvoir « %s » est tenu par %s ET %s"
                                 % (p, vus[p], nom))
            vus[p] = nom
    for p in POUVOIRS:
        if p not in vus:
            anomalies.append("[S1] aucun titulaire pour « %s »" % p)
    return anomalies


# =====================================================================
# LES TROIS NIVEAUX DE CONTRÔLE — correction de l'auteur, 2026-09-09
# =====================================================================
# INTERDIRE L'AUTOCONTRÔLE N'EST PAS INTERDIRE L'AUTOCORRECTION. Une autorité
# qui verse doit pouvoir suspendre immédiatement ce qu'elle croit erroné : la
# lui interdire ferait durer l'erreur au nom de la séparation des pouvoirs.
NIVEAUX = (
    ("interne", "contrôle immédiat par l'auteur de l'acte, avec capacité de "
                "SUSPENSION CONSERVATOIRE"),
    ("conformite", "contrôle INDÉPENDANT de la régularité de l'acte"),
    ("recours", "audit externe et voie juridictionnelle"),
)
NOM_NIVEAU = dict(NIVEAUX)

ETATS_TERMINAUX = ("acheve", "recupere")


def controler_autocontrole(dossier):
    """S3 — NUL N'EST L'UNIQUE NI LE DERNIER JUGE DE SES PROPRES ACTES.

    CE QUE S3 NE SIGNALE PAS, ET C'EST LA CORRECTION DE L'AUTEUR : la
    suspension conservatoire décidée par l'autorité qui a versé. C'est de
    l'autocorrection, pas de l'autocontrôle, et l'interdire retarderait la
    correction des erreurs.

    CE QUE S3 EXIGE, EN TROIS POINTS : qu'un contrôle de CONFORMITÉ ait été
    exercé par une institution étrangère à l'acte ; que la CLÔTURE ne soit pas
    le fait d'un auteur ; et qu'une voie de RECOURS extérieure existe, tenue
    par une institution distincte de l'auteur ET du contrôleur de conformité.
    """
    anomalies = []
    # EST AUTEUR celui qui a exercé un pouvoir de FOND — mesurer, qualifier,
    # prioriser, calibrer, verser. La suspension conservatoire du payeur en
    # relève aussi : elle est de l'autocorrection, non un contrôle. Définir
    # l'auteur par l'ÉTAT VISÉ rendrait tout clôturant auteur de son acte.
    auteurs = set(inst for _, _, pouvoir, inst, _, _ in dossier.journal
                  if pouvoir != "controler")
    conformite = [inst for _, _, _, inst, niveau, _ in dossier.journal
                  if niveau == "conformite"]
    independants = [x for x in conformite if x not in auteurs]
    termine = dossier.etat in ETATS_TERMINAUX

    if termine and not independants:
        anomalies.append(
            "[S3] %s : dossier clos sans aucun contrôle de conformité "
            "INDÉPENDANT — l'auteur a été l'unique juge de son acte"
            % dossier.projet.cle)
    for avant, apres, _, inst, _, _ in dossier.journal:
        if apres in ETATS_TERMINAUX and inst in auteurs:  # noqa: E501
            anomalies.append(
                "[S3] %s : la clôture (%s → %s) est le fait de « %s », qui a "
                "elle-même agi sur le dossier — nul n'est le DERNIER juge de "
                "son acte" % (dossier.projet.cle, avant, apres, inst))
    if dossier.recours is None:
        anomalies.append("[S3] %s : aucune voie de recours extérieure ouverte"
                         % dossier.projet.cle)
    elif dossier.recours in auteurs or dossier.recours in conformite:
        anomalies.append(
            "[S3] %s : la voie de recours est tenue par « %s », déjà "
            "intervenue sur le dossier" % (dossier.projet.cle, dossier.recours))
    return anomalies


# =====================================================================
# LES NEUF ÉTATS, ET QUI AUTORISE CHAQUE PASSAGE
# =====================================================================
ETATS = ("propose", "physiquement_admissible", "politiquement_prioritaire",
         "financierement_programme", "verse_par_tranches", "controle",
         "acheve", "suspendu", "recupere")

# Chaque passage nomme LES pouvoirs qui peuvent l'exercer. La suspension en
# admet DEUX : le contrôle, et l'auteur du versement à titre CONSERVATOIRE.
TRANSITIONS = {
    ("propose", "physiquement_admissible"): ("mesurer",),
    ("physiquement_admissible", "politiquement_prioritaire"): ("prioriser",),
    ("politiquement_prioritaire", "financierement_programme"): ("calibrer",),
    ("financierement_programme", "verse_par_tranches"): ("calibrer",),
    ("verse_par_tranches", "controle"): ("controler",),
    ("controle", "acheve"): ("controler",),
    ("verse_par_tranches", "suspendu"): ("controler", "calibrer"),
    ("controle", "suspendu"): ("controler", "calibrer"),
    ("suspendu", "recupere"): ("controler",),
    ("suspendu", "verse_par_tranches"): ("controler",),
}


class Dossier(object):
    """Un projet dans la chaîne. Le journal garde QUI a fait passer QUOI :
    sans cela, la séparation des pouvoirs n'est pas vérifiable."""

    def __init__(self, projet):
        self.projet = projet
        self.etat = "propose"
        self.journal = []
        self.recours = None      # institution devant laquelle le recours est
                                 # ouvert ; None = aucune, et S3 le signale

    def passer_a(self, etat, par, motif="", anomalies=None, institution=None,
                 niveau="interne"):
        """« institution » peut différer du titulaire de référence : c'est
        ainsi qu'une délégation, un détachement ou une double casquette se
        représentent. « niveau » dit à quel titre un contrôle s'exerce —
        interne, conformité ou recours — et c'est cette distinction qui sépare
        l'AUTOCORRECTION, permise, de l'AUTOCONTRÔLE, interdit."""
        institution = TITULAIRE.get(par) if institution is None else institution
        admis = TRANSITIONS.get((self.etat, etat))
        if anomalies is not None:
            if admis is None:
                anomalies.append("[S2] %s : passage %s → %s non prévu"
                                 % (self.projet.cle, self.etat, etat))
            elif par not in admis:
                anomalies.append("[S2] %s : %s → %s exercé par « %s » alors "
                                 "que seul %s le peut"
                                 % (self.projet.cle, self.etat, etat, par,
                                    " ou ".join("« %s »" % x for x in admis)))
        self.journal.append((self.etat, etat, par, institution, niveau, motif))
        self.etat = etat


# =====================================================================
# (3) MESURER N'EST PAS CONSTATER — le veto scientifique pluraliste
# =====================================================================
# Biais fixes, non aléatoires : le programme doit être reproductible.
ORGANISMES = [("A", 0.00), ("B", 0.10), ("C", -0.08), ("D", 0.05),
              ("E", -0.05)]
CAPTURE_AMPLEUR = 0.32      # ce qu'un organisme capté retranche à sa mesure
SEUIL_DIVERGENCE = 0.25     # au-delà, la divergence SAISIT la mesure externe
REGLES_DE_VETO = ("unique", "mediane", "prudente", "mediane_avec_recours",
                  "recours_pluriel")

# LE RECOURS EST UN INSTRUMENT, PAS UN ORACLE. La version précédente lui
# rendait la valeur VRAIE dès que la divergence dépassait le seuil : il
# possédait gratuitement ce qu'aucun dispositif réel ne possède, et le résultat
# publié en tirait sa robustesse. Corrigé sur remarque de l'auteur.
#
# CE À QUOI IL ACCÈDE, ET QUI EST NOUVEAU : un CANAL DE MESURE INDÉPENDANT —
# imagerie, traçabilité des matières, relevés de terrain — dont l'information ne
# passe ni par la déclaration du porteur ni par les modèles des organismes.
#
# CE QU'IL N'EST PAS, ET LE MOT COMPTE : une observation directe de la vérité.
# Un satellite, un capteur, une analyse matière dépendent d'un ÉTALONNAGE, d'un
# TRAITEMENT et parfois d'un MODÈLE. AUCUN INSTRUMENT NE POSSÈDE LA VÉRITÉ : il
# a une méthode, un étalonnage, une marge d'erreur et un risque de capture qui
# lui sont propres. C'est pourquoi son biais est déclaré ici comme celui des
# organismes, et qu'il figure parmi les cibles capturables.
CANAUX_DE_MESURE = [("satellite", 0.06), ("tracabilite", -0.04),
                    ("terrain", 0.09)]
INSTRUMENTS_DE_RECOURS = CANAUX_DE_MESURE   # nom conservé pour la lisibilité


def mesure_de_recours(vraie, captes=(), pluriel=False):
    """Rend (valeur, motif). Un seul instrument, ou trois en médiane.

    UN RECOURS À INSTRUMENT UNIQUE DÉPLACE LE POINT DE DÉFAILLANCE, IL NE LE
    SUPPRIME PAS : le capter suffit alors à museler l'alarme.
    """
    lot = INSTRUMENTS_DE_RECOURS if pluriel else INSTRUMENTS_DE_RECOURS[:1]
    vals = []
    for nom, biais in lot:
        if nom in captes:
            vals.append(vraie * (1.0 - CAPTURE_AMPLEUR))
        else:
            vals.append(vraie * (1.0 + biais))
    return (mediane(vals) if pluriel else vals[0],
            "canal de mesure indépendant (%s)" % ", ".join(n for n, _ in lot))


def estimations(vraie, captes=()):
    sorties = []
    for nom, biais in ORGANISMES:
        if nom in captes:
            sorties.append((nom, vraie * (1.0 - CAPTURE_AMPLEUR)))
        else:
            sorties.append((nom, vraie * (1.0 + biais)))
    return sorties


def mediane(valeurs):
    v = sorted(valeurs)
    n = len(v)
    return v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2])


def constat(vraie, regle, captes=()):
    """Rend (valeur retenue, motif). LE CONSTAT, JAMAIS LA CONTRAINTE.

    « unique » donne un pouvoir absolu à un seul organisme — c'est ce que
    l'auteur interdit. « prudente » retient l'estimation la plus haute : elle
    résiste tant qu'un organisme reste honnête, ET ELLE REFUSE DAVANTAGE DE
    PROJETS LÉGITIMES. « mediane_avec_recours » fait de LA DIVERGENCE le
    signal : au-delà du seuil, une mesure extérieure est saisie.
    """
    est = estimations(vraie, captes)
    vals = [v for _, v in est]
    if regle == "unique":
        return est[0][1], "estimation de l'organisme %s" % est[0][0]
    if regle == "prudente":
        return max(vals), "estimation la plus haute des %d" % len(vals)
    med = mediane(vals)
    if regle == "mediane":
        return med, "médiane de %d estimations" % len(vals)
    if regle in ("mediane_avec_recours", "recours_pluriel"):
        etendue = (max(vals) - min(vals)) / med if med else 0.0
        if etendue > SEUIL_DIVERGENCE:
            val, motif = mesure_de_recours(
                vraie, captes, pluriel=(regle == "recours_pluriel"))
            return val, ("divergence de %.0f %% : %s"
                         % (100 * etendue, motif))
        return med, ("médiane, divergence %.0f %% sous le seuil"
                     % (100 * etendue))
    raise ValueError(regle)


def captures_necessaires(vraie, seuil, regle):
    """Le MINIMUM de captures — organismes ET instruments de recours confondus
    — qui suffit à lever le veto. Rend (nombre, quoi) ou (None, None).

    LA RECHERCHE PORTE SUR TOUTES LES COMBINAISONS, et c'est le point : capter
    un organisme puis l'instrument de recours coûte deux captures, alors que
    faire taire la médiane seule en coûte trois. Ne compter que les organismes
    surestimait la robustesse du recours.
    """
    cibles = [n for n, _ in ORGANISMES] + [n for n, _ in INSTRUMENTS_DE_RECOURS]
    meilleur = None
    for masque in range(0, 2 ** len(cibles)):
        captes = tuple(cibles[i] for i in range(len(cibles))
                       if masque >> i & 1)
        if meilleur is not None and len(captes) >= meilleur[0]:
            continue
        val, _ = constat(vraie, regle, captes=captes)
        if val <= seuil:
            meilleur = (len(captes), captes)
    return meilleur if meilleur else (None, None)


# =====================================================================
# (1) LE VETO PHYSIQUE — exercé sur des CONSTATS, et il le dit
# =====================================================================
def veto_physique(projet, frontieres=None, ressources=None, regle="mediane",
                  captes=(), agregation=False):
    f = FRONTIERES if frontieres is None else frontieres
    r = RESSOURCES if ressources is None else ressources

    for nom, besoin in sorted(projet.ressources.items()):
        vu, _ = constat(besoin, regle, captes)
        if vu > r.get(nom, 0.0):
            return False, ("indisponible : %s, %.0f constatés pour %.0f "
                           "disponibles" % (nom, vu, r.get(nom, 0.0)))

    if agregation:
        if projet.pese() - projet.soulage() > 0:
            return False, "bilan agrégé défavorable"
        return True, "bilan agrégé favorable"

    for nom, effet in sorted(projet.frontieres.items()):
        if effet <= 0:
            continue
        vu, motif = constat(effet, regle, captes)
        if vu > f.get(nom, 0.0):
            return False, ("franchissement : %s, %.0f constatés pour %.0f "
                           "de budget" % (nom, vu, f.get(nom, 0.0)))
    return True, "admissible"


def infaisable_reellement(projet, frontieres=None, ressources=None):
    """Ce que le MONDE fait, indépendamment de tout constat : la contrainte
    physique ne se vote pas — correction (3) de l'auteur.

    ELLE PORTE SUR LES DEUX TESTS. Ne regarder que les limites franchies
    compterait comme « refusé à tort » un projet réellement impossible faute
    de matière — l'erreur que ce programme a commise en version 2.
    """
    f = FRONTIERES if frontieres is None else frontieres
    r = RESSOURCES if ressources is None else ressources
    if any(b > r.get(n, 0.0) for n, b in projet.ressources.items()):
        return True
    return any(v > f.get(n, 0.0) for n, v in projet.frontieres.items() if v > 0)


# =====================================================================
# (2) L'ARBITRAGE DE PORTEFEUILLE — et non un veto projet par projet
# =====================================================================
def portefeuilles_faisables(candidats, frontieres=None, ressources=None):
    """Rend la liste des sous-ensembles PHYSIQUEMENT faisables.

    LE VETO PROJET PAR PROJET EST LE PROBLÈME DU CAS 2 : il refuse isolément
    ce qui, entre usages concurrents, est arbitrable. Le physique borne
    L'ENSEMBLE des possibles ; le choix DANS cet ensemble appartient à la
    décision politique, et le programme ne le fait pas.
    """
    f = FRONTIERES if frontieres is None else frontieres
    r = RESSOURCES if ressources is None else ressources
    faisables = []
    for masque in range(1, 2 ** len(candidats)):
        lot = [candidats[i] for i in range(len(candidats)) if masque >> i & 1]
        ok = True
        for nom, dispo in r.items():
            if sum(p.ressources.get(nom, 0.0) for p in lot) > dispo:
                ok = False
                break
        if ok:
            for nom, budget in f.items():
                if sum(max(0.0, p.frontieres.get(nom, 0.0))
                       for p in lot) > budget:
                    ok = False
                    break
        if ok:
            faisables.append(lot)
    return faisables


# =====================================================================
# LA PRIORITÉ, ET LE DÉPARTAGE QUI RESTE POLITIQUE
# =====================================================================
DEPARTAGES = ("cout_par_beneficiaire", "nombre", "gravite", "anteriorite")


def departager(projets, regle):
    if regle == "cout_par_beneficiaire":
        return sorted(projets, key=lambda p: (p.demande / p.beneficiaires)
                      if p.beneficiaires else 1e9)
    if regle == "nombre":
        return sorted(projets, key=lambda p: -p.beneficiaires)
    if regle == "gravite":
        return sorted(projets, key=lambda p: -p.gravite)
    if regle == "anteriorite":
        return sorted(projets, key=lambda p: p.rang_depot)
    raise ValueError(regle)


class Saisine(object):
    """Ce que le mécanisme produit quand il ne peut pas trancher : NON PAS UN
    SILENCE, MAIS UNE SAISINE. C'est la correction du cas 3 — il faut une
    procédure, pas un critère."""

    instance = "instance-democratique"
    majorite = "à fixer — le corpus ne la fixe pas"
    motif_publie = True
    recours = "audit-et-juridiction"
    reexamen_du_perdant = "daté, à chaque cycle"

    def __init__(self, projets, enveloppe):
        self.projets = projets
        self.enveloppe = enveloppe

    def options(self):
        return dict((r, departager(self.projets, r)[0].cle)
                    for r in DEPARTAGES)


def prioriser(admissibles, enveloppe):
    """Rend (retenus, saisine). La saisine remplace l'ancien « indécidable »."""
    essentiels = [p for p in admissibles if p.essentiel]
    autres = [p for p in admissibles if not p.essentiel]
    if sum(p.demande for p in essentiels) > enveloppe and len(essentiels) > 1:
        return [], Saisine(essentiels, enveloppe)
    retenus = list(essentiels)
    reste = enveloppe - sum(p.demande for p in essentiels)
    for p in departager(autres, "anteriorite"):
        if p.demande <= reste:
            retenus.append(p)
            reste -= p.demande
    return retenus, None


# =====================================================================
# LE CALIBRAGE, LE VERSEMENT PAR TRANCHES ET LA REPRISE
# =====================================================================
# Correction (2) de l'auteur : non remboursable n'est pas irrévocable.
TAUX_INUTILISE = 1.00       # les sommes versées non employées reviennent
TAUX_RECOUVREMENT = 0.35    # ce qu'un recouvrement pour fraude rattrape
PART_EMPLOYEE = 0.70        # part d'une tranche déjà employée à la détection


def reprise(projet, periode_detection, fraude=False):
    """Rend (gele, restitue, recouvre, perdu) — les quatre volets distingués
    par l'auteur. LE GEL N'EST PAS UNE RÉCUPÉRATION : c'est de l'argent jamais
    versé, et il se compte à part."""
    par_tranche = projet.demande / projet.tranches
    versees = min(projet.tranches, periode_detection)
    verse = par_tranche * versees
    gele = projet.demande - verse
    employe = verse * PART_EMPLOYEE
    restitue = (verse - employe) * TAUX_INUTILISE
    recouvre = employe * TAUX_RECOUVREMENT if fraude else 0.0
    return gele, restitue, recouvre, verse - restitue - recouvre


# =====================================================================
# LA DÉTECTION EXTÉRIEURE — correction (1) de l'auteur
# =====================================================================
COUVERTURE_PHYSIQUE = 0.60   # part des projets couverts par mesure directe
INTERVALLE_AUDIT = 3         # un audit aléatoire toutes les N périodes
SEUIL_ECART = 0.15           # écart déclaré/constaté au-delà duquel on alerte


def detecter(vraie, declaree, rang, couvert_physiquement, alerte=False):
    """Rend (période de détection, canal) ou (None, None).

    TROIS CANAUX, ET ILS NE SE VALENT PAS. Le CANAL DE MESURE INDÉPENDANT ne
    passe par aucune déclaration : il voit tôt, mais ne couvre qu'une part des
    projets — et il a ses propres erreurs. L'AUDIT ALÉATOIRE couvre tout et
    arrive tard.
    L'ALERTE ne se planifie pas — elle est ici un PARAMÈTRE, non un mécanisme,
    et le programme ne prétend pas la produire.
    """
    if declaree >= vraie * (1.0 - SEUIL_ECART):
        return None, None
    if couvert_physiquement:
        return 1, "canal de mesure indépendant"
    if alerte:
        return 2, "alerte"
    return INTERVALLE_AUDIT * (1 + rang % 2), "audit aléatoire"


def couvert(projet):
    """Déterministe, non aléatoire : la couverture suit le rang de dépôt."""
    return (projet.rang_depot - 1) < COUVERTURE_PHYSIQUE * len(CATALOGUE)


def titre(n, libelle):
    print("")
    print("=" * 78)
    print("CAS %d — %s" % (n, libelle))
    print("=" * 78)


# =====================================================================
# A46 ET LE PROCESSUS, AVANT LES CAS
# =====================================================================
def separation():
    print("")
    print("=" * 78)
    print("A46 — LES CINQ FONCTIONS, ET CE QUE LEUR CUMUL PRODUIT")
    print("=" * 78)
    for nom, pouvoirs in CHAINE:
        for p in pouvoirs:
            print("  %-28s %-11s %s" % (nom, p, PORTEE[p]))
    saines = controler_separation(CHAINE)
    print("")
    print("  contrôle S1 sur la chaîne séparée : %s"
          % ("aucune anomalie" if not saines else saines))

    cumul = [("autorite-unique", ("mesurer", "qualifier", "calibrer")),
             ("instance-democratique", ("prioriser",)),
             ("audit-et-juridiction", ("controler",))]
    anomalies = controler_separation(cumul)
    print("")
    print("  Cinq CENTRES DE RESPONSABILITÉ, mandats et budgets séparés. Qu'ils")
    print("  soient cinq personnes juridiques ou cinq organes indépendants")
    print("  d'une même organisation est une MODALITÉ OUVERTE — A46 exige")
    print("  l'indépendance, pas le siège.")
    print("")
    print("  LA MÊME CHAÎNE AVEC UNE AUTORITÉ QUI MESURE, QUALIFIE ET VERSE :")
    for a in anomalies:
        print("    %s" % a)
    print("")
    print("  C'EST LA CONFIGURATION DU CAS 7 DE LA VERSION 1, et le contrôle")
    print("  la voit désormais — non par la SORTIE du dispositif, qui restait")
    print("  verte, mais PAR LA STRUCTURE DE L'INSTITUTION ELLE-MÊME.")

    # « ET SON PROPRE CONTRÔLE » — seconde exigence, et S1 n'y suffit pas.
    def dossier(cle):
        d = Dossier(PAR_CLE[cle])
        for etat, par in (("physiquement_admissible", "mesurer"),
                          ("politiquement_prioritaire", "prioriser"),
                          ("financierement_programme", "calibrer"),
                          ("verse_par_tranches", "calibrer")):
            d.passer_a(etat, par)
        return d

    print("")
    print("  LA SECONDE EXIGENCE — « ET SON PROPRE CONTRÔLE ». Elle ne se lit")
    print("  pas sur l'organigramme : S1 ne voit rien (%d anomalie) tant que"
          % len(controler_separation(CHAINE)))
    print("  cinq centres existent. S3 regarde LE DOSSIER.")
    print("")
    print("  LES TROIS NIVEAUX DE CONTRÔLE")
    for cle, portee in NIVEAUX:
        print("    %-11s %s" % (cle, portee))

    resultats = {}

    # (a) SUSPENSION CONSERVATOIRE par l'autorité qui a versé, PUIS contrôle
    #     indépendant. C'est de l'AUTOCORRECTION, et elle est permise.
    a = dossier("eau")
    a.recours = ORGANE_DE_RECOURS
    a.passer_a("suspendu", "calibrer", niveau="interne",
               motif="suspension conservatoire : versement présumé erroné")
    a.passer_a("verse_par_tranches", "controler", niveau="conformite")
    a.passer_a("controle", "controler", niveau="conformite")
    a.passer_a("acheve", "controler", niveau="conformite")
    resultats["autocorrection"] = controler_autocontrole(a)

    # (b) L'auteur du versement se contrôle lui-même ET clôt.
    b = dossier("hopital")
    b.recours = ORGANE_DE_RECOURS
    b.passer_a("controle", "controler", institution="autorite-monetaire",
               niveau="conformite")
    b.passer_a("acheve", "controler", institution="autorite-monetaire",
               niveau="conformite")
    resultats["autocontrole"] = controler_autocontrole(b)

    # (c) Contrôle indépendant, mais aucune voie de recours ouverte.
    c = dossier("logement")
    c.passer_a("controle", "controler", niveau="conformite")
    c.passer_a("acheve", "controler", niveau="conformite")
    resultats["sans recours"] = controler_autocontrole(c)

    print("")
    print("  %-46s %s" % ("situation", "S3"))
    for etiquette, anomalies in (
            ("suspension conservatoire par le payeur", resultats["autocorrection"]),
            ("le payeur se contrôle et clôt seul", resultats["autocontrole"]),
            ("contrôle indépendant, aucun recours", resultats["sans recours"])):
        print("  %-46s %s"
              % (etiquette, "aucune anomalie" if not anomalies
                 else "%d anomalie(s)" % len(anomalies)))
    print("")
    for a in resultats["autocontrole"] + resultats["sans recours"]:
        print("    %s" % a)
    print("")
    print("  LA PREMIÈRE LIGNE EST LA CORRECTION DE L'AUTEUR. L'autorité qui a")
    print("  versé SUSPEND elle-même ce qu'elle croit erroné, et S3 ne dit")
    print("  rien : c'est de l'AUTOCORRECTION. La lui interdire ferait durer")
    print("  l'erreur au nom de la séparation des pouvoirs.")
    print("")
    print("  CE QUE S3 REFUSE, C'EST D'ÊTRE L'UNIQUE OU LE DERNIER JUGE : un")
    print("  contrôle de conformité exercé par l'auteur lui-même, une clôture")
    print("  prononcée par lui, ou l'absence de voie de recours extérieure.")
    return {"saine": len(saines), "cumul": len(anomalies),
            "autocorrection": len(resultats["autocorrection"]),
            "autocontrole": len(resultats["autocontrole"])}


def processus():
    print("")
    print("=" * 78)
    print("LE PROCESSUS — NEUF ÉTATS, ET QUI AUTORISE CHAQUE PASSAGE")
    print("=" * 78)
    anomalies = []
    d = Dossier(PAR_CLE["eau"])
    chemin = [("physiquement_admissible", "mesurer", "interne"),
              ("politiquement_prioritaire", "prioriser", "interne"),
              ("financierement_programme", "calibrer", "interne"),
              ("verse_par_tranches", "calibrer", "interne"),
              ("controle", "controler", "conformite"),
              ("acheve", "controler", "conformite")]
    for etat, par, niveau in chemin:
        d.passer_a(etat, par, anomalies=anomalies, niveau=niveau)
    print("  chemin nominal   propose → %s"
          % " → ".join(x for x, _, _ in chemin))
    print("  issues défavorables : suspendu, recupere — par « controler » seul")
    d.recours = ORGANE_DE_RECOURS
    print("  anomalies S2 : %s" % (anomalies or "aucune"))
    print("  anomalies S3 : %s" % (controler_autocontrole(d) or "aucune"))

    mauvais = []
    e = Dossier(PAR_CLE["hopital"])
    e.passer_a("physiquement_admissible", "mesurer", anomalies=mauvais)
    e.passer_a("verse_par_tranches", "calibrer", anomalies=mauvais)
    f = Dossier(PAR_CLE["logement"])
    f.passer_a("physiquement_admissible", "qualifier", anomalies=mauvais)
    print("")
    print("  DEUX PASSAGES FAUTIFS, ET LE CONTRÔLE S2 LES VOIT :")
    for a in mauvais:
        print("    %s" % a)
    print("")
    print("  LE PREMIER SAUTE LA PRIORISATION — un versement sans décision")
    print("  politique. LE SECOND FAIT DÉCLARER L'ADMISSIBILITÉ PHYSIQUE PAR")
    print("  L'AUTORITÉ DE QUALIFICATION : c'est exactement la confusion que")
    print("  A46 interdit et que le cas 7 exploitait.")
    return {"nominal": len(anomalies), "fautifs": len(mauvais)}


# =====================================================================
# CAS 1 — DÉLAI MAXIMAL DE SERVICE ET CALENDRIER PUBLIC
# =====================================================================
DELAI_MAX = 3


def calibrer(retenus, capacite, horizon=8):
    reste = dict((p.cle, p.demande) for p in retenus)
    calendrier = []
    for t in range(1, horizon + 1):
        dispo, servi = capacite, {}
        for p in retenus:
            if reste[p.cle] <= 0 or dispo <= 0:
                continue
            part = min(reste[p.cle], dispo)
            servi[p.cle] = part
            reste[p.cle] -= part
            dispo -= part
        calendrier.append({"t": t, "servi": servi,
                           "attente": sum(reste.values())})
        if sum(reste.values()) <= 1e-9:
            break
    return calendrier


def cas_1():
    titre(1, "ESSENTIEL AU-DELÀ DE LA CAPACITÉ — délai maximal, calendrier")
    essentiels = [PAR_CLE[c] for c in ("eau", "hopital", "logement")]
    demande = sum(p.demande for p in essentiels)
    print("  Demande essentielle %.0f. DÉLAI MAXIMAL ENGAGÉ : %d périodes."
          % (demande, DELAI_MAX))
    print("")
    print("  %-24s %10s %14s %16s"
          % ("capacité par période", "périodes", "délai tenu", "servi en t=1"))
    resultats = {}
    for capacite in (CAPACITE, 300.0):
        cal = calibrer(essentiels, capacite)
        n = len(cal)
        t1 = 100.0 * sum(cal[0]["servi"].values()) / demande
        resultats[capacite] = (n, n <= DELAI_MAX, t1)
        print("  %-24.0f %10d %14s %15.0f %%"
              % (capacite, n, "oui" if n <= DELAI_MAX else "NON", t1))
    print("")
    print("  CE QUE LE DÉLAI MAXIMAL APPORTE : IL REND A44 FALSIFIABLE. Sans")
    print("  lui, « la disponibilité est garantie » n'a pas de démenti")
    print("  possible — tout retard se lit comme un simple échelonnement.")
    print("  AVEC LUI, le second scénario est un MANQUEMENT PUBLIC : %d"
          % resultats[300.0][0])
    print("  périodes pour un engagement de %d." % DELAI_MAX)
    print("")
    print("  ET LE CALENDRIER DOIT ÊTRE PUBLIÉ D'AVANCE, sinon il se réécrit")
    print("  après coup et le délai ne contraint plus personne.")
    print("")
    print("  CE QUE CELA NE DIT TOUJOURS PAS : si l'échelonnement était")
    print("  NÉCESSAIRE. L'écart de capacité est une condition nécessaire et")
    print("  NON SUFFISANTE d'une tension sur les prix. Les prix ne sont pas")
    print("  endogènes ici, et aucun indicateur d'inflation n'est publié.")
    return {"large": resultats[CAPACITE], "serre": resultats[300.0]}


# =====================================================================
# CAS 2 — ARBITRAGE DE PORTEFEUILLE
# =====================================================================
# Des usages VRAIMENT concurrents : chacun tient seul, les trois ensemble
# dépassent le lithium disponible. C'est là que le veto projet par projet
# révèle son défaut, et ce n'est pas celui qu'annonçait la version 1.
CONCURRENTS = [
    Projet("solaire-p", "Parc solaire", 600, False, {"lithium": 40},
           {"carbone": -150, "biodiversite": 18}, rang_depot=1),
    Projet("eolien", "Parc éolien", 500, False, {"lithium": 35},
           {"carbone": -110, "biodiversite": 12}, rang_depot=2),
    Projet("stockage", "Stockage réseau", 300, False, {"lithium": 30},
           {"carbone": -60, "biodiversite": 5}, rang_depot=3),
    Projet("solaire-xxl", "Parc solaire surdimensionné", 900, False,
           {"lithium": 45}, {"carbone": -200, "biodiversite": 40},
           rang_depot=4),
]


def cas_2():
    titre(2, "RESSOURCE RARE — arbitrage entre usages concurrents")
    admis = [p for p in CONCURRENTS if veto_physique(p)[0]]
    lithium_admis = sum(p.ressources.get("lithium", 0.0) for p in admis)
    biodiv_admis = sum(max(0.0, p.frontieres.get("biodiversite", 0.0))
                       for p in admis)
    lots = portefeuilles_faisables(CONCURRENTS)
    meilleur = max(lots, key=lambda l: sum(p.soulage() for p in l))

    print("  Quatre usages se disputent le lithium (%.0f disponible) et la"
          % RESSOURCES["lithium"])
    print("  biodiversité (%.0f de budget)." % FRONTIERES["biodiversite"])
    print("")
    print("  %-13s %9s %13s %10s %14s"
          % ("projet", "lithium", "biodiversité", "soulage", "veto isolé"))
    for p in CONCURRENTS:
        ok, _ = veto_physique(p)
        print("  %-13s %9.0f %13.0f %10.0f %14s"
              % (p.cle, p.ressources.get("lithium", 0),
                 p.frontieres.get("biodiversite", 0), p.soulage(),
                 "admis" if ok else "refusé"))
    print("")
    print("  LE VETO PROJET PAR PROJET ADMET %d PROJETS. Leur lithium cumulé"
          % len(admis))
    print("  vaut %.0f pour %.0f disponible, et leur pression cumulée sur la"
          % (lithium_admis, RESSOURCES["lithium"]))
    print("  biodiversité %.0f pour %.0f de budget."
          % (biodiv_admis, FRONTIERES["biodiversite"]))
    print("")
    if lithium_admis > RESSOURCES["lithium"]:
        print("  CE QUE CELA MONTRE RENVERSE LA CONCLUSION DE LA VERSION 1. Le")
        print("  veto isolé n'est pas seulement trop strict : ICI IL EST TROP")
        print("  PERMISSIF. Il laisse passer un ensemble PHYSIQUEMENT")
        print("  IMPOSSIBLE, parce qu'aucun projet ne franchit seul ce que les")
        print("  trois franchissent ensemble.")
    print("")
    print("  ARBITRAGE DE PORTEFEUILLE : %d combinaisons faisables" % len(lots))
    for lot in sorted(lots, key=lambda l: -sum(p.soulage() for p in l)):
        print("      {%-34s} soulage %5.0f"
              % (", ".join(p.cle for p in lot),
                 sum(p.soulage() for p in lot)))
    print("")
    print("  LE PHYSIQUE NE CHOISIT PLUS UN PROJET, IL BORNE L'ENSEMBLE DES")
    print("  POSSIBLES — c'est la correction de l'auteur. Le meilleur lot")
    print("  soulage %.0f ; le pire faisable %.0f."
          % (sum(p.soulage() for p in meilleur),
             min(sum(p.soulage() for p in l) for l in lots)))
    print("")
    print("  ET LE CHOIX DANS CET ENSEMBLE RESTE POLITIQUE. Le programme")
    print("  n'ordonne pas les %d lots : le meilleur au carbone n'est pas le"
          % len(lots))
    print("  moindre à la biodiversité, et les classer exigerait de pondérer")
    print("  l'un contre l'autre — ce qu'aucune donnée physique ne fait.")
    print("")
    print("  CE QUE LE PORTEFEUILLE NE SAUVE PAS : %s franchit la"
          % PAR_CLE_CONCURRENTS["solaire-xxl"].cle)
    print("  biodiversité À LUI SEUL (%.0f pour %.0f) et n'appartient à aucun"
          % (PAR_CLE_CONCURRENTS["solaire-xxl"].frontieres["biodiversite"],
             FRONTIERES["biodiversite"]))
    print("  lot faisable. LE VETO GARDE SON RÔLE DE REFUS : l'arbitrage de")
    print("  portefeuille organise les possibles, il n'en crée aucun.")
    return {"admis_isoles": len(admis), "lithium_admis": lithium_admis,
            "lots": len(lots),
            "soulagement_meilleur": sum(p.soulage() for p in meilleur)}


PAR_CLE_CONCURRENTS = dict((p.cle, p) for p in CONCURRENTS)


# =====================================================================
# CAS 3 — PROCÉDURE DE DÉPARTAGE
# =====================================================================
def cas_3():
    titre(3, "DEUX BESOINS ESSENTIELS — procédure de départage")
    a, b = PAR_CLE["hopital"], PAR_CLE["logement"]
    retenus, saisine = prioriser([a, b], 400.0)
    print("  Enveloppe 400, demande 800. Le mécanisme ne classe pas.")
    print("")
    options = saisine.options()
    for regle in DEPARTAGES:
        print("    %-22s → %s" % (regle, options[regle]))
    distincts = sorted(set(options.values()))
    print("")
    print("  %d gagnants pour %d départages : AUCUNE RÈGLE NEUTRE N'EXISTE,"
          % (len(distincts), len(DEPARTAGES)))
    print("  et le corpus n'en invente pas.")
    print("")
    print("  CE QUE LA VERSION 1 LAISSAIT EN PLAN : un « indécidable » sans")
    print("  suite. CE QUE LA PROCÉDURE AJOUTE — et c'est la correction :")
    print("    instance saisie        %s" % saisine.instance)
    print("    majorité               %s" % saisine.majorite)
    print("    motif publié           %s" % ("oui" if saisine.motif_publie
                                             else "non"))
    print("    recours ouvert devant  %s" % saisine.recours)
    print("    sort du perdant        réexamen %s" % saisine.reexamen_du_perdant)
    print("")
    print("  LA PROCÉDURE NE DIT PAS QUI GAGNE, ET ELLE NE LE DOIT PAS. Elle")
    print("  rend la décision TRAÇABLE, MOTIVÉE, ATTAQUABLE ET REVUE. C'est")
    print("  tout ce qu'un mécanisme peut offrir sur une question politique,")
    print("  et c'est plus que rien — ce que la version 1 ne voyait pas.")
    return {"distincts": len(distincts), "retenus": len(retenus)}


# =====================================================================
# CAS 4 — VERSEMENTS PAR TRANCHES, GEL ET RESTITUTION
# =====================================================================
def cas_4():
    titre(4, "ERREUR DE QUALIFICATION — tranches, gel et restitution")
    p = Projet("errone", "Projet qualifié à tort", 960, True, {}, {},
               tranches=4)
    print("  Projet de %.0f versé en %d tranches de %.0f. Part d'une tranche"
          % (p.demande, p.tranches, p.demande / p.tranches))
    print("  déjà employée à la détection : %.0f %%."
          % (100 * PART_EMPLOYEE))
    print("")
    print("  %-20s %9s %11s %11s %10s %10s"
          % ("détection", "gelé", "restitué", "recouvré", "perdu", "sauvé"))
    res = {}
    for t in (1, 2, 3, 4, 6):
        for fraude in (False, True):
            g, r, rc, perdu = reprise(p, t, fraude=fraude)
            sauve = 100.0 * (g + r + rc) / p.demande
            res[(t, fraude)] = (g, r, rc, perdu, sauve)
            print("  %-20s %9.0f %11.0f %11.0f %10.0f %9.0f %%"
                  % ("t=%d, %s" % (t, "fraude" if fraude else "erreur"),
                     g, r, rc, perdu, sauve))
    print("")
    print("  LA VERSION 1 ÉCRIVAIT « ZÉRO RÉCUPÉRÉ », ET C'ÉTAIT FAUX. Non")
    print("  remboursable veut dire qu'un bénéficiaire CONFORME ne rembourse")
    print("  pas ; cela ne protège aucun bénéficiaire INDU. Détectée à la")
    print("  première tranche, l'erreur sauve %.0f %% ; à la quatrième, %.0f %%."
          % (res[(1, False)][4], res[(4, False)][4]))
    print("")
    print("  ET LE GEL N'EST PAS UNE RÉCUPÉRATION : c'est de l'argent JAMAIS")
    print("  VERSÉ, compté à part de ce qui revient. Les confondre gonflerait")
    print("  le rendement de la procédure.")
    print("")
    print("  CE QUI RESTE VRAI DE LA VERSION 1 : la part déjà EMPLOYÉE ne")
    print("  revient qu'incomplètement — %.0f %%, et seulement en cas de"
          % (100 * TAUX_RECOUVREMENT))
    print("  fraude établie. LA DÉTECTION PRÉCOCE VAUT DONC PLUS QUE TOUTE")
    print("  PROCÉDURE DE REPRISE, ce qui renvoie au cas 7.")
    return {"sauve_t1": res[(1, False)][4], "sauve_t4": res[(4, False)][4],
            "sauve_t4_fraude": res[(4, True)][4]}


# =====================================================================
# CAS 5 — RÉEXAMEN PÉRIODIQUE DES AUTORISATIONS
# =====================================================================
def cas_5(budget=400.0, pression=30.0, t_revision=6, horizon=12, pas=2):
    titre(5, "RÉVISION SCIENTIFIQUE — réexamen périodique des autorisations")
    total = pression * horizon
    print("  Programme RÉGULIÈREMENT ADMIS : %.0f de pression pour %.0f de"
          % (total, budget))
    print("  budget. La science révise à la période %d." % t_revision)
    print("")
    print("  %-14s %14s %13s %13s %12s"
          % ("révision", "réexamen", "pression fin", "dépassement", "gelées"))
    res = {}
    for taux in (0.40, 0.60):
        revise = budget * (1.0 - taux)
        for reexamen in (0, pas):
            if reexamen == 0:
                fin, gelees = total, 0
            else:
                t_arret = t_revision + reexamen
                fin = pression * min(horizon, t_arret)
                gelees = max(0, horizon - t_arret)
            dep = max(0.0, fin - revise)
            res[(taux, reexamen)] = (fin, dep, gelees)
            print("  %-14s %14s %13.0f %13.0f %12d"
                  % ("−%.0f %% → %.0f" % (100 * taux, revise)
                     if reexamen == 0 else "",
                     "aucun" if reexamen == 0 else "tous les %d" % reexamen,
                     fin, dep, gelees))
        print("")
    print("  L'AUTORISATION DEVIENT RÉVOCABLE, ET C'EST TOUTE LA DIFFÉRENCE.")
    print("  À −40 %%, le réexamen ramène le dépassement de %.0f à %.0f ; à"
          % (res[(0.40, 0)][1], res[(0.40, pas)][1]))
    print("  −60 %%, de %.0f à %.0f — SANS L'ANNULER."
          % (res[(0.60, 0)][1], res[(0.60, pas)][1]))
    print("")
    print("  CE QUI RÉSISTE : la pression DÉJÀ ÉMISE. Le passé n'est pas")
    print("  révisable et aucune procédure ne le rend tel. LE RÉEXAMEN BORNE")
    print("  LE DOMMAGE FUTUR, IL NE RÉPARE PAS LE PASSÉ.")
    print("")
    print("  ET IL A UN COÛT SYMÉTRIQUE : un financement révocable tous les")
    print("  %d périodes finance mal un ouvrage de %d. LE PAS DU RÉEXAMEN EST"
          % (pas, horizon))
    print("  UN ARBITRAGE, non un réglage technique, et il n'est pas tranché.")
    print("")
    print("  A44 RESTE RESTREINT : le second engagement vaut À LA DATE DE LA")
    print("  DÉCISION, révisable au réexamen suivant. Sans cette lecture, une")
    print("  révision scientifique ORDINAIRE le falsifie sans faute commise.")
    return dict((k, v[1]) for k, v in res.items())


# =====================================================================
# CAS 6 — RÉSERVE D'URGENCE À EXPIRATION AUTOMATIQUE
# =====================================================================
def cas_6(total=12000.0, part=0.15, inadmissible=0.30, expiration=4):
    titre(6, "URGENCE — réserve prédéfinie, expiration automatique")
    reserve = total * part
    hors_veto = reserve * inadmissible
    p = Projet("urgence", "Décaissement d'urgence", hors_veto, True, {}, {},
               tranches=4)
    print("  Émission totale %.0f. RÉSERVE PRÉDÉFINIE : %.0f %% soit %.0f,"
          % (total, 100 * part, reserve))
    print("  contournant les décisions 1 et 2. Part révélée inadmissible au")
    print("  contrôle rapide : %.0f %% soit %.0f."
          % (100 * inadmissible, hors_veto))
    print("")
    print("  %-40s %12s" % ("contrôle rapide à t=2", "montant"))
    g, r, rc, perdu = reprise(p, 2, fraude=False)
    print("  %-40s %12.0f" % ("gelé — jamais versé", g))
    print("  %-40s %12.0f" % ("restitué — versé, non employé", r))
    print("  %-40s %12.0f" % ("perdu — employé, hors fraude", perdu))
    sauve = 100.0 * (g + r) / hors_veto
    print("  %-40s %11.0f %%" % ("part sauvée", sauve))
    print("")
    print("  TROIS PROPRIÉTÉS, ET AUCUNE N'EST FACULTATIVE. La réserve est")
    print("  PRÉDÉFINIE — sinon elle se redéfinit à chaque urgence. Elle")
    print("  EXPIRE au bout de %d périodes — sinon elle devient un second"
          % expiration)
    print("  guichet permanent sans veto. Et le contrôle a posteriori est")
    print("  RAPIDE, parce que le versement par tranches ne sauve que ce qui")
    print("  n'est pas encore parti.")
    print("")
    print("  CE QUE CELA NE FERME PAS. %.0f échappent au veto physique PAR"
          % reserve)
    print("  CONSTRUCTION, et c'est le but même de la réserve. Le plafond")
    print("  reste un NOMBRE POLITIQUE : trop bas il laisse mourir, trop haut")
    print("  il vide le veto. AUCUN CALCUL NE LE FIXE.")
    return {"reserve": reserve, "hors_veto": hors_veto, "sauve": sauve}


# =====================================================================
# CAS 7 — MESURE EXTÉRIEURE, AUDIT INDÉPENDANT, RECOURS
# =====================================================================
def cas_7():
    titre(7, "CAPTURE DE L'AUTORITÉ — mesure extérieure et audit indépendant")
    charbon = PAR_CLE["charbon"]
    vraie = charbon.frontieres["carbone"]
    seuil = FRONTIERES["carbone"]

    print("  LA VERSION 1 CONCLUAIT QUE CELA « NE SE RÉPARE PAS ». C'ÉTAIT")
    print("  FAUX. La capture ne s'élimine pas avec certitude ; elle se")
    print("  DÉTECTE et se RÉDUIT. Trois leviers, et ils sont mesurés.")

    print("")
    print("  LEVIER 1 — LA PLURALITÉ DES MESUREURS, ET CE QU'ELLE VAUT")
    print("  Pression vraie %.0f, budget %.0f. Combien de captures — organismes"
          % (vraie, seuil))
    print("  ET INSTRUMENTS DE RECOURS confondus — faut-il pour lever le veto ?")
    print("")
    print("  LE RECOURS N'EST PLUS UN ORACLE. La version précédente lui rendait")
    print("  la valeur VRAIE dès que la divergence dépassait le seuil : il")
    print("  possédait gratuitement ce qu'aucun dispositif réel ne possède, et")
    print("  le résultat publié en tirait toute sa robustesse. IL EST DÉSORMAIS")
    print("  UN CANAL DE MESURE INDÉPENDANT — dont l'information ne passe ni par")
    print("  la déclaration du porteur ni par les modèles des organismes. CE")
    print("  N'EST PAS UNE OBSERVATION DIRECTE DE LA VÉRITÉ : un satellite, un")
    print("  capteur, une analyse matière dépendent d'un étalonnage, d'un")
    print("  traitement et parfois d'un modèle. AUCUN INSTRUMENT NE POSSÈDE LA")
    print("  VÉRITÉ — il a sa méthode, sa marge d'erreur et son risque propre.")
    print("")
    print("  %-22s %10s %8s %30s"
          % ("règle de constat", "captures", "à tort", "cibles minimales"))
    banc = [Projet("b%d" % k, "banc", 100, False, {},
                   {"carbone": float(v)}, rang_depot=k)
            for k, v in enumerate((300, 340, 370, 380, 390), start=1)]
    besoins, faux, cibles = {}, {}, {}
    for regle in REGLES_DE_VETO:
        k, quoi = captures_necessaires(vraie, seuil, regle)
        besoins[regle], cibles[regle] = k, quoi
        n = len([p for p in banc
                 if not infaisable_reellement(p)
                 and not veto_physique(p, regle=regle)[0]])
        faux[regle] = n
        print("  %-22s %10s %8d %30s"
              % (regle, "aucune" if k == 0 else
                 ("%d" % k if k is not None else "impossible"), n,
                 ", ".join(quoi) if quoi else "—"))

    print("")
    print("  ET LE RÉSULTAT PUBLIÉ HIER TOMBE. « Médiane avec recours » exigeait")
    print("  cinq captures tant que le recours était infaillible ; avec un")
    print("  instrument réel il en exige %s — %s. UN RECOURS À INSTRUMENT"
          % (besoins["mediane_avec_recours"],
             ", ".join(cibles["mediane_avec_recours"] or [])))
    print("  UNIQUE DÉPLACE LE POINT DE DÉFAILLANCE, IL NE LE SUPPRIME PAS :")
    print("  capter un organisme fait diverger, et capter l'instrument saisi")
    print("  suffit ensuite à museler l'alarme.")
    print("")
    print("  CE QUI LE RÉTABLIT EN PARTIE : PLURALISER LE RECOURS LUI-MÊME.")
    print("  Avec %d instruments indépendants en médiane, il faut %s captures"
          % (len(INSTRUMENTS_DE_RECOURS), besoins["recours_pluriel"]))
    print("  au lieu de %s, sans aucun refus à tort — contre %d pour la règle"
          % (besoins["mediane_avec_recours"], faux["prudente"]))
    print("  prudente, qui reste la plus résistante (%s) au prix de ces refus."
          % besoins["prudente"])
    print("")
    print("  LE DILEMME DE L'AUTEUR N'EST DONC PAS LEVÉ, IL EST DÉPLACÉ D'UN")
    print("  CRAN : la pluralité protège tant qu'elle porte AUSSI sur les")
    print("  canaux du recours, et le désaccord ne sert d'alarme que si ce")
    print("  qu'il déclenche n'est pas capturable d'un seul coup.")
    print("")
    print("  ET IL FAUT LIRE CES NOMBRES POUR CE QU'ILS SONT. LE NOMBRE MINIMAL")
    print("  DE CAPTURES EST UNE PROPRIÉTÉ STRUCTURELLE DE L'ARCHITECTURE")
    print("  SIMULÉE. IL NE MESURE NI LA PROBABILITÉ D'UNE CAPTURE NI SON COÛT.")
    print("  Corrompre deux organismes scientifiques indépendants peut être")
    print("  bien plus difficile que compromettre cinq capteurs de même")
    print("  modèle, ou bien plus facile — le programme n'en sait rien et ne")
    print("  prétend pas le savoir. Ce qu'il compare, ce sont des ARCHITECTURES")
    print("  à effort de capture supposé égal, ce qu'aucun dispositif réel ne")
    print("  garantit.")

    print("")
    print("  LEVIER 2 — LA MESURE PHYSIQUE DIRECTE ET L'AUDIT ALÉATOIRE")
    declaree = vraie * (1.0 - CAPTURE_AMPLEUR)
    print("  L'autorité déclare %.0f au lieu de %.0f, soit %.0f %% d'écart."
          % (declaree, vraie, 100 * (1 - declaree / vraie)))
    print("")
    print("  %-30s %14s %18s"
          % ("canal", "détecté en", "part des projets"))
    for etiquette, couverture, alerte in (
            ("canal de mesure indépendant", True, False),
            ("audit aléatoire seul", False, False),
            ("alerte", False, True)):
        t, _ = detecter(vraie, declaree, charbon.rang_depot, couverture, alerte)
        part = COUVERTURE_PHYSIQUE if couverture else 1.0
        print("  %-30s %14s %16.0f %%"
              % (etiquette, "t=%d" % t if t else "jamais", 100 * part))

    print("")
    print("  LEVIER 3 — CE QUE LA DÉTECTION RÉCUPÈRE, GRÂCE AUX TRANCHES")
    print("  %-24s %9s %11s %11s %10s"
          % ("détection", "gelé", "restitué", "recouvré", "sauvé"))
    sauves = {}
    for t, etiquette in ((1, "canal indépendant"), (3, "audit, 1er tour"),
                         (6, "audit, 2e tour")):
        g, r, rc, _ = reprise(charbon, t, fraude=True)
        sauves[t] = 100.0 * (g + r + rc) / charbon.demande
        print("  %-24s %9.0f %11.0f %11.0f %9.0f %%"
              % ("t=%d, %s" % (t, etiquette), g, r, rc, sauves[t]))

    print("")
    print("  RÉSULTAT CORRIGÉ : DÉTECTABLE ET RÉDUCTIBLE, NON ÉLIMINABLE. Sur")
    print("  les %.0f détournés, le canal indépendant en sauve %.0f %% et l'audit"
          % (charbon.demande, sauves[1]))
    print("  tardif %.0f %%. LA DÉTECTION PRÉCOCE EST LE LEVIER, non la"
          % sauves[6])
    print("  procédure de reprise.")
    print("")
    print("  CE QUI RESTE VRAI DE LA VERSION 1, ET SEULEMENT CELA : un")
    print("  contrôle QUI NE PORTE QUE SUR DES DÉCLARATIONS ne détecte pas")
    print("  leur falsification. C'est pourquoi les trois leviers sont")
    print("  EXTÉRIEURS à la déclaration, et pourquoi A46 sépare le pouvoir de")
    print("  mesurer de celui de qualifier et de verser.")
    print("")
    print("  CE QUI N'EST PAS RÉSOLU. La capture de l'ORGANE DE MESURE")
    print("  lui-même, la collusion entre organismes, et le fait que %.0f %%"
          % (100 * (1 - COUVERTURE_PHYSIQUE)))
    print("  des projets ne sont couverts par aucune mesure directe. ET LE")
    print("  LANCEUR D'ALERTE N'EST PAS UN MÉCANISME : c'est un paramètre ici,")
    print("  et le programme ne prétend pas le produire.")
    return {"besoins": besoins, "faux": faux, "sauve_direct": sauves[1],
            "sauve_tardif": sauves[6]}


# =====================================================================
def main():
    print("=" * 78)
    print("LA RÈGLE D'ÉMISSION DE NEMO IMS — VERSION 2")
    print("=" * 78)
    print("Quatre conclusions de la version 1 étaient trop fortes ; elles sont")
    print("corrigées, et les corrections changent la conception. LA CONTRAINTE")
    print("PHYSIQUE reste infranchissable ; SON CONSTAT est incertain,")
    print("révisable et attaquable — et c'est là que tout se joue.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ. Les projets sont fictifs.")

    r = {}
    r["A46"] = separation()
    r["etats"] = processus()
    r[1], r[2], r[3] = cas_1(), cas_2(), cas_3()
    r[4], r[5] = cas_4(), cas_5()
    r[6], r[7] = cas_6(), cas_7()

    print("")
    print("=" * 78)
    print("CE QUE LES MÉCANISMES RATTRAPENT, ET CE QU'ILS LAISSENT")
    print("=" * 78)
    bilan = [
        (1, "délai maximal et calendrier public",
         "la promesse A44 devient FALSIFIABLE : %d périodes contre %d engagées"
         % (r[1]["serre"][0], DELAI_MAX),
         "le caractère nécessaire de l'échelonnement reste indémontré"),
        (2, "arbitrage de portefeuille",
         "le veto isolé admettait %d projets pour %.0f de lithium sur %.0f ; "
         "le portefeuille borne à %d lots, le meilleur soulageant %.0f"
         % (r[2]["admis_isoles"], r[2]["lithium_admis"], RESSOURCES["lithium"],
            r[2]["lots"], r[2]["soulagement_meilleur"]),
         "le choix entre les %d lots faisables reste politique" % r[2]["lots"]),
        (3, "procédure de départage",
         "saisine nommée, motif publié, recours ouvert, réexamen daté",
         "le critère de fond n'existe pas, et il ne doit pas exister"),
        (4, "tranches, gel et restitution",
         "%.0f %% sauvés en détection à t=1, %.0f %% à t=4"
         % (r[4]["sauve_t1"], r[4]["sauve_t4"]),
         "la part employée ne revient qu'en cas de fraude établie"),
        (5, "réexamen périodique des autorisations",
         "dépassement ramené de %.0f à %.0f à −40 %%"
         % (r[5][(0.40, 0)], r[5][(0.40, 2)]),
         "le passé n'est pas révisable, et le pas du réexamen a un coût"),
        (6, "réserve prédéfinie à expiration automatique",
         "%.0f %% du montant hors veto sauvé au contrôle rapide" % r[6]["sauve"],
         "le plafond reste un nombre politique qu'aucun calcul ne fixe"),
        (7, "pluralité, mesure directe, audit indépendant",
         "%.0f %% récupérés en détection précoce contre %.0f %% en détection "
         "tardive ; la pluralité du recours porte la capture nécessaire de "
         "%s à %s" % (r[7]["sauve_direct"], r[7]["sauve_tardif"],
                      r[7]["besoins"]["mediane_avec_recours"],
                      r[7]["besoins"]["recours_pluriel"]),
         "un recours à instrument UNIQUE ne coûte que %s captures ; la "
         "collusion unanime reste hors d'atteinte"
         % r[7]["besoins"]["mediane_avec_recours"]),
    ]
    for n, mecanisme, gain, reste in bilan:
        print("")
        print("  CAS %d — %s" % (n, mecanisme))
        print("      RATTRAPÉ : %s" % gain)
        print("      RESTE    : %s" % reste)

    print("")
    print("  LA VERSION 1 CONCLUAIT DEUX FOIS TROP FORT, dans le sens de")
    print("  l'impuissance : « le cas 7 ne se répare pas » et « une émission")
    print("  sans dette n'a aucune reprise » étaient FAUX.")
    print("")
    print("  ET LA VERSION 2 A CONCLU TROP FORT DANS L'AUTRE SENS. Elle donnait")
    print("  au recours la valeur VRAIE par construction, et en tirait une")
    print("  robustesse de cinq captures là où un instrument réel en coûte %s."
          % r[7]["besoins"]["mediane_avec_recours"])
    print("  L'auteur l'a relevé le jour même. UN CORPUS QUI CHERCHE LES ÉCHECS")
    print("  PEUT EN INVENTER, ET UN CORPUS QUI LES CORRIGE PEUT SE PAYER DE")
    print("  SA PROPRE CORRECTION : les deux fautes sont symétriques et aucune")
    print("  n'est vénielle.")
    print("")
    print("  CE QUI N'A PAS BOUGÉ. Un contrôle qui ne porte que sur des")
    print("  déclarations ne détecte pas leur falsification. Le passé n'est")
    print("  pas révisable. Aucun critère neutre ne départage deux besoins")
    print("  essentiels. ET LA CONTRAINTE PHYSIQUE NE SE VOTE PAS, alors que")
    print("  son constat, lui, se conteste — c'est la distinction qui commande")
    print("  toute l'architecture, et le dilemme qui reste ouvert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
