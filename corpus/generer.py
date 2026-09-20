#!/usr/bin/env python3
"""Générateur du § 13 de la convention.

Produit ce que le corpus publie, et rien d'autre : pages HTML des chapitres avec
JSON-LD, le `.md` servi à côté de chaque page, un index de recherche par livre,
l'index global léger, les tables des matières, le `sitemap.xml`, les entrées du
`llms.txt`, le glossaire tiré de `vocabulaire.yaml`, et la page de diagnostic en
trois sections.

DEUX RÈGLES QUI COMMANDENT TOUT CE FICHIER.

1. **Le générateur n'invente aucun jugement.** Il ne décide pas qu'un chapitre
   est bon : il lit ce que l'en-tête déclare et ce que `controle.py` a enregistré.
   Les empreintes viennent de `.etat-corpus.json`, jamais d'un calcul refait ici.

2. **Il n'émet un chapitre que si la convention l'autorise.** La règle du § 14,
   reprise du contrôle : statut `verifie`, `citable: true`, et toutes les sources
   à l'état `ouverte`. Tout le reste est compté, nommé, et laissé dehors.

L'autorité sur la validité reste `controle.py`. Ce script ne la contourne pas :
la page de diagnostic reproduit sa sortie telle quelle.

Usage :
    python corpus/generer.py                      # émet dans corpus/genere/
    python corpus/generer.py --sortie <dossier>   # ailleurs
    python corpus/generer.py --base /corpus       # préfixe des URL publiques
    python corpus/generer.py --brouillons         # inclut les non publiables
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent
ETAT = RACINE / ".etat-corpus.json"
LIVRES = RACINE / "livres.yaml"
VOCABULAIRE = RACINE / "vocabulaire.yaml"
CONTROLE = RACINE / "controle.py"

LICENCE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"
SITE = "https://debunkonomy.org"

REGIMES_LIBELLE = {
    "etat": ("état", "Ce paragraphe décrit un état de fait."),
    "hypothese": ("hypothèse", "Ce paragraphe défend une hypothèse du corpus."),
    "norme": ("norme", "Ce paragraphe énonce une prescription."),
}


# ─────────────────────────────────────────────────────────────────────────────
# Lecture
# ─────────────────────────────────────────────────────────────────────────────

class Chapitre:
    """Un chapitre lu sur le disque, sans jugement ajouté."""

    def __init__(self, chemin: Path, entete: dict, corps: str):
        self.chemin = chemin
        self.h = entete
        self.corps = corps
        self.id = str(entete["chapitre"])
        self.livre = int(entete["livre"])
        # § 3, révision 14 : l'URL ne dépend QUE de l'identifiant. Le nom de
        # fichier redevient libre, y compris après publication — c'est ce que
        # la convention promettait et que la dérivation depuis `chemin.stem`
        # contredisait. Un identifiant illisible refuse ici plutôt que de
        # produire une URL muette.
        m = re.fullmatch(r"L(\d+)\.C(\d+)", self.id)
        if not m:
            raise SystemExit(f"Identifiant impropre à porter une URL : "
                             f"« {self.id} » dans {chemin}")
        if int(m.group(1)) != self.livre:
            raise SystemExit(f"Identifiant et champ « livre » en désaccord : "
                             f"« {self.id} » contre livre {self.livre} dans {chemin}")
        self.slug = f"c{m.group(2)}"
        self.titre = str(entete.get("titre", "")).strip()

    @property
    def url(self) -> str:
        """URL publique, fixée au § 3 : /corpus/livre-6/c05/ — l'identifiant seul."""
        return f"livre-{self.livre}/{self.slug}/"

    @property
    def sources(self) -> list:
        return self.h.get("sources_primaires") or []

    def motifs_de_refus(self) -> list[str]:
        """Ce qui empêche la publication, dans les termes de la convention."""
        motifs = []
        if self.h.get("statut") != "verifie":
            motifs.append(f"statut « {self.h.get('statut')} » et non « verifie »")
        if self.h.get("citable") is not True:
            motifs.append("citable: false")
        fermees = [str(s.get("ref")) for s in self.sources
                   if s.get("etat_lecture") != "ouverte"]
        if fermees:
            motifs.append(f"{len(fermees)} source(s) non ouverte(s) : {', '.join(fermees)}")
        if not self.sources and self.h.get("type") != "synthese":
            motifs.append("aucune source primaire")
        return motifs


