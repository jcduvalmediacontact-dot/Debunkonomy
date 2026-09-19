# -*- coding: utf-8 -*-
"""Contrôle du générateur de dossier de supervision.

Sept sabotages et garanties, dont le point qui a motivé ce test : sous Windows,
un sous-processus écrit dans l'encodage de la console et la sortie arrive en
mojibake. Un verdict de contrôle illisible dans un dossier de supervision est
pire qu'absent : il se lit comme du bruit et se saute.

    python outils_claude/test_dossier_codex.py
"""
import io
import os
import re
import subprocess
import sys
import tempfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTIL = os.path.join(RACINE, "outils_claude", "dossier_codex.py")
CHAPITRE = "L1.C29"
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
echecs = []
faits = []


def lance(args, entree_faiblesses=None):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    return subprocess.run([sys.executable, OUTIL] + args, cwd=RACINE, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", env=env, timeout=1800)


def verifie(nom, condition, detail=""):
    faits.append(nom)
    out.write("  %-6s %s%s\n" % ("ok" if condition else "ÉCHEC", nom,
                                 "" if condition else "  — " + detail))
    if not condition:
        echecs.append(nom)


tmp = tempfile.mkdtemp(prefix="test-dossier-")
f_faib = os.path.join(tmp, "faiblesses.md")
f_vide = os.path.join(tmp, "vide.md")
f_sortie = os.path.join(tmp, "dossier.md")
io.open(f_faib, "w", encoding="utf-8").write(
    "Faiblesse d'épreuve, avec accents : é à ù ç œ « » — pour vérifier le transport.")
io.open(f_vide, "w", encoding="utf-8").write("   \n  \n")

out.write("Contrôle du générateur de dossier de supervision\n\n")

# T1 — refus sans la piece obligatoire
r = lance([CHAPITRE])
verifie("T1 refus sans --faiblesses", r.returncode != 0 and "REFUS" in (r.stderr or ""),
        "code %s" % r.returncode)

# T2 — refus si le fichier est vide
r = lance([CHAPITRE, "--faiblesses", f_vide])
verifie("T2 refus si faiblesses vides", r.returncode != 0 and "REFUS" in (r.stderr or ""),
        "code %s" % r.returncode)

# T3 — refus si le fichier n'existe pas
r = lance([CHAPITRE, "--faiblesses", os.path.join(tmp, "absent.md")])
verifie("T3 refus si fichier absent", r.returncode != 0, "code %s" % r.returncode)

# Production d'un dossier reel pour les controles suivants
r = lance([CHAPITRE, "--faiblesses", f_faib, "--sortie", f_sortie])
ok = r.returncode == 0 and os.path.exists(f_sortie)
verifie("T4 production du dossier", ok, (r.stderr or "").strip()[:120])
if not ok:
    out.write("\nProduction impossible : les contrôles suivants sont sautés.\n")
    sys.exit(1)
d = io.open(f_sortie, encoding="utf-8").read()

# T5 — ENCODAGE : aucun caractere de remplacement, et les accents sont transportes
mojibake = re.findall(r"[�]|Ã©|Ã¨|Ã |â€™|g\W?n\W?rateur conforme", d)
verifie("T5 aucun mojibake dans le dossier", not mojibake,
        "trouvé : %s" % sorted(set(mojibake))[:4])
verifie("T5 bis accents transportés depuis les faiblesses",
        "é à ù ç œ « »" in d, "la chaîne d'épreuve n'est pas ressortie intacte")

# T6 — le corps du chapitre N'EST PAS reproduit
chap = None
for racine, _, fichiers in os.walk(os.path.join(RACINE, "corpus")):
    for f in fichiers:
        if f.endswith(".md"):
            p = os.path.join(racine, f)
            t = io.open(p, encoding="utf-8").read()
            if re.search(r"(?m)^chapitre: %s$" % re.escape(CHAPITRE), t):
                chap = t
if chap is None:
    verifie("T6 corps non reproduit", False, "chapitre d'épreuve introuvable")
else:
    m = re.search(r"(?ms)\A---\n.*?\n---\n", chap)
    corps = chap[m.end():]
    # une phrase longue du corps ne doit pas se retrouver telle quelle dans le dossier
    longues = [l.strip() for l in corps.split("\n") if len(l.strip()) > 300]
    temoin = longues[len(longues) // 2][:200] if longues else None
    verifie("T6 corps du chapitre non reproduit",
            temoin is not None and temoin not in d,
            "une phrase de 200 signes du corps figure dans le dossier")
    verifie("T6 bis empreinte du corps présente",
            re.search(r"sha256:[0-9a-f]{64}", d) is not None,
            "le superviseur ne peut pas vérifier qu'il lit le bon état")

# T7 — compacite
mots = len(d.split())
verifie("T7 dossier compact (< 3000 mots)", mots < 3000, "%d mots" % mots)

out.write("\n%d contrôle(s), %d échec(s).\n" % (len(faits), len(echecs)))
if echecs:
    out.write("ÉCHECS : %s\n" % ", ".join(echecs))
out.flush()
sys.exit(1 if echecs else 0)
