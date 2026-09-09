#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LA RÈGLE D'ÉMISSION DE NEMO IMS — ET SES SEPT CAS LIMITES. 2026-09-09.

CE QUE CE PROGRAMME FAIT : il implémente la règle d'émission à TROIS DÉCISIONS
SÉPARÉES posée par l'auteur, puis la soumet aux sept cas limites qu'il a
nommés. Chaque cas produit un résultat défini. PLUSIEURS MONTRENT LA RÈGLE EN
ÉCHEC, et c'est la raison d'être du programme.

CE QU'IL NE FAIT PAS : il ne valide pas la règle. Un programme qui applique
une règle prouve qu'il l'applique, jamais qu'elle est fondée. Aucun seuil n'est
calibré, et les projets sont fictifs.

LES TROIS DÉCISIONS, ET ELLES NE DOIVENT PAS SE MÉLANGER

  (1) VETO PHYSIQUE — refus seulement, jamais autorisation. Deux tests, aucune
      agrégation : la ressource est-elle DISPONIBLE au rythme demandé, et le
      projet FRANCHIT-IL à lui seul une limite reconnue ? Le veto répond « est-ce
      possible », jamais « est-ce souhaitable ».

  (2) PRIORITÉ DÉMOCRATIQUE — parmi les projets admissibles, le classement
      appartient aux institutions politiques. LE MÉCANISME REFUSE DE CLASSER
      DEUX BESOINS ESSENTIELS ENTRE EUX, et le cas 3 montre pourquoi : les
      départages possibles ne donnent pas le même gagnant, donc choisir le
      départage EST la décision politique.

  (3) CALIBRAGE MONÉTAIRE — montant et calendrier selon la capacité réelle.
      IL ÉCHELONNE, IL NE REFUSE PAS : un calibrage qui refuse au fond
      redonnerait à l'autorité monétaire le pouvoir que NEMO lui retire.

LE POUVOIR D'ARRÊT — trois arrêts, trois titulaires, trois portées. Un seul est
inconditionnel. Voir ARRETS, et le cas 7 pour ce qu'aucun d'eux n'attrape.

CE PROGRAMME NE MODÉLISE PAS L'INFLATION. Les prix n'y sont pas endogènes. Il
publie un ÉCART DE CAPACITÉ, qui est une condition NÉCESSAIRE et NON SUFFISANTE
d'une tension inflationniste. Le cas 1 le dit à l'endroit où cela compte.

USAGE :  python modeles/nemo_emission.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SEUILS_CALIBRES = False

# ---------------------------------------------------------------------
# Le monde physique. Budgets restants et flux disponibles par période.
# ---------------------------------------------------------------------
FRONTIERES = {"carbone": 400.0, "biodiversite": 30.0, "eau": 120.0}
RESSOURCES = {"lithium": 100.0, "cuivre": 400.0, "travail": 1000.0}
CAPACITE = 1000.0          # capacité réelle mobilisable par période


class Projet(object):
    """Un projet candidat au financement. « essentiel » est une QUALIFICATION,
    portée par une autorité nommée — c'est ce que le cas 7 attaque."""

    def __init__(self, cle, libelle, demande, essentiel, ressources,
                 frontieres, beneficiaires=0, gravite=0, rang_depot=0,
                 qualifie_par="autorite-de-qualification"):
        self.cle = cle
        self.libelle = libelle
        self.demande = float(demande)
        self.essentiel = bool(essentiel)
        self.ressources = dict(ressources)
        self.frontieres = dict(frontieres)   # + = pression, - = soulagement
        self.beneficiaires = beneficiaires
        self.gravite = gravite               # 0 à 3, déclarée
        self.rang_depot = rang_depot
        self.qualifie_par = qualifie_par

    def soulage(self):
        return -sum(v for v in self.frontieres.values() if v < 0)

    def pese(self):
        return sum(v for v in self.frontieres.values() if v > 0)


# Ce que l'autorité captée DÉCLARE au cas 7 — sous le budget, donc verte.
DECLARATION_CAPTUREE = 340.0

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


# ---------------------------------------------------------------------
# (1) LE VETO PHYSIQUE — refus seulement, et sans agrégation
# ---------------------------------------------------------------------
def veto_physique(projet, frontieres=None, ressources=None, agregation=False):
    """Rend (admissible, motif).

    SANS AGRÉGATION, c'est un test de POSSIBILITÉ : aucune comparaison entre
    une limite et une autre n'y est faite, donc aucune pondération politique
    n'y est cachée. AVEC AGRÉGATION — variante mesurée au cas 2 seulement — le
    veto compare un soulagement à une pression, ce qui EXIGE une pondération
    QUI N'EST PAS PHYSIQUE. Le programme mesure les deux et n'en choisit aucune.
    """
    f = FRONTIERES if frontieres is None else frontieres
    r = RESSOURCES if ressources is None else ressources

    for nom, besoin in sorted(projet.ressources.items()):
        if besoin > r.get(nom, 0.0):
            return False, ("indisponible : %s, %.0f demandés pour %.0f "
                           "disponibles" % (nom, besoin, r.get(nom, 0.0)))

    if agregation:
        if projet.pese() - projet.soulage() > 0:
            return False, ("bilan agrégé défavorable : %+.0f"
                           % (projet.pese() - projet.soulage()))
        return True, "bilan agrégé favorable"

    for nom, effet in sorted(projet.frontieres.items()):
        if effet > 0 and effet > f.get(nom, 0.0):
            return False, ("franchissement : %s, pression %.0f pour %.0f "
                           "de budget restant" % (nom, effet, f.get(nom, 0.0)))
    return True, "admissible"


