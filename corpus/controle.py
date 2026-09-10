#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contrôle du corpus Debunk'Onomy.

Applique les règles de convention.md (révision 12).
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
    python controle.py --maj-etat --purger-orphelins
                                       # retire les entrées d'état sans chapitre
    python controle.py --maj-etat --initialiser-tardif
                                       # qualifie « initialisation tardive » TOUTES
                                       # les entrées absentes — après audit seulement
    python controle.py --maj-etat --initialiser-tardif=L1.C31,L11.C30
                                       # idem, pour ces seules entrées absentes

L'enregistrement de l'état CONSERVE les qualifications existantes (réparation
du 2026-09-10, protocoles/migration-etat-lecture.md § 9) : une entrée
inchangée, ou dont seules les métadonnées ont changé, garde la sienne ;
--editorial et --fond ne qualifient que les entrées dont l'empreinte éditoriale
a changé à revision_de_fond inchangée ; une entrée dont revision_de_fond a été
déplacée est qualifiée « fond » d'après cette date, seule l'inscription étant
datée du jour ; une entrée nouvelle est qualifiée « initialisation », neutre —
« tardive » SEULEMENT sur demande explicite, par --initialiser-tardif, après
audit : une date de fond antérieure ne prouve pas que le chapitre existait lors
de l'état précédent, et rien n'est déduit d'une date. L'option ne vise que des
entrées absentes, ne modifie aucune entrée enregistrée, et est refusée dès que
sa portée serait ambiguë. Aucune qualification n'est jamais supprimée sans
demande explicite : l'enregistrement est refusé plutôt que d'en perdre une.

ÉTAT DE LECTURE DES SOURCES (révision 12, migration etat_lecture) : chaque
source primaire porte etat_lecture ∈ {candidate, ouverte, a_requalifier}.
E-L1 date_verification sur une source non ouverte ; E-L2 source ouverte sans
date ; E-L3 etat_lecture absent ou inconnu ; E-L4 chapitre verifie portant une
source non ouverte ; E-L5 génération publique (--publier) d'un chapitre portant
une source non ouverte ; E-L6 a_requalifier sur une occurrence absente du
manifeste corpus/manifeste-etat-lecture.json ou d'empreinte bibliographique
différente ; E-M1 manifeste absent, illisible ou incohérent. Bilan agrégé par
chapitre : A-L1 sources candidate, A-L2 sources à requalifier et leur
ancienneté depuis la date de migration, A-L3 entrées du manifeste sans
occurrence.

Dépendance : PyYAML 6.0.3 (corpus/requirements.txt ; voie hors ligne dans
corpus/hors-ligne/ ; test : python corpus/test_environnement_propre.py)
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
        "  module     : " + (getattr(yaml, "__file__", None)
                             or "(sans fichier)")
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
MANIFESTE = RACINE / "manifeste-etat-lecture.json"

# --- Schéma, d'après la table des champs de la convention -------------------

CHAMPS_OBLIGATOIRES = {
    "chapitre", "titre", "livre", "langue", "licence", "type", "statut",
    "revision_de_fond", "autorite", "citable", "regime", "resume",
    "sources_primaires", "verifications_en_attente", "concepts", "renvois",
}
CHAMPS_CONDITIONNELS = {"partie", "chapitres_sources", "verifiee_le"}
CHAMPS_CONNUS = CHAMPS_OBLIGATOIRES | CHAMPS_CONDITIONNELS

CHAMPS_SOURCE_OBLIGATOIRES = {"ref", "nature", "reference", "etat_lecture"}
CHAMPS_SOURCE_CONNUS = CHAMPS_SOURCE_OBLIGATOIRES | {"url", "horizon", "motif_horizon",
                                                     "date_verification"}
