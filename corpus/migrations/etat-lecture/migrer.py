#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Migration etat_lecture — écrit UNE FOIS et UNIFORMÉMENT, depuis le HEAD courant.

    python corpus/migrations/etat-lecture/migrer.py --commit-source <sha> [--appliquer]
        [--date AAAA-MM-JJ] [--sale-attendu <chemin> ...] [--racine <dépôt>]

SANS ÉCRITURE PAR DÉFAUT. Le script relève, oriente, transforme en mémoire,
valide et rend compte de ce qu'il écrirait ; il n'écrit que sous --appliquer.

Ce qu'il fait, dans l'ordre (protocoles/migration-etat-lecture.md, § 7) :
  0. résout --commit-source, exige qu'il soit EXACTEMENT le HEAD courant, et
     vérifie que l'arbre n'est sale que là où on l'attend — jamais sur un
     chapitre ;
  1. relève, dans les chapitres du commit source lus par git show, chaque
     occurrence de source datée : identifiant chapitre/ref, empreinte
     bibliographique, ancienne date, traces T1..T7 avec leur appui ;
  2. oriente chaque occurrence vers une file d'examen A, B, C ou D ;
  3. exige que chaque chapitre de l'arbre soit IDENTIQUE, texte intégral, à
     celui du commit source — fins de ligne LF/CRLF mises à part —, calcule TOUS
     les nouveaux contenus, les valide un par un, prépare le manifeste et le
     rapport depuis le même relevé, vérifie toutes les égalités disponibles ;
     puis, sous --appliquer seulement, écrit les chapitres, puis le manifeste,
     puis le rapport, en inscrivant les octets d'origine de chaque fichier AVANT
     de l'écrire et en restaurant l'ensemble si une écriture échoue.

Ce qu'il REFUSE, avant toute écriture :
  - un commit source inexistant, ou différent du HEAD courant — pour répéter
    depuis un commit ancien, on positionne une copie sur ce commit ;
  - un arbre sale non attendu : tout chemin modifié qui n'est pas déclaré par
    --sale-attendu. Chaque déclaration désigne UN FICHIER EXACT de l'état Git :
    un répertoire, un préfixe, un chemin non modifié sont refusés, et tout
    chapitre l'est aussi, parce que les chapitres sont précisément l'objet dont
    l'identité avec le commit source doit être garantie ;
  - un manifeste ou un rapport déjà présent ;
  - un chapitre de l'arbre différent du commit source, où que soit l'écart :
    titre, statut, concepts, renvois, vérifications, sources, résumé, corps ;
  - un nombre d'occurrences dans l'arbre différent de son propre relevé ;
  - un identifiant chapitre/ref dupliqué, dans le relevé ou dans l'arbre ;
  - une source historique sans date ;
  - un état initial autre que a_requalifier — il n'en connaît aucun autre.

