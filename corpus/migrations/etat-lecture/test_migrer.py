#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests unitaires de migrer.py — sur des fichiers synthétiques, dans un répertoire
temporaire ; aucun corpus n'est touché. Code de sortie 0 si tout passe.

    python corpus/migrations/etat-lecture/test_migrer.py

  M1  la transformation remplace chaque ligne date_verification par
      etat_lecture: a_requalifier, ligne pour ligne, corps et résumé intacts,
      en LF comme en CRLF ;
  M2  une exception AVANT toute altération du troisième fichier ne laisse aucun
      corpus partiellement migré ;
  M2b une écriture qui CORROMPT le troisième fichier puis échoue est restaurée
      elle aussi : les cinq fichiers retrouvent exactement leurs octets, ni
      manifeste ni rapport n'existent ;
  M2c une exception pendant l'écriture du manifeste, après les chapitres,
      restaure les chapitres et laisse un rapport préexistant intact ;
  M3  sans erreur, les chapitres sont écrits, puis le manifeste, puis le rapport ;
  M4  la comparaison au commit source est intégrale : un titre modifié, un
      renvoi modifié, un statut modifié refusent ; un fichier identique à
      fins de ligne près passe ;
  M5  --sale-attendu est fermé, sur un dépôt Git temporaire : un répertoire,
      un préfixe, un fichier non modifié et un fichier modifié non déclaré
      refusent ; un fichier exact modifié est accepté ; aucun refus n'écrit.
