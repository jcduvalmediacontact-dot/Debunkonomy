#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Squelette de chapitre du corpus Debunk'Onomy à partir d'une source brute.

Le convertisseur ne remplit que ce qui peut être calculé : identifiants, chemin
de fichier, en-tête minimal valide, insertion du texte source. Tout le reste —
sources primaires, concepts, résumé, renvois, découpage, balises de régime,
choix des passages à retenir — reste à la charge de l'auteur. C'est délibéré :
la convention § 1 dit que l'auteur déclare les jugements, le script calcule le
reste, et ces champs sont des jugements.

Sources acceptées :
    .odt (OpenDocument), .md, .txt.

Usage :
    python convertir.py --source ep07.odt \\
                        --chapitre L1.C07 \\
                        --titre "Comment les banques créent vraiment la monnaie"

Options :
    --regime {descriptif,hybride,conception}   défaut : hybride
    --statut {brouillon,...}                   défaut : brouillon
    --autorite {canonique,preparatoire}        défaut : preparatoire
    --citable {true,false}                     défaut : false
    --slug <slug>                              défaut : calculé du titre
    --force                                    autoriser l'écrasement

Le fichier est déposé dans corpus/livre-<n>/c<nn>-<slug>.md. Le convertisseur
refuse d'écraser un chapitre existant sauf --force.

Dépendance : PyYAML  (pip install pyyaml)
"""

import argparse
import io
import re
import sys
import unicodedata
import zipfile
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

RACINE = Path(__file__).resolve().parent
RE_ID = re.compile(r"^L(\d+)\.C(\d+)$")


# --- Extraction du texte ---------------------------------------------------

def texte_odt(chemin: Path) -> str:
    """Extrait le texte d'un .odt sans dépendance externe."""
    with zipfile.ZipFile(chemin) as z:
        xml = z.read("content.xml").decode("utf-8")
    xml = re.sub(r"</text:(?:p|h|list-item|list)[^>]*>", "\n", xml)
    xml = re.sub(r"<text:tab\s*/>", "\t", xml)
    xml = re.sub(r"<text:line-break\s*/>", "\n", xml)
    xml = re.sub(r"<text:s\s+text:c=\"(\d+)\"\s*/>",
                 lambda m: " " * int(m.group(1)), xml)
    xml = re.sub(r"<text:s\s*/>", " ", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    xml = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), xml)
    for entite, valeur in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                            ("&apos;", "'"), ("&quot;", '"')):
        xml = xml.replace(entite, valeur)
    return re.sub(r"\n{3,}", "\n\n", xml).strip()


def texte_source(chemin: Path) -> str:
    suffixe = chemin.suffix.lower()
    if suffixe == ".odt":
        return texte_odt(chemin)
    if suffixe in (".md", ".txt"):
        return chemin.read_text(encoding="utf-8").strip()
    sys.exit(f"Extension non supportée : {suffixe} — .odt, .md, .txt uniquement")


# --- Identifiants et chemin ------------------------------------------------

def parse_chapitre(brut: str) -> tuple[int, int]:
    m = RE_ID.match(brut.strip())
    if not m:
        sys.exit(f"Identifiant invalide : « {brut} » — format attendu : L<n>.C<nn>")
    return int(m.group(1)), int(m.group(2))


def slug_de(titre: str) -> str:
    """kebab-case ASCII, adapté à un nom de fichier stable."""
    normalise = unicodedata.normalize("NFKD", titre)
    ascii_ = "".join(c for c in normalise if not unicodedata.combining(c))
    ascii_ = ascii_.lower()
    ascii_ = re.sub(r"[^a-z0-9]+", "-", ascii_).strip("-")
    return ascii_ or "chapitre"


def chemin_cible(livre: int, chapitre: int, slug: str) -> Path:
    return RACINE / f"livre-{livre:02d}" / f"c{chapitre:02d}-{slug}.md"


# --- Rendu de l'en-tête ----------------------------------------------------

# Rendu manuel pour deux raisons :
# - yaml.dump réordonne les clés et casse la lisibilité pensée pour l'auteur ;
# - la convention est explicite sur la forme des blocs, pas seulement la
#   sémantique. Un en-tête produit à la main respecte cette forme.

ENTETE = """\
---
chapitre: {chapitre}
titre: "{titre}"
livre: {livre}
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: {statut}
revision_de_fond: {date}
autorite: {autorite}
citable: {citable}
regime: {regime}
sources_primaires: []
verifications_en_attente:
  - "À COMPLÉTER — sources primaires à établir"
  - "À COMPLÉTER — concepts à extraire et à ajouter au vocabulaire s'ils manquent"
  - "À COMPLÉTER — renvois croisés vers les autres chapitres"
  - "À COMPLÉTER — balises ::hypothese:: ::etat:: ::norme:: à poser sur les passages qui s'écartent du régime déclaré"
resume: "À COMPLÉTER — 2 à 4 phrases énonçant ce que le chapitre établit."
concepts: []
renvois: []
---
"""


def entete(args, chapitre_court: int, livre: int) -> str:
    return ENTETE.format(
        chapitre=args.chapitre,
        titre=args.titre.replace('"', '\\"'),
        livre=livre,
        statut=args.statut,
        date=date.today().isoformat(),
        autorite=args.autorite,
        citable="true" if args.citable == "true" else "false",
        regime=args.regime,
    )


# --- Programme principal ---------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True, help="Fichier source (.odt, .md, .txt)")
    p.add_argument("--chapitre", required=True, help="Identifiant, ex. L1.C07")
    p.add_argument("--titre", required=True, help="Titre du chapitre")
    p.add_argument("--regime", default="hybride",
                   choices=["descriptif", "hybride", "conception"])
    p.add_argument("--statut", default="brouillon",
                   choices=["brouillon", "audit_contradictoire", "audit_factuel", "verifie"])
    p.add_argument("--autorite", default="preparatoire",
                   choices=["canonique", "preparatoire"])
    p.add_argument("--citable", default="false", choices=["true", "false"])
    p.add_argument("--slug", help="Slug de fichier (défaut : calculé du titre)")
    p.add_argument("--force", action="store_true",
                   help="Écraser un fichier existant")
    args = p.parse_args()

    source = Path(args.source)
    if not source.is_file():
        sys.exit(f"Source introuvable : {source}")

    livre, chapitre_court = parse_chapitre(args.chapitre)
    slug = args.slug or slug_de(args.titre)
    cible = chemin_cible(livre, chapitre_court, slug)

    if cible.exists() and not args.force:
        sys.exit(f"Refus : {cible.relative_to(RACINE)} existe déjà (utiliser --force)")

    cible.parent.mkdir(parents=True, exist_ok=True)
    corps = texte_source(source)
    contenu = entete(args, chapitre_court, livre) + "\n" + f"# {args.titre}\n\n" + corps + "\n"
    cible.write_text(contenu, encoding="utf-8")

    print(f"Écrit : {cible.relative_to(RACINE)}")
    print(f"  {len(corps.splitlines())} lignes de source insérées")
    print()
    print("Reste à la charge de l'auteur :")
    print("  - rédiger le resume (2 à 4 phrases)")
    print("  - renseigner sources_primaires et concepts")
    print("  - vérifier / restructurer le corps selon la convention")
    print("  - poser les renvois vers les autres chapitres")
    print("  - lancer :  python controle.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
