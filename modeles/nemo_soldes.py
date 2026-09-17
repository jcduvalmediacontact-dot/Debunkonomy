#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÉSÉQUILIBRES COURANTS PERSISTANTS — version 2, 2026-09-09.

CINQ CORRECTIONS DE L'AUTEUR SUR LA VERSION 1, ET ELLES TOUCHENT LA STRUCTURE.

  (1) HORIZON. Chaque simulation va AU-DELÀ de l'échéance de toutes les
      facilités. Une maturité reportée hors de l'horizon n'est pas une
      résolution : c'est un report, et la version 1 le comptait comme un
      succès.

  (2) IDENTITÉ STOCK-FLUX COMPLÈTE. La version 1 affichait 499 de contraction
      d'un côté et 584 d'expansion de l'autre sans dire où passaient les 85.
      L'identité est désormais vérifiée à chaque période, et la réconciliation
      est publiée : l'écart est un EFFET DE PARITÉ, et il prouve que les masses
      monétaires nationales NE SONT PAS SOMMABLES entre pays.

  (3) UNE VARIATION DE MASSE MONÉTAIRE N'EST PAS UN EFFORT RÉEL. Le mot
      « effort » est retiré. Sont publiés SÉPARÉMENT : contraction, expansion,
      tension inflationniste, production, consommation essentielle et transfert
      réel de ressources. Aucun n'est agrégé avec un autre.

  (4) LES ÉCHANGES RÉPONDENT. Volumes élastiques à la parité relative, et
      rationnement par la capacité de paiement — les importations NON
      ESSENTIELLES cèdent les premières. Avec des flux exogènes, conclure
      qu'une charge n'arrête pas une accumulation était en partie tautologique.

  (5) UN PLAFOND EST UNE PROCÉDURE, PAS UN NOMBRE. Trois procédures sont
      implémentées — blocage, recyclage obligatoire des excédents, conversion
      du dépassement en contribution — et la première montre ce qu'un plafond
      sans procédure produit : il bloque le règlement, y compris celui des
      biens essentiels.

ARCHITECTURE DE RÉFÉRENCE, ARRÊTÉE LE 2026-09-09 : DEUX GUICHETS.

  FACILITÉ REMBOURSABLE pour un choc TEMPORAIRE.
  ALLOCATION SOLIDAIRE NON REMBOURSABLE pour un besoin essentiel STRUCTUREL
  qu'un pays ne peut financer par ses exportations sans sacrifier ces mêmes
  besoins. C'est la décision que l'auteur pose : sans elle, le dispositif ne
  protège les pays vulnérables que temporairement, avant de leur restituer la
  contraction sous forme de remboursement.

ET LA SYMÉTRIE NE SIGNIFIE PAS L'ÉGALITÉ DES SACRIFICES. Elle signifie que les
deux côtés ont une OBLIGATION D'AJUSTEMENT. La contribution est différenciée
selon la capacité, la cause du déséquilibre et le caractère essentiel des flux.

AUCUN SEUIL N'EST CALIBRÉ.

USAGE :  python modeles/nemo_soldes.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PAYS = [
    ("EXC", "Pays excédentaire, exportateur net"),
    ("DEF", "Pays déficitaire, importateur industriel"),
    ("PAU", "Pays pauvre, dépendant d'importations essentielles"),
]
CODES = [p for p, _ in PAYS]
NOM = dict(PAYS)
INST = "INST"
COMPTES = CODES + [INST]

# (1) HORIZON — au-delà de toute échéance.
PERIODES = 20
DUREE_FACILITE = 4
assert PERIODES > 3 * DUREE_FACILITE, "l'horizon doit dépasser les maturités"

# ---------------------------------------------------------------------
# PARAMÈTRES DÉCLARÉS. AUCUN N'EST CALIBRÉ.
# ---------------------------------------------------------------------
QUOTA = {"EXC": 1000, "DEF": 1000, "PAU": 400}
CORRIDOR = 0.25
TRANCHE_2 = 0.50
PLAFOND_SOLDE = 1.00          # (5) le plafond DUR, en fraction du quota
# Plafond propre aux soldes CRÉDITEURS, instruit pour la condition (3) d'A43 (3b) :
# None le rend égal au plafond dur, qui vaut alors des deux côtés.
PLAFOND_CREANCIER = None
TAUX_CHARGE_1 = 0.02
TAUX_CHARGE_2 = 0.04

PLAFOND_FACILITE = {"EXC": 0, "DEF": 300, "PAU": 300}
PERSISTANCE_STRUCTUREL = 5    # périodes de déficit essentiel avant allocation
PAS_PARITE = 0.05
PERSISTANCE_PARITE = 2

# RECYCLAGE EN PRÊT (D72, 2026-09-17) : part du solde positif du débiteur
# consacrée chaque période au remboursement. Déclarée, non calibrée.
REMBOURSEMENT_PRET = 0.5

# DÉCOUVERT DES GUICHETS APURÉ PAR LE REFLUX (D75, 2026-09-17). Le reflux du
# Symposium N'EST PAS modélisé : aucun flux d'apurement n'est donc supposé dans la
# configuration de l'auteur. La comparaison l'exprime en multiples du besoin moyen
# des guichets, que le modèle calcule au lieu de le recevoir.
MULTIPLES_REFLUX = (0.5, 1.0, 2.0, 4.0)

# RÈGLE DE RÉVISION DE L'AUTEUR — A43 (3b), condition (1), arrêtée le 2026-09-16.
# Deux repères DÉCLARÉS, non calibrés ; la durée d'une période reste abstraite.
PAS_GLISSEMENT_AUTEUR = 0.025
BUTEE_AUTEUR = 0.30

# (4) élasticité des échanges à la parité relative. Les postes ESSENTIELS
# sont inélastiques par définition : c'est ce qui les rend essentiels.
ELASTICITE = 0.8

SEUILS_CALIBRES = False

PROCEDURES = ("blocage", "recyclage", "conversion")


def echanges_de_base():
    v = dict(((a, b), 0) for a in CODES for b in CODES)
    v[("EXC", "DEF")] = 100
    v[("EXC", "PAU")] = 40
    v[("DEF", "EXC")] = 70
    v[("PAU", "EXC")] = 25
    v[("PAU", "DEF")] = 10
    return v


ESSENTIEL = {("EXC", "PAU"): True}
PRIX_BASE = 1.0


class Scenario(object):
    def __init__(self, cle, titre, choc, note):
        self.cle, self.titre, self.choc, self.note = cle, titre, choc, note


def sans_choc(t, volumes, prix):
    return volumes, prix


def choc_energetique(t, volumes, prix):
    """Choc TEMPORAIRE : trois périodes, puis retour."""
    if 3 <= t <= 5:
        prix = dict(prix)
        prix[("EXC", "PAU")] = PRIX_BASE * 2.0
        prix[("EXC", "DEF")] = PRIX_BASE * 1.5
    return volumes, prix


def choc_energetique_durable(t, volumes, prix):
    """Choc STRUCTUREL : il ne se retire pas. C'est le cas que la facilité
    remboursable ne peut pas traiter, et que l'allocation vise."""
    if t >= 3:
        prix = dict(prix)
        prix[("EXC", "PAU")] = PRIX_BASE * 2.0
    return volumes, prix


def mauvaise_recolte(t, volumes, prix):
    if 3 <= t <= 5:
        volumes = dict(volumes)
        volumes[("PAU", "EXC")] = 5
        volumes[("PAU", "DEF")] = 2
        volumes[("EXC", "PAU")] = 60
    return volumes, prix


def rupture_commerciale(t, volumes, prix):
    if t >= 4:
        volumes = dict(volumes)
        volumes[("DEF", "EXC")] = 10
    return volumes, prix


SCENARIOS = [
    Scenario("S0", "Référence, sans choc", sans_choc,
             "les déséquilibres de structure sont déjà là"),
    Scenario("S1", "Choc énergétique TEMPORAIRE", choc_energetique,
             "trois périodes puis retour : le cas que la facilité remboursable "
             "est censée traiter"),
    Scenario("S2", "Choc énergétique STRUCTUREL", choc_energetique_durable,
             "le prix ne redescend pas : le cas que la facilité NE PEUT PAS "
             "traiter, et qui décide de l'allocation non remboursable"),
    Scenario("S3", "Mauvaise récolte", mauvaise_recolte,
             "les exportations s'effondrent ET les achats vivriers montent"),
    Scenario("S4", "Rupture commerciale", rupture_commerciale,
             "un débouché se ferme durablement pour le déficitaire"),
]


class Etat(object):
    def __init__(self):
        self.solde = dict((c, 0.0) for c in COMPTES)
        self.masse = dict((c, 1000.0) for c in CODES)
        self.fac = dict((c, 0.0) for c in CODES)
        self.tirages = dict((c, []) for c in CODES)
        self.alloc = dict((c, 0.0) for c in CODES)      # non remboursable
        self.parite = dict((c, 1.0) for c in CODES)
        self.hors_corridor = dict((c, 0) for c in CODES)
        self.deficit_essentiel_persistant = dict((c, 0) for c in CODES)
        # périodes consécutives où l'excédentaire est au-delà du corridor
        self.attente_creancier = dict((c, 0) for c in CODES)
        # procédure structurelle : périodes consécutives en débit au-delà du
        # corridor, période d'ouverture (None si fermée), montants versés
        self.debit_persistant = dict((c, 0) for c in CODES)
        self.procedure_ouverte = dict((c, None) for c in CODES)
        self.procedure_close = dict((c, None) for c in CODES)
        self.structurel = dict((c, 0.0) for c in CODES)
        self.perte_reconnue = dict((c, 0.0) for c in CODES)
        # recyclage en PRÊT : dette par (débiteur, créancier), et ses mouvements
        self.dette = {}
        self.dette_creee = dict((c, 0.0) for c in CODES)
        self.rembourse_pret = dict((c, 0.0) for c in CODES)
        self.dette_annulee = dict((c, 0.0) for c in CODES)
        # découvert de l'institution pour les guichets et la reconversion (D75)
        self.verse_guichets = 0.0
        self.decouvert = 0.0
        self.apure = 0.0
        # accumulation d'un créancier au-delà du plafond (instruite le 2026-09-17)
        self.au_dela_plafond = dict((c, 0) for c in CODES)
        self.demurrage = dict((c, 0.0) for c in CODES)
        self.reliquat_converti = dict((c, 0.0) for c in CODES)
        self.placement = dict((c, 0.0) for c in CODES)
        self.placement_restitue = dict((c, 0.0) for c in CODES)
        self.apure_conversion = 0.0
        # procédure côté importateur (D79, instruite le 2026-09-17) : ouverture,
        # clôture, financement versé, surcoût mesuré de la facture essentielle
        self.imp_ouverte = dict((c, None) for c in CODES)
        self.imp_close = dict((c, None) for c in CODES)
        self.imp_verse = dict((c, 0.0) for c in CODES)
        self.surcout = dict((c, 0.0) for c in CODES)
        self.surcout_ouverture = dict((c, 0.0) for c in CODES)
        # sortie des dettes durables (D87, instruite le 2026-09-17)
        self.annule_sortie = dict((c, 0.0) for c in CODES)
        # (3) registres SÉPARÉS, jamais agrégés entre eux
        self.contraction = dict((c, 0.0) for c in CODES)
        self.expansion = dict((c, 0.0) for c in CODES)
        self.charges = dict((c, 0.0) for c in CODES)
        self.production = dict((c, 0.0) for c in CODES)
        self.essentiel_recu = dict((c, 0.0) for c in CODES)
        self.essentiel_voulu = dict((c, 0.0) for c in CODES)
        self.transfert_reel = dict((c, 0.0) for c in CODES)
        self.soldes_par_periode = dict((c, []) for c in CODES)


def plafond_creancier():
    """Le plafond des soldes créditeurs, en fraction du quota."""
    return PLAFOND_SOLDE if PLAFOND_CREANCIER is None else PLAFOND_CREANCIER


def charge_graduee(solde, quota):
    a, c1, c2 = abs(solde), CORRIDOR * quota, TRANCHE_2 * quota
    charge = 0.0
    if a > c1:
        charge += TAUX_CHARGE_1 * (min(a, c2) - c1)
    if a > c2:
        charge += TAUX_CHARGE_2 * (a - c2)
    return charge


OBLIGATIONS_CREANCIER = ("charge", "plafond", "parite")