"""
import contextlib
import importlib.util
import io
import shutil
import sys
import tempfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("migrer", ICI / "migrer.py")
migrer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migrer)
RESULTATS = []


def test(nom, condition, detail=""):
    RESULTATS.append((nom, bool(condition)))
    print(("  ok     " if condition else "  ÉCHEC  ") + nom + (("  — " + detail) if detail and not condition else ""))


CHAPITRE = (
    "---\n"
    "chapitre: L9.C50\n"
    "titre: \"Test\"\n"
    "statut: brouillon\n"
    "revision_de_fond: 2026-09-01\n"
    "sources_primaires:\n"
    "  - ref: S1\n"
    "    nature: theorie\n"
    "    reference: \"Un ouvrage\"\n"
    "    url: \"https://exemple.test/\"\n"
    "    date_verification: 2026-09-03\n"
    "  - ref: S2\n"
    "    nature: donnees\n"
    "    reference: \"Une série\"\n"
    "    date_verification: 2026-09-04\n"
    "verifications_en_attente: []\n"
    "resume: \"Résumé de test.\"\n"
    "concepts: []\n"
    "renvois: [L9.C01]\n"
    "---\n"
    "\n"
    "::etat:: Corps de test, avec une date_verification: 2026-09-03 dans le texte qui ne doit pas bouger.\n"
)
ATTENDUES = {"L9.C50/S1": migrer.empreinte_bibliographique({"nature": "theorie", "reference": "Un ouvrage", "url": "https://exemple.test/"}),
             "L9.C50/S2": migrer.empreinte_bibliographique({"nature": "donnees", "reference": "Une série"})}

print("M1  transformation ligne à ligne, LF et CRLF")
for nom, octets in (("LF", CHAPITRE.encode("utf-8")), ("CRLF", CHAPITRE.replace("\n", "\r\n").encode("utf-8"))):
    neuf = migrer.transformer(octets, "L9.C50", ATTENDUES)
    texte = neuf.decode("utf-8")
    test(f"M1 {nom} : deux lignes remplacées, aucune date de source restante",
         texte.count("etat_lecture: a_requalifier") == 2 and "    date_verification:" not in texte)
    test(f"M1 {nom} : le corps est intact, y compris sa fausse date", "date_verification: 2026-09-03 dans le texte" in texte)
    test(f"M1 {nom} : fins de ligne conservées", ("\r\n" in texte) == (nom == "CRLF"))
    test(f"M1 {nom} : même nombre de lignes", len(texte.splitlines()) == len(octets.decode("utf-8").splitlines()))
    r0, r1 = migrer.analyser(migrer.lf(octets.decode("utf-8"))), migrer.analyser(migrer.lf(texte))
    test(f"M1 {nom} : empreinte éditoriale identique", r0[2] == r1[2])


def corpus_synthetique():
    racine = Path(tempfile.mkdtemp(prefix="migrer-test-"))
    originaux = {}
    for i in range(5):
        chemin = racine / f"c{i}.md"
        chemin.write_bytes(f"original {i}\n".encode("utf-8"))
        originaux[chemin] = chemin.read_bytes()
    nouveaux = {chemin: (octets, f"migré {i}\n".encode("utf-8")) for i, (chemin, octets) in enumerate(originaux.items())}
    return racine, originaux, nouveaux, (racine / "manifeste.json", "{}"), (racine / "rapport.md", "# rapport")


def intact(originaux, manifeste, rapport):
    return all(c.read_bytes() == o for c, o in originaux.items()) and not manifeste[0].exists() and not rapport[0].exists()


print("M2  exception avant toute altération du troisième fichier")
racine, originaux, nouveaux, manifeste, rapport = corpus_synthetique()
compteur = {"n": 0}


def tombe_avant(chemin, octets):
    compteur["n"] += 1
    if compteur["n"] == 3:
        raise OSError("disque plein (simulé)")
    chemin.write_bytes(octets)


erreur = None
try:
    migrer.appliquer(nouveaux, manifeste, rapport, ecrire=tombe_avant)
except RuntimeError as e:
    erreur = str(e)
test("M2 l'erreur est relevée et nommée", erreur is not None and "restauré" in erreur, erreur or "aucune erreur")
test("M2 les cinq fichiers sont revenus à leurs octets, ni manifeste ni rapport", intact(originaux, manifeste, rapport))
shutil.rmtree(racine, ignore_errors=True)

print("M2b écriture partielle corrompue puis exception")
racine, originaux, nouveaux, manifeste, rapport = corpus_synthetique()
compteur = {"n": 0}


def corrompt_puis_tombe(chemin, octets):
    compteur["n"] += 1
    if compteur["n"] == 3:
        chemin.write_bytes(b"CORROMPU " + octets[:3])   # écriture partielle, contenu faux
        raise OSError("coupure pendant l'écriture (simulée)")
    chemin.write_bytes(octets)


erreur = None
try:
    migrer.appliquer(nouveaux, manifeste, rapport, ecrire=corrompt_puis_tombe)
except RuntimeError as e:
    erreur = str(e)
troisieme = list(originaux)[2]
test("M2b l'erreur est relevée", erreur is not None and "restauré" in erreur, erreur or "aucune erreur")
test("M2b le fichier corrompu a retrouvé exactement ses octets", troisieme.read_bytes() == originaux[troisieme])
test("M2b les cinq fichiers sont revenus à leurs octets, ni manifeste ni rapport", intact(originaux, manifeste, rapport))
shutil.rmtree(racine, ignore_errors=True)

print("M2c exception pendant l'écriture du manifeste, rapport préexistant")
racine, originaux, nouveaux, manifeste, rapport = corpus_synthetique()
rapport[0].write_bytes(b"ancien rapport")


def tombe_sur_manifeste(chemin, octets):
    if chemin.name == "manifeste.json":
        chemin.write_bytes(b"{ tronq")
        raise OSError("coupure sur le manifeste (simulée)")
    chemin.write_bytes(octets)


erreur = None
try:
    migrer.appliquer(nouveaux, manifeste, rapport, ecrire=tombe_sur_manifeste)
except RuntimeError as e:
    erreur = str(e)
test("M2c les chapitres sont restaurés et le manifeste tronqué retiré",
     erreur is not None and all(c.read_bytes() == o for c, o in originaux.items()) and not manifeste[0].exists())
test("M2c le rapport préexistant est intact", rapport[0].read_bytes() == b"ancien rapport")
shutil.rmtree(racine, ignore_errors=True)

print("M3  application sans erreur, dans l'ordre chapitres, manifeste, rapport")
racine, originaux, nouveaux, manifeste, rapport = corpus_synthetique()
ordre = []
n = migrer.appliquer(nouveaux, manifeste, rapport, ecrire=lambda c, o: (ordre.append(c.name), c.write_bytes(o)))
test("M3 sept écritures, les chapitres avant le manifeste, le manifeste avant le rapport",
     n == 7 and ordre[-2:] == ["manifeste.json", "rapport.md"] and all(x.startswith("c") for x in ordre[:5]))
test("M3 les chapitres portent leur nouveau contenu", all(c.read_bytes() == a for c, (_, a) in nouveaux.items()))
shutil.rmtree(racine, ignore_errors=True)

print("M4  comparaison intégrale au commit source")
racine = Path(tempfile.mkdtemp(prefix="migrer-test-"))
dossier = racine / "corpus" / "livre-09-test"
dossier.mkdir(parents=True)
fichier = dossier / "c50-test.md"
entete, corps, edito = migrer.analyser(CHAPITRE)
source = {"L9.C50": {"chemin": "corpus/livre-09-test/c50-test.md", "entete": entete, "corps": corps,
                     "edito": edito, "texte": CHAPITRE}}
occurrences = [{"id": "L9.C50/S1", "empreinte_bibliographique": ATTENDUES["L9.C50/S1"], "ancienne_date_verification": "2026-09-03"},
               {"id": "L9.C50/S2", "empreinte_bibliographique": ATTENDUES["L9.C50/S2"], "ancienne_date_verification": "2026-09-04"}]


def verdict(texte):
    """None si l'arbre passe, sinon le message de refus."""
    fichier.write_bytes(texte.encode("utf-8"))
    sortie = io.StringIO()
    try:
        with contextlib.redirect_stdout(sortie):
            migrer.verifier_arbre(racine, source, occurrences)
        return None
    except SystemExit as e:
        return sortie.getvalue().strip() if e.code == 2 else f"code {e.code}"