def lire_chapitres() -> list[Chapitre]:
    chapitres = []
    for chemin in sorted(RACINE.glob("livre-*/*.md")):
        texte = chemin.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", texte, re.S)
        if not m:
            raise SystemExit(f"En-tête illisible : {chemin}")
        entete = yaml.safe_load(m.group(1))
        if not isinstance(entete, dict) or "chapitre" not in entete:
            raise SystemExit(f"En-tête sans champ « chapitre » : {chemin}")
        chapitres.append(Chapitre(chemin, entete, m.group(2)))
    return chapitres


def lire_livres() -> dict[int, dict]:
    donnees = yaml.safe_load(LIVRES.read_text(encoding="utf-8")) or {}
    return {int(l["livre"]): l for l in donnees.get("livres", [])}


def lire_etat() -> dict:
    if not ETAT.exists():
        return {}
    return json.loads(ETAT.read_text(encoding="utf-8"))


def lire_vocabulaire() -> list[dict]:
    if not VOCABULAIRE.exists():
        return []
    d = yaml.safe_load(VOCABULAIRE.read_text(encoding="utf-8")) or []
    if isinstance(d, dict):                       # tolère les deux formes
        for cle in ("termes", "vocabulaire", "concepts"):
            if cle in d:
                d = d[cle]
                break
    return d if isinstance(d, list) else []


# ─────────────────────────────────────────────────────────────────────────────
# Rendu du Markdown — volontairement étroit
# ─────────────────────────────────────────────────────────────────────────────
#
# Le corpus n'emploie qu'un sous-ensemble arrêté de Markdown : titres, gras,
# italique, listes, tableaux, liens, appels [S1], marqueurs de régime en tête de
# paragraphe, et métaphores « (*Image : ...*) ». Le rendu échappe TOUT d'abord,
# puis n'applique que ces transformations-là. Un rendu généreux corromprait des
# citations ; celui-ci refuse ce qu'il ne reconnaît pas et le laisse en clair.

def _inline(texte: str, appels: bool = True) -> str:
    """Rendu des marques de niveau ligne.

    `appels` commande la transformation des `[Sn]` en liens vers la fiche de la
    source. Elle est DÉSACTIVÉE dans les fiches elles-mêmes : une entrée de
    source cite couramment le matricule d'une source d'un AUTRE chapitre —
    « ouverte par versement depuis L1.C12 [S6] » — et un lien y pointerait vers
    une ancre de la page courante, qui désigne autre chose ou n'existe pas.
    """
    t = html.escape(texte, quote=False)
    # liens Markdown, avant les appels de source pour ne pas manger leurs crochets
    t = re.sub(r"\[([^\]\[]+)\]\((https?://[^)\s]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2), quote=True)}" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    if appels:
        # appels de source : ancre vers la fiche de la source, en bas de page
        t = re.sub(r"\[(S\d+)\]",
                   lambda m: f'<a class="ref" href="#{m.group(1).lower()}">[{m.group(1)}]</a>', t)
    return t


def _marqueur(texte: str) -> tuple[str, str, str]:
    """Détache un marqueur de régime en tête de texte.

    Renvoie (classe, étiquette HTML, reste). Les marqueurs ne se trouvent pas
    seulement en tête de paragraphe : dans une liste numérotée, chaque item
    porte le sien.
    """
    m = re.match(r"^::(etat|hypothese|norme)::\s*(.*)$", texte, re.S)
    if not m:
        return "", "", texte
    cle, reste = m.group(1), m.group(2)
    libelle, infobulle = REGIMES_LIBELLE[cle]
    etiquette = (f'<span class="marqueur" title="{html.escape(infobulle, quote=True)}">'
                 f"{libelle}</span> ")
    return f"regime regime-{cle}", etiquette, reste


def _tableau(lignes: list[str]) -> str:
    rangs = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lignes]
    rangs = [r for r in rangs if not all(re.fullmatch(r":?-{2,}:?", c or "") for c in r)]
    if not rangs:
        return ""
    out = ["<table>", "<thead><tr>"]
    out += [f"<th>{_inline(c)}</th>" for c in rangs[0]]
    out.append("</tr></thead><tbody>")
    for r in rangs[1:]:
        out.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def corps_vers_html(corps: str) -> str:
    morceaux = []
    for bloc in re.split(r"\n\s*\n", corps.strip()):
        bloc = bloc.strip("\n")
        if not bloc.strip():
            continue
        lignes = bloc.split("\n")

        if all(l.lstrip().startswith("|") for l in lignes if l.strip()):
            morceaux.append(_tableau([l for l in lignes if l.strip()]))
            continue

        def _items(motif: str) -> str:
            rendus = []
            for l in lignes:
                if not l.strip():
                    continue
                classe, etiquette, reste = _marqueur(re.sub(motif, "", l).strip())
                attribut = f' class="{classe}"' if classe else ""
                rendus.append(f"<li{attribut}>{etiquette}{_inline(reste)}</li>")
            return "".join(rendus)

        if all(re.match(r"^\s*[-*]\s+", l) for l in lignes if l.strip()):
            morceaux.append(f"<ul>{_items(r'^\s*[-*]\s+')}</ul>")
            continue

        # liste numérotée : chaque item porte son propre marqueur de régime
        if all(re.match(r"^\s*\d+[.)]\s+", l) for l in lignes if l.strip()):
            depart = re.match(r"^\s*(\d+)", lignes[0]).group(1)
            attr = f' start="{depart}"' if depart != "1" else ""
            morceaux.append(f"<ol{attr}>{_items(r'^\s*\d+[.)]\s+')}</ol>")
            continue

        titre = re.match(r"^(#{1,4})\s+(.*)$", lignes[0])
        if titre and len(lignes) == 1:
            n = min(len(titre.group(1)) + 1, 6)      # le h1 de la page est le titre du chapitre
            texte = titre.group(2).strip()
            ancre = re.sub(r"[^a-z0-9]+", "-", texte.lower()).strip("-")[:60]
            morceaux.append(f'<h{n} id="{ancre}">{_inline(texte)}</h{n}>')
            continue

        plat = " ".join(l.strip() for l in lignes)

        image = re.match(r"^\(\*\s*(Image\s*:.*?)\*\)$", plat, re.S)
        if image:
            morceaux.append(
                '<aside class="metaphore" role="note">'
                f'<p>{_inline(image.group(1).strip())}</p></aside>')
            continue

        classe, etiquette, reste = _marqueur(plat)
        if classe:
            morceaux.append(f'<p class="{classe}">{etiquette}{_inline(reste)}</p>')
            continue

        morceaux.append(f"<p>{_inline(plat)}</p>")
    return "\n".join(morceaux)


