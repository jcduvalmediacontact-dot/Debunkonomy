#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contrôle du corpus Debunk'Onomy.

Applique les règles de convention.md (révision 7).
Le script est l'autorité : il refuse la publication en cas d'erreur bloquante.

Usage :
    python controle.py                 # contrôle seul
    python controle.py --publier       # contrôle + règles de publication
    python controle.py --maj-etat      # enregistre l'état après arbitrage
    python controle.py --maj-etat --editorial
                                       # déclare les changements non substantiels
    python controle.py --maj-etat --fond
                                       # déclare les changements substantiels
                                       # (même jour que la revision_de_fond en cours)

Dépendance : PyYAML  (pip install pyyaml)
"""

import sys
import json
import hashlib
import re
from datetime import date, datetime
from pathlib import Path

# Sortie UTF-8 sous Windows (cmd, PowerShell) : sans quoi les accents des
# messages ressortent en mojibake dans le diagnostic.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML manquant. Installer avec : pip install pyyaml\n"
        "Interpreteur utilise : " + sys.executable
    )

# PyYAML peut etre PRESENT et MAL RESOLU : installation partielle, paquet
# homonyme, ou module masque par un fichier yaml.py du repertoire courant.
# L'ImportError ci-dessus ne voit pas ce cas ; le diagnostic qui suit si.
if not hasattr(yaml, "safe_load"):
    sys.exit(
        "PyYAML mal resolu : le module importe n'expose pas safe_load.\n"
        "  module     : " + getattr(yaml, "__file__", "(sans fichier)")
        + "\n  interprete : " + sys.executable
        + "\nCauses frequentes : un fichier yaml.py dans le repertoire\n"
        "courant, ou le paquet 'yaml' installe au lieu de 'pyyaml'.\n"
        "Verifier avec : python -c \"import yaml; print(yaml.__file__)\""
    )

RACINE = Path(__file__).resolve().parent
VOCABULAIRE = RACINE / "vocabulaire.yaml"
HORIZONS = RACINE / "horizons.yaml"
LIVRES = RACINE / "livres.yaml"
ETAT = RACINE / ".etat-corpus.json"

# --- Schéma, d'après la table des champs de la convention -------------------

CHAMPS_OBLIGATOIRES = {
    "chapitre", "titre", "livre", "langue", "licence", "type", "statut",
    "revision_de_fond", "autorite", "citable", "regime", "resume",
    "sources_primaires", "verifications_en_attente", "concepts", "renvois",
}
CHAMPS_CONDITIONNELS = {"partie", "chapitres_sources", "verifiee_le"}
CHAMPS_CONNUS = CHAMPS_OBLIGATOIRES | CHAMPS_CONDITIONNELS

CHAMPS_SOURCE_OBLIGATOIRES = {"ref", "nature", "reference", "date_verification"}
CHAMPS_SOURCE_CONNUS = CHAMPS_SOURCE_OBLIGATOIRES | {"url", "horizon", "motif_horizon"}

STATUTS = ["brouillon", "audit_contradictoire", "audit_factuel", "verifie"]
TYPES = ["chapitre", "synthese"]
AUTORITES = ["canonique", "preparatoire"]
REGIMES = ["descriptif", "hybride", "conception"]
NATURES = ["normatif", "jurisprudence", "donnees", "actualite", "theorie"]
BALISES = ["hypothese", "norme", "etat"]

RE_BALISE = re.compile(r"^::([a-z_]+)::", re.MULTILINE)
RE_DUREE = re.compile(r"^(\d+)\s*([jma])$")

HORIZONS_DEFAUT = {
    "normatif":      {"mode": "revue", "horizon": "1a", "motif": "Vérifier que le texte est toujours en vigueur."},
    "jurisprudence": {"mode": "revue", "horizon": "1a", "motif": "Vérifier l'absence d'appel ou de renversement."},
    "donnees":       {"mode": "date",  "horizon": "1a", "motif": "Séries révisées."},
    "actualite":     {"mode": "date",  "horizon": "9m", "motif": "État de la situation vite périmé."},
    "theorie":       {"mode": "date",  "horizon": "aucun", "motif": "Travaux stabilisés."},
}

blocages, decisions, alertes = [], [], []


def bloque(fichier, message):
    blocages.append((fichier, message))


def decide(fichier, message):
    decisions.append((fichier, message))


def alerte(fichier, message):
    alertes.append((fichier, message))


# --- Utilitaires -----------------------------------------------------------

def jours(duree):
    """'9m' -> 274, '1a' -> 365, '30j' -> 30, 'aucun' -> None."""
    if not duree or duree == "aucun":
        return None
    m = RE_DUREE.match(str(duree).strip())
    if not m:
        return None
    n, unite = int(m.group(1)), m.group(2)
    return n * {"j": 1, "m": 30, "a": 365}[unite]


def en_date(valeur):
    if isinstance(valeur, date):
        return valeur
    if isinstance(valeur, datetime):
        return valeur.date()
    try:
        return datetime.strptime(str(valeur), "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def normalise(texte):
    return "\n".join(l.strip() for l in texte.strip().splitlines() if l.strip())


def empreinte(*morceaux):
    h = hashlib.sha256()
    for m in morceaux:
        h.update(normalise(str(m)).encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:16]


def lire_fichier(chemin):
    """Retourne (en-tête, corps) ou (None, erreur)."""
    brut = chemin.read_text(encoding="utf-8")
    if not brut.startswith("---"):
        return None, "en-tête YAML absent"
    parties = brut.split("---", 2)
    if len(parties) < 3:
        return None, "en-tête YAML non refermé"
    try:
        entete = yaml.safe_load(parties[1])
    except yaml.YAMLError as e:
        return None, f"YAML invalide : {e}"
    if not isinstance(entete, dict):
        return None, "en-tête vide ou mal formé"
    return (entete, parties[2]), None


# --- Chargement -------------------------------------------------------------

def charger_vocabulaire():
    if not VOCABULAIRE.exists():
        return {}
    contenu = yaml.safe_load(VOCABULAIRE.read_text(encoding="utf-8"))
    if not contenu:
        return {}
    return {e["terme"]: e for e in contenu if isinstance(e, dict) and "terme" in e}


def charger_livres():
    """Matricules déclarés. Seul l'existence du matricule est contrôlée :
    collections, motifs et statuts sont matière d'arbitrage éditorial."""
    if not LIVRES.exists():
        return None
    contenu = yaml.safe_load(LIVRES.read_text(encoding="utf-8")) or {}
    entrees = contenu.get("livres") or []
    return {e["livre"]: e for e in entrees if isinstance(e, dict) and "livre" in e}


