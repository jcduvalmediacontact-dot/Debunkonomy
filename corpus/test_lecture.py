#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests négatifs de l'état de lecture — E-L1 à E-L6, E-M1 — par sabotage.

Chaque sabotage s'exécute sur une COPIE du corpus dans un répertoire temporaire,
sur un corpus MIGRÉ (manifeste présent) ; le corpus réel n'est jamais touché.
Un sabotage réussit quand le contrôle produit le blocage attendu. Code de
sortie 0 si tous passent, 1 sinon.

    python corpus/test_lecture.py

  S0   le corpus copié passe le contrôle sans blocage — sinon rien ne prouve rien
  S1   une date sur une source candidate                    → E-L1
  S2   une source ouverte sans date                          → E-L2
  S3   une valeur d'état inconnue                            → E-L3
  S4   un chapitre verifie portant une source non ouverte    → E-L4
  S5   une génération publique illicite (--publier)          → E-L5
  S6   une occurrence a_requalifier absente du manifeste     → E-L6
  S7   une empreinte bibliographique modifiée                → E-L6
  S8   un manifeste absent, cassé, puis dupliqué             → E-M1, trois fois
  S10  deux références S1 dans un même chapitre              → référence dupliquée
  S11  identifiant incohérent avec chapitre/ref              → E-M1
  S12  empreinte mal formée                                  → E-M1
  S13  file inconnue                                         → E-M1
  S14  commit_source absent                                  → E-M1
  S15  schéma inconnu                                        → E-M1
  S16  code de trace inconnu                                 → E-M1
  S17  file et orientation incohérentes avec les traces      → E-M1
  S18  date calendairement invalide                          → E-M1
  S19  revision_convention différente de 12                  → E-M1
  S20  champ inconnu au niveau supérieur                     → E-M1 (schéma fermé)
  S21  champ inconnu dans migration                          → E-M1
  S22  champ inconnu dans une occurrence                     → E-M1
  S23  champ obligatoire absent dans une occurrence          → E-M1
  S24  trace sans appui                                      → E-M1
  S25  python qui n'est pas une chaîne                       → E-M1
  S9   le corpus restauré passe de nouveau sans blocage
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

import yaml

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CORPUS = Path(__file__).resolve().parent
JOUR = str(date.today())
RESULTATS = []


def copier_corpus():
    racine = Path(tempfile.mkdtemp(prefix="corpus-lecture-"))
    dest = racine / "corpus"
    shutil.copytree(CORPUS, dest, ignore=shutil.ignore_patterns(
        "sources", "__pycache__", "*.pyc", "test_*.py", "migrations", "hors-ligne"))
    shutil.copytree(CORPUS.parent / "protocoles", racine / "protocoles",
                    ignore=shutil.ignore_patterns("audits*", "*-audit.md", "*-deep-research.md"))
    return dest