def jouer(scenario, symetrie_contraignante=True, procedure="recyclage",
          allocation_active=True, regle=None, obligations_creancier=None,
          delai_creancier=0, charge_debiteur=True, procedure_structurelle=None,
          recyclage_pret=False, reflux_apurement=None, demurrage_soldes=0.0,
          reliquat_plafond=None, persistance_reliquat=0, procedure_importateur=None,
          quotas=None, sortie_dettes=None, recyclage_au_besoin=False,
          corridor_position_nette=False):
    """`symetrie_contraignante` reste l'interrupteur général des obligations de
    l'excédentaire. `obligations_creancier` choisit lesquelles s'appliquent
    parmi la charge graduée, la procédure au plafond et la révision de sa
    parité (toutes par défaut). `delai_creancier` ne les applique qu'après ce
    nombre de périodes consécutives au-delà du corridor : c'est la délibération
    avant activation (aucune par défaut). `charge_debiteur` prélève ou non la
    charge graduée sur les soldes débiteurs (oui par défaut, comme Keynes).

    `procedure_structurelle` (aucune par défaut) est un dictionnaire. Elle
    s'ouvre pour un pays resté `declencheur` périodes en débit au-delà du
    corridor. Tant qu'elle est ouverte et le pays hors corridor, `restriction`
    retire cette part de ses importations non essentielles. `reconversion`
    — {"delai", "part", "financement"} — rend, `delai` périodes après
    l'ouverture, cette `part` des exportations perdues, et verse pendant le
    délai `financement` fois leur valeur. `transfert` verse chaque période la
    valeur des exportations encore perdues. Les versements sont non
    remboursables, portés par l'institution. `duree`, si elle est donnée, clôt
    la procédure ce nombre de périodes après l'ouverture ; sans elle, elle ne
    se clôt jamais.

    `recyclage_pret` (non par défaut, le recyclage étant alors un transfert de
    solde) fait du recyclage un PRÊT sans intérêt : la dette est remboursée sur
    les soldes positifs futurs du débiteur, à raison de REMBOURSEMENT_PRET, et
    à la clôture d'une procédure structurelle la part qui correspond à la
    perte de débouché reconnue pendant qu'elle était ouverte est annulée.

    Tout ce que l'institution verse sans remboursement — allocations et
    reconversion — est tenu dans un registre de DÉCOUVERT. `reflux_apurement`
    (aucun par défaut) en apure cette quantité chaque période, au titre de
    l'excédent du reflux du Symposium, que ce modèle ne représente pas. AUCUN
    SOLDE N'EN EST AFFECTÉ, ni ceux des pays ni celui de l'institution : le
    registre compte ce que le reflux aurait à retirer, il ne le retire pas.

    Deux instruments contre l'accumulation d'un créancier, tranchés le
    2026-09-17 : la conversion est retenue (D77), le démurrage sur la
    compensation écarté (D78). `demurrage_soldes` (nul par défaut) retire
    chaque période cette fraction des soldes POSITIFS des pays au profit de
    l'institution : le démurrage uniforme de D76, appliqué aux soldes de
    compensation. `reliquat_plafond` (aucun par défaut) traite ce qui reste
    au-delà du plafond après recyclage et remboursements, pour un pays qui y
    est depuis plus de `persistance_reliquat` périodes : « conversion » le
    verse à l'institution sans retour, comme l'annulation des soldes
    créditeurs persistants que Keynes envisageait en 1943 ; « placement » le
    change en créance de long terme sur l'institution, hors compensation et
    sans effet sur la masse du pays, restituée quand il passe en débit.

    `procedure_importateur` (aucune par défaut), instruite pour D79, est un
    dictionnaire. Elle s'ouvre pour un pays resté `declencheur` périodes en
    déficit essentiel, si le SURCOÛT mesuré de sa facture d'importations
    essentielles — sa valeur aux volumes et prix courants, rapportée à sa
    valeur de base — atteint `surcout_min`. `reconversion` — {"delai", "part",
    "financement"} — verse chaque période `financement` fois la facture
    essentielle de base, sans remboursement, et réduit de `part`, `delai`
    périodes après l'ouverture, les volumes essentiels importés : c'est la
    réussite, que le modèle suppose ou non mais ne produit pas. Le financement
    dure `duree` périodes (le délai par défaut). `revue` : « cloture » l'arrête
    à cette échéance ; « prolongation » le poursuit tant que le surcoût mesuré
    reste au seuil ; « jalons » ne le poursuit que si le surcoût a DÉJÀ baissé
    d'au moins `progres_min` depuis l'ouverture, en restant au seuil ; les deux
    dans la limite de `plafond_factures` factures essentielles de base, ou de
    `plafond_financement` en valeur.

    `quotas` (les quotas déclarés par défaut) donne les quotas du jeu, dont le
    corridor et le plafond dur sont des fractions : condition (3) d'A43 (3b).

    `sortie_dettes` (aucune par défaut), instruite pour D87, est un dictionnaire.
    Au-delà d'une dette de recyclage de `seuil` quotas du débiteur, ses `modes`
    s'appliquent : « annulation » annule la part de la dette qui dépasse le
    seuil, au détriment des créanciers ; « plafond » cesse de prêter au débiteur
    au-delà du seuil ; « devaluation » libère sa parité de la butée, la règle de
    révision restant déclenchée par le solde hors corridor ; « devaluation_flux »
    fait glisser sa parité, sans butée, tant que ses échanges de la période sont
    déficitaires, quel que soit son solde ; « restriction » retire cette part
    (`restriction`) de ses importations non essentielles.

    `recyclage_au_besoin` (non par défaut) borne ce que chaque déficitaire reçoit
    du recyclage à son solde négatif : il ne repasse pas créditeur, et ce qui
    reste au-delà du plafond relève du reliquat. Par défaut, l'excès entier est
    réparti au prorata des besoins, même quand il les dépasse.

    `corridor_position_nette` (non par défaut) fait lire à la révision des
    parités la POSITION NETTE d'un pays — son solde, moins ses dettes de
    recyclage, plus ses créances — au lieu de son solde : le recyclage en prêt
    ramène le solde du débiteur dans le corridor sans rien changer à sa position."""
    assert reliquat_plafond in (None, "conversion", "placement"), reliquat_plafond
    # les quotas du jeu : ceux que la configuration donne, sinon les quotas déclarés
    quota = QUOTA if quotas is None else quotas
    modes_sortie = set((sortie_dettes or {}).get("modes", ()))
    assert modes_sortie <= {"annulation", "plafond", "devaluation", "devaluation_flux",
                            "restriction"}, modes_sortie
    e = Etat()
    journal, anomalies = [], []

    def dette_de(d):
        return sum(v for (x, k), v in e.dette.items() if x == d)

    def seuil_dette(d):
        return (sortie_dettes or {}).get("seuil", 1.0) * quota[d]

    def endette(d):
        """Le débiteur d dépasse-t-il le seuil de sortie des dettes durables ?"""
        return bool(modes_sortie) and dette_de(d) >= seuil_dette(d) - 1e-9

    def position(c):
        """Ce que la révision des parités lit : le solde, ou la position nette."""
        if not corridor_position_nette:
            return e.solde[c]
        return (e.solde[c] - dette_de(c)
                + sum(v for (x, k), v in e.dette.items() if k == c))
    retenues = set(OBLIGATIONS_CREANCIER if obligations_creancier is None
                   else obligations_creancier)
    assert retenues <= set(OBLIGATIONS_CREANCIER), retenues

    def tenu(c, obligation):
        """L'excédentaire c est-il tenu, à cette période, par cette obligation ?"""
        return (symetrie_contraignante and obligation in retenues
                and e.attente_creancier[c] >= delai_creancier)
    base = echanges_de_base()
    prix_base = dict((k, PRIX_BASE) for k in base)

    for t in range(1, PERIODES + 1):
        volumes, prix = scenario.choc(t, base, prix_base)

        # --- PROCÉDURE STRUCTURELLE : ouverture, reconversion, perte --------
        ps = procedure_structurelle
        perte = dict((c, 0.0) for c in CODES)
        if ps:
            # part des exportations de base perdue à cette période, AVANT toute
            # reconversion : un déficit persistant sans débouché perdu n'ouvre rien
            base_exp = dict((c, sum(v for (a, b), v in base.items() if a == c))
                            for c in CODES)
            perdu = dict((c, sum(max(0.0, v - volumes.get((a, b), 0))
                                 for (a, b), v in base.items() if a == c)) for c in CODES)
            for c in CODES:
                e.debit_persistant[c] = (e.debit_persistant[c] + 1
                                         if e.solde[c] < -CORRIDOR * quota[c] else 0)
                part_perdue = perdu[c] / base_exp[c] if base_exp[c] else 0.0
                if (e.procedure_ouverte[c] is None and e.debit_persistant[c]
                        >= ps.get("declencheur", PERSISTANCE_STRUCTUREL)
                        and part_perdue >= ps.get("perte_min", 0.0)):
                    e.procedure_ouverte[c] = t
                if (e.procedure_ouverte[c] is not None and e.procedure_close[c] is None
                        and ps.get("duree") is not None
                        and t >= e.procedure_ouverte[c] + ps["duree"]
                        and (t - e.procedure_ouverte[c]) % ps["duree"] == 0):
                    # REVUE : la part de la dette de recyclage qui correspond à la
                    # perte reconnue depuis la revue précédente est annulée. Puis,
                    # selon `revue` : « cloture » clôt à la première échéance ;
                    # « prolongation » maintient la procédure tant que la perte
                    # mesurée reste au-dessus du seuil.
                    dues = dict((k, v) for k, v in e.dette.items() if k[0] == c and v > 0)
                    total_du = sum(dues.values())
                    annule = min(total_du, e.perte_reconnue[c])
                    plafond = ps.get("plafond_annulation")
                    if plafond is not None:
                        annule = max(0.0, min(annule, plafond - e.dette_annulee[c]))
                    for k, v in dues.items():
                        e.dette[k] = v - annule * v / total_du
                    e.dette_annulee[c] += annule
                    e.perte_reconnue[c] = 0.0
                    epuise = plafond is not None and e.dette_annulee[c] >= plafond - 1e-9
                    if epuise or not (ps.get("revue", "cloture") == "prolongation"
                                      and part_perdue >= ps.get("perte_min", 0.0)):
                        # clôture ; si le plafond d'annulation est atteint, c'est un
                        # CONSTAT D'ÉCHEC, et la suite n'est plus une question de règle
                        e.procedure_close[c] = t
            rec = ps.get("reconversion")
            volumes = dict(volumes)
            for (a, b), vol0 in base.items():
                if e.procedure_ouverte[a] is None:
                    continue
                manque = max(0.0, vol0 - volumes.get((a, b), 0))
                if manque and rec and t >= e.procedure_ouverte[a] + rec["delai"]:
                    volumes[(a, b)] = volumes.get((a, b), 0) + rec["part"] * manque
                perte[a] += max(0.0, vol0 - volumes.get((a, b), 0)) * PRIX_BASE
            for c in CODES:
                if e.procedure_ouverte[c] is not None and e.procedure_close[c] is None:
                    e.perte_reconnue[c] += perte[c]

        # --- PROCÉDURE CÔTÉ IMPORTATEUR : ouverture, reconversion (D79) -----
        pi = procedure_importateur
        imp_finance = dict((c, False) for c in CODES)
        facture_base = dict((c, sum(v * PRIX_BASE for (a, b), v in base.items()
                                    if b == c and ESSENTIEL.get((a, b))))
                            for c in CODES)
        def plafond_imp(c):
            if pi.get("plafond_factures") is not None:
                return pi["plafond_factures"] * facture_base[c]
            return pi.get("plafond_financement")
        if pi:
            rec_i = pi.get("reconversion") or {}
            volumes = dict(volumes)

            def facture(c):
                return sum(volumes.get((a, b), 0) * prix.get((a, b), PRIX_BASE)
                           for (a, b) in base if b == c and ESSENTIEL.get((a, b)))
            for c in CODES:
                if not facture_base[c]:
                    continue
                # le surcoût du CHOC, avant toute reconversion : c'est lui qui ouvre
                surcout_choc = facture(c) / facture_base[c] - 1.0
                if (e.imp_ouverte[c] is None and e.deficit_essentiel_persistant[c]
                        >= pi.get("declencheur", PERSISTANCE_STRUCTUREL)
                        and surcout_choc >= pi.get("surcout_min", 0.0)):
                    e.imp_ouverte[c] = t
                    e.surcout_ouverture[c] = surcout_choc
                ouverte = e.imp_ouverte[c]
                if ouverte is not None and t >= ouverte + rec_i.get("delai", 0):
                    # la réussite SUPPOSÉE : une part des importations essentielles
                    # est remplacée par une production que le modèle ne représente pas
                    for (a, b) in base:
                        if b == c and ESSENTIEL.get((a, b)) and (a, b) in volumes:
                            volumes[(a, b)] *= (1.0 - rec_i.get("part", 0.0))
                e.surcout[c] = facture(c) / facture_base[c] - 1.0
                if ouverte is None or e.imp_close[c] is not None:
                    continue
                plafond = plafond_imp(c)
                if t < ouverte + pi.get("duree", rec_i.get("delai", 0)):
                    imp_finance[c] = True
                elif (pi.get("revue", "cloture") in ("prolongation", "jalons")
                        and e.surcout[c] >= pi.get("surcout_min", 0.0)
                        and (plafond is None or e.imp_verse[c] < plafond - 1e-9)
                        and (pi["revue"] == "prolongation"
                             or e.surcout[c] <= (1.0 - pi.get("progres_min", 0.25))
                             * e.surcout_ouverture[c])):
                    imp_finance[c] = True
                else:
                    e.imp_close[c] = t

        # --- (4) LES ÉCHANGES RÉPONDENT À LA PARITÉ RELATIVE ------------
        desire = {}
        for (a, b), vol in volumes.items():
            if not vol:
                continue
            if ESSENTIEL.get((a, b)):
                desire[(a, b)] = float(vol)          # inélastique, par définition
            else:
                ratio = e.parite[a] / e.parite[b]
                desire[(a, b)] = vol * (ratio ** ELASTICITE)
                if (ps and ps.get("restriction") and e.procedure_ouverte[b] is not None
                        and e.procedure_close[b] is None
                        and e.solde[b] < -CORRIDOR * quota[b]):
                    # restriction temporaire des importations non essentielles,
                    # levée dès le retour dans le corridor
                    desire[(a, b)] *= (1.0 - ps["restriction"])
                if "restriction" in modes_sortie and endette(b):
                    # sortie par restriction : un débiteur trop endetté limite ses
                    # importations non essentielles
                    desire[(a, b)] *= (1.0 - sortie_dettes.get("restriction", 0.30))

        # --- capacité de paiement, et RATIONNEMENT ----------------------
        # Les postes ESSENTIELS sont servis les premiers : c'est la
        # protection prioritaire des paiements essentiels.
        realise = dict(desire)
        essentiel_bloque = dict((c, 0.0) for c in CODES)
        for b in CODES:
            postes = [(a, b) for a in CODES if (a, b) in desire]
            ess = [k for k in postes if ESSENTIEL.get(k)]
            non_ess = [k for k in postes if not ESSENTIEL.get(k)]
            cout = sum(desire[k] * prix.get(k, PRIX_BASE) for k in postes)
            recettes = sum(desire[k] * prix.get(k, PRIX_BASE)
                           for k in desire if k[0] == b)
            capacite = (e.solde[b] + recettes + PLAFOND_SOLDE * quota[b]
                        + max(0.0, PLAFOND_FACILITE[b] - e.fac[b]))
            if procedure == "blocage":
                capacite = min(capacite, e.solde[b] + recettes
                               + PLAFOND_SOLDE * quota[b])
            manque = cout - capacite
            if manque <= 0:
                continue
            # on comprime d'abord le NON essentiel
            for k in non_ess:
                if manque <= 0:
                    break
                p = prix.get(k, PRIX_BASE)
                reduction = min(realise[k], manque / p)
                realise[k] -= reduction
                manque -= reduction * p
            # et si cela ne suffit pas, l'essentiel cède — et c'est un échec
            for k in ess:
                if manque <= 0:
                    break
                p = prix.get(k, PRIX_BASE)
                reduction = min(realise[k], manque / p)
                realise[k] -= reduction
                essentiel_bloque[b] += reduction * p
                manque -= reduction * p

        # --- flux réels et valeurs -------------------------------------
        vend = dict((c, 0.0) for c in CODES)
        achete = dict((c, 0.0) for c in CODES)
        ach_ess = dict((c, 0.0) for c in CODES)
        voulu_ess = dict((c, 0.0) for c in CODES)
        vol_vend = dict((c, 0.0) for c in CODES)
        reel_net = dict((c, 0.0) for c in CODES)
        for k, vol in realise.items():
            a, b = k
            p = prix.get(k, PRIX_BASE)
            vend[a] += vol * p
            achete[b] += vol * p
            vol_vend[a] += vol
            reel_net[a] -= vol
            reel_net[b] += vol
            if ESSENTIEL.get(k):
                ach_ess[b] += vol * p
        for k, vol in desire.items():
            if ESSENTIEL.get(k):
                voulu_ess[k[1]] += vol * prix.get(k, PRIX_BASE)

        # --- règlement --------------------------------------------------
        net = dict((c, vend[c] - achete[c]) for c in CODES)
        for c in CODES:
            e.solde[c] += net[c]

        # --- DEUX GUICHETS ---------------------------------------------
        tirage = dict((c, 0.0) for c in CODES)
        don = dict((c, 0.0) for c in CODES)
        for c in CODES:
            deficit_ess = max(0.0, min(-min(e.solde[c], 0.0), ach_ess[c]))
            e.deficit_essentiel_persistant[c] = (
                e.deficit_essentiel_persistant[c] + 1 if deficit_ess > 0 else 0)
            structurel = (e.deficit_essentiel_persistant[c]
                          >= PERSISTANCE_STRUCTUREL)
            if deficit_ess <= 0:
                continue
            if structurel and allocation_active:
                # ALLOCATION SOLIDAIRE, NON REMBOURSABLE
                don[c] = deficit_ess
                e.solde[c] += deficit_ess
                e.solde[INST] -= deficit_ess
                e.alloc[c] += deficit_ess
            else:
                marge = PLAFOND_FACILITE[c] - e.fac[c]
                montant = max(0.0, min(deficit_ess, marge))
                if montant:
                    tirage[c] = montant
                    e.solde[c] += montant
                    e.solde[INST] -= montant
                    e.fac[c] += montant
                    e.tirages[c].append((t, montant))

        # --- PROCÉDURE STRUCTURELLE : versements non remboursables ----------
        if ps:
            rec = ps.get("reconversion")
            for c in CODES:
                if e.procedure_ouverte[c] is None:
                    continue
                verse = 0.0
                if rec and t < e.procedure_ouverte[c] + rec["delai"]:
                    verse += rec.get("financement", 0.0) * perte[c]
                if ps.get("transfert") and e.procedure_close[c] is None:
                    verse += perte[c]
                if verse:
                    don[c] += verse
                    e.solde[c] += verse
                    e.solde[INST] -= verse
                    e.structurel[c] += verse

        # --- PROCÉDURE CÔTÉ IMPORTATEUR : financement non remboursable ----
        if pi:
            for c in CODES:
                if not imp_finance[c]:
                    continue
                verse = (pi.get("reconversion") or {}).get("financement", 0.0) * facture_base[c]
                if plafond_imp(c) is not None:
                    verse = max(0.0, min(verse, plafond_imp(c) - e.imp_verse[c]))
                if verse:
                    don[c] += verse
                    e.solde[c] += verse
                    e.solde[INST] -= verse
                    e.imp_verse[c] += verse

        # --- DÉCOUVERT DES GUICHETS : émis au besoin, apuré par le reflux --
        verse_t = sum(don.values())
        e.verse_guichets += verse_t
        e.decouvert += verse_t
        if reflux_apurement:
            apure_t = min(e.decouvert, reflux_apurement)
            e.decouvert -= apure_t
            e.apure += apure_t

        rembourse = dict((c, 0.0) for c in CODES)
        for c in CODES:
            restants = []
            for (t0, m) in e.tirages[c]:
                if t - t0 >= DUREE_FACILITE:
                    e.solde[c] -= m
                    e.solde[INST] += m
                    e.fac[c] -= m
                    rembourse[c] += m
                else:
                    restants.append((t0, m))
            e.tirages[c] = restants

        # --- obligations graduées, différenciées ------------------------
        for c in CODES:
            au_dela = e.solde[c] > CORRIDOR * quota[c]
            e.attente_creancier[c] = e.attente_creancier[c] + 1 if au_dela else 0
        charge = dict((c, 0.0) for c in CODES)
        for c in CODES:
            crediteur = e.solde[c] > 0
            if crediteur and not tenu(c, "charge"):
                continue
            if not crediteur and not charge_debiteur:
                continue
            m = charge_graduee(e.solde[c], quota[c])
            if m:
                e.solde[c] -= m
                e.solde[INST] += m
                e.charges[c] += m
                charge[c] = m

        # --- DÉMURRAGE SUR LES SOLDES POSITIFS (non tranché) --------------
        demurrage = dict((c, 0.0) for c in CODES)
        if demurrage_soldes:
            for c in CODES:
                if e.solde[c] > 0:
                    d = demurrage_soldes * e.solde[c]
                    e.solde[c] -= d
                    e.solde[INST] += d
                    e.demurrage[c] += d
                    demurrage[c] = d

        # --- (5) LE PLAFOND EST UNE PROCÉDURE ---------------------------
        recyclage = dict((c, 0.0) for c in CODES)
        recu = dict((c, 0.0) for c in CODES)
        if procedure in ("recyclage", "conversion"):
            for c in CODES:
                exces = e.solde[c] - plafond_creancier() * quota[c]
                if exces <= 0:
                    continue
                if not tenu(c, "plafond"):
                    continue          # l'excédentaire n'est pas tenu
                if procedure == "recyclage":
                    # il prête l'excès aux déficitaires, au prorata
                    besoins = dict((d, -min(e.solde[d], 0.0)) for d in CODES
                                   if d != c)
                    total = sum(besoins.values())
                    if total <= 0:
                        continue
                    for d, bes in besoins.items():
                        part = exces * bes / total
                        if recyclage_au_besoin:
                            # pas au-delà du besoin : le débiteur ne repasse pas créditeur
                            part = min(part, bes)
                        if "plafond" in modes_sortie:
                            # sortie par plafond : on ne prête plus au-delà du seuil
                            part = min(part, max(0.0, seuil_dette(d) - dette_de(d)))
                        if part <= 0:
                            continue
                        e.solde[c] -= part
                        e.solde[d] += part
                        recyclage[c] += part
                        recu[d] += part
                        if recyclage_pret:
                            e.dette[(d, c)] = e.dette.get((d, c), 0.0) + part
                            e.dette_creee[d] += part
                else:
                    # il verse l'excès à l'institution, sans retour
                    e.solde[c] -= exces
                    e.solde[INST] += exces
                    recyclage[c] += exces

        # --- RECYCLAGE EN PRÊT : remboursement sur les soldes positifs -----
        pret_net = dict((c, 0.0) for c in CODES)
        if recyclage_pret:
            for (d, c), du in sorted(e.dette.items()):
                if du <= 1e-12 or e.solde[d] <= 0:
                    continue
                remb = min(du, REMBOURSEMENT_PRET * e.solde[d])
                e.solde[d] -= remb
                e.solde[c] += remb
                e.dette[(d, c)] = du - remb
                e.rembourse_pret[d] += remb
                pret_net[d] -= remb
                pret_net[c] += remb

        # --- SORTIE PAR ANNULATION : la dette au-delà du seuil est annulée -----
        if "annulation" in modes_sortie:
            for d in CODES:
                total_du = dette_de(d)
                exces_dette = total_du - seuil_dette(d)
                if exces_dette <= 1e-9:
                    continue
                for cle_dette, du in list(e.dette.items()):
                    if cle_dette[0] == d and du > 0:
                        e.dette[cle_dette] = du - exces_dette * du / total_du
                e.dette_annulee[d] += exces_dette
                e.annule_sortie[d] += exces_dette

        # --- RELIQUAT AU-DELÀ DU PLAFOND, après recyclage et remboursements --
        converti = dict((c, 0.0) for c in CODES)
        for c in CODES:
            reste = e.solde[c] - plafond_creancier() * quota[c]
            e.au_dela_plafond[c] = e.au_dela_plafond[c] + 1 if reste > 1e-9 else 0
            if (reliquat_plafond is None or reste <= 1e-9 or not tenu(c, "plafond")
                    or e.au_dela_plafond[c] <= persistance_reliquat):
                continue
            e.solde[c] -= reste
            e.solde[INST] += reste
            if reliquat_plafond == "conversion":
                e.reliquat_converti[c] += reste
                converti[c] = reste
            else:
                # simple changement de forme de la créance : la masse ne bouge pas
                e.placement[c] += reste
        converti_t = sum(converti.values())
        if converti_t:
            # le reliquat converti est annulé CONTRE le découvert de l'institution
            apure_c = min(e.decouvert, converti_t)
            e.decouvert -= apure_c
            e.apure_conversion += apure_c
        if reliquat_plafond == "placement":
            for c in CODES:
                if e.placement[c] > 1e-12 and e.solde[c] < 0:
                    rendu = min(e.placement[c], -e.solde[c])
                    e.placement[c] -= rendu
                    e.solde[c] += rendu
                    e.solde[INST] -= rendu
                    e.placement_restitue[c] += rendu

        # --- parités administrées ---------------------------------------
        for c in CODES:
            dehors = abs(position(c)) > CORRIDOR * quota[c]
            e.hors_corridor[c] = e.hors_corridor[c] + 1 if dehors else 0
            if "devaluation_flux" in modes_sortie and endette(c) and net[c] < 0:
                # sortie par dévaluation jusqu'à l'équilibre des échanges : c'est la
                # dette qui la déclenche, non le solde, que le recyclage peut garder
                # dans le corridor ; elle s'arrête quand les échanges ne sont plus
                # déficitaires
                e.parite[c] *= (1.0 + PAS_GLISSEMENT_AUTEUR)
                e.hors_corridor[c] = 0
                continue
            if regle is not None:
                # RÈGLE DE RÉVISION FOURNIE : elle décide seule du moment et
                # de l'ampleur ; une parité changée remet le compteur à zéro.
                # L'obligation excédentaire délibérative reste un paramètre
                # du régime, non de la règle.
                if not dehors or (position(c) > 0 and not tenu(c, "parite")):
                    continue
                if position(c) < 0 and "devaluation" in modes_sortie and endette(c):
                    # sortie par dévaluation : la butée ne retient plus un débiteur
                    # dont la dette dépasse le seuil
                    nouvelle = e.parite[c] * (1.0 + PAS_GLISSEMENT_AUTEUR)
                else:
                    nouvelle = regle(position(c), quota[c], e.hors_corridor[c],
                                     e.parite[c])
                if nouvelle != e.parite[c]:
                    e.parite[c] = nouvelle
                    e.hors_corridor[c] = 0
                continue
            if e.hors_corridor[c] < PERSISTANCE_PARITE:
                continue
            crediteur = position(c) > 0
            if crediteur and not tenu(c, "parite"):
                continue
            e.parite[c] *= (1.0 - PAS_PARITE) if crediteur \
                else (1.0 + PAS_PARITE)
            e.hors_corridor[c] = 0

        # --- masses monétaires, et (2) L'IDENTITÉ ----------------------
        for c in CODES:
            flux_nemo = (net[c] + tirage[c] + don[c] - rembourse[c]
                         - charge[c] + recu[c] - recyclage[c] + pret_net[c]
                         - demurrage[c] - converti[c])
            variation = flux_nemo * e.parite[c]
            e.masse[c] += variation
            if variation < 0:
                e.contraction[c] += -variation
            else:
                e.expansion[c] += variation
            e.production[c] += vol_vend[c]
            e.essentiel_recu[c] += ach_ess[c]
            e.essentiel_voulu[c] += voulu_ess[c]
            e.transfert_reel[c] += reel_net[c]
            e.soldes_par_periode[c].append(e.solde[c])

        # --- CONTRÔLES --------------------------------------------------
        total = sum(e.solde[c] for c in COMPTES)
        if abs(total) > 1e-6:
            anomalies.append("[C1] période %d : somme des soldes %+.2f" % (t, total))
        for c in CODES:
            if e.masse[c] < -1e-9:
                # AJOUTÉ LE 2026-09-17 : ce contrôle manquait, et une conclusion
                # publiée la veille sur S4 en dépendait
                anomalies.append(
                    "[C8] période %d : la masse monétaire de %s est négative (%.0f) "
                    "— le drain extérieur cumulé dépasse sa masse initiale, et le "
                    "modèle ne représente pas la création intérieure qui devrait le "
                    "compenser" % (t, c, e.masse[c]))
            if e.fac[c] < -1e-9 or e.fac[c] > PLAFOND_FACILITE[c] + 1e-9:
                anomalies.append("[C2] période %d : facilité de %s hors bornes"
                                 % (t, c))
            if essentiel_bloque[c] > 1e-6:
                anomalies.append(
                    "[C3] période %d : %.1f d'importations ESSENTIELLES de %s "
                    "sont BLOQUÉES faute de règlement — la protection "
                    "prioritaire a cédé" % (t, essentiel_bloque[c], c))
            borne = (plafond_creancier() if e.solde[c] > 0 else PLAFOND_SOLDE) * quota[c]
            if abs(e.solde[c]) > borne + 1e-6:
                anomalies.append(
                    "[C6] période %d : le solde de %s (%+.0f) dépasse le "
                    "plafond dur (%.0f) — la procédure « %s » ne l'a pas "
                    "ramené" % (t, c, e.solde[c], borne, procedure))

        # (2) IDENTITÉ STOCK-FLUX, vérifiée à chaque période et par pays.
        for c in CODES:
            attendu = (net[c] + tirage[c] + don[c] - rembourse[c] - charge[c]
                       + recu[c] - recyclage[c] + pret_net[c]
                       - demurrage[c] - converti[c]) * e.parite[c]
            constate = e.masse[c] - (journal[-1]["masse"][c] if journal
                                     else 1000.0)
            if abs(attendu - constate) > 1e-6:
                anomalies.append(
                    "[C5] période %d : la variation de masse de %s vaut %.3f "
                    "et le flux NEMO converti en donne %.3f — l'identité "
                    "stock-flux est rompue" % (t, c, constate, attendu))

        journal.append({"t": t, "solde": dict(e.solde), "masse": dict(e.masse),
                        "fac": dict(e.fac), "alloc": dict(e.alloc),
                        "parite": dict(e.parite), "vol": dict(vol_vend),
                        "don": dict(don), "tirage": dict(tirage),
                        "bloque": dict(essentiel_bloque),
                        "recyclage": dict(recyclage), "recu": dict(recu),
                        "dette": dict((c, sum(v for (d, k), v in e.dette.items() if d == c))
                                      for c in CODES),
                        "decouvert": e.decouvert, "surcout": dict(e.surcout),
                        "converti": dict(e.reliquat_converti)})

    # --- (1) l'horizon couvre-t-il les maturités ? ----------------------
    for c in CODES:
        if e.tirages[c]:
            anomalies.append(
                "[C7] %s termine avec %d tirage(s) non échus : le report hors "
                "horizon n'est pas une résolution" % (c, len(e.tirages[c])))
    return e, journal, anomalies


