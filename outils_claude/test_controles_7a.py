# -*- coding: utf-8 -*-
"""Sabotages des trois contrôles de la file 7a. Sur copies, jamais sur le dépôt.

Un contrôle qui passe sur un corpus intact ne prouve rien : il faut lui faire
subir l'attaque qu'il prétend détecter. **Et un contrôle qui crierait toujours
obtiendrait un sans-faute** : d'où les contrôles négatifs, marqués N, qui
doivent rester MUETS. Ce sont eux qui ont manqué à la première écriture des
trois outils, et chacun d'eux a rendu des défauts qui n'en étaient pas.

ANCRES — `controle_ancres.py`

  E-A1  « L9.C02 § 7 » quand le chapitre cible s'arrête au § 2
  E-A2  « L9.C44 § 1 » — chapitre inexistant
  N-A1  corpus intact                              — doit rester MUET
  N-A2  « IPSAS 51 § 10 » : paragraphe d'une norme — doit rester MUET
  N-A3  « [S10, section 4.3.6, § 58] »             — doit rester MUET

COMPTEURS — `controle_compteurs.py`

  E-C1  « dix-neuf sont arbitrées » quand la référence en rend dix-sept
  E-C2  « quarante-six sont ouvertes ou orientées » contre quarante-huit
  N-C1  compteur JUSTE, écrit en toutes lettres    — doit rester MUET
  N-C2  « dix-huit pays classés IDA »              — doit rester MUET
  N-C3  « un arbitrage ouvert » — article, non nombre — doit rester MUET
  G-C1  la référence est LUE dans controle.py, jamais recalculée : si ce
        contrôle-là ne rend rien, l'outil sort en 2 et n'invente pas de chiffre

CHIFFRES — `controle_chiffres.py`

  E-F1  fait chiffré sous `::etat::` sans appel  -> defaut_potentiel
  R-F1  même fait sous `::hypothese::`           -> a_relire, ET NON un défaut
  N-F1  appel placé APRÈS le point, comme le corpus l'écrit — doit être MUET
  N-F2  millésime « en 1971 »                                — MUET
  N-F3  numéros de page dans « [S1, p. 393-394, 408-409] »    — MUET
  N-F4  quantième « le 13 septembre 2023 »                    — MUET
  N-F5  renvoi « L9.C02 § 2 »                                 — MUET
  N-F6  identifiant « IPSAS 47 »                              — MUET

    python outils_claude/test_controles_7a.py
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

OUTILS = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = ("controle_ancres.py", "controle_compteurs.py", "controle_chiffres.py")

EN_TETE = """---
chapitre: {cid}
titre: "{titre}"
livre: 9
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-20
autorite: preparatoire
citable: false
regime: {regime}
sources_primaires: []
verifications_en_attente: []
resume: "Fixture."
concepts: []
renvois: []
---
"""

# Le faux controle.py : il ne fait qu'imprimer la ligne de reference, ce qui
# prouve que l'outil LIT ce decompte au lieu de le recalculer de son cote.
FAUX_CONTROLE = (
    "# -*- coding: utf-8 -*-\n"
    "import io, sys\n"
    "out = io.open(sys.stdout.fileno(), 'w', encoding='utf-8', closefd=False)\n"
    "out.write('  17 arbitr\\u00e9(s) \\u2014 dont 15 par l\\'auteur et 2 par le corpus ; "
    "48 ouvert(s) ou orient\\u00e9(s).\\n')\n"
    "out.flush()\n")

CONTROLE_MUET = ("# -*- coding: utf-8 -*-\n"
                 "print('aucune ligne de d\\u00e9compte ici')\n")


def atelier(chapitres, controle=FAUX_CONTROLE):
    """Monte un dépôt jetable : outils + faux controle.py + chapitres."""
    d = tempfile.mkdtemp(prefix="test7a-")
    os.makedirs(os.path.join(d, "outils_claude"))
    os.makedirs(os.path.join(d, "corpus", "livre-09-essais"))
    for s in SCRIPTS:
        shutil.copy(os.path.join(OUTILS, s), os.path.join(d, "outils_claude", s))
    io.open(os.path.join(d, "corpus", "controle.py"), "w",
            encoding="utf-8", newline="\n").write(controle)
    for nom, (cid, titre, regime, corps) in chapitres.items():
        io.open(os.path.join(d, "corpus", "livre-09-essais", nom), "w",
                encoding="utf-8", newline="\n").write(
            EN_TETE.format(cid=cid, titre=titre, regime=regime) + "\n" + corps + "\n")
    return d


def lancer(d, script, *args):
    r = subprocess.run([sys.executable, os.path.join(d, "outils_claude", script),
                        "--livre", "9"] + list(args),
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=d)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


BASE = {"c02-beta.md": ("L9.C02", "Beta", "hybride",
                        "## 1. Premier\n\nTexte.\n\n## 2. Second\n\nTexte.\n")}


def ch(corps, regime="hybride"):
    d = dict(BASE)
    d["c01-alpha.md"] = ("L9.C01", "Alpha", regime,
                         "## 1. Premier\n\nTexte neutre.\n\n## 2. Second\n\n" + corps + "\n")
    return d


def main():
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    ok = fail = 0

    def verifie(code, attendu, sortie, libelle, motif=None):
        nonlocal ok, fail
        bon = (code == attendu) and (motif is None or re.search(motif, sortie))
        out.write("  %-5s %-58s %s\n" % (code == attendu and "ok" or "ÉCHEC",
                                         libelle, "" if bon else "<<<"))
        if bon:
            ok += 1
        else:
            fail += 1
            if motif and code == attendu:
                out.write("        motif attendu absent : %s\n" % motif)
        return bon

    # ---------------------------------------------------------------- ANCRES
    out.write("\nANCRES\n")
    cas = [
        ("E-A1", "Le point est traité en L9.C02 § 7.", 1, "n'a pas de § 7"),
        ("E-A2", "Voir L9.C44 § 1 pour le détail.", 1, "chapitre inexistant"),
        ("N-A1", "Aucun renvoi ici.", 0, None),
        ("N-A2", "La condition est posée par IPSAS 51 § 10, lue au texte.", 0, None),
        ("N-A3", "Elle est reprise [S10, section 4.3.6, § 58] sans réserve.", 0, None),
    ]
    for code, corps, attendu, motif in cas:
        d = atelier(ch(corps))
        try:
            c, s = lancer(d, "controle_ancres.py")
            verifie(c, attendu, s, "%s  %s" % (code, corps[:46]), motif)
        finally:
            shutil.rmtree(d, ignore_errors=True)

    # ------------------------------------------------------------- COMPTEURS
    out.write("\nCOMPTEURS\n")
    cas = [
        ("E-C1", "Au registre, dix-neuf sont arbitrées à ce jour.", 1, "17"),
        ("E-C2", "Et quarante-six sont ouvertes ou orientées.", 1, "48"),
        ("N-C1", "Au registre, dix-sept sont arbitrées et quarante-huit "
                 "sont ouvertes ou orientées.", 0, None),
        ("N-C2", "Dix-huit pays classés IDA ont reçu des prêts d'ajustement.", 0, None),
        ("N-C3", "Le corpus a enregistré un arbitrage ouvert sur ce point.", 0, None),
    ]
    for code, corps, attendu, motif in cas:
        d = atelier(ch(corps))
        try:
            c, s = lancer(d, "controle_compteurs.py")
            verifie(c, attendu, s, "%s  %s" % (code, corps[:46]), motif)
        finally:
            shutil.rmtree(d, ignore_errors=True)

    d = atelier(ch("Texte neutre."), controle=CONTROLE_MUET)
    try:
        c, s = lancer(d, "controle_compteurs.py")
        verifie(c, 2, s, "G-C1  référence illisible : sortie 2, aucun chiffre inventé",
                "ne recalcule jamais")
    finally:
        shutil.rmtree(d, ignore_errors=True)

    # --------------------------------------------------------------- CHIFFRES
    out.write("\nCHIFFRES\n")
    cas = [
        ("E-F1", "::etat:: La part atteint 37 % du total.", "hybride", 1,
         "defaut_potentiel"),
        ("N-F1", "::etat:: La part atteint 37 % du total. [S1]", "hybride", 0, None),
        ("N-F2", "::etat:: La convertibilité a cessé en 1971.", "hybride", 0, None),
        ("N-F3", "::etat:: Le point est repris [S1, p. 393-394, 408-409].", "hybride",
         0, None),
        ("N-F4", "::etat:: La mise à jour du 13 septembre 2023 le confirme. [S1]",
         "hybride", 0, None),
        ("N-F5", "::etat:: Le mécanisme est exposé en L9.C02 § 2.", "hybride", 0, None),
        ("N-F6", "::etat:: La condition vient d'IPSAS 47 et de BPM6.", "hybride",
         0, None),
    ]
    for code, corps, regime, attendu, motif in cas:
        d = atelier(ch(corps, regime))
        try:
            c, s = lancer(d, "controle_chiffres.py")
            verifie(c, attendu, s, "%s  %s" % (code, corps[:46]), motif)
        finally:
            shutil.rmtree(d, ignore_errors=True)

    # R-F1 : le même fait sous ::hypothese:: n'est PAS un défaut, mais il est vu.
    d = atelier(ch("::hypothese:: La part atteindrait 37 % du total."))
    try:
        c, s = lancer(d, "controle_chiffres.py", "--tout")
        vu = bool(re.search(r"a_relire\s+1", s)) and bool(
            re.search(r"defaut_potentiel\s+0", s))
        out.write("  %-5s %-58s %s\n" % ("ok" if vu else "ÉCHEC",
                                         "R-F1  ::hypothese:: -> a_relire, et non un défaut",
                                         "" if vu else "<<<"))
        ok, fail = (ok + 1, fail) if vu else (ok, fail + 1)
    finally:
        shutil.rmtree(d, ignore_errors=True)

    out.write("\n%d contrôle(s) passé(s), %d échec(s).\n" % (ok, fail))
    if not fail:
        out.write("Les trois outils détectent ce qu'ils annoncent, et restent muets\n"
                  "sur les millésimes, les appels, les pages, les renvois et les\n"
                  "identifiants — ce qu'aucun d'eux ne faisait à sa première écriture.\n")
    out.flush()
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
