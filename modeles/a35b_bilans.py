#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATRICE COMPTABLE STATIQUE DE NEMO IMS — arbitrage A35b, 2026-09-09
====================================================================

CE QUE CE PROGRAMME ÉPROUVE, ET RIEN D'AUTRE.

Les branches ouvertes par l'arbitrage A35b — nature de l'obligation, droits du
détenteur, contrepartie à l'actif, reflux, extinction, traitement des pertes —
peuvent-elles s'écrire dans des bilans qui se ferment, sans qu'aucun financement
n'apparaisse implicitement ?

AUCUN COMPORTEMENT ÉCONOMIQUE N'EST MODÉLISÉ ICI. Ni prix, ni élasticité, ni
capacité productive, ni délai, ni importation, ni intérêt. L'auteur du corpus a
arrêté cette progression le 2026-09-09 : on valide d'abord que le dispositif
peut exister dans des bilans cohérents ; ses effets économiques viennent après,
et seulement si les écritures tiennent.

LES SEPT CONTRÔLES. Chacun peut rejeter une branche à lui seul.

  1. ÉQUILIBRE DE L'ÉCRITURE — pour chaque secteur touché, actif = passif +
     situation nette, à chaque écriture.
  2. ÉQUILIBRE FINAL — la même identité sur les bilans cumulés.
  3. MOTIF DE TOUTE VARIATION DE SITUATION NETTE — une richesse qui bouge sans
     motif déclaré est un financement caché.
  4. QUALIFICATION DU PASSIF — quatre exigences, et chacune peut rejeter seule.
     (a) un passif suppose une OBLIGATION PRÉSENTE identifiée ;
     (b) cette obligation doit courir vers quelqu'un qui DÉTIENT l'unité à un
         moment du circuit — une obligation dont le bénéficiaire ne tient jamais
         l'unité ne donne aucun droit au détenteur ;
     (c) une obligation de CONVERSION suppose que l'émetteur détienne de quoi la
         servir, et une créance sur le bénéficiaire même de l'obligation ne
         compte pas : elle est circulaire ;
     (d) un actif porté par l'émetteur suppose un DÉBITEUR identifié à la date
         où il est inscrit.
     Correction de l'auteur du 2026-09-09 : « pour qu'un passif existe, A35b
     doit identifier une obligation de l'émetteur envers le détenteur ».
  5. MIROIRS — tout encours croisé doit se retrouver à l'identique chez la
     contrepartie, et l'encours d'unités émises doit égaler la somme des unités
     détenues. C'est la règle « chaque flux doit avoir une contrepartie »,
     appliquée aux stocks : la créance de l'un est la dette de l'autre.
  6. AUCUNE RICHESSE NE NAÎT DANS LA MATRICE — la somme des variations de
     situation nette sur les six secteurs doit être NULLE à chaque écriture.
     Une matrice statique n'enregistre aucune production. Toute richesse qui y
     apparaît globalement est un financement implicite, et c'est la faute que
     ce programme existe pour trouver.
  7. ENCOURS NÉGATIF — il ne peut s'éteindre plus d'unités qu'il n'en a été
     inscrit.

Les contrôles 4 et 5 ne sont pas arithmétiques, et c'est voulu : une écriture
peut se fermer parfaitement tout en nommant « passif » une chose qui n'en est
pas une.

USAGE :  python modeles/a35b_bilans.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------
# Six secteurs, et pas un de plus : ceux que l'auteur a nommés.
# ---------------------------------------------------------------------
SECTEURS = [
    ("INST", "Institution internationale émettrice"),
    ("BCN", "Banque centrale nationale"),
    ("BQ", "Banques commerciales"),
    ("BEN", "Bénéficiaires des allocations"),
    ("ETAT", "État, guichet national"),
    ("RDM", "Reste de l'économie et du monde"),
]
NOM = dict(SECTEURS)

ACTIF, PASSIF, SN = "A", "P", "SN"
COTE = {ACTIF: "actif", PASSIF: "passif", SN: "situation nette"}

AVOIRS = "avoirs en unités NEMO"
EMISES = "unités NEMO émises"

M = 100   # unités émises et allouées
D = 100   # dépensées par les bénéficiaires
R = 40    # refluées par prélèvement transactionnel et démurrage