def reconciliation(e):
    """(2) L'IDENTITÉ, ET CE QU'ELLE PROUVE.

    En unités NEMO, tout se boucle : la somme des soldes est nulle à chaque
    période, institution comprise. En monnaies nationales, RIEN NE SE BOUCLE —
    et l'écart est exactement l'effet des parités divergentes. C'est la preuve
    que les masses monétaires nationales NE SONT PAS SOMMABLES entre pays, et
    donc qu'on ne peut pas en tirer un « effort » agrégé.
    """
    contraction = sum(e.contraction[c] for c in CODES)
    expansion = sum(e.expansion[c] for c in CODES)
    return contraction, expansion, expansion - contraction


# ---------------------------------------------------------------------
# Restitution
# ---------------------------------------------------------------------
def rendre(scenario):
    print("")
    print("=" * 78)
    print("%s — %s" % (scenario.cle, scenario.titre))
    print("=" * 78)
    print("  %s" % scenario.note)

    e, journal, anomalies = jouer(scenario)

    print("")
    print("  CHRONOLOGIE — %d périodes, au-delà de toute maturité (%d)"
          % (PERIODES, DUREE_FACILITE))
    print("  %2s | %-26s | %-18s | %s"
          % ("t", "soldes NEMO", "facilité", "allocation NON remb."))
    for j in journal:
        if j["t"] % 2 and j["t"] != PERIODES:
            continue
        soldes = " ".join("%s%+5.0f" % (c, j["solde"][c]) for c in CODES)
        fac = " ".join("%s%4.0f" % (c, j["fac"][c]) for c in CODES
                       if PLAFOND_FACILITE[c])
        al = " ".join("%s%5.0f" % (c, j["alloc"][c]) for c in CODES)
        print("  %2d | %-26s | %-18s | %s" % (j["t"], soldes, fac, al))

    print("")
    print("  (3) REGISTRES SÉPARÉS — aucun n'est agrégé avec un autre")
    print("  %-5s %11s %11s %11s %12s %11s"
          % ("", "contraction", "expansion", "production", "essentiel",
             "transfert"))
    for c in CODES:
        recu = e.essentiel_recu[c]
        voulu = e.essentiel_voulu[c]
        taux = (100.0 * recu / voulu) if voulu else 100.0
        print("  %-5s %11.0f %11.0f %11.0f %10.0f %%  %11.0f"
              % (c, e.contraction[c], e.expansion[c], e.production[c],
                 taux, e.transfert_reel[c]))
    print("      « essentiel » = part des importations essentielles VOULUES")
    print("      qui ont été effectivement REÇUES. C'est le registre qui")
    print("      compte pour l'exigence de l'auteur — pas la masse monétaire.")

    contraction, expansion, ecart = reconciliation(e)
    print("")
    print("  (2) RÉCONCILIATION — et elle règle la question des 85")
    print("      contraction totale %.0f, expansion totale %.0f, écart %+.0f"
          % (contraction, expansion, ecart))
    print("      EN UNITÉS NEMO, tout se boucle : la somme des soldes est nulle")
    print("      à chaque période, institution comprise, et le contrôle C1 le")
    print("      vérifie. EN MONNAIES NATIONALES, rien ne se boucle — l'écart")
    print("      est l'effet des parités divergentes. CE QUE CELA PROUVE : les")
    print("      masses monétaires nationales NE SONT PAS SOMMABLES entre pays,")
    print("      et la version 1 avait tort d'en tirer un « effort » agrégé.")

    if anomalies:
        print("")
        print("  MANQUEMENTS")
        for a in dict.fromkeys(anomalies)[:8] if False else \
                list(dict.fromkeys(anomalies))[:8]:
            print("    %s" % a)
        reste = len(list(dict.fromkeys(anomalies))) - 8
        if reste > 0:
            print("    ... et %d autres du même type" % reste)
    return e, journal, anomalies


def comparer_procedures(scenario, plafond=0.30):
    """(5) UN PLAFOND EST UNE PROCÉDURE, PAS UN NOMBRE.

    À plafond large, les trois procédures donnent le même résultat : le plafond
    n'est jamais atteint, et la comparaison ne dit rien. ON LA JOUE DONC À
    PLAFOND CONTRAIGNANT — sans quoi on affirmerait ce que la sortie ne montre
    pas, et c'est la faute que ce modèle existe pour éviter.
    """
    global PLAFOND_SOLDE
    garde = PLAFOND_SOLDE
    print("")
    print("  (5) LE PLAFOND, SELON LA PROCÉDURE — joué à plafond CONTRAIGNANT")
    print("      (%.0f %% du quota au lieu de %.0f %% : au plafond large, les"
          % (100 * plafond, 100 * garde))
    print("      trois procédures sont indiscernables parce qu'aucune ne mord)")
    print("  %-12s %10s %13s %16s %12s"
          % ("procédure", "solde EXC", "essentiel PAU", "essentiel bloqué",
             "dépassements"))
    try:
        PLAFOND_SOLDE = plafond
        for proc in PROCEDURES:
            e, journal, anomalies = jouer(scenario, procedure=proc)
            bloque = sum(j["bloque"][c] for j in journal for c in CODES)
            voulu = e.essentiel_voulu["PAU"]
            taux = (100.0 * e.essentiel_recu["PAU"] / voulu) if voulu else 100.0
            depass = len([a for a in anomalies if a.startswith("[C6]")])
            print("  %-12s %10.0f %12.0f %% %16.0f %12d"
                  % (proc, e.soldes_par_periode["EXC"][-1], taux, bloque,
                     depass))
    finally:
        PLAFOND_SOLDE = garde
    print("      CE QUE LA SORTIE MONTRE. Le « blocage » est dépassé à CHAQUE")
    print("      période : un plafond sans procédure est un nombre, pas un")
    print("      mécanisme, et il ne ramène rien. Le recyclage et la conversion")
    print("      réduisent les dépassements et le solde.")
    print("      ET CE QU'ELLE NE MONTRE PAS : aucun paiement essentiel n'est")
    print("      bloqué dans aucune des trois. Le risque que l'auteur signalait")
    print("      ne se matérialise pas ICI — parce que le guichet d'allocation")
    print("      sert l'essentiel AVANT que le plafond ne morde. Retirer ce")
    print("      guichet ferait réapparaître le risque, et c'est vérifié.")


def jouer_a_parites(scenario, pas, **options):
    """Joue un scénario avec un pas de révision des parités donné, puis rend
    au paramètre sa valeur déclarée. Un pas nul donne des parités STRICTEMENT
    FIXES ; rien d'autre ne change."""
    global PAS_PARITE
    garde = PAS_PARITE
    try:
        PAS_PARITE = pas
        return jouer(scenario, **options)
    finally:
        PAS_PARITE = garde


def regle_mecanique(solde, quota, periodes_hors_corridor, parite):
    """La règle employée par défaut, écrite comme une règle fournie : un pas de
    PAS_PARITE après PERSISTANCE_PARITE périodes hors corridor. Elle sert à
    vérifier que le chemin des règles fournies reproduit exactement le modèle."""
    if periodes_hors_corridor < PERSISTANCE_PARITE:
        return parite
    return parite * (1.0 - PAS_PARITE) if solde > 0 else parite * (1.0 + PAS_PARITE)


def regle_de_revision_auteur(solde, quota, periodes_hors_corridor, parite):
    """CONDITION (1) D'A43 (3b) : LA RÈGLE DE RÉVISION DES PARITÉS, CHOISIE PAR
    L'AUTEUR LE 2026-09-16 PARMI QUATRE RÈGLES MESURÉES.

    « Tant qu'un pays reste hors du corridor, sa parité glisse de 2,5 % à
    chaque période — vers la réévaluation s'il est excédentaire, vers la
    dévaluation s'il est déficitaire. Aucune révision ne l'éloigne de plus de
    30 % de sa valeur de départ ; au-delà, la révision s'arrête et la procédure
    structurelle prend le relais. »

    Une formule, non un comité : elle ne s'anticipe pas et ne se bloque pas par
    un veto intéressé. De petits pas plutôt que des sauts. Les deux côtés
    bougent. Le modèle ne l'appelle qu'hors du corridor.

    Entrées, pour un pays et une période :
      solde                   solde NEMO cumulé (positif : créancier)
      quota                   quota du pays (CORRIDOR * quota = seuil toléré)
      periodes_hors_corridor  périodes consécutives hors du corridor
      parite                  parité courante (1.0 au départ)
    Sortie : la nouvelle parité. Rendre `parite` inchangée, c'est ne pas réviser.
    """
    if solde > 0:
        nouvelle = parite * (1.0 - PAS_GLISSEMENT_AUTEUR)
    else:
        nouvelle = parite * (1.0 + PAS_GLISSEMENT_AUTEUR)
    if abs(nouvelle - 1.0) > BUTEE_AUTEUR:
        # au-delà de la butée, la révision s'arrête : la perte durable d'un
        # débouché relève de la procédure structurelle, non du change
        return parite
    return nouvelle


def comparer_parites():
    """A43 (3), SCINDÉ PAR L'AUTEUR LE 2026-09-16 : PARITÉS ADMINISTRÉES
    CONTRE PARITÉS STRICTEMENT FIXES.

    Le même modèle, joué deux fois par scénario : révision des parités active,
    puis coupée. Dans ce modèle, la parité est le SEUL canal qui agit sur les
    volumes échangés : le SENS de l'effet est donc presque acquis d'avance. Ce
    que la comparaison apporte, c'est l'ORDRE DE GRANDEUR de ce que les autres
    instruments — charges, recyclage, guichets — doivent porter à sa place.
    """
    print("")
    print("  A43 (3) — PARITÉS ADMINISTRÉES (pas de %.0f %% après %d périodes hors"
          % (100 * PAS_PARITE, PERSISTANCE_PARITE))
    print("  corridor) CONTRE PARITÉS STRICTEMENT FIXES (pas nul)")
    print("  %-4s %-13s %16s %13s %15s %11s %12s"
          % ("", "parités", "contraction DEF", "solde EXC", "essentiel PAU",
             "alloc PAU", "dépassements"))
    for sc in SCENARIOS:
        for libelle, pas in (("administrées", PAS_PARITE), ("fixes", 0.0)):
            e, journal, anomalies = jouer_a_parites(sc, pas)
            voulu = e.essentiel_voulu["PAU"]
            taux = (100.0 * e.essentiel_recu["PAU"] / voulu) if voulu else 100.0
            print("  %-4s %-13s %16.0f %13.0f %14.1f %% %11.0f %12d"
                  % (sc.cle, libelle, e.contraction["DEF"],
                     e.soldes_par_periode["EXC"][-1], taux, e.alloc["PAU"],
                     len([a for a in anomalies if a.startswith("[C6]")])))
    s2 = [x for x in SCENARIOS if x.cle == "S2"][0]
    print("")
    print("  S2 À PARITÉS FIXES, SANS L'UN DES DEUX APPUIS")
    for libelle, options in (("sans allocation", {"allocation_active": False}),
                             ("symétrie délibérative",
                              {"symetrie_contraignante": False})):
        e, journal, anomalies = jouer_a_parites(s2, 0.0, **options)
        voulu = e.essentiel_voulu["PAU"]
        taux = (100.0 * e.essentiel_recu["PAU"] / voulu) if voulu else 100.0
        bloque = sum(j["bloque"][c] for j in journal for c in CODES)
        print("  %-22s solde EXC %6.0f, essentiel PAU %5.1f %%, bloqué %4.0f, "
              "dépassements %d"
              % (libelle, e.soldes_par_periode["EXC"][-1], taux, bloque,
                 len([a for a in anomalies if a.startswith("[C6]")])))
    print("      CE QUE LA SORTIE MONTRE. De S0 à S3, figer les parités accroît")
    print("      la contraction du déficitaire et le solde de l'excédentaire. Le")
    print("      pays pauvre reste servi en totalité, mais par le guichet")
    print("      d'allocation, qui verse davantage ; sans lui, au choc structurel,")
    print("      l'essentiel est bloqué. Sous obligation délibérative, l'excédent")
    print("      crève le plafond. Et en S4 AUCUN des deux régimes ne tient le")
    print("      plafond : la perte durable d'un débouché ne relève pas du change.")
    print("      CE QU'ELLE NE MONTRE PAS : un seuil acceptable de contraction —")
    print("      aucun n'est calibré —, ni l'inflation, les prix n'étant pas")
    print("      endogènes.")


def regle_proportionnelle_bornee(solde, quota, periodes_hors_corridor, parite):
    """CANDIDATE ÉCARTÉE LE 2026-09-16. Après PERSISTANCE_PARITE périodes hors
    corridor, un pas égal à la moitié de l'écart au corridor, borné à 10 %, avec
    la même butée que la règle de l'auteur. Correction comparable, mais des
    sauts jusqu'à 10 %, plus faciles à anticiper."""
    if periodes_hors_corridor < PERSISTANCE_PARITE:
        return parite
    pas = min(0.10, 0.5 * (abs(solde) / quota - CORRIDOR))
    nouvelle = parite * (1.0 - pas) if solde > 0 else parite * (1.0 + pas)
    return parite if abs(nouvelle - 1.0) > BUTEE_AUTEUR else nouvelle