# ─────────────────────────────────────────────────────────────────────────────
# Gabarit
# ─────────────────────────────────────────────────────────────────────────────

FEUILLE = """
:root{--encre:#16181d;--papier:#fffdf9;--trait:#ddd6ca;--doux:#6a6357;--lien:#7a3b2e}
@media(prefers-color-scheme:dark){:root{--encre:#e8e4dc;--papier:#16181d;--trait:#3a3b40;--doux:#9b958a;--lien:#d98b72}}
*{box-sizing:border-box}
body{margin:0;background:var(--papier);color:var(--encre);
 font:17px/1.65 Iowan Old Style,Palatino Linotype,Georgia,serif;
 -webkit-text-size-adjust:100%}
.enveloppe{max-width:44rem;margin:0 auto;padding:2.5rem 16px 5rem}
h1{font-size:1.9rem;line-height:1.2;margin:0 0 .4rem}
h2{font-size:1.3rem;margin:2.6rem 0 .8rem;padding-top:.6rem;border-top:1px solid var(--trait)}
h3{font-size:1.1rem;margin:1.8rem 0 .5rem}
a{color:var(--lien)}
.chapeau{color:var(--doux);font-size:.92rem;margin:0 0 2rem}
.chapeau code{font-size:.85rem}
.regime{position:relative}
.marqueur{display:inline-block;font:600 .68rem/1 ui-sans-serif,system-ui,sans-serif;
 text-transform:uppercase;letter-spacing:.06em;padding:.25em .5em;border-radius:3px;
 vertical-align:.12em;margin-right:.35em;cursor:help;white-space:nowrap}
.regime-etat .marqueur{background:#e7eef6;color:#2a4a6b}
.regime-hypothese .marqueur{background:#f5ead8;color:#7a5520}
.regime-norme .marqueur{background:#e8f0e6;color:#33562f}
@media(prefers-color-scheme:dark){
 .regime-etat .marqueur{background:#22354a;color:#bcd6f0}
 .regime-hypothese .marqueur{background:#45341c;color:#f0d6a8}
 .regime-norme .marqueur{background:#24391f;color:#c3e0bb}}
.metaphore{border-left:3px solid var(--trait);padding:.1rem 0 .1rem 1rem;margin:1.6rem 0;
 color:var(--doux);font-style:italic}
.ref{font-size:.82em;text-decoration:none;vertical-align:.25em}
table{border-collapse:collapse;width:100%;margin:1.4rem 0;font-size:.93rem}
th,td{border:1px solid var(--trait);padding:.45rem .6rem;text-align:left;vertical-align:top}
th{background:rgba(125,125,125,.08);font-weight:600}
.sources{margin-top:3.5rem;padding-top:1rem;border-top:2px solid var(--trait)}
.sources li{margin-bottom:1.1rem;font-size:.9rem}
.sources .ouverte{color:var(--doux)}
.pied{margin-top:4rem;padding-top:1rem;border-top:1px solid var(--trait);
 color:var(--doux);font-size:.85rem}
.liste-chap{list-style:none;padding:0}
.liste-chap li{padding:.55rem 0;border-bottom:1px solid var(--trait)}
.liste-chap .meta{color:var(--doux);font-size:.85rem}
.etiquette{display:inline-block;font:600 .66rem/1 ui-sans-serif,system-ui,sans-serif;
 text-transform:uppercase;letter-spacing:.05em;padding:.25em .5em;border-radius:3px;
 background:#e8f0e6;color:#33562f;margin-left:.4rem}
pre{white-space:pre-wrap;word-wrap:break-word;font-size:.78rem;line-height:1.45;
 background:rgba(125,125,125,.07);padding:1rem;border-radius:4px;overflow-x:auto}
@media(max-width:480px){body{font-size:16px}.enveloppe{padding:1.5rem 16px 4rem}h1{font-size:1.55rem}}
""".strip()