test("M4 un fichier identique passe", verdict(CHAPITRE) is None)
test("M4 identique à fins de ligne près (CRLF) passe", verdict(CHAPITRE.replace("\n", "\r\n")) is None)
r = verdict(CHAPITRE.replace('titre: "Test"', 'titre: "Test modifié"'))
test("M4 un titre modifié refuse", r is not None and "différent du commit source" in r, r or "")
r = verdict(CHAPITRE.replace("renvois: [L9.C01]", "renvois: [L9.C02]"))
test("M4 un renvoi modifié refuse", r is not None and "différent du commit source" in r, r or "")
r = verdict(CHAPITRE.replace("statut: brouillon", "statut: audit_contradictoire"))
test("M4 un statut modifié refuse", r is not None and "différent du commit source" in r, r or "")
r = verdict(CHAPITRE.replace("Corps de test", "Corps de test retouché"))
test("M4 un corps modifié refuse", r is not None and "différent du commit source" in r, r or "")
shutil.rmtree(racine, ignore_errors=True)

print("M5  --sale-attendu : fichiers exacts de l'état Git seulement, aucune écriture sur refus")
import os
import stat
import subprocess


def supprimer(racine):
    def forcer(fonction, chemin, _exc):
        os.chmod(chemin, stat.S_IWRITE)
        fonction(chemin)
    shutil.rmtree(racine, onexc=forcer)


racine = Path(tempfile.mkdtemp(prefix="migrer-test-"))
(racine / "corpus" / "livre-09-test").mkdir(parents=True)
(racine / "protocoles").mkdir()
(racine / "corpus" / "livre-09-test" / "c50-test.md").write_bytes(CHAPITRE.encode("utf-8"))
(racine / "notes.md").write_bytes(b"notes\n")
(racine / "autre.md").write_bytes(b"autre\n")
(racine / "protocoles" / "index.md").write_bytes(b"protocoles\n")


def g(*args):
    return subprocess.run(["git", "-c", "user.name=test", "-c", "user.email=test@test.invalid", *args],
                          cwd=str(racine), capture_output=True, text=True, encoding="utf-8")


g("init", "-q")
g("add", "-A")
g("commit", "-q", "-m", "base")
head = g("rev-parse", "HEAD").stdout.strip()
(racine / "notes.md").write_bytes(b"notes modifiees\n")


def lancer_migrer(*sale):
    p = subprocess.run([sys.executable, str(ICI / "migrer.py"), "--racine", str(racine), "--commit-source", head, *sale],
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, p.stdout


def etat_fichiers():
    return {p: p.read_bytes() for p in racine.rglob("*") if p.is_file() and ".git" not in p.parts}


avant = etat_fichiers()
code, out = lancer_migrer("--sale-attendu=corpus")
test("M5 --sale-attendu=corpus est refusé : un répertoire", code == 2 and "répertoire" in out, out[-200:])
code, out = lancer_migrer("--sale-attendu=notes.md", "--sale-attendu=autre.md")
test("M5 un fichier déclaré mais non modifié est refusé", code == 2 and "absent de l'état Git" in out, out[-200:])
code, out = lancer_migrer("--sale-attendu=notes")
test("M5 une correspondance par préfixe est refusée", code == 2 and "absent de l'état Git" in out, out[-200:])
code, out = lancer_migrer()
test("M5 un fichier modifié non déclaré est refusé", code == 2 and "arbre sale non attendu" in out, out[-200:])
test("M5 aucun refus n'a écrit quoi que ce soit", etat_fichiers() == avant)
code, out = lancer_migrer("--sale-attendu=notes.md")
test("M5 un fichier exact modifié est accepté, passage sans écriture", code == 0 and "SANS ÉCRITURE" in out, out[-300:])
test("M5 le passage sans écriture n'a rien écrit non plus", etat_fichiers() == avant)
supprimer(racine)

echecs = [nom for nom, ok in RESULTATS if not ok]
print()
print(f"{len(RESULTATS) - len(echecs)} test(s) passé(s), {len(echecs)} échec(s).")
sys.exit(1 if echecs else 0)