def regle_crediteur_dabord(solde, quota, periodes_hors_corridor, parite):
    """CANDIDATE ÉCARTÉE LE 2026-09-16. L'excédentaire réévalue de 5 % après
    deux périodes hors corridor ; le déficitaire ne dévalue de 5 % qu'après
    quatre. Un choix de doctrine, que le modèle ne soutient pas."""
    if solde > 0:
        return parite * 0.95 if periodes_hors_corridor >= 2 else parite
    return parite * 1.05 if periodes_hors_corridor >= 4 else parite


def regle_glissement_lent(solde, quota, periodes_hors_corridor, parite):
    """CANDIDATE ÉCARTÉE LE 2026-09-16. Un pas de 1 % à chaque période hors
    corridor, sans butée : la même forme que la règle de l'auteur, trop lente."""
    return parite * 0.99 if solde > 0 else parite * 1.01


REGLES_MESUREES = (
    ("mécanique, par défaut", regle_mecanique),
    ("auteur : glissement + butée", regle_de_revision_auteur),
    ("proportionnelle bornée", regle_proportionnelle_bornee),
    ("créancier d'abord", regle_crediteur_dabord),
    ("glissement lent (1 %)", regle_glissement_lent),
)


# CONDITION (2) D'A43 (3b), ARRÊTÉE PAR L'AUTEUR LE 2026-09-17 : les obligations
# des excédentaires sont AUTOMATIQUES, sans vote d'activation — réévaluation de
# leur parité par la règle de l'auteur, recyclage de l'excès au-delà du plafond
# vers les déficitaires —, et AUCUNE CHARGE n'est prélevée sur les soldes, ni
# débiteurs ni créditeurs. Le financement des allocations passe à l'émission.
OPTIONS_AUTEUR = {
    "regle": regle_de_revision_auteur,
    "symetrie_contraignante": True,
    "obligations_creancier": ("plafond", "parite"),
    "delai_creancier": 0,
    "charge_debiteur": False,
    "procedure": "recyclage",
}


def mesurer_configuration(**options):
    """Synthèse d'une configuration sur les cinq scénarios : contraction du
    déficitaire cumulée de S0 à S3 et en S4, solde final de l'excédentaire
    cumulé de S0 à S3, dépassements du plafond dur, charges payées par
    l'excédentaire et le déficitaire, allocations versées, solde final de
    l'institution cumulé, et plus faible part d'importations essentielles
    servies au pays pauvre."""
    r = {"contraction": 0.0, "contraction_s4": 0.0, "solde_exc": 0.0,
         "depass": 0, "charges_exc": 0.0, "charges_def": 0.0,
         "allocations": 0.0, "institution": 0.0, "essentiel_min": 100.0,
         "masse_negative": 0}
    for sc in SCENARIOS:
        e, journal, anomalies = jouer(sc, **options)
        if sc.cle == "S4":
            r["contraction_s4"] = e.contraction["DEF"]
        else:
            r["contraction"] += e.contraction["DEF"]
            r["solde_exc"] += e.soldes_par_periode["EXC"][-1]
        r["depass"] += len([a for a in anomalies if a.startswith("[C6]")])
        r["masse_negative"] += len([a for a in anomalies if a.startswith("[C8]")])
        r["charges_exc"] += e.charges["EXC"]
        r["charges_def"] += e.charges["DEF"]
        r["allocations"] += sum(e.alloc[c] for c in CODES)
        r["institution"] += e.solde[INST]
        voulu = e.essentiel_voulu["PAU"]
        r["essentiel_min"] = min(r["essentiel_min"], 100.0 * e.essentiel_recu["PAU"]
                                 / voulu if voulu else 100.0)
    return r


def comparer_obligations():
    """A43 (3b), CONDITION (2) : QUELLE OBLIGATION DE L'EXCÉDENTAIRE FAIT LE
    TRAVAIL, CE QUE COÛTE UN DÉLAI D'ACTIVATION, ET CE QUE FONT LES CHARGES.

    Joué sous la règle de révision de l'auteur. La sortie doit porter le prix
    du choix de l'auteur autant que son effet : sans charge, l'institution ne
    perçoit rien, et les allocations doivent être financées ailleurs.
    """
    base = {"regle": regle_de_revision_auteur}
    print("")
    print("  (1) QUELLE OBLIGATION DE L'EXCÉDENTAIRE FAIT LE TRAVAIL")
    print("  %-26s %14s %12s %13s" % ("obligations tenues", "contr. S0-S3",
                                      "EXC S0-S3", "dépassements"))
    for libelle, oblig in (("aucune (délibérative)", ()), ("charge seule", ("charge",)),
                           ("plafond seul", ("plafond",)), ("parité seule", ("parite",)),
                           ("les trois", OBLIGATIONS_CREANCIER)):
        r = mesurer_configuration(obligations_creancier=oblig, **base)
        print("  %-26s %14.0f %12.0f %13d" % (libelle, r["contraction"],
                                             r["solde_exc"], r["depass"]))
    print("")
    print("  (2) CE QUE COÛTE UNE DÉLIBÉRATION AVANT ACTIVATION (les trois obligations)")
    print("  %-26s %14s %13s" % ("périodes d'attente", "contr. S0-S3", "dépassements"))
    for d in (0, 2, 4, 8, PERIODES):
        r = mesurer_configuration(delai_creancier=d, **base)
        print("  %-26s %14.0f %13d" % (d, r["contraction"], r["depass"]))
    print("")
    print("  (3) CE QUE FONT LES CHARGES, obligations automatiques")
    print("  %-34s %12s %8s %8s %9s %12s" % ("", "contr.S0-S3", "S4", "dépass.",
                                            "masse<0", "institution"))
    for libelle, opts in (
            ("charges des deux côtés", dict(base)),
            ("charges des seuls excédents", dict(base, charge_debiteur=False)),
            ("AUCUNE CHARGE — choix de l'auteur", dict(OPTIONS_AUTEUR)),
            ("aucune charge, mais conversion", dict(OPTIONS_AUTEUR,
                                                    procedure="conversion"))):
        r = mesurer_configuration(**opts)
        print("  %-34s %12.0f %8.0f %8d %9d %12.0f" % (libelle, r["contraction"],
                                                        r["contraction_s4"], r["depass"],
                                                        r["masse_negative"], r["institution"]))
    print("      CE QUE LA SORTIE MONTRE. La réévaluation de l'excédentaire fait")
    print("      l'essentiel du soulagement du déficitaire ; la charge seule n'en")
    print("      apporte aucun. Chaque période d'attente avant activation en retire.")
    print("      La charge sur les débiteurs les enfonce, celle sur les excédents")
    print("      détourne vers l'institution ce que le recyclage leur aurait prêté ;")
    print("      et la conversion, qui verse l'excès à l'institution, ne soulage pas")
    print("      le déficitaire en S4 comme le recyclage. ET LE PRIX DU CHOIX DE L'AUTEUR EST")
    print("      PUBLIÉ : sans charge, l'institution ne perçoit rien, et le solde")
    print("      qu'elle cumule est le plus négatif — les allocations devront être")
    print("      financées par l'émission, sous la règle d'émission et le reflux.")
    print("      CORRECTION DU 2026-09-17. « Plus aucun plafond n'est dépassé » en S4")
    print("      ne disait pas que le drain extérieur du déficitaire y dépasse sa masse")
    print("      initiale : la colonne « masse<0 » compte ces périodes, que le contrôle")
    print("      C8 signale désormais. C'est l'objet de la condition (5).")


# CONDITION (5) D'A43 (3b), ARRÊTÉE PAR L'AUTEUR LE 2026-09-17 (D72 à D74).
# La procédure s'ouvre sur un déficit persistant ET une perte mesurée d'au moins
# 30 % des exportations ; la reconversion est financée par l'émission, sans
# remboursement, pendant quatre périodes ; sa réussite N'EST PAS supposée ; la
# procédure se clôt à l'échéance, et la part de la dette de recyclage — un prêt —
# qui correspond à la perte reconnue pendant l'ouverture est alors annulée.
PROCEDURE_AUTEUR = {
    "declencheur": 5,
    "perte_min": 0.30,
    "reconversion": {"delai": 4, "part": 0.0, "financement": 1.0},
    "duree": 4,
    "revue": "cloture",
}
# CHAQUE SECTION DATÉE REPRODUIT LA CONFIGURATION DE SON MOMENT : une décision
# ultérieure ne doit pas changer rétroactivement des chiffres publiés.
#
# Conditions (5) et (4) — recyclage en prêt, procédure structurelle (D72 à D75).
OPTIONS_AVANT_D77 = dict(OPTIONS_AUTEUR, recyclage_pret=True,
                         procedure_structurelle=PROCEDURE_AUTEUR, reliquat_plafond=None)
# L'accumulation de l'exportateur (D77, D78) : ce qui reste au-delà du plafond après
# recyclage est converti, c'est-à-dire annulé contre le découvert de l'institution ;
# le démurrage ne s'applique pas aux soldes de compensation (il reste nul ici).
OPTIONS_AVANT_D80 = dict(OPTIONS_AVANT_D77, reliquat_plafond="conversion")
# La procédure côté importateur (D79, instruite en D80 à D82) : ouverture sur un
# déficit essentiel persistant ET un surcoût d'au moins 30 % de la facture
# essentielle ; financement non remboursable de la facture de base pendant quatre
# périodes ; au-delà, seulement si le surcoût a déjà baissé d'au moins 25 %, dans la
# limite de huit factures de base. SA RÉUSSITE N'EST PAS SUPPOSÉE.
PROCEDURE_IMPORTATEUR_AUTEUR = {
    "declencheur": PERSISTANCE_STRUCTUREL,
    "surcout_min": 0.30,
    "reconversion": {"delai": 4, "part": 0.0, "financement": 1.0},
    "revue": "jalons",
    "progres_min": 0.25,
    "plafond_factures": 8,
}
OPTIONS_AVANT_D83 = dict(OPTIONS_AVANT_D80,
                         procedure_importateur=PROCEDURE_IMPORTATEUR_AUTEUR)


def quotas_proportionnels(base_de, total=None):
    """Des quotas de même total que les quotas déclarés, proportionnels aux
    importations, aux exportations ou au commerce total de chaque pays."""
    echanges = echanges_de_base()
    total = float(sum(QUOTA.values())) if total is None else total
    poids = dict((c, sum(v for (a, b), v in echanges.items()
                         if (base_de in ("importations", "commerce") and b == c)
                         or (base_de in ("exportations", "commerce") and a == c)))
                 for c in CODES)
    return dict((c, total * poids[c] / float(sum(poids.values()))) for c in CODES)


# LES SEUILS DU PLAFOND — condition (3) d'A43 (3b), choix de l'auteur du 2026-09-17.
# D83 : les quotas sont proportionnels aux importations, à total inchangé. D84 : le
# plafond dur vaut 100 % du quota, des deux côtés (PLAFOND_SOLDE, sans plafond
# créancier distinct). D85 : le corridor vaut 25 % du quota (CORRIDOR). Les deux
# derniers étaient les repères déclarés ; ils deviennent des choix, non calibrés.
QUOTAS_AUTEUR = quotas_proportionnels("importations")
OPTIONS_AVANT_D88 = dict(OPTIONS_AVANT_D83, quotas=QUOTAS_AUTEUR)
# LA SORTIE DES DETTES DURABLES — D87 instruite, choix de l'auteur du 2026-09-17. D88 : la
# révision des parités lit la POSITION NETTE (solde, moins les dettes de recyclage, plus
# les créances), que le recyclage en prêt ne ramène pas dans le corridor. D89 : au-delà
# du seuil, la dette de recyclage est annulée, et la parité du débiteur glisse sans butée
# tant que ses échanges de la période sont déficitaires. D90 : le seuil vaut un quota du
# débiteur. L'INFLATION QU'IMPORTERAIT LA DÉVALUATION N'EST PAS REPRÉSENTÉE.
SORTIE_DETTES_AUTEUR = {"modes": ("annulation", "devaluation_flux"), "seuil": 1.0}
OPTIONS_AUTEUR_COMPLETES = dict(OPTIONS_AVANT_D88, corridor_position_nette=True,
                                sortie_dettes=SORTIE_DETTES_AUTEUR)


def jouer_a_horizon(scenario, horizon, **options):
    """Joue un scénario sur un horizon donné, puis rend à PERIODES sa valeur."""
    global PERIODES
    garde = PERIODES
    try:
        PERIODES = horizon
        return jouer(scenario, **options)
    finally:
        PERIODES = garde


def jouer_avec_seuils(scenario, horizon, corridor=None, plafond=None,
                      plafond_creancier_=None, quotas=None, **options):
    """Joue un scénario sous d'autres seuils — corridor et plafond dur en fraction du
    quota, plafond propre aux créanciers, quotas — puis rend les seuils déclarés."""
    global CORRIDOR, PLAFOND_SOLDE, PLAFOND_CREANCIER
    garde = (CORRIDOR, PLAFOND_SOLDE, PLAFOND_CREANCIER)
    try:
        if corridor is not None:
            CORRIDOR = corridor
        if plafond is not None:
            PLAFOND_SOLDE = plafond
        if plafond_creancier_ is not None:
            PLAFOND_CREANCIER = plafond_creancier_
        if quotas is not None:
            options = dict(options, quotas=dict(quotas))
        return jouer_a_horizon(scenario, horizon, **options)
    finally:
        CORRIDOR, PLAFOND_SOLDE, PLAFOND_CREANCIER = garde


def mesurer_s4(horizon, **options):
    """Ce que la perte durable d'un débouché fait au déficitaire, au créancier
    et à l'institution, sur un horizon donné."""
    s4 = [x for x in SCENARIOS if x.cle == "S4"][0]
    e, journal, anomalies = jouer_a_horizon(s4, horizon, **options)
    negatifs = [a for a in anomalies if a.startswith("[C8]")]
    premiere = int(negatifs[0].split("période ")[1].split(" ")[0]) if negatifs else None
    return {"masse_min": min(p["masse"]["DEF"] for p in journal),
            "premiere_negative": premiere, "negatifs": len(negatifs),
            "recycle": sum(p["recyclage"]["EXC"] for p in journal),
            "dette": journal[-1]["dette"]["DEF"], "annulee": e.dette_annulee["DEF"],
            "creee": e.dette_creee["DEF"], "remboursee": e.rembourse_pret["DEF"],
            "institution": e.solde[INST], "exportations": e.production["DEF"],
            "ouverte": e.procedure_ouverte["DEF"], "close": e.procedure_close["DEF"],
            "identite": len([a for a in anomalies if a.startswith("[C5]")])}


def comparer_procedure_structurelle():
    """A43 (3b), CONDITION (5) : LA PERTE DURABLE D'UN DÉBOUCHÉ.

    La sortie publie d'abord la correction qui a ouvert ce chantier, puis la
    procédure de l'auteur sans supposer la réussite de la reconversion, puis le
    choix de revue qui lui a été posé, et le prix de celui qu'il a retenu.
    """
    print("")
    print("  (1) LA CORRECTION : SANS PROCÉDURE, LE DRAIN DÉPASSE LA MASSE INITIALE")
    for libelle, opts in (("défaut du modèle", {}),
                          ("configuration de l'auteur, conditions (1) et (2)",
                           dict(OPTIONS_AUTEUR))):
        r = mesurer_s4(PERIODES, **opts)
        print("  %-52s masse minimale %6.0f, négative dès la période %s"
              % (libelle, r["masse_min"], r["premiere_negative"]))
    print("")
    print("  (2) LA PROCÉDURE DE L'AUTEUR — réussite de la reconversion NON supposée,")
    print("      puis jouée à 25 % et 50 % ; recyclage en prêt ; clôture à l'échéance")
    print("  %-9s %-8s %9s %9s %9s %9s %11s %s" % ("réussite", "horizon", "masse min",
                                              "recyclé", "dette", "annulée",
                                              "institution", "ouverte→close"))
    for part in (0.0, 0.25, 0.5):
        proc = dict(PROCEDURE_AUTEUR,
                    reconversion=dict(PROCEDURE_AUTEUR["reconversion"], part=part))
        for h in (40, 60):
            r = mesurer_s4(h, **dict(OPTIONS_AVANT_D77, procedure_structurelle=proc))
            print("  %-9s %-8d %9.0f %9.0f %9.0f %9.0f %11.0f %s→%s"
                  % ("%d %%" % (100 * part), h, r["masse_min"], r["recycle"], r["dette"],
                     r["annulee"], r["institution"], r["ouverte"], r["close"]))
    print("")
    print("  (3) LA RÈGLE DE REVUE, reconversion ratée, 60 périodes — le choix posé")
    for libelle, extra in (("clôture à l'échéance — CHOIX DE L'AUTEUR", {}),
                           ("prolongation", {"revue": "prolongation"}),
                           ("prolongation, annulation plafonnée au quota",
                            {"revue": "prolongation",
                             "plafond_annulation": float(QUOTA["DEF"])})):
        r = mesurer_s4(60, **dict(OPTIONS_AVANT_D77,
                                  procedure_structurelle=dict(PROCEDURE_AUTEUR, **extra)))
        print("  %-46s le déficitaire doit %6.0f, le créancier perd %6.0f"
              % (libelle, r["dette"], r["annulee"]))
    print("      CE QUE LA SORTIE MONTRE. Le financement de la reconversion garde la")
    print("      masse du déficitaire positive, que la reconversion réussisse ou non.")
    print("      Sous recyclage, la reconversion ne change pas sa monnaie : elle")
    print("      réduit ce que le créancier doit lui recycler, donc sa dette. ET LE")
    print("      PRIX DU CHOIX DE L'AUTEUR EST PUBLIÉ : si la reconversion échoue, la")
    print("      procédure close laisse au déficitaire une dette de recyclage qui")
    print("      dépasse son quota, et la suite n'est écrite nulle part.")
    print("      CE QU'ELLE NE MONTRE PAS : la réussite d'une reconversion — le modèle")
    print("      la suppose ou non, il ne la produit pas —, ni aucun calibrage.")


def besoins_des_guichets(horizon, **options):
    """Ce que l'institution verse SANS REMBOURSEMENT, période par période et par
    scénario : allocations et reconversion. La facilité, qui se rembourse, n'y
    entre pas."""
    besoins = {}
    for sc in SCENARIOS:
        _, journal, _ = jouer_a_horizon(sc, horizon, **options)
        besoins[sc.cle] = [sum(p["don"].values()) for p in journal]
    return besoins


def besoin_moyen(besoins):
    """LE REPÈRE DU REFLUX : le besoin moyen par période, tous scénarios confondus.
    Il est tiré des besoins eux-mêmes, faute de reflux modélisé."""
    return (sum(sum(s) for s in besoins.values())
            / float(sum(len(s) for s in besoins.values())))