# Les actifs que l'émetteur peut porter, et le secteur qui les doit.
# `None` signifie qu'aucun débiteur n'est identifié — le contrôle 4 (d) s'en
# saisit.
DEBITEUR = {
    "créance d'allocation sur la BCN": "BCN",
    "créance sur les bénéficiaires": "BEN",
    "créance de prélèvement": "RDM",
    "créance sur reflux futur": None,
    "devises reçues en souscription": "RDM",
}

# ---------------------------------------------------------------------
# MIROIRS — la créance de l'un est la dette de l'autre.
# L'encours d'unités fait l'objet d'un contrôle propre : il se mire dans la
# somme des détentions, et non dans un seul secteur.
# ---------------------------------------------------------------------
MIROIRS = [
    (("INST", "créance d'allocation sur la BCN", ACTIF),
     ("BCN", "engagement d'allocation envers l'émetteur", PASSIF)),
    (("INST", "créance de prélèvement", ACTIF),
     ("RDM", "dette de prélèvement", PASSIF)),
    (("INST", "créance sur les bénéficiaires", ACTIF),
     ("BEN", "dette envers l'émetteur", PASSIF)),
    (("BCN", "dépôt du guichet national", PASSIF),
     ("ETAT", "dépôt à la banque centrale", ACTIF)),
    (("BCN", "créance sur l'État", ACTIF),
     ("ETAT", "dette envers la banque centrale", PASSIF)),
    (("BCN", "réserves des banques", PASSIF),
     ("BQ", "réserves à la banque centrale", ACTIF)),
    (("BQ", "dépôts des bénéficiaires", PASSIF),
     ("BEN", "dépôts bancaires", ACTIF)),
    (("BQ", "dépôts du reste de l'économie", PASSIF),
     ("RDM", "dépôts bancaires", ACTIF)),
    (("ETAT", "créance sur les bénéficiaires", ACTIF),
     ("BEN", "dette envers le guichet", PASSIF)),
    (("ETAT", "participation dans l'émetteur", ACTIF),
     ("INST", "parts des souscripteurs", PASSIF)),
]


class Ecriture(object):
    """Une opération. `motifs` déclare toute variation de situation nette."""

    def __init__(self, libelle, postes, motifs=None):
        self.libelle = libelle
        self.postes = postes            # (secteur, compte, cote, montant)
        self.motifs = motifs or {}


class Branche(object):
    """Une branche de l'arbitrage A35b, décrite par ses axes et par sa fiche.

    AXES DE CONCEPTION
      circulation   ce qui circule dans l'économie : la MONNAIE NATIONALE créée
                    en regard de l'unité, ou l'UNITÉ ELLE-MÊME
      inscription   ce que l'ÉMETTEUR inscrit en regard de l'unité émise
      allocation    ce que la BANQUE CENTRALE inscrit en regard de l'unité reçue
      beneficiaire  ce que le BÉNÉFICIAIRE reçoit
      souscription  le capital versé À L'AVANCE par les membres et détenu par
                    l'émetteur ; zéro si l'émetteur n'est doté de rien

    FICHE DE L'UNITÉ
      obligation        l'obligation PRÉSENTE de l'émetteur, ou None
      obligation_envers le secteur envers qui elle court
      obligation_type   'acceptation' (recevoir l'unité en règlement) ou
                        'conversion' (remettre autre chose contre l'unité)
      droit / extinction / pertes
    """

    def __init__(self, cle, titre, circulation, inscription, allocation,
                 beneficiaire, obligation, obligation_envers, obligation_type,
                 droit, extinction, pertes, souscription=0):
        self.cle, self.titre = cle, titre
        self.circulation = circulation
        self.inscription = inscription
        self.allocation = allocation
        self.beneficiaire = beneficiaire
        self.souscription = souscription
        self.obligation = obligation
        self.obligation_envers = obligation_envers
        self.obligation_type = obligation_type
        self.droit = droit
        self.extinction = extinction
        self.pertes = pertes


