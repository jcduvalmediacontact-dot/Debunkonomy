#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MATRICE COMPTABLE DE NEMO IMS — arbre A35b, version 3, 2026-09-09
==================================================================

CE QUE CE PROGRAMME CALCULE, ET CE QU'IL NE FAIT QUE PROPOSER.

  R1a  COHÉRENCE ARITHMÉTIQUE — VÉRIFIÉE MÉCANIQUEMENT. Les identités de bilan, les miroirs
       des encours croisés, la somme des situations nettes, et l'identité
       centrale contrôlée À CHAQUE ÉTAPE :
           total des passifs représentatifs de l'unité, QUEL QU'EN SOIT LE
           PORTEUR = total des avoirs correspondants chez les détenteurs.
       Le porteur n'est pas toujours l'émetteur : dans une architecture de type
       droit de tirage spécial, le passif est inscrit chez CHAQUE MEMBRE
       RECEVEUR. Parler du « passif de l'émetteur » y serait faux.
       VÉRIFIÉE MÉCANIQUEMENT SELON LES ÉCRITURES POSÉES — et c'est tout ce que
       cela veut dire. **Le programme ne valide pas la représentation comptable
       ou économique qu'on lui a donnée : des écritures fausses peuvent
       s'équilibrer parfaitement.** L'arithmétique ne se discute pas ; le choix
       des écritures, si.

  R1b  QUALIFICATION COMPTABLE — PROPOSÉE, NON CALCULÉE. Le programme constate
       que des éléments sont renseignés et que la créance suit son détenteur.
       **Il ne peut pas établir qu'un élément EST un passif au sens du § 4.101 :
       cela suppose une lecture de la norme et la validité juridique des
       obligations déclarées, dont aucune n'est vérifiée ici.** Le résultat est
       une PROPOSITION soumise à un comptable national.

  R2   LIQUIDITÉ — CALCULÉE, MAIS CONDITIONNELLE. Le calcul est exact ; ce
       qu'il calcule dépend entièrement de paramètres déclarés et non calibrés :
       montant émis, montant dépensé, taux des deux mécanismes de reflux,
       volume de l'échange volontaire, devises détenues par les autres
       participants, et facteur du plafond de désignation. Ce dernier est
       JURIDIQUEMENT SOURCÉ pour le dispositif des droits de tirage spéciaux
       (art. XIX § 4(a)) ; **sa transposition à NEMO IMS reste un choix de
       conception non arbitré**, et les autres repères ne sont calibrés sur
       rien. Changer un seul de ces repères change le résultat. **R2 ne dit
       donc pas si le dispositif serait liquide : il dit ce qui suit des
       paramètres qu'on lui a donnés.** Pour un instrument servi par d'autres
       participants, trois scénarios SÉPARÉS : fonctionnement normal, capacité
       résiduelle de désignation, ruée à cent pour cent. **Le troisième est un
       stress, jamais l'état ordinaire.**

  R3   SOLVABILITÉ INTERTEMPORELLE — NON ÉVALUABLE. Un seul cycle, sans intérêt
       ni horizon.

  R4a  CONCEPTION JURIDIQUE À PRODUIRE — une institution prospective écrit son
       droit constitutif : droits, obligations, gouvernance, retrait,
       liquidation, immunités, règlement des différends. Aucun de ces textes
       n'existe.

  R4b  COMPATIBILITÉ JURIDIQUE À ÉVALUER — mais elle ne peut pas ignorer les
       ordres juridiques dans lesquels elle devra être reconnue et fonctionner :
       traités, droits nationaux et régionaux, normes comptables.

TROIS CORRECTIONS DE L'AUTEUR, LE 2026-09-09, APRÈS LA VERSION 2.

  LE CRÉANCIER EST DYNAMIQUE. Un instrument transférable change de créancier
  avec son détenteur. La qualité de créancier MIGRE, et la créance de chacun
  vaut son encours. Une fiche ne peut pas figer un créancier unique.

  LE COLLECTEUR NE DÉCIDE PAS DE L'EXTINCTION. Il décide de la PREMIÈRE
  DESTINATION des unités perçues. Ce qu'il en fait ensuite — les conserver, les
  remettre en circulation, les transférer à l'émetteur — décide de l'encours
  final. Trois sous-branches l'établissent.

  UNE ARCHITECTURE DIFFÉRENTE N'EST PAS UNE ARCHITECTURE INVALIDE. La structure
  de type droit de tirage spécial place le passif chez LE MEMBRE QUI REÇOIT, et
  chacun est le débiteur déterminé de sa propre allocation [S1, § 12.49]. Elle
  CONTREDIT A35a ; elle n'est pas comptablement méconnaissable.

AUCUN COMPORTEMENT ÉCONOMIQUE N'EST MODÉLISÉ, et la matrice n'établit AUCUNE
incidence économique : elle impose par paramètre qui est redevable, puis
retrouve ce qu'elle a imposé.

USAGE :  python modeles/a35b_bilans.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

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
DUE = "contribution statutaire due"

M = 100
D = 100
TAUX_PRELEVEMENT = (1, 4)     # assiette : LA TRANSACTION
TAUX_DEMURRAGE = (1, 5)       # assiette : L'ENCAISSE DÉTENUE
PRELEVEMENT = D * TAUX_PRELEVEMENT[0] // TAUX_PRELEVEMENT[1]        # 25
ASSIETTE_DEMURRAGE = D - PRELEVEMENT                                # 75
DEMURRAGE = ASSIETTE_DEMURRAGE * TAUX_DEMURRAGE[0] // TAUX_DEMURRAGE[1]  # 15

CONTRIB_DETENTEUR = 20        # obligation présente du détenteur envers l'émetteur
ECHANGE = 60
CONTRIBUTION = 40
DEVISES_BCN2 = 60

