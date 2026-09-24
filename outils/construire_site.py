"""Assemble une prévisualisation locale du site et du corpus public.

La sortie est toujours ``build/`` et n'est pas versionnée. Les sources du
corpus ne sont jamais copiées dans cette sortie : seul ``corpus/generer.py`` y
émet les chapitres publiables sous ``/corpus/``.

Usage :
    python outils/construire_site.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


RACINE = Path(__file__).resolve().parents[1]
SORTIE = RACINE / "build"
TEMPORAIRE = RACINE / ".build-en-cours"
# `.build-env` est ignoré par git, donc absent du dépôt, et pèse 15 Mo :
# sans cette ligne il entrerait dans la construction, et de là dans ce qui
# serait publié. Les autres pièces de la racine qui ne sont pas du site —
# le plan directeur en PDF, le plan des livres en XLSX — sont déjà suivies
# par git : les copier ne divulgue rien, et leur sort est éditorial.
EXCLUS = {
    ".git", ".claude", "build", ".build-en-cours", ".build-env", "corpus",
    "coordination", "protocoles", "outils", "outils_claude", "Codex", "tmp",
    "__pycache__",
}


def ignorer(dossier: str, noms: list[str]) -> set[str]:
    """Ne copie ni les sources, ni les outils, ni les notes privées."""
    rejetes = {nom for nom in noms if nom in EXCLUS or nom.endswith((".md", ".pyc"))}
    if Path(dossier).resolve() == RACINE:
        rejetes.update({"AGENTS.md", "CLAUDE.md", "GUIDE-PUBLIER-CONTENU.md",
                         "INTEGRATION-ASSISTANT.md", "KNOWLEDGE-BASE.md"})
    return rejetes


def lancer(*commande: str) -> None:
    resultat = subprocess.run(commande, cwd=RACINE, text=True)
    if resultat.returncode:
        raise SystemExit(resultat.returncode)


def fusionner_sitemaps(site: Path, corpus: Path) -> None:
    """Ajoute les URL générées sans réécrire les URL déjà servies du site.

    DÉFAUT CONNU, NON CORRIGÉ ICI — constaté le 2026-09-24. Le ``sitemap.xml``
    de la racine déclare ``https://www.sitemaps.org/...`` (avec un s, hors
    norme) et le générateur émet le ``http://`` officiel. ``espace`` ci-dessous
    suppose ``http://`` pour les deux : ``existantes`` se réduit donc à
    ``{None}``, le dédoublonnage ne dédoublonne rien, et le fichier produit
    mélange les deux espaces sous une racine non standard — un analyseur de
    sitemap n'y lirait aucune URL du corpus. Trancher quel espace fait foi
    touche le fichier servi depuis ``main`` : c'est une décision d'auteur.
    """
    cible = site / "sitemap.xml"
    genere = corpus / "sitemap.xml"
    if not cible.exists() or not genere.exists():
        raise SystemExit("Sitemap absent : construction interrompue.")

    arbre_site = ET.parse(cible)
    racine_site = arbre_site.getroot()
    arbre_corpus = ET.parse(genere)
    espace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    existantes = {element.findtext(espace + "loc") for element in racine_site}
    for entree in arbre_corpus.getroot():
        loc = entree.findtext(espace + "loc")
        if loc not in existantes:
            racine_site.append(entree)
            existantes.add(loc)
    ET.indent(arbre_site, space="  ")
    arbre_site.write(cible, encoding="utf-8", xml_declaration=True)


def main() -> int:
    # Le contrôle structurel doit passer. Les chapitres non publiables ne sont
    # pas une erreur : le générateur les écarte lui-même selon la convention.
    lancer(sys.executable, "corpus/controle.py")

    if TEMPORAIRE.exists():
        shutil.rmtree(TEMPORAIRE)
    shutil.copytree(RACINE, TEMPORAIRE, ignore=ignorer)

    etape_corpus = TEMPORAIRE / ".corpus-en-cours"
    lancer(sys.executable, "corpus/generer.py", "--sortie", str(etape_corpus), "--base", "/corpus")
    destination = TEMPORAIRE / "corpus"
    shutil.move(str(etape_corpus), destination)
    fusionner_sitemaps(TEMPORAIRE, destination)

    if SORTIE.exists():
        shutil.rmtree(SORTIE)
    TEMPORAIRE.rename(SORTIE)
    print(f"Construction prête : {SORTIE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