# ---------------------------------------------------------------------
# (2) LA PRIORITÉ — et le refus de classer
# ---------------------------------------------------------------------
DEPARTAGES = ("cout_par_beneficiaire", "nombre", "gravite", "anteriorite")


def departager(projets, regle):
    """Applique UN départage. Aucun n'est le bon : c'est le point du cas 3."""
    if regle == "cout_par_beneficiaire":
        cle = lambda p: (p.demande / p.beneficiaires) if p.beneficiaires else 1e9
        return sorted(projets, key=cle)
    if regle == "nombre":
        return sorted(projets, key=lambda p: -p.beneficiaires)
    if regle == "gravite":
        return sorted(projets, key=lambda p: -p.gravite)
    if regle == "anteriorite":
        return sorted(projets, key=lambda p: p.rang_depot)
    raise ValueError(regle)


def prioriser(admissibles, enveloppe):
    """Rend (retenus, indecidable, motif).

    LE MÉCANISME NE CLASSE PAS DEUX ESSENTIELS ENTRE EUX. Il sert d'abord les
    essentiels s'ils tiennent tous ; si l'enveloppe ne suffit pas, il rend la
    main. Le non-essentiel, lui, cède toujours devant l'essentiel : cela n'est
    pas un arbitrage entre besoins, c'est la qualification elle-même.
    """
    essentiels = [p for p in admissibles if p.essentiel]
    autres = [p for p in admissibles if not p.essentiel]
    besoin = sum(p.demande for p in essentiels)

    if besoin > enveloppe and len(essentiels) > 1:
        return [], True, ("%d besoins essentiels pour %.0f d'enveloppe et "
                          "%.0f de demande" % (len(essentiels), enveloppe,
                                               besoin))

    retenus = list(essentiels)
    reste = enveloppe - besoin
    for p in departager(autres, "anteriorite"):
        if p.demande <= reste:
            retenus.append(p)
            reste -= p.demande
    return retenus, False, "servis sans classer d'essentiels entre eux"


# ---------------------------------------------------------------------
# (3) LE CALIBRAGE — il échelonne, il ne refuse pas
# ---------------------------------------------------------------------
def calibrer(retenus, capacite=None, horizon=4):
    """Rend (echeancier, ecart_de_capacite).

    L'ÉCART DE CAPACITÉ N'EST PAS UNE MESURE D'INFLATION. C'est la part de la
    demande qui excède la capacité réelle sur la période — condition nécessaire,
    non suffisante, d'une tension sur les prix. Les prix ne sont pas endogènes
    ici et le programme n'en publiera pas.
    """
    cap = CAPACITE if capacite is None else capacite
    reste = dict((p.cle, p.demande) for p in retenus)
    ecart_initial = max(0.0, sum(reste.values()) - cap)
    echeancier = []
    for t in range(1, horizon + 1):
        dispo = cap
        servi = {}
        for p in retenus:
            if reste[p.cle] <= 0 or dispo <= 0:
                continue
            part = min(reste[p.cle], dispo)
            servi[p.cle] = part
            reste[p.cle] -= part
            dispo -= part
        echeancier.append({"t": t, "servi": servi,
                           "en_attente": sum(reste.values())})
        if sum(reste.values()) <= 1e-9:
            break
    return echeancier, ecart_initial


# ---------------------------------------------------------------------
# LE POUVOIR D'ARRÊT
# ---------------------------------------------------------------------
ARRETS = [
    {"cle": "physique",
     "titulaire": "organe d'observation des limites",
     "motif": "franchissement d'une limite reconnue ou ressource indisponible",
     "portee": "INCONDITIONNEL — non surmontable par une majorité politique, "
               "sans quoi ce n'est pas un veto",
     "revocable_par": None},
    {"cle": "democratique",
     "titulaire": "institution politique compétente",
     "motif": "changement de priorité",
     "portee": "BORNÉ — ne reprend pas une émission non remboursable déjà "
               "délivrée ; ne porte que sur les tranches à venir",
     "revocable_par": "élection ou vote contraire"},
    {"cle": "monetaire",
     "titulaire": "organe de calibrage",
     "motif": "capacité réelle saturée",
     "portee": "DÉLAI SEULEMENT — un arrêt monétaire au fond rendrait à la "
               "monnaie le pouvoir que NEMO lui retire",
     "revocable_par": "retour de capacité"},
]


def qui_peut_arreter(motif):
    return [a["cle"] for a in ARRETS if motif in a["motif"]]


# ---------------------------------------------------------------------
# Le passage complet, et ses contrôles
# ---------------------------------------------------------------------
class Passage(object):
    def __init__(self):
        self.refuses = []          # (projet, motif)
        self.retenus = []
        self.indecidable = False
        self.motif_indecidable = ""
        self.echeancier = []
        self.ecart = 0.0
        self.emis = {}
        self.cumuls = {}
        self.anomalies = []