# RÈGLE DE DÉSIGNATION — SOURCÉE LE 2026-09-09, article XIX, section 4(a) des
# Statuts du Fonds, lu dans le texte via l'eLibrary [S2] :
#   « A participant's obligation to provide currency shall not extend beyond
#     the point at which its holdings of special drawing rights IN EXCESS OF
#     its net cumulative allocation are equal to TWICE its net cumulative
#     allocation or such higher limit as may be agreed between a participant
#     and the Fund. »
# C'est L'EXCÉDENT qui est borné à deux allocations, non les avoirs totaux :
# le plafond total des avoirs vaut donc TROIS allocations. Une version
# antérieure écrivait « 2 x allocation - avoirs » et sous-estimait la capacité
# de 100 % d'une allocation. Erreur relevée par l'auteur et corrigée.
# Et § 4(b) : « A participant MAY provide currency in excess of the obligatory
# limit » — la limite borne L'OBLIGATION, jamais la possibilité.
EXCEDENT_MAX_FACTEUR = 2          # art. XIX § 4(a)
PLAFOND_DESIGNATION_SOURCE = True


def capacite_designation(allocation, avoirs, facteur=EXCEDENT_MAX_FACTEUR):
    """Ce qu'un participant peut encore être TENU d'accepter, en unités.

    Fonction pure, éprouvable sans aucun scénario : c'est la demande de
    l'auteur du 2026-09-09, un test de scénario ayant masqué l'erreur
    précédente parce que la ressource était nulle de toute façon.

        limite_excedent   = facteur x allocation        (art. XIX § 4(a))
        plafond_total     = allocation + limite_excedent
        capacite_restante = max(0, plafond_total - avoirs)
    """
    limite_excedent = facteur * allocation
    plafond_total = allocation + limite_excedent
    return max(0, plafond_total - avoirs)

DEBITEUR = {
    "créance d'allocation sur la BCN": "BCN",
    "créance sur les bénéficiaires": "BEN",
    "créance de prélèvement": "RDM",
    "créance de démurrage": "RDM",
    "créance de contribution": None,      # le débiteur varie : voir les miroirs
    "créance sur reflux futur": None,
    DEVISES: "RDM",
}
MOBILISABLES = (DEVISES,)

