#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPENSATION SYMÉTRIQUE DES DÉSÉQUILIBRES COURANTS — trois pays, plusieurs
périodes. Ouvert le 2026-09-09.

CE QUE CE MODÈLE ÉPROUVE.

Une union de compensation : chaque banque centrale tient un compte auprès de
l'institution NEMO, le commerce s'y règle, un corridor de solde est toléré des
deux côtés, des obligations graduées s'appliquent au-delà, une facilité
temporaire de liquidité existe, et les parités sont administrées — stables mais
révisables.

DEUX EXIGENCES DE L'AUTEUR, ET ELLES SONT LE CŒUR DU MODÈLE.
  (1) Un déficit causé par l'IMPORTATION DE BIENS ESSENTIELS ne doit PAS imposer
      automatiquement une contraction monétaire au pays concerné.
  (2) Le mécanisme doit empêcher l'ACCUMULATION INDÉFINIE D'EXCÉDENTS et la
      création monétaire correspondante.

AUCUN SEUIL N'EST FIXÉ. Corridor, tranches, pas de parité, plafond de
liquidité : tous sont des PARAMÈTRES DÉCLARÉS, aucun n'est calibré, et changer
l'un d'eux change le résultat. Le programme le répète parce que la tentation de
lire ses chiffres comme des estimations est forte.

CE QUE F6 IMPOSE À LA CONCEPTION, ET CE N'EST PAS NÉGOCIABLE.

Le corpus a lu sur pièces la seule tentative historique comparable — les
*Collected Writings* de Keynes, volume XXV, L1.C25 [S12]. La charge symétrique
de l'Union internationale de compensation existait : un pour cent l'an sur le
solde moyen dépassant le quart du quota, « whether it is a credit or a debit
balance ». MAIS ELLE N'ÉTAIT PAS CONTRAIGNANTE : le Governing Board « may
require » du déficitaire une dévaluation, le contrôle des sorties de capitaux et
la remise d'une part de ses réserves d'or ; l'excédentaire « shall discuss [...]
but shall retain the ultimate decision in its own hands ». Keynes l'avait
déclarée non essentielle et avait prévu le refus. ELLE A ÉTÉ REFUSÉE QUAND MÊME.

CONSÉQUENCE : LA SYMÉTRIE EST UN PARAMÈTRE, JAMAIS UNE HYPOTHÈSE. Chaque
scénario est joué DEUX FOIS — obligation excédentaire CONTRAIGNANTE, puis
DÉLIBÉRATIVE — et l'écart entre les deux répartitions de l'effort est le
résultat que ce modèle existe pour produire.

CE QUI EST SUIVI SÉPARÉMENT, comme demandé : les échanges RÉELS (volumes), les
SOLDES NEMO, les MASSES MONÉTAIRES nationales, la LIQUIDITÉ temporaire, les
AJUSTEMENTS DE PARITÉ, et la RÉPARTITION DE L'EFFORT.

USAGE :  python modeles/nemo_soldes.py
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------
# Les trois pays, et l'institution qui tient les comptes.
# ---------------------------------------------------------------------
PAYS = [
    ("EXC", "Pays excédentaire, exportateur net"),
    ("DEF", "Pays déficitaire, importateur industriel"),
    ("PAU", "Pays pauvre, dépendant d'importations essentielles"),
]
CODES = [p for p, _ in PAYS]
NOM = dict(PAYS)
INST = "INST"
COMPTES = CODES + [INST]

PERIODES = 8

# ---------------------------------------------------------------------
# PARAMÈTRES DÉCLARÉS. AUCUN N'EST CALIBRÉ.
# L'auteur a demandé le 2026-09-09 de NE PAS fixer les seuils : ceux-ci sont
# des repères destinés à faire tourner le mécanisme, pas des propositions.
# ---------------------------------------------------------------------
QUOTA = {"EXC": 1000, "DEF": 1000, "PAU": 400}