def mesurer_apurement(scenario, horizon, reflux, **options):
    """Le découvert des guichets sous un flux d'apurement donné : pic, premier
    versement, périodes entre le premier versement et le retour DÉFINITIF à zéro
    — None s'il n'y revient pas dans l'horizon, 0 s'il ne passe jamais d'une
    période à l'autre —, et ce qui reste à l'horizon."""
    e, journal, _ = jouer_a_horizon(scenario, horizon,
                                    **dict(options, reflux_apurement=reflux))
    premier = next((p["t"] for p in journal if sum(p["don"].values()) > 1e-9), None)
    positifs = [p["t"] for p in journal if p["decouvert"] > 1e-9]
    if not positifs:
        apure_en = 0
    elif positifs[-1] == journal[-1]["t"]:
        apure_en = None
    else:
        apure_en = positifs[-1] + 1 - premier + 1
    return {"verse": e.verse_guichets, "allocations": sum(e.alloc.values()),
            "reconversion": sum(e.structurel.values()), "premier": premier,
            "pic": max(p["decouvert"] for p in journal), "apure_en": apure_en,
            "reste": e.decouvert, "apure": e.apure}


def calendrier_reflux_seul(besoin, flux):
    """Si les guichets ne pouvaient verser que le reflux déjà reçu : ce qui
    manquerait au moment du besoin sous ce flux, le flux constant minimal pour
    que rien ne manque, et le fonds à constituer d'avance si le flux égale le
    besoin moyen du scénario lui-même.

    MESURE DE CALENDRIER SUR LA TRAJECTOIRE FINANCÉE. Ce n'est pas la simulation
    d'un régime sans émission, où les versements manquants changeraient la
    trajectoire elle-même."""
    propre = sum(besoin) / float(len(besoin))
    reserve = manque = cumul = flux_minimal = fonds = 0.0
    for t, verse in enumerate(besoin, 1):
        reserve += flux - verse
        if reserve < 0:
            manque -= reserve
            reserve = 0.0
        cumul += verse
        flux_minimal = max(flux_minimal, cumul / t)
        fonds = max(fonds, cumul - propre * t)
    return {"manque": manque, "flux_minimal": flux_minimal, "flux_propre": propre,
            "fonds_prealable": fonds}


def mesurer_incidence_allocation(horizon, allocation_active, **options):
    """S2, le choc structurel : où aboutit ce que l'allocation émet. Le même jeu
    se joue avec et sans le guichet d'allocation."""
    s2 = [x for x in SCENARIOS if x.cle == "S2"][0]
    e, journal, anomalies = jouer_a_horizon(
        s2, horizon, **dict(options, allocation_active=allocation_active))
    voulu = e.essentiel_voulu["PAU"]

    def depassements(c):
        return [int(a.split("période ")[1].split(" ")[0]) for a in anomalies
                if a.startswith("[C6]") and "le solde de %s " % c in a]
    exc, pau = depassements("EXC"), depassements("PAU")
    return {"essentiel": 100.0 * e.essentiel_recu["PAU"] / voulu if voulu else 100.0,
            "contraction_pau": e.contraction["PAU"], "exportations_pau": e.production["PAU"],
            "parite_pau": e.parite["PAU"], "plafond_pau": len(pau),
            "solde_exc": e.solde["EXC"], "parite_exc": e.parite["EXC"],
            "plafond_exc": len(exc), "premier_plafond_exc": exc[0] if exc else None,
            "recycle_exc": sum(p["recyclage"]["EXC"] for p in journal),
            "institution": e.solde[INST]}


def comparer_financement_guichets():
    """A43 (3b), CONDITION (4) : QUI FINANCE LES GUICHETS ET LA RECONVERSION.

    L'auteur a choisi le découvert apuré (D75) : l'institution verse par émission
    au moment du besoin, et l'excédent du reflux apure le découvert dans le
    temps. Le reflux n'étant pas modélisé, la sortie n'en suppose aucun : elle en
    fait varier la taille, montre pourquoi le reflux seul manque au moment des
    chocs, et où aboutit ce que l'allocation émet.

    Elle reproduit la configuration AU MOMENT DE D75 (`OPTIONS_AVANT_D77`) :
    la conversion du reliquat, décidée ensuite, a sa propre section.
    """
    horizon = 40
    besoins = besoins_des_guichets(horizon, **OPTIONS_AVANT_D77)
    repere = besoin_moyen(besoins)
    print("")
    print("  (1) CE QUE LES GUICHETS VERSENT SANS REMBOURSEMENT — %d périodes," % horizon)
    print("      configuration de l'auteur au moment de D75, avant D77")
    print("  %-4s %12s %13s %8s %18s" % ("", "allocations", "reconversion", "total",
                                         "premier versement"))
    for sc in SCENARIOS:
        r = mesurer_apurement(sc, horizon, None, **OPTIONS_AVANT_D77)
        print("  %-4s %12.0f %13.0f %8.0f %18s" % (sc.cle, r["allocations"],
                                                 r["reconversion"], r["verse"],
                                                 "période %d" % r["premier"]))
    print("  REPÈRE DU REFLUX : besoin moyen par période, tous scénarios, %.2f —" % repere)
    print("  tiré des besoins eux-mêmes, et S2 en fait l'essentiel")
    print("")
    print("  (2) LE DÉCOUVERT APURÉ PAR LE REFLUX — CHOIX DE L'AUTEUR (D75)")
    print("      pic du découvert, puis périodes du premier versement au retour à")
    print("      zéro ; « reste » si le découvert n'est pas apuré dans l'horizon")
    print("  %-14s" % "reflux" + "".join("%15s" % sc.cle for sc in SCENARIOS))
    for k in MULTIPLES_REFLUX:
        cellules = []
        for sc in SCENARIOS:
            r = mesurer_apurement(sc, horizon, k * repere, **OPTIONS_AVANT_D77)
            if r["apure_en"] is None:
                cellules.append("reste %6.0f" % r["reste"])
            elif r["apure_en"] == 0:
                cellules.append("sans report")
            else:
                cellules.append("%4.0f en %2d" % (r["pic"], r["apure_en"]))
        print("  %-14s" % ("%.1f × %.1f" % (k, repere))
              + "".join("%15s" % x for x in cellules))
    print("")
    print("  (3) POURQUOI PAS LE REFLUX SEUL — calendrier sur la trajectoire financée")
    print("  %-4s %17s %20s %14s %22s" % ("", "manque au repère", "flux minimal, sans",
                                          "flux propre", "fonds à constituer"))
    print("  %-4s %17s %20s %14s %22s" % ("", "", "fonds préalable", "du scénario",
                                          "au flux propre"))
    for sc in SCENARIOS:
        c = calendrier_reflux_seul(besoins[sc.cle], repere)
        print("  %-4s %17.0f %20.1f %14.1f %22.0f"
              % (sc.cle, c["manque"], c["flux_minimal"], c["flux_propre"],
                 c["fonds_prealable"]))
    print("")
    print("  (4) OÙ ABOUTIT L'ÉMISSION — S2, avec et sans allocation, à %d et %d périodes"
          % (horizon, 2 * horizon))
    jeux = [(actif, h, mesurer_incidence_allocation(h, actif, **OPTIONS_AVANT_D77))
            for h in (horizon, 2 * horizon) for actif in (False, True)]
    print("      le pays pauvre")
    print("  %-26s %10s %12s %12s %8s %11s" % ("", "essentiel", "contraction",
                                               "exportations", "parité", "sous son"))
    print("  %-26s %10s %12s %12s %8s %11s" % ("", "servi", "", "", "", "plancher"))
    for actif, h, x in jeux:
        print("  %-26s %9.0f %% %12.0f %12.0f %8.2f %11d"
              % ("%s, %d" % ("facilité + allocation" if actif else "facilité seule", h),
                 x["essentiel"], x["contraction_pau"], x["exportations_pau"],
                 x["parite_pau"], x["plafond_pau"]))
    print("      l'exportateur des biens essentiels, et l'institution")
    print("  %-26s %10s %8s %13s %10s %12s" % ("", "solde EXC", "parité", "au-delà du",
                                               "recyclé", "solde de"))
    print("  %-26s %10s %8s %13s %10s %12s" % ("", "final", "EXC", "plafond, dès",
                                               "par EXC", "l'institution"))
    for actif, h, x in jeux:
        print("  %-26s %10.0f %8.3f %13s %10.0f %12.0f"
              % ("%s, %d" % ("facilité + allocation" if actif else "facilité seule", h),
                 x["solde_exc"], x["parite_exc"],
                 ("%d fois, %d" % (x["plafond_exc"], x["premier_plafond_exc"])
                  if x["plafond_exc"] else "jamais"),
                 x["recycle_exc"], x["institution"]))
    print("      CE QUE LA SORTIE MONTRE. Sur un choc passager, le découvert se")
    print("      résorbe, d'autant plus lentement que le reflux affecté est faible.")
    print("      Sur un choc STRUCTUREL, il ne se résorbe que si le reflux dépasse")
    print("      le flux du besoin lui-même : le reflux le financerait alors en")
    print("      permanence, ce qui est la voie de L1.C19 § 2 ; en deçà, c'est une")
    print("      ÉMISSION PERMANENTE, et elle se compte dans F1. Le reflux seul manque")
    print("      au moment des chocs : il y faudrait un flux plusieurs fois le besoin")
    print("      moyen, ou un fonds constitué d'avance.")
    print("      ET L'ÉMISSION NE DISPARAÎT PAS. L'allocation sert tout l'essentiel du")
    print("      pays pauvre et épargne sa monnaie, qui n'ajuste plus par le change ;")
    print("      ce qu'elle émet aboutit chez l'exportateur des biens essentiels. Sa")
    print("      réévaluation atteint la butée, le recyclage ne trouve d'abord aucun")
    print("      destinataire, et son solde dépasse le plafond sans limite visible :")
    print("      L'ÉMISSION PERMANENTE DEVIENT SON ACCUMULATION PERMANENTE. Sans")
    print("      allocation, c'est le pays pauvre qui passe sous son plancher.")
    print("      D77 Y RÉPOND : voir la section suivante.")
    print("      LE REGISTRE DU DÉCOUVERT N'EST PAS LE SOLDE DE L'INSTITUTION : dans les")
    print("      comptes, ce solde a toujours pour contrepartie les soldes positifs des")
    print("      pays. Apurer, c'est les réduire quelque part ; le modèle compte ce que")
    print("      le reflux aurait à retirer, il ne le retire pas.")
    print("      CE QU'ELLE NE MONTRE PAS : la taille du reflux — il n'est pas")
    print("      modélisé —, qui le paie, l'effet du démurrage maintenu (D76) sur le")
    print("      solde de l'excédentaire, l'inflation, ni aucun calibrage.")


def regle_sans_butee_creancier(solde, quota, periodes_hors_corridor, parite):
    """VARIANTE MESURÉE, NON RETENUE : la règle de l'auteur, dont la butée ne borne
    plus que la dévaluation des déficitaires."""
    if solde > 0:
        return parite * (1.0 - PAS_GLISSEMENT_AUTEUR)
    return regle_de_revision_auteur(solde, quota, periodes_hors_corridor, parite)


def s2_avec_substitution(part, depuis):
    """S2, dont la dépendance à l'importation essentielle baisse de `part` à partir
    de la période `depuis`. LA RÉUSSITE EST SUPPOSÉE, ET SON COÛT N'EST PAS COMPTÉ :
    ce scénario mesure ce qu'une procédure côté importateur (D79) aurait à obtenir,
    non ce qu'elle obtiendrait."""
    def choc(t, volumes, prix):
        volumes, prix = choc_energetique_durable(t, volumes, prix)
        if t >= depuis:
            volumes = dict(volumes)
            volumes[("EXC", "PAU")] = volumes[("EXC", "PAU")] * (1.0 - part)
        return volumes, prix
    return Scenario("S2-%d" % round(100 * part),
                    "S2, dépendance réduite de %d %% SUPPOSÉE" % round(100 * part),
                    choc, "supposition, non production")


def s2_puis_retournement(retour=45):
    """S2 jusqu'à la période `retour`, puis le prix redescend et l'exportateur se met
    à importer : sa position se retourne. C'est le seul jeu où un placement est
    restitué, et où l'on voit ce que la conversion a retiré à l'exportateur."""
    def choc(t, volumes, prix):
        if 3 <= t < retour:
            prix = dict(prix)
            prix[("EXC", "PAU")] = PRIX_BASE * 2.0
        elif t >= retour:
            volumes = dict(volumes)
            volumes[("DEF", "EXC")] = 300
            volumes[("PAU", "EXC")] = 80
        return volumes, prix
    return Scenario("S2R", "S2 puis retournement à la période %d" % retour, choc,
                    "la position de l'exportateur se retourne")


def mesurer_accumulation(scenario, horizon, **options):
    """Ce que deviennent l'exportateur, le déficitaire et l'institution sous un
    remède donné."""
    e, journal, anomalies = jouer_a_horizon(scenario, horizon, **options)

    def compte(code, pays=None):
        return len([a for a in anomalies if a.startswith(code)
                    and (pays is None or "de %s " % pays in a)])
    return {"solde_exc": e.solde["EXC"], "au_dela_exc": compte("[C6]", "EXC"),
            "depassements": compte("[C6]"), "negatives": compte("[C8]"),
            "institution": e.solde[INST], "converti": sum(e.reliquat_converti.values()),
            "place": sum(e.placement.values()),
            "restitue": sum(e.placement_restitue.values()),
            "dette_def": journal[-1]["dette"]["DEF"], "masse_exc": e.masse["EXC"],
            "masse_min_def": min(p["masse"]["DEF"] for p in journal),
            "allocations": sum(e.alloc.values()), "demurrage_exc": e.demurrage["EXC"],
            "recycle_exc": sum(p["recyclage"]["EXC"] for p in journal),
            "parite_exc": e.parite["EXC"], "parite_min": min(e.parite.values()),
            "converti_exc": e.reliquat_converti["EXC"], "place_exc": e.placement["EXC"],
            "restitue_exc": e.placement_restitue["EXC"],
            "solde_exc_min": min(p["solde"]["EXC"] for p in journal),
            "identite": compte("[C5]") + compte("[C1]")}


def comparer_accumulation_exportateur():
    """A43 (3b) : L'ACCUMULATION DE L'EXPORTATEUR SOUS CHOC STRUCTUREL.

    La condition (4) a montré que ce que l'allocation émet aboutit chez
    l'exportateur des biens essentiels, au-delà de son plafond et sans limite.
    L'auteur a choisi la conversion du reliquat (D77), écarté le démurrage sur les
    soldes de compensation (D78) et retenu dans son principe une procédure côté
    importateur (D79). La sortie publie les remèdes mesurés, puis le prix du choix.

    Elle reproduit la configuration AU MOMENT DE D77 (`OPTIONS_AVANT_D80`).
    """
    s2 = [x for x in SCENARIOS if x.cle == "S2"][0]
    s4 = [x for x in SCENARIOS if x.cle == "S4"][0]
    print("")
    print("  (1) LES REMÈDES MESURÉS — S2, configuration de l'auteur, seul le remède varie")
    remedes = (("aucun : accumulation acceptée", {"reliquat_plafond": None}),
               ("conversion — CHOIX DE L'AUTEUR (D77)", {}),
               ("placement forcé", {"reliquat_plafond": "placement"}),
               ("démurrage 4 % sur la compensation",
                {"reliquat_plafond": None, "demurrage_soldes": 0.04}),
               ("butée levée pour les créanciers",
                {"reliquat_plafond": None, "regle": regle_sans_butee_creancier}))
    mesures = [(libelle, h, mesurer_accumulation(s2, h, **dict(OPTIONS_AVANT_D80,
                                                               **extra)))
               for libelle, extra in remedes for h in (40, 80, 120)]
    print("      les soldes")
    print("  %-37s %4s %9s %11s %13s %7s %11s %11s"
          % ("remède", "hor.", "solde EXC", "au-delà EXC", "au-delà, tous", "inst.",
             "allocations", "parité min."))
    for libelle, h, r in mesures:
        print("  %-37s %4d %9.0f %11d %13d %7.0f %11.0f %11.3f"
              % (libelle if h == 40 else "", h, r["solde_exc"], r["au_dela_exc"],
                 r["depassements"], r["institution"], r["allocations"], r["parite_min"]))
    print("      ce que chaque remède coûte")
    print("  %-37s %4s %9s %7s %13s %9s %9s %12s"
          % ("remède", "hor.", "converti", "placé", "démurrage EXC", "masse EXC",
             "dette DEF", "recyclé EXC"))
    for libelle, h, r in mesures:
        print("  %-37s %4d %9.0f %7.0f %13.0f %9.0f %9.0f %12.0f"
              % (libelle if h == 40 else "", h, r["converti"], r["place"],
                 r["demurrage_exc"], r["masse_exc"], r["dette_def"], r["recycle_exc"]))
    print("")
    print("  (2) LE DÉMURRAGE SUR LES SOLDES DE COMPENSATION — S4, 40 périodes (D78)")
    print("  %-7s %13s %12s %14s %13s %17s"
          % ("taux", "payé par EXC", "recyclé EXC", "masse min DEF", "dépassements",
             "masses négatives"))
    for taux in (0.0, 0.005, 0.01, 0.02, 0.04):
        r = mesurer_accumulation(s4, 40, **dict(OPTIONS_AVANT_D80,
                                                 demurrage_soldes=taux))
        print("  %-7s %13.0f %12.0f %14.0f %13d %17d"
              % ("%.1f %%" % (100 * taux), r["demurrage_exc"], r["recycle_exc"],
                 r["masse_min_def"], r["depassements"], r["negatives"]))
    print("")
    print("  (3) CE QUE LA CONVERSION CHANGE AILLEURS — soldes différents, avec et sans")
    for h in (40, 80, 120):
        ecarts = []
        for sc in SCENARIOS:
            _, j0, a0 = jouer_a_horizon(sc, h, **OPTIONS_AVANT_D77)
            _, j1, a1 = jouer_a_horizon(sc, h, **OPTIONS_AVANT_D80)
            n = int(a0 != a1) + sum(abs(p0["solde"][c] - p1["solde"][c]) > 1e-9
                                    for p0, p1 in zip(j0, j1) for c in COMPTES)
            ecarts.append("%s %d" % (sc.cle, n))
        print("  horizon %3d : %s" % (h, ", ".join(ecarts)))
    print("")
    print("  (4) LA DÉPENDANCE DE L'IMPORTATEUR — S2, baisse SUPPOSÉE dès la période 11 (D79)")
    print("  %-10s %4s %12s %9s %16s %16s" % ("baisse", "hor.", "allocations", "converti",
                                              "solde EXC, sans", "au-delà, sans"))
    for part in (0.0, 0.25, 0.5):
        sc = s2 if part == 0.0 else s2_avec_substitution(part, 11)
        for h in (40, 80):
            r = mesurer_accumulation(sc, h, **OPTIONS_AVANT_D80)
            r0 = mesurer_accumulation(sc, h, **OPTIONS_AVANT_D77)
            print("  %-10s %4d %12.0f %9.0f %16.0f %16d"
                  % ("%d %%" % round(100 * part) if h == 40 else "", h, r["allocations"],
                     r["converti"], r0["solde_exc"], r0["au_dela_exc"]))
    print("      (« sans » : sans conversion, pour voir ce que la baisse obtient seule)")
    print("")
    print("  (5) SI LE CHOC SE RETOURNE — S2 jusqu'à la période 45, puis l'exportateur")
    print("      importe ; 90 périodes, montants de l'exportateur seul")
    print("  %-26s %9s %13s %9s %13s %15s"
          % ("remède", "converti", "encore placé", "restitué", "solde EXC min",
             "solde EXC final"))
    retournement = s2_puis_retournement(45)
    for libelle, extra in (("conversion (D77)", {}),
                           ("placement forcé", {"reliquat_plafond": "placement"})):
        r = mesurer_accumulation(retournement, 90, **dict(OPTIONS_AVANT_D80, **extra))
        print("  %-26s %9.0f %13.0f %9.0f %13.0f %15.0f"
              % (libelle, r["converti_exc"], r["place_exc"], r["restitue_exc"],
                 r["solde_exc_min"], r["solde_exc"]))
    print("      CE QUE LA SORTIE MONTRE. Sans remède, l'accumulation est sans limite, et")
    print("      le recyclage d'un excès accumulé déraille en gros prêts ponctuels que le")
    print("      déficitaire rembourse aussitôt. LA CONVERSION arrête l'exportateur au")
    print("      plafond et stabilise le solde de l'institution, sans toucher aucun autre")
    print("      scénario. SON PRIX : l'exportateur perd les créances annulées, sa masse")
    print("      reste plus basse, et SI SA POSITION SE RETOURNE, il n'a plus de réserve et")
    print("      passe en débit là où le placement l'aurait couvert ; et la dette de")
    print("      recyclage du déficitaire continue de croître à long terme.")
    print("      Le placement ne fait que changer l'accumulation de registre. Le démurrage")
    print("      sur la compensation retire à l'excédentaire ce que le recyclage aurait")
    print("      prêté : en S4, la masse du déficitaire devient négative dès 0,5 %. La")
    print("      butée levée finit par arrêter l'allocation, au prix d'une spirale de")
    print("      réévaluations où l'excédent passe d'un pays à l'autre, chacun au-delà de")
    print("      son plafond. HORS CETTE SPIRALE, SEULE UNE BAISSE DE LA DÉPENDANCE ARRÊTE")
    print("      L'ÉMISSION ELLE-MÊME — supposée ici, non produite.")
    print("      CE QU'ELLE NE MONTRE PAS : qu'un exportateur accepte d'avance l'annulation")
    print("      (F6), la réussite d'une reconversion, l'inflation, ni aucun calibrage.")


