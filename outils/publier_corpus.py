"""Écrit les pages du corpus dans l'arbre, sous ``corpus/``, et nomme les périmées.

POURQUOI CE SCRIPT EXISTE. Depuis la décision L2 du 2026-09-25, la sortie du
générateur est VERSIONNÉE : elle voyage vers ``main`` dans une PR ordinaire, et
le site la sert sous ``/corpus/``. Une sortie versionnée ne se comporte pas
comme une sortie jetable.

LE DANGER QU'IL TRAITE. ``corpus/generer.py`` n'efface rien : il écrit fichier
par fichier avec ``exist_ok=True``. C'était sans effet tant que la sortie
partait dans un dossier neuf. Ce ne l'est plus : **un chapitre qui perd
``citable`` garde sa page**, et le site continue de la servir. La porte du § 13
se refermerait sans fermer la page.

IL NE SUPPRIME RIEN PAR DÉFAUT, et c'est délibéré : effacer à l'intérieur du
dossier qui porte les 335 chapitres est l'opération qui mérite le plus de
prudence. Il nomme les fichiers périmés ; ``--retirer`` les retire, et
seulement eux.

CE QU'IL NE PEUT PAS CONFONDRE. Un livre SOURCE est ``livre-01-un-slug`` ; un
livre ÉMIS est ``livre-1``, chiffres seuls. Le script n'accepte comme chemin
émis que la seconde forme et les sept fichiers nommés ci-dessous. Une source ne
peut donc pas y entrer, même par erreur d'appel.

    python outils/publier_corpus.py              # écrit, et nomme les périmées
    python outils/publier_corpus.py --retirer    # retire aussi les périmées
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
CORPUS = RACINE / "corpus"
# Les sept fichiers que le generateur pose a la racine de sa sortie.
FICHIERS_EMIS = {"index.html", "index.json", "glossaire.html", "glossaire.json",
                 "diagnostic.html", "llms.txt", "sitemap.xml"}
# Un livre EMIS : chiffres seuls. `livre-01-monnaie-...` ne peut pas correspondre.
LIVRE_EMIS = re.compile(r"^livre-\d+$")


def chemins_emis() -> list[Path]:
    """Tout ce qui, dans ``corpus/``, appartient à la sortie du générateur."""
    out = [CORPUS / n for n in FICHIERS_EMIS if (CORPUS / n).exists()]
    for d in CORPUS.iterdir():
        if d.is_dir() and LIVRE_EMIS.match(d.name):
            out.extend(p for p in d.rglob("*") if p.is_file())
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Écrit les pages du corpus dans l'arbre.")
    p.add_argument("--retirer", action="store_true",
                   help="retire les fichiers émis autrefois et plus aujourd'hui")
    a = p.parse_args()

    # Le controle structurel d'abord : l'autorite reste `controle.py`.
    r = subprocess.run([sys.executable, "corpus/controle.py"], cwd=RACINE)
    if r.returncode:
        raise SystemExit(r.returncode)

    # Le repere : tout fichier emis dont la date precede ce point n'a pas ete
    # reecrit, donc n'est plus emis. On attend une seconde pour que la
    # resolution de l'horodatage ne puisse pas confondre les deux.
    avant = set(chemins_emis())
    time.sleep(1.1)
    repere = time.time()

    r = subprocess.run([sys.executable, "corpus/generer.py", "--sortie",
                        str(CORPUS), "--base", "/corpus"], cwd=RACINE)
    if r.returncode:
        raise SystemExit(r.returncode)

    apres = set(chemins_emis())
    perimes = sorted(p for p in (avant | apres) if p.stat().st_mtime < repere)

    print()
    if not perimes:
        print("Aucune page périmée : tout ce qui est là vient d'être émis.")
        return 0

    print("PAGES PÉRIMÉES — émises autrefois, plus aujourd'hui  [%d]" % len(perimes))
    for chemin in perimes:
        print("    %s" % chemin.relative_to(RACINE).as_posix())
    if not a.retirer:
        print("\nRien n'est retiré. `--retirer` les retire, et seulement elles.")
        return 1

    for chemin in perimes:
        # Ceinture et bretelles : on re-verifie que chaque chemin est bien emis.
        rel = chemin.relative_to(CORPUS).parts
        assert (len(rel) == 1 and rel[0] in FICHIERS_EMIS) or LIVRE_EMIS.match(rel[0]), \
            "chemin hors de la sortie du générateur : %s" % chemin
        chemin.unlink()

    # Le dossier du chapitre reste, vide. Git ne suit pas les dossiers vides,
    # donc rien n'apparaitrait ; mais un dossier fantome dans `corpus/` est
    # precisement ce qu'on ne veut pas y laisser.
    vides = 0
    for d in sorted(CORPUS.glob("livre-*/*"), key=lambda p: -len(p.parts)):
        if d.is_dir() and LIVRE_EMIS.match(d.parent.name) and not any(d.iterdir()):
            d.rmdir()
            vides += 1
    print("\n%d page(s) retirée(s), %d dossier(s) vide(s)." % (len(perimes), vides))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