CORRIDOR = 0.25          # fraction du quota tolérée, des DEUX côtés
TRANCHE_2 = 0.50         # au-delà, obligations renforcées
TAUX_CHARGE_1 = 0.02     # sur la part du solde au-delà du corridor
TAUX_CHARGE_2 = 0.04     # sur la part au-delà de la seconde tranche

PLAFOND_LIQUIDITE = {"EXC": 0, "DEF": 300, "PAU": 300}
DUREE_LIQUIDITE = 4      # périodes avant remboursement exigible

PAS_PARITE = 0.05        # ajustement administré, par déclenchement
PERSISTANCE_PARITE = 2   # périodes consécutives hors corridor avant ajustement

SEUILS_CALIBRES = False  # NE PAS METTRE À True SANS UNE SOURCE PAR SEUIL


# ---------------------------------------------------------------------
# Les échanges. Matrice bilatérale : flux[a][b] = ce que a vend à b.
# Une matrice bilatérale garantit par construction que la somme des soldes
# est nulle — c'est une identité, non une hypothèse.
# ---------------------------------------------------------------------
def echanges_de_base():
    """Volumes, puis prix unitaires. Les deux sont suivis séparément."""
    v = {}
    for a in CODES:
        for b in CODES:
            v[(a, b)] = 0
    # l'excédentaire vend des biens manufacturés aux deux autres
    v[("EXC", "DEF")] = 100
    v[("EXC", "PAU")] = 40
    # le déficitaire vend des services à l'excédentaire
    v[("DEF", "EXC")] = 70
    # le pays pauvre vend des matières premières
    v[("PAU", "EXC")] = 25
    v[("PAU", "DEF")] = 10
    return v


# Ce qui est ESSENTIEL est déclaré poste par poste, jamais déduit.
ESSENTIEL = {("EXC", "PAU"): True}     # énergie et vivres vers le pays pauvre
PRIX_BASE = 1.0


class Scenario(object):
    def __init__(self, cle, titre, choc, note):
        self.cle, self.titre, self.choc, self.note = cle, titre, choc, note


def sans_choc(t, volumes, prix):
    return volumes, prix


def choc_energetique(t, volumes, prix):
    """Le prix des importations essentielles double sur trois périodes."""
    if 3 <= t <= 5:
        prix = dict(prix)
        prix[("EXC", "PAU")] = PRIX_BASE * 2.0
        prix[("EXC", "DEF")] = PRIX_BASE * 1.5
    return volumes, prix


def mauvaise_recolte(t, volumes, prix):
    """Les exportations du pays pauvre s'effondrent ; ses achats vivriers montent."""
    if 3 <= t <= 5:
        volumes = dict(volumes)
        volumes[("PAU", "EXC")] = 5
        volumes[("PAU", "DEF")] = 2
        volumes[("EXC", "PAU")] = 60
    return volumes, prix


def rupture_commerciale(t, volumes, prix):
    """Un canal se ferme : l'excédentaire cesse d'acheter au déficitaire."""
    if t >= 4:
        volumes = dict(volumes)
        volumes[("DEF", "EXC")] = 10
    return volumes, prix


SCENARIOS = [
    Scenario("S0", "Référence, sans choc", sans_choc,
             "les déséquilibres de structure sont déjà là : l'excédentaire vend "
             "plus qu'il n'achète, période après période"),
    Scenario("S1", "Choc énergétique", choc_energetique,
             "le prix des importations essentielles double : c'est le cas type "
             "où un déficit n'est pas une faute de politique"),
    Scenario("S2", "Mauvaise récolte", mauvaise_recolte,
             "les exportations du pays pauvre s'effondrent ET ses achats "
             "vivriers montent : le choc frappe des deux côtés à la fois"),
    Scenario("S3", "Rupture commerciale", rupture_commerciale,
             "un débouché se ferme durablement pour le déficitaire"),
]


