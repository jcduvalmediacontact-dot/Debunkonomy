#!/usr/bin/env python3
"""Contrôle de la sortie du générateur du § 13.

Ce test ne vérifie pas que `generer.py` s'exécute : il vérifie que ce qu'il
écrit tient. Il émet dans un dossier temporaire, jamais dans l'arbre du dépôt,
et il contrôle sept invariants.

1. Tout JSON produit est du JSON valide, JSON-LD des pages compris.
2. Le `sitemap.xml` est du XML valide.
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

        try:                                                          # 2
            ET.parse(sortie / "sitemap.xml")
        except Exception as e:
            echecs.append(f"sitemap.xml invalide : {e}")

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

    echecs += refus_d_identifiant()                                   # 8

    if echecs:
        print(f"ÉCHEC — {len(echecs)} défaut(s) dans la sortie du générateur.")
        for e in echecs:
            print(f"  {e}")
        return 1
    print(f"Sortie du générateur conforme : {len(attendus)} chapitre(s) émis, "
          "JSON et XML valides, aucun Markdown résiduel, appels de source résolus, "
          "fichiers .md identiques au dépôt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
