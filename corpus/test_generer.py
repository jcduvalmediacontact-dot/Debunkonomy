#!/usr/bin/env python3
"""Contrôle de la sortie du générateur du § 13.

Ce test ne vérifie pas que `generer.py` s'exécute : il vérifie que ce qu'il
écrit tient. Il émet dans un dossier temporaire, jamais dans l'arbre du dépôt,
et il contrôle sept invariants.

1. Tout JSON produit est du JSON valide, JSON-LD des pages compris.
2. Le `sitemap.xml` est du XML valide, porte l'ensemble EXACT des URL attendues,
   et **aucun `lastmod`** : le corpus ne détient aucune date attestant la
   dernière modification significative d'une page, et le champ est facultatif.
   Jusqu'au 2026-09-28, les entrées portaient la date de génération ; le test ne
   lisait que la validité XML et laissait donc passer un fichier valide dont le
   contenu était faux. L'absence de date se contrôle avec l'ensemble des URL,
   sans quoi un fichier vidé de ses entrées passerait aussi.
3. Aucune marque Markdown ne subsiste en clair dans une page : ni marqueur de
   régime, ni gras, ni titre. Un rendu qui laisse passer `::etat::` ment sur le
   régime du paragraphe, ce qui est pire qu'une page laide.
4. Tout appel `[Sn]` transformé en lien pointe sur une fiche présente dans la
   même page. Les fiches de sources ne doivent PAS être liées : elles citent
   couramment le matricule d'une source d'un autre chapitre.
5. Le `.md` servi à côté d'une page est identique, octet pour octet, au fichier
   du dépôt.
6. L'ensemble émis est exactement l'ensemble publiable au sens de la convention.
7. Aucun chapitre non publiable n'a fui dans la sortie.

    python corpus/test_generer.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent
GENERER = RACINE / "generer.py"


def publiables() -> set[str]:
    """La règle de la convention, écrite ici une seule fois."""
    out = set()
    for chemin in RACINE.glob("livre-*/*.md"):
        m = re.match(r"^---\n(.*?)\n---\n", chemin.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        h = yaml.safe_load(m.group(1))
        srcs = h.get("sources_primaires") or []
        # Une synthèse n'ouvre pas de pièce : elle est dispensée de
        # `sources_primaires` depuis la révision 15 (§ 6). `generer.py`
        # l'exempte déjà ; cette règle-ci ne l'avait pas suivi.
        if (h.get("statut") == "verifie" and h.get("citable") is True
                and (srcs or h.get("type") == "synthese")
                and all(s.get("etat_lecture") == "ouverte" for s in srcs)):
            out.add(str(h["chapitre"]))
    return out


def controle_sitemap(texte: str, attendus: set[str]) -> list[str]:
    """2. XML valide, ensemble EXACT des URL, et aucun `lastmod`.

    Fonction séparée pour être appelable sur un sitemap saboté : un contrôle
    qu'on ne peut pas mettre en échec ne prouve rien. Une première version,
    écrite en ligne dans `main`, exigeait l'égalité de date pour les pages de
    chapitre et la simple appartenance à l'ensemble des dates pour les quatre
    agrégats — trois dates fausses y passaient sans erreur.

    L'absence de date et l'ensemble des URL se contrôlent ENSEMBLE : dire qu'un
    fichier ne porte aucune date ne prouve rien s'il a perdu ses entrées.
    """
    echecs = []
    try:
        racine = ET.fromstring(texte)
    except Exception as e:
        return [f"sitemap.xml invalide : {e}"]
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    if racine.find(f".//{ns}lastmod") is not None:
        echecs.append("sitemap.xml : un `lastmod` est apparu, alors qu'aucune "
                      "date de page n'est attestée")
    vus, agreges = set(), set()
    for bloc in racine.iter(f"{ns}url"):
        loc = bloc.findtext(f"{ns}loc") or ""
        m = re.search(r"/livre-(\d+)/(c\d+)/?$", loc)
        if m:
            vus.add(f"L{int(m.group(1))}.{m.group(2).upper()}")
        else:
            agreges.add(loc)
    if vus != attendus:
        echecs.append(f"sitemap.xml : chapitres {sorted(vus ^ attendus)} en "
                      f"écart avec l'ensemble publiable")
    # index général, glossaire, et une table par livre représenté
    livres = {c.split(".")[0] for c in attendus}
    if len(agreges) != 2 + len(livres):
        echecs.append(f"sitemap.xml : {len(agreges)} page(s) d'index, attendu "
                      f"{2 + len(livres)} — {sorted(agreges)}")
    return echecs


def sitemap_sur_collection_vide() -> list[str]:
    """2 (cas limite). Zéro chapitre publiable ne doit pas faire lever le sitemap.

    Le cas courant ne l'atteint jamais, et c'est ce qui le rend dangereux : une
    version datée du 2026-09-28 calculait le maximum des dates de chapitres pour
    les pages d'index, et levait `ValueError: max() iterable argument is empty`
    dès que la collection était vide — là où le code précédent écrivait ses URL
    d'index sans broncher. Le contrôle appelle donc la fonction directement,
    plutôt que d'espérer qu'un corpus vide se présente un jour.
    """
    from generer import emettre_sitemap

    echecs = []
    with tempfile.TemporaryDirectory(prefix="corpus-sitemap-vide-") as tmp:
        try:
            emettre_sitemap({}, "/corpus", Path(tmp))
        except Exception as e:
            echecs.append(f"sitemap sur collection vide : "
                          f"{type(e).__name__} : {e}")
            return echecs
        t = (Path(tmp) / "sitemap.xml").read_text(encoding="utf-8")
        if "<lastmod>" in t:
            echecs.append("sitemap sur collection vide : une date est apparue")
        try:
            ET.fromstring(t)
        except Exception as e:
            echecs.append(f"sitemap sur collection vide, XML invalide : {e}")
    return echecs


def refus_d_identifiant() -> list[str]:
    """8. Les deux refus du § 3 ne sont pas des affirmations : ils s'exécutent.

    Depuis la révision 14, l'URL ne dérive que de l'identifiant. Un identifiant
    mal formé, ou en désaccord avec le champ `livre`, doit donc ARRÊTER
    l'émission plutôt que produire une adresse muette ou mensongère. Le contrôle
    positif qui suit est indispensable : un constructeur qui refuserait tout
    passerait les sabotages sans rien garantir.
    """
    from generer import Chapitre

    faux = Path("livre-06-un-dossier") / "c05-un-libelle.md"
    echecs = []
    for ident, livre, quoi in [("L6-C05", 6, "séparateur absent"),
                               ("L6.C05.b", 6, "identifiant surnuméraire"),
                               ("C05", 6, "matricule de livre absent"),
                               ("L7.C05", 6, "désaccord avec le champ « livre »")]:
        try:
            Chapitre(faux, {"chapitre": ident, "livre": livre}, "")
        except SystemExit:
            continue
        echecs.append(f"identifiant « {ident} » accepté — {quoi} non refusé")
    try:                                        # contrôle positif, et l'URL du § 3
        ch = Chapitre(faux, {"chapitre": "L6.C05", "livre": 6, "titre": "T"}, "")
        if ch.url != "livre-6/c05/":
            echecs.append(f"URL « {ch.url} » au lieu de « livre-6/c05/ »")
    except SystemExit as e:
        echecs.append(f"identifiant régulier refusé : {e}")
    return echecs


# Le lien de retour, ÉCRIT EN ENTIER. Chercher `href="/"` ne suffit pas : avec
# `--base ""` cette adresse est l'index du corpus lui-même, et le compte donne
# alors 21 pages sur 21 dans les DEUX cas. Deux liens différents sous la même
# adresse. C'est le libellé qui les sépare.
RETOUR = "<a href=\"/\">Debunk'Onomy</a>"


def retour_au_site(sortie: Path, pages: list[Path]) -> list[str]:
    """Chaque page émise ramène-t-elle au site, en tête ET au pied ?

    Le corpus a été une porte à sens unique jusqu'au 2026-09-27 : le site y
    menait, lui ne menait nulle part. Le pied seul ne suffit pas — un lecteur au
    milieu d'un chapitre de quarante mille signes ne l'atteint qu'en traversant
    tout le texte —, d'où les deux emplacements, et d'où ce contrôle qui exige
    les deux.

    Il vérifie aussi que les liens INTERNES survivent : un retour ajouté qui
    casserait la navigation du corpus ne serait pas un progrès.
    """
    echecs = []
    for p in pages:
        t = p.read_text(encoding="utf-8")
        fil = re.search(r"(?s)<nav class=\"fil\".*?</nav>", t)
        pied = re.search(r"(?s)<footer class=\"pied\">.*?</footer>", t)
        if not fil or RETOUR not in fil.group(0):
            echecs.append(f"{p.parent.name}/{p.name} : pas de retour au site en tête")
        if not pied or RETOUR not in pied.group(0):
            echecs.append(f"{p.parent.name}/{p.name} : pas de retour au site au pied")
        for cible, quoi in (("/corpus/", "index du corpus"),
                            ("/corpus/glossaire.html", "glossaire"),
                            ("/corpus/diagnostic.html", "diagnostic")):
            if pied and f'href="{cible}"' not in pied.group(0):
                echecs.append(f"{p.parent.name}/{p.name} : lien interne perdu — {quoi}")
    return echecs


def retour_absent_a_la_racine() -> list[str]:
    """Et le corpus se tait-il quand il EST la racine ?

    Généré avec `--base ""`, il n'y a pas de site où revenir : le lien
    renverrait sur la page qu'on lit. La condition porte sur `base`, non sur une
    supposition quant à l'endroit où la sortie sera servie — et ce contrôle
    l'éprouve plutôt que de la croire.
    """
    with tempfile.TemporaryDirectory(prefix="corpus-racine-") as tmp:
        r = subprocess.run([sys.executable, str(GENERER), "--base", "",
                            "--sortie", tmp],
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace")
        if r.returncode != 0:
            return [f"génération à la racine en échec : {(r.stderr or '')[:120]}"]
        fautives = [p.parent.name + "/" + p.name
                    for p in sorted(Path(tmp).rglob("*.html"))
                    if RETOUR in p.read_text(encoding="utf-8")]
        if fautives:
            return [f"--base \"\" : {len(fautives)} page(s) portent un retour "
                    f"vers un site qui n'existe pas — {fautives[:3]}"]
    return []


def main() -> int:
    echecs: list[str] = []
    attendus = publiables()
    if not attendus:
        print("Aucun chapitre publiable : le générateur doit refuser d'écrire.")

    with tempfile.TemporaryDirectory(prefix="corpus-genere-") as tmp:
        sortie = Path(tmp)
        r = subprocess.run([sys.executable, str(GENERER), "--sortie", str(sortie)],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if not attendus:
            return 0 if r.returncode == 1 else 1
        if r.returncode != 0:
            print(r.stdout, r.stderr)
            return 1

        pages = sorted(sortie.rglob("*.html"))

        for p in sorted(sortie.rglob("*.json")):                      # 1
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except Exception as e:
                echecs.append(f"JSON invalide, {p.name} : {e}")

        echecs += controle_sitemap(                                   # 2
            (sortie / "sitemap.xml").read_text(encoding="utf-8"), attendus)

        for p in pages:
            t = p.read_text(encoding="utf-8")
            corps = t.split("<body>", 1)[-1]
            # le diagnostic reproduit la sortie du contrôle dans un <pre> : elle
            # porte légitimement des marques que le rendu ne traite pas.
            corps = re.sub(r"(?s)<pre>.*?</pre>", "", corps)
            for motif, nom in ((r"::(?:etat|hypothese|norme)::", "marqueur de régime"),
                               (r"\*\*[^*\n]+\*\*", "gras"),
                               (r"(?m)^#{1,4}\s", "titre")):
                trouve = re.search(motif, corps)
                if trouve:                                            # 3
                    echecs.append(f"{p.name} : {nom} non rendu — « {trouve.group(0)[:40]} »")
            bloc = re.search(r'<script type="application/ld\+json">(.*?)</script>', t, re.S)
            if bloc:
                try:
                    json.loads(bloc.group(1).replace("<\\/", "</"))
                except Exception as e:
                    echecs.append(f"{p.name} : JSON-LD invalide : {e}")
            appels = set(re.findall(r'<a class="ref" href="#(s\d+)"', t))
            ancres = set(re.findall(r'<li id="(s\d+)"', t))
            if appels - ancres:                                       # 4
                echecs.append(f"{p.parent.name} : appels sans fiche : {sorted(appels - ancres)}")

        for servi in sorted(sortie.rglob("index.md")):                # 5
            # L'URL ne porte plus le libellé (§ 3, révision 14) : la source se
            # retrouve par son identifiant, et non plus par le nom du dossier
            # servi — lequel ne dit plus rien du nom de fichier.
            n = int(servi.parent.parent.name.split("-")[1])
            num = servi.parent.name
            origine = [p for p in RACINE.glob(f"livre-{n:02d}-*/{num}*.md")
                       if p.stem == num or p.stem.startswith(num + "-")]
            if len(origine) != 1:
                echecs.append(f"source introuvable pour {servi.parent.name}")
            elif servi.read_bytes() != origine[0].read_bytes():
                echecs.append(f"{servi.parent.name} : le .md servi diffère du dépôt")

        index = json.loads((sortie / "index.json").read_text(encoding="utf-8"))
        emis = {c["id"] for c in index["chapitres"]}
        if emis != attendus:                                          # 6 et 7
            echecs.append(f"écart entre publiables et émis : {sorted(emis ^ attendus)}")

        pages_chapitres = len([p for p in pages if re.search(r"livre-\d+[\\/]c\d", str(p))])
        if pages_chapitres != len(attendus):
            echecs.append(f"{pages_chapitres} page(s) de chapitre pour {len(attendus)} publiable(s)")

        echecs += retour_au_site(sortie, pages)                       # 9 et 10

    echecs += retour_absent_a_la_racine()                             # 11
    echecs += sitemap_sur_collection_vide()                           # 2 bis
    echecs += refus_d_identifiant()                                   # 8

    if echecs:
        print(f"ÉCHEC — {len(echecs)} défaut(s) dans la sortie du générateur.")
        for e in echecs:
            print(f"  {e}")
        return 1
    print(f"Sortie du générateur conforme : {len(attendus)} chapitre(s) émis, "
          "JSON et XML valides, aucun Markdown résiduel, appels de source résolus, "
          "fichiers .md identiques au dépôt, retour au site en tête et au pied "
          "sous /corpus — et absent quand le corpus est la racine.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