# ---------------------------------------------------------------------
# Le mécanisme
# ---------------------------------------------------------------------
class Etat(object):
    def __init__(self):
        self.solde = dict((c, 0.0) for c in COMPTES)
        self.masse = dict((c, 1000.0) for c in CODES)
        self.liq = dict((c, 0.0) for c in CODES)
        self.tirages = dict((c, []) for c in CODES)      # (période, montant)
        self.parite = dict((c, 1.0) for c in CODES)
        self.hors_corridor = dict((c, 0) for c in CODES)
        # répartition de l'effort, suivie séparément
        self.charges = dict((c, 0.0) for c in CODES)
        self.contraction = dict((c, 0.0) for c in CODES)
        self.expansion = dict((c, 0.0) for c in CODES)
        self.ajust_parite = dict((c, 0.0) for c in CODES)
        self.soldes_par_periode = dict((c, []) for c in CODES)


def charge_graduee(solde, quota):
    """Barème gradué, appliqué au SOLDE EN VALEUR ABSOLUE.

    Symétrique par construction : le même barème vaut pour un solde créditeur
    et pour un solde débiteur. Que la face créditrice s'applique ou non est un
    PARAMÈTRE DE SCÉNARIO — voir F6.
    """
    a = abs(solde)
    c1 = CORRIDOR * quota
    c2 = TRANCHE_2 * quota
    charge = 0.0
    if a > c1:
        charge += TAUX_CHARGE_1 * (min(a, c2) - c1)
    if a > c2:
        charge += TAUX_CHARGE_2 * (a - c2)
    return charge