Autonome : n'importe ni controle.py ni aucun autre script du dépôt. Il applique
la règle d'empreinte que la convention spécifie (§ 4, § 12) avec ses propres
fonctions, et prouver.py la réapplique ensuite, séparément. Aucun chiffre n'est
une preuve : les égalités d'ensembles et les empreintes décident.
"""
import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ETAT_INITIAL = "a_requalifier"
CHAMPS_EMPREINTE_BIBLIO = ("nature", "reference", "url")
FILES = {"A": "orientation vers ouverte", "B": "traces contradictoires",
         "C": "orientation vers candidate", "D": "sans orientation"}
NIE = ["non ouvert", "non ouverte", "non ouverts", "non ouvertes", "pas ouvert",
       "pas encore ouvert", "à ouvrir", "non consulté", "non lu", "pas lu",
       "accès refusé", "refuse les requêtes", "requêtes automatiques", "paywall",
       "doi confirmé", "doi seulement", "résumé seulement", "non vérifié",
       "introuvable", "non téléchargé", "scan sans couche de texte"]
AFFIRME = ["est ouvert", "est ouverte", "a été ouvert", "a été ouverte", "ouvert le",
           "ouverte le", "ouvert par téléchargement", "texte lu", "le texte est lu",
           "lu et", "ocr lu", "citation retrouvée", "passage retrouvé"]
DETTE = ["ocr", "folio", "numéro de page", "pagination"]
MARQUEUR_T1 = "TÉLÉCHARGEMENT DIRECT"
RE_DATE = re.compile(r"^([ \t]+)date_verification:[ \t]*\S+[ \t]*$", re.M)
RE_CHAPITRE = re.compile(r"^corpus/livre-[^/]+(/.*)?$")


# --- règles de la convention, réimplémentées ici ------------------------------

def normalise(texte):
    return "\n".join(l.strip() for l in str(texte).strip().splitlines() if l.strip())


def empreinte16(*morceaux):
    """Empreinte éditoriale (convention § 5) : sha256 des morceaux normalisés,
    séparés par un octet nul, tronquée à seize hexadécimaux."""
    h = hashlib.sha256()
    for m in morceaux:
        h.update(normalise(str(m)).encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:16]


def empreinte_bibliographique(src):
    """Empreinte des métadonnées bibliographiques d'origine (convention § 12) :
    nature, reference, url normalisés, clés absentes omises, JSON canonique,
    sha256 complet."""
    base = {k: normalise(str(src[k])) for k in CHAMPS_EMPREINTE_BIBLIO
            if k in src and src[k] is not None}
    canon = json.dumps(base, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def orienter(codes):
    fort = codes & {"T1", "T2", "T7"}
    if fort and "T3" in codes:
        return "B"
    if fort:
        return "A"
    if "T3" in codes:
        return "C"
    return "D"


# --- outillage --------------------------------------------------------------

def refuser(message):
    print(f"\nREFUS — {message}\nRien n'a été écrit.")
    sys.exit(2)


def git(racine, *args):
    return subprocess.check_output(["git", "-c", "core.quotepath=off", *args],
                                   cwd=str(racine), stderr=subprocess.STDOUT).decode("utf-8", "replace")


def norm(texte):
    return re.sub(r"\s+", " ", str(texte or "")).lower()


def lf(texte):
    return texte.replace("\r\n", "\n")


def analyser(brut):
    """(en-tête, corps, empreinte éditoriale) d'un chapitre en texte LF, ou None."""
    if not brut.startswith("---"):
        return None
    parties = brut.split("---", 2)
    if len(parties) < 3:
        return None
    try:
        entete = yaml.safe_load(parties[1])
    except Exception:
        return None
    if not isinstance(entete, dict) or not entete.get("chapitre"):
        return None
    return entete, parties[2], empreinte16(parties[2], entete.get("resume", ""))


# --- 1. relevé au commit source ------------------------------------------------

def relever(racine, commit):
    chemins = [l for l in git(racine, "ls-tree", "-r", "--name-only", commit, "--", "corpus").splitlines()
               if re.match(r"^corpus/livre-[^/]+/[^/]+\.md$", l)]
    chapitres = {}
    for chemin in sorted(chemins):
        texte = lf(git(racine, "show", f"{commit}:{chemin}"))
        r = analyser(texte)
        if r is None:
            continue
        entete, corps, edito = r
        if entete.get("partie", 1) != 1:
            continue
        cle = entete["chapitre"]
        if cle in chapitres:
            refuser(f"identifiant de chapitre dupliqué au commit source : {cle}")
        chapitres[cle] = {"chemin": chemin, "entete": entete, "corps": corps, "edito": edito, "texte": texte}
    ouvertes_ailleurs = {}
    for cle, d in chapitres.items():
        for s in d["entete"].get("sources_primaires") or []:
            if isinstance(s, dict) and MARQUEUR_T1 in str(s.get("reference", "")):
                ouvertes_ailleurs.setdefault(norm(s.get("reference"))[:90], []).append(cle)
    creations = {}
    occurrences, ids = [], set()
    for cle, d in sorted(chapitres.items()):
        e = d["entete"]
        attente = [str(x) for x in (e.get("verifications_en_attente") or [])]
        sources = [s for s in (e.get("sources_primaires") or []) if isinstance(s, dict)]
        if sources:
            jours = git(racine, "log", "--follow", "--diff-filter=A", "--format=%ad", "--date=short",
                        commit, "--", d["chemin"]).split()
            creations[cle] = jours[-1] if jours else None
        for s in sources:
            ref = str(s.get("ref"))
            ident = f"{cle}/{ref}"
            if ident in ids:
                refuser(f"identifiant dupliqué dans le relevé : {ident}")
            ids.add(ident)
            if not s.get("date_verification"):
                refuser(f"source historique sans date : {ident}")
            texte = str(s.get("reference", ""))
            traces = []
            if MARQUEUR_T1 in texte:
                i = texte.find(MARQUEUR_T1)
                traces.append({"code": "T1", "emplacement": "reference", "appui": texte[max(0, i - 60):i + 40]})
            for i, item in enumerate(attente):
                if ref not in set(re.findall(r"\bS\d{1,2}\b", item)):
                    continue
                bas = norm(item)
                if any(m in bas for m in AFFIRME):
                    traces.append({"code": "T2", "emplacement": f"verifications_en_attente[{i}]", "appui": item[:240]})
                if any(m in bas for m in NIE):
                    traces.append({"code": "T3", "emplacement": f"verifications_en_attente[{i}]", "appui": item[:240]})
                if any(m in bas for m in DETTE):
                    traces.append({"code": "T7", "emplacement": f"verifications_en_attente[{i}]", "appui": item[:240]})
            m4 = re.search(r"[«\"][^»\"]{40,}[»\"][^.]{0,80}\[%s\]" % re.escape(ref), d["corps"])
            if m4:
                traces.append({"code": "T4", "emplacement": "corps", "appui": m4.group(0)[:240]})
            autres = [c for c in ouvertes_ailleurs.get(norm(texte)[:90], []) if c != cle]
            if autres and MARQUEUR_T1 not in texte:
                traces.append({"code": "T5", "emplacement": ", ".join(autres), "appui": "même référence marquée T1 ailleurs"})
            ancienne = str(s.get("date_verification"))
            if creations.get(cle) and ancienne > creations[cle]:
                traces.append({"code": "T6", "emplacement": "git",
                               "appui": f"date {ancienne} postérieure à la création {creations[cle]}"})
            fichier = orienter({t["code"] for t in traces})
            occurrences.append({
                "id": ident, "chapitre": cle, "ref": ref,
                "empreinte_bibliographique": empreinte_bibliographique(s),
                "ancienne_date_verification": ancienne,
                "traces": sorted(traces, key=lambda t: t["code"]),
                "file": fichier, "orientation": FILES[fichier],
                "etat_initial": ETAT_INITIAL,
            })
    return chapitres, occurrences