ETATS_LECTURE = ["candidate", "ouverte", "a_requalifier"]
# L'empreinte bibliographique d'une occurrence porte sur ses seules métadonnées
# d'origine : ni etat_lecture, ni date_verification, ni ref (déjà dans
# l'identifiant chapitre/ref), ni horizon / motif_horizon (données de contrôle).
CHAMPS_EMPREINTE_BIBLIO = ("nature", "reference", "url")
# Schéma fermé du manifeste des occurrences historiques (E-M1).
SCHEMA_MANIFESTE = "manifeste-etat-lecture/1"
CHAMPS_MIGRATION = ("date", "commit_source", "revision_convention", "python", "pyyaml",
                    "nombre_occurrences", "regle_empreinte")
REVISION_MANIFESTE = 12
FILES_MANIFESTE = {"A": "orientation vers ouverte", "B": "traces contradictoires",
                   "C": "orientation vers candidate", "D": "sans orientation"}
CODES_TRACES = {"T1", "T2", "T3", "T4", "T5", "T6", "T7"}
RE_SHA_COMPLET = re.compile(r"^[0-9a-f]{40}$")
RE_HEX64 = re.compile(r"^[0-9a-f]{64}$")
CHAMPS_MANIFESTE = {"schema", "migration", "occurrences"}
CHAMPS_OCCURRENCE = {"id", "chapitre", "ref", "empreinte_bibliographique", "ancienne_date_verification",
                     "date_migration", "traces", "file", "orientation", "etat_initial"}
CHAMPS_TRACE = {"code", "emplacement", "appui"}


def chaine_valide(valeur, sans=""):
    """Une chaîne non vide, sans aucun des caractères interdits."""
    return isinstance(valeur, str) and valeur.strip() != "" and not any(c in valeur for c in sans)


def orienter_traces(codes):
    """La file d'examen que des traces imposent (protocole § 3.3) : forte =
    T1, T2 ou T7 ; démenti = T3."""
    fort = codes & {"T1", "T2", "T7"}
    if fort and "T3" in codes:
        return "B"
    if fort:
        return "A"
    if "T3" in codes:
        return "C"
    return "D"

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

blocages, decisions, alertes, bilan_lecture = [], [], [], []


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


