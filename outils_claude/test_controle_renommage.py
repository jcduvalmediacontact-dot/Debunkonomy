# -*- coding: utf-8 -*-
"""Sabotages du contrôle par ancrage. Sur copies, jamais sur le dépôt.

Un contrôle qui passe sur un corpus intact ne prouve rien : il faut lui faire
subir l'attaque qu'il prétend détecter. **Et un contrôle qui échouerait toujours
obtiendrait un sans-faute** : d'où les contrôles négatifs et positifs, marqués N.

La DÉTECTION — le relevé contre le registre :

  E-R1  substitution à total constant     — LE DÉFAUT NOMMÉ PAR LA PASSE ADVERSE
  E-R2  occurrence neuve, chapitre déjà déclaré
  E-R3  occurrence retirée
  E-R4  occurrence neuve, chapitre non déclaré
  E-R5  phrase réécrite autour d'une occurrence conservée
  E-R6  note déclarée dupliquée           — le multi-ensemble, et non l'ensemble
  N-R1  corpus intact                     — doit PASSER
  N-R2  retouche loin de toute occurrence — doit PASSER

L'ADMISSION — ce qui entre au registre, et qui l'approuve :

  G-R1  occurrence neuve dans un chapitre DÉJÀ déclaré : refusée, registre intact
  G-R2  ancrage admis sans motif propre
  G-R3  ancrage admis mais absent du relevé
  G-R4  admission en règle                — doit PASSER, et inscrire LE motif donné
  G-R5  aucun changement                  — doit PASSER, registre inchangé
  G-R6  disparition seule                 — doit PASSER sans admission
  G-R7  cinq ancrages d'un coup : refusés, et le refus propose de scinder
  G-R8  quatre ancrages d'un coup         — doit PASSER, le plafond est à quatre

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


def generer(tmp, *args):
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable,
                        os.path.join(tmp, "outils_claude", "controle_renommage.py"),
                        "--generer-ancrages"] + list(args),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=300)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def registre(tmp):
    return lire(os.path.join(tmp, "outils_claude", "ancrages-renommage.json"))


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

    # ═══ L'ADMISSION : par ancrage, et non par chapitre ═════════════════════
    # Le motif du chapitre ne doit plus couvrir une occurrence neuve dans ce
    # chapitre. C'est la limite de gouvernance relevée par l'auteur le 2026-09-20.
    out.write("\n  — admission par ancrage —\n")
    REGISTRE = registre(tmp)

    # G-R5 : contrôle négatif — rien n'a changé, la génération est un no-op ───
    code, j = generer(tmp)
    verifier("G-R5", False, code, j)
    faits.append(("G-R5b", "OK" if registre(tmp) == REGISTRE else "MANQUÉ", 0))
    out.write("  %-5s %-6s le registre est inchangé (idempotence)\n"
              % ("G-R5b", faits[-1][1]))

    # G-R1 : une occurrence neuve dans un chapitre DÉJÀ déclaré ──────────────
    ecrire(F, INTACT + "\n\nPhrase neuve en voix propre : sans dette.\n")
    code, j = generer(tmp)
    verifier("G-R1", True, code, j)
    faits.append(("G-R1b", "OK" if registre(tmp) == REGISTRE else "MANQUÉ", 0))
    out.write("  %-5s %-6s le registre n'a pas été écrit\n" % ("G-R1b", faits[-1][1]))
    neuf = re.findall(r"(?m)^  ([0-9a-f]{16}) ", j)
    assert len(neuf) == 1, ("le refus doit nommer UN ancrage, pas %d" % len(neuf), j)
    NEUF = neuf[0]

    # G-R3 : un ancrage admis qui ne figure pas au relevé ────────────────────
    code, j = generer(tmp, "--admettre", "0" * 16, "--motif", "x")
    verifier("G-R3", True, code, j)

    # G-R2 : l'ancrage est bon, le motif manque ──────────────────────────────
    code, j = generer(tmp, "--admettre", NEUF)
    verifier("G-R2", True, code, j)

    # G-R4 : CONTRÔLE POSITIF — l'admission en règle passe, et le motif écrit
    # est celui qui a été donné, PAS celui du chapitre.
    PROPRE = "motif propre à cette occurrence, et non celui du chapitre"
    code, j = generer(tmp, "--admettre", NEUF, "--motif", PROPRE)
    verifier("G-R4", False, code, j)
    inscrit = [o for o in json.loads(registre(tmp)) if o["ancrage"] == NEUF]
    ok = len(inscrit) == 1 and inscrit[0].get("motif") == PROPRE
    faits.append(("G-R4b", "OK" if ok else "MANQUÉ", 0))
    out.write("  %-5s %-6s le motif inscrit est celui qui a été donné\n"
              % ("G-R4b", faits[-1][1]))
    code, j = controler(tmp)
    verifier("G-R4c", False, code, j)
    ecrire(os.path.join(tmp, "outils_claude", "ancrages-renommage.json"), REGISTRE)
    ecrire(F, INTACT)

    # G-R6 : une disparition seule n'exige aucune admission ──────────────────
    tete, c = coupe_corps(INTACT)
    i = c.lower().index("sans dette")
    ecrire(F, tete + c[:i] + NEUTRE + c[i + len("sans dette"):])
    code, j = generer(tmp)
    verifier("G-R6", False, code, j)
    ok = len(json.loads(registre(tmp))) == len(json.loads(REGISTRE)) - 1
    faits.append(("G-R6b", "OK" if ok else "MANQUÉ", 0))
    out.write("  %-5s %-6s le registre a perdu exactement une entrée\n"
              % ("G-R6b", faits[-1][1]))

    # ═══ LE PLAFOND : quatre ancrages par admission ═════════════════════════
    # Le motif partagé tient parce qu'il est un acte lisible d'un coup d'œil.
    # Au-delà de quatre il redevient un tampon — arbitrage de l'auteur, 2026-09-20.
    out.write("\n  — plafond d'admission —\n")
    ecrire(os.path.join(tmp, "outils_claude", "ancrages-renommage.json"), REGISTRE)

    def semer(n):
        """n occurrences neuves, aux contextes deux à deux distincts."""
        t = INTACT
        for k in range(n):
            t += "\n\nSabotage %d, %s : le corpus dirait ici sans dette.\n" % (k, "zeta" * (k + 1))
        ecrire(F, t)
        code, j = generer(tmp)
        assert code != 0, "les occurrences neuves auraient dû être refusées"
        vus = sorted(set(re.findall(r"(?m)^  ([0-9a-f]{16}) ", j)))
        assert len(vus) == n, ("%d ancrages distincts attendus, %d obtenus" % (n, len(vus)), j)
        return vus, j

    # G-R7 : cinq d'un coup — refusés, et POUR LA BONNE RAISON ───────────────
    cinq, refus = semer(5)
    assert "SÉPARÉMENT" in refus, ("le refus doit proposer de scinder le lot", refus)
    code, j = generer(tmp, "--admettre", ",".join(cinq), "--motif", "un motif pour cinq")
    verifier("G-R7", True, code, j)
    ok = "plafond" in j and registre(tmp) == REGISTRE
    faits.append(("G-R7b", "OK" if ok else "MANQUÉ", 0))
    out.write("  %-5s %-6s le refus nomme le plafond, registre intact\n"
              % ("G-R7b", faits[-1][1]))

    # G-R8 : CONTRÔLE POSITIF — quatre passent. Sans lui, un plafond de zéro
    # réussirait G-R7 et l'admission serait morte.
    quatre, _ = semer(4)
    code, j = generer(tmp, "--admettre", ",".join(quatre), "--motif",
                      "quatre dettes `a_requalifier` de même nature")
    verifier("G-R8", False, code, j)
    ok = len(json.loads(registre(tmp))) == len(json.loads(REGISTRE)) + 4
    faits.append(("G-R8b", "OK" if ok else "MANQUÉ", 0))
    out.write("  %-5s %-6s le registre a gagné exactement quatre entrées\n"
              % ("G-R8b", faits[-1][1]))
    code, j = controler(tmp)
    verifier("G-R8c", False, code, j)

finally:
    shutil.rmtree(tmp, ignore_errors=True)

rates = [f for f in faits if f[1] != "OK"]
out.write("\n%d contrôle(s), %d manqué(s).\n" % (len(faits), len(rates)))
if rates:
    out.write("ÉCHEC : %s\n" % ", ".join(f[0] for f in rates))
    sys.exit(1)
out.write("Le contrôle détecte la substitution à total constant, laisse passer ce qui ne\n")
out.write("touche à aucune occurrence déclarée, et n'admet une occurrence neuve que\n")
out.write("nommée par son ancrage, avec son propre motif, et par lots de quatre au plus.\n")