def page(titre: str, contenu: str, base: str, description: str = "",
         jsonld: dict | None = None, canonique: str = "") -> str:
    tete = [
        "<!doctype html>",
        '<html lang="fr">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        f"<title>{html.escape(titre)}</title>",
    ]
    if description:
        tete.append(f'<meta name="description" content="{html.escape(description[:300], quote=True)}">')
    if canonique:
        tete.append(f'<link rel="canonical" href="{html.escape(canonique, quote=True)}">')
    tete.append(f'<link rel="license" href="{LICENCE_URL}">')
    tete.append(f"<style>{FEUILLE}</style>")
    if jsonld:
        charge = json.dumps(jsonld, ensure_ascii=False, indent=1).replace("</", "<\\/")
        tete.append(f'<script type="application/ld+json">{charge}</script>')
    tete.append("</head><body><div class=enveloppe>")
    pied = (
        '<footer class="pied"><p>'
        f'<a href="{base}/">Corpus Debunk\'Onomy</a> — '
        f'<a href="{base}/glossaire.html">glossaire</a> — '
        f'<a href="{base}/diagnostic.html">diagnostic</a><br>'
        f'Publié sous <a href="{LICENCE_URL}" rel="license">CC BY-SA 4.0</a>. '
        "Page produite par <code>corpus/generer.py</code> : ne pas la modifier à la main."
        "</p></footer>"
    )
    return "\n".join(tete) + "\n" + contenu + pied + "</div></body></html>\n"


# ─────────────────────────────────────────────────────────────────────────────
# Émission
# ─────────────────────────────────────────────────────────────────────────────

def fiche_sources(ch: Chapitre) -> str:
    if not ch.sources:
        return ""
    items = []
    for s in ch.sources:
        ref = str(s.get("ref", "?"))
        # appels=False : une fiche cite couramment le matricule d'une source d'un
        # autre chapitre, et le lier pointerait vers la mauvaise ancre.
        texte = _inline(str(s.get("reference", "")).strip(), appels=False)
        url = s.get("url")
        lien = (f' <a href="{html.escape(str(url), quote=True)}" rel="noopener">source en ligne</a>'
                if url else "")
        etat = s.get("etat_lecture", "?")
        datee = s.get("date_verification")
        mention = f'<span class="ouverte">état de lecture : {html.escape(str(etat))}'
        mention += f", vérifiée le {html.escape(str(datee))}" if datee else ""
        mention += "</span>"
        items.append(f'<li id="{ref.lower()}"><strong>[{html.escape(ref)}]</strong> '
                     f"{texte}{lien}<br>{mention}</li>")
    return ('<section class="sources"><h2>Sources primaires</h2>'
            "<p>Chaque source porte l'édition sur laquelle elle a été lue et la date de sa "
            "vérification. Une source « ouverte » a été lue dans son texte, pas dans un résumé.</p>"
            "<ol>" + "".join(items) + "</ol></section>")


