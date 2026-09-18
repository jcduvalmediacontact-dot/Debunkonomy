#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests négatifs de la vérification des exemplaires, par sabotage.

Chaque sabotage s'exécute sur un corpus et un dossier d'exemplaires SYNTHÉTIQUES,
construits dans un répertoire temporaire ; ni le corpus réel ni le dossier des
exemplaires ne sont touchés, et le test ne suppose pas qu'un dossier
d'exemplaires existe sur la machine. Un sabotage réussit quand la vérification
produit le verdict attendu ET le code de sortie attendu. Code de sortie 0 si
tous passent, 1 sinon.

    python corpus/test_verifier_exemplaires.py

  S0   le bac fidèle passe sans anomalie — sinon rien ne prouve rien
  S1   un octet ajouté à la pièce                       → DISCORDANTE, code 1
  S2   la pièce supprimée                               → ABSENTE, code 1
  S3   la pièce renommée, empreinte retrouvée           → RENOMMEE, code 0
  S4   la même, en --strict                             → RENOMMEE, code 1
  S5   une autre pièce sous le nom cité                 → DEPLACEE, code 1
  S6   pièce écartée citée sans empreinte               → aucune discordance
  S7   racine des exemplaires introuvable               → code 2
  S8   le bac restauré passe de nouveau

S6 est le test de non-régression de la RÈGLE D'APPARIEMENT. Une entrée cite
couramment l'exemplaire ouvert, avec son empreinte, ET des exemplaires écartés,
sans la leur. Un contrôle qui attacherait l'unique empreinte de l'entrée à tous
les chemins qu'elle cite fabriquerait des discordances inexistantes — c'est
l'erreur commise et corrigée le 2026-09-18.
"""
import hashlib
import importlib.util
import io
import shutil
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

ICI = Path(__file__).resolve().parent
SCRIPT = ICI / "verifier-exemplaires.py"

if not SCRIPT.exists():
    sys.exit(f"Script absent : {SCRIPT}")

spec = importlib.util.spec_from_file_location("verifier_exemplaires", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

RESULTATS = []


def test(nom, ok, precision=""):
    RESULTATS.append((nom, ok))
    print(f"  {'OK  ' if ok else 'RATÉ'}  {nom}")
    if not ok and precision:
        print(f"        {precision}")


def sha(chemin):
    h = hashlib.sha256()
    h.update(chemin.read_bytes())
    return h.hexdigest().upper()


SEANCE = "2026-01-01/seance"
OUVERTE = f"{SEANCE}/piece-ouverte.pdf"
ECARTEE = f"{SEANCE}/piece-ecartee.pdf"
VOISINE = f"{SEANCE}/piece-voisine.pdf"

base = Path(tempfile.mkdtemp(prefix="essai-exemplaires-"))
corpus = base / "corpus"
bac = base / "exemplaires"


def batir():
    """Corpus et bac neufs. Les empreintes sont calculées, jamais écrites."""
    if corpus.exists():
        shutil.rmtree(corpus)
    if bac.exists():
        shutil.rmtree(bac)
    (bac / SEANCE).mkdir(parents=True)
    (bac / OUVERTE).write_bytes(b"texte de la piece ouverte\n" * 64)
    (bac / ECARTEE).write_bytes(b"couche de texte illisible\n" * 32)
    (bac / VOISINE).write_bytes(b"une autre piece du meme dossier\n" * 16)

    livre = corpus / "livre-01-essai"
    livre.mkdir(parents=True)
    (livre / "c01-essai.md").write_text(
        "---\n"
        "chapitre: L1.C01\n"
        "titre: \"Chapitre d'essai\"\n"
        "statut: brouillon\n"
        "sources_primaires:\n"
        "  - ref: S1\n"
        "    nature: theorie\n"
        "    etat_lecture: ouverte\n"
        "    reference: \"Un auteur, Un titre, 1970 — OUVERT PAR TÉLÉCHARGEMENT\n"
        "      DIRECT le 2026-01-01, exemplaire au dossier (" + OUVERTE + ",\n"
        "      4 pages, SHA-256 " + sha(bac / OUVERTE) + "). ÉCARTÉ, ET SANS\n"
        "      EMPREINTE : l'exemplaire " + ECARTEE + " porte une couche de\n"
        "      texte illisible et n'est pas retenu.\"\n"
        "verifications_en_attente: []\n"
        "---\n\nCorps d'essai.\n",
        encoding="utf-8")
    mod.RACINE = corpus


def lancer(racine=None, *extra):
    mod._cache.clear()
    sys.argv = ["verifier-exemplaires.py", "--dossier",
                str(racine if racine is not None else bac)] + list(extra)
    tampon = io.StringIO()
    with redirect_stdout(tampon):
        code = mod.main()
    return code, tampon.getvalue()


def bilan(sortie):
    """Le récapitulatif seul : les lignes d'anomalie répètent les mots."""
    compte = {}
    for ligne in sortie.splitlines():
        p = ligne.split()
        if len(p) == 2 and p[0].isupper() and p[1].isdigit():
            compte[p[0]] = int(p[1])
    return compte