# ---------------------------------------------------------------------
# Les écritures
# ---------------------------------------------------------------------
def _emission_chez_emetteur(b):
    """Ce que l'émetteur inscrit. Retourne (postes, motifs)."""
    p, m = [], {}
    if b.inscription == "creance_allocation":
        p += [("INST", "créance d'allocation sur la BCN", ACTIF, +M),
              ("INST", EMISES, PASSIF, +M)]
    elif b.inscription == "creance_reflux":
        p += [("INST", "créance sur reflux futur", ACTIF, +M),
              ("INST", EMISES, PASSIF, +M)]
    elif b.inscription == "creance_beneficiaire":
        p += [("INST", "créance sur les bénéficiaires", ACTIF, +M),
              ("INST", EMISES, PASSIF, +M)]
    elif b.inscription == "situation_nette":
        p += [("INST", EMISES, PASSIF, +M),
              ("INST", "report à nouveau", SN, -M)]
        m["INST"] = ("émission sans contrepartie à l'actif : la situation nette "
                     "de l'émetteur absorbe le montant")
    elif b.inscription != "hors_bilan":
        raise ValueError(b.inscription)
    return p, m


def ouverture(b):
    """Les positions DÉJÀ LÀ quand la matrice commence.

    Ce ne sont pas des écritures : personne ne s'enrichit en constatant qu'il
    possédait déjà quelque chose. Elles sont donc exemptes du contrôle 6, qui
    porte sur les FLUX, mais soumises au contrôle 1 : un bilan d'ouverture qui
    ne se ferme pas est faux avant même qu'on ait rien fait.
    """
    if not b.souscription:
        return []
    return [("ETAT", "devises", ACTIF, +b.souscription),
            ("ETAT", "report à nouveau", SN, +b.souscription)]


