#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vérification des exemplaires cités par les entrées de source.

OUTIL SÉPARÉ ET FACULTATIF, hors du chemin de publication. `controle.py` ne
l'appelle pas et reste seul autorité : l'échec de ce script ne bloque aucune
publication. Motif du choix (décision de l'auteur du 2026-09-18) : les
exemplaires vivent dans un dossier local, hors du dépôt ; un contrôle qui en
dépendrait échouerait chez tout autre porteur du dépôt, et `controle.py` doit
rester reproductible par quiconque le clone.

CE QU'IL VÉRIFIE. Les entrées de source inscrivent l'empreinte SHA-256 de
l'exemplaire qu'elles déclarent avoir lu — « OUVERT PAR TÉLÉCHARGEMENT DIRECT »,
« OUVERTE PAR VERSEMENT ». Ces empreintes ne servaient à rien de mécanique. Ce
script les rend opérantes, et répond à trois questions que le dépôt ne savait
pas poser :

    l'exemplaire déclaré lu est-il encore là ?
    est-ce le même, octet pour octet ?
    une entrée nomme-t-elle une pièce sous un nom qu'elle n'a pas ?

Il ne lit que les en-têtes — `reference` et `verifications_en_attente` — et
jamais le corps. Il n'ajoute aucun champ au schéma et ne touche ni à la
convention ni à `controle.py`.

CE QU'IL NE VÉRIFIE PAS. Que la pièce porte ce que l'entrée lui fait dire.
Établir que l'exemplaire est le bon fichier et établir qu'il porte la citation
sont deux questions distinctes ; seule la première est traitée ici.

RÈGLE D'APPARIEMENT, ET ELLE EST LE POINT DÉLICAT. Une entrée cite couramment
plusieurs pièces : l'exemplaire ouvert, avec son empreinte, ET des exemplaires
écartés, sans la leur — une édition en fraktur illisible, un substitut refusé,
un prolongement non lu. **Une empreinte appartient à la pièce qu'elle suit,
jamais à l'entrée.** Un contrôle qui attache l'unique empreinte d'une entrée à
tous les chemins qu'elle cite fabrique des discordances qui n'existent pas
(constaté le 2026-09-18 : quatre faux défauts sur L1.C10 et L1.C22). L'empreinte
n'est donc retenue que si elle suit le chemin dans la même fenêtre de texte.

Usage :
    python corpus/verifier-exemplaires.py --dossier <racine>
    python corpus/verifier-exemplaires.py --dossier <racine> --detail
    python corpus/verifier-exemplaires.py --dossier <racine> --chapitre L1.C08
    python corpus/verifier-exemplaires.py --dossier <racine> --strict

La racine peut aussi venir de la variable d'environnement
DEBUNKONOMY_EXEMPLAIRES. Les chemins cités lui sont relatifs.

    --detail     liste toutes les occurrences, et non les seules anomalies
    --chapitre   restreint à un chapitre (répétable)
    --strict     fait échouer aussi sur les signalements (pièce renommée)

Codes de sortie :
    0  tout concorde — signalements possibles, sans --strict
    1  au moins une pièce absente, discordante ou mal nommée
    2  racine des exemplaires non fournie ou introuvable
       — ce n'est PAS un défaut du corpus
    3  dépendance manquante

Dépendance : PyYAML 6.0.3 (corpus/requirements.txt)
"""

import hashlib
import os
import re
import sys
from pathlib import Path

# Sortie UTF-8 sous Windows (cmd, PowerShell) : sans quoi les accents des
# messages ressortent en mojibake.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("PyYAML manquant. Installer avec : pip install pyyaml", file=sys.stderr)
    print("Interpreteur utilise : " + sys.executable, file=sys.stderr)
    sys.exit(3)

if not hasattr(yaml, "safe_load"):
    print("PyYAML mal resolu : le module importe n'expose pas safe_load.", file=sys.stderr)
    print("  module     : " + (getattr(yaml, "__file__", None) or "(sans fichier)"), file=sys.stderr)
    print("  interprete : " + sys.executable, file=sys.stderr)
    sys.exit(3)

RACINE = Path(__file__).resolve().parent

# Un chemin d'exemplaire s'ouvre sur la date de la séance : AAAA-MM-JJ/…
# Le préfixe éventuel (« dossier Documents/Codex/ ») est ignoré, la racine
# étant fournie en argument.
RE_CHEMIN = re.compile(r"20\d{2}-\d{2}-\d{2}/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*")
RE_EMPREINTE = re.compile(r"SHA-256\s+([0-9A-Fa-f]{64})")

# Fenêtre d'appariement : l'empreinte doit suivre le chemin d'assez près pour
# lui appartenir. Les entrées écrivent « (chemin, 56 pages, SHA-256 …) » ;
# 120 caractères couvrent la pagination et la ponctuation intercalées sans
# atteindre la pièce suivante.
FENETRE = 120

_cache = {}


def empreinte(chemin):
    """SHA-256 majuscule d'un fichier, calculé une seule fois par chemin."""
    cle = str(chemin)
    if cle not in _cache:
        h = hashlib.sha256()
        with open(chemin, "rb") as f:
            for bloc in iter(lambda: f.read(1 << 20), b""):
                h.update(bloc)
        _cache[cle] = h.hexdigest().upper()
    return _cache[cle]


def paires(texte):
    """(chemin cité, empreinte inscrite ou None), dans l'ordre du texte."""
    trouvees = []
    for m in RE_CHEMIN.finditer(texte):
        suite = texte[m.end():m.end() + FENETRE]
        e = RE_EMPREINTE.search(suite)
        trouvees.append((m.group(0), e.group(1).upper() if e else None))
    return trouvees


def porteur(dossier, cherchee):
    """Nom du fichier de ce dossier qui porte l'empreinte cherchée, ou None.

    Sert à distinguer une pièce PERDUE d'une pièce RENOMMÉE : l'entrée nomme
    couramment le fichier de l'éditeur quand le dossier en garde une copie
    sous un autre nom. L'empreinte tranche ce que le nom laisse ambigu.
    Recherche non récursive, et seulement en cas d'anomalie.
    """
    if not dossier.is_dir():
        return None
    try:
        noms = sorted(os.listdir(dossier))
    except OSError:
        return None
    for nom in noms:
        p = dossier / nom
        if p.is_file():
            try:
                if empreinte(p) == cherchee:
                    return nom
            except OSError:
                continue
    return None


def examiner(racine, chemin_cite, inscrite):
    """(verdict, précision) pour un couple (chemin, empreinte)."""
    cible = racine / chemin_cite

    if inscrite is None:
        if cible.is_file():
            return "PRESENTE", "sans empreinte inscrite — présence seule vérifiée"
        if cible.is_dir():
            return "PRESENTE", "dossier, sans empreinte inscrite"
        return "ABSENTE", "sans empreinte inscrite — rien à cette adresse"

    if cible.is_file():
        reelle = empreinte(cible)
        if reelle == inscrite:
            return "CONCORDE", ""
        autre = porteur(cible.parent, inscrite)
        if autre:
            return "DEPLACEE", (f"l'entrée nomme « {cible.name} », mais l'empreinte "
                                f"inscrite est celle de « {autre} » dans le même dossier")
        return "DISCORDANTE", (f"inscrite {inscrite}\n           réelle   {reelle}")

    # Le chemin ne désigne pas un fichier : dossier cité, ou pièce renommée.
    dossier = cible if cible.is_dir() else cible.parent
    autre = porteur(dossier, inscrite)
    if autre:
        ou = chemin_cite if cible.is_dir() else str(Path(chemin_cite).parent).replace("\\", "/")
        return "RENOMMEE", (f"l'empreinte inscrite est celle de « {autre} », "
                            f"dans {ou}/")
    if cible.is_dir():
        return "ABSENTE", "dossier présent, mais aucune pièce n'y porte l'empreinte inscrite"
    return "ABSENTE", "rien à cette adresse, et aucune pièce du dossier ne porte l'empreinte"


def relever(chapitres_voulus):
    """Toutes les occurrences (chapitre, ref, champ, chemin, empreinte)."""
    occurrences = []
    fichiers = sorted(RACINE.glob("livre-*/*.md"))
    if not fichiers:
        print(f"Aucun chapitre trouvé sous {RACINE}/livre-*/", file=sys.stderr)
        return None
    for fichier in fichiers:
        brut = fichier.read_text(encoding="utf-8")
        if not brut.startswith("---"):
            continue
        parties = brut.split("---", 2)
        if len(parties) < 3:
            continue
        try:
            entete = yaml.safe_load(parties[1])
        except yaml.YAMLError:
            continue
        if not isinstance(entete, dict):
            continue
        chapitre = entete.get("chapitre")
        if chapitres_voulus and chapitre not in chapitres_voulus:
            continue

        champs = []
        for src in entete.get("sources_primaires") or []:
            if isinstance(src, dict):
                champs.append((src.get("ref"), "reference",
                               src.get("etat_lecture"), str(src.get("reference", ""))))
        for i, att in enumerate(entete.get("verifications_en_attente") or []):
            champs.append((None, f"verifications_en_attente[{i}]", None, str(att)))

        for ref, champ, etat, texte in champs:
            for chemin_cite, inscrite in paires(texte):
                occurrences.append({
                    "chapitre": chapitre, "ref": ref, "champ": champ,
                    "etat_lecture": etat, "statut": entete.get("statut"),
                    "chemin": chemin_cite, "inscrite": inscrite,
                })
    return occurrences


ECHECS = {"DISCORDANTE", "DEPLACEE", "ABSENTE"}
SIGNALEMENTS = {"RENOMMEE"}


def main():
    args = sys.argv[1:]
    detail = "--detail" in args
    strict = "--strict" in args

    chapitres = set()
    for i, a in enumerate(args):
        if a == "--chapitre" and i + 1 < len(args):
            chapitres.add(args[i + 1])
        elif a.startswith("--chapitre="):
            chapitres.add(a.split("=", 1)[1])

    brut = os.environ.get("DEBUNKONOMY_EXEMPLAIRES")
    for i, a in enumerate(args):
        if a == "--dossier" and i + 1 < len(args):
            brut = args[i + 1]
        elif a.startswith("--dossier="):
            brut = a.split("=", 1)[1]

    if not brut:
        print("Racine des exemplaires non fournie.")
        print("  python corpus/verifier-exemplaires.py --dossier <racine>")
        print("  ou définir DEBUNKONOMY_EXEMPLAIRES")
        print()
        print("Les exemplaires vivent hors du dépôt : ce script ne devine pas")
        print("où, et son absence n'est pas un défaut du corpus.")
        return 2

    racine = Path(brut).expanduser()
    if not racine.is_dir():
        print(f"Racine des exemplaires introuvable : {racine}")
        print("Ce n'est pas un défaut du corpus.")
        return 2

    occurrences = relever(chapitres)
    if occurrences is None:
        return 2
    if not occurrences:
        cible = ", ".join(sorted(chapitres)) if chapitres else "le corpus"
        print(f"Aucun exemplaire cité dans {cible}.")
        return 0

    print(f"Racine des exemplaires : {racine}")
    print(f"{len(occurrences)} chemin(s) cité(s) dans "
          f"{len({o['chapitre'] for o in occurrences})} chapitre(s).")
    print()

    bilan = {}
    anomalies = []
    for o in occurrences:
        verdict, precision = examiner(racine, o["chemin"], o["inscrite"])
        o["verdict"], o["precision"] = verdict, precision
        bilan[verdict] = bilan.get(verdict, 0) + 1
        if verdict in ECHECS or verdict in SIGNALEMENTS:
            anomalies.append(o)

    def ligne(o):
        ref = f" [{o['ref']}]" if o["ref"] else ""
        champ = "" if o["champ"] == "reference" else f" {o['champ']}"
        print(f"  {o['verdict']:<12} {o['chapitre']}{ref}{champ}")
        print(f"           {o['chemin']}")
        if o["precision"]:
            print(f"           {o['precision']}")

    if detail:
        for o in occurrences:
            ligne(o)
        print()
    elif anomalies:
        for o in anomalies:
            ligne(o)
        print()

    for verdict in ("CONCORDE", "PRESENTE", "RENOMMEE", "DEPLACEE", "DISCORDANTE", "ABSENTE"):
        if verdict in bilan:
            print(f"  {verdict:<12} {bilan[verdict]}")
    print()

    echecs = sum(bilan.get(v, 0) for v in ECHECS)
    signales = sum(bilan.get(v, 0) for v in SIGNALEMENTS)

    if echecs:
        print(f"ÉCHEC — {echecs} exemplaire(s) absent(s), discordant(s) ou mal nommé(s).")
        print("Ce script ne bloque aucune publication : controle.py reste l'autorité.")
        return 1
    if signales and strict:
        print(f"ÉCHEC (--strict) — {signales} signalement(s).")
        return 1
    if signales:
        print(f"Exemplaires vérifiés. {signales} signalement(s) ci-dessus : la pièce "
              f"est là et son empreinte le prouve, seul le nom diffère.")
        return 0
    print("Exemplaires vérifiés — toutes les empreintes inscrites concordent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