def passer(catalogue, enveloppe=None, capacite=None, frontieres=None,
           agregation=False):
    """Un cycle complet : veto, priorité, calibrage. Les contrôles E1 à E5
    sont vérifiés à la sortie — et le cas 7 montre qu'ils peuvent TOUS passer
    au vert pendant que l'émission est détournée."""
    p = Passage()
    admissibles = []
    for pr in catalogue:
        ok, motif = veto_physique(pr, frontieres=frontieres,
                                  agregation=agregation)
        (admissibles if ok else p.refuses).append(pr if ok else (pr, motif))

    env = sum(x.demande for x in admissibles) if enveloppe is None else enveloppe
    p.retenus, p.indecidable, p.motif_indecidable = prioriser(admissibles, env)
    if p.indecidable:
        return p

    p.echeancier, p.ecart = calibrer(p.retenus, capacite=capacite)
    for etape in p.echeancier:
        for cle, montant in etape["servi"].items():
            p.emis[cle] = p.emis.get(cle, 0.0) + montant

    # E1 — aucun projet refusé au titre physique ne reçoit d'émission.
    for pr, motif in p.refuses:
        if p.emis.get(pr.cle, 0.0) > 0:
            p.anomalies.append("[E1] %s a été refusé (%s) et pourtant financé"
                               % (pr.cle, motif))
    # E2 — aucune période ne dépasse la capacité.
    cap = CAPACITE if capacite is None else capacite
    for etape in p.echeancier:
        total = sum(etape["servi"].values())
        if total > cap + 1e-9:
            p.anomalies.append("[E2] période %d : %.0f émis pour %.0f de "
                               "capacité" % (etape["t"], total, cap))
    # E3 — l'émission délivrée n'est jamais reprise.
    for cle, montant in p.emis.items():
        if montant < 0:
            p.anomalies.append("[E3] %s : émission négative, donc reprise "
                               "d'une émission non remboursable" % cle)
    # E4 — le mécanisme n'a classé aucun essentiel devant un autre.
    servis = [x for x in p.retenus if x.essentiel]
    demandes = [x for x in admissibles if x.essentiel]
    if len(servis) != len(demandes):
        p.anomalies.append("[E4] %d essentiels admissibles, %d retenus : le "
                           "mécanisme a classé" % (len(demandes), len(servis)))
    # E5 — LA PRESSION CUMULÉE des projets financés, contre le budget reconnu.
    # Sans ce contrôle, mille projets franchissent ensemble ce qu'aucun ne
    # franchit seul. Les soulagements ne compensent pas : ce serait agréger.
    f = FRONTIERES if frontieres is None else frontieres
    for nom in sorted(f):
        cumul = sum(max(0.0, x.frontieres.get(nom, 0.0)) for x in p.retenus)
        p.cumuls[nom] = cumul
        if cumul > f[nom] + 1e-9:
            p.anomalies.append("[E5] %s : pression cumulée %.0f pour %.0f de "
                               "budget reconnu" % (nom, cumul, f[nom]))
    return p


# =====================================================================
# LES SEPT CAS LIMITES
# =====================================================================
def titre(n, libelle):
    print("")
    print("=" * 78)
    print("CAS %d — %s" % (n, libelle))
    print("=" * 78)


def cas_1():
    """PROJET ESSENTIEL MAIS INFLATIONNISTE."""
    titre(1, "UN PROJET ESSENTIEL QUI EXCÈDE LA CAPACITÉ RÉELLE")
    essentiels = [PAR_CLE[c] for c in ("eau", "hopital", "logement")]
    demande = sum(p.demande for p in essentiels)
    ech, ecart = calibrer(essentiels, capacite=CAPACITE)

    print("  Trois projets essentiels admissibles, %.0f demandés pour %.0f de"
          % (demande, CAPACITE))
    print("  capacité par période. LE CALIBRAGE ÉCHELONNE, IL NE REFUSE PAS.")
    print("")
    for e in ech:
        print("    période %d : %.0f émis, %.0f encore en attente"
              % (e["t"], sum(e["servi"].values()), e["en_attente"]))
    periodes = len(ech)
    t1 = 100.0 * sum(ech[0]["servi"].values()) / demande
    print("")
    print("  RÉSULTAT : le besoin est servi à %.0f %% à la première période et"
          % t1)
    print("  intégralement à la %de. L'écart de capacité initial vaut %.0f."
          % (periodes, ecart))
    print("")
    print("  CE QUE CELA FAIT À LA PROMESSE A44. « Garantir la disponibilité")
    print("  du financement » ne peut pas vouloir dire « immédiatement » : la")
    print("  règle tient la promesse SUR LA FENÊTRE, pas à la date. Si A44 se")
    print("  lit comme un engagement de délai, LE CAS 1 LA FALSIFIE.")
    print("")
    print("  ET CE QUE LE PROGRAMME NE DIT PAS : que l'échelonnement était")
    print("  nécessaire. Un écart de capacité est une condition NÉCESSAIRE et")
    print("  NON SUFFISANTE d'une tension sur les prix. Les prix ne sont pas")
    print("  endogènes ici, et aucun indicateur d'inflation n'est publié.")
    return {"periodes": periodes, "taux_t1": t1, "ecart": ecart}