def sequence(b):
    """Les écritures de la branche, dérivées de ses axes."""
    E = []
    if b.souscription:
        E.append(Ecriture(
            "0. Souscription : les membres dotent l'émetteur en devises",
            [("ETAT", "devises", ACTIF, -b.souscription),
             ("ETAT", "participation dans l'émetteur", ACTIF, +b.souscription),
             ("INST", "devises reçues en souscription", ACTIF, +b.souscription),
             ("INST", "parts des souscripteurs", PASSIF, +b.souscription)]))
    p, m = _emission_chez_emetteur(b)

    if b.circulation == "unite_directe":
        # --- 1. L'unité est allouée directement aux bénéficiaires ------
        p += [("BEN", AVOIRS, ACTIF, +M)]
        if b.beneficiaire == "credit":
            p += [("BEN", "dette envers l'émetteur", PASSIF, +M)]
        else:
            p += [("BEN", "report à nouveau", SN, +M)]
            m["BEN"] = "allocation non remboursable : enrichissement net"
        E.append(Ecriture("1. Émission de l'unité et allocation directe aux "
                          "bénéficiaires", p, m))

        # --- 2. Dépense : un échange, et rien de plus ------------------
        E.append(Ecriture(
            "2. Dépense des bénéficiaires, réglée en unités",
            [("BEN", AVOIRS, ACTIF, -D),
             ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
             ("RDM", AVOIRS, ACTIF, +D),
             ("RDM", "biens et capacités cédés", ACTIF, -D)]))
        reglement = [("RDM", AVOIRS, ACTIF, -R)]

    elif b.circulation == "monnaie_nationale":
        # --- 1. L'unité est allouée à la banque centrale ---------------
        p += [("BCN", AVOIRS, ACTIF, +M)]
        if b.allocation == "engagement":
            p += [("BCN", "engagement d'allocation envers l'émetteur",
                   PASSIF, +M)]
        elif b.allocation == "definitive":
            p += [("BCN", "report à nouveau", SN, +M)]
            m["BCN"] = ("allocation définitive : aucune contrepartie n'est "
                        "exigible par l'émetteur")
        else:
            raise ValueError(b.allocation)
        E.append(Ecriture("1. Émission de l'unité et allocation à la banque "
                          "centrale", p, m))

        # --- 2. Dotation du guichet en monnaie centrale ----------------
        E.append(Ecriture(
            "2. Dotation du guichet en monnaie centrale",
            [("BCN", "dépôt du guichet national", PASSIF, +M),
             ("BCN", "report à nouveau", SN, -M),
             ("ETAT", "dépôt à la banque centrale", ACTIF, +M),
             ("ETAT", "report à nouveau", SN, +M)],
            {"BCN": "dotation du guichet imputée sur la situation nette de la "
                    "banque centrale",
             "ETAT": "dotation reçue du dispositif, sans contrepartie "
                     "exigible"}))

        # --- 3. Versement aux bénéficiaires ---------------------------
        p3 = [("BCN", "dépôt du guichet national", PASSIF, -M),
              ("BCN", "réserves des banques", PASSIF, +M),
              ("ETAT", "dépôt à la banque centrale", ACTIF, -M),
              ("BQ", "réserves à la banque centrale", ACTIF, +M),
              ("BQ", "dépôts des bénéficiaires", PASSIF, +M),
              ("BEN", "dépôts bancaires", ACTIF, +M)]
        m3 = {}
        if b.beneficiaire == "credit":
            p3 += [("BEN", "dette envers le guichet", PASSIF, +M),
                   ("ETAT", "créance sur les bénéficiaires", ACTIF, +M)]
        elif b.beneficiaire in ("subvention", "conditionnel"):
            # Une obligation conditionnelle dont la réalisation n'est pas
            # probable n'est PAS un passif : c'est un engagement hors bilan. À
            # l'inception, la branche conditionnelle s'écrit donc exactement
            # comme la subvention. C'est une conclusion, non une approximation.
            p3 += [("BEN", "report à nouveau", SN, +M),
                   ("ETAT", "report à nouveau", SN, -M)]
            m3["BEN"] = "allocation non remboursable : enrichissement net"
            m3["ETAT"] = "transfert définitif aux bénéficiaires"
        else:
            raise ValueError(b.beneficiaire)
        E.append(Ecriture("3. Versement aux bénéficiaires", p3, m3))

        # --- 4. Dépense : un échange, et rien de plus ------------------
        # ATTENTION. Cette écriture ne dit RIEN de la disponibilité des
        # ressources réelles. Elle enregistre un échange au coût : le
        # bénéficiaire troque un dépôt contre un ouvrage, le vendeur troque des
        # biens et des capacités contre un dépôt. Savoir si le travail,
        # l'énergie et les matériaux existaient est la question de L1.C31, et
        # aucune matrice comptable ne peut y répondre. Aucune situation nette ne
        # bouge ici, et c'est délibéré : la matrice refuse de trancher ce
        # qu'elle ne sait pas.
        E.append(Ecriture(
            "4. Dépense des bénéficiaires vers le reste de l'économie",
            [("BEN", "dépôts bancaires", ACTIF, -D),
             ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
             ("RDM", "dépôts bancaires", ACTIF, +D),
             ("RDM", "biens et capacités cédés", ACTIF, -D),
             ("BQ", "dépôts des bénéficiaires", PASSIF, -D),
             ("BQ", "dépôts du reste de l'économie", PASSIF, +D)]))
        reglement = [("RDM", "dépôts bancaires", ACTIF, -R),
                     ("BQ", "dépôts du reste de l'économie", PASSIF, -R),
                     ("BQ", "réserves à la banque centrale", ACTIF, -R),
                     ("BCN", "réserves des banques", PASSIF, -R),
                     ("BCN", AVOIRS, ACTIF, -R)]
    else:
        raise ValueError(b.circulation)

    # --- Fait générateur du prélèvement et du démurrage ----------------
    E.append(Ecriture(
        "%d. Fait générateur du prélèvement et du démurrage" % (len(E) + 1),
        [("INST", "créance de prélèvement", ACTIF, +R),
         ("INST", "report à nouveau", SN, +R),
         ("RDM", "dette de prélèvement", PASSIF, +R),
         ("RDM", "report à nouveau", SN, -R)],
        {"INST": "produit du prélèvement transactionnel et du démurrage",
         "RDM": "prélèvement et démurrage supportés par les détenteurs"}))

    # --- Règlement du reflux et extinction à due concurrence -----------
    E.append(Ecriture(
        "%d. Règlement du reflux et extinction à due concurrence" % (len(E) + 1),
        reglement + [("RDM", "dette de prélèvement", PASSIF, -R),
                     ("INST", "créance de prélèvement", ACTIF, -R),
                     ("INST", EMISES, PASSIF, -R)]))
    return E


