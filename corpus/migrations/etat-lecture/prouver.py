#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preuve de conservation de la migration etat_lecture — huit invariants,
calculés INDÉPENDAMMENT du script qui écrit et du script qui contrôle.

    python corpus/migrations/etat-lecture/prouver.py --commit-source <sha> [--racine <dépôt>]

Ce script n'importe ni controle.py ni migrer.py. Il possède son propre
chargement YAML, sa propre normalisation, son propre calcul SHA-256, sa propre
validation du manifeste — schéma fermé — et sa propre détection des doublons
de chapitres et de références : un doublon n'écrase jamais rien en silence, il
rend l'invariant faux. Il applique les règles que la convention spécifie
(§ 4, § 5, § 12) ; si deux implémentations en divergeaient, la preuve le
montrerait.

L'état « avant » se lit dans le commit source, par git show ; l'état « après »
dans l'arbre de travail. Le manifeste doit porter EXACTEMENT ce commit source :
un manifeste écrit depuis un autre commit rend I6 faux, quelle que soit la
validité de ses autres champs. Chaque invariant est imprimé avec ses valeurs
mesurées ; le script sort en erreur si l'un d'eux est faux.

  I1  identifiants : a_requalifier après = datés avant = manifeste (trois ensembles)
  I2  vidage : zéro date_verification, zéro ouverte, zéro candidate après
  I3  effectifs : nombre d'occurrences identique par chapitre, avant et après,
      mêmes chapitres, aucun doublon de chapitre ni de référence
  I4  empreintes bibliographiques : après = avant = manifeste, occurrence par occurrence
  I5  corps : empreinte éditoriale identique pour tous les chapitres ; empreinte de
      métadonnées changée pour exactement les chapitres porteurs, et pour eux seuls
  I6  manifeste : schéma fermé, commit source égal à celui demandé, dates, files,
      traces, doublons
  I7  état enregistré : .etat-corpus.json à jour sur les trois champs, et
      empreinte éditoriale enregistrée = celle du commit source, pour tous
  I8  qualifications : celles du commit source se retrouvent après, à l'identique
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

FILES = {"A": "orientation vers ouverte", "B": "traces contradictoires",
         "C": "orientation vers candidate", "D": "sans orientation"}
CODES = {"T1", "T2", "T3", "T4", "T5", "T6", "T7"}
CHAMPS_MANIFESTE = {"schema", "migration", "occurrences"}
CHAMPS_MIGRATION = {"date", "commit_source", "revision_convention", "python", "pyyaml",
                    "nombre_occurrences", "regle_empreinte"}
CHAMPS_OCCURRENCE = {"id", "chapitre", "ref", "empreinte_bibliographique", "ancienne_date_verification",
                     "date_migration", "traces", "file", "orientation", "etat_initial"}
CHAMPS_TRACE = {"code", "emplacement", "appui"}
RE_HEX64 = re.compile(r"^[0-9a-f]{64}$")
RE_SHA = re.compile(r"^[0-9a-f]{40}$")


# --- règles de la convention, réimplémentées ici ------------------------------

def normalise(texte):
    return "\n".join(l.strip() for l in str(texte).strip().splitlines() if l.strip())


def empreinte16(*morceaux):
    h = hashlib.sha256()
    for m in morceaux:
        h.update(normalise(str(m)).encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:16]