def jouer(scenario, symetrie_contraignante):
    """Retourne (états par période, anomalies).

    `symetrie_contraignante` : si False, l'excédentaire DISCUTE — charge et
    ajustement de parité ne lui sont pas appliqués. C'est la configuration
    historiquement observée, et la seule jamais adoptée.
    """
    e = Etat()
    journal, anomalies = [], []
    base = echanges_de_base()
    prix_base = dict((k, PRIX_BASE) for k in base)

    for t in range(1, PERIODES + 1):
        volumes, prix = scenario.choc(t, base, prix_base)

        # --- 1. ÉCHANGES RÉELS, suivis en volume ET en valeur -----------
        vend = dict((c, 0.0) for c in CODES)
        achete = dict((c, 0.0) for c in CODES)
        achete_essentiel = dict((c, 0.0) for c in CODES)
        vol_vend = dict((c, 0.0) for c in CODES)
        vol_achete = dict((c, 0.0) for c in CODES)
        for (a, b), vol in volumes.items():
            if not vol:
                continue
            valeur = vol * prix.get((a, b), PRIX_BASE)
            vend[a] += valeur
            achete[b] += valeur
            vol_vend[a] += vol
            vol_achete[b] += vol
            if ESSENTIEL.get((a, b)):
                achete_essentiel[b] += valeur

        # --- 2. RÈGLEMENT sur les comptes NEMO --------------------------
        net = dict((c, vend[c] - achete[c]) for c in CODES)
        for c in CODES:
            e.solde[c] += net[c]

        # --- 3. FACILITÉ DE LIQUIDITÉ ----------------------------------
        # RÈGLE CENTRALE : la part du déficit imputable aux importations
        # ESSENTIELLES est couverte, afin qu'elle n'impose aucune contraction.
        tirage = dict((c, 0.0) for c in CODES)
        for c in CODES:
            if e.solde[c] >= 0:
                continue
            eligible = min(-e.solde[c], achete_essentiel[c])
            marge = PLAFOND_LIQUIDITE[c] - e.liq[c]
            montant = max(0.0, min(eligible, marge))
            if montant:
                e.solde[c] += montant
                e.solde[INST] -= montant
                e.liq[c] += montant
                e.tirages[c].append((t, montant))
                tirage[c] = montant

        # --- remboursement à échéance ----------------------------------
        rembourse = dict((c, 0.0) for c in CODES)
        for c in CODES:
            restants = []
            for (t0, m) in e.tirages[c]:
                if t - t0 >= DUREE_LIQUIDITE:
                    e.solde[c] -= m
                    e.solde[INST] += m
                    e.liq[c] -= m
                    rembourse[c] += m
                else:
                    restants.append((t0, m))
            e.tirages[c] = restants

        # --- 4. OBLIGATIONS GRADUÉES, symétriques par barème ------------
        charge = dict((c, 0.0) for c in CODES)
        for c in CODES:
            crediteur = e.solde[c] > 0
            if crediteur and not symetrie_contraignante:
                continue          # l'excédentaire DISCUTE : rien ne lui est pris
            m = charge_graduee(e.solde[c], QUOTA[c])
            if m:
                # une charge alourdit un solde debiteur et reduit un
                # solde crediteur : dans les deux cas elle se retranche.
                e.solde[c] -= m
                e.solde[INST] += m
                e.charges[c] += m
                charge[c] = m

        # --- 5. PARITÉS ADMINISTRÉES -----------------------------------
        ajust = dict((c, 0.0) for c in CODES)
        for c in CODES:
            dehors = abs(e.solde[c]) > CORRIDOR * QUOTA[c]
            e.hors_corridor[c] = e.hors_corridor[c] + 1 if dehors else 0
            if e.hors_corridor[c] < PERSISTANCE_PARITE:
                continue
            crediteur = e.solde[c] > 0
            if crediteur and not symetrie_contraignante:
                continue          # l'excédentaire n'est pas tenu de réévaluer
            pas = -PAS_PARITE if crediteur else +PAS_PARITE
            e.parite[c] *= (1.0 + pas)
            e.ajust_parite[c] += abs(pas)
            ajust[c] = pas
            e.hors_corridor[c] = 0

        # --- 6. MASSES MONÉTAIRES NATIONALES ---------------------------
        # Le règlement crée ou détruit de la monnaie ; le tirage l'empêche de
        # se contracter ; le remboursement et la charge la contractent.
        for c in CODES:
            variation = (net[c] + tirage[c] - rembourse[c] - charge[c]) \
                * e.parite[c]
            e.masse[c] += variation
            if variation < 0:
                e.contraction[c] += -variation
            else:
                e.expansion[c] += variation
        for c in CODES:
            e.soldes_par_periode[c].append(e.solde[c])

        # --- CONTRÔLES, et ils peuvent échouer -------------------------
        total = sum(e.solde[c] for c in COMPTES)
        if abs(total) > 1e-6:
            anomalies.append(
                "[C1] période %d : la somme des soldes vaut %+.2f et non zéro — "
                "une compensation n'est pas une compensation si elle ne se "
                "boucle pas" % (t, total))
        for c in CODES:
            if e.liq[c] < -1e-9 or e.liq[c] > PLAFOND_LIQUIDITE[c] + 1e-9:
                anomalies.append(
                    "[C2] période %d : la liquidité de %s vaut %.1f, hors des "
                    "bornes [0, %d]" % (t, c, e.liq[c], PLAFOND_LIQUIDITE[c]))
        # RÈGLE DE L'AUTEUR : un déficit essentiel n'impose pas de contraction.
        for c in CODES:
            deficit_essentiel_non_couvert = max(
                0.0, min(-min(e.solde[c], 0.0), achete_essentiel[c]) - tirage[c])
            variation = (net[c] + tirage[c] - rembourse[c] - charge[c]) \
                * e.parite[c]
            if deficit_essentiel_non_couvert > 1e-6 and variation < -1e-6:
                anomalies.append(
                    "[C3] période %d : %s subit une contraction de %.1f alors "
                    "que %.1f de son déficit vient d'importations ESSENTIELLES "
                    "non couvertes — la règle de l'auteur est enfreinte"
                    % (t, c, -variation, deficit_essentiel_non_couvert))

        # C4 — SECONDE EXIGENCE DE L'AUTEUR : le mécanisme doit empêcher
        # l'accumulation indéfinie d'excédents et la création monétaire
        # correspondante. On ne peut le constater qu'à la fin, sur la
        # trajectoire : c'est fait après la boucle.
        journal.append({
            "t": t, "vol_vend": dict(vol_vend), "vol_achete": dict(vol_achete),
            "vend": dict(vend), "achete": dict(achete),
            "essentiel": dict(achete_essentiel),
            "solde": dict(e.solde), "masse": dict(e.masse),
            "liq": dict(e.liq), "parite": dict(e.parite),
            "tirage": tirage, "rembourse": rembourse,
            "charge": charge, "ajust": ajust})

    # --- C4, sur la trajectoire entière --------------------------------
    for c in CODES:
        serie = e.soldes_par_periode[c]
        moitie = len(serie) // 2
        croissance = serie[-1] - serie[moitie]
        if serie[-1] > CORRIDOR * QUOTA[c] and croissance > 0:
            anomalies.append(
                "[C4] %s finit à %+.0f, au-delà du corridor de %.0f, ET son "
                "excédent croît encore sur la seconde moitié (%+.0f) — "
                "L'ACCUMULATION INDÉFINIE N'EST PAS EMPÊCHÉE"
                % (c, serie[-1], CORRIDOR * QUOTA[c], croissance))
        if serie[-1] < -CORRIDOR * QUOTA[c] and croissance < 0:
            anomalies.append(
                "[C4] %s finit à %+.0f et son déficit se creuse encore "
                "(%+.0f) — le corridor ne l'a pas ramené" % (c, serie[-1],
                                                             croissance))
    return e, journal, anomalies