cite = bac / OUVERTE

print("S0  le bac fidèle passe sans anomalie")
batir()
code, out = lancer()
b = bilan(out)
test("S0 code 0, une pièce concordante, une présente sans empreinte",
     code == 0 and b.get("CONCORDE") == 1 and b.get("PRESENTE") == 1, f"{code} {b}")

print("S1  un octet ajouté")
batir()
with open(cite, "ab") as f:
    f.write(b"\x00")
code, out = lancer()
test("S1 DISCORDANTE, code 1", code == 1 and bilan(out).get("DISCORDANTE") == 1,
     f"{code} {bilan(out)}")

print("S2  la pièce supprimée")
batir()
cite.unlink()
code, out = lancer()
test("S2 ABSENTE, code 1", code == 1 and bilan(out).get("ABSENTE") == 1,
     f"{code} {bilan(out)}")

print("S3  la pièce renommée")
batir()
cite.rename(cite.with_name("nom-different.pdf"))
code, out = lancer()
test("S3 RENOMMEE, code 0 — l'empreinte retrouve la pièce",
     code == 0 and bilan(out).get("RENOMMEE") == 1 and "nom-different.pdf" in out,
     f"{code} {bilan(out)}")

print("S4  la même, en --strict")
batir()
cite.rename(cite.with_name("nom-different.pdf"))
code, out = lancer(bac, "--strict")
test("S4 RENOMMEE, code 1 sous --strict",
     code == 1 and bilan(out).get("RENOMMEE") == 1, f"{code} {bilan(out)}")

print("S5  une autre pièce sous le nom cité")
batir()
cite.rename(cite.with_name("rangee-ailleurs.pdf"))
shutil.copy2(bac / VOISINE, cite)
code, out = lancer()
test("S5 DEPLACEE, code 1 — l'entrée nomme la mauvaise pièce",
     code == 1 and bilan(out).get("DEPLACEE") == 1, f"{code} {bilan(out)}")

print("S6  la pièce écartée, citée sans empreinte")
batir()
code, out = lancer()
b = bilan(out)
test("S6 aucune discordance : l'empreinte n'appartient qu'à la pièce qu'elle suit",
     not b.get("DISCORDANTE") and not b.get("DEPLACEE") and b.get("PRESENTE") == 1,
     f"{code} {b}")

print("S7  racine des exemplaires introuvable")
batir()
code, out = lancer(base / "racine-qui-n-existe-pas")
test("S7 code 2, et ce n'est pas un défaut du corpus",
     code == 2 and "défaut du corpus" in out, f"{code} {out[:120]}")

print("S8  le bac restauré")
batir()
code, out = lancer()
test("S8 code 0 de nouveau", code == 0 and bilan(out).get("CONCORDE") == 1,
     f"{code} {bilan(out)}")

shutil.rmtree(base, ignore_errors=True)
echecs = [n for n, ok in RESULTATS if not ok]
print()
print(f"{len(RESULTATS) - len(echecs)} sabotage(s) détecté(s) comme attendu, {len(echecs)} échec(s).")
sys.exit(1 if echecs else 0)
