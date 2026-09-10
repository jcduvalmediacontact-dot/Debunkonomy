#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test d'environnement propre — le contrôle du corpus est-il reproductible ?

Crée un environnement virtuel dans un répertoire temporaire hors du dépôt, y
installe la dépendance épinglée (corpus/requirements.txt) par la voie
connectée puis, à défaut, par la voie hors ligne, vérifie la version
installée, exécute la commande unique de contrôle avec cet interprète et
compare son bilan à celui de l'interprète courant.

    python corpus/test_environnement_propre.py [--voie {auto,connectee,hors-ligne}] [--garder]

La voie hors ligne est FERMÉE : chaque roue de corpus/hors-ligne/ compatible
avec la plateforme doit être inscrite dans SHA256SUMS et y correspondre ; une
seule roue compatible non vérifiée refuse la voie entière, et pip n'a accès
qu'à un répertoire ne contenant que les roues vérifiées — il ne peut pas en
choisir une autre.

Quatre issues, quatre codes de sortie, jamais confondus :
  0  environnement installé et contrôle réussi
  1  contrôle du corpus en échec — défaut du corpus, ou bilan différent de
     celui de l'interprète courant
  2  dépendance indisponible — ni index accessible, ni cache, ni voie hors
     ligne utilisable (artefact absent, non vérifié, ou installation refusée) :
     CE N'EST PAS UN DÉFAUT DU CORPUS
  3  plateforme non couverte par l'artefact hors ligne — la roue conservée ne
     vaut que pour l'étiquette qu'elle porte, et rien n'est revendiqué au-delà

La version de pip n'est pas épinglée ; la version de Python est constatée,
non exigée. Une voie inconnue ou une option --voie sans valeur est refusée.
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import sysconfig
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CORPUS = Path(__file__).resolve().parent
REQUIS = CORPUS / "requirements.txt"
HORS_LIGNE = CORPUS / "hors-ligne"
SOMMES = HORS_LIGNE / "SHA256SUMS"
ISSUES = {0: "environnement installé et contrôle réussi",
          1: "contrôle du corpus en échec",
          2: "dépendance indisponible — ce n'est pas un défaut du corpus",
          3: "plateforme non couverte par l'artefact hors ligne"}
RE_ENTETE = re.compile(r"^(\d+) chapitre\(s\), ")


def version_epinglee():
    for ligne in REQUIS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*PyYAML==([\w.]+)\s*$", ligne, re.I)
        if m:
            return m.group(1)
    raise SystemExit("requirements.txt n'épingle pas PyYAML")


def etiquettes_courantes():
    py = f"cp{sys.version_info.major}{sys.version_info.minor}"
    plat = sysconfig.get_platform().replace("-", "_").replace(".", "_")
    return py, plat


def sommes_attendues():
    """{nom de fichier: sha256} lu dans SHA256SUMS, format « hash  nom »."""
    if not SOMMES.exists():
        return {}
    res = {}
    for ligne in SOMMES.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([0-9a-fA-F]{64})\s+\*?(\S+)\s*$", ligne)
        if m:
            res[m.group(2)] = m.group(1).lower()
    return res


def roues():
    """Les roues de corpus/hors-ligne/ : (nom, compatible, vérifiée)."""
    py, plat = etiquettes_courantes()
    attendues = sommes_attendues()
    res = []
    for roue in sorted(HORS_LIGNE.glob("*.whl")) if HORS_LIGNE.exists() else []:
        m = re.match(r"^(?P<nom>[^-]+)-(?P<ver>[^-]+)-(?P<py>[^-]+)-(?P<abi>[^-]+)-(?P<plat>[^-]+)\.whl$", roue.name)
        compatible = bool(m) and (py in m.group("py").split(".") or "py3" in m.group("py").split(".")) \
            and (plat in m.group("plat").split(".") or "any" in m.group("plat").split("."))
        calcule = hashlib.sha256(roue.read_bytes()).hexdigest()
        res.append((roue.name, compatible, attendues.get(roue.name) == calcule))
    return res


def lancer(commande, cwd=None, delai=300):
    try:
        p = subprocess.run(commande, cwd=cwd, capture_output=True, timeout=delai)
        return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        return 124, "", "délai dépassé"


def bilan(sortie):
    """Les lignes comparables entre deux interprètes : l'en-tête de décompte
    (« N chapitre(s), ... »), quel que soit N, et la ligne finale."""
    lignes = sortie.splitlines()
    entete = [l for l in lignes if RE_ENTETE.match(l)]
    finale = [l for l in lignes if l.startswith(("Contrôle structurel", "ÉCHEC"))]
    return entete[-1:] + finale[-1:]


def chapitres(sortie):
    for l in sortie.splitlines():
        m = RE_ENTETE.match(l)
        if m:
            return int(m.group(1))
    return None