def jsonld_chapitre(ch: Chapitre, livre: dict, base: str, empreintes: dict) -> dict:
    d = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": ch.titre,
        "identifier": ch.id,
        "inLanguage": ch.h.get("langue", "fr"),
        "license": LICENCE_URL,
        "url": f"{SITE}{base}/{ch.url}",
        "abstract": str(ch.h.get("resume", "")).strip(),
        "publisher": {"@type": "Organization", "name": "Debunk'Onomy", "url": SITE},
        "isAccessibleForFree": True,
    }
    if ch.h.get("revision_de_fond"):
        d["dateModified"] = str(ch.h["revision_de_fond"])
    if livre:
        d["isPartOf"] = {"@type": "Book", "name": str(livre.get("titre", f"Livre {ch.livre}"))}
    mots = [str(c) for c in (ch.h.get("concepts") or [])]
    if mots:
        d["keywords"] = ", ".join(mots)
    citations = [str(s.get("reference", ""))[:300] for s in ch.sources]
    if citations:
        d["citation"] = citations
    return d


def chapeau(ch: Chapitre, livre: dict, empreintes: dict) -> str:
    bouts = [f"<strong>{html.escape(ch.id)}</strong>"]
    if livre:
        bouts.append(html.escape(str(livre.get("titre", ""))))
    bouts.append(f"statut : {html.escape(str(ch.h.get('statut')))}")
    bouts.append(f"autorité : {html.escape(str(ch.h.get('autorite')))}")
    bouts.append(f"révision de fond : {html.escape(str(ch.h.get('revision_de_fond')))}")
    bouts.append(f"{len(ch.sources)} source(s), toutes ouvertes")
    ligne = " · ".join(bouts)
    emp = ""
    if empreintes:
        emp = ("<br>empreintes enregistrées — éditoriale <code>"
               f"{html.escape(str(empreintes.get('editoriale', '?')))}</code>, métadonnées <code>"
               f"{html.escape(str(empreintes.get('metadonnees', '?')))}</code>")
    return f'<p class="chapeau">{ligne}{emp}</p>'


def emettre_chapitre(ch: Chapitre, livre: dict, base: str, etat: dict, sortie: Path) -> None:
    dossier = sortie / f"livre-{ch.livre}" / ch.slug
    dossier.mkdir(parents=True, exist_ok=True)
    empreintes = etat.get(ch.id, {})
    corps = ch.corps
    # le premier titre du corps répète le titre du chapitre : il devient le h1 de la page
    corps = re.sub(r"^#\s+.*?\n", "", corps.lstrip(), count=1)
    contenu = (
        f"<h1>{html.escape(ch.titre)}</h1>"
        + chapeau(ch, livre, empreintes)
        + corps_vers_html(corps)
        + fiche_sources(ch)
    )
    ecrire(dossier / "index.html",
           page(f"{ch.titre} — Corpus Debunk'Onomy", contenu, base,
                description=str(ch.h.get("resume", "")),
                jsonld=jsonld_chapitre(ch, livre, base, empreintes),
                canonique=f"{SITE}{base}/{ch.url}"))
    # le .md servi à côté de la page, à l'identique du dépôt
    ecrire(dossier / "index.md", ch.chemin.read_text(encoding="utf-8"))


def emettre_livre(num: int, livre: dict, chapitres: list[Chapitre], base: str,
                  sortie: Path) -> None:
    dossier = sortie / f"livre-{num}"
    dossier.mkdir(parents=True, exist_ok=True)
    titre = str(livre.get("titre", f"Livre {num}")) if livre else f"Livre {num}"
    items = []
    for ch in chapitres:
        items.append(
            f'<li><a href="{base}/{ch.url}">{html.escape(ch.titre)}</a>'
            f'<span class="etiquette">{html.escape(str(ch.h.get("autorite")))}</span>'
            f'<div class="meta">{html.escape(ch.id)} · {len(ch.sources)} source(s) · '
            f'révision de fond {html.escape(str(ch.h.get("revision_de_fond")))}</div>'
            f'<div class="meta">{html.escape(str(ch.h.get("resume", ""))[:260])}…</div></li>')
    contenu = (f"<h1>{html.escape(titre)}</h1>"
               f'<p class="chapeau">Table des matières · {len(chapitres)} chapitre(s) publié(s)</p>'
               + (str(livre.get("fonction", "")).strip() and
                  f"<p>{_inline(str(livre['fonction']).strip())}</p>" or "")
               + '<ul class="liste-chap">' + "".join(items) + "</ul>")
    ecrire(dossier / "index.html", page(f"{titre} — Corpus Debunk'Onomy", contenu, base,
                                        description=str(livre.get("fonction", ""))[:300] if livre else ""))
    # index de recherche propre au livre — un index unique deviendrait trop lourd (§ 13)
    recherche = [{
        "id": ch.id,
        "titre": ch.titre,
        "url": f"{base}/{ch.url}",
        "resume": str(ch.h.get("resume", "")),
        "concepts": [str(c) for c in (ch.h.get("concepts") or [])],
        "texte": re.sub(r"\s+", " ", re.sub(r"::(etat|hypothese|norme)::", " ", ch.corps)).strip(),
    } for ch in chapitres]
    ecrire(dossier / "recherche.json",
           json.dumps({"livre": num, "titre": titre, "chapitres": recherche},
                      ensure_ascii=False, indent=1))