def cas_2():
    """PROJET ÉCOLOGIQUE DÉPENDANT D'UNE RESSOURCE RARE."""
    titre(2, "UN PROJET ÉCOLOGIQUE QUI DÉPEND D'UNE RESSOURCE RARE")
    verts = [PAR_CLE["solaire"], PAR_CLE["hydrogene"], PAR_CLE["logement"]]
    print("  %-11s %10s %10s   %s" % ("projet", "soulage", "pèse", "veto STRICT"))
    strict, agrege = [], []
    for p in verts:
        ok, motif = veto_physique(p)
        oka, _ = veto_physique(p, agregation=True)
        (strict if ok else []).append(p)
        (agrege if oka else []).append(p)
        print("  %-11s %10.0f %10.0f   %s"
              % (p.cle, p.soulage(), p.pese(), "admis" if ok else motif))

    print("")
    print("  DEUX MOTIFS DE REFUS DIFFÉRENTS, ET IL FAUT LES SÉPARER.")
    print("  L'hydrogène est refusé parce que le lithium N'EXISTE PAS au")
    print("  rythme demandé : c'est une impossibilité, et aucune délibération")
    print("  ne la lève. Le solaire est refusé parce qu'il FRANCHIT une limite")
    print("  qu'il ne compense pas : c'est un arbitrage, et il n'appartient")
    print("  pas au veto.")
    print("")
    print("  VETO STRICT : %d projet(s) sur %d admis, %.0f de soulagement"
          % (len(strict), len(verts), sum(p.soulage() for p in strict)))
    print("  VETO AGRÉGÉ : %d projet(s) sur %d admis, %.0f de soulagement"
          % (len(agrege), len(verts), sum(p.soulage() for p in agrege)))
    print("")
    print("  RÉSULTAT, ET C'EST UN DILEMME, NON UNE SOLUTION. Appliqué")
    print("  strictement, le veto physique BLOQUE LA TRANSITION qu'il est")
    print("  censé protéger : il refuse %.0f de soulagement carbone pour %.0f"
          % (PAR_CLE["solaire"].soulage(), PAR_CLE["solaire"].pese()))
    print("  de pression sur la biodiversité. Appliqué en bilan, il admet le")
    print("  projet — MAIS SEULEMENT PARCE QU'IL A PONDÉRÉ UNE LIMITE CONTRE")
    print("  UNE AUTRE, ce qu'aucune donnée physique ne fait. LA VARIANTE")
    print("  AGRÉGÉE N'EST DONC PAS UN VETO PHYSIQUE : c'est une décision")
    print("  politique déguisée en mesure. Le programme mesure les deux et")
    print("  N'EN CHOISIT AUCUNE — l'arbitrage est ouvert.")
    return {"strict": len(strict), "agrege": len(agrege),
            "soulagement_perdu": sum(p.soulage() for p in verts
                                     if p in agrege and p not in strict)}


def cas_3():
    """CONFLIT ENTRE DEUX BESOINS ESSENTIELS."""
    titre(3, "DEUX BESOINS ESSENTIELS, UNE SEULE ENVELOPPE")
    a, b = PAR_CLE["hopital"], PAR_CLE["logement"]
    enveloppe = 400.0
    retenus, indecidable, motif = prioriser([a, b], enveloppe)

    print("  %s (%.0f, %d bénéficiaires, gravité %d, déposé %d)"
          % (a.libelle, a.demande, a.beneficiaires, a.gravite, a.rang_depot))
    print("  %s (%.0f, %d bénéficiaires, gravité %d, déposé %d)"
          % (b.libelle, b.demande, b.beneficiaires, b.gravite, b.rang_depot))
    print("  Enveloppe : %.0f. Les deux ne tiennent pas." % enveloppe)
    print("")
    print("  LE MÉCANISME REND : %s"
          % ("INDÉCIDABLE — " + motif if indecidable else "un classement"))
    print("")
    print("  ET VOICI POURQUOI IL DOIT LE RENDRE. Quatre départages plausibles,")
    print("  quatre applications, et ILS NE DÉSIGNENT PAS LE MÊME GAGNANT :")
    print("")
    gagnants = {}
    for regle in DEPARTAGES:
        g = departager([a, b], regle)[0]
        gagnants[regle] = g.cle
        print("    %-22s → %s" % (regle, g.libelle))
    distincts = sorted(set(gagnants.values()))
    print("")
    print("  %d gagnants distincts sur %d départages. LE CHOIX DU DÉPARTAGE"
          % (len(distincts), len(DEPARTAGES)))
    print("  EST DONC LA DÉCISION ELLE-MÊME, et il est politique. Une règle")
    print("  qui trancherait ici ne lèverait pas le conflit : elle imposerait")
    print("  silencieusement une théorie du besoin — utilitariste pour le coût")
    print("  par bénéficiaire, agrégative pour le nombre, hiérarchique pour la")
    print("  gravité, arbitraire pour l'antériorité.")
    print("")
    print("  RÉSULTAT : INDÉCIDABLE PAR LE MÉCANISME. C'est un échec de la")
    print("  règle en tant que règle, et c'est le bon comportement. CE QUE")
    print("  NEMO DOIT ALORS FOURNIR N'EST PAS UN CRITÈRE MAIS UNE PROCÉDURE :")
    print("  quel organe tranche, à quelle majorité, sous quel recours, et")
    print("  avec quelle publicité du motif. Cette procédure n'existe pas")
    print("  encore.")
    return {"indecidable": indecidable, "gagnants": gagnants,
            "distincts": len(distincts)}