# ---------------------------------------------------------------------
# Passage et contrôles
# ---------------------------------------------------------------------
def totaux(bilans, s):
    c = bilans[s]
    a = sum(v for (cpt, co), v in c.items() if co == ACTIF)
    p = sum(v for (cpt, co), v in c.items() if co == PASSIF)
    n = sum(v for (cpt, co), v in c.items() if co == SN)
    return a, p, n


def passer(b):
    bilans = dict((s, {}) for s, _ in SECTEURS)
    anomalies = []
    detenteurs = set()          # secteurs ayant tenu l'unité à un moment

    for (s, cpt, co, v) in ouverture(b):
        bilans[s][(cpt, co)] = bilans[s].get((cpt, co), 0) + v
    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append(
                "[1] position d'ouverture : le bilan de %s ne se ferme pas "
                "(écart %+d)" % (s, a - p - n))

    for i, e in enumerate(sequence(b), 1):
        touches, sn_bougee, dsn = set(), set(), 0
        for (s, cpt, co, v) in e.postes:
            bilans[s][(cpt, co)] = bilans[s].get((cpt, co), 0) + v
            touches.add(s)
            if cpt == AVOIRS and bilans[s][(cpt, co)] > 0:
                detenteurs.add(s)
            if co == SN and v:
                sn_bougee.add(s)
                dsn += v

        for s in [k for k, _ in SECTEURS if k in touches]:
            a, p, n = totaux(bilans, s)
            if a - p - n:
                anomalies.append(
                    "[1] écriture %d : le bilan de %s ne se ferme pas "
                    "(écart %+d)" % (i, s, a - p - n))

        for s in [k for k, _ in SECTEURS if k in sn_bougee]:
            if s not in e.motifs:
                anomalies.append(
                    "[3] écriture %d : la situation nette de %s varie sans "
                    "motif déclaré — financement implicite" % (i, s))

        if dsn:
            anomalies.append(
                "[6] écriture %d « %s » : la somme des situations nettes varie "
                "de %+d — %d de richesse %s dans la matrice sans contrepartie"
                % (i, e.libelle, dsn, abs(dsn),
                   "apparaît" if dsn > 0 else "disparaît"))

    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append("[2] bilan final de %s : ne se ferme pas "
                             "(écart %+d)" % (s, a - p - n))

    # -- 4. qualification du passif -------------------------------------
    emis = bilans["INST"].get((EMISES, PASSIF), 0)

    if b.inscription == "hors_bilan":
        anomalies.append(
            "[4a] l'unité n'est inscrite NULLE PART chez l'émetteur : la règle "
            "de conception du 2026-09-09 n'est pas respectée")
    elif not b.obligation:
        anomalies.append(
            "[4a] l'unité est inscrite au PASSIF de l'émetteur sans obligation "
            "présente identifiée : la qualification est IMPROPRE")
    else:
        if b.obligation_envers not in detenteurs:
            anomalies.append(
                "[4b] l'obligation court envers %s, qui ne détient l'unité à "
                "aucun moment du circuit : le détenteur ne tient aucun droit, "
                "et le passif ne lui doit rien" % b.obligation_envers)
        if b.obligation_type == "conversion":
            servables = 0
            for (cpt, co), v in bilans["INST"].items():
                if co != ACTIF or v <= 0:
                    continue
                if DEBITEUR.get(cpt, None) == b.obligation_envers:
                    continue     # créance sur le bénéficiaire même : circulaire
                if DEBITEUR.get(cpt, "?") is None:
                    continue     # débiteur non identifié : ne sert rien
                servables += v
            if servables < emis:
                anomalies.append(
                    "[4c] l'émetteur promet la CONVERSION de %d unités mais ne "
                    "détient que %d d'actifs propres à la servir : ses seules "
                    "créances sont sur %s, c'est-à-dire sur le bénéficiaire "
                    "même de l'obligation" % (emis, servables,
                                              b.obligation_envers))

    for (cpt, co), v in sorted(bilans["INST"].items()):
        if co == ACTIF and v and cpt in DEBITEUR and DEBITEUR[cpt] is None:
            anomalies.append(
                "[4d] « %s » est portée à l'actif alors qu'aucun débiteur "
                "n'est identifié à la date où elle est inscrite : le fait "
                "générateur n'a pas eu lieu" % cpt)

    # -- 5. miroirs ------------------------------------------------------
    detenu = sum(bilans[s].get((AVOIRS, ACTIF), 0)
                 for s, _ in SECTEURS if s != "INST")
    if emis != detenu:
        anomalies.append(
            "[5] l'encours d'unités émises est de %d, mais %d sont détenues — "
            "l'encours n'a pas de contrepartie" % (emis, detenu))
    for (s1, c1, k1), (s2, c2, k2) in MIROIRS:
        v1 = bilans[s1].get((c1, k1), 0)
        v2 = bilans[s2].get((c2, k2), 0)
        if v1 != v2:
            anomalies.append(
                "[5] miroir rompu : %s / %s = %d, mais %s / %s = %d — "
                "l'encours n'a pas de contrepartie" % (s1, c1, v1, s2, c2, v2))

    # -- 7. encours négatif ----------------------------------------------
    if emis < 0:
        anomalies.append(
            "[7] l'encours d'unités émises devient NÉGATIF (%d) : il s'éteint "
            "plus d'unités qu'il n'en a été inscrit" % emis)

    return bilans, anomalies