def emettre_index(par_livre: dict, livres: dict, base: str, sortie: Path,
                  refuses: list[tuple[Chapitre, list[str]]]) -> None:
    total = sum(len(v) for v in par_livre.values())
    blocs = []
    for num in sorted(par_livre):
        livre = livres.get(num, {})
        titre = str(livre.get("titre", f"Livre {num}"))
        liens = "".join(
            f'<li><a href="{base}/{ch.url}">{html.escape(ch.titre)}</a> '
            f'<span class="meta">{html.escape(ch.id)}</span></li>'
            for ch in par_livre[num])
        blocs.append(f'<h2><a href="{base}/livre-{num}/">{html.escape(titre)}</a></h2>'
                     f'<ul class="liste-chap">{liens}</ul>')
    avertissement = (
        "<p>Ce corpus publie <strong>ce qu'il a vérifié, et cela seulement</strong>. "
        f"À ce jour, <strong>{total} chapitre(s)</strong> remplissent les trois conditions de "
        "publication : statut vérifié, autorité canonique, et toutes les sources lues dans leur "
        f"texte. <strong>{len(refuses)} autre(s) chapitre(s)</strong> existent dans le dépôt et "
        "ne sont pas publiés, parce qu'ils ne les remplissent pas encore. "
        f'Le <a href="{base}/diagnostic.html">diagnostic</a> dit lesquels et pourquoi.</p>')
    contenu = (f"<h1>Corpus Debunk'Onomy</h1>"
               f'<p class="chapeau">Index général · {total} chapitre(s) publié(s)</p>'
               + avertissement + "".join(blocs))
    ecrire(sortie / "index.html",
           page("Corpus Debunk'Onomy", contenu, base,
                description="Le corpus documentaire de Debunk'Onomy : ce qui a été vérifié, "
                            "source par source, et ce qui ne l'est pas encore."))
    # index global léger : identifiants, titres, résumés, concepts (§ 13)
    leger = [{
        "id": ch.id,
        "titre": ch.titre,
        "livre": ch.livre,
        "url": f"{base}/{ch.url}",
        "resume": str(ch.h.get("resume", "")),
        "concepts": [str(c) for c in (ch.h.get("concepts") or [])],
        "statut": ch.h.get("statut"),
        "autorite": ch.h.get("autorite"),
        "revision_de_fond": str(ch.h.get("revision_de_fond")),
        "sources": len(ch.sources),
    } for num in sorted(par_livre) for ch in par_livre[num]]
    ecrire(sortie / "index.json", json.dumps(
        {"genere_le": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
         "licence": LICENCE_URL, "publies": len(leger),
         "non_publies": len(refuses), "chapitres": leger},
        ensure_ascii=False, indent=1))


def emettre_glossaire(vocabulaire: list[dict], publies: set[str], base: str,
                      sortie: Path) -> int:
    if not vocabulaire:
        return 0
    lignes = []
    for terme in sorted(vocabulaire, key=lambda t: str(t.get("libelle") or t.get("terme", ""))):
        nom = str(terme.get("libelle") or terme.get("terme", "")).strip()
        definition = re.sub(r"\s+", " ", str(terme.get("definition", ""))).strip()
        origine = str(terme.get("premiere_occurrence", "")).strip()
        marque = " · publié" if origine in publies else ""
        lignes.append(f"<dt id=\"{re.sub(r'[^a-z0-9]+', '-', str(terme.get('terme', '')).lower())}\">"
                      f"{html.escape(nom)}</dt>"
                      f"<dd>{_inline(definition)}"
                      + (f'<div class="meta">première occurrence : {html.escape(origine)}{marque}</div>'
                         if origine else "")
                      + "</dd>")
    contenu = ("<h1>Glossaire</h1>"
               f'<p class="chapeau">{len(vocabulaire)} terme(s) · produit depuis '
               "<code>corpus/vocabulaire.yaml</code></p>"
               "<p>Chaque concept garde le même nom dans tout le corpus, et sa définition "
               "ne varie pas d'un chapitre à l'autre.</p>"
               "<dl>" + "".join(lignes) + "</dl>")
    ecrire(sortie / "glossaire.html", page("Glossaire — Corpus Debunk'Onomy", contenu, base,
                                           description="Le vocabulaire du corpus Debunk'Onomy."))
    ecrire(sortie / "glossaire.json", json.dumps(vocabulaire, ensure_ascii=False, indent=1))
    return len(vocabulaire)