def lancer(copie, *options):
    p = subprocess.run([sys.executable, str(copie / "controle.py"), *options],
                       cwd=str(copie), capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def fichier(copie, cle):
    for chemin in sorted(copie.glob("livre-*/*.md")):
        if re.search(r"^chapitre:\s*%s\s*$" % re.escape(cle), chemin.read_text(encoding="utf-8"), re.M):
            return chemin
    raise KeyError(cle)


def test(nom, condition, detail=""):
    RESULTATS.append((nom, bool(condition)))
    print(("  ok     " if condition else "  ÉCHEC  ") + nom + (("  — " + detail) if detail and not condition else ""))


def blocages(sortie):
    debut = sortie.find("BLOCAGES")
    fin = sortie.find("DÉCISIONS EN ATTENTE")
    return sortie[debut:fin] if debut >= 0 and fin >= 0 else sortie


class Sabotage:
    """Modifie un fichier, restaure toujours."""

    def __init__(self, chemin):
        self.chemin = chemin
        self.original = chemin.read_bytes() if chemin.exists() else None

    def texte(self):
        return self.chemin.read_text(encoding="utf-8")

    def ecrire(self, texte):
        self.chemin.write_text(texte, encoding="utf-8")

    def restaurer(self):
        if self.original is None:
            if self.chemin.exists():
                self.chemin.unlink()
        else:
            self.chemin.write_bytes(self.original)


def remplacer_premiere_source(texte, ancien_etat, nouveau_bloc):
    motif = re.compile(r"^([ \t]+)etat_lecture: %s[ \t]*$" % re.escape(ancien_etat), re.M)
    m = motif.search(texte)
    assert m, "aucune source " + ancien_etat
    return texte[:m.start()] + nouveau_bloc.replace("§", m.group(1)) + texte[m.end():]


def saboter_chapitre(nom, transformation, attendu, *options):
    s = Sabotage(cible)
    s.ecrire(transformation(s.texte()))
    code, sortie = lancer(copie, *options)
    test(nom, code == 1 and attendu in blocages(sortie), blocages(sortie)[:300])
    s.restaurer()


def saboter_manifeste(nom, modification, attendu):
    s = Sabotage(manifeste)
    contenu = json.loads(s.texte())
    modification(contenu)
    s.ecrire(json.dumps(contenu, ensure_ascii=False, indent=2))
    code, sortie = lancer(copie)
    test(nom, code == 1 and "E-M1" in blocages(sortie) and attendu in blocages(sortie), blocages(sortie)[:300])
    s.restaurer()


def modif(fn):
    return lambda c: fn(c["occurrences"][0])


def choisir_cible(copie, manifeste):
    """Cherche un chapitre qui se prête aux sabotages, au lieu de le fixer en dur.

    UNE CIBLE NOMMÉE EN DUR SE PÉRIME, et silencieusement. `L1.C08` a servi
    jusqu'à ce que ses quinze sources soient toutes ouvertes, le 2026-09-11 :
    le test s'est alors interrompu sur une assertion à son PREMIER sabotage, et
    les règles E-L1 à E-L6 ont cessé d'être éprouvées pendant cinq jours sans
    que rien ne le signale. Le corpus progresse ; la cible doit suivre.

    Cinq propriétés sont nécessaires, et chacune sert un sabotage précis.

    - statut autre que `verifie`, sinon S4 ne prouve rien et la copie bloquerait
      déjà en S0 ;
    - `citable` faux, que S5 doit pouvoir passer à vrai ;
    - au moins une source `a_requalifier`, que S1, S2 et S3 remplacent ;
    - **la PREMIÈRE source** `a_requalifier` et présente au manifeste : S7
      modifie la première ligne `reference:` du fichier, et sans cela il ne
      toucherait aucune empreinte bibliographique ;
    - cette première référence tenant sur une seule ligne, forme que le motif
      de S7 attend ; et une source de matricule `S2`, que S10 duplique.
    """
    occurrences = set()
    if manifeste.exists():
        try:
            occurrences = {o["id"] for o in
                           json.loads(manifeste.read_text(encoding="utf-8"))["occurrences"]}
        except Exception:
            pass

    recale = {}
    for chemin in sorted(copie.glob("livre-*/*.md")):
        texte = chemin.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
        if not m:
            continue
        try:
            entete = yaml.safe_load(m.group(1))
        except Exception:
            continue
        if not isinstance(entete, dict):
            continue
        sources = entete.get("sources_primaires") or []
        cle = str(entete.get("chapitre", chemin.name))
        manque = []
        if entete.get("statut") == "verifie":
            manque.append("statut verifie")
        if entete.get("citable") is True:
            manque.append("déjà citable")
        if not sources:
            manque.append("aucune source")
        else:
            premiere = sources[0]
            if premiere.get("etat_lecture") != "a_requalifier":
                manque.append("première source non a_requalifier")
            elif f"{cle}/{premiere.get('ref')}" not in occurrences:
                manque.append("première source absente du manifeste")
            if not re.search(r'^[ \t]+reference: ".*"[ \t]*$', texte, re.M):
                manque.append("référence sur plusieurs lignes")
            if not any(str(s.get("ref")) == "S2" for s in sources):
                manque.append("pas de source S2")
        if "\nverifications_en_attente:" not in texte:
            manque.append("pas de verifications_en_attente")
        if not manque:
            return chemin, cle
        recale[cle] = manque

    print("AUCUNE CIBLE UTILISABLE. Les sabotages E-L ont besoin d'un chapitre")
    print("non vérifié, non citable, dont la PREMIÈRE source est a_requalifier et")
    print("figure au manifeste, avec une source S2 et une référence sur une ligne.")
    print(f"{len(recale)} chapitre(s) examiné(s). Motifs les plus fréquents :")
    frequence = {}
    for motifs in recale.values():
        for motif in motifs:
            frequence[motif] = frequence.get(motif, 0) + 1
    for motif, n in sorted(frequence.items(), key=lambda x: -x[1])[:6]:
        print(f"  {n:4d}  {motif}")
    sys.exit(1)


copie = copier_corpus()
manifeste = copie / "manifeste-etat-lecture.json"
cible, cible_cle = choisir_cible(copie, manifeste)

print("S0  le corpus copié passe le contrôle")
code, sortie = lancer(copie)
test("S0 aucun blocage sur la copie migrée", code == 0 and "BLOCAGES — la publication est refusée  [0]" in sortie,
     blocages(sortie)[:300])

print(f"S1 à S7  les six règles E-L, par sabotage du chapitre {cible_cle}")
saboter_chapitre("S1 E-L1 bloque : une date sur une source candidate",
                 lambda t: remplacer_premiere_source(t, "a_requalifier", f"§etat_lecture: candidate\n§date_verification: {JOUR}"), "E-L1")
saboter_chapitre("S2 E-L2 bloque : une source ouverte sans date",
                 lambda t: remplacer_premiere_source(t, "a_requalifier", "§etat_lecture: ouverte"), "E-L2")
saboter_chapitre("S3 E-L3 bloque : une valeur d'état inconnue",
                 lambda t: remplacer_premiere_source(t, "a_requalifier", "§etat_lecture: lue"), "E-L3")
saboter_chapitre("S4 E-L4 bloque : un chapitre verifie à source non ouverte",
                 lambda t: re.sub(r"^statut: .*$", "statut: verifie", t, count=1, flags=re.M), "E-L4")
saboter_chapitre("S5 E-L5 bloque sous --publier : génération publique illicite",
                 lambda t: re.sub(r"^citable: .*$", "citable: true",
                                  re.sub(r"^statut: .*$", "statut: verifie", t, count=1, flags=re.M), count=1, flags=re.M),
                 "E-L5", "--publier")


def ajouter_s99(t):
    i = t.index("\nverifications_en_attente:")
    return t[:i] + '\n  - ref: S99\n    nature: theorie\n    reference: "Source ajoutée par sabotage"\n    etat_lecture: a_requalifier' + t[i:]


saboter_chapitre("S6 E-L6 bloque : occurrence a_requalifier absente du manifeste", ajouter_s99, "absente du manifeste")
saboter_chapitre("S7 E-L6 bloque : empreinte bibliographique modifiée",
                 lambda t: re.sub(r'^([ \t]+reference: ".*)"[ \t]*$', r'\1 (édition remplacée)"', t, count=1, flags=re.M),
                 "empreinte bibliographique")

print("S8  un manifeste absent, cassé, puis dupliqué")
s = Sabotage(manifeste)
manifeste.unlink()
code, sortie = lancer(copie)
test("S8a E-M1 bloque : manifeste absent", code == 1 and "E-M1" in blocages(sortie) and "absent" in blocages(sortie),
     blocages(sortie)[:300])
s.restaurer()
s = Sabotage(manifeste)
s.ecrire("{ ceci n'est pas du JSON")
code, sortie = lancer(copie)
test("S8b E-M1 bloque : manifeste illisible", code == 1 and "E-M1" in blocages(sortie) and "illisible" in blocages(sortie),
     blocages(sortie)[:300])
s.restaurer()


def dupliquer(c):
    c["occurrences"].append(dict(c["occurrences"][0]))
    c["migration"]["nombre_occurrences"] = len(c["occurrences"])


saboter_manifeste("S8c E-M1 bloque : identifiant dupliqué dans le manifeste", dupliquer, "doublon")

print("S10  deux références S1 dans un même chapitre")
saboter_chapitre("S10 référence dupliquée dans le chapitre bloque",
                 lambda t: t.replace("  - ref: S2\n", "  - ref: S1\n", 1), "référence dupliquée dans le chapitre")

print("S11 à S25  le schéma fermé du manifeste")
saboter_manifeste("S11 E-M1 : identifiant incohérent avec chapitre/ref",
                  modif(lambda o: o.update(id=o["chapitre"] + "/S9")), "identifiant incohérent")
saboter_manifeste("S12 E-M1 : empreinte mal formée",
                  modif(lambda o: o.update(empreinte_bibliographique="abc")), "empreinte bibliographique mal formée")
saboter_manifeste("S13 E-M1 : file inconnue", modif(lambda o: o.update(file="E")), "hors de A, B, C, D")
saboter_manifeste("S14 E-M1 : commit_source absent",
                  lambda c: c["migration"].pop("commit_source"), "champ de migration absent : commit_source")
saboter_manifeste("S15 E-M1 : schéma inconnu", lambda c: c.update(schema="autre/9"), "schema")
saboter_manifeste("S16 E-M1 : code de trace inconnu",
                  modif(lambda o: o.update(traces=[{"code": "T9", "emplacement": "x", "appui": "y"}])), "traces mal formées")
saboter_manifeste("S17 E-M1 : file et orientation incohérentes avec les traces",
                  modif(lambda o: o.update(file="A", orientation="orientation vers ouverte", traces=[])),
                  "incohérentes avec les traces")
saboter_manifeste("S18 E-M1 : date calendairement invalide",
                  modif(lambda o: o.update(ancienne_date_verification="2026-02-30")), "ancienne_date_verification invalide")
saboter_manifeste("S19 E-M1 : revision_convention différente de 12",
                  lambda c: c["migration"].update(revision_convention=11), "revision_convention")
saboter_manifeste("S20 E-M1 : champ inconnu au niveau supérieur",
                  lambda c: c.update(annexe=1), "champ inconnu au niveau supérieur")
saboter_manifeste("S21 E-M1 : champ inconnu dans migration",
                  lambda c: c["migration"].update(auteur="x"), "champ de migration inconnu")
saboter_manifeste("S22 E-M1 : champ inconnu dans une occurrence",
                  modif(lambda o: o.update(note="x")), "champ inconnu : note")
saboter_manifeste("S23 E-M1 : champ obligatoire absent dans une occurrence",
                  modif(lambda o: o.pop("orientation")), "champ obligatoire absent : orientation")
saboter_manifeste("S24 E-M1 : trace sans appui",
                  modif(lambda o: o.update(traces=[{"code": "T1", "emplacement": "reference"}])), "traces mal formées")
saboter_manifeste("S25 E-M1 : python qui n'est pas une chaîne",
                  lambda c: c["migration"].update(python=3.14), "chaîne non vide attendue")

print("S9  le corpus restauré passe de nouveau")
code, sortie = lancer(copie)
test("S9 aucun blocage après restauration", code == 0 and "BLOCAGES — la publication est refusée  [0]" in sortie,
     blocages(sortie)[:300])

shutil.rmtree(copie.parent, ignore_errors=True)
echecs = [n for n, ok in RESULTATS if not ok]
print()
print(f"{len(RESULTATS) - len(echecs)} sabotage(s) détecté(s) comme attendu, {len(echecs)} échec(s).")
sys.exit(1 if echecs else 0)