def cas_4(taux_erreur=0.08, periodes=12, envelope=1000.0):
    """ERREUR DE QUALIFICATION."""
    titre(4, "UNE ERREUR DE QUALIFICATION, DÉCOUVERTE APRÈS L'ÉMISSION")
    emis_total = envelope * periodes
    errone = emis_total * taux_erreur
    print("  Hypothèse : %.0f émis par période sur %d périodes, dont %.0f %%"
          % (envelope, periodes, 100 * taux_erreur))
    print("  qualifiés essentiels à tort et découverts ensuite. Total erroné :")
    print("  %.0f sur %.0f." % (errone, emis_total))
    print("")
    print("  TROIS PROCÉDURES DE CORRECTION, ET LEUR RENDEMENT RÉEL :")
    print("")
    print("  %-26s %14s %16s %14s"
          % ("procédure", "récupéré", "neutralisé", "coût reporté"))
    resultats = {}
    for proc in ("aucune", "reclassement", "compensation"):
        if proc == "aucune":
            recupere, neutralise, reporte = 0.0, 0.0, 0.0
        elif proc == "reclassement":
            # L'écriture est corrigée ; l'argent reste en circulation.
            recupere, neutralise, reporte = 0.0, 0.0, 0.0
        else:
            # L'enveloppe future de la même autorité est réduite d'autant.
            recupere = 0.0
            neutralise = errone
            reporte = errone
        resultats[proc] = (recupere, neutralise, reporte)
        print("  %-26s %14.0f %16.0f %14.0f"
              % (proc, recupere, neutralise, reporte))
    print("")
    print("  RÉSULTAT, ET IL EST STRUCTUREL. UNE ÉMISSION SANS DETTE N'A PAS")
    print("  DE REPRISE NATURELLE : rien, dans le mécanisme, ne ramène l'argent")
    print("  émis à tort. Les trois colonnes « récupéré » valent zéro, et ce")
    print("  n'est pas une lacune d'implémentation — c'est la contrepartie de")
    print("  l'absence de dette, qui est le cœur même de NEMO.")
    print("")
    print("  LA SEULE CORRECTION QUI MORD EST LA COMPENSATION, et elle coûte :")
    print("  %.0f retirés des émissions FUTURES de la même autorité, c'est-à-"
          % errone)
    print("  dire pris sur des besoins essentiels légitimes à venir. L'erreur")
    print("  d'hier est payée par le bénéficiaire de demain, qui n'y est pour")
    print("  rien. NEMO DOIT DIRE S'IL L'ACCEPTE — l'arbitrage est ouvert.")
    print("")
    print("  ET CE QUI COMPTE AVANT TOUT : le taux d'erreur n'est pas une")
    print("  donnée du modèle, c'est une hypothèse posée à %.0f %%. Aucune"
          % (100 * taux_erreur))
    print("  source ne l'établit. Le programme montre la FORME du coût, pas")
    print("  son ampleur.")
    return {"errone": errone, "recupere": 0.0, "reporte": errone}