def empreinte_bibliographique(src):
    base = {k: normalise(str(src[k])) for k in ("nature", "reference", "url")
            if k in src and src[k] is not None}
    canon = json.dumps(base, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def empreinte_metadonnees(entete):
    return empreinte16(json.dumps({k: str(v) for k, v in sorted(entete.items()) if k != "resume"},
                                  ensure_ascii=False))


def orienter(codes):
    fort = codes & {"T1", "T2", "T7"}
    if fort and "T3" in codes:
        return "B"
    if fort:
        return "A"
    if "T3" in codes:
        return "C"
    return "D"


def date_valide(valeur):
    try:
        date.fromisoformat(str(valeur))
        return True
    except (TypeError, ValueError):
        return False


def chaine(valeur, sans=""):
    return isinstance(valeur, str) and valeur.strip() != "" and not any(c in valeur for c in sans)


# --- lecture -----------------------------------------------------------------

def git(racine, *args):
    return subprocess.check_output(["git", "-c", "core.quotepath=off", *args],
                                   cwd=str(racine), stderr=subprocess.DEVNULL).decode("utf-8", "replace")


def analyser(brut):
    """(en-tête, empreinte éditoriale, empreinte de métadonnées) ou None."""
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
    return entete, empreinte16(parties[2], entete.get("resume", "")), empreinte_metadonnees(entete)


def charger_chapitres(textes):
    """(chapitres, doublons_chapitres, doublons_refs) — un doublon est relevé,
    jamais absorbé."""
    chapitres, doublons_chapitres, doublons_refs = {}, [], []
    for brut in textes:
        r = analyser(brut)
        if r is None or r[0].get("partie", 1) != 1:
            continue
        cle = r[0]["chapitre"]
        if cle in chapitres:
            doublons_chapitres.append(cle)
            continue
        chapitres[cle] = r
        vus = set()
        for s in r[0].get("sources_primaires") or []:
            if isinstance(s, dict):
                ref = str(s.get("ref"))
                if ref in vus:
                    doublons_refs.append(f"{cle}/{ref}")
                vus.add(ref)
    return chapitres, doublons_chapitres, doublons_refs


def occurrences_de(chapitres):
    res = {}
    for cle, (entete, _, _) in chapitres.items():
        for s in entete.get("sources_primaires") or []:
            if isinstance(s, dict):
                ident = f"{cle}/{s.get('ref')}"
                if ident not in res:
                    res[ident] = s
    return res


def valider_manifeste(chemin, commit_demande):
    """Validation propre, schéma fermé, sans controle.py. Retourne
    (manifeste ou None, erreurs)."""
    erreurs = []
    if not chemin.exists():
        return None, ["manifeste absent"]
    try:
        contenu = json.loads(chemin.read_text(encoding="utf-8"))
    except Exception as e:
        return None, [f"manifeste illisible : {e}"]
    if not isinstance(contenu, dict):
        return None, ["manifeste mal formé"]
    for champ in sorted(set(contenu) - CHAMPS_MANIFESTE):
        erreurs.append(f"champ inconnu au niveau supérieur : {champ}")
    if contenu.get("schema") != "manifeste-etat-lecture/1":
        erreurs.append(f"schema {contenu.get('schema')!r}")
    migration = contenu.get("migration")
    occurrences = contenu.get("occurrences")
    if not isinstance(migration, dict) or not isinstance(occurrences, list):
        return None, erreurs + ["migration ou occurrences absents"]
    for champ in sorted(CHAMPS_MIGRATION - set(migration)):
        erreurs.append(f"champ de migration absent : {champ}")
    for champ in sorted(set(migration) - CHAMPS_MIGRATION):
        erreurs.append(f"champ de migration inconnu : {champ}")
    for champ in ("python", "pyyaml", "regle_empreinte"):
        if champ in migration and not chaine(migration[champ]):
            erreurs.append(f"{champ} : chaîne non vide attendue")
    commit_manifeste = str(migration.get("commit_source", ""))
    if not RE_SHA.match(commit_manifeste):
        erreurs.append("commit_source n'est pas un SHA complet")
    elif commit_manifeste != commit_demande:
        erreurs.append(f"commit_source du manifeste {commit_manifeste[:10]} ≠ commit demandé {commit_demande[:10]}")
    if migration.get("revision_convention") != 12:
        erreurs.append(f"revision_convention {migration.get('revision_convention')!r}")
    if not date_valide(migration.get("date")):
        erreurs.append("date de migration invalide")
    if migration.get("nombre_occurrences") != len(occurrences):
        erreurs.append("nombre_occurrences différent du nombre d'entrées")
    ids, refs = {}, set()
    for rang, o in enumerate(occurrences, 1):
        if not isinstance(o, dict):
            erreurs.append(f"occurrence {rang} mal formée")
            continue
        ident = str(o.get("id"))
        for champ in sorted(CHAMPS_OCCURRENCE - set(o)):
            erreurs.append(f"{ident} : champ obligatoire absent : {champ}")
        for champ in sorted(set(o) - CHAMPS_OCCURRENCE):
            erreurs.append(f"{ident} : champ inconnu : {champ}")
        if not chaine(o.get("chapitre"), sans="/ \t\n") or not chaine(o.get("ref"), sans="/ \t\n"):
            erreurs.append(f"{ident} : chapitre ou ref n'est pas une chaîne valide")
        if ident != f"{o.get('chapitre')}/{o.get('ref')}":
            erreurs.append(f"{ident} : identifiant incohérent avec chapitre/ref")
        if ident in ids:
            erreurs.append(f"{ident} : identifiant dupliqué")
        ids[ident] = o
        paire = (str(o.get("chapitre")), str(o.get("ref")))
        if paire in refs:
            erreurs.append(f"{ident} : référence dupliquée")
        refs.add(paire)
        if not RE_HEX64.match(str(o.get("empreinte_bibliographique", ""))):
            erreurs.append(f"{ident} : empreinte mal formée")
        if not date_valide(o.get("ancienne_date_verification")) or not date_valide(o.get("date_migration")):
            erreurs.append(f"{ident} : date invalide")
        if str(o.get("date_migration")) != str(migration.get("date")):
            erreurs.append(f"{ident} : date_migration différente de l'en-tête")
        if o.get("etat_initial") != "a_requalifier":
            erreurs.append(f"{ident} : etat_initial {o.get('etat_initial')!r}")
        if o.get("file") not in FILES:
            erreurs.append(f"{ident} : file {o.get('file')!r}")
        traces = o.get("traces")
        if not isinstance(traces, list) or any(
                not isinstance(t, dict) or set(t) != CHAMPS_TRACE or t.get("code") not in CODES
                or not chaine(t.get("emplacement")) or not chaine(t.get("appui")) for t in traces):
            erreurs.append(f"{ident} : traces mal formées")
        else:
            attendu = orienter({t["code"] for t in traces})
            if o.get("file") != attendu or o.get("orientation") != FILES.get(attendu):
                erreurs.append(f"{ident} : file ou orientation incohérentes avec les traces")
    if erreurs:
        return None, erreurs
    return {"date": migration["date"], "commit_source": commit_manifeste, "occurrences": ids}, []


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--commit-source", required=True)
    p.add_argument("--racine", default=str(Path(__file__).resolve().parents[3]))
    a = p.parse_args()
    racine = Path(a.racine).resolve()
    commit = git(racine, "rev-parse", "--verify", a.commit_source + "^{commit}").strip()

    textes_avant = [git(racine, "show", f"{commit}:{c}").replace("\r\n", "\n")
                    for c in git(racine, "ls-tree", "-r", "--name-only", commit, "--", "corpus").splitlines()
                    if re.match(r"^corpus/livre-[^/]+/[^/]+\.md$", c)]
    avant, dbl_ch_avant, dbl_ref_avant = charger_chapitres(textes_avant)
    try:
        etat_avant = json.loads(git(racine, "show", f"{commit}:corpus/.etat-corpus.json"))
    except subprocess.CalledProcessError:
        etat_avant = {}
    textes_apres = [c.read_bytes().decode("utf-8").replace("\r\n", "\n")
                    for c in sorted((racine / "corpus").glob("livre-*/*.md"))]
    apres, dbl_ch_apres, dbl_ref_apres = charger_chapitres(textes_apres)
    chemin_etat = racine / "corpus" / ".etat-corpus.json"
    etat_apres = json.loads(chemin_etat.read_text(encoding="utf-8")) if chemin_etat.exists() else {}
    manifeste, erreurs_manifeste = valider_manifeste(racine / "corpus" / "manifeste-etat-lecture.json", commit)
    doublons = dbl_ch_avant + dbl_ch_apres + dbl_ref_avant + dbl_ref_apres

    occ_avant, occ_apres = occurrences_de(avant), occurrences_de(apres)
    dates_avant = {i for i, s in occ_avant.items() if s.get("date_verification")}
    requal_apres = {i for i, s in occ_apres.items() if s.get("etat_lecture") == "a_requalifier"}
    ids_manifeste = set(manifeste["occurrences"]) if manifeste else set()
    resultats = []

    def inv(code, vrai, detail):
        resultats.append((code, bool(vrai) and not doublons,
                          detail + (" ; DOUBLONS : " + ", ".join(doublons[:5]) if doublons else "")))

    inv("I1", dates_avant == requal_apres == ids_manifeste and len(ids_manifeste) > 0,
        f"datés avant {len(dates_avant)} = a_requalifier après {len(requal_apres)} = manifeste {len(ids_manifeste)} ; "
        f"écarts : {len(dates_avant ^ requal_apres) + len(requal_apres ^ ids_manifeste)}")
    n_date = sum(1 for s in occ_apres.values() if "date_verification" in s)
    n_ouv = sum(1 for s in occ_apres.values() if s.get("etat_lecture") == "ouverte")
    n_cand = sum(1 for s in occ_apres.values() if s.get("etat_lecture") == "candidate")
    inv("I2", n_date == 0 and n_ouv == 0 and n_cand == 0, f"date_verification {n_date}, ouverte {n_ouv}, candidate {n_cand}")
    eff_avant = collections.Counter(i.split("/")[0] for i in occ_avant)
    eff_apres = collections.Counter(i.split("/")[0] for i in occ_apres)
    inv("I3", eff_avant == eff_apres and set(avant) == set(apres),
        f"{len(avant)} chapitres avant, {len(apres)} après ; "
        f"{sum(1 for c in set(avant) | set(apres) if eff_avant[c] != eff_apres[c])} chapitre(s) d'effectif différent ; "
        f"doublons de chapitre {len(dbl_ch_avant) + len(dbl_ch_apres)}, de référence {len(dbl_ref_avant) + len(dbl_ref_apres)}")
    ecarts4 = [i for i in occ_avant if i not in occ_apres
               or empreinte_bibliographique(occ_avant[i]) != empreinte_bibliographique(occ_apres[i])
               or not manifeste
               or manifeste["occurrences"].get(i, {}).get("empreinte_bibliographique") != empreinte_bibliographique(occ_apres[i])]
    inv("I4", not ecarts4 and manifeste is not None, f"{len(occ_avant)} occurrence(s) comparées, {len(ecarts4)} écart(s)")
    porteurs = {c for c in avant if eff_avant[c]}
    edito_ok = [c for c in avant if c in apres and avant[c][1] == apres[c][1]]
    meta_changee = {c for c in avant if c in apres and avant[c][2] != apres[c][2]}
    inv("I5", len(edito_ok) == len(avant) == len(apres) and meta_changee == porteurs,
        f"éditoriale identique {len(edito_ok)}/{len(avant)} ; métadonnées changées {len(meta_changee)}, "
        f"porteurs {len(porteurs)}, non porteurs intacts {len(avant) - len(porteurs)}")
    inv("I6", manifeste is not None,
        f"cohérent, commit source du manifeste = {commit[:10]} demandé" if manifeste is not None
        else "; ".join(erreurs_manifeste[:3]))
    a_jour = [c for c in apres if c in etat_apres
              and etat_apres[c].get("editoriale") == apres[c][1]
              and etat_apres[c].get("metadonnees") == apres[c][2]
              and str(etat_apres[c].get("revision_de_fond")) == str(apres[c][0].get("revision_de_fond"))]
    source_ok = [c for c in avant if c in etat_apres and etat_apres[c].get("editoriale") == avant[c][1]]
    inv("I7", len(a_jour) == len(apres) == len(etat_apres) and len(source_ok) == len(avant),
        f"entrées à jour {len(a_jour)}/{len(apres)} ({len(etat_apres)} enregistrées) ; "
        f"éditoriale = commit source pour {len(source_ok)}/{len(avant)}")
    q_avant = {c: e.get("qualification") for c, e in etat_avant.items() if e.get("qualification")}
    perdues = [c for c, q in q_avant.items() if etat_apres.get(c, {}).get("qualification") != q]
    inv("I8", not perdues and len(q_avant) > 0,
        f"{len(q_avant)} qualification(s) avant, {len(q_avant) - len(perdues)} retrouvées à l'identique, {len(perdues)} perdue(s)")

    print(f"PREUVE DE CONSERVATION — commit source {commit[:10]}, arbre de travail {racine}")
    print("  (calculs propres : YAML, normalisation, SHA-256, manifeste, doublons — sans controle.py ni migrer.py)")
    print("-" * 78)
    for code, vrai, detail in resultats:
        print(f"  {code}  {'VRAI' if vrai else 'FAUX'}  {detail}")
    faux = [c for c, v, _ in resultats if not v]
    print("-" * 78)
    print("VERDICT : " + ("les huit invariants tiennent" if not faux else "invariant(s) faux : " + ", ".join(faux)))
    return 0 if not faux else 1


if __name__ == "__main__":
    sys.exit(main())
