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
        # (3) registres SÉPARÉS, jamais agrégés entre eux
        self.contraction = dict((c, 0.0) for c in CODES)
        self.expansion = dict((c, 0.0) for c in CODES)
        self.charges = dict((c, 0.0) for c in CODES)
        self.production = dict((c, 0.0) for c in CODES)
        self.essentiel_recu = dict((c, 0.0) for c in CODES)
        self.essentiel_voulu = dict((c, 0.0) for c in CODES)
        self.transfert_reel = dict((c, 0.0) for c in CODES)
        self.soldes_par_periode = dict((c, []) for c in CODES)


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
          recyclage_pret=False, reflux_apurement=None):
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
    registre compte ce que le reflux aurait à retirer, il ne le retire pas."""
    e = Etat()
    journal, anomalies = [], []
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
                                         if e.solde[c] < -CORRIDOR * QUOTA[c] else 0)
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
                        and e.solde[b] < -CORRIDOR * QUOTA[b]):
                    # restriction temporaire des importations non essentielles,
                    # levée dès le retour dans le corridor
                    desire[(a, b)] *= (1.0 - ps["restriction"])

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
            capacite = (e.solde[b] + recettes + PLAFOND_SOLDE * QUOTA[b]
                        + max(0.0, PLAFOND_FACILITE[b] - e.fac[b]))
            if procedure == "blocage":
                capacite = min(capacite, e.solde[b] + recettes
                               + PLAFOND_SOLDE * QUOTA[b])
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
            au_dela = e.solde[c] > CORRIDOR * QUOTA[c]
            e.attente_creancier[c] = e.attente_creancier[c] + 1 if au_dela else 0
        charge = dict((c, 0.0) for c in CODES)
        for c in CODES:
            crediteur = e.solde[c] > 0
            if crediteur and not tenu(c, "charge"):
                continue
            if not crediteur and not charge_debiteur:
                continue
            m = charge_graduee(e.solde[c], QUOTA[c])
            if m:
                e.solde[c] -= m
                e.solde[INST] += m
                e.charges[c] += m
                charge[c] = m

        # --- (5) LE PLAFOND EST UNE PROCÉDURE ---------------------------
        recyclage = dict((c, 0.0) for c in CODES)
        recu = dict((c, 0.0) for c in CODES)
        if procedure in ("recyclage", "conversion"):
            for c in CODES:
                exces = e.solde[c] - PLAFOND_SOLDE * QUOTA[c]
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

        # --- parités administrées ---------------------------------------
        for c in CODES:
            dehors = abs(e.solde[c]) > CORRIDOR * QUOTA[c]
            e.hors_corridor[c] = e.hors_corridor[c] + 1 if dehors else 0
            if regle is not None:
                # RÈGLE DE RÉVISION FOURNIE : elle décide seule du moment et
                # de l'ampleur ; une parité changée remet le compteur à zéro.
                # L'obligation excédentaire délibérative reste un paramètre
                # du régime, non de la règle.
                if not dehors or (e.solde[c] > 0 and not tenu(c, "parite")):
                    continue
                nouvelle = regle(e.solde[c], QUOTA[c], e.hors_corridor[c],
                                 e.parite[c])
                if nouvelle != e.parite[c]:
                    e.parite[c] = nouvelle
                    e.hors_corridor[c] = 0
                continue
            if e.hors_corridor[c] < PERSISTANCE_PARITE:
                continue
            crediteur = e.solde[c] > 0
            if crediteur and not tenu(c, "parite"):
                continue
            e.parite[c] *= (1.0 - PAS_PARITE) if crediteur \
                else (1.0 + PAS_PARITE)
            e.hors_corridor[c] = 0

        # --- masses monétaires, et (2) L'IDENTITÉ ----------------------
        for c in CODES:
            flux_nemo = (net[c] + tirage[c] + don[c] - rembourse[c]
                         - charge[c] + recu[c] - recyclage[c] + pret_net[c])
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
            if abs(e.solde[c]) > PLAFOND_SOLDE * QUOTA[c] + 1e-6:
                anomalies.append(
                    "[C6] période %d : le solde de %s (%+.0f) dépasse le "
                    "plafond dur (%.0f) — la procédure « %s » ne l'a pas "
                    "ramené" % (t, c, e.solde[c], PLAFOND_SOLDE * QUOTA[c],
                                procedure))

        # (2) IDENTITÉ STOCK-FLUX, vérifiée à chaque période et par pays.
        for c in CODES:
            attendu = (net[c] + tirage[c] + don[c] - rembourse[c] - charge[c]
                       + recu[c] - recyclage[c] + pret_net[c]) * e.parite[c]
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
                        "decouvert": e.decouvert})

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
OPTIONS_AUTEUR_COMPLETES = dict(OPTIONS_AUTEUR, recyclage_pret=True,
                                procedure_structurelle=PROCEDURE_AUTEUR)


def jouer_a_horizon(scenario, horizon, **options):
    """Joue un scénario sur un horizon donné, puis rend à PERIODES sa valeur."""
    global PERIODES
    garde = PERIODES
    try:
        PERIODES = horizon
        return jouer(scenario, **options)
    finally:
        PERIODES = garde


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
            r = mesurer_s4(h, **dict(OPTIONS_AUTEUR_COMPLETES, procedure_structurelle=proc))
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
        r = mesurer_s4(60, **dict(OPTIONS_AUTEUR_COMPLETES,
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
    """
    horizon = 40
    besoins = besoins_des_guichets(horizon, **OPTIONS_AUTEUR_COMPLETES)
    repere = besoin_moyen(besoins)
    print("")
    print("  (1) CE QUE LES GUICHETS VERSENT SANS REMBOURSEMENT — %d périodes," % horizon)
    print("      configuration complète de l'auteur")
    print("  %-4s %12s %13s %8s %18s" % ("", "allocations", "reconversion", "total",
                                         "premier versement"))
    for sc in SCENARIOS:
        r = mesurer_apurement(sc, horizon, None, **OPTIONS_AUTEUR_COMPLETES)
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
            r = mesurer_apurement(sc, horizon, k * repere, **OPTIONS_AUTEUR_COMPLETES)
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
    jeux = [(actif, h, mesurer_incidence_allocation(h, actif, **OPTIONS_AUTEUR_COMPLETES))
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
    print("      LE REGISTRE DU DÉCOUVERT N'EST PAS LE SOLDE DE L'INSTITUTION : dans les")
    print("      comptes, ce solde a toujours pour contrepartie les soldes positifs des")
    print("      pays. Apurer, c'est les réduire quelque part ; le modèle compte ce que")
    print("      le reflux aurait à retirer, il ne le retire pas.")
    print("      CE QU'ELLE NE MONTRE PAS : la taille du reflux — il n'est pas")
    print("      modélisé —, qui le paie, l'effet du démurrage maintenu (D76) sur le")
    print("      solde de l'excédentaire, l'inflation, ni aucun calibrage.")


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
    return 0


if __name__ == "__main__":
    sys.exit(main())