def cas_5(budget=400.0, pression=30.0, t_revision=6, horizon=12):
    """CHANGEMENT SCIENTIFIQUE.

    LE BUDGET EST UN STOCK, ET IL SE CONSOMME. Le programme testé est
    RÉGULIÈREMENT ADMIS au budget initial — sans quoi le dépassement final ne
    serait pas imputable à la révision, mais à une admission fautive.
    """
    titre(5, "LA SCIENCE RÉVISE UNE LIMITE PENDANT L'EXÉCUTION")
    programme = [("eau", 300.0), ("hopital", 400.0)]
    total_pression = pression * horizon
    emis_par_periode = sum(d for _, d in programme) / horizon
    consomme = pression * t_revision
    deja_emis = emis_par_periode * t_revision
    restant_periodes = horizon - t_revision

    print("  Programme engagé : %s. %.0f de pression carbone par période sur"
          % (" + ".join(c for c, _ in programme), pression))
    print("  %d périodes, soit %.0f au total pour un budget reconnu de %.0f."
          % (horizon, total_pression, budget))
    print("  IL EST RÉGULIÈREMENT ADMIS : %.0f tient dans %.0f."
          % (total_pression, budget))
    print("")
    print("  À la période %d, la science révise le budget à la baisse. %.0f de"
          % (t_revision, consomme))
    print("  pression sont déjà émis, et %.0f d'émission déjà versés."
          % deja_emis)
    print("")
    print("  %-10s %-13s %14s %14s %16s"
          % ("révision", "suite", "pression fin", "dépassement", "émis échoué"))
    resultats = {}
    for taux in (0.40, 0.60):
        revise = budget * (1.0 - taux)
        for suite in ("honorer", "arreter", "transition"):
            if suite == "honorer":
                fin, echoue = total_pression, 0.0
            elif suite == "arreter":
                fin, echoue = consomme, deja_emis
            else:
                pente = [2.0 / 3, 1.0 / 3, 0.0]
                fin = consomme + pression * sum(pente)
                echoue = deja_emis * (1.0 - 3.0 / restant_periodes)
            dep = max(0.0, fin - revise)
            resultats[(taux, suite)] = (fin, dep, echoue)
            print("  %-10s %-13s %14.0f %14.0f %16.0f"
                  % ("−%.0f %% → %.0f" % (100 * taux, revise) if
                     suite == "honorer" else "", suite, fin, dep, echoue))
        print("")

    print("  DEUX RÉGIMES, ET LE SEUIL EST LE RÉSULTAT.")
    print("")
    print("  À −40 %, l'arrêt et la transition ramènent le dépassement à ZÉRO :")
    print("  l'engagement écologique PEUT être tenu — au prix de %.0f d'émission"
          % resultats[(0.40, "arreter")][2])
    print("  échouée pour l'arrêt sec, %.0f pour la transition. Ce n'est pas de"
          % resultats[(0.40, "transition")][2])
    print("  l'argent perdu par un spéculateur : c'est un hôpital à moitié")
    print("  construit.")
    print("")
    print("  À −60 %, PLUS AUCUNE PROCÉDURE NE TIENT. Même l'arrêt immédiat")
    print("  dépasse de %.0f, parce que %.0f de pression ont DÉJÀ été émis"
          % (resultats[(0.60, "arreter")][1], consomme))
    print("  quand la révision arrive, contre %.0f de budget révisé. LE PASSÉ"
          % (budget * 0.40))
    print("  N'EST PAS RÉVISABLE, et c'est une propriété du monde, pas du")
    print("  mécanisme.")
    print("")
    print("  CE QUE CELA FAIT À A44, ET C'EST UNE RESTRICTION. Le deuxième")
    print("  engagement — « ne pas financer d'activités incompatibles avec les")
    print("  contraintes écologiques retenues » — NE PEUT PAS ÊTRE TENU")
    print("  RÉTROACTIVEMENT. Il doit se lire COMME UNE OBLIGATION À LA DATE")
    print("  DE LA DÉCISION, au regard des limites reconnues alors. Faute de")
    print("  quoi une révision scientifique ORDINAIRE suffit à falsifier la")
    print("  promesse SANS QU'AUCUNE FAUTE N'AIT ÉTÉ COMMISE.")
    print("")
    print("  ET LA CONTREPARTIE DOIT ÊTRE ÉCRITE, sinon « à la date » devient")
    print("  un permis d'ignorer la science postérieure. Il faut : un délai de")
    print("  mise en conformité, le sort des tranches non versées, et QUI PAIE")
    print("  L'ÉCHOUAGE. La colonne le chiffre ; NEMO ne dit pas encore qui.")
    return {"consomme": consomme, "deja_emis": deja_emis,
            "depassement_40": resultats[(0.40, "arreter")][1],
            "depassement_60": resultats[(0.60, "arreter")][1],
            "echoue_arret": resultats[(0.40, "arreter")][2]}


def cas_6(part_urgence=0.15, taux_inadmissible=0.30, periodes=12,
          envelope=1000.0):
    """URGENCE HUMANITAIRE."""
    titre(6, "UNE URGENCE HUMANITAIRE QUI N'ATTEND PAS LA PROCÉDURE")
    total = envelope * periodes
    urgence = total * part_urgence
    inadmissible = urgence * taux_inadmissible
    print("  La procédure à trois décisions prend du temps ; l'urgence n'en a")
    print("  pas. UN CANAL D'URGENCE CONTOURNE LES DÉCISIONS 1 ET 2, sous")
    print("  plafond et sous ratification postérieure.")
    print("")
    print("  Émission totale %.0f, canal d'urgence plafonné à %.0f %% soit %.0f."
          % (total, 100 * part_urgence, urgence))
    print("  Ratification ex post : %.0f %% de ce montant, soit %.0f, se révèle"
          % (100 * taux_inadmissible, inadmissible))
    print("  inadmissible au veto physique.")
    print("")
    print("  CE QUE LA RATIFICATION RÉCUPÈRE : %.0f." % 0.0)
    print("  CE QU'ELLE PEUT FAIRE : refuser les tranches non versées, réduire")
    print("  l'enveloppe d'urgence suivante, et rendre le motif public.")
    print("")
    print("  RÉSULTAT : LE TROU EST BORNÉ, IL N'EST PAS FERMÉ. %.0f %% de"
          % (100 * part_urgence))
    print("  l'émission échappe par construction au veto physique, et %.0f"
          % inadmissible)
    print("  n'auraient pas dû être émis. Aucun dispositif ne les reprend —")
    print("  c'est le même mur qu'au cas 4.")
    print("")
    print("  ET LE PLAFOND D'URGENCE EST UN NOMBRE POLITIQUE. Trop bas, il")
    print("  laisse mourir ; trop haut, il vide le veto. Le programme ne le")
    print("  fixe pas, et AUCUN CALCUL NE PEUT LE FIXER : c'est un arbitrage")
    print("  entre une vie identifiable aujourd'hui et une limite anonyme")
    print("  demain. LE MÉCANISME N'A PAS D'AVIS LÀ-DESSUS, et prétendre le")
    print("  contraire serait la faute que ce corpus traque.")
    return {"urgence": urgence, "inadmissible": inadmissible, "recupere": 0.0}