# ---------------------------------------------------------------------
# L'ARBRE A35b
# ---------------------------------------------------------------------
ACCEPTATION = ("accepter l'unité en règlement du prélèvement, à tout moment et "
               "à sa valeur faciale")
CONVERSION = ("remettre au détenteur des devises ou un autre avoir de réserve "
              "contre l'unité, à sa demande")

BRANCHES = [
    Branche(
        "B1", "Allocation gagée sur les reflux futurs",
        circulation="monnaie_nationale", inscription="creance_reflux",
        allocation="engagement", beneficiaire="subvention",
        obligation=None, obligation_envers=None, obligation_type=None,
        droit="aucun droit exprès du détenteur",
        extinction="par les reflux, dont la créance est inscrite d'avance",
        pertes="non désigné"),
    Branche(
        "B2", "Allocation de type DTS : la banque centrale s'engage, "
              "l'émetteur convertit",
        circulation="monnaie_nationale", inscription="creance_allocation",
        allocation="engagement", beneficiaire="subvention",
        obligation=CONVERSION, obligation_envers="BCN",
        obligation_type="conversion",
        droit="obtenir des devises contre l'unité",
        extinction="par le reflux, à due concurrence des unités reçues",
        pertes="la banque centrale nationale, par sa situation nette"),
    Branche(
        "B3", "Émission définitive, absorbée par la situation nette de "
              "l'émetteur",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        obligation=ACCEPTATION, obligation_envers="RDM",
        obligation_type="acceptation",
        droit="s'acquitter du prélèvement au moyen de l'unité",
        extinction="par le reflux, à due concurrence des unités reçues",
        pertes="l'émetteur, par sa situation nette"),
    Branche(
        "B4", "Émission définitive, le bénéficiaire recevant un crédit du "
              "guichet",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="credit",
        obligation=ACCEPTATION, obligation_envers="RDM",
        obligation_type="acceptation",
        droit="s'acquitter du prélèvement au moyen de l'unité",
        extinction="par le reflux et par le remboursement du bénéficiaire",
        pertes="le bénéficiaire d'abord, le guichet ensuite"),
    Branche(
        "B5", "Émission définitive, le bénéficiaire recevant un droit "
              "monétaire conditionnel",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="conditionnel",
        obligation=ACCEPTATION, obligation_envers="RDM",
        obligation_type="acceptation",
        droit="s'acquitter du prélèvement au moyen de l'unité",
        extinction="par le reflux ; la condition reste hors bilan",
        pertes="l'émetteur, la réalisation de la condition n'étant pas "
               "probable"),
    Branche(
        "B6", "L'unité est allouée sans être inscrite chez l'émetteur",
        circulation="monnaie_nationale", inscription="hors_bilan",
        allocation="definitive", beneficiaire="subvention",
        obligation=None, obligation_envers=None, obligation_type=None,
        droit="aucun", extinction="non définie", pertes="non désigné"),
    Branche(
        "B7", "L'unité circule elle-même, et le bénéficiaire la reçoit sans "
              "contrepartie",
        circulation="unite_directe", inscription="situation_nette",
        allocation=None, beneficiaire="subvention",
        obligation=ACCEPTATION, obligation_envers="RDM",
        obligation_type="acceptation",
        droit="s'acquitter du prélèvement au moyen de l'unité",
        extinction="par le reflux, à due concurrence des unités reçues",
        pertes="l'émetteur, par sa situation nette"),
    Branche(
        "B8", "L'unité circule elle-même, et le bénéficiaire la reçoit en prêt",
        circulation="unite_directe", inscription="creance_beneficiaire",
        allocation=None, beneficiaire="credit",
        obligation=ACCEPTATION, obligation_envers="RDM",
        obligation_type="acceptation",
        droit="s'acquitter du prélèvement au moyen de l'unité",
        extinction="par le reflux et par le remboursement du bénéficiaire",
        pertes="le bénéficiaire d'abord, l'émetteur ensuite"),
    Branche(
        "B9", "L'émetteur est doté d'un capital souscrit, et peut convertir",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        souscription=M - R,
        obligation=CONVERSION, obligation_envers="BCN",
        obligation_type="conversion",
        droit="obtenir des devises contre l'unité",
        extinction="par le reflux, à due concurrence des unités reçues",
        pertes="l'émetteur, puis les souscripteurs par leurs parts"),
]