# --- 2. l'arbre est-il le commit source, texte intégral ? -------------------------------

def verifier_arbre(racine, chapitres_source, occurrences):
    """Chaque chapitre de l'arbre doit être identique, texte intégral, à celui
    du commit source — seules les fins de ligne LF/CRLF sont neutralisées.
    Titre, statut, autorité, citable, concepts, renvois, vérifications,
    sources, résumé, corps : tout écart refuse."""
    attendues = {o["id"]: o for o in occurrences}
    vues, fichiers = set(), {}
    for chemin in sorted((racine / "corpus").glob("livre-*/*.md")):
        octets = chemin.read_bytes()
        texte = lf(octets.decode("utf-8"))
        r = analyser(texte)
        if r is None:
            continue
        entete, corps, edito = r
        if entete.get("partie", 1) != 1:
            continue
        cle = entete["chapitre"]
        if cle in fichiers:
            refuser(f"identifiant de chapitre dupliqué dans l'arbre : {cle}")
        if cle not in chapitres_source:
            refuser(f"chapitre {cle} présent dans l'arbre et absent du commit source")
        if texte != chapitres_source[cle]["texte"]:
            refuser(f"chapitre {cle} différent du commit source — texte intégral comparé, "
                    f"fins de ligne mises à part")
        for s in entete.get("sources_primaires") or []:
            if not isinstance(s, dict):
                continue
            ident = f"{cle}/{s.get('ref')}"
            if ident in vues:
                refuser(f"identifiant dupliqué dans l'arbre : {ident}")
            if ident not in attendues:
                refuser(f"occurrence {ident} présente dans l'arbre et absente du relevé")
            if empreinte_bibliographique(s) != attendues[ident]["empreinte_bibliographique"]:
                refuser(f"occurrence {ident} : métadonnées bibliographiques différentes du commit source")
            if str(s.get("date_verification")) != attendues[ident]["ancienne_date_verification"]:
                refuser(f"occurrence {ident} : date différente du commit source")
            vues.add(ident)
        fichiers[cle] = (chemin, octets)
    manquants = sorted(set(chapitres_source) - set(fichiers))
    if manquants:
        refuser("chapitre(s) du commit source absent(s) de l'arbre : " + ", ".join(manquants))
    if vues != set(attendues):
        refuser(f"{len(vues)} occurrence(s) dans l'arbre, {len(attendues)} dans le relevé")
    return fichiers