def s2_intensite(multiple):
    """S2, le prix de l'importation essentielle étant multiplié par `multiple` à
    partir de la période 3, et ne redescendant pas."""
    def choc(t, volumes, prix):
        if t >= 3:
            prix = dict(prix)
            prix[("EXC", "PAU")] = PRIX_BASE * multiple
        return volumes, prix
    return Scenario("S2x%s" % multiple, "S2, prix essentiel ×%s" % multiple, choc,
                    "intensité du choc structurel")


def procedure_importateur_type(declencheur=PERSISTANCE_STRUCTUREL, surcout_min=0.30,
                               delai=4, part=0.0, financement=1.0, revue="cloture",
                               duree=None, plafond_financement=None, progres_min=None,
                               plafond_factures=None):
    """Un jeu de paramètres de la procédure côté importateur, pour les mesures."""
    p = {"declencheur": declencheur, "surcout_min": surcout_min, "revue": revue,
         "reconversion": {"delai": delai, "part": part, "financement": financement}}
    if duree is not None:
        p["duree"] = duree
    if plafond_financement is not None:
        p["plafond_financement"] = plafond_financement
    if progres_min is not None:
        p["progres_min"] = progres_min
    if plafond_factures is not None:
        p["plafond_factures"] = plafond_factures
    return p


def mesurer_importateur(scenario, horizon, procedure_imp, **options):
    """Ce que la procédure côté importateur verse, ce qu'elle épargne et à qui."""
    e, journal, anomalies = jouer_a_horizon(
        scenario, horizon, **dict(options, procedure_importateur=procedure_imp))
    premiere = next((p["t"] for p in journal if sum(p["converti"].values()) > 1e-9), None)
    return {"ouverte": e.imp_ouverte["PAU"], "close": e.imp_close["PAU"],
            "verse": sum(e.imp_verse.values()), "allocations": sum(e.alloc.values()),
            "emis": sum(e.imp_verse.values()) + sum(e.alloc.values()),
            "converti": sum(e.reliquat_converti.values()), "premiere_conversion": premiere,
            "institution": e.solde[INST], "contraction_pau": e.contraction["PAU"],
            "exportations_exc": e.production["EXC"], "surcout": e.surcout["PAU"],
            "ouvertures": dict((c, v) for c, v in e.imp_ouverte.items() if v is not None),
            "anomalies": len([a for a in anomalies if a[:4] in ("[C1]", "[C3]", "[C5]", "[C8]")])}


def croissance_allocations(multiple, part, **options):
    """Ce que les allocations croissent encore entre 40 et 80 périodes quand la
    dépendance baisse de `part`, pour un prix essentiel ×`multiple`."""
    sc = s2_intensite(multiple)
    proc = procedure_importateur_type(part=part)
    return (mesurer_importateur(sc, 80, proc, **options)["allocations"]
            - mesurer_importateur(sc, 40, proc, **options)["allocations"])


def comparer_procedure_importateur():
    """D79 : LA DÉPENDANCE DURABLE À UNE IMPORTATION ESSENTIELLE.

    La procédure est retenue dans son principe, sa réussite n'est pas supposée.
    La sortie instruit ses quatre termes — ouverture, seuils, financement,
    revue — et dit ce qu'une reconversion devrait obtenir pour arrêter
    l'émission, sans jamais produire cette réussite.
    """
    s = dict((x.cle, x) for x in SCENARIOS)
    base = OPTIONS_AVANT_D80
    print("")
    print("  (1) OÙ LA PROCÉDURE S'OUVRE — période d'ouverture pour le pays pauvre, 80 périodes")
    print("  %-38s" % "critère" + "".join("%7s" % k for k in ("S0", "S1", "S2", "S3", "S4")))
    for libelle, proc in (("persistance seule", procedure_importateur_type(surcout_min=0.0)),
                          ("surcoût de 30 % seul", procedure_importateur_type(declencheur=0)),
                          ("persistance + surcoût 30 % — AUTEUR (D80)",
                           procedure_importateur_type()),
                          ("persistance + surcoût 50 %", procedure_importateur_type(surcout_min=0.5))):
        cellules = []
        for k in ("S0", "S1", "S2", "S3", "S4"):
            o = mesurer_importateur(s[k], 80, proc, **base)["ouvertures"]
            cellules.append("%d" % o["PAU"] if "PAU" in o else "—")
        print("  %-38s" % libelle + "".join("%7s" % x for x in cellules))
    print("")
    print("  (2) L'INTENSITÉ DU CHOC — S2 à prix essentiel ×m, 80 périodes, sans procédure")
    print("  %-6s %12s %9s %20s %12s %12s"
          % ("×m", "allocations", "converti", "première conversion", "ouverte 30 %",
             "ouverte 50 %"))
    for m in (1.2, 1.3, 1.5, 2.0, 3.0):
        sans = mesurer_importateur(s2_intensite(m), 80, None, **base)
        o30 = mesurer_importateur(s2_intensite(m), 80, procedure_importateur_type(), **base)
        o50 = mesurer_importateur(s2_intensite(m), 80,
                                  procedure_importateur_type(surcout_min=0.5), **base)
        print("  %-6s %12.0f %9.0f %20s %12s %12s"
              % ("×%s" % m, sans["allocations"], sans["converti"],
                 sans["premiere_conversion"] or "jamais",
                 "période %d" % o30["ouverte"] if o30["ouverte"] else "non",
                 "période %d" % o50["ouverte"] if o50["ouverte"] else "non"))
    print("")
    print("  (3) LE FINANCEMENT ET LA RÉUSSITE — S2, 80 périodes, ouverture persistance + 30 %")
    print("      financement : émission non remboursable de la facture de base — AUTEUR (D81) ;")
    print("      pris sur les créances converties, il n'arriverait qu'à la « première")
    print("      conversion » du tableau (2)")
    print("  %-14s %6s %7s %12s %7s %9s %7s %12s %13s"
          % ("réussite", "délai", "versé", "allocations", "émis", "converti", "inst.",
             "contr. PAU", "export. EXC"))
    sans = mesurer_importateur(s["S2"], 80, None, **base)
    print("  %-14s %6s %7.0f %12.0f %7.0f %9.0f %7.0f %12.0f %13.0f"
          % ("sans procédure", "—", 0, sans["allocations"], sans["emis"], sans["converti"],
             sans["institution"], sans["contraction_pau"], sans["exportations_exc"]))
    for part in (0.0, 0.25, 0.5):
        for delai in (4, 8):
            r = mesurer_importateur(s["S2"], 80,
                                    procedure_importateur_type(delai=delai, part=part), **base)
            print("  %-14s %6d %7.0f %12.0f %7.0f %9.0f %7.0f %12.0f %13.0f"
                  % ("%d %% supposée" % round(100 * part) if part else "non supposée",
                     delai, r["verse"], r["allocations"], r["emis"], r["converti"],
                     r["institution"], r["contraction_pau"], r["exportations_exc"]))
    print("")
    print("  (4) LA REVUE — S2, délai 4, 80 périodes")
    print("  %-14s %-42s %7s %7s %9s" % ("réussite", "revue", "versé", "émis", "converti"))
    for part in (0.0, 0.25, 0.5):
        for libelle, proc in (("clôture à l'échéance", procedure_importateur_type(part=part)),
                              ("jalons : 25 % de baisse, 8 factures (D82)",
                               procedure_importateur_type(part=part, revue="jalons",
                                                          progres_min=0.25,
                                                          plafond_factures=8)),
                              ("prolongation plafonnée à 8 factures",
                               procedure_importateur_type(part=part, revue="prolongation",
                                                          plafond_factures=8)),
                              ("prolongation sans plafond",
                               procedure_importateur_type(part=part, revue="prolongation"))):
            r = mesurer_importateur(s["S2"], 80, proc, **base)
            print("  %-14s %-42s %7.0f %7.0f %9.0f"
                  % ("%d %% supposée" % round(100 * part) if part else "non supposée",
                     libelle, r["verse"], r["emis"], r["converti"]))
    print("")
    print("  (5) LA BAISSE NÉCESSAIRE — croissance des allocations entre 40 et 80 périodes,")
    print("      selon la baisse de dépendance, autour de la part du surcoût dans la facture")
    print("  %-6s %16s %18s %16s %18s" % ("×m", "part du surcoût", "10 points de moins",
                                         "à la part", "10 points de plus"))
    for m in (1.5, 2.0, 3.0):
        part = 1.0 - 1.0 / m
        print("  %-6s %16s %18.0f %16.0f %18.0f"
              % ("×%s" % m, "%d %%" % round(100 * part),
                 croissance_allocations(m, part - 0.1, **base),
                 croissance_allocations(m, part, **base),
                 croissance_allocations(m, part + 0.1, **base)))
    print("")
    print("  (6) LA CONFIGURATION DE L'AUTEUR (D80 à D82) — S2, sa réussite étant jouée")
    print("  %-14s %4s %8s %7s %7s %7s %9s %7s" % ("réussite", "hor.", "ouverte", "close",
                                                "versé", "émis", "converti", "inst."))
    for part in (0.0, 0.25, 0.5):
        proc = dict(PROCEDURE_IMPORTATEUR_AUTEUR,
                    reconversion=dict(PROCEDURE_IMPORTATEUR_AUTEUR["reconversion"], part=part))
        for h in (40, 80):
            r = mesurer_importateur(s["S2"], h, proc, **OPTIONS_AVANT_D83)
            print("  %-14s %4d %8s %7s %7.0f %7.0f %9.0f %7.0f"
                  % (("%d %% supposée" % round(100 * part) if part else "non supposée")
                     if h == 40 else "", h, r["ouverte"], r["close"] or "—", r["verse"],
                     r["emis"], r["converti"], r["institution"]))
    ailleurs = []
    for k in ("S0", "S1", "S3", "S4"):
        n = 0
        for h in (40, 80):
            _, j0, a0 = jouer_a_horizon(s[k], h, **OPTIONS_AVANT_D80)
            _, j1, a1 = jouer_a_horizon(s[k], h, **OPTIONS_AVANT_D83)
            n += int(a0 != a1) + sum(abs(p0["solde"][c] - p1["solde"][c]) > 1e-9
                                     for p0, p1 in zip(j0, j1) for c in COMPTES)
        ailleurs.append("%s %d" % (k, n))
    print("  soldes différents ailleurs, à 40 et 80 périodes : %s" % ", ".join(ailleurs))
    print("      CE QUE LA SORTIE MONTRE. La procédure ne s'ouvre sur les seuls chocs")
    print("      durables qu'en combinant la persistance et le surcoût. Tant que la")
    print("      reconversion échoue, son financement REMPLACE l'allocation : l'émission")
    print("      totale ne change pas ; seule la réussite la réduit, et avec elle ce que")
    print("      l'exportateur perd par conversion. Prolonger sans plafond un financement")
    print("      qui échoue ajoute de l'émission, qui finit chez l'exportateur. Et les")
    print("      allocations ne cessent de croître qu'autour d'une baisse de dépendance égale")
    print("      à la part du surcoût dans la facture — ni en deçà, ni toujours au-delà ;")
    print("      ce que la réussite retire aux importations, elle le retire aux exportations")
    print("      de l'exportateur. SOUS LES CHOIX DE L'AUTEUR, une reconversion qui échoue")
    print("      coûte quatre factures de base, prises sur l'allocation, puis se clôt ; une")
    print("      reconversion qui avance est financée jusqu'à huit ; et aucun autre scénario")
    print("      ne change.")
    print("      CE QU'ELLE NE MONTRE PAS : qu'une reconversion réussisse, en combien de")
    print("      temps, à quel coût réel — la production qui remplace les importations")
    print("      n'est pas représentée —, l'inflation, ni aucun calibrage.")


def mesurer_seuils(horizon, corridor=None, plafond=None, plafond_creancier_=None,
                   quotas=None, **options):
    """Les cinq scénarios sous des seuils donnés : anomalies, révisions de parité,
    contraction du déficitaire, masse minimale du déficitaire en S4, conversions
    en S2, dette de recyclage du déficitaire en S4, ouverture de sa procédure."""
    r = {"C1": 0, "C3": 0, "C5": 0, "C6": 0, "C8": 0, "revisions": 0, "contraction": 0.0}
    for sc in SCENARIOS:
        e, journal, anomalies = jouer_avec_seuils(
            sc, horizon, corridor=corridor, plafond=plafond,
            plafond_creancier_=plafond_creancier_, quotas=quotas, **options)
        for code in ("C1", "C3", "C5", "C6", "C8"):
            r[code] += len([a for a in anomalies if a.startswith("[%s]" % code)])
        precedente = dict((c, 1.0) for c in CODES)
        for p in journal:
            r["revisions"] += sum(1 for c in CODES if abs(p["parite"][c] - precedente[c]) > 1e-12)
            precedente = p["parite"]
        if sc.cle in ("S0", "S1", "S2", "S3"):
            r["contraction"] += e.contraction["DEF"]
        if sc.cle == "S2":
            r["converti"] = sum(e.reliquat_converti.values())
        if sc.cle == "S4":
            r["masse_min_def"] = min(p["masse"]["DEF"] for p in journal)
            r["dette_def"] = journal[-1]["dette"]["DEF"]
            r["ouverture"] = e.procedure_ouverte["DEF"]
    return r


def comparer_seuils_du_plafond():
    """A43 (3b), CONDITION (3) : UN PLAFOND DUR ASSORTI D'UNE PROCÉDURE — SES SEUILS.

    La procédure est arrêtée (recyclage en prêt, puis conversion du reliquat). La
    sortie instruit ses seuils — la base des quotas, le niveau du plafond, la
    largeur du corridor — et publie la configuration de l'auteur (D83 à D85).
    """
    base = OPTIONS_AVANT_D83
    qi = quotas_proportionnels("importations")

    def q(quotas):
        return "/".join("%d" % round(quotas[c]) for c in CODES)
    print("")
    print("  (1) LA BASE DES QUOTAS — même total ; plafond 100 %, corridor 25 %")
    print("  %-38s %14s %4s %4s %4s %14s %11s"
          % ("base", "EXC/DEF/PAU", "hor.", "C6", "C8", "masse min DEF", "converti S2"))
    for libelle, quotas, pc in (("déclarés", dict(QUOTA), None),
                                ("importations — AUTEUR (D83)", qi, None),
                                ("commerce, créanciers à 85 %", quotas_proportionnels("commerce"), 0.85),
                                ("commerce", quotas_proportionnels("commerce"), None),
                                ("exportations", quotas_proportionnels("exportations"), None)):
        for h in (40, 80):
            r = mesurer_seuils(h, quotas=quotas, plafond_creancier_=pc, **base)
            print("  %-38s %14s %4d %4d %4d %14.0f %11.0f"
                  % (libelle if h == 40 else "", q(quotas) if h == 40 else "", h, r["C6"],
                     r["C8"], r["masse_min_def"], r["converti"]))
    print("")
    print("  (2) LE NIVEAU DU PLAFOND — quotas aux importations, corridor 25 %")
    print("  %-38s %4s %4s %4s %14s %11s %10s"
          % ("plafond", "hor.", "C6", "C8", "masse min DEF", "converti S2", "dette DEF"))
    for libelle, pl, pc in (("100 %, symétrique — AUTEUR (D84)", None, None),
                            ("créanciers à 75 %", None, 0.75),
                            ("créanciers à 50 %", None, 0.50),
                            ("50 %, symétrique", 0.50, None),
                            ("créanciers à 150 %", None, 1.50),
                            ("150 %, symétrique", 1.50, None)):
        for h in (40, 80):
            r = mesurer_seuils(h, plafond=pl, plafond_creancier_=pc, quotas=qi, **base)
            print("  %-38s %4d %4d %4d %14.0f %11.0f %10.0f"
                  % (libelle if h == 40 else "", h, r["C6"], r["C8"], r["masse_min_def"],
                     r["converti"], r["dette_def"]))
    print("")
    print("  (3) LE CORRIDOR — quotas aux importations, plafond 100 %")
    print("  %-38s %4s %10s %20s %14s %10s"
          % ("corridor", "hor.", "révisions", "contraction DEF S0-S3", "masse min DEF",
             "ouverture"))
    for libelle, cor in (("10 %", 0.10), ("25 % — AUTEUR (D85)", None), ("50 %", 0.50)):
        for h in (40, 80, 120):
            r = mesurer_seuils(h, corridor=cor, quotas=qi, **base)
            print("  %-38s %4d %10d %20.0f %14.0f %10s"
                  % (libelle if h == 40 else "", h, r["revisions"], r["contraction"],
                     r["masse_min_def"], r["ouverture"]))
    print("")
    print("  (4) LA CONFIGURATION DE L'AUTEUR — avant et après D83 à D85")
    print("  %-26s %4s %10s %14s %11s %10s %20s"
          % ("configuration", "hor.", "anomalies", "masse min DEF", "converti S2", "dette DEF",
             "contraction DEF S0-S3"))
    for libelle, options in (("avant D83", OPTIONS_AVANT_D83),
                             ("complète (D83 à D85)", OPTIONS_AVANT_D88)):
        for h in (40, 80, 120):
            r = mesurer_seuils(h, **options)
            print("  %-26s %4d %10d %14.0f %11.0f %10.0f %20.0f"
                  % (libelle if h == 40 else "", h,
                     r["C1"] + r["C3"] + r["C5"] + r["C6"] + r["C8"], r["masse_min_def"],
                     r["converti"], r["dette_def"], r["contraction"]))
    print("      CE QUE LA SORTIE MONTRE. C'est le plafond des CRÉANCIERS qui mord : celui")
    print("      des débiteurs ne change aucune trajectoire tant que le premier ne dépasse")
    print("      pas le second (« créanciers à 50 % » et « 50 %, symétrique » donnent les")
    print("      mêmes chiffres), et il n'est franchi que si les créanciers ont plus de")
    print("      marge que les débiteurs. Plus un quota repose")
    print("      sur les exportations, plus l'excédentaire a de marge et plus le déficitaire")
    print("      s'enfonce en S4 ; aux importations, aucune anomalie, et une meilleure")
    print("      protection du déficitaire, contre un peu plus de conversions. Un plafond")
    print("      plus haut pour les créanciers, ou à 150 %, rend sa masse négative ; plus bas,")
    print("      il le protège davantage et coûte à l'exportateur. LE CORRIDOR N'A PAS")
    print("      D'OPTIMUM ROBUSTE : la contraction du déficitaire change d'ordre selon")
    print("      l'horizon ; plus large, il réduit les révisions mais retarde la procédure")
    print("      structurelle et affaiblit la protection en S4.")
    print("      CE QU'ELLE NE MONTRE PAS : un modèle à trois pays ne dit pas ce que donnent")
    print("      des quotas aux importations quand le plus gros importateur est riche ; ni")
    print("      l'inflation, ni aucun calibrage.")