# ---------------------------------------------------------------------
# Restitution
# ---------------------------------------------------------------------
def effort(e):
    """La répartition de l'effort, suivie séparément comme demandé.

    L'EXPANSION EST RAPPORTÉE À CÔTÉ DE LA CONTRACTION, et ce n'est pas un
    ornement : la contraction du déficitaire a pour miroir exact l'expansion de
    l'excédentaire. Ne compter que la première ferait passer pour un coût
    unilatéral ce qui est un transfert.
    """
    return dict((c, {"charges": e.charges[c],
                     "contraction": e.contraction[c],
                     "expansion": e.expansion[c],
                     "parite": e.ajust_parite[c],
                     "total": e.charges[c] + e.contraction[c]}) for c in CODES)


def rendre(scenario):
    print("")
    print("=" * 78)
    print("%s — %s" % (scenario.cle, scenario.titre))
    print("=" * 78)
    print("  %s" % scenario.note)

    resultats = {}
    for contraignante in (True, False):
        e, journal, anomalies = jouer(scenario, contraignante)
        resultats[contraignante] = (e, journal, anomalies)

    # --- la chronologie, sous obligation contraignante ------------------
    e, journal, anomalies = resultats[True]
    print("")
    print("  CHRONOLOGIE — obligation excédentaire CONTRAIGNANTE")
    print("  %2s | %-28s | %-26s | %s"
          % ("t", "soldes NEMO", "masses monétaires", "liquidité"))
    for j in journal:
        soldes = " ".join("%s%+6.0f" % (c, j["solde"][c]) for c in CODES)
        masses = " ".join("%s%6.0f" % (c, j["masse"][c]) for c in CODES)
        liq = " ".join("%s%4.0f" % (c, j["liq"][c]) for c in CODES if
                       PLAFOND_LIQUIDITE[c])
        print("  %2d | %-28s | %-26s | %s" % (j["t"], soldes, masses, liq))

    print("")
    print("  ÉCHANGES RÉELS ET PARITÉS — mêmes périodes, suivis séparément")
    print("  %2s | %-26s | %s" % ("t", "volumes vendus", "parités"))
    for j in journal:
        vols = " ".join("%s%5.0f" % (c, j["vol_vend"][c]) for c in CODES)
        par = " ".join("%s%5.2f" % (c, j["parite"][c]) for c in CODES)
        print("  %2d | %-26s | %s" % (j["t"], vols, par))

    # --- LES DEUX EXIGENCES DE L'AUTEUR, jugees explicitement -----------
    c3 = [a for a in anomalies if a.startswith("[C3]")]
    c4 = [a for a in anomalies if a.startswith("[C4]")]
    print("")
    print("  LES DEUX EXIGENCES DE L'AUTEUR")
    print("    (1) un déficit d'importations ESSENTIELLES n'impose pas de")
    print("        contraction : %s"
          % ("TENUE" if not c3 else "ENFREINTE, %d fois" % len(c3)))
    print("    (2) l'accumulation indéfinie d'excédents est empêchée : %s"
          % ("TENUE" if not c4 else "NON TENUE"))

    if anomalies:
        print("")
        print("  DÉTAIL DES MANQUEMENTS")
        for a in dict.fromkeys(anomalies):
            print("    %s" % a)

    # --- LE RÉSULTAT QUE F6 COMMANDE -----------------------------------
    print("")
    print("  RÉPARTITION DE L'EFFORT — et c'est ce que F6 met en jeu")
    print("  %-26s %8s %11s %10s %8s"
          % ("", "charges", "contraction", "expansion", "total"))
    for contraignante in (True, False):
        e2 = resultats[contraignante][0]
        eff = effort(e2)
        titre = ("obligation excédentaire CONTRAIGNANTE" if contraignante
                 else "obligation excédentaire DÉLIBÉRATIVE (cas historique)")
        print("  %s" % titre)
        for c in CODES:
            print("    %-26s %8.1f %11.1f %10.1f %8.1f"
                  % (NOM[c][:26], eff[c]["charges"], eff[c]["contraction"],
                     eff[c]["expansion"], eff[c]["total"]))
        part_exc = eff["EXC"]["total"]
        part_def = eff["DEF"]["total"] + eff["PAU"]["total"]
        tot = part_exc + part_def
        if tot > 0:
            print("    part portée par l'excédentaire : %5.1f %%"
                  % (100.0 * part_exc / tot))
    return resultats