STATUTS_ARBITRAGE = {"ouvert", "oriente", "arbitre", "conditionnel"}
TRANCHE_PAR = {"auteur", "corpus", "non-tranche"}
SECTIONS_ARBITRAGE = ("arbitrages", "falsifieurs",
                      "pieces_de_conception_manquantes")
# Le registre est une PROJECTION : il porte des etats, jamais des raisonnements.
# Ces deux plafonds sont la seule chose qui empeche mecaniquement qu'il
# redevienne un second protocole. Ils ont ete poses le 2026-09-09, apres que le
# registre eut atteint 833 lignes en dupliquant passe-2.md et falsification.md.
CHAMPS_ARBITRAGE_OBLIGATOIRES = ("id", "objet", "statut", "tranche_par",
                                 "decision", "texte", "maj")
LONGUEUR_DECISION = 500
LONGUEUR_ACQUISITION = 400


def charger_arbitrages():
    """Registre des arbitrages et falsifieurs ouverts.

    Ce registre est une projection : les textes de `protocoles/` font foi,
    et en cas d'ecart c'est le registre qui est corrige, jamais l'inverse.

    UNE ABSENCE OU UNE ERREUR DE LECTURE BLOQUE. Motif : un registre qui
    disparait en silence rendrait au controle l'image trompeuse qu'il a
    precisement pour objet de corriger.
    """
    chemin = RACINE / "arbitrages.yaml"
    if not chemin.exists():
        bloque("arbitrages.yaml", "registre des arbitrages absent")
        return None
    try:
        registre = yaml.safe_load(chemin.read_text(encoding="utf-8"))
    except Exception as erreur:
        bloque("arbitrages.yaml", f"registre illisible : {erreur}")
        return None
    if not isinstance(registre, dict):
        bloque("arbitrages.yaml", "registre vide ou mal forme")
        return None

    vus = {}
    for cle in SECTIONS_ARBITRAGE:
        entrees = registre.get(cle)
        if entrees is None:
            bloque("arbitrages.yaml", f"section « {cle} » absente")
            continue
        if not isinstance(entrees, list):
            bloque("arbitrages.yaml", f"section « {cle} » n'est pas une liste")
            continue
        for rang, e in enumerate(entrees, 1):
            ou = f"{cle}[{rang}]"
            if not isinstance(e, dict):
                bloque("arbitrages.yaml", f"{ou} : entree mal formee")
                continue
            ident = e.get("id")
            for champ in CHAMPS_ARBITRAGE_OBLIGATOIRES:
                if not e.get(champ):
                    bloque("arbitrages.yaml",
                           f"{ou} ({ident}) : champ « {champ} » manquant")

            # Le texte qui fait foi doit exister : un renvoi mort rendrait la
            # projection invérifiable, ce qui est pire qu'une projection absente.
            texte = e.get("texte")
            if texte and not (RACINE.parent / str(texte)).exists():
                bloque("arbitrages.yaml",
                       f"{ou} ({ident}) : texte « {texte} » introuvable")

            date_maj = e.get("maj")
            if date_maj:
                try:
                    date.fromisoformat(str(date_maj))
                except ValueError:
                    bloque("arbitrages.yaml",
                           f"{ou} ({ident}) : maj « {date_maj} » n'est pas "
                           f"une date AAAA-MM-JJ")

            for champ, plafond in (("decision", LONGUEUR_DECISION),
                                   ("acquisition_bloquante",
                                    LONGUEUR_ACQUISITION)):
                valeur = e.get(champ)
                if valeur:
                    n = len(" ".join(str(valeur).split()))
                    if n > plafond:
                        bloque("arbitrages.yaml",
                               f"{ou} ({ident}) : « {champ} » fait {n} signes "
                               f"pour un plafond de {plafond}. Le registre "
                               f"projette, il ne raisonne pas : le "
                               f"développement va au texte qui fait foi.")
            if ident:
                if ident in vus:
                    bloque("arbitrages.yaml",
                           f"identifiant duplique : « {ident} » "
                           f"({vus[ident]} et {ou})")
                else:
                    vus[ident] = ou
            statut = e.get("statut")
            if statut and statut not in STATUTS_ARBITRAGE:
                bloque("arbitrages.yaml",
                       f"{ou} ({ident}) : statut « {statut} » hors liste "
                       f"{sorted(STATUTS_ARBITRAGE)}")
            tp = e.get("tranche_par")
            if tp and tp not in TRANCHE_PAR:
                bloque("arbitrages.yaml",
                       f"{ou} ({ident}) : tranche_par « {tp} » hors liste "
                       f"{sorted(TRANCHE_PAR)}")
            if statut == "arbitre" and tp == "non-tranche":
                bloque("arbitrages.yaml",
                       f"{ou} ({ident}) : declare « arbitre » sans qui a tranche")
            if statut != "arbitre" and tp == "auteur" and not e.get("note"):
                alerte("arbitrages.yaml",
                       f"{ident} : oriente par l'auteur sans note disant "
                       f"ce qui reste ouvert")
    # `lie_a` declare que deux entrees sont les faces d'un meme probleme.
    # La reciprocite est exigee : une relation qui ne vaudrait que dans un sens
    # laisserait l'autre entree ignorer qu'elle est engagee.
    liens = {}
    for cle in SECTIONS_ARBITRAGE:
        for e in registre.get(cle) or []:
            if isinstance(e, dict) and e.get("id"):
                liens[e["id"]] = e.get("lie_a") or []
    for ident, cibles in liens.items():
        if not isinstance(cibles, list):
            bloque("arbitrages.yaml", f"{ident} : « lie_a » n'est pas une liste")
            continue
        for cible in cibles:
            if cible not in liens:
                bloque("arbitrages.yaml",
                       f"{ident} : « lie_a » renvoie à « {cible} », inconnu")
            elif ident not in (liens.get(cible) or []):
                bloque("arbitrages.yaml",
                       f"lien non réciproque : {ident} → {cible}, "
                       f"mais {cible} ne renvoie pas à {ident}")

    return registre


