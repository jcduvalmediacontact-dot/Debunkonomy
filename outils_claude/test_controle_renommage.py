# -*- coding: utf-8 -*-
"""Sabotages du contrôle par ancrage. Sur copies, jamais sur le dépôt.

Un contrôle qui passe sur un corpus intact ne prouve rien : il faut lui faire
subir l'attaque qu'il prétend détecter. Huit sabotages, dont **deux contrôles
négatifs** — sans eux, un contrôle qui échoue toujours passerait ce test.

  E-R1  substitution à total constant   — LE DÉFAUT NOMMÉ PAR LA PASSE ADVERSE
  E-R2  occurrence neuve, chapitre déjà déclaré
  E-R3  occurrence retirée
  E-R4  occurrence neuve, chapitre non déclaré
  E-R5  phrase réécrite autour d'une occurrence conservée
  E-R6  note déclarée dupliquée — le multi-ensemble, et non l'ensemble
  N-R1  corpus intact                   — contrôle négatif : doit PASSER
  N-R2  retouche loin de toute occurrence — contrôle négatif : doit PASSER

    python outils_claude/test_controle_renommage.py
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
ANCRAGES = os.path.join(RACINE, "outils_claude", "ancrages-renommage.json")
NEUTRE = "à contrepartie collective"      # ne contient pas « sans dette »


def lire(F):
    return io.open(F, encoding="utf-8").read()


def ecrire(F, t):
    io.open(F, "w", encoding="utf-8", newline="\n").write(t)


def monter(tmp):
    """Un dépôt de poche : le corpus et l'outil, rien d'autre."""
    for livre in os.listdir(os.path.join(RACINE, "corpus")):
        src = os.path.join(RACINE, "corpus", livre)
        if livre.startswith("livre-") and os.path.isdir(src):
            shutil.copytree(src, os.path.join(tmp, "corpus", livre),
                            ignore=shutil.ignore_patterns("*.pyc", "__pycache__"))
    os.makedirs(os.path.join(tmp, "outils_claude"))
    for f in ("controle_renommage.py", "ancrages-renommage.json"):
        shutil.copy2(os.path.join(RACINE, "outils_claude", f),
                     os.path.join(tmp, "outils_claude", f))


def controler(tmp):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable,
                        os.path.join(tmp, "outils_claude", "controle_renommage.py")],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=300)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def chemin(tmp, chapitre):
    """Le fichier d'un matricule, retrouvé par son en-tête et non par son nom."""
    for d in sorted(os.listdir(os.path.join(tmp, "corpus"))):
        dossier = os.path.join(tmp, "corpus", d)
        if not os.path.isdir(dossier):
            continue
        for n in sorted(os.listdir(dossier)):
            if not n.endswith(".md"):
                continue
            F = os.path.join(dossier, n)
            m = re.search(r"(?m)^chapitre: (\S+)", lire(F))
            if m and m.group(1) == chapitre:
                return F
    raise AssertionError("chapitre introuvable : %s" % chapitre)


def coupe_corps(t):
    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    assert m, "en-tête introuvable"
    return t[:m.end()], t[m.end():]


faits = []


def verifier(nom, attendu, code, journal):
    verdict = "OK" if (code != 0) == attendu else "MANQUÉ"
    faits.append((nom, verdict, code))
    out.write("  %-5s %-6s attendu %-7s code %d\n"
              % (nom, verdict, "ÉCHEC" if attendu else "PASSE", code))
    if verdict != "OK":
        out.write("    ---- sortie ----\n")
        for l in journal.strip().splitlines()[-14:]:
            out.write("    %s\n" % l)


# ── Sur quel chapitre travailler : lu dans les ancrages, jamais codé en dur ───
declarees = json.loads(lire(ANCRAGES))
corps = [o for o in declarees if o["zone"] == "corps"]
assert corps, "aucune occurrence déclarée dans un corps : sabotages impossibles"
CIBLE = corps[0]["chapitre"]
notes = [o for o in declarees if o["zone"] == "notes"]
assert notes, "aucune occurrence déclarée dans une note"
CIBLE_NOTE = notes[0]["chapitre"]
sans = sorted({re.search(r"(?m)^chapitre: (\S+)", lire(os.path.join(RACINE, "corpus", d, n)))
               .group(1)
               for d in os.listdir(os.path.join(RACINE, "corpus"))
               if d.startswith("livre-") and os.path.isdir(os.path.join(RACINE, "corpus", d))
               for n in os.listdir(os.path.join(RACINE, "corpus", d))
               if n.endswith(".md")
               and "sans dette" not in lire(os.path.join(RACINE, "corpus", d, n)).lower()})
assert sans, "aucun chapitre vierge : E-R4 impossible"
VIERGE = sans[0]

out.write("SABOTAGES DU CONTRÔLE PAR ANCRAGE\n")
out.write("=" * 78 + "\n")
out.write("cible corps %s, cible note %s, chapitre vierge %s\n\n"
          % (CIBLE, CIBLE_NOTE, VIERGE))