# --- 3. transformation en mémoire ----------------------------------------------------

def transformer(octets, cle, attendues_du_chapitre):
    """Nouveaux octets du chapitre : chaque ligne date_verification d'une source
    devient etat_lecture: a_requalifier. Ligne à ligne, fins de ligne intactes,
    corps et résumé vérifiés identiques."""
    texte = octets.decode("utf-8")
    crlf = "\r\n" in texte
    texte_lf = lf(texte) if crlf else texte
    parties = texte_lf.split("---", 2)
    tete, nb = RE_DATE.subn(r"\1etat_lecture: " + ETAT_INITIAL, parties[1])
    if nb != len(attendues_du_chapitre):
        refuser(f"{cle} : {nb} ligne(s) date_verification pour {len(attendues_du_chapitre)} occurrence(s)")
    neuf = "---".join([parties[0], tete, parties[2]])
    avant, apres = analyser(texte_lf), analyser(neuf)
    if apres is None:
        refuser(f"{cle} : en-tête illisible après transformation")
    if apres[2] != avant[2]:
        refuser(f"{cle} : empreinte éditoriale modifiée par la transformation")
    vus = set()
    for s in apres[0].get("sources_primaires") or []:
        if not isinstance(s, dict):
            continue
        ident = f"{cle}/{s.get('ref')}"
        if s.get("etat_lecture") != ETAT_INITIAL or "date_verification" in s:
            refuser(f"{ident} : état initial différent de {ETAT_INITIAL} après transformation")
        if empreinte_bibliographique(s) != attendues_du_chapitre.get(ident):
            refuser(f"{ident} : empreinte bibliographique altérée par la transformation")
        vus.add(ident)
    if vus != set(attendues_du_chapitre):
        refuser(f"{cle} : occurrences différentes après transformation")
    if len(texte_lf.splitlines()) != len(neuf.splitlines()):
        refuser(f"{cle} : nombre de lignes modifié")
    return (neuf.replace("\n", "\r\n") if crlf else neuf).encode("utf-8")


def rapport(commit, jour, chapitres, occurrences, versions):
    files = collections.Counter(o["file"] for o in occurrences)
    par_chapitre = collections.defaultdict(list)
    for o in occurrences:
        par_chapitre[o["chapitre"]].append(o)
    L = []
    w = L.append
    w("# Rapport de conservation — migration etat_lecture")
    w("")
    w("**Généré par `migrer.py` depuis le même relevé que le manifeste ; le manifeste fait foi.**")
    w("")
    w("| champ | valeur |")
    w("|---|---|")
    w(f"| date de migration | {jour} |")
    w(f"| commit source | `{commit}` — le HEAD courant au moment de la migration, vérifié égal par le script ; "
      f"le commit de migration n'est pas inscrit ici |")
    w(f"| Python, PyYAML | {versions['python']}, {versions['pyyaml']} |")
    w(f"| chapitres | {len(chapitres)}, dont {len(par_chapitre)} portant au moins une occurrence |")
    w(f"| occurrences historiques | {len(occurrences)} — toutes `a_requalifier` |")
    for f, libelle in FILES.items():
        w(f"| file {f} — {libelle} | {files[f]} |")
    w(f"| bouclage | {files['A']} + {files['B']} + {files['C']} + {files['D']} = {sum(files.values())} |")
    w("")
    w("## Par chapitre")
    w("")
    w("| chapitre | occurrences | A | B | C | D |")
    w("|---|---|---|---|---|---|")
    for cle in sorted(par_chapitre):
        c = collections.Counter(o["file"] for o in par_chapitre[cle])
        w(f"| {cle} | {len(par_chapitre[cle])} | {c['A']} | {c['B']} | {c['C']} | {c['D']} |")
    w("")
    w("## Par occurrence — ancienne date, file, traces et appui")
    w("")
    for cle in sorted(par_chapitre):
        w(f"### {cle}")
        w("")
        for o in par_chapitre[cle]:
            traces = "aucune" if not o["traces"] else " ; ".join(
                f"{t['code']} ({t['emplacement']}) « {t['appui'][:120]} »" for t in o["traces"])
            w(f"- `{o['id']}` — ancienne date {o['ancienne_date_verification']} — file {o['file']}, "
              f"{o['orientation']} — traces : {traces}")
        w("")
    return "\n".join(L) + "\n"


# --- 4. application transactionnelle -----------------------------------------------------

