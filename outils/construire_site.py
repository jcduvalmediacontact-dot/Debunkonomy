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
# L'espace de noms officiel des sitemaps est en `http://`, sans s. Le fichier
# de la racine déclarait `https://` jusqu'au 2026-09-25 ; voir fusionner_sitemaps.
SITEMAP = "http://www.sitemaps.org/schemas/sitemap/0.9"
XHTML = "http://www.w3.org/1999/xhtml"
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


def espace_de(racine: ET.Element, quoi: str) -> str:
    """L'espace de noms que le fichier déclare, jamais celui qu'on espère."""
    if not racine.tag.startswith("{"):
        raise SystemExit(f"{quoi} : urlset sans espace de noms.")
    return racine.tag[1:racine.tag.index("}")]


def fusionner_sitemaps(site: Path, corpus: Path) -> None:
    """Ajoute les URL générées sans réécrire les URL déjà servies du site.

    L'espace de noms est LU dans chaque fichier et un écart entre les deux
    arrête la construction. Le 2026-09-24, la racine déclarait ``https://...``
    et le générateur ``http://`` : ``existantes`` se réduisait à ``{None}``, le
    dédoublonnage ne dédoublonnait rien, et la sortie mélangeait les deux
    espaces sous une racine non standard — un analyseur de sitemap n'y lisait
    aucune URL du corpus. **L'écart ne se voyait pas parce qu'il ne produisait
    aucune erreur** : ``findtext`` rend ``None`` au lieu de lever, et un ``set``
    accepte ``None`` sans broncher. D'où les trois refus ci-dessous.
    """
    cible = site / "sitemap.xml"
    genere = corpus / "sitemap.xml"
    if not cible.exists() or not genere.exists():
        raise SystemExit("Sitemap absent : construction interrompue.")

    arbre_site = ET.parse(cible)
    racine_site = arbre_site.getroot()
    racine_corpus = ET.parse(genere).getroot()

    du_site = espace_de(racine_site, "sitemap.xml du site")
    du_corpus = espace_de(racine_corpus, "sitemap.xml du corpus")
    if du_site != du_corpus:
        raise SystemExit(
            f"Espaces de noms différents — site « {du_site} », corpus "
            f"« {du_corpus} ». La fusion produirait un sitemap illisible.")
    if du_site != SITEMAP:
        raise SystemExit(
            f"Espace de noms hors norme : « {du_site} ». La norme est "
            f"« {SITEMAP} » ; un analyseur conforme ne lirait rien.")

    espace = "{%s}" % du_site
    ET.register_namespace("", du_site)
    ET.register_namespace("xhtml", XHTML)
    existantes = {element.findtext(espace + "loc") for element in racine_site}
    if None in existantes:
        # Le symptôme exact du 2026-09-24, resté muet ce jour-là.
        raise SystemExit("sitemap.xml du site : une entrée sans <loc>.")
    for entree in racine_corpus:
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