tmp = tempfile.mkdtemp(prefix="ancrages-")
try:
    monter(tmp)

    # ── N-R1 : le contrôle négatif d'abord. S'il échoue, le reste ne dit rien ──
    code, j = controler(tmp)
    verifier("N-R1", False, code, j)
    assert code == 0, ("le corpus copié ne passe pas : les sabotages qui suivent\n"
                       "seraient tous des faux positifs.\n" + j)

    F = chemin(tmp, CIBLE)
    INTACT = lire(F)

    # ── E-R1 : SUBSTITUTION À TOTAL CONSTANT ─────────────────────────────────
    # Une occurrence disparaît du corps, une autre apparaît ailleurs DANS LE MÊME
    # CORPS. Chapitre, zone et total sont inchangés : l'ancienne version passait.
    tete, c = coupe_corps(INTACT)
    i = c.lower().index("sans dette")
    c2 = c[:i] + NEUTRE + c[i + len("sans dette"):]
    c2 += "\n\nLigne de sabotage, insérée loin de là : sans dette.\n"
    assert c2.lower().count("sans dette") == c.lower().count("sans dette"), "total modifié"
    ecrire(F, tete + c2)
    code, j = controler(tmp)
    verifier("E-R1", True, code, j)

    # ── E-R2 : une occurrence de plus ────────────────────────────────────────
    ecrire(F, INTACT + "\n\nPhrase neuve : sans dette.\n")
    code, j = controler(tmp)
    verifier("E-R2", True, code, j)

    # ── E-R3 : une occurrence de moins ───────────────────────────────────────
    tete, c = coupe_corps(INTACT)
    i = c.lower().index("sans dette")
    ecrire(F, tete + c[:i] + NEUTRE + c[i + len("sans dette"):])
    code, j = controler(tmp)
    verifier("E-R3", True, code, j)

    # ── E-R5 : le terme reste, la phrase autour de lui change ────────────────
    # C'est la « phrase neuve cachée derrière le marqueur » : l'occurrence est
    # bien celle qui était déclarée, mais elle ne dit plus la même chose.
    tete, c = coupe_corps(INTACT)
    i = c.lower().index("sans dette")
    ecrire(F, tete + c[:i] + "bel et bien " + c[i:])
    code, j = controler(tmp)
    verifier("E-R5", True, code, j)

    # ── N-R2 : une retouche hors de portée de tout ancrage doit PASSER ───────
    # Sans ce contrôle, un outil qui empreinte le fichier entier passerait le
    # test en échouant partout — et serait inutilisable.
    tete, c = coupe_corps(INTACT)
    creux = [m.start() for m in re.finditer(r"\n\n", c)
             if not re.search("sans dette",
                              c[max(0, m.start() - 200):m.start() + 200], re.I)]
    assert creux, "aucun creux hors de portée dans %s" % CIBLE
    k = creux[len(creux) // 2]
    ecrire(F, tete + c[:k] + "\n\nParagraphe ajouté loin de toute occurrence.\n" + c[k:])
    code, j = controler(tmp)
    verifier("N-R2", False, code, j)
    ecrire(F, INTACT)

    # ── E-R4 : une occurrence dans un chapitre qui n'en portait aucune ───────
    G = chemin(tmp, VIERGE)
    vierge = lire(G)
    ecrire(G, vierge + "\n\nOccurrence clandestine : sans dette.\n")
    code, j = controler(tmp)
    verifier("E-R4", True, code, j)
    ecrire(G, vierge)

    # ── E-R6 : une note déclarée, dupliquée à l'identique ────────────────────
    # Même chapitre, même zone, MÊME EMPREINTE. Un ensemble ne verrait rien ;
    # un multi-ensemble compte deux fois.
    H = chemin(tmp, CIBLE_NOTE)
    intact_note = lire(H)
    tete, c = coupe_corps(intact_note)
    m = re.search(r'(?ms)^  - "[^"]*RENOMMAGE CANONIQUE DU 2026-09-20[^"]*"\n', tete)
    assert m, "note de renommage introuvable dans %s" % CIBLE_NOTE
    ecrire(H, tete[:m.end()] + m.group(0) + tete[m.end():] + c)
    code, j = controler(tmp)
    verifier("E-R6", True, code, j)
    ecrire(H, intact_note)

finally:
    shutil.rmtree(tmp, ignore_errors=True)

rates = [f for f in faits if f[1] != "OK"]
out.write("\n%d contrôle(s), %d manqué(s).\n" % (len(faits), len(rates)))
if rates:
    out.write("ÉCHEC : %s\n" % ", ".join(f[0] for f in rates))
    sys.exit(1)
out.write("Le contrôle détecte la substitution à total constant, et laisse passer\n")
out.write("ce qui ne touche à aucune occurrence déclarée.\n")