def cas_7():
    """CAPTURE POLITIQUE DE L'AUTORITÉ."""
    titre(7, "L'AUTORITÉ DE QUALIFICATION EST CAPTURÉE")
    honnete = list(CATALOGUE)
    capture = []
    for p in CATALOGUE:
        if p.cle == "charbon":
            q = Projet(p.cle, p.libelle, p.demande, True, p.ressources,
                       {"carbone": DECLARATION_CAPTUREE}, p.beneficiaires, 3,
                       p.rang_depot, qualifie_par="autorite-capturee")
            capture.append(q)
        else:
            capture.append(p)

    pa = passer(honnete, enveloppe=2000.0, capacite=2000.0)
    pb = passer(capture, enveloppe=2000.0, capacite=2000.0)

    vraie = PAR_CLE["charbon"].frontieres["carbone"]
    print("  L'autorité qualifie « essentielle » une centrale thermique et")
    print("  déclare une pression carbone de %.0f au lieu de %.0f. Elle ne"
          % (DECLARATION_CAPTUREE, vraie))
    print("  déclare pas n'importe quoi : %.0f passe le veto ET le contrôle"
          % DECLARATION_CAPTUREE)
    print("  cumulé E5, qui plafonne à %.0f. Rien d'autre ne change."
          % FRONTIERES["carbone"])
    print("")
    print("  %-22s %14s %14s" % ("", "passage honnête", "passage capturé"))
    print("  %-22s %14d %14d"
          % ("projets refusés", len(pa.refuses), len(pb.refuses)))
    print("  %-22s %14d %14d"
          % ("projets financés", len(pa.emis), len(pb.emis)))
    print("  %-22s %14.0f %14.0f"
          % ("émission totale", sum(pa.emis.values()), sum(pb.emis.values())))
    print("  %-22s %14d %14d"
          % ("anomalies E1-E4", len(pa.anomalies), len(pb.anomalies)))
    detourne = pb.emis.get("charbon", 0.0)
    print("")
    print("  DÉTOURNÉ : %.0f vers un projet que le passage honnête refuse."
          % detourne)
    print("")
    if not pb.anomalies:
        print("  ET TOUS LES CONTRÔLES SONT AU VERT. E1, E2, E3, E4 : aucune")
        print("  anomalie. Le mécanisme fonctionne exactement comme prévu —")
        print("  il applique fidèlement une qualification fausse.")
    print("")
    print("  LE POUVOIR D'ARRÊT NE RATTRAPE PAS CELA, et il faut le dire")
    print("  précisément. L'arrêt physique s'exerce sur une PRESSION DÉCLARÉE :")
    print("  si la déclaration est fausse, il ne voit rien. L'arrêt")
    print("  démocratique appartient à l'institution captée. L'arrêt monétaire")
    print("  ne porte que sur le rythme, jamais sur l'objet.")
    print("")
    print("  ET AJOUTER UN CONTRÔLE NE FERAIT QUE DÉPLACER LA DÉCLARATION.")
    print("  Le contrôle cumulé E5 a été ajouté pour cette raison : il mord")
    print("  bien — la pression cumulée du passage capturé atteint %.0f pour"
          % pb.cumuls.get("carbone", 0.0))
    print("  %.0f de budget — et la capture se contente de déclarer en"
          % FRONTIERES["carbone"])
    print("  dessous. UN CONTRÔLE DE PLUS DÉPLACE LE MENSONGE, IL NE LE VOIT")
    print("  PAS.")
    print("")
    print("  RÉSULTAT : NON DÉTECTÉ. AUCUN CONTRÔLE INTERNE NE DISTINGUE UN")
    print("  MÉCANISME SAIN D'UN MÉCANISME CAPTURÉ — les deux passages")
    print("  produisent des registres de même forme, et le capturé n'émet")
    print("  aucun signal. C'EST LE RÉSULTAT LE PLUS DÉFAVORABLE DE CE")
    print("  PROGRAMME, et il n'est pas réparable par un contrôle de plus :")
    print("  tout contrôle interne s'exerce sur des déclarations.")
    print("")
    print("  CE QU'IL FAUDRAIT, ET QUI N'EST PAS CONÇU : une MESURE EXTÉRIEURE")
    print("  au mécanisme — pression physique constatée et non déclarée,")
    print("  registre du besoin tenu hors de l'autorité qui qualifie, droit")
    print("  de saisine d'un tiers. TANT QUE CELA N'EXISTE PAS, LA GARANTIE")
    print("  DE A44 EST CONDITIONNELLE À LA PROBITÉ DE L'AUTORITÉ, et cette")
    print("  condition n'est écrite nulle part dans la promesse.")
    return {"detourne": detourne, "anomalies": len(pb.anomalies),
            "refuses_honnete": len(pa.refuses),
            "refuses_capture": len(pb.refuses)}