def charger_horizons():
    if not HORIZONS.exists():
        return HORIZONS_DEFAUT
    contenu = yaml.safe_load(HORIZONS.read_text(encoding="utf-8"))
    return contenu or HORIZONS_DEFAUT


def charger_etat():
    if ETAT.exists():
        return json.loads(ETAT.read_text(encoding="utf-8"))
    return {}


# --- Contrôles par fichier --------------------------------------------------

def controler_entete(nom, entete):
    inconnus = set(entete) - CHAMPS_CONNUS
    for champ in sorted(inconnus):
        bloque(nom, f"champ inconnu : « {champ} » — toute évolution du schéma passe par une migration")

    if "partie" in entete and entete["partie"] != 1:
        return  # partie secondaire : en-tête minimal, rien d'autre à exiger

    for champ in sorted(CHAMPS_OBLIGATOIRES - set(entete)):
        bloque(nom, f"champ obligatoire absent : « {champ} »")

    for champ, valeurs in (("statut", STATUTS), ("type", TYPES),
                           ("autorite", AUTORITES), ("regime", REGIMES)):
        if champ in entete and entete[champ] not in valeurs:
            bloque(nom, f"{champ} « {entete[champ]} » hors des valeurs admises : {', '.join(valeurs)}")

    if not en_date(entete.get("revision_de_fond")):
        bloque(nom, "revision_de_fond absente ou mal formée (AAAA-MM-JJ)")