def main():
    print("=" * 78)
    print("COMPENSATION SYMÉTRIQUE DES DÉSÉQUILIBRES COURANTS — trois pays")
    print("=" * 78)
    print("Chaque banque centrale tient un compte auprès de l'institution. Le")
    print("commerce s'y règle. Un corridor est toléré DES DEUX CÔTÉS, des")
    print("obligations graduées s'appliquent au-delà, une facilité temporaire")
    print("de liquidité couvre les déficits d'importations ESSENTIELLES, et les")
    print("parités sont administrées.")
    print("")
    print("AUCUN SEUIL N'EST CALIBRÉ. Corridor %.0f %% du quota, tranche %.0f %%,"
          % (100 * CORRIDOR, 100 * TRANCHE_2))
    print("charges %.0f et %.0f %%, pas de parité %.0f %%, plafonds de liquidité"
          % (100 * TAUX_CHARGE_1, 100 * TAUX_CHARGE_2, 100 * PAS_PARITE))
    print("déclarés : CE SONT DES REPÈRES POUR FAIRE TOURNER LE MÉCANISME,")
    print("PAS DES PROPOSITIONS. Changer l'un d'eux change tous les résultats.")
    print("")
    print("ET LA SYMÉTRIE EST UN PARAMÈTRE, JAMAIS UNE HYPOTHÈSE — F6 : la")
    print("charge symétrique de Keynes existait, elle n'était pas contraignante")
    print("pour le créancier, et elle a été refusée quand même.")

    tous = [(s, rendre(s)) for s in SCENARIOS]

    print("")
    print("=" * 78)
    print("CE QUE LE MODÈLE MONTRE, ET CE QU'IL NE MONTRE PAS")
    print("=" * 78)
    ecarts = []
    for s, res in tous:
        a = effort(res[True][0])
        b = effort(res[False][0])
        pa = a["EXC"]["total"]
        pb = b["EXC"]["total"]
        ta = pa + a["DEF"]["total"] + a["PAU"]["total"]
        tb = pb + b["DEF"]["total"] + b["PAU"]["total"]
        if ta > 0 and tb > 0:
            ecarts.append((s.cle, 100.0 * pa / ta, 100.0 * pb / tb))
    print("  part de l'effort portée par l'excédentaire, par scénario :")
    print("  %-4s %14s %16s" % ("", "contraignante", "délibérative"))
    for cle, x, y in ecarts:
        print("  %-4s %13.1f %% %15.1f %%" % (cle, x, y))
    print("")
    print("  L'ÉCART ENTRE LES DEUX COLONNES EST LE RÉSULTAT PRINCIPAL. Il")
    print("  mesure ce que la symétrie apporte — et c'est exactement la")
    print("  disposition dont le corpus a établi, sur pièces, qu'elle est celle")
    print("  qui saute [F6, L1.C25].")
    print("")
    print("  TROIS RÉSULTATS, ET LES TROIS SONT CONTRE LA SOLUTION DE RÉFÉRENCE")
    print("  TELLE QUE PARAMÉTRÉE ICI.")
    print("")
    print("  (1) LA PROTECTION DES IMPORTATIONS ESSENTIELLES CÈDE QUAND LE CHOC")
    print("      DURE PLUS LONGTEMPS QUE LA FACILITÉ. Le remboursement à")
    print("      échéance ne supprime pas la contraction : il la DIFFÈRE, et il")
    print("      la fait tomber pendant que le choc dure encore. Une facilité")
    print("      « temporaire » ne protège que d'un choc temporaire.")
    print("")
    print("  (2) LE CORRIDOR N'EMPÊCHE PAS L'ACCUMULATION, DES DEUX CÔTÉS. Il")
    print("      TARIFE le dépassement, il ne le BORNE pas. Un taux appliqué au")
    print("      dépassement fait converger le solde vers CORRIDOR PLUS FLUX")
    print("      DIVISÉ PAR TAUX : il borne asymptotiquement, il ne pose aucun")
    print("      plafond, et la convergence peut être plus lente que le choc.")
    print("      Empêcher demande un PLAFOND DUR, ou une charge croissant plus")
    print("      vite que le solde. Le test le vérifie sur les deux barèmes.")
    print("")
    print("  (3) MÊME SOUS OBLIGATION CONTRAIGNANTE, LA SYMÉTRIE EST NOMINALE.")
    print("      La charge graduée reste d'un ordre de grandeur inférieur à la")
    print("      contraction qu'elle devrait compenser. Et l'expansion monétaire")
    print("      de l'excédentaire, miroir exact de la contraction du")
    print("      déficitaire, n'est comptée nulle part comme un avantage.")
    print("")
    print("  CE QUE CELA NE DIT PAS : que le mécanisme soit impossible. Cela dit")
    print("  que CES PARAMÈTRES ne satisfont ni l'une ni l'autre exigence, et")
    print("  pourquoi. Les seuils sont à fixer — c'est le travail suivant, et")
    print("  l'auteur a demandé de ne pas le faire avant ce modèle.")
    print("")
    print("  CE QUE LE MODÈLE NE MONTRE PAS. Aucun comportement : ni élasticité,")
    print("  ni substitution d'importations, ni réaction des prix intérieurs, ni")
    print("  capacité productive, ni mouvement de capitaux — ceux-ci sont")
    print("  réglementés par A32 et sortent du périmètre. Les chocs sont")
    print("  IMPOSÉS, non expliqués. Et aucun seuil n'est calibré : le modèle")
    print("  dit ce qui suit des repères qu'on lui a donnés, rien de plus.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