def appliquer(nouveaux, manifeste, rapport_final, ecrire=None):
    """Écrit les chapitres, puis le manifeste, puis le rapport.

    nouveaux       : {Path: (octets d'origine, nouveaux octets)}
    manifeste      : (Path, texte)     rapport_final : (Path, texte)
    ecrire         : fonction (chemin, octets) — injectable pour les tests.

    Les octets d'origine de CHAQUE fichier sont inscrits dans la liste de
    restauration AVANT que son écriture soit tentée : une écriture qui tronque
    ou corrompt le fichier puis échoue est restaurée elle aussi. Un fichier qui
    n'existait pas est retiré. En cas d'échec, tout est rendu à son état
    d'origine, dans l'ordre inverse, et l'erreur est relevée.
    """
    ecrire = ecrire or (lambda chemin, octets: chemin.write_bytes(octets))
    restauration = []
    try:
        for chemin, (avant, apres) in nouveaux.items():
            restauration.append((chemin, avant))
            ecrire(chemin, apres)
        for chemin, texte in (manifeste, rapport_final):
            restauration.append((chemin, chemin.read_bytes() if chemin.exists() else None))
            ecrire(chemin, texte.encode("utf-8"))
    except Exception as erreur:
        restaures = 0
        for chemin, avant in reversed(restauration):
            if avant is None:
                chemin.unlink(missing_ok=True)
            else:
                chemin.write_bytes(avant)
            restaures += 1
        raise RuntimeError(f"écriture interrompue ({erreur}) — {restaures} fichier(s) restauré(s), "
                           f"corpus rendu à son état d'origine") from erreur
    return len(restauration)