def conclure(code, racine, garder):
    print(f"\nVERDICT : {code} — {ISSUES[code]}")
    if garder:
        print(f"Environnement conservé : {racine}")
    else:
        shutil.rmtree(racine, ignore_errors=True)
    return code


def main():
    p = argparse.ArgumentParser(description="Contrôle du corpus depuis un environnement neuf.")
    p.add_argument("--voie", choices=["auto", "connectee", "hors-ligne"], default="auto",
                   help="auto : connectée puis hors ligne")
    p.add_argument("--garder", action="store_true", help="ne pas supprimer l'environnement temporaire")
    a = p.parse_args()
    attendu = version_epinglee()
    py, plat = etiquettes_courantes()
    racine = Path(tempfile.mkdtemp(prefix="controle-propre-"))
    env = racine / "env"
    print(f"Interprète courant : Python {sys.version.split()[0]} ({py}, {plat})")
    print(f"Dépendance épinglée : PyYAML=={attendu}")
    print(f"Environnement temporaire : {env}")

    code, out, err = lancer([sys.executable, "-m", "venv", str(env)], delai=300)
    if code != 0:
        print("Création de l'environnement virtuel impossible :\n" + err.strip())
        return conclure(2, racine, a.garder)
    python_env = env / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    pip = [str(python_env), "-m", "pip", "--disable-pip-version-check", "--no-input"]

    installee = None
    if a.voie in ("auto", "connectee"):
        print("Voie connectée : python -m pip install -r corpus/requirements.txt")
        code, out, err = lancer(pip + ["install", "--quiet", "-r", str(REQUIS)], delai=300)
        if code == 0:
            installee = "connectée"
        else:
            print("  échec de la voie connectée : " + (err.strip().splitlines() or ["?"])[-1])
    if installee is None and a.voie in ("auto", "hors-ligne"):
        presentes = roues()
        compatibles = [r for r in presentes if r[1]]
        verifiees = [r for r in compatibles if r[2]]
        non_verifiees = [r for r in compatibles if not r[2]]
        print(f"Voie hors ligne : {len(presentes)} roue(s) conservée(s), {len(compatibles)} compatible(s) "
              f"avec {py}-{plat}, {len(verifiees)} vérifiée(s) contre SHA256SUMS")
        for nom, compatible, verifiee in presentes:
            print(f"  {nom} — {'compatible' if compatible else 'autre plateforme'}, "
                  f"{'SHA-256 conforme' if verifiee else 'SHA-256 NON VÉRIFIÉ'}")
        if not presentes:
            print("  aucun artefact hors ligne instruit")
            return conclure(2, racine, a.garder)
        if not compatibles:
            return conclure(3, racine, a.garder)
        if non_verifiees:
            print("  roue(s) compatible(s) non inscrite(s) dans SHA256SUMS ou non conforme(s) : "
                  + ", ".join(r[0] for r in non_verifiees) + " — installation refusée, la voie hors ligne "
                  "n'admet aucune roue non vérifiée")
            return conclure(2, racine, a.garder)
        # pip ne voit que les roues vérifiées : un répertoire d'index restreint.
        index = racine / "roues-verifiees"
        index.mkdir()
        for nom, _, _ in verifiees:
            shutil.copy2(HORS_LIGNE / nom, index / nom)
        code, out, err = lancer(pip + ["install", "--quiet", "--no-index", "--find-links", str(index),
                                       "-r", str(REQUIS)], delai=300)
        if code == 0:
            installee = "hors ligne"
        else:
            print("  échec de la voie hors ligne : " + (err.strip().splitlines() or ["?"])[-1])
    if installee is None:
        return conclure(2, racine, a.garder)

    code, out, err = lancer([str(python_env), "-c", "import yaml; print(yaml.__version__)"])
    version = out.strip()
    print(f"Installée par la voie {installee} : PyYAML {version or '?'}")
    if code != 0 or version != attendu:
        print(f"  version différente de l'épinglage ({attendu})")
        return conclure(2, racine, a.garder)

    print("Contrôle du corpus avec l'interprète de l'environnement propre")
    code_env, out_env, err_env = lancer([str(python_env), str(CORPUS / "controle.py")], cwd=str(CORPUS))
    code_ici, out_ici, _ = lancer([sys.executable, str(CORPUS / "controle.py")], cwd=str(CORPUS))
    for ligne in bilan(out_env):
        print("  | " + ligne)
    identique = bilan(out_env) == bilan(out_ici) and code_env == code_ici and chapitres(out_env) == chapitres(out_ici)
    print(f"Chapitres contrôlés : {chapitres(out_env)} ; bilan identique à celui de l'interprète courant : "
          f"{'oui' if identique else 'NON'}")
    if code_env != 0 or not identique:
        if err_env.strip():
            print("  " + err_env.strip().splitlines()[-1])
        return conclure(1, racine, a.garder)
    return conclure(0, racine, a.garder)


if __name__ == "__main__":
    sys.exit(main())
