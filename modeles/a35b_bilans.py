#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATRICE COMPTABLE DE NEMO IMS — arbre A35b, version 2, 2026-09-09
==================================================================

CE QUE CE PROGRAMME FAIT, ET CE QU'IL NE FAIT PLUS.

La version 1 rendait UN verdict par branche : elle « se ferme » ou elle est
« rejetée ». **C'était une faute, et l'auteur du corpus l'a relevée le
2026-09-09.** Elle traitait une insuffisance d'actifs comme une inexistence de
passif : une dette reste une dette quand son débiteur ne peut pas la payer.
L'insuffisance produit un RISQUE DE LIQUIDITÉ ou DE SOLVABILITÉ, elle ne fait
pas disparaître l'écriture. Des banques centrales fonctionnent avec des fonds
propres négatifs.

CETTE VERSION REND DONC QUATRE RÉSULTATS SÉPARÉS, ET ILS NE SE COMMANDENT PAS.

  R1  COHÉRENCE COMPTABLE — les identités de bilan tiennent, et l'élément est
      reconnu comme passif au sens du § 4.101 du SNA 2025 : une obligation, un
      débiteur, un créancier, et la créance correspondante inscrite chez ce
      créancier (§ 4.103). CALCULÉ.
  R2  LIQUIDITÉ IMMÉDIATE — à CHAQUE étape, l'obligé peut-il servir la demande
      maximale exigible à cette date ? Une obligation stipulée « à tout moment »
      se contrôle au PIC, jamais au bilan final. CALCULÉ.
  R3  SOLVABILITÉ INTERTEMPORELLE — les ressources, revenus, appels de capital
      et garanties disponibles dans le temps couvrent-ils l'obligation ?
      NON ÉVALUABLE ICI : la matrice ne porte qu'UN cycle. Elle rapporte le
      résidu et les ressources de ce cycle, et s'arrête là.
  R4  CONFORMITÉ JURIDIQUE — NON ÉVALUÉE. Chaque branche déclare ce qu'elle
      exigerait ; le corpus ne détient aucun de ces instruments.

UNE BRANCHE PEUT DONC ÊTRE COMPTABLEMENT COHÉRENTE ET ILLIQUIDE. C'est le cas
normal d'un émetteur qui promet plus qu'il ne détient, et ce n'est pas une
anomalie d'écriture : c'est un risque, et il se nomme.

AUCUN COMPORTEMENT ÉCONOMIQUE N'EST MODÉLISÉ. Ni prix, ni salaire, ni profit, ni
élasticité, ni capacité productive, ni transfert international, ni intérêt.
**En particulier, la matrice n'établit AUCUNE incidence économique** : elle
impose par paramètre que tel secteur soit redevable, puis retrouve ce qu'elle a
imposé. Qui supporte réellement la charge dépend des prix, des salaires, des
profits et des comportements, et cela relève du modèle comportemental, pas
d'ici.

A36 EST RESPECTÉ : LE DÉMURRAGE ET LE PRÉLÈVEMENT SONT DEUX MÉCANISMES.
Deux assiettes — l'ENCAISSE détenue pour l'un, la TRANSACTION pour l'autre.
Deux redevables. Deux rythmes. Et deux collecteurs possibles, car A36 laisse
ouverte l'architecture juridique du prélèvement : selon qu'il est perçu par
l'émetteur ou par l'État, IL N'ÉTEINT PAS LA MÊME CHOSE.

USAGE :  python modeles/a35b_bilans.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------
# Sept secteurs. Les deux derniers ont été ajoutés le 2026-09-09 parce que le
# précédent des droits de tirage spéciaux ne peut PAS se représenter avec une
# seule banque centrale : sa liquidité vient des AUTRES participants.
# ---------------------------------------------------------------------
SECTEURS = [
    ("INST", "Institution émettrice, et département qui tient les comptes"),
    ("BCN", "Banque centrale bénéficiaire de l'allocation"),
    ("BCN2", "Banque centrale contributrice, détentrice de devises"),
    ("BQ", "Banques commerciales"),
    ("BEN", "Bénéficiaires des allocations"),
    ("ETAT", "État membre, guichet national et redevable statutaire"),
    ("RDM", "Reste de l'économie et du monde"),
]
NOM = dict(SECTEURS)

ACTIF, PASSIF, SN = "A", "P", "SN"
COTE = {ACTIF: "actif", PASSIF: "passif", SN: "situation nette"}

AVOIRS = "avoirs en unités NEMO"
EMISES = "unités NEMO émises"
ALLOC = "allocation cumulative reçue"
DEVISES = "devises librement utilisables"

# ---------------------------------------------------------------------
# Paramètres. Ce sont des repères, non des estimations : aucun n'est calibré.
# ---------------------------------------------------------------------
M = 100                      # unités émises et allouées
D = 100                      # montant de la dépense

# A36 — DEUX mécanismes, DEUX assiettes, DEUX redevables.
TAUX_PRELEVEMENT = (1, 4)    # assiette : le MONTANT DE LA TRANSACTION
TAUX_DEMURRAGE = (1, 5)      # assiette : L'ENCAISSE DÉTENUE à la date