def main():
    p = argparse.ArgumentParser(description="Migration etat_lecture, une fois et uniformément ; sans écriture sauf --appliquer.")
    p.add_argument("--commit-source", required=True, help="doit être exactement le HEAD courant")
    p.add_argument("--appliquer", action="store_true", help="écrit réellement ; sinon, tout est calculé et rien n'est écrit")
    p.add_argument("--date", default=str(date.today()))
    p.add_argument("--sale-attendu", action="append", default=[])
    p.add_argument("--racine", default=str(Path(__file__).resolve().parents[3]))
    a = p.parse_args()
    racine = Path(a.racine).resolve()
    try:
        date.fromisoformat(a.date)
    except ValueError:
        refuser(f"date de migration invalide : {a.date}")

    # 0. commit source = HEAD, arbre attendu, aucun chapitre déclaré sale
    try:
        commit = git(racine, "rev-parse", "--verify", "--quiet", a.commit_source + "^{commit}").strip()
    except subprocess.CalledProcessError:
        refuser(f"commit source inexistant : {a.commit_source}")
    head = git(racine, "rev-parse", "HEAD").strip()
    if commit != head:
        refuser(f"commit source {commit[:10]} différent du HEAD courant {head[:10]} — "
                f"pour répéter depuis un commit ancien, positionner une copie sur ce commit")
    manifeste_chemin = racine / "corpus" / "manifeste-etat-lecture.json"
    rapport_chemin = racine / "protocoles" / "rapport-migration-etat-lecture.md"
    for chemin in (manifeste_chemin, rapport_chemin):
        if chemin.exists():
            refuser(f"déjà présent : {chemin.relative_to(racine)} — la migration a déjà eu lieu ?")
    attendus = sorted({s.replace("\\", "/") for s in a.sale_attendu})
    chapitres_declares = [x for x in attendus if RE_CHAPITRE.match(x)]
    if chapitres_declares:
        refuser("un chapitre ne peut pas être déclaré sale, son identité avec le commit source est "
                "précisément ce qui est garanti : " + ", ".join(chapitres_declares[:6]))
    repertoires = [x for x in attendus if x.endswith("/") or (racine / x).is_dir()]
    if repertoires:
        refuser("un répertoire ne peut pas être déclaré sale — chaque déclaration désigne un fichier "
                "exact de l'état Git : " + ", ".join(repertoires[:6]))
    sales = []
    for ligne in git(racine, "status", "--porcelain", "--untracked-files=all").splitlines():
        chemin = ligne[3:].strip().strip('"')
        if " -> " in chemin:
            chemin = chemin.split(" -> ")[-1]
        sales.append(chemin)
    non_modifies = [x for x in attendus if x not in sales]
    if non_modifies:
        refuser("déclaré sale mais absent de l'état Git — chaque déclaration désigne un fichier exact, "
                "modifié ou non suivi, sans correspondance par préfixe : " + ", ".join(non_modifies[:6]))
    inattendus = [c for c in sales if c not in attendus]
    if inattendus:
        refuser("arbre sale non attendu : " + ", ".join(inattendus[:12]))
    print(f"Commit source : {commit} = HEAD")
    print(f"Arbre : {len(sales)} fichier(s) modifié(s), chacun déclaré exactement, aucun chapitre")

    # 1. relevé et 2. orientation
    chapitres, occurrences = relever(racine, commit)
    porteurs = {o["chapitre"] for o in occurrences}
    files = collections.Counter(o["file"] for o in occurrences)
    if sum(files.values()) != len(occurrences):
        refuser("les files ne se bouclent pas")
    print(f"Relevé : {len(occurrences)} occurrence(s) datée(s) dans {len(porteurs)} chapitre(s) "
          f"sur {len(chapitres)} ; identifiants uniques")
    print(f"Files : A {files['A']}, B {files['B']}, C {files['C']}, D {files['D']} = {sum(files.values())}")
    fichiers = verifier_arbre(racine, chapitres, occurrences)
    print("Arbre de travail : chaque chapitre identique au commit source, texte intégral, fins de ligne mises à part")

    # 3. tout calculer, tout valider, avant d'écrire quoi que ce soit
    attendues = collections.defaultdict(dict)
    for o in occurrences:
        attendues[o["chapitre"]][o["id"]] = o["empreinte_bibliographique"]
        o["date_migration"] = a.date
    nouveaux = {}
    for cle in sorted(porteurs):
        chemin, octets = fichiers[cle]
        nouveaux[chemin] = (octets, transformer(octets, cle, attendues[cle]))
    versions = {"python": sys.version.split()[0], "pyyaml": str(getattr(yaml, "__version__", "?"))}
    manifeste = {
        "schema": "manifeste-etat-lecture/1",
        "migration": {
            "date": a.date, "commit_source": commit, "revision_convention": 12,
            "python": versions["python"], "pyyaml": versions["pyyaml"],
            "nombre_occurrences": len(occurrences),
            "regle_empreinte": "sha256(json.dumps({nature, reference, url} normalisés — lignes épurées, "
                               "lignes vides retirées —, sort_keys=True, ensure_ascii=False, "
                               "separators=(',', ':'))) ; convention § 4 et § 12",
        },
        "occurrences": sorted(occurrences, key=lambda o: (o["chapitre"], o["ref"])),
    }
    texte_manifeste = json.dumps(manifeste, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    texte_rapport = rapport(commit, a.date, chapitres, occurrences, versions)
    ids_manifeste = [o["id"] for o in manifeste["occurrences"]]
    if len(set(ids_manifeste)) != len(ids_manifeste) or set(ids_manifeste) != {o["id"] for o in occurrences}:
        refuser("le manifeste ne porte pas exactement les identifiants du relevé")
    if json.loads(texte_manifeste)["migration"]["nombre_occurrences"] != len(occurrences):
        refuser("nombre d'occurrences du manifeste différent du relevé")
    if any(o["etat_initial"] != ETAT_INITIAL for o in occurrences):
        refuser("un état initial autre que a_requalifier a été produit")
    print(f"Calculé et validé : {len(nouveaux)} chapitre(s) à migrer, {len(chapitres) - len(nouveaux)} sans "
          f"occurrence intact(s) ; manifeste de {len(occurrences)} occurrence(s) ; rapport de "
          f"{len(texte_rapport.splitlines())} lignes")

    if not a.appliquer:
        print("\nSANS ÉCRITURE : rien n'a été modifié. Relancer avec --appliquer pour écrire.")
        return 0

    ecrits = appliquer(nouveaux, (manifeste_chemin, texte_manifeste), (rapport_chemin, texte_rapport))
    print(f"\nAPPLIQUÉ : {ecrits} fichier(s) écrit(s) — {len(nouveaux)} chapitre(s), le manifeste, le rapport.")
    print(f"Manifeste clos : {manifeste_chemin.relative_to(racine)} — date de migration {a.date}")
    print(f"Rapport : {rapport_chemin.relative_to(racine)}")
    print("Étape suivante : contrôle complet, --maj-etat, puis prouver.py --commit-source", commit[:8])
    return 0


if __name__ == "__main__":
    sys.exit(main())