def imprimer_bilan(bilans, s):
    a, p, n = totaux(bilans, s)
    lignes = [(cpt, co, v) for (cpt, co), v in sorted(bilans[s].items()) if v]
    if not lignes:
        return
    print("    %-5s %s" % (s, NOM[s]))
    for co in (ACTIF, PASSIF, SN):
        for cpt, c, v in lignes:
            if c == co:
                print("          %-16s %-42s %+7d" % (COTE[co], cpt, v))
    print("          %-16s %-42s %+7d" % ("", "SITUATION NETTE", n))


def main():
    largeur = 78
    print("=" * largeur)
    print("MATRICE COMPTABLE STATIQUE DE NEMO IMS — l'arbre de l'arbitrage A35b")
    print("=" * largeur)
    print("Émission %d, dépense %d, reflux %d. Aucun comportement économique "
          "n'est" % (M, D, R))
    print("modélisé : on éprouve les ÉCRITURES, et rien d'autre.")

    resultats = []
    for b in BRANCHES:
        bilans, anomalies = passer(b)
        resultats.append((b, bilans, anomalies))
        print("")
        print("-" * largeur)
        print("%s — %s" % (b.cle, b.titre))
        print("     %s" % ("SE FERME" if not anomalies
                           else "REJETÉE (%d)" % len(anomalies)))
        print("     ce qui circule      : %s"
              % ("l'unité elle-même" if b.circulation == "unite_directe"
                 else "la monnaie nationale créée en regard"))
        print("     obligation présente : %s" % (b.obligation or "AUCUNE"))
        print("     elle court envers   : %s" % (b.obligation_envers or "—"))
        print("     droit du détenteur  : %s" % b.droit)
        print("     extinction          : %s" % b.extinction)
        print("     porteur des pertes  : %s" % b.pertes)
        if anomalies:
            print("     ANOMALIES :")
            vues = set()
            for a in anomalies:
                if a not in vues:
                    print("       %s" % a)
                    vues.add(a)
        else:
            print("     BILANS FINAUX :")
            for s, _ in SECTEURS:
                imprimer_bilan(bilans, s)

    fermees = [b.cle for b, _, a in resultats if not a]
    rejetees = [b.cle for b, _, a in resultats if a]
    print("")
    print("=" * largeur)
    print("BRANCHES QUI SE FERMENT : %s" % (", ".join(fermees) or "aucune"))
    print("BRANCHES REJETÉES       : %s" % (", ".join(rejetees) or "aucune"))
    print("")
    print("CE QUE CE RÉSULTAT NE DIT PAS. Qu'une branche se ferme signifie que")
    print("ses écritures sont cohérentes, qu'aucune richesse n'y naît sans")
    print("contrepartie, et que l'obligation invoquée court vers quelqu'un qui")
    print("détient l'unité. Cela ne dit RIEN de sa légalité, de sa")
    print("soutenabilité, ni de la disponibilité des ressources réelles que la")
    print("dépense suppose — question de L1.C31, hors de portée d'une matrice.")
    return 0 if fermees else 1


if __name__ == "__main__":
    sys.exit(main())