def chocs_combines(*chocs):
    """Plusieurs chocs appliqués à la suite, période par période."""
    def choc(t, volumes, prix):
        for f in chocs:
            volumes, prix = f(t, volumes, prix)
        return volumes, prix
    return choc


def chocs_energetiques_repetes(periode=12, duree=3):
    """Le choc énergétique passager de S1, répété toutes les `periode` périodes."""
    def choc(t, volumes, prix):
        if t >= 3 and (t - 3) % periode < duree:
            prix = dict(prix)
            prix[("EXC", "PAU")] = PRIX_BASE * 2.0
            prix[("EXC", "DEF")] = PRIX_BASE * 1.5
        return volumes, prix
    return choc


def recoltes_repetees(periode=10):
    """La mauvaise récolte de S3, répétée toutes les `periode` périodes."""
    def choc(t, volumes, prix):
        if t >= 3 and (t - 3) % periode < 3:
            volumes = dict(volumes)
            volumes[("PAU", "EXC")] = 5
            volumes[("PAU", "DEF")] = 2
            volumes[("EXC", "PAU")] = 60
        return volumes, prix
    return choc


def scenarios_de_stress():
    """Ce que les cinq scénarios ne jouent pas : des chocs combinés, répétés, plus
    intenses. Ils servent à chercher ce qui démentirait un verdict favorable."""
    return [
        Scenario("S2+S4", "choc structurel et perte d'un débouché ensemble",
                 chocs_combines(choc_energetique_durable, rupture_commerciale), "stress"),
        Scenario("S1r", "choc énergétique passager toutes les 12 périodes",
                 chocs_energetiques_repetes(12, 3), "stress"),
        Scenario("S3r", "mauvaise récolte toutes les 10 périodes", recoltes_repetees(10), "stress"),
        Scenario("S2x3", "choc structurel à prix triplé", s2_intensite(3.0).choc, "stress"),
        Scenario("S1+S3", "choc énergétique et mauvaise récolte ensemble",
                 chocs_combines(choc_energetique, mauvaise_recolte), "stress"),
    ]


def mesurer_applicabilite(scenario, horizon, **options):
    """Anomalies, dettes de recyclage en quotas, conversions et allocations d'un jeu."""
    quotas = options.get("quotas") or QUOTA
    e, journal, anomalies = jouer_a_horizon(scenario, horizon, **options)
    codes = dict((k, len([a for a in anomalies if a.startswith("[%s]" % k)]))
                 for k in ("C1", "C2", "C3", "C5", "C6", "C7", "C8"))
    return {"codes": codes, "graves": codes["C1"] + codes["C3"] + codes["C5"] + codes["C6"] + codes["C8"],
            "dette_def": journal[-1]["dette"]["DEF"], "dette_pau": journal[-1]["dette"]["PAU"],
            "dette_def_quotas": journal[-1]["dette"]["DEF"] / quotas["DEF"],
            "dette_pau_quotas": journal[-1]["dette"]["PAU"] / quotas["PAU"],
            "rembourse_def": e.rembourse_pret["DEF"], "converti": sum(e.reliquat_converti.values()),
            "allocations": sum(e.alloc.values()),
            "masse_min": dict((c, min(p["masse"][c] for p in journal)) for c in CODES)}


def comparer_applicabilite():
    """A43 (3b) : LE JUGEMENT D'APPLICABILITÉ, LES CINQ CONDITIONS ÉTANT INSTRUITES.

    La sortie cherche ce qui démentirait un verdict favorable — horizon long, chocs
    combinés et répétés, créancier qui n'adopte pas ses obligations — et publie le
    verdict de l'auteur (D86) avec la condition qu'il ajoute (D87). Elle reproduit
    la configuration AU MOMENT DE D86 (`OPTIONS_AVANT_D88`).
    """
    O = OPTIONS_AVANT_D88
    print("")
    print("  (1) LA CONFIGURATION DE L'AUTEUR — les cinq scénarios, à 40 et 200 périodes")
    print("  %-8s %4s %8s %4s %16s %16s %9s %12s"
          % ("scénario", "hor.", "anomalies", "C7", "dette DEF (quotas)", "dette PAU (quotas)",
             "converti", "allocations"))
    for sc in SCENARIOS:
        for h in (40, 200):
            r = mesurer_applicabilite(sc, h, **O)
            print("  %-8s %4d %8d %4d %11.0f (%4.1f) %11.0f (%4.1f) %9.0f %12.0f"
                  % (sc.cle if h == 40 else "", h, r["graves"], r["codes"]["C7"], r["dette_def"],
                     r["dette_def_quotas"], r["dette_pau"], r["dette_pau_quotas"], r["converti"],
                     r["allocations"]))
    print("      (anomalies : dépassements, masses négatives, essentiel bloqué, identités ;")
    print("      C7 : tirages de facilité non échus à l'horizon, compté à part)")
    print("")
    print("  (2) CHOCS COMBINÉS ET RÉPÉTÉS — configuration de l'auteur, 80 et 160 périodes")
    print("  %-8s %-46s %4s %8s %4s %16s %16s"
          % ("jeu", "choc", "hor.", "anomalies", "C7", "dette DEF (quotas)", "dette PAU (quotas)"))
    for sc in scenarios_de_stress():
        for h in (80, 160):
            r = mesurer_applicabilite(sc, h, **O)
            print("  %-8s %-46s %4d %8d %4d %11.0f (%4.1f) %11.0f (%4.1f)"
                  % (sc.cle if h == 80 else "", sc.titre if h == 80 else "", h, r["graves"],
                     r["codes"]["C7"], r["dette_def"], r["dette_def_quotas"], r["dette_pau"],
                     r["dette_pau_quotas"]))
    print("")
    print("  (3) SI LE CRÉANCIER N'ADOPTE PAS SES OBLIGATIONS — cinq scénarios, 80 périodes")
    print("  %-40s %12s %17s" % ("créancier", "dépassements", "masses négatives"))
    for libelle, extra in (("tenu par les règles de l'auteur", {}),
                           ("délibère, comme dans l'histoire", {"symetrie_contraignante": False}),
                           ("refuse la réévaluation", {"obligations_creancier": ("plafond",)}),
                           ("refuse la conversion du reliquat", {"reliquat_plafond": None}),
                           ("refuse recyclage et conversion",
                            {"obligations_creancier": ("parite",), "reliquat_plafond": None})):
        depass = negatives = 0
        for sc in SCENARIOS:
            r = mesurer_applicabilite(sc, 80, **dict(O, **extra))
            depass += r["codes"]["C6"]
            negatives += r["codes"]["C8"]
        print("  %-40s %12d %17d" % (libelle, depass, negatives))
    print("")
    print("  (4) LA DETTE DURABLE — S4, perte d'un débouché, reconversion ratée")
    print("  %-8s %12s %8s %12s" % ("horizon", "dette DEF", "quotas", "remboursée"))
    s4 = [x for x in SCENARIOS if x.cle == "S4"][0]
    for h in (40, 80, 120, 160, 200):
        r = mesurer_applicabilite(s4, h, **O)
        print("  %-8d %12.0f %8.1f %12.0f" % (h, r["dette_def"], r["dette_def_quotas"],
                                             r["rembourse_def"]))
    print("      VERDICT DE L'AUTEUR (D86) : EXPÉRIMENTABLE EN COALITION POUR DES CHOCS")
    print("      PASSAGERS ; NON APPLICABLE EN L'ÉTAT AUX DÉSÉQUILIBRES DURABLES. Condition")
    print("      ajoutée (D87) : une règle de sortie des dettes durables, à instruire.")
    print("      CE QUE LA SORTIE MONTRE. Sous les règles de l'auteur, aucune anomalie, même")
    print("      à 200 périodes et sous chocs combinés ou répétés ; les chocs passagers")
    print("      ISOLÉS ne laissent aucune dette. Mais un déséquilibre durable non résorbé")
    print("      devient une dette de recyclage qui croît sans fin et n'est jamais")
    print("      remboursée ; des chocs passagers répétés laissent aussi des dettes, et des")
    print("      mauvaises récoltes répétées, trop brèves pour déclencher l'allocation,")
    print("      endettent le pays pauvre. Enfin tout repose sur l'automaticité des")
    print("      obligations du créancier : s'il délibère, ou s'il refuse recyclage et")
    print("      conversion, les dépassements et les masses négatives reviennent.")
    print("      CE QU'ELLE NE MONTRE PAS : que des créanciers adoptent ces obligations (F6),")
    print("      la conception du contrôle des capitaux, l'inflation, le calibrage (F1),")
    print("      l'avantage sur les instruments existants (F10), ni ce que donnerait un")
    print("      monde de plus de trois pays.")


# LES RÈGLES DE SORTIE DES DETTES DURABLES MESURÉES POUR D87, du seuil d'un quota de
# dette de recyclage par défaut. Aucune n'est retenue : c'est à l'auteur de trancher.
REGLES_DE_SORTIE = (
    ("aucune", None),
    ("annulation au-delà du seuil", {"modes": ("annulation",)}),
    ("plafond du prêt au seuil", {"modes": ("plafond",)}),
    ("restriction de 30 %", {"modes": ("restriction",), "restriction": 0.30}),
    ("dévaluation, butée levée", {"modes": ("devaluation",)}),
    ("dévaluation jusqu'à l'équilibre", {"modes": ("devaluation_flux",)}),
    ("annulation + dévaluation à l'équilibre", {"modes": ("annulation", "devaluation_flux")}),
)


def mesurer_sortie(scenario, horizon, **options):
    """Dettes et annulations en quotas, parités, soldes, échanges en volume des dix
    dernières périodes et anomalies graves d'un jeu : la sortie des dettes durables."""
    quotas = options.get("quotas") or QUOTA
    e, journal, anomalies = jouer_a_horizon(scenario, horizon, **options)
    avant = jouer_a_horizon(scenario, horizon - 10, **options)[0]
    codes = dict((k, len([a for a in anomalies if a.startswith("[%s]" % k)]))
                 for k in ("C1", "C3", "C5", "C6", "C8"))

    def importations(etat, c):
        return etat.production[c] + etat.transfert_reel[c]
    r = {"codes": codes, "graves": sum(codes.values()), "journal": journal,
         "parite_exc": e.parite["EXC"]}
    for c in ("DEF", "PAU"):
        r[c] = {"dette": journal[-1]["dette"][c] / quotas[c],
                "annulee": e.annule_sortie[c] / quotas[c],
                "parite": e.parite[c], "solde": e.solde[c] / quotas[c],
                "importe": (importations(e, c) - importations(avant, c)) / 10.0,
                "exporte": (e.production[c] - avant.production[c]) / 10.0}
    return r


def trajectoire_changee(scenario, horizon, sortie, **options):
    """Une règle de sortie change-t-elle les parités ou les soldes d'un jeu ?"""
    sans = jouer_a_horizon(scenario, horizon, **options)[1]
    avec = jouer_a_horizon(scenario, horizon, **dict(options, sortie_dettes=sortie))[1]
    return any(abs(p["parite"][c] - q["parite"][c]) > 1e-9
               or abs(p["solde"][c] - q["solde"][c]) > 1e-9
               for p, q in zip(sans, avec) for c in CODES)


def comparer_sortie_dettes():
    """D87 : LA SORTIE DES DETTES DURABLES, INSTRUITE LE 2026-09-17.

    Deux questions, dans cet ordre : la révision des parités voit-elle la dette de
    recyclage ? Et la perte qu'aucune parité bornée ne compense, quelle règle la
    fait sortir, au détriment de qui ? La sortie mesure ; l'auteur a tranché le même
    jour (D88 à D90). Elle part de la configuration AU MOMENT DE D87 (`OPTIONS_AVANT_D88`).
    """
    O = OPTIONS_AVANT_D88
    ON = dict(O, corridor_position_nette=True)
    jeux = SCENARIOS + scenarios_de_stress()
    s4 = [x for x in SCENARIOS if x.cle == "S4"][0]
    print("")
    print("  (1) LE SIGNAL MASQUÉ — dix jeux, 200 périodes, sans règle de sortie")
    print("  %-7s %-26s %-26s" % ("", "la révision lit le solde", "lit la position nette"))
    print("  %-7s %8s %8s %8s %8s %8s %8s"
          % ("jeu", "dette D", "dette P", "parité D", "dette D", "dette P", "parité D"))
    for sc in jeux:
        a = mesurer_sortie(sc, 200, **O)
        b = mesurer_sortie(sc, 200, **ON)
        print("  %-7s %8.2f %8.2f %8.3f %8.2f %8.2f %8.3f"
              % (sc.cle, a["DEF"]["dette"], a["PAU"]["dette"], a["DEF"]["parite"],
                 b["DEF"]["dette"], b["PAU"]["dette"], b["DEF"]["parite"]))
    long_ = mesurer_sortie(s4, 400, **ON)
    s2 = [x for x in SCENARIOS if x.cle == "S2"][0]
    e_s2 = jouer_a_horizon(s2, 200, **O)[0]
    e_s2b, j_s2b, _ = jouer_a_horizon(s2, 200, **dict(O, recyclage_au_besoin=True))
    print("      (dettes de recyclage du déficitaire D et du pays pauvre P, en quotas.")
    print("      Position nette : solde, moins les dettes de recyclage, plus les créances.")
    print("      S4 sur la position nette, à 400 périodes : dette D %.2f quotas.)"
          % long_["DEF"]["dette"])
    print("      Ce n'est pas l'excès de prêt : en S2, un prêt borné au besoin du débiteur")
    print("      divise la dette créée (%.0f au lieu de %.0f) et change à peine la dette restante"
          % (e_s2b.dette_creee["DEF"], e_s2.dette_creee["DEF"]))
    print("      (%.2f quotas au lieu de %.2f)."
          % (j_s2b[-1]["dette"]["DEF"] / QUOTAS_AUTEUR["DEF"],
             sum(v for (d, k), v in e_s2.dette.items() if d == "DEF") / QUOTAS_AUTEUR["DEF"]))
    print("")
    print("  (2) LES RÈGLES DE SORTIE — position nette lue, seuil d'un quota, 200 périodes")
    print("  %-40s %6s %8s %7s %8s %8s %6s"
          % ("règle", "dette", "annulée", "parité", "importe", "exporte", "anom."))
    for sc in [x for x in jeux if x.cle in ("S4", "S2+S4")]:
        print("  %s — %s" % (sc.cle, sc.titre))
        for libelle, sortie in REGLES_DE_SORTIE:
            r = mesurer_sortie(sc, 200, **dict(ON, sortie_dettes=sortie))
            d = r["DEF"]
            print("  %-40s %6.2f %8.2f %7.3f %8.1f %8.1f %6d"
                  % (libelle, d["dette"], d["annulee"], d["parite"], d["importe"],
                     d["exporte"], r["graves"]))
    print("      (déficitaire : dette et annulation cumulée en quotas, parité, importations")
    print("      et exportations en volume par période, sur les dix dernières ; anomalies")
    print("      graves : dépassements, masses négatives, essentiel bloqué, identités)")
    combinee = dict(ON, sortie_dettes=REGLES_DE_SORTIE[-1][1])
    sans_butee = dict(ON, sortie_dettes=REGLES_DE_SORTIE[4][1])
    print("      À plus long terme, S4 — annulation + dévaluation à l'équilibre : annulée")
    print("      %.2f quota à 300 périodes, %.2f à 600 ; dévaluation, butée levée : parité"
          % (mesurer_sortie(s4, 300, **combinee)["DEF"]["annulee"],
             mesurer_sortie(s4, 600, **combinee)["DEF"]["annulee"]))
    loin = mesurer_sortie(s4, 600, **sans_butee)
    print("      du déficitaire %.2f et de l'excédentaire %.3f à 600 périodes."
          % (loin["DEF"]["parite"], loin["parite_exc"]))
    print("")
    print("  (3) LE SEUIL — annulation + dévaluation à l'équilibre, position nette lue")
    print("  %-6s %-32s %10s %10s"
          % ("seuil", "jeux dont la trajectoire change", "S4 : dette", "annulée"))
    for seuil in (0.5, 1.0, 2.0):
        sortie = {"modes": ("annulation", "devaluation_flux"), "seuil": seuil}
        touches = [sc.cle for sc in jeux if trajectoire_changee(sc, 200, sortie, **ON)]
        r = mesurer_sortie(s4, 200, **dict(ON, sortie_dettes=sortie))
        print("  %-6.1f %-32s %10.2f %10.2f"
              % (seuil, ", ".join(touches), r["DEF"]["dette"], r["DEF"]["annulee"]))
    print("      CE QUE LA SORTIE MONTRE. (1) Le recyclage en prêt ramène le solde du")
    print("      débiteur vers le corridor sans rien changer à sa position : la révision,")
    print("      qui lit le solde, s'arrête, et le déficit devient une dette qui croît —")
    print("      même en S2, où la parité du déficitaire reste réévaluée. Lue sur la")
    print("      position nette, la révision ramène sous un quota, sans règle de sortie,")
    print("      les dettes de tous les jeux sauf deux : la perte d'un débouché, que la")
    print("      butée ne laisse pas compenser. (2) Aucune règle ne fait disparaître cette")
    print("      perte ; chacune désigne qui la porte. L'annulation seule fait du créancier")
    print("      le payeur sans fin d'un transfert réel. Le plafond seul comprime le")
    print("      débiteur jusqu'à ses recettes et rompt le plafond dur et les masses. La")
    print("      restriction ralentit la dette sans l'arrêter. La dévaluation sans butée")
    print("      dépasse de loin l'équilibre, fait du débiteur un excédentaire au plafond")
    print("      et entraîne le créancier dans la dévaluation. La dévaluation arrêtée à")
    print("      l'équilibre des échanges contient la dette sans anomalie — elle culmine,")
    print("      puis se rembourse lentement —, au prix d'importations fortement réduites")
    print("      et d'exportations accrues ; jointe à l'annulation au-delà du seuil, elle")
    print("      borne aussi la perte du créancier.")
    print("      (3) Au seuil d'un quota, cette combinaison ne touche que la perte d'un")
    print("      débouché ; au demi-quota, elle atteint aussi les récoltes répétées.")
    print("      PRÉCÉDENTS, LUS SUR PIÈCES. Keynes (1943, § 8) : pour laisser un solde")
    print("      débiteur dépasser la moitié du quota, le conseil peut exiger une")
    print("      dévaluation ; au-delà des trois quarts, s'il n'est pas réduit en deux ans,")
    print("      il peut déclarer le défaut et suspendre le droit de tirer. Londres (1953) :")
    print("      trois gouvernements créanciers consentent des concessions sur le montant")
    print("      de leurs créances d'après-guerre, et le transfert des paiements suppose")
    print("      une balance des paiements qui les finance par les recettes courantes.")
    print("      CE QU'ELLE NE MONTRE PAS : l'inflation qu'importerait une dévaluation, que")
    print("      le modèle ne représente pas ; que des créanciers acceptent d'annuler (F6) ;")
    print("      ni le retrait d'un pays de la coalition, que les statuts du FMI prévoient")
    print("      (article XXVI) et que le modèle ne joue pas.")
    print("      CHOIX DE L'AUTEUR (D88 À D90) : la révision lit la position nette ; au-delà")
    print("      d'un quota de dette de recyclage, la dette est annulée et la parité du")
    print("      débiteur glisse jusqu'à l'équilibre de ses échanges.")