PRELEVEMENT = D * TAUX_PRELEVEMENT[0] // TAUX_PRELEVEMENT[1]        # 25
ASSIETTE_DEMURRAGE = D - PRELEVEMENT                                # 75
DEMURRAGE = (ASSIETTE_DEMURRAGE * TAUX_DEMURRAGE[0]
             // TAUX_DEMURRAGE[1])                                  # 15

ECHANGE = 60                 # unités échangées contre devises entre participants
CONTRIBUTION = 40            # contribution statutaire réglée en unités
DEVISES_BCN2 = 60            # devises que la banque centrale contributrice tient

# Les actifs que l'émetteur peut porter, et le secteur qui les doit.
# `None` : aucun débiteur identifié — la reconnaissance s'en saisit.
DEBITEUR = {
    "créance d'allocation sur la BCN": "BCN",
    "créance sur les bénéficiaires": "BEN",
    "créance de prélèvement": "RDM",
    "créance de démurrage": "RDM",
    "créance de contribution": "BCN2",
    "créance sur reflux futur": None,
    DEVISES: "RDM",
}

# Actifs qu'un obligé peut effectivement remettre pour servir une conversion.
MOBILISABLES = (DEVISES,)

MIROIRS = [
    (("INST", "créance d'allocation sur la BCN", ACTIF),
     ("BCN", "engagement d'allocation envers l'émetteur", PASSIF)),
    (("INST", "créance de prélèvement", ACTIF),
     ("RDM", "dette de prélèvement", PASSIF)),
    (("INST", "créance de démurrage", ACTIF),
     ("RDM", "dette de démurrage", PASSIF)),
    (("INST", "créance de contribution", ACTIF),
     ("BCN2", "contribution statutaire due", PASSIF)),
    (("INST", "créance sur les bénéficiaires", ACTIF),
     ("BEN", "dette envers l'émetteur", PASSIF)),
    (("ETAT", "créance de prélèvement", ACTIF),
     ("RDM", "dette de prélèvement fiscale", PASSIF)),
    (("ETAT", "participation dans l'émetteur", ACTIF),
     ("INST", "parts des souscripteurs", PASSIF)),
    (("ETAT", "créance sur les bénéficiaires", ACTIF),
     ("BEN", "dette envers le guichet", PASSIF)),
    (("BCN", "dépôt du guichet national", PASSIF),
     ("ETAT", "dépôt à la banque centrale", ACTIF)),
    (("BCN", "réserves des banques", PASSIF),
     ("BQ", "réserves à la banque centrale", ACTIF)),
    (("BQ", "dépôts des bénéficiaires", PASSIF),
     ("BEN", "dépôts bancaires", ACTIF)),
    (("BQ", "dépôts du reste de l'économie", PASSIF),
     ("RDM", "dépôts bancaires", ACTIF)),
]


class Ecriture(object):
    """Une opération. `motifs` déclare toute variation de situation nette."""

    def __init__(self, libelle, postes, motifs=None):
        self.libelle = libelle
        self.postes = postes            # (secteur, compte, cote, montant)
        self.motifs = motifs or {}


class Branche(object):
    """Une branche de l'arbre A35b : ses axes de conception et sa fiche.

    AXES
      circulation   'monnaie_nationale' — la monnaie créée en regard circule ;
                    'unite_directe'     — l'unité elle-même circule ;
                    'avoir_de_reserve'  — l'unité reste entre banques centrales ;
                    'collectif'         — structure de type droit de tirage
                                          spécial, sans passif chez l'émetteur.
      inscription   ce que l'ÉMETTEUR inscrit en regard de l'unité émise
      allocation    ce que la banque centrale inscrit en regard de l'unité reçue
      beneficiaire  'subvention' | 'credit' | 'conditionnel'
      souscription  capital versé à l'avance par les membres et détenu par
                    l'émetteur, en devises
      collecteur    qui perçoit le PRÉLÈVEMENT TRANSACTIONNEL — 'INST' ou
                    'ETAT'. A36 laisse ce point ouvert, et il décide de ce que
                    le reflux éteint.

    RECONNAISSANCE — les quatre éléments du § 4.101 et du § 4.103 [S1]
      obligation, debiteur, creancier, creance = (secteur, compte, côté)

    EXIGIBILITÉ
      exigibilite   'a_vue' | 'a_echeance' | 'sans_decaissement'
      service       'obligé_seul' | 'autres_participants' | None
    """

    def __init__(self, cle, titre, circulation, inscription, allocation,
                 beneficiaire, obligation, debiteur, creancier, creance,
                 exigibilite, service, droit, extinction, pertes,
                 exigences_juridiques, souscription=0, collecteur="INST"):
        self.cle, self.titre = cle, titre
        self.circulation = circulation
        self.inscription = inscription
        self.allocation = allocation
        self.beneficiaire = beneficiaire
        self.souscription = souscription
        self.collecteur = collecteur
        self.obligation = obligation
        self.debiteur = debiteur
        self.creancier = creancier
        self.creance = creance
        self.exigibilite = exigibilite
        self.service = service
        self.droit = droit
        self.extinction = extinction
        self.pertes = pertes
        self.exigences_juridiques = exigences_juridiques


# ---------------------------------------------------------------------
# Positions d'ouverture et écritures
# ---------------------------------------------------------------------
def ouverture(b):
    """Ce qui est DÉJÀ LÀ quand la matrice commence.

    Ce ne sont pas des flux : personne ne s'enrichit en constatant qu'il
    possédait déjà quelque chose. Exemptes du contrôle 6, soumises au
    contrôle 1.
    """
    p = []
    if b.souscription:
        p += [("ETAT", DEVISES, ACTIF, +b.souscription),
              ("ETAT", "report à nouveau", SN, +b.souscription)]
    if b.circulation in ("avoir_de_reserve", "collectif"):
        p += [("BCN2", DEVISES, ACTIF, +DEVISES_BCN2),
              ("BCN2", "report à nouveau", SN, +DEVISES_BCN2)]
    return p


def _emission(b):
    """Ce que l'émetteur inscrit en regard de l'unité. (postes, motifs)"""
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
    elif b.inscription == "aucune":
        pass          # structure collective : l'émetteur n'est pas le débiteur
    elif b.inscription != "hors_bilan":
        raise ValueError(b.inscription)
    return p, m


def _prelevement_transactionnel(b, compte_regle, secteur_regle):
    """A36, premier mécanisme. Assiette : LA TRANSACTION. Redevable : le vendeur.

    Le collecteur est un PARAMÈTRE, parce que A36 n'a pas arrêté l'architecture
    juridique. S'il est l'émetteur, le règlement ÉTEINT l'unité. S'il est
    l'État, il ne l'éteint pas : l'État devient détenteur.
    """
    col = b.collecteur
    dette = ("dette de prélèvement" if col == "INST"
             else "dette de prélèvement fiscale")
    E = [Ecriture(
        "Prélèvement transactionnel — fait générateur (assiette : la "
        "transaction, %d %% de %d)" % (100 * TAUX_PRELEVEMENT[0]
                                       // TAUX_PRELEVEMENT[1], D),
        [(col, "créance de prélèvement", ACTIF, +PRELEVEMENT),
         (col, "report à nouveau", SN, +PRELEVEMENT),
         ("RDM", dette, PASSIF, +PRELEVEMENT),
         ("RDM", "report à nouveau", SN, -PRELEVEMENT)],
        {col: "produit du prélèvement transactionnel",
         "RDM": "prélèvement transactionnel dû par le vendeur"})]

    regle = [("RDM", compte_regle, ACTIF, -PRELEVEMENT),
             ("RDM", dette, PASSIF, -PRELEVEMENT),
             (col, "créance de prélèvement", ACTIF, -PRELEVEMENT)]
    if secteur_regle:      # le circuit passe par la banque centrale
        regle += [("BQ", "dépôts du reste de l'économie", PASSIF, -PRELEVEMENT),
                  ("BQ", "réserves à la banque centrale", ACTIF, -PRELEVEMENT),
                  ("BCN", "réserves des banques", PASSIF, -PRELEVEMENT),
                  ("BCN", AVOIRS, ACTIF, -PRELEVEMENT)]
    if col == "INST":
        regle += [("INST", EMISES, PASSIF, -PRELEVEMENT)]
    else:
        regle += [("ETAT", AVOIRS, ACTIF, +PRELEVEMENT)]
    E.append(Ecriture("Prélèvement transactionnel — règlement", regle))
    return E


def _demurrage(compte_regle, secteur_regle):
    """A36, second mécanisme. Assiette : L'ENCAISSE. Redevable : le détenteur.

    Règle monétaire : le collecteur est l'émetteur, et le règlement éteint.
    """
    E = [Ecriture(
        "Démurrage — fait générateur (assiette : l'encaisse détenue, %d %% de "
        "%d)" % (100 * TAUX_DEMURRAGE[0] // TAUX_DEMURRAGE[1],
                 ASSIETTE_DEMURRAGE),
        [("INST", "créance de démurrage", ACTIF, +DEMURRAGE),
         ("INST", "report à nouveau", SN, +DEMURRAGE),
         ("RDM", "dette de démurrage", PASSIF, +DEMURRAGE),
         ("RDM", "report à nouveau", SN, -DEMURRAGE)],
        {"INST": "produit du démurrage sur les encaisses",
         "RDM": "démurrage supporté par le détenteur de l'encaisse"})]

    regle = [("RDM", compte_regle, ACTIF, -DEMURRAGE),
             ("RDM", "dette de démurrage", PASSIF, -DEMURRAGE),
             ("INST", "créance de démurrage", ACTIF, -DEMURRAGE),
             ("INST", EMISES, PASSIF, -DEMURRAGE)]
    if secteur_regle:
        regle += [("BQ", "dépôts du reste de l'économie", PASSIF, -DEMURRAGE),
                  ("BQ", "réserves à la banque centrale", ACTIF, -DEMURRAGE),
                  ("BCN", "réserves des banques", PASSIF, -DEMURRAGE),
                  ("BCN", AVOIRS, ACTIF, -DEMURRAGE)]
    E.append(Ecriture("Démurrage — règlement", regle))
    return E


def sequence(b):
    """Les écritures de la branche, dérivées de ses axes."""
    E = []
    if b.souscription:
        E.append(Ecriture(
            "Souscription : les membres dotent l'émetteur en devises",
            [("ETAT", DEVISES, ACTIF, -b.souscription),
             ("ETAT", "participation dans l'émetteur", ACTIF, +b.souscription),
             ("INST", DEVISES, ACTIF, +b.souscription),
             ("INST", "parts des souscripteurs", PASSIF, +b.souscription)]))

    p, m = _emission(b)

    # ---------------------------------------------------------------
    if b.circulation == "collectif":
        # Structure de type droit de tirage spécial : l'ALLOCATION est un
        # passif du RÉCEVEUR, non de l'émetteur, et l'émetteur ne tient que
        # les comptes. Deux participants au moins sont nécessaires : la
        # liquidité ne vient pas de l'émetteur, elle vient des autres.
        for s in ("BCN", "BCN2"):
            p += [(s, AVOIRS, ACTIF, +M), (s, ALLOC, PASSIF, +M)]
        E.append(Ecriture("Allocation aux participants : avoirs à l'actif, "
                          "allocation cumulative au passif de CHAQUE receveur",
                          p, m))
        E.append(Ecriture(
            "Échange volontaire entre participants : la BCN cède des avoirs "
            "contre des devises",
            [("BCN", AVOIRS, ACTIF, -ECHANGE),
             ("BCN", DEVISES, ACTIF, +ECHANGE),
             ("BCN2", DEVISES, ACTIF, -ECHANGE),
             ("BCN2", AVOIRS, ACTIF, +ECHANGE)]))
        return E

    # ---------------------------------------------------------------
    if b.circulation == "avoir_de_reserve":
        p += [("BCN", AVOIRS, ACTIF, +M)]
        if b.allocation == "engagement":
            p += [("BCN", "engagement d'allocation envers l'émetteur",
                   PASSIF, +M)]
        else:
            p += [("BCN", "report à nouveau", SN, +M)]
            m["BCN"] = ("allocation définitive : aucune contrepartie n'est "
                        "exigible par l'émetteur")
        E.append(Ecriture("Émission et allocation à la banque centrale", p, m))
        E.append(Ecriture(
            "Échange volontaire entre participants : la BCN cède des unités "
            "contre des devises",
            [("BCN", AVOIRS, ACTIF, -ECHANGE),
             ("BCN", DEVISES, ACTIF, +ECHANGE),
             ("BCN2", DEVISES, ACTIF, -ECHANGE),
             ("BCN2", AVOIRS, ACTIF, +ECHANGE)]))
        E.append(Ecriture(
            "Contribution statutaire due à l'émetteur — fait générateur",
            [("INST", "créance de contribution", ACTIF, +CONTRIBUTION),
             ("INST", "report à nouveau", SN, +CONTRIBUTION),
             ("BCN2", "contribution statutaire due", PASSIF, +CONTRIBUTION),
             ("BCN2", "report à nouveau", SN, -CONTRIBUTION)],
            {"INST": "produit de la contribution statutaire",
             "BCN2": "contribution statutaire due à l'émetteur"}))
        E.append(Ecriture(
            "Contribution réglée EN UNITÉS : l'émetteur accepte, et éteint",
            [("BCN2", AVOIRS, ACTIF, -CONTRIBUTION),
             ("BCN2", "contribution statutaire due", PASSIF, -CONTRIBUTION),
             ("INST", "créance de contribution", ACTIF, -CONTRIBUTION),
             ("INST", EMISES, PASSIF, -CONTRIBUTION)]))
        return E

    # ---------------------------------------------------------------
    if b.circulation == "unite_directe":
        p += [("BEN", AVOIRS, ACTIF, +M)]
        if b.beneficiaire == "credit":
            p += [("BEN", "dette envers l'émetteur", PASSIF, +M)]
        else:
            p += [("BEN", "report à nouveau", SN, +M)]
            m["BEN"] = "allocation non remboursable : enrichissement net"
        E.append(Ecriture("Émission et allocation directe aux bénéficiaires",
                          p, m))
        # Échange au coût. Aucune situation nette ne bouge, et c'est délibéré :
        # la matrice ne sait pas si l'ouvrage vaut son coût, ni si les
        # ressources réelles existaient. C'est la question de L1.C31.
        E.append(Ecriture(
            "Dépense des bénéficiaires, réglée en unités",
            [("BEN", AVOIRS, ACTIF, -D),
             ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
             ("RDM", AVOIRS, ACTIF, +D),
             ("RDM", "biens et capacités cédés", ACTIF, -D)]))
        E += _prelevement_transactionnel(b, AVOIRS, None)
        E += _demurrage(AVOIRS, None)
        return E

    # ---------------------------------------------------------------
    if b.circulation != "monnaie_nationale":
        raise ValueError(b.circulation)

    p += [("BCN", AVOIRS, ACTIF, +M)]
    if b.allocation == "engagement":
        p += [("BCN", "engagement d'allocation envers l'émetteur", PASSIF, +M)]
    elif b.allocation == "definitive":
        p += [("BCN", "report à nouveau", SN, +M)]
        m["BCN"] = ("allocation définitive : aucune contrepartie n'est exigible "
                    "par l'émetteur")
    else:
        raise ValueError(b.allocation)
    E.append(Ecriture("Émission et allocation à la banque centrale", p, m))

    E.append(Ecriture(
        "Dotation du guichet en monnaie centrale",
        [("BCN", "dépôt du guichet national", PASSIF, +M),
         ("BCN", "report à nouveau", SN, -M),
         ("ETAT", "dépôt à la banque centrale", ACTIF, +M),
         ("ETAT", "report à nouveau", SN, +M)],
        {"BCN": "dotation du guichet imputée sur la situation nette de la "
                "banque centrale",
         "ETAT": "dotation reçue du dispositif, sans contrepartie exigible"}))

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
        # Une obligation conditionnelle dont la réalisation n'est pas probable
        # n'est PAS un passif : c'est un engagement hors bilan [S1, glossaire].
        # À l'inception, la branche conditionnelle s'écrit donc comme la
        # subvention. C'est une conclusion du texte de la norme, non une
        # approximation du modèle.
        p3 += [("BEN", "report à nouveau", SN, +M),
               ("ETAT", "report à nouveau", SN, -M)]
        m3["BEN"] = "allocation non remboursable : enrichissement net"
        m3["ETAT"] = "transfert définitif aux bénéficiaires"
    else:
        raise ValueError(b.beneficiaire)
    E.append(Ecriture("Versement aux bénéficiaires", p3, m3))

    E.append(Ecriture(
        "Dépense des bénéficiaires vers le reste de l'économie",
        [("BEN", "dépôts bancaires", ACTIF, -D),
         ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
         ("RDM", "dépôts bancaires", ACTIF, +D),
         ("RDM", "biens et capacités cédés", ACTIF, -D),
         ("BQ", "dépôts des bénéficiaires", PASSIF, -D),
         ("BQ", "dépôts du reste de l'économie", PASSIF, +D)]))

    E += _prelevement_transactionnel(b, "dépôts bancaires", "BCN")
    E += _demurrage("dépôts bancaires", "BCN")
    return E


# ---------------------------------------------------------------------
# Passage
# ---------------------------------------------------------------------
def totaux(bilans, s):
    c = bilans[s]
    a = sum(v for (cpt, co), v in c.items() if co == ACTIF)
    p = sum(v for (cpt, co), v in c.items() if co == PASSIF)
    n = sum(v for (cpt, co), v in c.items() if co == SN)
    return a, p, n


def _copie(bilans):
    return dict((s, dict(c)) for s, c in bilans.items())


def passer(b):
    """Retourne (bilans finaux, chronologie, anomalies arithmétiques).

    La chronologie porte un instantané des bilans APRÈS chaque opération :
    une obligation exigible à tout moment ne se contrôle pas sur le seul
    bilan final.
    """
    bilans = dict((s, {}) for s, _ in SECTEURS)
    anomalies = []

    for (s, cpt, co, v) in ouverture(b):
        bilans[s][(cpt, co)] = bilans[s].get((cpt, co), 0) + v
    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append("[1] ouverture : le bilan de %s ne se ferme pas "
                             "(écart %+d)" % (s, a - p - n))
    chrono = [("Position d'ouverture", _copie(bilans))]

    for i, e in enumerate(sequence(b), 1):
        touches, sn_bougee, dsn = set(), set(), 0
        for (s, cpt, co, v) in e.postes:
            bilans[s][(cpt, co)] = bilans[s].get((cpt, co), 0) + v
            touches.add(s)
            if co == SN and v:
                sn_bougee.add(s)
                dsn += v

        for s in [k for k, _ in SECTEURS if k in touches]:
            a, p, n = totaux(bilans, s)
            if a - p - n:
                anomalies.append("[1] opération %d : le bilan de %s ne se "
                                 "ferme pas (écart %+d)" % (i, s, a - p - n))
        for s in [k for k, _ in SECTEURS if k in sn_bougee]:
            if s not in e.motifs:
                anomalies.append("[3] opération %d : la situation nette de %s "
                                 "varie sans motif déclaré" % (i, s))
        if dsn:
            anomalies.append(
                "[6] opération %d « %s » : la somme des situations nettes "
                "varie de %+d — richesse sans contrepartie" % (i, e.libelle,
                                                               dsn))
        chrono.append(("%d. %s" % (i, e.libelle), _copie(bilans)))

    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append("[2] bilan final de %s : ne se ferme pas "
                             "(écart %+d)" % (s, a - p - n))

    # -- 5. miroirs -----------------------------------------------------
    detenu = sum(bilans[s].get((AVOIRS, ACTIF), 0)
                 for s, _ in SECTEURS if s != "INST")
    if b.circulation == "collectif":
        alloue = sum(bilans[s].get((ALLOC, PASSIF), 0) for s, _ in SECTEURS)
        if alloue != detenu:
            anomalies.append(
                "[5] allocations cumulatives %d, avoirs détenus %d — dans une "
                "structure collective, les deux totaux doivent coïncider"
                % (alloue, detenu))
    else:
        emis = bilans["INST"].get((EMISES, PASSIF), 0)
        if emis != detenu:
            anomalies.append(
                "[5] encours émis %d, avoirs détenus %d — l'encours n'a pas de "
                "contrepartie" % (emis, detenu))
        if emis < 0:
            anomalies.append("[7] l'encours émis devient NÉGATIF (%d)" % emis)
    for (s1, c1, k1), (s2, c2, k2) in MIROIRS:
        v1, v2 = bilans[s1].get((c1, k1), 0), bilans[s2].get((c2, k2), 0)
        if v1 != v2:
            anomalies.append("[5] miroir rompu : %s/%s = %d, %s/%s = %d"
                             % (s1, c1, v1, s2, c2, v2))
    return bilans, chrono, anomalies


# ---------------------------------------------------------------------
# R1 — reconnaissance comptable
# ---------------------------------------------------------------------
def reconnaissance(b, chrono):
    """Les quatre éléments du § 4.101 et du § 4.103 [S1].

    Un passif suppose une obligation, un débiteur et un créancier ; et le
    créancier doit détenir la créance correspondante. C'EST TOUT CE QUE CE
    CONTRÔLE VÉRIFIE. Il ne demande à personne d'être capable de payer :
    la capacité de payer est le sujet de R2 et de R3, et une dette impayable
    reste une dette.
    """
    manques = []
    if not b.obligation:
        manques.append("aucune OBLIGATION n'est identifiée")
    if not b.debiteur:
        manques.append("aucun DÉBITEUR n'est identifié")
    elif b.debiteur == "collectif":
        manques.append(
            "le DÉBITEUR est collectif et n'est pas une unité déterminée, "
            "alors que le § 4.101 exige « another unit » — c'est exactement le "
            "point que L19.C09 a vu disparaître de la révision")
    if not b.creancier:
        manques.append("aucun CRÉANCIER n'est identifié")
    if b.creance:
        s, cpt, co = b.creance
        if b.creancier and s != b.creancier:
            manques.append("la créance est inscrite chez %s alors que le "
                           "créancier déclaré est %s" % (s, b.creancier))
        jamais = all(inst[s].get((cpt, co), 0) == 0 for _, inst in chrono)
        if jamais:
            manques.append("le créancier %s ne détient à AUCUNE étape la "
                           "créance correspondante « %s »" % (s, cpt))
    else:
        manques.append("aucune CRÉANCE correspondante n'est désignée")
    return manques


# ---------------------------------------------------------------------
# R2 — liquidité immédiate, contrôlée au PIC
# ---------------------------------------------------------------------
def liquidite(b, chrono):
    """L'obligé peut-il servir la demande maximale exigible, à CHAQUE étape ?

    Une obligation stipulée « à tout moment et à la demande » se contrôle au
    pic de l'encours exigible, jamais sur le bilan final. Contrôler l'état
    final reviendrait à supposer que personne ne demande rien avant la fin.
    """
    if b.exigibilite == "sans_decaissement":
        return {"objet": False, "note":
                "sans objet : l'obligation ne demande aucun décaissement de "
                "l'obligé — il REÇOIT l'unité, il ne la rachète pas"}

    lignes, pire = [], None
    for libelle, inst in chrono:
        exigible = sum(inst[s].get((AVOIRS, ACTIF), 0)
                       for s, _ in SECTEURS if s != b.debiteur)
        if b.service == "autres_participants":
            couverture = sum(inst[s].get((DEVISES, ACTIF), 0)
                             for s, _ in SECTEURS
                             if s not in (b.creancier, "INST"))
            qui = "les autres participants"
        else:
            couverture = sum(v for (cpt, co), v in inst[b.debiteur].items()
                             if co == ACTIF and cpt in MOBILISABLES)
            qui = b.debiteur
        lignes.append((libelle, exigible, couverture))
        if exigible > couverture and (pire is None
                                      or exigible - couverture > pire[1]):
            pire = (libelle, exigible - couverture, exigible, couverture)
    return {"objet": True, "lignes": lignes, "pire": pire, "qui": qui}


# ---------------------------------------------------------------------
# R3 — ce que la matrice peut seulement RAPPORTER
# ---------------------------------------------------------------------
def solvabilite(b, bilans):
    if b.circulation == "collectif":
        residu = sum(bilans[s].get((ALLOC, PASSIF), 0) for s, _ in SECTEURS)
    else:
        residu = bilans["INST"].get((EMISES, PASSIF), 0)
    ressources = b.souscription
    for (cpt, co), v in bilans["INST"].items():
        if co == ACTIF and v > 0 and cpt != DEVISES:
            ressources += v
    ressources += sum(v for (cpt, co), v in bilans["INST"].items()
                      if co == ACTIF and cpt == DEVISES)
    return residu, ressources


# ---------------------------------------------------------------------
# L'arbre A35b
# ---------------------------------------------------------------------
ACCEPT = ("accepter l'unité en règlement de ce qui est dû à l'émetteur, à sa "
          "valeur faciale")
CONVERT = ("remettre au détenteur des devises librement utilisables contre "
           "l'unité, à tout moment et à sa demande")

JUR_COMMUN = ["l'instrument qui crée l'obligation et la rend opposable",
              "le statut de l'émetteur et sa capacité à contracter",
              "l'autorité qui lève, et sur quel fondement"]

BRANCHES = [
    Branche(
        "B1", "Allocation gagée sur les reflux futurs",
        circulation="monnaie_nationale", inscription="creance_reflux",
        allocation="engagement", beneficiaire="subvention",
        obligation=None, debiteur="INST", creancier=None, creance=None,
        exigibilite="sans_decaissement", service=None,
        droit="aucun droit exprès du détenteur",
        extinction="par les reflux, dont la créance est inscrite d'avance",
        pertes="non désigné",
        exigences_juridiques=JUR_COMMUN),
    Branche(
        "B2", "Émission définitive, prélèvement perçu PAR L'ÉMETTEUR",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention", collecteur="INST",
        obligation=ACCEPT, debiteur="INST", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="remettre l'unité en règlement de ce qui est dû à l'émetteur",
        extinction="par le prélèvement ET par le démurrage",
        pertes="l'émetteur, par sa situation nette",
        exigences_juridiques=JUR_COMMUN + [
            "la qualification du prélèvement comme ressource de l'émetteur"]),
    Branche(
        "B3", "Émission définitive, prélèvement perçu PAR L'ÉTAT (A36 ouvert)",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention", collecteur="ETAT",
        obligation=ACCEPT, debiteur="INST", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="remettre l'unité en règlement de ce qui est dû à l'émetteur",
        extinction="par le démurrage SEUL : le prélèvement fiscal n'éteint rien",
        pertes="l'émetteur, par sa situation nette",
        exigences_juridiques=JUR_COMMUN + [
            "le fondement fiscal du prélèvement et son affectation",
            "le droit pour l'État de détenir et d'employer l'unité"]),
    Branche(
        "B4", "Émission définitive, le bénéficiaire recevant un crédit",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="credit",
        obligation=ACCEPT, debiteur="INST", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="remettre l'unité en règlement de ce qui est dû à l'émetteur",
        extinction="par le reflux et par le remboursement du bénéficiaire",
        pertes="le bénéficiaire d'abord, le guichet ensuite",
        exigences_juridiques=JUR_COMMUN + [
            "le contrat de prêt et son rang"]),
    Branche(
        "B5", "Émission définitive, droit monétaire conditionnel",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="conditionnel",
        obligation=ACCEPT, debiteur="INST", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="remettre l'unité en règlement de ce qui est dû à l'émetteur",
        extinction="par le reflux ; la condition reste hors bilan",
        pertes="l'émetteur ; la condition n'étant pas probable, elle n'est pas "
               "reconnue [S1, glossaire]",
        exigences_juridiques=JUR_COMMUN + [
            "la condition, sa constatation et l'autorité qui la constate"]),
    Branche(
        "B6", "L'unité n'est inscrite nulle part chez l'émetteur",
        circulation="monnaie_nationale", inscription="hors_bilan",
        allocation="definitive", beneficiaire="subvention",
        obligation=None, debiteur=None, creancier=None, creance=None,
        exigibilite="sans_decaissement", service=None,
        droit="aucun", extinction="non définie", pertes="non désigné",
        exigences_juridiques=JUR_COMMUN),
    Branche(
        "B7", "L'unité circule elle-même, allocation non remboursable",
        circulation="unite_directe", inscription="situation_nette",
        allocation=None, beneficiaire="subvention",
        obligation=ACCEPT, debiteur="INST", creancier="RDM",
        creance=("RDM", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="s'acquitter du prélèvement et du démurrage au moyen de l'unité",
        extinction="par le prélèvement et par le démurrage",
        pertes="l'émetteur, par sa situation nette",
        exigences_juridiques=JUR_COMMUN + [
            "les quatre conditions sous lesquelles un actif conçu comme moyen "
            "d'échange est enregistré comme monnaie [L19.C08]"]),
    Branche(
        "B8", "L'unité circule elle-même, le bénéficiaire recevant un prêt",
        circulation="unite_directe", inscription="creance_beneficiaire",
        allocation=None, beneficiaire="credit",
        obligation=ACCEPT, debiteur="INST", creancier="RDM",
        creance=("RDM", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="s'acquitter du prélèvement et du démurrage au moyen de l'unité",
        extinction="par le reflux et par le remboursement du bénéficiaire",
        pertes="le bénéficiaire d'abord, l'émetteur ensuite",
        exigences_juridiques=JUR_COMMUN + [
            "les quatre conditions de L19.C08", "le contrat de prêt"]),
    Branche(
        "B9", "Conversion à vue, l'émetteur étant doté d'un capital souscrit",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        souscription=M - PRELEVEMENT - DEMURRAGE,
        obligation=CONVERT, debiteur="INST", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="a_vue", service="oblige_seul",
        droit="obtenir des devises contre l'unité, à tout moment",
        extinction="par le reflux, et par la conversion si elle est demandée",
        pertes="l'émetteur, puis les souscripteurs par leurs parts",
        exigences_juridiques=JUR_COMMUN + [
            "l'engagement de conversion et son plafond",
            "l'appel de capital et son caractère exécutoire"]),
    Branche(
        "B10", "Avoir de réserve non gagé : règlements entre participants et "
               "contributions dues",
        circulation="avoir_de_reserve", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        obligation=ACCEPT, debiteur="INST", creancier="BCN2",
        creance=("BCN2", AVOIRS, ACTIF),
        exigibilite="sans_decaissement", service=None,
        droit="régler en unités les contributions dues à l'émetteur, et céder "
              "l'unité à un autre participant contre devises",
        extinction="par le règlement des contributions statutaires",
        pertes="l'émetteur, par sa situation nette",
        exigences_juridiques=JUR_COMMUN + [
            "l'accord d'échange volontaire entre participants",
            "le régime des contributions statutaires réglables en unités"]),
    Branche(
        "B11", "Structure collective de type droit de tirage spécial",
        circulation="collectif", inscription="aucune",
        allocation=None, beneficiaire="subvention",
        obligation="fournir des devises librement utilisables contre l'unité, "
                   "par accord volontaire ou, en dernier ressort, sur "
                   "désignation",
        debiteur="collectif", creancier="BCN",
        creance=("BCN", AVOIRS, ACTIF),
        exigibilite="a_vue", service="autres_participants",
        droit="obtenir des devises d'un autre participant",
        extinction="aucune : l'allocation cumulative demeure au passif du "
                   "receveur",
        pertes="les participants, par le mécanisme de désignation",
        exigences_juridiques=JUR_COMMUN + [
            "le mécanisme de désignation et ses plafonds",
            "les accords d'échange volontaire",
            "le régime des intérêts sur l'écart avoirs / allocation"]),
]


# ---------------------------------------------------------------------
# Restitution
# ---------------------------------------------------------------------
def imprimer_bilan(bilans, s, marge="      "):
    a, p, n = totaux(bilans, s)
    lignes = [(cpt, co, v) for (cpt, co), v in sorted(bilans[s].items()) if v]
    if not lignes:
        return
    print("%s%-5s %s" % (marge, s, NOM[s]))
    for co in (ACTIF, PASSIF, SN):
        for cpt, c, v in lignes:
            if c == co:
                print("%s      %-16s %-40s %+7d" % (marge, COTE[co], cpt, v))
    print("%s      %-16s %-40s %+7d" % (marge, "", "SITUATION NETTE", n))


def rendre(b, largeur=78):
    bilans, chrono, arith = passer(b)
    manques = reconnaissance(b, chrono)
    liq = liquidite(b, chrono)
    residu, ressources = solvabilite(b, bilans)

    print("")
    print("=" * largeur)
    print("%s — %s" % (b.cle, b.titre))
    print("=" * largeur)
    print("  FICHE DE L'UNITÉ")
    print("    ce qui circule   : %s" % {
        "monnaie_nationale": "la monnaie nationale créée en regard",
        "unite_directe": "l'unité elle-même",
        "avoir_de_reserve": "l'unité, entre banques centrales seulement",
        "collectif": "l'unité, entre participants, sans passif chez l'émetteur",
    }[b.circulation])
    print("    obligation       : %s" % (b.obligation or "AUCUNE"))
    print("    débiteur         : %s" % (b.debiteur or "—"))
    print("    créancier        : %s" % (b.creancier or "—"))
    print("    créance inscrite : %s" % (
        "%s / %s" % (b.creance[0], b.creance[1]) if b.creance else "—"))
    print("    exigibilité      : %s" % {
        "a_vue": "À VUE, à tout moment et à la demande",
        "a_echeance": "à échéance",
        "sans_decaissement": "sans décaissement de l'obligé",
    }[b.exigibilite])
    print("    droit            : %s" % b.droit)
    print("    extinction       : %s" % b.extinction)
    print("    porteur du risque: %s" % b.pertes)
    print("    prélèvement perçu par : %s   (A36 : architecture NON arrêtée)"
          % b.collecteur)

    print("")
    print("  R1 — COHÉRENCE COMPTABLE")
    if arith or manques:
        if arith:
            for a in dict.fromkeys(arith):
                print("      IDENTITÉ : %s" % a)
        for m in manques:
            print("      RECONNAISSANCE : %s" % m)
        print("      => l'élément n'est PAS reconnu comme passif en l'état")
    else:
        print("      identités de bilan : tenues à chaque opération")
        print("      obligation, débiteur, créancier et créance : identifiés")
        print("      => reconnu comme passif au sens du § 4.101 [S1]")

    print("")
    print("  R2 — LIQUIDITÉ IMMÉDIATE")
    if not liq["objet"]:
        print("      %s" % liq["note"])
    else:
        print("      contrôlée à CHAQUE étape, et non sur le bilan final")
        print("      %-52s %8s %9s" % ("étape", "exigible", "couvert"))
        for libelle, ex, co in liq["lignes"]:
            marque = "  <<<" if ex > co else ""
            print("      %-52s %8d %9d%s" % (libelle[:52], ex, co, marque))
        if liq["pire"]:
            lib, ecart, ex, co = liq["pire"]
            print("      PIC DE TENSION : %s" % lib[:56])
            print("      exigible %d, mobilisable par %s %d, MANQUE %d"
                  % (ex, liq["qui"], co, ecart))
            print("      => ILLIQUIDE À CE MOMENT. Ce n'est pas un défaut "
                  "d'écriture :")
            print("         le passif existe, et il ne peut pas être servi à "
                  "cette date.")
        else:
            print("      => servable à chaque étape par %s" % liq["qui"])

    print("")
    print("  R3 — SOLVABILITÉ INTERTEMPORELLE : NON ÉVALUABLE SUR CETTE MATRICE")
    print("      un seul cycle est modélisé ; la solvabilité se juge sur un")
    print("      horizon, avec des revenus, des appels de capital et des")
    print("      garanties que cette matrice ne porte pas.")
    print("      sur ce cycle : encours non éteint %d, ressources identifiées %d"
          % (residu, ressources))

    print("")
    print("  R4 — CONFORMITÉ JURIDIQUE : NON ÉVALUÉE")
    for e in b.exigences_juridiques:
        print("      exigerait : %s" % e)

    print("")
    print("  CHRONOLOGIE DES BILANS")
    for libelle, inst in chrono:
        actifs = [(s, sum(v for (c, co), v in inst[s].items() if co == ACTIF))
                  for s, _ in SECTEURS]
        actifs = [(s, v) for s, v in actifs if v]
        if not actifs:
            continue
        print("    %s" % libelle)
        print("        actifs : %s" % ", ".join("%s %d" % (s, v)
                                                for s, v in actifs))
    print("")
    print("  BILANS FINAUX")
    for s, _ in SECTEURS:
        imprimer_bilan(bilans, s)
    return {"cle": b.cle, "r1": not (arith or manques),
            "r2": (None if not liq["objet"] else liq["pire"] is None)}


def main():
    print("=" * 78)
    print("MATRICE COMPTABLE DE NEMO IMS — arbre A35b, version 2")
    print("=" * 78)
    print("Émission %d ; dépense %d ; prélèvement transactionnel %d sur une "
          "assiette" % (M, D, PRELEVEMENT))
    print("de transaction de %d ; démurrage %d sur une assiette d'encaisse de "
          "%d." % (D, DEMURRAGE, ASSIETTE_DEMURRAGE))
    print("Ce sont des repères. Aucun n'est calibré, et aucun comportement")
    print("économique n'est modélisé.")
    print("")
    print("QUATRE RÉSULTATS SÉPARÉS PAR BRANCHE, ET ILS NE SE COMMANDENT PAS :")
    print("  R1 cohérence comptable   — calculé")
    print("  R2 liquidité immédiate   — calculé, au PIC et non au bilan final")
    print("  R3 solvabilité           — NON ÉVALUABLE sur un cycle unique")
    print("  R4 conformité juridique  — NON ÉVALUÉE")
    print("")
    print("UNE BRANCHE PEUT ÊTRE COMPTABLEMENT COHÉRENTE ET ILLIQUIDE.")
    print("Une dette impayable reste une dette : l'insuffisance d'actifs est un")
    print("risque, elle n'efface pas l'écriture.")

    res = [rendre(b) for b in BRANCHES]

    print("")
    print("=" * 78)
    print("RÉCAPITULATIF — DEUX RÉSULTATS CALCULÉS, AUCUNE CONCLUSION EXCLUSIVE")
    print("=" * 78)
    print("  %-6s %-26s %s" % ("", "R1 cohérence comptable", "R2 liquidité"))
    for r in res:
        r2 = ("sans objet" if r["r2"] is None
              else ("servable" if r["r2"] else "TENSION"))
        print("  %-6s %-26s %s" % (r["cle"],
                                   "reconnu" if r["r1"] else "NON reconnu", r2))
    print("")
    print("CE QUE CE TABLEAU NE DIT PAS. Il ne dit pas qu'une branche est")
    print("possible, ni qu'une autre est impossible. Les branches écrites sont")
    print("onze ; une branche qui n'est pas écrite n'est pas rejetée, elle est")
    print("absente. Et les règles de reconnaissance retenues ici sont des")
    print("HYPOTHÈSES DE LECTURE de la norme, non la norme elle-même.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