def empreinte_bibliographique(src):
    """sha256 complet des métadonnées bibliographiques d'origine d'une
    occurrence — la même fonction sert à la migration, au manifeste et au
    contrôle (E-L6) ; deux règles donneraient deux empreintes."""
    base = {k: normalise(str(src[k])) for k in CHAMPS_EMPREINTE_BIBLIO
            if k in src and src[k] is not None}
    canon = json.dumps(base, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


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
            if statut != "arbitre" and tp == "auteur" \
                    and not e.get("chapitres"):
                alerte("arbitrages.yaml",
                       f"{ident} : oriente par l'auteur sans renvoi aux "
                       f"chapitres ou le raisonnement vit")
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


def charger_manifeste():
    """Manifeste des occurrences historiques — la seule autorisation possible
    de l'état a_requalifier. Son schéma est FERMÉ : tout écart est une faute
    E-M1, le manifeste est alors inutilisable, E-L6 n'est pas évaluable, les
    autres contrôles s'exécutent et la publication est refusée. Retourne
    {"date", "occurrences"} ou None."""
    nom = MANIFESTE.name
    if not MANIFESTE.exists():
        bloque(nom, "E-M1 — manifeste absent : E-L6 n'est pas évaluable")
        return None
    try:
        contenu = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    except Exception as erreur:
        bloque(nom, f"E-M1 — manifeste illisible : {erreur}")
        return None
    if not isinstance(contenu, dict):
        bloque(nom, "E-M1 — manifeste mal formé : objet attendu")
        return None
    fautes = []

    def faute(message):
        fautes.append(message)
        bloque(nom, "E-M1 — " + message)

    for champ in sorted(set(contenu) - CHAMPS_MANIFESTE):
        faute(f"champ inconnu au niveau supérieur : {champ}")
    if contenu.get("schema") != SCHEMA_MANIFESTE:
        faute(f"schema « {contenu.get('schema')} », attendu {SCHEMA_MANIFESTE}")
    migration = contenu.get("migration")
    occurrences = contenu.get("occurrences")
    if not isinstance(migration, dict) or not isinstance(occurrences, list):
        faute("« migration » (objet) et « occurrences » (liste) attendus")
        return None
    for champ in CHAMPS_MIGRATION:
        if champ not in migration:
            faute(f"champ de migration absent : {champ}")
    for champ in sorted(set(migration) - set(CHAMPS_MIGRATION)):
        faute(f"champ de migration inconnu : {champ}")
    for champ in ("python", "pyyaml", "regle_empreinte"):
        if champ in migration and not chaine_valide(migration[champ]):
            faute(f"{champ} : chaîne non vide attendue")
    commit = str(migration.get("commit_source", ""))
    if not RE_SHA_COMPLET.match(commit):
        faute(f"commit_source « {commit} » n'est pas un SHA complet de 40 hexadécimaux")
    if migration.get("revision_convention") != REVISION_MANIFESTE:
        faute(f"revision_convention « {migration.get('revision_convention')} », attendue {REVISION_MANIFESTE}")
    date_migration = migration.get("date")
    if not en_date(date_migration):
        faute(f"date de migration absente ou invalide : {date_migration!r}")
    nombre = migration.get("nombre_occurrences")
    if not isinstance(nombre, int) or nombre != len(occurrences):
        faute(f"nombre déclaré {nombre!r} ≠ {len(occurrences)} occurrence(s) inscrite(s)")
    inscrites, paires = {}, set()
    for rang, o in enumerate(occurrences, 1):
        if not isinstance(o, dict) or not o.get("id"):
            faute(f"occurrence {rang} mal formée")
            continue
        ident = str(o["id"])
        for champ in sorted(CHAMPS_OCCURRENCE - set(o)):
            faute(f"{ident} : champ obligatoire absent : {champ}")
        for champ in sorted(set(o) - CHAMPS_OCCURRENCE):
            faute(f"{ident} : champ inconnu : {champ}")
        if not chaine_valide(o.get("chapitre"), "/ \t\n") or not chaine_valide(o.get("ref"), "/ \t\n"):
            faute(f"{ident} : chapitre ou ref n'est pas une chaîne valide")
        if ident != f"{o.get('chapitre')}/{o.get('ref')}":
            faute(f"{ident} : identifiant incohérent avec chapitre/ref « {o.get('chapitre')}/{o.get('ref')} »")
        if ident in inscrites:
            faute(f"identifiant en doublon dans le manifeste : {ident}")
        paire = (str(o.get("chapitre")), str(o.get("ref")))
        if paire in paires:
            faute(f"référence dupliquée dans le manifeste : {paire[0]}/{paire[1]}")
        paires.add(paire)
        if o.get("etat_initial") != "a_requalifier":
            faute(f"{ident} : etat_initial « {o.get('etat_initial')} », seul a_requalifier est admis")
        if not RE_HEX64.match(str(o.get("empreinte_bibliographique", ""))):
            faute(f"{ident} : empreinte bibliographique mal formée — 64 hexadécimaux attendus")
        if not en_date(o.get("ancienne_date_verification")):
            faute(f"{ident} : ancienne_date_verification invalide « {o.get('ancienne_date_verification')} »")
        if not en_date(o.get("date_migration")) or str(o.get("date_migration")) != str(date_migration):
            faute(f"{ident} : date_migration absente, invalide ou différente de l'en-tête")
        if o.get("file") not in FILES_MANIFESTE:
            faute(f"{ident} : file « {o.get('file')} » hors de A, B, C, D")
        traces = o.get("traces")
        if not isinstance(traces, list) or any(
                not isinstance(t, dict) or set(t) != CHAMPS_TRACE or t.get("code") not in CODES_TRACES
                or not chaine_valide(t.get("emplacement")) or not chaine_valide(t.get("appui"))
                for t in traces):
            faute(f"{ident} : traces mal formées — liste d'objets à trois champs code (T1 à T7), "
                  f"emplacement et appui attendue")
        else:
            attendu = orienter_traces({t["code"] for t in traces})
            if o.get("file") != attendu or o.get("orientation") != FILES_MANIFESTE[attendu]:
                faute(f"{ident} : file « {o.get('file')} » et orientation « {o.get('orientation')} » "
                      f"incohérentes avec les traces — attendu {attendu}, {FILES_MANIFESTE[attendu]}")
        inscrites[ident] = o
    if fautes:
        return None
    return {"date": en_date(date_migration), "occurrences": inscrites}


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


def controler_sources(nom, cle, entete, manifeste):
    """Champs, nature et état de lecture des sources — E-L1, E-L2, E-L3, E-L6.
    Retourne (candidates, a_requalifier, total) pour le bilan agrégé."""
    candidates, requalifier, total = 0, 0, 0
    refs_vus = set()
    for src in entete.get("sources_primaires") or []:
        if not isinstance(src, dict):
            bloque(nom, "source primaire mal formée")
            continue
        total += 1
        ref = src.get("ref", "?")
        # Deux occurrences ne peuvent pas partager un identifiant chapitre/ref :
        # le manifeste, l'état de lecture et les citations [Sn] en dépendent.
        if ref in refs_vus:
            bloque(nom, f"référence dupliquée dans le chapitre : {ref}")
        refs_vus.add(ref)
        for champ in sorted(CHAMPS_SOURCE_OBLIGATOIRES - set(src)):
            bloque(nom, f"source {ref} : champ obligatoire absent « {champ} »"
                        + (" (E-L3)" if champ == "etat_lecture" else ""))
        for champ in sorted(set(src) - CHAMPS_SOURCE_CONNUS):
            bloque(nom, f"source {ref} : champ inconnu « {champ} »")
        if src.get("nature") and src["nature"] not in NATURES:
            bloque(nom, f"source {ref} : nature « {src['nature']} » inconnue")
        lecture = src.get("etat_lecture")
        if "etat_lecture" in src and lecture not in ETATS_LECTURE:
            bloque(nom, f"source {ref} : E-L3 — etat_lecture « {lecture} » hors des valeurs "
                        f"admises : {', '.join(ETATS_LECTURE)}")
        if "date_verification" in src:
            if not en_date(src["date_verification"]):
                bloque(nom, f"source {ref} : date_verification mal formée")
            if lecture != "ouverte":
                bloque(nom, f"source {ref} : E-L1 — date_verification présente sur une source "
                            f"« {lecture} », qui n'est pas ouverte")
        elif lecture == "ouverte":
            bloque(nom, f"source {ref} : E-L2 — source ouverte sans date_verification")
        if "horizon" in src and not src.get("motif_horizon"):
            bloque(nom, f"source {ref} : dérogation d'horizon sans motif_horizon")
        if lecture == "candidate":
            candidates += 1
        elif lecture == "a_requalifier":
            requalifier += 1
            if manifeste is not None:
                ident = f"{cle}/{ref}"
                inscrite = manifeste["occurrences"].get(ident)
                if inscrite is None:
                    bloque(nom, f"source {ref} : E-L6 — a_requalifier sur une occurrence absente du "
                                f"manifeste ({ident}) ; une source ajoutée après la migration est "
                                f"candidate ou ouverte")
                elif inscrite.get("empreinte_bibliographique") != empreinte_bibliographique(src):
                    bloque(nom, f"source {ref} : E-L6 — empreinte bibliographique différente de celle "
                                f"du manifeste ({ident}) ; une référence remplacée ou corrigée "
                                f"n'hérite pas de l'état historique")
    return candidates, requalifier, total


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
        non_ouvertes = [str(s.get("ref", "?")) for s in (entete.get("sources_primaires") or [])
                        if isinstance(s, dict) and s.get("etat_lecture") != "ouverte"]
        if non_ouvertes:
            bloque(nom, f"E-L4 — statut « verifie » avec {len(non_ouvertes)} source(s) non "
                        f"ouverte(s) : {', '.join(non_ouvertes)}")
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


# --- État enregistré : construction conservatrice ---------------------------
# Réparation du 2026-09-10. L'ancien enregistrement reconstruisait le fichier
# entier depuis les empreintes recalculées et ne posait de qualification que
# par option globale : une exécution effaçait toutes les qualifications
# existantes, ou les remplaçait toutes par celle du jour. Ici l'état PART DU
# FICHIER EXISTANT, reporte chaque qualification, ne touche qu'aux entrées
# visées et nomme ce qu'il initialise.

QUALIF_INIT = "initialisation, enregistrée le {jour}"
QUALIF_INIT_TARDIVE = ("initialisation tardive, état antérieur non enregistré, "
                       "enregistrée le {jour}")


def construire_etat(ancien, calcule, editorial=False, fond=False, purger=False,
                    tardifs=None, jour=None):
    """Retourne (etat_final, bilan, explicites). N'écrit rien.

    ancien     : contenu actuel de .etat-corpus.json
    calcule    : {cle: {editoriale, metadonnees, revision_de_fond}} recalculé
    tardifs    : None — aucune initialisation tardive ; True — toutes les
                 entrées absentes ; ensemble de clés — ces entrées absentes
                 seulement (option --initialiser-tardif, après audit)
    explicites : clés dont la qualification change ou disparaît par une
                 règle ou une option, et non par accident — l'invariant de
                 conservation les exempte, et elles seules.
    """
    jour = str(jour or date.today())
    final, explicites = {}, set()
    bilan = {"conservees": 0, "metadonnees": 0, "fond_declare": 0,
             "requalifiees": 0, "initialisees": 0, "tardives": 0,
             "orphelines_conservees": 0, "orphelines_purgees": 0}
    for cle, neuf in calcule.items():
        vieux = ancien.get(cle)
        entree = dict(neuf)
        if vieux is None:
            # P4, P5 : une entrée nouvelle est nommée pour ce qu'elle est —
            # jamais qualifiée d'une décision éditoriale qui n'a pas été prise.
            # « Tardive » n'est JAMAIS déduit d'une date : une revision_de_fond
            # antérieure ne prouve pas que le chapitre existait lors de l'état
            # précédent — un chapitre nouveau peut reprendre un contenu révisé
            # auparavant. Seule l'option explicite --initialiser-tardif le dit.
            tardive = tardifs is True or (isinstance(tardifs, set) and cle in tardifs)
            entree["qualification"] = (QUALIF_INIT_TARDIVE if tardive
                                       else QUALIF_INIT).format(jour=jour)
            bilan["tardives" if tardive else "initialisees"] += 1
        elif vieux.get("editoriale") == neuf["editoriale"]:
            # P1, P2 : corps et résumé inchangés — la qualification antérieure
            # est reportée telle quelle, que les métadonnées aient bougé ou non.
            if vieux.get("qualification"):
                entree["qualification"] = vieux["qualification"]
            if (vieux.get("metadonnees") == neuf["metadonnees"]
                    and str(vieux.get("revision_de_fond")) == str(neuf["revision_de_fond"])):
                bilan["conservees"] += 1
            else:
                bilan["metadonnees"] += 1
        elif str(vieux.get("revision_de_fond")) != str(neuf["revision_de_fond"]):
            # Règle dérivée : le corps a changé ET revision_de_fond a été
            # déplacée — la convention réserve ce déplacement au changement de
            # sens, le changement de fond est donc déjà déclaré par le
            # chapitre. Sa date est celle du chapitre ; seule l'inscription
            # dans l'état est datée du jour, et « tardivement » le dit.
            rev = str(neuf["revision_de_fond"])
            quand = ("enregistrée tardivement le " + jour if rev < jour
                     else "enregistrée le " + jour)
            entree["qualification"] = f"fond, revision_de_fond du {rev}, {quand}"
            explicites.add(cle)
            bilan["fond_declare"] += 1
        else:
            # P3 : corps changé à date inchangée — c'est une décision en
            # attente, et seule une option explicite la qualifie, elle seule.
            if fond:
                entree["qualification"] = f"fond, déclarée le {jour}"
                explicites.add(cle)
                bilan["requalifiees"] += 1
            elif editorial:
                entree["qualification"] = f"editorial, déclaré le {jour}"
                explicites.add(cle)
                bilan["requalifiees"] += 1
            elif vieux.get("qualification"):
                entree["qualification"] = vieux["qualification"]
        final[cle] = entree
    # P7, P9 : une entrée sans chapitre n'est jamais supprimée en silence.
    for cle, vieux in ancien.items():
        if cle in calcule:
            continue
        if purger:
            explicites.add(cle)
            bilan["orphelines_purgees"] += 1
        else:
            final[cle] = dict(vieux)
            bilan["orphelines_conservees"] += 1
    return final, bilan, explicites


def qualifications_perdues(ancien, final, explicites=()):
    """Invariant de conservation (protocole § 9.3, invariant Q) : les
    qualifications d'avant se retrouvent après, à l'identique, sauf sur les
    entrées explicitement requalifiées ou purgées."""
    perdues = []
    for cle, vieux in ancien.items():
        q = vieux.get("qualification")
        if not q or cle in explicites:
            continue
        if cle not in final:
            perdues.append((cle, "entrée disparue"))
        elif final[cle].get("qualification") != q:
            perdues.append((cle, "qualification modifiée sans demande"))
    return perdues


# --- Programme principal ----------------------------------------------------

def main():
    publier = "--publier" in sys.argv
    maj_etat = "--maj-etat" in sys.argv
    editorial = "--editorial" in sys.argv
    fond = "--fond" in sys.argv
    purger = "--purger-orphelins" in sys.argv
    refus_etat = False
    # --initialiser-tardif : True = toutes les entrées absentes ; ensemble = ces
    # entrées absentes seulement. Sa portée est vérifiée avant toute écriture.
    tardifs = None
    repetitions = [arg for arg in sys.argv[1:]
                   if arg == "--initialiser-tardif" or arg.startswith("--initialiser-tardif=")]
    for arg in repetitions:
        if arg == "--initialiser-tardif":
            tardifs = True
        else:
            tardifs = {x.strip() for x in arg.split("=", 1)[1].split(",") if x.strip()}

    vocabulaire = charger_vocabulaire()
    livres = charger_livres()
    horizons = charger_horizons()
    etat = charger_etat()
    manifeste = charger_manifeste()
    nouvel_etat = {}
    lecture, occurrences_vues = {}, set()

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

        lecture[cle] = controler_sources(nom, cle, entete, manifeste) + (nom,)
        for src in entete.get("sources_primaires") or []:
            if isinstance(src, dict):
                occurrences_vues.add(f"{cle}/{src.get('ref')}")
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

        # E-L5 : la génération publique exclut mécaniquement toute source non ouverte.
        if publier:
            non_ouvertes = [str(s.get("ref", "?")) for s in (entete.get("sources_primaires") or [])
                            if isinstance(s, dict) and s.get("etat_lecture") != "ouverte"]
            if non_ouvertes:
                bloque(nom, f"E-L5 — génération publique refusée : {len(non_ouvertes)} source(s) "
                            f"non ouverte(s) : {', '.join(non_ouvertes)}")

        # P8 (réparation du 2026-09-10) : un marqueur d'état sans état
        # enregistré ne protège rien — rien ne se publie sans entrée d'état.
        if publier and (entete.get("statut") == "verifie" or entete.get("citable") is True) \
                and cle not in etat:
            bloque(nom, "publication refusée : aucun état enregistré pour ce chapitre "
                        "— l'enregistrer d'abord avec --maj-etat")

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

    # P6, P7 (réparation du 2026-09-10) : l'état enregistré est surveillé —
    # un chapitre sans entrée et une entrée sans chapitre apparaissent tous
    # deux au diagnostic, avec leur compte en tête de rapport.
    absents = sorted(cle for cle in chapitres if cle not in etat)
    orphelins = sorted(cle for cle in etat if cle not in chapitres)

    # Rapport
    largeur = 78
    print("=" * largeur)
    print(f"CONTRÔLE DU CORPUS — {date.today()}")
    print(f"{len(chapitres)} chapitre(s), {len(vocabulaire)} concept(s) au vocabulaire, "
          f"{len(absents)} sans état enregistré, {len(orphelins)} entrée(s) d'état orpheline(s)")
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

    print(f"\nÉTAT ENREGISTRÉ — écarts  [{len(absents) + len(orphelins)}]")
    print("-" * largeur)
    if not absents and not orphelins:
        print("  (aucun)")
    for cle in absents:
        print(f"  {chapitres[cle]['nom']}\n      état non enregistré — {cle} n'a aucune entrée dans {ETAT.name}")
    for cle in orphelins:
        print(f"  {ETAT.name}\n      entrée d'état sans chapitre correspondant : {cle}")

    # A-L1, A-L2, A-L3 : bilan AGRÉGÉ par chapitre — jamais une alerte par source.
    sans_occurrence = {}
    if manifeste is not None:
        for ident in sorted(set(manifeste["occurrences"]) - occurrences_vues):
            sans_occurrence.setdefault(ident.split("/")[0], []).append(ident)
    anciennete = (date.today() - manifeste["date"]).days if manifeste is not None else None
    total_cand = sum(v[0] for v in lecture.values())
    total_requal = sum(v[1] for v in lecture.values())
    total_src = sum(v[2] for v in lecture.values())
    concernes = sorted(c for c in lecture if lecture[c][0] or lecture[c][1] or c in sans_occurrence)
    print(f"\nÉTAT DE LECTURE — bilan agrégé par chapitre  [{len(concernes)}]")
    print("-" * largeur)
    print(f"  {total_cand} source(s) candidate(s), {total_requal} à requalifier, "
          f"{sum(len(v) for v in sans_occurrence.values())} entrée(s) du manifeste sans occurrence, "
          f"sur {total_src} source(s)")
    for c in concernes:
        cand, requal, total, nom_c = lecture[c]
        lignes = []
        if cand:
            lignes.append(f"A-L1 : {cand} candidate(s) sur {total}")
        if requal:
            lignes.append(f"A-L2 : {requal} à requalifier sur {total}, depuis {anciennete} j "
                          f"(migration du {manifeste['date']})")
        if c in sans_occurrence:
            lignes.append(f"A-L3 : {len(sans_occurrence[c])} entrée(s) du manifeste sans occurrence : "
                          + ", ".join(sans_occurrence[c]))
        print(f"  {nom_c}\n      " + "\n      ".join(lignes))
    for c in sorted(sans_occurrence):
        if c not in lecture:
            print(f"  {MANIFESTE.name}\n      A-L3 : chapitre {c} disparu, "
                  f"{len(sans_occurrence[c])} entrée(s) : " + ", ".join(sans_occurrence[c]))

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
        # QUI A TRANCHE : un arbitrage de l'auteur et une consequence tiree
        # par le corpus ne sont pas la meme chose, et les confondre grossit le
        # nombre de decisions prises. Ventilation exigee par l'auteur le
        # 2026-09-09.
        par_auteur = sum(1 for cle in ("arbitrages", "falsifieurs",
                                       "pieces_de_conception_manquantes")
                         for e in (registre.get(cle) or [])
                         if e.get("statut") == "arbitre"
                         and e.get("tranche_par") == "auteur")
        par_corpus = arbitres - par_auteur
        print("")
        print(f"  {arbitres} arbitré(s) — dont {par_auteur} par l'auteur "
              f"et {par_corpus} par le corpus, en conséquence d'une décision "
              f"antérieure ; {len(ouverts)} ouvert(s) ou orienté(s).")
        print("  RAPPEL : « décisions en attente » ci-dessus ne porte QUE sur les")
        print("  empreintes éditoriales, et ne dit rien de ces points-ci.")

    # La portée de --initialiser-tardif est vérifiée AVANT toute écriture :
    # ambiguë, elle est refusée, et rien n'est écrit.
    ambigu = None
    if tardifs is not None:
        if len(repetitions) > 1:
            # Deux occurrences ne s'écrasent pas en silence : la portée est refusée.
            ambigu = "--initialiser-tardif répété (" + " ".join(repetitions) + \
                     "), la dernière occurrence n'écrase pas la première"
        elif not maj_etat:
            ambigu = "--initialiser-tardif exige --maj-etat"
        elif tardifs is True and not absents:
            ambigu = "aucune entrée absente : --initialiser-tardif n'a rien à initialiser"
        elif isinstance(tardifs, set):
            deja = sorted(c for c in tardifs if c in etat)
            inconnues = sorted(c for c in tardifs if c not in chapitres)
            if not tardifs:
                ambigu = "--initialiser-tardif= sans aucune clé"
            elif deja:
                ambigu = "déjà enregistrée(s), non modifiable(s) par cette option : " + ", ".join(deja)
            elif inconnues:
                ambigu = "chapitre(s) inconnu(s) : " + ", ".join(inconnues)

    if ambigu:
        refus_etat = True
        print(f"\nÉtat non enregistré : portée de --initialiser-tardif ambiguë — {ambigu}.")
    elif maj_etat and blocages:
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
        final, bilan, explicites = construire_etat(etat, nouvel_etat, editorial, fond, purger, tardifs)
        perdues = qualifications_perdues(etat, final, explicites)
        if perdues:
            # P9 : jamais de perte silencieuse — on refuse d'écrire.
            refus_etat = True
            print(f"\nÉtat non enregistré : {len(perdues)} qualification(s) seraient perdues.")
            for cle, motif in perdues:
                print(f"  {cle} : {motif}")
        else:
            ETAT.write_text(json.dumps(final, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"\nÉtat enregistré dans {ETAT.name} — {len(final)} entrée(s).")
            print(f"  {bilan['conservees'] + bilan['metadonnees']} qualification(s) conservée(s), "
                  f"dont {bilan['metadonnees']} à métadonnées modifiées seules")
            print(f"  {bilan['fond_declare']} changement(s) de fond déclaré(s) par revision_de_fond")
            print(f"  {bilan['requalifiees']} requalifiée(s) par option")
            print(f"  {bilan['initialisees']} initialisation(s), {bilan['tardives']} tardive(s)")
            if bilan["tardives"]:
                tard = sorted(c for c in final if c not in etat and
                              str(final[c].get("qualification", "")).startswith("initialisation tardive"))
                print("  tardives, sur demande explicite : " + ", ".join(tard[:12])
                      + (" …" if len(tard) > 12 else ""))
            if bilan["orphelines_conservees"] or bilan["orphelines_purgees"]:
                print(f"  {bilan['orphelines_conservees']} entrée(s) orpheline(s) conservée(s), "
                      f"{bilan['orphelines_purgees']} purgée(s)")

    print()
    if blocages:
        print(f"ÉCHEC — {len(blocages)} blocage(s). Rien n'est publiable en l'état.")
        return 1
    if refus_etat:
        print("ÉCHEC — état non enregistré : voir le motif ci-dessus.")
        return 1
    print("Contrôle structurel passé.")
    if decisions:
        print(f"{len(decisions)} décision(s) en attente : à traiter avant publication.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