ADOPTIONS_DU_CREANCIER = (
    ("tenu par les règles de l'auteur", {}),
    ("délibère, comme dans l'histoire", {"symetrie_contraignante": False}),
    ("refuse la réévaluation", {"obligations_creancier": ("plafond",)}),
    ("refuse la conversion du reliquat", {"reliquat_plafond": None}),
    ("refuse recyclage et conversion", {"obligations_creancier": ("parite",), "reliquat_plafond": None}),
)


def anomalies_adoption(base, extra, horizon=80):
    """Dépassements et masses négatives cumulés sur les cinq scénarios."""
    depass = negatives = 0
    for sc in SCENARIOS:
        codes = mesurer_sortie(sc, horizon, **dict(base, **extra))["codes"]
        depass += codes["C6"]
        negatives += codes["C8"]
    return depass, negatives


def comparer_applicabilite_apres_sortie():
    """A43 (3b) : LE JUGEMENT D'APPLICABILITÉ REJOUÉ APRÈS D88 À D90.

    La configuration complète porte désormais la sortie des dettes durables. La
    sortie cherche ce qui démentirait un verdict plus favorable que D86 : horizon
    long, jeux de stress, créancier qui n'adopte pas ses obligations, et ce que coûte
    la sortie à qui la porte. L'auteur a rejugé le même jour (D91).
    """
    O = OPTIONS_AUTEUR_COMPLETES
    jeux = SCENARIOS + scenarios_de_stress()
    s4 = [x for x in SCENARIOS if x.cle == "S4"][0]
    print("")
    print("  (1) DIX JEUX SOUS LA CONFIGURATION COMPLÈTE — 200 et 400 périodes")
    print("  %-7s %4s %9s %11s %11s %9s %9s %9s"
          % ("jeu", "hor.", "anomalies", "dette D max", "dette P max", "annulée", "parité D", "parité P"))
    for sc in jeux:
        for h in (200, 400):
            r = mesurer_sortie(sc, h, **O)
            maxi = dict((c, max(p["dette"][c] for p in r["journal"]) / O["quotas"][c])
                        for c in ("DEF", "PAU"))
            print("  %-7s %4d %9d %11.2f %11.2f %9.2f %9.3f %9.3f"
                  % (sc.cle if h == 200 else "", h, r["graves"], maxi["DEF"], maxi["PAU"],
                     r["DEF"]["annulee"] + r["PAU"]["annulee"], r["DEF"]["parite"],
                     r["PAU"]["parite"]))
    print("      (dettes de recyclage maximales sur la trajectoire et annulations cumulées,")
    print("      en quotas du débiteur ; parités du déficitaire D et du pays pauvre P)")
    print("")
    print("  (2) SI LE CRÉANCIER N'ADOPTE PAS SES OBLIGATIONS — cinq scénarios, 80 périodes")
    print("  %-40s %22s %22s" % ("", "avant D88", "complète (D88 à D90)"))
    print("  %-40s %11s %10s %11s %10s"
          % ("créancier", "dépassements", "négatives", "dépassements", "négatives"))
    for libelle, extra in ADOPTIONS_DU_CREANCIER:
        avant = anomalies_adoption(OPTIONS_AVANT_D88, extra)
        apres = anomalies_adoption(O, extra)
        print("  %-40s %11d %10d %11d %10d" % (libelle, avant[0], avant[1], apres[0], apres[1]))
    refus = anomalies_adoption(O, {"sortie_dettes": dict(SORTIE_DETTES_AUTEUR,
                                                         modes=("devaluation_flux",))})
    print("  %-40s %11s %10s %11d %10d" % ("refuse l'annulation des dettes", "", "", refus[0], refus[1]))
    print("")
    print("  (3) CE QUE COÛTE LA SORTIE — S4, perte d'un débouché")
    print("  %-8s %8s %9s %9s %9s %9s %9s"
          % ("horizon", "dette D", "annulée", "parité D", "importe", "exporte", "anomalies"))
    for h in (40, 80, 200, 400, 600):
        r = mesurer_sortie(s4, h, **O)
        d = r["DEF"]
        print("  %-8d %8.2f %9.2f %9.3f %9.1f %9.1f %9d"
              % (h, d["dette"], d["annulee"], d["parite"], d["importe"], d["exporte"], r["graves"]))
    sans = mesurer_sortie(s4, 200, **OPTIONS_AVANT_D88)["DEF"]
    print("      (avant D88, à 200 périodes : dette %.2f quotas, parité %.3f, importations"
          % (sans["dette"], sans["parite"]))
    print("      %.1f et exportations %.1f par période)" % (sans["importe"], sans["exporte"]))
    print("      CE QUE LA SORTIE MONTRE. Sous la configuration complète, aucune anomalie")
    print("      dans les dix jeux jusqu'à 400 périodes, et aucune dette de recyclage ne")
    print("      dépasse un quota : les déséquilibres durables ont une sortie. Elle a un prix")
    print("      et des porteurs : le débiteur qui perd un débouché dévalue bien au-delà de")
    print("      la butée et importe beaucoup moins pour exporter davantage ; le créancier")
    print("      annule une part bornée de ses créances. À 400 périodes, les récoltes")
    print("      répétées atteignent aussi le seuil : le pays pauvre dévalue au-delà de la")
    print("      butée. Et rien ne change à la dépendance déjà mesurée : si le créancier")
    print("      délibère, ou refuse recyclage et conversion, les anomalies sont les mêmes")
    print("      qu'avant D88 ; s'il refuse seulement d'annuler, aucune n'apparaît.")
    print("      CE QU'ELLE NE MONTRE PAS : l'inflation qu'une dévaluation de cette ampleur")
    print("      importerait, et donc si elle serait tenable ; que des créanciers adoptent")
    print("      ces obligations et l'annulation (F6) ; le calibrage (F1) ; ni un monde de")
    print("      plus de trois pays.")
    print("      VERDICT DE L'AUTEUR (D91) : LES DÉSÉQUILIBRES DURABLES DEVIENNENT")
    print("      EXPÉRIMENTABLES EN COALITION, SOUS DEUX CONDITIONS DÉCLARÉES : mesurer")
    print("      l'inflation qu'importerait la dévaluation, et obtenir l'adhésion des")
    print("      créanciers à l'annulation. Aucune des deux n'est remplie par le modèle.")


def mesurer_regle(regle):
    """Synthèse d'une règle sur les cinq scénarios : contraction du déficitaire
    et solde final de l'excédentaire cumulés de S0 à S3, parité du déficitaire
    en S4, dépassements sous obligation contraignante puis délibérative, et
    plus grand pas de révision observé."""
    r = {"contraction": 0.0, "solde_exc": 0.0, "parite_s4": None,
         "depass": 0, "depass_delib": 0, "pas_max": 0.0}
    for sc in SCENARIOS:
        e, journal, anomalies = jouer(sc, regle=regle)
        _, _, delib = jouer(sc, regle=regle, symetrie_contraignante=False)
        if sc.cle in ("S0", "S1", "S2", "S3"):
            r["contraction"] += e.contraction["DEF"]
            r["solde_exc"] += e.soldes_par_periode["EXC"][-1]
        if sc.cle == "S4":
            r["parite_s4"] = e.parite["DEF"]
        r["depass"] += len([a for a in anomalies if a.startswith("[C6]")])
        r["depass_delib"] += len([a for a in delib if a.startswith("[C6]")])
        prec = dict((c, 1.0) for c in CODES)
        for p in journal:
            for c in CODES:
                if abs(p["parite"][c] - prec[c]) > 1e-12:
                    r["pas_max"] = max(r["pas_max"],
                                       abs(p["parite"][c] / prec[c] - 1.0))
                prec[c] = p["parite"][c]
    return r


def comparer_regles():
    """A43 (3b), CONDITION (1) : LA RÈGLE DE L'AUTEUR CONTRE LA RÈGLE MÉCANIQUE.

    Le modèle départage mal les règles et très bien les conditions. La sortie
    doit montrer les deux, et ne pas taire le résultat défavorable en S4.
    """
    print("")
    print("  RÈGLE DE L'AUTEUR — glissement de %.1f %% par période hors corridor,"
          % (100 * PAS_GLISSEMENT_AUTEUR))
    print("  butée cumulée de %.0f %% — CONTRE LA RÈGLE MÉCANIQUE (%.0f %% après %d"
          % (100 * BUTEE_AUTEUR, 100 * PAS_PARITE, PERSISTANCE_PARITE))
    print("  périodes hors corridor)")
    print("  %-4s %-10s %16s %10s %11s %13s %16s"
          % ("", "règle", "contraction DEF", "solde EXC", "parité DEF",
             "dépassements", "si délibérative"))
    for sc in SCENARIOS:
        for libelle, regle in (("mécanique", regle_mecanique),
                               ("auteur", regle_de_revision_auteur)):
            e, _, anomalies = jouer(sc, regle=regle)
            _, _, delib = jouer(sc, regle=regle, symetrie_contraignante=False)
            print("  %-4s %-10s %16.0f %10.0f %11.2f %13d %16d"
                  % (sc.cle, libelle, e.contraction["DEF"],
                     e.soldes_par_periode["EXC"][-1], e.parite["DEF"],
                     len([a for a in anomalies if a.startswith("[C6]")]),
                     len([a for a in delib if a.startswith("[C6]")])))
    print("      CE QUE LA SORTIE MONTRE. De S0 à S3, la règle de l'auteur réduit")
    print("      un peu la contraction du déficitaire. En S4, la butée borne la")
    print("      dérive de sa parité SANS y réduire la contraction : la perte")
    print("      durable d'un débouché passe à la procédure structurelle. Et sous")
    print("      obligation délibérative, les dépassements restent : AUCUNE RÈGLE DE")
    print("      RÉVISION NE REMPLACE L'OBLIGATION CONTRAIGNANTE DES EXCÉDENTAIRES.")
    print("      CE QU'ELLE NE MONTRE PAS : la prévisibilité — le modèle n'a ni")
    print("      anticipations ni spéculation —, ni aucun calibrage.")
    print("")
    print("  LES CINQ RÈGLES MESURÉES AVANT LE CHOIX DE L'AUTEUR")
    print("  %-28s %12s %10s %11s %8s %10s %8s"
          % ("règle", "contr. S0-S3", "EXC S0-S3", "parité S4", "dépass.",
             "délibér.", "pas max"))
    for libelle, regle in REGLES_MESUREES:
        r = mesurer_regle(regle)
        print("  %-28s %12.0f %10.0f %11.2f %8d %10d %7.1f %%"
              % (libelle, r["contraction"], r["solde_exc"], r["parite_s4"],
                 r["depass"], r["depass_delib"], 100 * r["pas_max"]))
    print("      LE MODÈLE DÉPARTAGE MAL LES RÈGLES ET TRÈS BIEN LES CONDITIONS.")
    print("      Les meilleures ne réduisent la contraction que de quelques pour")
    print("      cent ; « créancier d'abord » et un glissement trop lent font pire")
    print("      que la règle par défaut ; et sous obligation délibérative, toutes")
    print("      dépassent le plafond bien davantage.")


def comparer_guichets(scenario):
    """LA DÉCISION POSÉE : une part du soutien essentiel doit-elle être
    définitivement non remboursable ?"""
    print("")
    print("  LES DEUX GUICHETS — avec et sans allocation non remboursable")
    print("  %-22s %13s %14s %12s" % ("", "essentiel reçu", "contraction PAU",
                                      "dette PAU"))
    for actif in (False, True):
        e, journal, anomalies = jouer(scenario, allocation_active=actif)
        voulu = e.essentiel_voulu["PAU"]
        taux = (100.0 * e.essentiel_recu["PAU"] / voulu) if voulu else 100.0
        print("  %-22s %12.0f %% %14.0f %12.0f"
              % ("facilité seule" if not actif else "facilité + allocation",
                 taux, e.contraction["PAU"], e.fac["PAU"]))


def main():
    print("=" * 78)
    print("DÉSÉQUILIBRES COURANTS PERSISTANTS — version 2")
    print("=" * 78)
    print("Cinq corrections de l'auteur : horizon au-delà des maturités,")
    print("identité stock-flux complète, registres séparés au lieu d'un")
    print("« effort » agrégé, échanges élastiques, et un plafond qui est une")
    print("PROCÉDURE et non un nombre.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ. Horizon %d périodes, maturité %d,"
          % (PERIODES, DUREE_FACILITE))
    print("élasticité %.1f, plafond dur %.0f %% du quota, corridor %.0f %%."
          % (ELASTICITE, 100 * PLAFOND_SOLDE, 100 * CORRIDOR))

    for sc in SCENARIOS:
        rendre(sc)

    print("")
    print("=" * 78)
    print("LA DÉCISION POSÉE — S2, CHOC STRUCTUREL")
    print("=" * 78)
    sc = [x for x in SCENARIOS if x.cle == "S2"][0]
    comparer_guichets(sc)
    comparer_procedures(sc)

    print("")
    print("  CE QUE CELA ÉTABLIT, ET C'EST ÉTROIT. Une facilité REMBOURSABLE")
    print("  convient à un choc temporaire et NE PEUT PAS financer un déficit")
    print("  essentiel STRUCTUREL : le remboursement restitue la contraction.")
    print("  L'allocation non remboursable est le seul des deux guichets qui")
    print("  tienne l'exigence sur l'horizon. CE QUE CELA NE DIT PAS : qui la")
    print("  finance, à quelles conditions, et sous quel contrôle — c'est la")
    print("  question suivante, et elle est politique.")
    print("")
    print("  ET LE MODÈLE NE MESURE TOUJOURS PAS L'INFLATION. Les prix ne sont")
    print("  pas endogènes : les échanges répondent aux parités, pas les prix")
    print("  intérieurs à la monnaie. La « tension inflationniste » demandée")
    print("  n'est donc PAS publiée, faute de mécanisme qui la produise.")

    print("")
    print("=" * 78)
    print("A43 (3) SCINDÉ — CE QUE COÛTENT DES PARITÉS STRICTEMENT FIXES")
    print("=" * 78)
    comparer_parites()

    print("")
    print("=" * 78)
    print("A43 (3b), CONDITION (1) — LA RÈGLE DE RÉVISION DE L'AUTEUR")
    print("=" * 78)
    comparer_regles()

    print("")
    print("=" * 78)
    print("A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES")
    print("=" * 78)
    comparer_obligations()

    print("")
    print("=" * 78)
    print("A43 (3b), CONDITION (5) — LA PERTE DURABLE D'UN DÉBOUCHÉ")
    print("=" * 78)
    comparer_procedure_structurelle()

    print("")
    print("=" * 78)
    print("A43 (3b), CONDITION (4) — QUI FINANCE LES GUICHETS ET LA RECONVERSION")
    print("=" * 78)
    comparer_financement_guichets()

    print("")
    print("=" * 78)
    print("A43 (3b) — L'ACCUMULATION DE L'EXPORTATEUR SOUS CHOC STRUCTUREL")
    print("=" * 78)
    comparer_accumulation_exportateur()

    print("")
    print("=" * 78)
    print("D79 — LA DÉPENDANCE DURABLE À UNE IMPORTATION ESSENTIELLE")
    print("=" * 78)
    comparer_procedure_importateur()

    print("")
    print("=" * 78)
    print("A43 (3b), CONDITION (3) — LES SEUILS DU PLAFOND")
    print("=" * 78)
    comparer_seuils_du_plafond()

    print("")
    print("=" * 78)
    print("A43 (3b) — LE JUGEMENT D'APPLICABILITÉ")
    print("=" * 78)
    comparer_applicabilite()

    print("")
    print("=" * 78)
    print("D87 — LA SORTIE DES DETTES DURABLES")
    print("=" * 78)
    comparer_sortie_dettes()

    print("")
    print("=" * 78)
    print("A43 (3b) — LE JUGEMENT D'APPLICABILITÉ REJOUÉ APRÈS D88 À D90")
    print("=" * 78)
    comparer_applicabilite_apres_sortie()
    return 0


if __name__ == "__main__":
    sys.exit(main())