def controler_sources(nom, entete):
    for src in entete.get("sources_primaires") or []:
        if not isinstance(src, dict):
            bloque(nom, "source primaire mal formée")
            continue
        ref = src.get("ref", "?")
        for champ in sorted(CHAMPS_SOURCE_OBLIGATOIRES - set(src)):
            bloque(nom, f"source {ref} : champ obligatoire absent « {champ} »")
        for champ in sorted(set(src) - CHAMPS_SOURCE_CONNUS):
            bloque(nom, f"source {ref} : champ inconnu « {champ} »")
        if src.get("nature") and src["nature"] not in NATURES:
            bloque(nom, f"source {ref} : nature « {src['nature']} » inconnue")
        if "date_verification" in src and not en_date(src["date_verification"]):
            bloque(nom, f"source {ref} : date_verification mal formée")
        if "horizon" in src and not src.get("motif_horizon"):
            bloque(nom, f"source {ref} : dérogation d'horizon sans motif_horizon")


def controler_statut(nom, entete):
    statut = entete.get("statut")
    attente = entete.get("verifications_en_attente") or []
    if statut == "verifie":
        if attente:
            bloque(nom, "statut « verifie » avec des vérifications en attente")
        # Une synthèse n'a pas de sources documentaires : ses sources sont des
        # chapitres, contrôlés par controler_synthese().
        if entete.get("type") != "synthese" and not (entete.get("sources_primaires") or []):
            bloque(nom, "statut « verifie » sans aucune source primaire")
        if not (entete.get("concepts") or []):
            bloque(nom, "statut « verifie » sans aucun concept déclaré")
    elif attente:
        alerte(nom, f"{len(attente)} vérification(s) en attente")

    # Les marqueurs d'état ne valent que s'ils ne peuvent pas mentir :
    # un texte non vérifié ne peut pas se déclarer citable.
    if entete.get("citable") is True and statut != "verifie":
        bloque(nom, f"citable: true avec statut « {statut} » — "
                    f"un chapitre n'est citable qu'une fois vérifié")


def controler_synthese(nom, entete, chapitres):
    if entete.get("type") != "synthese":
        for champ in ("chapitres_sources", "verifiee_le"):
            if champ in entete:
                bloque(nom, f"« {champ} » réservé aux entrées de type synthese")
        return

    if not entete.get("chapitres_sources"):
        bloque(nom, "synthèse sans chapitres_sources")
    verifiee = en_date(entete.get("verifiee_le"))
    if not verifiee:
        bloque(nom, "synthèse sans verifiee_le valide")

    for cible in entete.get("chapitres_sources") or []:
        if cible not in chapitres:
            bloque(nom, f"chapitre source inexistant : {cible}")
        elif verifiee:
            revision = en_date(chapitres[cible]["entete"].get("revision_de_fond"))
            if revision and revision > verifiee:
                alerte(nom, f"synthèse périmée : {cible} révisé sur le fond le {revision}, "
                            f"entrée vérifiée le {verifiee}")


def controler_balises(nom, corps):
    for balise in set(RE_BALISE.findall(corps)):
        if balise not in BALISES:
            bloque(nom, f"balise de régime inconnue : ::{balise}:: — "
                        f"seules {', '.join('::%s::' % b for b in BALISES)} existent")


def controler_fraicheur(nom, entete, horizons):
    aujourdhui = date.today()
    for src in entete.get("sources_primaires") or []:
        if not isinstance(src, dict):
            continue
        nature = src.get("nature")
        regle = horizons.get(nature, {})
        mode = regle.get("mode", "date")
        if "horizon" in src:
            limite, motif, origine = jours(src["horizon"]), src.get("motif_horizon"), "dérogation"
        else:
            limite, motif, origine = jours(regle.get("horizon")), regle.get("motif"), "défaut de nature"
        if limite is None:
            continue
        verif = en_date(src.get("date_verification"))
        if not verif:
            continue
        age = (aujourdhui - verif).days
        if age > limite:
            libelle = ("contenu potentiellement périmé" if mode == "date"
                       else "revue due, sans changement connu")
            alerte(nom, f"source {src.get('ref', '?')} ({nature}) : {libelle} — "
                        f"{age} j depuis le {verif}, horizon {limite} j ({origine}) — {motif}")