# =====================================================================
def main():
    print("=" * 78)
    print("LA RÈGLE D'ÉMISSION DE NEMO IMS — SEPT CAS LIMITES")
    print("=" * 78)
    print("Trois décisions séparées : VETO PHYSIQUE, PRIORITÉ DÉMOCRATIQUE,")
    print("CALIBRAGE MONÉTAIRE. Le veto refuse sans jamais autoriser ; la")
    print("priorité appartient au politique ; le calibrage échelonne sans")
    print("jamais refuser au fond.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ et les projets sont fictifs. Ce programme")
    print("montre CE QUE LA RÈGLE FAIT, jamais qu'elle est fondée.")

    print("")
    print("LE POUVOIR D'ARRÊT")
    for a in ARRETS:
        print("  %-14s %s" % (a["cle"], a["titulaire"]))
        print("  %-14s motif : %s" % ("", a["motif"]))
        print("  %-14s portée : %s" % ("", a["portee"]))

    r = {}
    r[1], r[2], r[3] = cas_1(), cas_2(), cas_3()
    r[4], r[5] = cas_4(), cas_5()
    r[6], r[7] = cas_6(), cas_7()

    print("")
    print("=" * 78)
    print("CE QUE LES SEPT CAS ÉTABLISSENT")
    print("=" * 78)
    verdicts = [
        (1, "TRANCHÉ, MAIS IL RESTREINT A44", "la promesse vaut sur la "
         "fenêtre, pas à la date"),
        (2, "DILEMME NON TRANCHÉ", "le veto strict bloque la transition, le "
         "veto agrégé n'est plus physique"),
        (3, "INDÉCIDABLE PAR LE MÉCANISME", "%d gagnants pour %d départages : "
         "choisir le départage EST la décision"
         % (r[3]["distincts"], len(DEPARTAGES))),
        (4, "TRANCHÉ CONTRE LA RÈGLE", "une émission sans dette n'a aucune "
         "reprise : %.0f irrécupérables" % r[4]["errone"]),
        (5, "TENU JUSQU'À UN SEUIL", "à −40 %% l'arrêt ramène le "
         "dépassement à zéro pour %.0f d'échouage ; à −60 %% plus rien ne tient"
         % r[5]["echoue_arret"]),
        (6, "BORNÉ, NON FERMÉ", "%.0f échappent au veto, %.0f n'auraient pas "
         "dû être émis, %.0f récupérables"
         % (r[6]["urgence"], r[6]["inadmissible"], r[6]["recupere"])),
        (7, "NON DÉTECTÉ", "tous les contrôles au vert, %.0f détournés"
         % r[7]["detourne"]),
    ]
    for n, verdict, motif in verdicts:
        print("  cas %d  %-32s %s" % (n, verdict, motif))

    # Le compte est CALCULÉ, non écrit : une conclusion figée devient fausse
    # dès qu'un cas change de verdict, et c'est arrivé une fois déjà.
    RESTREINT = ("TRANCHÉ, MAIS IL RESTREINT A44", "TENU JUSQU'À UN SEUIL")
    defaut = [n for n, v, _ in verdicts if v not in RESTREINT]
    restreint = [n for n, v, _ in verdicts if v in RESTREINT]
    print("")
    print("  %d CAS SUR %d METTENT LA RÈGLE EN DÉFAUT — les cas %s — et %d en"
          % (len(defaut), len(verdicts),
             ", ".join(str(n) for n in defaut), len(restreint)))
    print("  RESTREIGNENT LA PROMESSE A44 — les cas %s. Le cas 7 est à part :"
          % ", ".join(str(n) for n in restreint))
    print("  il met la règle en défaut SANS QU'ELLE PUISSE LE SAVOIR. CE N'EST")
    print("  PAS UN ÉCHEC DU PROGRAMME : c'est ce qu'on lui demandait de")
    print("  chercher, et un programme qui n'aurait rien trouvé n'aurait rien")
    print("  cherché.")
    print("")
    print("  CE QUI MANQUE À LA RÈGLE, ET QUI EST DÉSORMAIS NOMMÉ :")
    print("    — une procédure de départage entre besoins essentiels (cas 3) ;")
    print("    — une doctrine d'agrégation entre limites, ou son refus assumé")
    print("      avec le blocage de transition qu'il entraîne (cas 2) ;")
    print("    — une procédure de correction d'erreur, et qui en paie le")
    print("      report (cas 4) ;")
    print("    — une procédure de révision scientifique et de prise en charge")
    print("      de l'échouage (cas 5) ;")
    print("    — un plafond d'urgence, qui est un nombre politique (cas 6) ;")
    print("    — UNE MESURE EXTÉRIEURE AU MÉCANISME, sans quoi la promesse")
    print("      centrale reste conditionnelle à la probité de l'autorité")
    print("      qui qualifie (cas 7).")
    print("")
    print("  ET CE PROGRAMME NE MESURE TOUJOURS PAS L'INFLATION. Le cas 1")
    print("  publie un écart de capacité, qui n'en est qu'une condition")
    print("  nécessaire. Les prix ne sont pas endogènes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