MIROIRS = [
    (("INST", "créance d'allocation sur la BCN", ACTIF),
     ("BCN", "engagement d'allocation envers l'émetteur", PASSIF)),
    (("INST", "créance de prélèvement", ACTIF),
     ("RDM", "dette de prélèvement", PASSIF)),
    (("INST", "créance de démurrage", ACTIF),
     ("RDM", "dette de démurrage", PASSIF)),
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
    def __init__(self, libelle, postes, motifs=None):
        self.libelle = libelle
        self.postes = postes
        self.motifs = motifs or {}


class Branche(object):
    """Une branche de l'arbre A35b.

    LE CRÉANCIER N'EST PAS UN CHAMP. Il est DÉRIVÉ des écritures : à chaque
    étape, les créanciers sont les détenteurs de l'unité, et la créance de
    chacun vaut son encours. C'est la correction de l'auteur du 2026-09-09.
    """

    def __init__(self, cle, titre, circulation, inscription, allocation,
                 beneficiaire, obligation, passif_chez, compte_passif,
                 droit_attache, servi_par, exigibilite, extinction, pertes,
                 conception_juridique, compatibilite_juridique,
                 souscription=0, collecteur="INST",
                 emploi_collecte=None, contrib_detenteur=0):
        self.cle, self.titre = cle, titre
        self.circulation = circulation
        self.inscription = inscription
        self.allocation = allocation
        self.beneficiaire = beneficiaire
        self.souscription = souscription
        self.collecteur = collecteur
        self.emploi_collecte = emploi_collecte
        self.contrib_detenteur = contrib_detenteur
        self.obligation = obligation
        self.passif_chez = passif_chez          # "INST" ou "receveur"
        self.compte_passif = compte_passif      # EMISES ou ALLOC
        self.droit_attache = droit_attache
        self.servi_par = servi_par              # "INST", "participants", None
        self.exigibilite = exigibilite          # "a_vue", "sans_decaissement"
        self.extinction = extinction
        self.pertes = pertes
        self.conception_juridique = conception_juridique
        self.compatibilite_juridique = compatibilite_juridique


# ---------------------------------------------------------------------
# Écritures
# ---------------------------------------------------------------------
def ouverture(b):
    p = []
    if b.souscription:
        p += [("ETAT", DEVISES, ACTIF, +b.souscription),
              ("ETAT", "report à nouveau", SN, +b.souscription)]
    if b.circulation in ("avoir_de_reserve", "collectif"):
        p += [("BCN2", DEVISES, ACTIF, +DEVISES_BCN2),
              ("BCN2", "report à nouveau", SN, +DEVISES_BCN2)]
    return p


def _emission(b):
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
        pass
    elif b.inscription != "hors_bilan":
        raise ValueError(b.inscription)
    return p, m


def _contribution(debiteur, montant, libelle_suffixe=""):
    """Une obligation PRÉSENTE du détenteur envers l'émetteur, avec son fait
    générateur, puis son règlement EN UNITÉS.

    Sans elle, le droit « remettre l'unité en règlement de ce qui est dû » ne
    porte sur rien : il resterait une possibilité future. Correction de
    l'auteur du 2026-09-09.
    """
    return [
        Ecriture(
            "Contribution statutaire due par %s — fait générateur%s"
            % (debiteur, libelle_suffixe),
            [("INST", "créance de contribution", ACTIF, +montant),
             ("INST", "report à nouveau", SN, +montant),
             (debiteur, DUE, PASSIF, +montant),
             (debiteur, "report à nouveau", SN, -montant)],
            {"INST": "produit de la contribution statutaire",
             debiteur: "contribution statutaire due à l'émetteur"}),
        Ecriture(
            "Contribution réglée EN UNITÉS : le droit du détenteur s'exerce%s"
            % libelle_suffixe,
            [(debiteur, AVOIRS, ACTIF, -montant),
             (debiteur, DUE, PASSIF, -montant),
             ("INST", "créance de contribution", ACTIF, -montant),
             ("INST", EMISES, PASSIF, -montant)])]


def _prelevement(b, compte, via_bcn):
    col = b.collecteur
    dette = ("dette de prélèvement" if col == "INST"
             else "dette de prélèvement fiscale")
    E = [Ecriture(
        "Prélèvement transactionnel — fait générateur (assiette : LA "
        "TRANSACTION, %d %% de %d)" % (100 * TAUX_PRELEVEMENT[0]
                                       // TAUX_PRELEVEMENT[1], D),
        [(col, "créance de prélèvement", ACTIF, +PRELEVEMENT),
         (col, "report à nouveau", SN, +PRELEVEMENT),
         ("RDM", dette, PASSIF, +PRELEVEMENT),
         ("RDM", "report à nouveau", SN, -PRELEVEMENT)],
        {col: "produit du prélèvement transactionnel",
         "RDM": "prélèvement transactionnel dû par le vendeur"})]
    regle = [("RDM", compte, ACTIF, -PRELEVEMENT),
             ("RDM", dette, PASSIF, -PRELEVEMENT),
             (col, "créance de prélèvement", ACTIF, -PRELEVEMENT)]
    if via_bcn:
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


def _emploi_collecte(b):
    """CE QUE LE COLLECTEUR FAIT DES UNITÉS PERÇUES, et cela décide de l'encours.

    Le collecteur détermine le DÉTENTEUR IMMÉDIAT. La règle d'emploi ultérieur
    détermine l'encours final. Correction de l'auteur du 2026-09-09.
    """
    if b.collecteur != "ETAT" or not b.emploi_collecte:
        return []
    if b.emploi_collecte == "conservation":
        return []
    if b.emploi_collecte == "remise_en_circulation":
        return [Ecriture(
            "Emploi : l'État REMET les unités en circulation (achat de biens)",
            [("ETAT", AVOIRS, ACTIF, -PRELEVEMENT),
             ("ETAT", "biens et services acquis, au coût", ACTIF, +PRELEVEMENT),
             ("RDM", AVOIRS, ACTIF, +PRELEVEMENT),
             ("RDM", "biens et capacités cédés", ACTIF, -PRELEVEMENT)])]
    if b.emploi_collecte == "transfert_emetteur":
        return _contribution("ETAT", PRELEVEMENT,
                             " (emploi des unités perçues)")
    raise ValueError(b.emploi_collecte)


def _demurrage(compte, via_bcn):
    E = [Ecriture(
        "Démurrage — fait générateur (assiette : L'ENCAISSE DÉTENUE, %d %% de "
        "%d)" % (100 * TAUX_DEMURRAGE[0] // TAUX_DEMURRAGE[1],
                 ASSIETTE_DEMURRAGE),
        [("INST", "créance de démurrage", ACTIF, +DEMURRAGE),
         ("INST", "report à nouveau", SN, +DEMURRAGE),
         ("RDM", "dette de démurrage", PASSIF, +DEMURRAGE),
         ("RDM", "report à nouveau", SN, -DEMURRAGE)],
        {"INST": "produit du démurrage sur les encaisses",
         "RDM": "démurrage supporté par le détenteur de l'encaisse"})]
    regle = [("RDM", compte, ACTIF, -DEMURRAGE),
             ("RDM", "dette de démurrage", PASSIF, -DEMURRAGE),
             ("INST", "créance de démurrage", ACTIF, -DEMURRAGE),
             ("INST", EMISES, PASSIF, -DEMURRAGE)]
    if via_bcn:
        regle += [("BQ", "dépôts du reste de l'économie", PASSIF, -DEMURRAGE),
                  ("BQ", "réserves à la banque centrale", ACTIF, -DEMURRAGE),
                  ("BCN", "réserves des banques", PASSIF, -DEMURRAGE),
                  ("BCN", AVOIRS, ACTIF, -DEMURRAGE)]
    E.append(Ecriture("Démurrage — règlement", regle))
    return E


def sequence(b):
    E = []
    if b.souscription:
        E.append(Ecriture(
            "Souscription : les membres dotent l'émetteur en devises",
            [("ETAT", DEVISES, ACTIF, -b.souscription),
             ("ETAT", "participation dans l'émetteur", ACTIF, +b.souscription),
             ("INST", DEVISES, ACTIF, +b.souscription),
             ("INST", "parts des souscripteurs", PASSIF, +b.souscription)]))
    p, m = _emission(b)

    if b.circulation == "collectif":
        # Chaque membre est le DÉBITEUR DÉTERMINÉ de sa propre allocation
        # [S1, § 12.49]. L'émetteur tient les comptes et n'est pas débiteur.
        for s in ("BCN", "BCN2"):
            p += [(s, AVOIRS, ACTIF, +M), (s, ALLOC, PASSIF, +M)]
        E.append(Ecriture("Allocation : avoirs à l'actif, allocation au passif "
                          "de CHAQUE membre receveur", p, m))
        E.append(Ecriture(
            "Échange entre participants : la BCN cède des avoirs contre des "
            "devises",
            [("BCN", AVOIRS, ACTIF, -ECHANGE), ("BCN", DEVISES, ACTIF, +ECHANGE),
             ("BCN2", DEVISES, ACTIF, -ECHANGE),
             ("BCN2", AVOIRS, ACTIF, +ECHANGE)]))
        return E

    if b.circulation == "avoir_de_reserve":
        p += [("BCN", AVOIRS, ACTIF, +M)]
        p += [("BCN", "report à nouveau", SN, +M)]
        m["BCN"] = ("allocation définitive : aucune contrepartie n'est exigible "
                    "par l'émetteur")
        E.append(Ecriture("Émission et allocation à la banque centrale", p, m))
        E.append(Ecriture(
            "Échange entre participants : la BCN cède des unités contre des "
            "devises",
            [("BCN", AVOIRS, ACTIF, -ECHANGE), ("BCN", DEVISES, ACTIF, +ECHANGE),
             ("BCN2", DEVISES, ACTIF, -ECHANGE),
             ("BCN2", AVOIRS, ACTIF, +ECHANGE)]))
        E += _contribution("BCN2", CONTRIBUTION)
        return E

    if b.circulation == "unite_directe":
        p += [("BEN", AVOIRS, ACTIF, +M)]
        if b.beneficiaire == "credit":
            p += [("BEN", "dette envers l'émetteur", PASSIF, +M)]
        else:
            p += [("BEN", "report à nouveau", SN, +M)]
            m["BEN"] = "allocation non remboursable : enrichissement net"
        E.append(Ecriture("Émission et allocation directe aux bénéficiaires",
                          p, m))
        E.append(Ecriture(
            "Dépense des bénéficiaires, réglée en unités",
            [("BEN", AVOIRS, ACTIF, -D),
             ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
             ("RDM", AVOIRS, ACTIF, +D),
             ("RDM", "biens et capacités cédés", ACTIF, -D)]))
        E += _prelevement(b, AVOIRS, False)
        E += _emploi_collecte(b)
        E += _demurrage(AVOIRS, False)
        return E

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
    else:
        # Une obligation conditionnelle dont la réalisation n'est pas probable
        # n'est pas reconnue comme passif [S1, glossaire] : à l'inception, la
        # branche conditionnelle s'écrit comme la subvention.
        p3 += [("BEN", "report à nouveau", SN, +M),
               ("ETAT", "report à nouveau", SN, -M)]
        m3["BEN"] = "allocation non remboursable : enrichissement net"
        m3["ETAT"] = "transfert définitif aux bénéficiaires"
    E.append(Ecriture("Versement aux bénéficiaires", p3, m3))

    E.append(Ecriture(
        "Dépense des bénéficiaires vers le reste de l'économie",
        [("BEN", "dépôts bancaires", ACTIF, -D),
         ("BEN", "ouvrage réalisé, au coût", ACTIF, +D),
         ("RDM", "dépôts bancaires", ACTIF, +D),
         ("RDM", "biens et capacités cédés", ACTIF, -D),
         ("BQ", "dépôts des bénéficiaires", PASSIF, -D),
         ("BQ", "dépôts du reste de l'économie", PASSIF, +D)]))

    E += _prelevement(b, "dépôts bancaires", True)
    E += _emploi_collecte(b)
    E += _demurrage("dépôts bancaires", True)
    if b.contrib_detenteur:
        E += _contribution("BCN", b.contrib_detenteur)
    return E


# ---------------------------------------------------------------------
# Passage et R1a
# ---------------------------------------------------------------------
def totaux(bilans, s):
    c = bilans[s]
    a = sum(v for (cpt, co), v in c.items() if co == ACTIF)
    p = sum(v for (cpt, co), v in c.items() if co == PASSIF)
    n = sum(v for (cpt, co), v in c.items() if co == SN)
    return a, p, n


def detenteurs(inst):
    """Les créanciers du moment : ceux qui tiennent l'unité, et pour combien."""
    return [(s, inst[s].get((AVOIRS, ACTIF), 0)) for s, _ in SECTEURS
            if inst[s].get((AVOIRS, ACTIF), 0) > 0]


def passif_total(b, inst):
    """Le total des passifs représentatifs de l'unité, QUEL QU'EN SOIT LE
    PORTEUR : l'émetteur dans les architectures A35a, chaque membre receveur
    dans l'architecture collective."""
    if b.passif_chez == "receveur":
        return sum(inst[s].get((ALLOC, PASSIF), 0) for s, _ in SECTEURS)
    return inst["INST"].get((EMISES, PASSIF), 0)


def _copie(bilans):
    return dict((s, dict(c)) for s, c in bilans.items())


def passer(b):
    bilans = dict((s, {}) for s, _ in SECTEURS)
    anomalies = []

    for (s, cpt, co, v) in ouverture(b):
        bilans[s][(cpt, co)] = bilans[s].get((cpt, co), 0) + v
    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append("[R1a] ouverture : le bilan de %s ne se ferme pas "
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
                anomalies.append("[R1a] opération %d : le bilan de %s ne se "
                                 "ferme pas (écart %+d)" % (i, s, a - p - n))
        for s in [k for k, _ in SECTEURS if k in sn_bougee]:
            if s not in e.motifs:
                anomalies.append("[R1a] opération %d : la situation nette de %s "
                                 "varie sans motif déclaré" % (i, s))
        if dsn:
            anomalies.append("[R1a] opération %d « %s » : la somme des "
                             "situations nettes varie de %+d"
                             % (i, e.libelle, dsn))
        # L'IDENTITÉ CENTRALE, contrôlée à CHAQUE étape et non à la fin :
        # le TOTAL DES PASSIFS REPRÉSENTATIFS DE L'UNITÉ, quel qu'en soit le
        # porteur, doit égaler le TOTAL DES AVOIRS chez les détenteurs. Le
        # porteur est l'émetteur dans les architectures A35a, et CHAQUE MEMBRE
        # RECEVEUR dans l'architecture collective. C'est ainsi que la qualité
        # de créancier migre.
        pt = passif_total(b, bilans)
        det = sum(v for _, v in detenteurs(bilans))
        if pt != det:
            anomalies.append(
                "[R1a] opération %d : passifs représentatifs %d, avoirs "
                "détenus %d — l'identité entre le total inscrit au passif, "
                "quel qu'en soit le porteur, et le total détenu est rompue"
                % (i, pt, det))
        chrono.append(("%d. %s" % (i, e.libelle), _copie(bilans)))

    for s, _ in SECTEURS:
        a, p, n = totaux(bilans, s)
        if a - p - n:
            anomalies.append("[R1a] bilan final de %s : ne se ferme pas "
                             "(écart %+d)" % (s, a - p - n))
    if b.passif_chez == "INST" and bilans["INST"].get((EMISES, PASSIF), 0) < 0:
        anomalies.append("[R1a] l'encours émis devient NÉGATIF")
    # miroir des contributions : l'émetteur face à des débiteurs variables
    v1 = bilans["INST"].get(("créance de contribution", ACTIF), 0)
    v2 = sum(bilans[s].get((DUE, PASSIF), 0) for s, _ in SECTEURS)
    if v1 != v2:
        anomalies.append("[R1a] miroir des contributions : %d contre %d"
                         % (v1, v2))
    for (s1, c1, k1), (s2, c2, k2) in MIROIRS:
        a1, a2 = bilans[s1].get((c1, k1), 0), bilans[s2].get((c2, k2), 0)
        if a1 != a2:
            anomalies.append("[R1a] miroir rompu : %s/%s = %d, %s/%s = %d"
                             % (s1, c1, a1, s2, c2, a2))
    return bilans, chrono, anomalies


# ---------------------------------------------------------------------
# R1b — qualification PROPOSÉE. Rien ici n'est calculé.
# ---------------------------------------------------------------------
def qualification(b, chrono):
    obs, reserves = [], []

    obs.append("obligation déclarée : %s" % ("oui" if b.obligation else "NON"))
    if not b.obligation:
        reserves.append("aucune obligation n'est déclarée : rien ne permet de "
                        "proposer la qualification de passif")

    if b.passif_chez == "receveur":
        obs.append("débiteur : CHAQUE MEMBRE RECEVEUR, pour sa propre "
                   "allocation — débiteur déterminé, et non collectif")
        obs.append("architecture DIFFÉRENTE de A35a, qui place le passif chez "
                   "l'émetteur ; ce n'est pas un défaut, c'est une "
                   "architecture concurrente")
    else:
        obs.append("débiteur : l'émetteur, pour la totalité de l'encours")

    # Le créancier MIGRE avec l'instrument.
    mouvements = []
    for libelle, inst in chrono:
        d = detenteurs(inst)
        if d:
            mouvements.append((libelle, d))
    if mouvements:
        finaux = mouvements[-1][1]
        obs.append("créanciers à la dernière étape : %s"
                   % ", ".join("%s pour %d" % (s, v) for s, v in finaux))
        porteurs = set()
        for _, d in mouvements:
            porteurs.update(s for s, _ in d)
        obs.append("la qualité de créancier a migré entre %d secteurs au cours "
                   "du circuit : %s" % (len(porteurs), ", ".join(sorted(porteurs))))
    else:
        reserves.append("personne ne détient l'unité à aucune étape")

    # L'obligation présente que l'unité peut éteindre est-elle MODÉLISÉE ?
    materialisee = False
    for libelle, inst in chrono:
        du = sum(inst[s].get((DUE, PASSIF), 0) for s, _ in SECTEURS)
        du += sum(inst[s].get(("dette de prélèvement", PASSIF), 0)
                  for s, _ in SECTEURS)
        du += sum(inst[s].get(("dette de démurrage", PASSIF), 0)
                  for s, _ in SECTEURS)
        if du:
            porteurs_du = set()
            for s, _ in SECTEURS:
                if (inst[s].get((DUE, PASSIF), 0)
                        or inst[s].get(("dette de prélèvement", PASSIF), 0)
                        or inst[s].get(("dette de démurrage", PASSIF), 0)):
                    porteurs_du.add(s)
            if any(inst[s].get((AVOIRS, ACTIF), 0) > 0 for s in porteurs_du):
                materialisee = True
                break
    if b.exigibilite == "sans_decaissement":
        if materialisee:
            obs.append("obligation présente du détenteur envers l'obligé : "
                       "MODÉLISÉE, avec son fait générateur — le droit "
                       "s'exerce sur quelque chose")
        else:
            reserves.append(
                "le droit consiste à remettre l'unité en règlement de ce qui "
                "est dû à l'émetteur, MAIS AUCUNE DETTE DE CE GENRE N'EST "
                "MODÉLISÉE chez un détenteur : le droit reste une possibilité "
                "future, et la qualification reste à examiner")

    return obs, reserves


# ---------------------------------------------------------------------
# R2 — liquidité, par scénario
# ---------------------------------------------------------------------
def liquidite(b, chrono):
    if b.exigibilite == "sans_decaissement":
        return {"type": "sans_objet"}

    if b.servi_par == "participants":
        # TROIS SCÉNARIOS SÉPARÉS, chacun évalué AU MOMENT OÙ IL S'EXERCERAIT.
        # Le stress n'est jamais la mesure ordinaire de la liquidité d'un
        # instrument : correction de l'auteur du 2026-09-09.
        def dispo(inst, demandeur):
            return sum(inst[s].get((DEVISES, ACTIF), 0) for s, _ in SECTEURS
                       if s not in ("INST", demandeur))

        avant = chrono[1][1] if len(chrono) > 1 else chrono[0][1]
        fin = chrono[-1][1]
        # LE PLAFOND DE DÉSIGNATION EST UNE CAPACITÉ D'ACCEPTATION, PAS UNE
        # DEMANDE. Une version antérieure le portait dans la colonne des
        # demandes, ce qui n'avait aucun sens : on comparait une capacité à une
        # ressource comme si c'était un besoin. Correction du 2026-09-09.
        #   plafond de règle = capacite_designation(allocation, avoirs)
        #   capacité effective = min(plafond de règle, devises encore détenues)
        # La règle dit ce qu'un participant peut être TENU d'accepter ; elle ne
        # crée pas les devises qu'il faudrait remettre.
        alloc = fin["BCN2"].get((ALLOC, PASSIF), 0)
        avoirs = fin["BCN2"].get((AVOIRS, ACTIF), 0)
        plafond = capacite_designation(alloc, avoirs)
        restantes = dispo(fin, "BCN")
        return {"type": "participants", "scenarios": [
            {"nom": "fonctionnement normal, par accord volontaire",
             "genre": "demande", "valeur": ECHANGE,
             "ressource": dispo(avant, "BCN"),
             "note": "demande courante, servie par les devises que l'autre "
                     "participant détient AVANT l'échange"},
            {"nom": "capacité résiduelle de désignation",
             "genre": "capacite", "valeur": plafond, "ressource": restantes,
             "effective": min(plafond, restantes),
             "note": "CE N'EST PAS UNE DEMANDE. La règle autoriserait "
                     "d'appeler %d de plus ; les devises encore détenues en "
                     "permettent %d. La contrainte effective est la "
                     "RESSOURCE, non la règle." % (plafond, restantes)},
            {"nom": "RUÉE : la totalité des détenteurs à la fois",
             "genre": "demande", "valeur": sum(v for _, v in detenteurs(fin)),
             "ressource": dispo(fin, None),
             "note": "scénario de STRESS, jamais l'état ordinaire de "
                     "liquidité"}]}

    lignes, pire = [], None
    for libelle, inst in chrono:
        exigible = sum(v for _, v in detenteurs(inst))
        couverture = sum(v for (cpt, co), v in inst["INST"].items()
                         if co == ACTIF and cpt in MOBILISABLES)
        lignes.append((libelle, exigible, couverture))
        if exigible > couverture and (pire is None
                                      or exigible - couverture > pire[1]):
            pire = (libelle, exigible - couverture, exigible, couverture)
    return {"type": "oblige", "lignes": lignes, "pire": pire}


def solvabilite(b, bilans):
    residu = passif_total(b, bilans)
    ressources = sum(v for (cpt, co), v in bilans["INST"].items()
                     if co == ACTIF and v > 0)
    return residu, ressources


# ---------------------------------------------------------------------
# L'arbre
# ---------------------------------------------------------------------
ACCEPT = ("accepter l'unité en règlement des contributions et prélèvements dus "
          "à l'émetteur, à sa valeur faciale")
CONVERT = ("remettre au détenteur des devises librement utilisables contre "
           "l'unité, à tout moment et à sa demande")
ECHANGE_STAT = ("obtenir des devises librement utilisables auprès des AUTRES "
                "participants, par accord ou sur désignation")
# R4a — CE QU'UNE INSTITUTION PROSPECTIVE DOIT CRÉER. Elle écrit son droit
# constitutif : personne ne le lui fournira.
JUR_A = ["les DROITS du détenteur, énumérés et opposables",
         "les OBLIGATIONS de l'émetteur, et leur fait générateur",
         "la GOUVERNANCE : qui décide d'émettre, et à quelle majorité",
         "le RETRAIT d'un participant, et le sort de ses unités",
         "la LIQUIDATION de l'institution, et le rang des détenteurs",
         "les IMMUNITÉS et privilèges de l'institution",
         "le RÈGLEMENT DES DIFFÉRENDS, entre participants et avec l'émetteur"]

# R4b — CE QU'ELLE NE PEUT PAS IGNORER. Une institution prospective crée son
# droit constitutif, mais elle devra être reconnue et fonctionner DANS des
# ordres juridiques qui existent déjà.
JUR_B = ["les traités en vigueur : statuts du Fonds et de la Banque, accords "
         "monétaires régionaux",
         "les droits nationaux : capacité d'une banque centrale à détenir "
         "l'unité, cours légal, contrôle des changes",
         "les normes comptables : classement de l'unité, consolidation, "
         "information financière",
         "le droit de l'Union et les droits régionaux, là où ils encadrent "
         "l'émission monétaire"]


def _mn(cle, titre, **kw):
    base = dict(circulation="monnaie_nationale", inscription="situation_nette",
                allocation="definitive", beneficiaire="subvention",
                obligation=ACCEPT, passif_chez="INST", compte_passif=EMISES,
                droit_attache="remettre l'unité en règlement de ce qui est dû "
                              "à l'émetteur",
                servi_par=None, exigibilite="sans_decaissement",
                extinction="par le prélèvement, le démurrage et les "
                           "contributions",
                pertes="l'émetteur, par sa situation nette",
                conception_juridique=JUR_A,
                compatibilite_juridique=JUR_B,
                contrib_detenteur=CONTRIB_DETENTEUR)
    base.update(kw)
    return Branche(cle, titre, **base)


BRANCHES = [
    _mn("B1", "Allocation gagée sur les reflux futurs",
        inscription="creance_reflux", allocation="engagement",
        obligation=None, contrib_detenteur=0,
        droit_attache="aucun droit exprès",
        extinction="par les reflux, dont la créance est inscrite d'avance",
        pertes="non désigné"),
    _mn("B2", "Prélèvement perçu PAR L'ÉMETTEUR, contribution du détenteur "
              "modélisée"),
    _mn("B3a", "Prélèvement perçu PAR L'ÉTAT, qui CONSERVE les unités",
        collecteur="ETAT", emploi_collecte="conservation",
        extinction="par le démurrage et la contribution ; le prélèvement "
                   "fiscal n'éteint rien tant que l'État conserve"),
    _mn("B3b", "Prélèvement perçu PAR L'ÉTAT, qui les REMET EN CIRCULATION",
        collecteur="ETAT", emploi_collecte="remise_en_circulation",
        extinction="par le démurrage et la contribution ; les unités remises "
                   "en circulation restent en encours"),
    _mn("B3c", "Prélèvement perçu PAR L'ÉTAT, qui les TRANSFÈRE À L'ÉMETTEUR",
        collecteur="ETAT", emploi_collecte="transfert_emetteur",
        extinction="par le démurrage, la contribution, et le reversement des "
                   "unités perçues"),
    _mn("B4", "Le bénéficiaire reçoit un crédit du guichet",
        beneficiaire="credit",
        extinction="par le reflux, les contributions et le remboursement",
        pertes="le bénéficiaire d'abord, le guichet ensuite"),
    _mn("B5", "Le bénéficiaire reçoit un droit monétaire conditionnel",
        beneficiaire="conditionnel",
        extinction="par le reflux ; la condition reste hors bilan",
        pertes="l'émetteur ; la condition n'étant pas probable, elle n'est pas "
               "reconnue [S1, glossaire]"),
    _mn("B6", "L'unité n'est inscrite nulle part chez l'émetteur",
        inscription="hors_bilan", obligation=None, contrib_detenteur=0,
        droit_attache="aucun", extinction="non définie", pertes="non désigné"),
    _mn("B12", "Comme B2, mais SANS obligation présente du détenteur",
        contrib_detenteur=0,
        extinction="par le prélèvement et le démurrage seuls"),
    Branche(
        "B7", "L'unité circule elle-même, allocation non remboursable",
        circulation="unite_directe", inscription="situation_nette",
        allocation=None, beneficiaire="subvention",
        obligation=ACCEPT, passif_chez="INST", compte_passif=EMISES,
        droit_attache="s'acquitter du prélèvement et du démurrage au moyen de "
                      "l'unité",
        servi_par=None, exigibilite="sans_decaissement",
        extinction="par le prélèvement et par le démurrage",
        pertes="l'émetteur, par sa situation nette",
        conception_juridique=JUR_A,
        compatibilite_juridique=JUR_B + [
            "les quatre conditions sous lesquelles un actif conçu comme moyen "
            "d'échange est enregistré comme monnaie [L19.C08]"]),
    Branche(
        "B8", "L'unité circule elle-même, le bénéficiaire recevant un prêt",
        circulation="unite_directe", inscription="creance_beneficiaire",
        allocation=None, beneficiaire="credit",
        obligation=ACCEPT, passif_chez="INST", compte_passif=EMISES,
        droit_attache="s'acquitter du prélèvement et du démurrage au moyen de "
                      "l'unité",
        servi_par=None, exigibilite="sans_decaissement",
        extinction="par le reflux et par le remboursement du bénéficiaire",
        pertes="le bénéficiaire d'abord, l'émetteur ensuite",
        conception_juridique=JUR_A + ["le contrat de prêt, et son rang"],
        compatibilite_juridique=JUR_B + ["les quatre conditions de L19.C08"]),
    Branche(
        "B9", "Conversion à vue, l'émetteur étant doté d'un capital souscrit",
        circulation="monnaie_nationale", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        souscription=M - PRELEVEMENT - DEMURRAGE - CONTRIB_DETENTEUR,
        contrib_detenteur=CONTRIB_DETENTEUR,
        obligation=CONVERT, passif_chez="INST", compte_passif=EMISES,
        droit_attache="obtenir des devises contre l'unité, à tout moment",
        servi_par="INST", exigibilite="a_vue",
        extinction="par le reflux, et par la conversion si elle est demandée",
        pertes="l'émetteur, puis les souscripteurs par leurs parts",
        conception_juridique=JUR_A + [
            "l'engagement de conversion, son plafond et ses conditions "
            "de suspension",
            "l'appel de capital, et son caractère exécutoire"],
        compatibilite_juridique=JUR_B + [
            "le droit budgétaire des souscripteurs, qui conditionne "
            "l'exigibilité de l'appel de capital"]),
    Branche(
        "B10", "Avoir de réserve non gagé, transféré entre participants",
        circulation="avoir_de_reserve", inscription="situation_nette",
        allocation="definitive", beneficiaire="subvention",
        obligation=ACCEPT, passif_chez="INST", compte_passif=EMISES,
        droit_attache="régler en unités les contributions dues à l'émetteur, "
                      "et céder l'unité à un autre participant contre devises",
        servi_par=None, exigibilite="sans_decaissement",
        extinction="par le règlement des contributions statutaires",
        pertes="l'émetteur, par sa situation nette",
        conception_juridique=JUR_A + [
            "l'accord d'échange volontaire entre participants",
            "le régime des contributions statutaires réglables en unités"],
        compatibilite_juridique=JUR_B),
    Branche(
        "B11", "Structure collective : le passif est chez CHAQUE MEMBRE "
               "RECEVEUR",
        circulation="collectif", inscription="aucune",
        allocation=None, beneficiaire="subvention",
        obligation=ECHANGE_STAT, passif_chez="receveur", compte_passif=ALLOC,
        droit_attache="obtenir des devises d'un AUTRE participant",
        servi_par="participants", exigibilite="a_vue",
        extinction="aucune dans ce cycle : l'allocation demeure au passif du "
                   "receveur",
        pertes="les participants, par le dispositif statutaire",
        conception_juridique=JUR_A + [
            "le mécanisme de désignation, ses plafonds et ses exemptions",
            "les accords d'échange volontaire, et leurs clauses de "
            "durée, de suspension et de sortie",
            "le régime des intérêts sur l'écart avoirs / allocation"],
        compatibilite_juridique=JUR_B + [
            "l'articulation avec le département qui tient les comptes, et "
            "le statut de ses écritures"]),
]


# ---------------------------------------------------------------------
# Restitution
# ---------------------------------------------------------------------
def imprimer_bilan(bilans, s):
    a, p, n = totaux(bilans, s)
    lignes = [(cpt, co, v) for (cpt, co), v in sorted(bilans[s].items()) if v]
    if not lignes:
        return
    print("      %-5s %s" % (s, NOM[s]))
    for co in (ACTIF, PASSIF, SN):
        for cpt, c, v in lignes:
            if c == co:
                print("            %-16s %-38s %+7d" % (COTE[co], cpt, v))
    print("            %-16s %-38s %+7d" % ("", "SITUATION NETTE", n))


def rendre(b):
    bilans, chrono, arith = passer(b)
    obs, reserves = qualification(b, chrono)
    liq = liquidite(b, chrono)
    residu, ressources = solvabilite(b, bilans)

    print("")
    print("=" * 78)
    print("%s — %s" % (b.cle, b.titre))
    print("=" * 78)
    print("  obligation : %s" % (b.obligation or "AUCUNE"))
    print("  passif inscrit chez : %s" % (
        "CHAQUE MEMBRE RECEVEUR" if b.passif_chez == "receveur"
        else "l'émetteur"))
    print("  droit attaché : %s" % b.droit_attache)
    print("  exigibilité : %s" % ("À VUE" if b.exigibilite == "a_vue"
                                  else "sans décaissement de l'obligé"))
    print("  extinction : %s" % b.extinction)
    print("  porteur du risque : %s" % b.pertes)

    print("")
    print("  R1a — COHÉRENCE ARITHMÉTIQUE (vérifiée mécaniquement selon")
    print("        les écritures posées, dont elle ne juge pas la validité)")
    if arith:
        for a in dict.fromkeys(arith):
            print("      %s" % a)
    else:
        print("      identités tenues à chaque opération, y compris")
        print("      « total des passifs représentatifs de l'unité, quel qu'en")
        print("      soit le porteur = total des avoirs chez les détenteurs »")

    print("")
    print("  R1b — QUALIFICATION PROPOSÉE (non calculée, à valider humainement)")
    for o in obs:
        print("      %s" % o)
    for r in reserves:
        print("      RÉSERVE : %s" % r)
    if arith:
        print("      => aucune qualification n'est proposée : l'arithmétique "
              "ne tient pas")
    elif reserves:
        print("      => QUALIFICATION À EXAMINER — proposition suspendue")
    else:
        print("      => PROPOSITION : passif de l'obligé désigné, sous réserve")
        print("         de la lecture des § 4.101 et 4.103 et de la validité")
        print("         juridique des obligations déclarées. NON ÉTABLI ICI.")

    print("")
    print("  R2 — LIQUIDITÉ (calculée, mais CONDITIONNELLE aux paramètres")
    print("       déclarés, dont aucun n'est calibré)")
    if liq["type"] == "sans_objet":
        print("      sans objet : l'obligé ne décaisse rien, il REÇOIT l'unité")
    elif liq["type"] == "participants":
        print("      servie par les AUTRES PARTICIPANTS, non par l'émetteur.")
        print("      TROIS SCÉNARIOS SÉPARÉS. Le troisième est un STRESS :")
        for sc in liq["scenarios"]:
            print("        %s" % sc["nom"])
            if sc["genre"] == "demande":
                etat = ("servie" if sc["valeur"] <= sc["ressource"]
                        else "MANQUE %d" % (sc["valeur"] - sc["ressource"]))
                print("          demande %3d | devises disponibles %3d | %s"
                      % (sc["valeur"], sc["ressource"], etat))
            else:
                print("          plafond de règle %3d | devises disponibles "
                      "%3d | capacité effective %3d"
                      % (sc["valeur"], sc["ressource"], sc["effective"]))
            print("          %s" % sc["note"])
        print("        plafond tiré de l'ARTICLE XIX § 4(a) des Statuts "
              "du Fonds [S2], lu")
        print("        dans le texte le 2026-09-09 : l'EXCÉDENT sur "
              "l'allocation est borné à")
        print("        deux allocations, donc le plafond TOTAL des avoirs vaut "
              "TROIS")
        print("        allocations. Et le § 4(b) permet de fournir AU-DELÀ : "
              "la limite borne")
        print("        l'OBLIGATION, jamais la possibilité.")
    else:
        print("      contrôlée à CHAQUE étape, au pic")
        for libelle, ex, co in liq["lignes"]:
            print("        %-50s %5d %6d%s" % (libelle[:50], ex, co,
                                               "  <<<" if ex > co else ""))
        if liq["pire"]:
            lib, ecart, ex, co = liq["pire"]
            print("      PIC : %s" % lib[:60])
            print("      exigible %d, mobilisable %d, MANQUE %d" % (ex, co,
                                                                    ecart))
            print("      => illiquide à cette date. Le passif existe.")
        else:
            print("      => servable à chaque étape")

    print("")
    print("  R3 — SOLVABILITÉ INTERTEMPORELLE : NON ÉVALUABLE")
    print("      un cycle unique, sans intérêt ni horizon. Sur ce cycle :")
    print("      passif résiduel %d, ressources de l'émetteur %d"
          % (residu, ressources))
    print("")
    print("  R4a — CONCEPTION JURIDIQUE À PRODUIRE (aucune n'existe)")
    print("      une institution prospective ÉCRIT son droit constitutif :")
    for e in b.conception_juridique:
        print("        à produire : %s" % e)
    print("")
    print("  R4b — COMPATIBILITÉ JURIDIQUE À ÉVALUER (non évaluée)")
    print("      mais elle devra être reconnue DANS des ordres qui existent :")
    for e in b.compatibilite_juridique:
        print("        à confronter : %s" % e)

    print("")
    print("  CHRONOLOGIE — DÉTENTEURS ET ENCOURS APRÈS CHAQUE OPÉRATION")
    for libelle, inst in chrono:
        d = detenteurs(inst)
        print("      %-52s passif %3d | %s" % (
            libelle[:52], passif_total(b, inst),
            ", ".join("%s %d" % (s, v) for s, v in d) or "aucun détenteur"))
    print("")
    print("  BILANS FINAUX")
    for s, _ in SECTEURS:
        imprimer_bilan(bilans, s)
    return {"cle": b.cle, "r1a": not arith,
            "r1b": ("—" if arith else ("à examiner" if reserves
                                       else "proposée")),
            "encours": residu,
            "r2": ("sans objet" if liq["type"] == "sans_objet"
                   else ("3 scénarios" if liq["type"] == "participants"
                         else ("servable" if liq["pire"] is None
                               else "TENSION")))}


def main():
    print("=" * 78)
    print("MATRICE COMPTABLE DE NEMO IMS — arbre A35b, version 3")
    print("=" * 78)
    print("Émission %d ; dépense %d ; prélèvement %d sur LA TRANSACTION ; "
          "démurrage %d" % (M, D, PRELEVEMENT, DEMURRAGE))
    print("sur L'ENCAISSE de %d ; contribution du détenteur %d. Repères, non "
          "estimations." % (ASSIETTE_DEMURRAGE, CONTRIB_DETENTEUR))
    print("")
    print("R1a VÉRIFIÉE selon les écritures posées | R1b PROPOSÉE | R2 "
          "CONDITIONNELLE")
    print("R3 NON ÉVALUABLE | R4a À PRODUIRE | R4b À ÉVALUER")
    print("Le programme ne peut PAS établir qu'un élément est un passif : il")
    print("propose une qualification, et elle attend une validation humaine.")

    res = [rendre(b) for b in BRANCHES]

    print("")
    print("=" * 78)
    print("RÉCAPITULATIF")
    print("=" * 78)
    print("  %-5s %-11s %-14s %-14s %s" % ("", "R1a", "R1b", "R2", "encours"))
    for r in res:
        print("  %-5s %-11s %-14s %-14s %d"
              % (r["cle"], "tenue" if r["r1a"] else "ROMPUE", r["r1b"],
                 r["r2"], r["encours"]))
    print("")
    print("A36 — LE COLLECTEUR ET L'EMPLOI, LUS SUR B2, B3a, B3b, B3c :")
    for r in res:
        if r["cle"] in ("B2", "B3a", "B3b", "B3c"):
            print("    %-5s encours final %d" % (r["cle"], r["encours"]))
    print("  À CIRCUIT ULTÉRIEUR INCHANGÉ, le choix du collecteur modifie")
    print("  l'encours IMMÉDIATEMENT APRÈS PERCEPTION. L'encours FINAL dépend")
    print("  ensuite de l'emploi des unités collectées.")
    print("")
    print("AUCUNE CONCLUSION EXCLUSIVE. Une branche non écrite n'est pas")
    print("rejetée, elle est absente. Les règles de qualification sont une")
    print("lecture de la norme, et elles attendent un comptable national.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