def controler_empreintes(nom, cle, entete, corps, etat):
    edito = empreinte(corps, entete.get("resume", ""))
    meta = empreinte(json.dumps(
        {k: str(v) for k, v in sorted(entete.items()) if k != "resume"},
        ensure_ascii=False))
    ancien = etat.get(cle)
    if ancien and ancien.get("editoriale") != edito:
        if str(ancien.get("revision_de_fond")) == str(entete.get("revision_de_fond")):
            decide(nom, "texte modifié sans que revision_de_fond ait bougé — "
                        "qualifier en révision de fond, ou déclarer le changement éditorial")
    return {"editoriale": edito, "metadonnees": meta,
            "revision_de_fond": str(entete.get("revision_de_fond"))}


# --- Programme principal ----------------------------------------------------

def main():
    publier = "--publier" in sys.argv
    maj_etat = "--maj-etat" in sys.argv
    editorial = "--editorial" in sys.argv
    fond = "--fond" in sys.argv

    vocabulaire = charger_vocabulaire()
    livres = charger_livres()
    horizons = charger_horizons()
    etat = charger_etat()
    nouvel_etat = {}

    fichiers = sorted(RACINE.glob("livre-*/*.md"))
    if not fichiers:
        sys.exit(f"Aucun chapitre trouvé sous {RACINE}/livre-*/")

    chapitres, parties, concepts_employes = {}, {}, set()

    # Première passe : lecture et contrôles locaux
    for chemin in fichiers:
        nom = str(chemin.relative_to(RACINE))
        resultat, erreur = lire_fichier(chemin)
        if erreur:
            bloque(nom, erreur)
            continue
        entete, corps = resultat

        cle = entete.get("chapitre")
        if not cle:
            bloque(nom, "champ obligatoire absent : « chapitre »")
            continue

        numero = entete.get("partie", 1)
        parties.setdefault(cle, {})[numero] = nom

        controler_entete(nom, entete)
        controler_balises(nom, corps)

        if numero != 1:
            continue

        if cle in chapitres:
            bloque(nom, f"identifiant dupliqué : {cle} déjà utilisé par {chapitres[cle]['nom']}")
            continue
        chapitres[cle] = {"nom": nom, "entete": entete, "corps": corps}

        controler_sources(nom, entete)
        controler_statut(nom, entete)
        controler_fraicheur(nom, entete, horizons)
        nouvel_etat[cle] = controler_empreintes(nom, cle, entete, corps, etat)

        if livres is not None:
            numero = entete.get("livre")
            if numero not in livres:
                bloque(nom, f"livre absent du registre : « {numero} » "
                            f"(déclarer le livre dans livres.yaml)")

        for concept in entete.get("concepts") or []:
            concepts_employes.add(concept)
            if concept not in vocabulaire:
                bloque(nom, f"concept absent du vocabulaire : « {concept} »")

        if publier and (entete.get("statut") != "verifie" or entete.get("citable") is False):
            bloque(nom, f"publication refusée : statut « {entete.get('statut')} », "
                        f"citable={entete.get('citable')}")

    # Seconde passe : contrôles transversaux
    for cle, infos in chapitres.items():
        for renvoi in infos["entete"].get("renvois") or []:
            if renvoi not in chapitres:
                bloque(infos["nom"], f"renvoi vers un chapitre inexistant : {renvoi}")
        controler_synthese(infos["nom"], infos["entete"], chapitres)

        statut = infos["entete"].get("statut")
        revision = en_date(infos["entete"].get("revision_de_fond"))
        if statut == "brouillon" and revision and (date.today() - revision).days > 90:
            alerte(infos["nom"], f"en brouillon depuis {(date.today() - revision).days} jours")

    for cle, morceaux in parties.items():
        if 1 not in morceaux:
            for numero, nom in sorted(morceaux.items()):
                bloque(nom, f"partie orpheline : {cle} partie {numero} sans partie 1")

    for terme in sorted(set(vocabulaire) - concepts_employes):
        alerte("vocabulaire.yaml", f"concept déclaré et employé nulle part : « {terme} »")

    registre = charger_arbitrages()

    # Rapport
    largeur = 78
    print("=" * largeur)
    print(f"CONTRÔLE DU CORPUS — {date.today()}")
    print(f"{len(chapitres)} chapitre(s), {len(vocabulaire)} concept(s) au vocabulaire")
    print("=" * largeur)

    for titre, entrees in (("BLOCAGES — la publication est refusée", blocages),
                           ("DÉCISIONS EN ATTENTE — à trancher, pas à ignorer", decisions),
                           ("ALERTES — fraîcheur documentaire", alertes)):
        print(f"\n{titre}  [{len(entrees)}]")
        print("-" * largeur)
        if not entrees:
            print("  (aucune)")
        for fichier, message in entrees:
            print(f"  {fichier}\n      {message}")

    if registre:
        ouverts = []
        for cle, libelle in (("arbitrages", "arbitrage"),
                             ("falsifieurs", "falsifieur"),
                             ("pieces_de_conception_manquantes", "conception")):
            for e in registre.get(cle) or []:
                if e.get("statut") != "arbitre":
                    ouverts.append((libelle, e))
        titre = "ARBITRAGES ET FALSIFIEURS OUVERTS — le corpus ne conclut pas"
        print("")
        print(f"{titre}  [{len(ouverts)}]")
        print("-" * largeur)
        print("  (registre corpus/arbitrages.yaml — les protocoles font foi)")
        for libelle, e in ouverts:
            marque_acq = "!" if e.get("acquisition_bloquante") else " "
            print(f"  {marque_acq} {str(e.get('id')):<16} {str(e.get('statut')):<12} {libelle}")
            print(f"      {e.get('objet')}")
            if e.get("decision"):
                dec = " ".join(str(e["decision"]).split())
                print(f"      DÉCISION ({e.get('maj')}) : {dec[:200]}")
            if e.get("lie_a"):
                print(f"      LIÉ À : {', '.join(e['lie_a'])}")
            if e.get("acquisition_bloquante"):
                acq = " ".join(str(e["acquisition_bloquante"]).split())
                print(f"      ACQUISITION BLOQUANTE : {acq[:140]}")
        arbitres = sum(1 for cle in ("arbitrages", "falsifieurs",
                                     "pieces_de_conception_manquantes")
                       for e in (registre.get(cle) or [])
                       if e.get("statut") == "arbitre")
        print("")
        print(f"  {arbitres} arbitré(s) ; {len(ouverts)} ouvert(s) ou orienté(s).")
        print("  RAPPEL : « décisions en attente » ci-dessus ne porte QUE sur les")
        print("  empreintes éditoriales, et ne dit rien de ces points-ci.")

    if maj_etat and blocages:
        print("\nÉtat non enregistré : des blocages subsistent.")
    elif maj_etat and editorial and fond:
        print("\nÉtat non enregistré : --editorial et --fond s'excluent.")
    elif maj_etat and decisions and not (editorial or fond):
        # Enregistrer l'empreinte ferait disparaître la décision sans qu'elle
        # ait été tranchée. Trois réponses possibles, aucune n'est le silence.
        print("\nÉtat non enregistré : des décisions sont en attente.")
        print("  Le changement touche au sens, à une date ultérieure :")
        print("    mettre à jour revision_de_fond, puis --maj-etat.")
        print("  Le changement touche au sens, le même jour :")
        print("    --maj-etat --fond (revision_de_fond ne peut pas l'enregistrer seule).")
        print("  Le changement est éditorial :")
        print("    --maj-etat --editorial.")
    elif maj_etat:
        for cle in nouvel_etat:
            if fond:
                nouvel_etat[cle]["qualification"] = f"fond, déclarée le {date.today()}"
            elif editorial:
                nouvel_etat[cle]["qualification"] = f"editorial, déclaré le {date.today()}"
        ETAT.write_text(json.dumps(nouvel_etat, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nÉtat enregistré dans {ETAT.name}")
        if decisions and fond:
            print(f"  {len(decisions)} changement(s) déclaré(s) substantiels.")
        elif decisions and editorial:
            print(f"  {len(decisions)} changement(s) déclaré(s) éditoriaux.")

    print()
    if blocages:
        print(f"ÉCHEC — {len(blocages)} blocage(s). Rien n'est publiable en l'état.")
        return 1
    print("Contrôle structurel passé.")
    if decisions:
        print(f"{len(decisions)} décision(s) en attente : à traiter avant publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