def emettre_llms(par_livre: dict, livres: dict, base: str, sortie: Path,
                 refuses: list) -> None:
    """Les entrées du corpus pour le llms.txt (§ 13).

    Fichier à part : il n'écrase pas le `llms.txt` du site, qui est écrit à la
    main et décrit autre chose. C'est à l'auteur de décider comment les réunir.
    """
    total = sum(len(v) for v in par_livre.values())
    L = ["# Corpus Debunk'Onomy", "",
         "> Corpus documentaire sous licence CC BY-SA 4.0. Chaque chapitre publié ici a le "
         "statut « vérifié » : toutes ses sources ont été lues dans leur texte, leur édition "
         "est identifiée et datée. Les paragraphes portent un marqueur de régime — état, "
         "hypothèse, norme — qui dit si le texte décrit, défend ou prescrit.", "",
         f"Chapitres publiés : {total}. Chapitres du dépôt non encore publiables : {len(refuses)}. "
         "Le corpus ne publie que ce qu'il a vérifié ; l'absence d'un chapitre n'est pas un oubli.",
         ""]
    for num in sorted(par_livre):
        titre = str(livres.get(num, {}).get("titre", f"Livre {num}"))
        L.append(f"## {titre}")
        L.append("")
        for ch in par_livre[num]:
            resume = re.sub(r"\s+", " ", str(ch.h.get("resume", ""))).strip()
            L.append(f"- [{ch.titre}]({SITE}{base}/{ch.url}): {resume}")
        L.append("")
    L += ["## Ressources", "",
          f"- [Index général]({SITE}{base}/): la liste des chapitres publiés, par livre.",
          f"- [Index lisible par machine]({SITE}{base}/index.json): identifiants, titres, résumés, concepts.",
          f"- [Glossaire]({SITE}{base}/glossaire.html): le vocabulaire du corpus, un nom par concept.",
          f"- [Diagnostic]({SITE}{base}/diagnostic.html): ce qui bloque la publication des autres chapitres.",
          ""]
    ecrire(sortie / "llms.txt", "\n".join(L))


def emettre_sitemap(par_livre: dict, base: str, sortie: Path) -> None:
    aujourd = date.today().isoformat()
    urls = [f"{SITE}{base}/", f"{SITE}{base}/glossaire.html"]
    urls += [f"{SITE}{base}/livre-{n}/" for n in sorted(par_livre)]
    urls += [f"{SITE}{base}/{ch.url}" for n in sorted(par_livre) for ch in par_livre[n]]
    L = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
         '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
         "<!-- Équivalences de langue : le corpus n'existe qu'en français à ce jour ;",
         "     chaque URL ne porte donc qu'un hreflang, celui de sa propre version. -->"]
    for u in urls:
        L += [" <url>", f"  <loc>{html.escape(u, quote=True)}</loc>",
              f"  <lastmod>{aujourd}</lastmod>",
              f'  <xhtml:link rel="alternate" hreflang="fr" href="{html.escape(u, quote=True)}"/>',
              " </url>"]
    L.append("</urlset>")
    ecrire(sortie / "sitemap.xml", "\n".join(L) + "\n")


def emettre_diagnostic(refuses: list[tuple[Chapitre, list[str]]], base: str,
                       sortie: Path, sortie_controle: str) -> None:
    """Trois sections distinctes (§ 13). L'autorité reste controle.py."""
    rangs = "".join(
        f"<tr><td>{html.escape(ch.id)}</td><td>{html.escape(ch.titre)}</td>"
        f"<td>{html.escape(' ; '.join(motifs))}</td></tr>"
        for ch, motifs in refuses)
    contenu = (
        "<h1>Diagnostic</h1>"
        f'<p class="chapeau">Produit le {date.today().isoformat()} par '
        "<code>corpus/generer.py</code></p>"
        "<h2>1. Blocages — ce qui n'est pas publié, et pourquoi</h2>"
        f"<p>{len(refuses)} chapitre(s) du dépôt ne remplissent pas les trois conditions de "
        "publication : statut vérifié, <code>citable: true</code>, et toutes les sources à "
        "l'état « ouverte ». Le corpus les garde hors ligne plutôt que de les publier sous "
        "réserve.</p>"
        "<table><thead><tr><th>chapitre</th><th>titre</th><th>ce qui manque</th></tr></thead>"
        f"<tbody>{rangs}</tbody></table>"
        "<h2>2. Décisions en attente et alertes de fraîcheur</h2>"
        "<p>Ces deux sections sont produites par <code>corpus/controle.py</code>, qui fait "
        "autorité sur la validité du corpus. Sa sortie est reproduite ci-dessous "
        "<strong>telle quelle</strong> : ce générateur ne réimplémente pas ses règles et ne "
        "les interprète pas.</p>"
        f"<pre>{html.escape(sortie_controle)}</pre>"
        "<h2>3. Ce que ce diagnostic ne dit pas</h2>"
        "<p>Aucun statut n'atteste la justesse d'un raisonnement. Un chapitre vérifié est un "
        "chapitre dont les sources ont été lues, datées et identifiées ; ce n'est pas un "
        "chapitre dont la thèse est démontrée. Le nombre d'audits traversés ne prouve rien non "
        "plus, et le corpus se l'interdit comme argument.</p>")
    ecrire(sortie / "diagnostic.html",
           page("Diagnostic — Corpus Debunk'Onomy", contenu, base,
                description="Ce que le corpus ne publie pas, et pour quelle raison."))


# ─────────────────────────────────────────────────────────────────────────────

ECRITS: list[Path] = []


def ecrire(chemin: Path, contenu: str) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenu)
    ECRITS.append(chemin)


def main() -> int:
    ap = argparse.ArgumentParser(description="Générateur du § 13 de la convention du corpus.")
    ap.add_argument("--sortie", default=str(RACINE / "genere"),
                    help="dossier de sortie (défaut : corpus/genere)")
    ap.add_argument("--base", default="/corpus",
                    help="préfixe des URL publiques (défaut : /corpus)")
    ap.add_argument("--brouillons", action="store_true",
                    help="émet AUSSI les chapitres non publiables, pour relecture privée")
    args = ap.parse_args()

    sortie = Path(args.sortie).resolve()
    base = "/" + args.base.strip("/") if args.base.strip("/") else ""

    chapitres = lire_chapitres()
    livres = lire_livres()
    etat = lire_etat()
    vocabulaire = lire_vocabulaire()

    publies, refuses = [], []
    for ch in chapitres:
        motifs = ch.motifs_de_refus()
        if motifs and not args.brouillons:
            refuses.append((ch, motifs))
        else:
            publies.append(ch)
            if motifs:
                refuses.append((ch, motifs))

    if not publies:
        print("Aucun chapitre ne remplit les conditions de publication. Rien n'est écrit.")
        print("Conditions : statut « verifie », citable: true, toutes les sources « ouverte ».")
        return 1

    par_livre: dict[int, list[Chapitre]] = {}
    for ch in publies:
        par_livre.setdefault(ch.livre, []).append(ch)
    for num in par_livre:
        # tri numérique, et non lexicographique : « c100 » précéderait « c11 »
        par_livre[num].sort(key=lambda c: int(c.slug[1:]))

    for ch in publies:
        emettre_chapitre(ch, livres.get(ch.livre, {}), base, etat, sortie)
    for num, liste in par_livre.items():
        emettre_livre(num, livres.get(num, {}), liste, base, sortie)
    emettre_index(par_livre, livres, base, sortie, refuses)
    n_termes = emettre_glossaire(vocabulaire, {c.id for c in publies}, base, sortie)
    emettre_llms(par_livre, livres, base, sortie, refuses)
    emettre_sitemap(par_livre, base, sortie)

    r = subprocess.run([sys.executable, str(CONTROLE), "--publier"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    emettre_diagnostic(refuses, base, sortie, r.stdout.strip() or "(sortie vide)")

    print(f"Sortie : {sortie}")
    print(f"  {len(publies)} chapitre(s) publié(s), sur {len(chapitres)} dans le dépôt")
    print(f"  {len(par_livre)} livre(s) : " +
          ", ".join(f"livre {n} ({len(v)})" for n, v in sorted(par_livre.items())))
    print(f"  {n_termes} terme(s) au glossaire")
    print(f"  {len(ECRITS)} fichier(s) écrit(s)")
    print(f"  {len(refuses)} chapitre(s) non publiés, nommés dans diagnostic.html")
    if args.brouillons:
        print("  ATTENTION : --brouillons a émis des chapitres non publiables. "
              "Ne jamais servir cette sortie en public.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
