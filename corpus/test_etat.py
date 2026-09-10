#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests de conservation de l'état enregistré — controle.py --maj-etat.

Réparation du 2026-09-10 (protocoles/migration-etat-lecture.md, § 9.2 et
§ 9.3). Chaque test s'exécute sur une COPIE du corpus dans un répertoire
temporaire : le corpus réel n'est jamais touché. Code de sortie 0 si tous les
tests passent, 1 sinon.

    python corpus/test_etat.py

  T-Q8  sur le corpus courant : bilan de l'enregistrement, aucune qualification perdue
  T-Q1  une entrée inchangée conserve sa qualification (P1)
  T-Q2  un en-tête seul modifié la conserve (P2)
  T-Q3  --fond ne qualifie que l'entrée dont le corps a changé, et rien d'autre (P3, P10)
  T-Q4  initialisation nommée, tardive si le chapitre existait avant (P4, P5)
  T-Q5  entrées absentes et orphelines au diagnostic, orphelines conservées sauf purge (P6, P7, P9)
  T-Q6  --publier refuse un chapitre verifie ou citable sans état (P8)
  T-Q7  aucune combinaison d'options ne fait disparaître une qualification sans demande (P9)

Un test qui passerait sur le script d'avant la réparation serait un test
faux. Exécutée contre ce script le 2026-09-10, la suite a donné 16 échecs sur
31 assertions : T-Q8 (toute qualification perdue), T-Q3, T-Q4, T-Q5, T-Q6 et
T-Q7 (--editorial) mordent. T-Q1 et T-Q2 y passaient À VIDE — le premier
enregistrement ayant effacé toutes les qualifications, il n'en restait aucune
à conserver ; ils ne prouvent quelque chose qu'après T-Q8.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CORPUS = Path(__file__).resolve().parent
JOUR = str(date.today())
RESULTATS = []


# --- outillage --------------------------------------------------------------

def copier_corpus():
    racine = Path(tempfile.mkdtemp(prefix="corpus-test-"))
    dest = racine / "corpus"
    shutil.copytree(CORPUS, dest, ignore=shutil.ignore_patterns(
        "sources", "__pycache__", "*.pyc", "test_*.py"))
    # Le registre des arbitrages renvoie aux textes de protocoles/, à la racine
    # du dépôt, et le contrôle vérifie qu'ils existent : la copie les emporte.
    shutil.copytree(CORPUS.parent / "protocoles", racine / "protocoles",
                    ignore=shutil.ignore_patterns("audits*", "*-audit.md", "*-deep-research.md"))
    return dest


def lancer(copie, *options):
    p = subprocess.run([sys.executable, str(copie / "controle.py"), *options],
                       cwd=str(copie), capture_output=True)
    return p.returncode, p.stdout.decode("utf-8", "replace")


def etat(copie):
    return json.loads((copie / ".etat-corpus.json").read_text(encoding="utf-8"))


def ecrire_etat(copie, contenu):
    (copie / ".etat-corpus.json").write_text(
        json.dumps(contenu, indent=2, ensure_ascii=False), encoding="utf-8")


def fichier(copie, cle):
    for chemin in sorted(copie.glob("livre-*/*.md")):
        if re.search(r"^chapitre:\s*%s\s*$" % re.escape(cle),
                     chemin.read_text(encoding="utf-8"), re.M):
            return chemin
    raise KeyError(cle)


def modifier_entete(chemin, motif, remplacement):
    """Remplace UNE ligne d'en-tête, le corps restant intact."""
    parties = chemin.read_text(encoding="utf-8").split("---", 2)
    tete, nb = re.subn(motif, remplacement, parties[1], flags=re.M)
    assert nb == 1, f"{chemin.name} : motif {motif!r} trouvé {nb} fois"
    chemin.write_text("---".join([parties[0], tete, parties[2]]), encoding="utf-8")


def vider_verifications(chemin):
    parties = chemin.read_text(encoding="utf-8").split("---", 2)
    lignes = parties[1].split("\n")
    sortie, saute = [], False
    for ligne in lignes:
        if ligne.startswith("verifications_en_attente:"):
            sortie.append("verifications_en_attente: []")
            saute = True
            continue
        if saute and (ligne.startswith(" ") or ligne.startswith("\t")):
            continue
        saute = False
        sortie.append(ligne)
    chemin.write_text("---".join([parties[0], "\n".join(sortie), parties[2]]), encoding="utf-8")


def ajouter_au_corps(chemin, texte):
    with chemin.open("a", encoding="utf-8") as f:
        f.write("\n::etat:: " + texte + "\n")


def identiques_sauf(avant, apres, exceptions):
    """Toutes les entrées hors `exceptions` sont identiques, clé par clé."""
    ecarts = []
    for cle in set(avant) | set(apres):
        if cle in exceptions:
            continue
        if avant.get(cle) != apres.get(cle):
            ecarts.append(cle)
    return ecarts


def test(nom, condition, detail=""):
    RESULTATS.append((nom, bool(condition)))
    print(("  ok     " if condition else "  ÉCHEC  ") + nom
          + (("  — " + detail) if detail and not condition else ""))


def qualif(e, cle):
    return str(e.get(cle, {}).get("qualification", ""))


# --- T-Q8 : le corpus courant, tel quel ---------------------------------------
print("T-Q8  enregistrement sur une copie du corpus courant")
copie = copier_corpus()
avant = etat(copie)
code, sortie = lancer(copie, "--maj-etat")
apres = etat(copie)
nb_chapitres = len(list(copie.glob("livre-*/*.md")))
perdues = [c for c in avant if avant[c].get("qualification")
           and (c not in apres or not apres[c].get("qualification"))]
conservees = [c for c in avant if c in apres
              and apres[c].get("qualification") == avant[c].get("qualification")]
fond_tardif = [c for c in apres if qualif(apres, c).startswith("fond, revision_de_fond du")]
init_tardive = [c for c in apres if qualif(apres, c).startswith("initialisation tardive")]
init = [c for c in apres if qualif(apres, c).startswith("initialisation, ")]
print(f"        {len(apres)} entrées pour {nb_chapitres} chapitres ; conservées {len(conservees)} ; "
      f"fond enregistrées tardivement {len(fond_tardif)} ; initialisations tardives {len(init_tardive)} ; "
      f"initialisations {len(init)} ; perdues {len(perdues)}")
test("T-Q8 l'enregistrement s'est fait", code == 0 and "État enregistré" in sortie, sortie[-400:])
test("T-Q8 une entrée par chapitre, ni plus ni moins", len(apres) == nb_chapitres)
test("T-Q8 aucune qualification perdue", not perdues, ", ".join(perdues[:10]))
test("T-Q8 les classes se bouclent",
     len(conservees) + len(fond_tardif) + len(init_tardive) + len(init) == len(apres))
test("T-Q8 toute entrée ancienne à corps inchangé est conservée",
     all(c in conservees for c in avant if c in apres
         and avant[c].get("editoriale") == apres[c].get("editoriale")))
test("T-Q8 toute entrée ancienne à corps changé et date déplacée est un fond enregistré tardivement",
     all(c in fond_tardif for c in avant if c in apres
         and avant[c].get("editoriale") != apres[c].get("editoriale")
         and str(avant[c].get("revision_de_fond")) != str(apres[c].get("revision_de_fond"))))
test("T-Q8 chaque fond tardif conserve la date réelle du chapitre",
     all(qualif(apres, c) == f"fond, revision_de_fond du {apres[c]['revision_de_fond']}, "
         f"enregistrée tardivement le {JOUR}" for c in fond_tardif))
test("T-Q8 toute entrée nouvelle est une initialisation nommée",
     all(c in init or c in init_tardive for c in apres if c not in avant))

# --- T-Q1 : idempotence -----------------------------------------------------------
print("T-Q1  une entrée inchangée conserve sa qualification")
octets_avant = (copie / ".etat-corpus.json").read_bytes()
code, sortie = lancer(copie, "--maj-etat")
test("T-Q1 un second enregistrement ne change rien, octet pour octet",
     code == 0 and (copie / ".etat-corpus.json").read_bytes() == octets_avant)
reference = etat(copie)

# --- T-Q2 : metadonnees seules ----------------------------------------------------
print("T-Q2  un en-tête seul modifié conserve la qualification")
cle2 = sorted(reference)[0]
modifier_entete(fichier(copie, cle2), r'^titre: "(.*)"$', r'titre: "\1 (test T-Q2)"')
code, sortie = lancer(copie, "--maj-etat")
e2 = etat(copie)
test("T-Q2 l'empreinte de métadonnées a changé",
     code == 0 and e2[cle2]["metadonnees"] != reference[cle2]["metadonnees"])
test("T-Q2 la qualification est conservée", qualif(e2, cle2) == qualif(reference, cle2))
test("T-Q2 aucune autre entrée n'a bougé", not identiques_sauf(reference, e2, {cle2}))

# --- T-Q3 : --fond ne qualifie que l'entree visee ---------------------------------
print("T-Q3  --fond ne qualifie que l'entrée dont le corps a changé")
cle3 = sorted(reference)[1]
ajouter_au_corps(fichier(copie, cle3), "Ligne ajoutée par test_etat, T-Q3.")
code, sortie = lancer(copie, "--maj-etat")
test("T-Q3 sans option, la décision en attente bloque l'enregistrement",
     "des décisions sont en attente" in sortie and etat(copie) == e2)
code, sortie = lancer(copie, "--maj-etat", "--fond")
e3 = etat(copie)
test("T-Q3 --fond qualifie l'entrée visée", code == 0 and qualif(e3, cle3) == f"fond, déclarée le {JOUR}")
test("T-Q3 et elle seule : toutes les autres sont identiques octet pour octet",
     not identiques_sauf(e2, e3, {cle3}))

# --- T-Q4 : initialisation nommee --------------------------------------------------
print("T-Q4  initialisation nommée, tardive si le chapitre existait avant")
modele = fichier(copie, "L9.C01")
for cle, nom, rev in (("L9.C98", "c98-test-initialisation.md", JOUR),
                      ("L9.C99", "c99-test-tardive.md", "2026-09-01")):
    cible = modele.parent / nom
    shutil.copy(modele, cible)
    modifier_entete(cible, r"^chapitre: L9\.C01$", "chapitre: " + cle)
    modifier_entete(cible, r'^titre: "(.*)"$', r'titre: "Test %s"' % cle)
    modifier_entete(cible, r"^revision_de_fond: .*$", "revision_de_fond: " + rev)
code, sortie = lancer(copie, "--maj-etat")
e4 = etat(copie)
test("T-Q4 un chapitre du jour est une initialisation datée",
     code == 0 and qualif(e4, "L9.C98") == f"initialisation, enregistrée le {JOUR}")
test("T-Q4 un chapitre antérieur est une initialisation tardive, nommée comme telle",
     qualif(e4, "L9.C99") == f"initialisation tardive, état antérieur non enregistré, enregistrée le {JOUR}")
test("T-Q4 aucune autre entrée n'a bougé", not identiques_sauf(e3, e4, {"L9.C98", "L9.C99"}))

# --- T-Q5 : absents et orphelins au diagnostic -------------------------------------
print("T-Q5  entrées absentes et orphelines au diagnostic")
cle5 = next(c for c in sorted(e4) if str(e4[c].get("revision_de_fond")) < JOUR and c not in (cle2, cle3))
tronque = dict(e4)
del tronque[cle5]
tronque["L99.C99"] = {"editoriale": "0" * 16, "metadonnees": "0" * 16,
                      "revision_de_fond": "2026-09-01", "qualification": "test orpheline"}
ecrire_etat(copie, tronque)
code, sortie = lancer(copie)
test("T-Q5 le chapitre sans entrée est au diagnostic", f"état non enregistré — {cle5}" in sortie)
test("T-Q5 l'entrée sans chapitre est au diagnostic",
     "entrée d'état sans chapitre correspondant : L99.C99" in sortie)
test("T-Q5 le compte figure en tête du rapport",
     "1 sans état enregistré, 1 entrée(s) d'état orpheline(s)" in sortie)
code, sortie = lancer(copie, "--maj-etat")
e5 = etat(copie)
test("T-Q5 l'entrée orpheline est conservée sans purge explicite",
     code == 0 and e5.get("L99.C99", {}).get("qualification") == "test orpheline")
test("T-Q5 le chapitre réinscrit est une initialisation tardive",
     qualif(e5, cle5).startswith("initialisation tardive"))
code, sortie = lancer(copie, "--maj-etat", "--purger-orphelins")
e5b = etat(copie)
test("T-Q5 la purge explicite retire l'orpheline, et elle seule",
     code == 0 and "L99.C99" not in e5b and not identiques_sauf(e5, e5b, {"L99.C99"}))

# --- T-Q6 : publication sans etat ----------------------------------------------------
print("T-Q6  --publier refuse un chapitre verifie ou citable sans état")
cle6 = "L9.C01"
f6 = fichier(copie, cle6)
modifier_entete(f6, r"^statut: .*$", "statut: verifie")
modifier_entete(f6, r"^citable: .*$", "citable: true")
vider_verifications(f6)
# Un chapitre verifie doit déclarer au moins un concept du vocabulaire, sans
# quoi le contrôle bloque et l'état n'est plus enregistrable.
import yaml  # la dépendance même de controle.py
vocab = yaml.safe_load((copie / "vocabulaire.yaml").read_text(encoding="utf-8"))
terme = next(e["terme"] for e in vocab if isinstance(e, dict) and "terme" in e)
modifier_entete(f6, r"^concepts: \[\]$", 'concepts: ["%s"]' % terme)
sans = dict(e5b)
del sans[cle6]
ecrire_etat(copie, sans)
code, sortie = lancer(copie, "--publier")
motif6 = "aucun état enregistré pour ce chapitre"
test("T-Q6 sans état, la publication est refusée pour ce motif",
     code == 1 and motif6 in sortie)
code, sortie = lancer(copie, "--maj-etat")
test("T-Q6 l'état s'enregistre ensuite sans blocage", code == 0 and "État enregistré" in sortie,
     sortie[-300:])
code, sortie = lancer(copie, "--publier")
test("T-Q6 une fois l'état enregistré, ce motif disparaît", motif6 not in sortie)

# --- T-Q7 : aucune option ne perd une qualification --------------------------------
print("T-Q7  aucune combinaison d'options ne fait disparaître une qualification")
base = etat(copie)
qualifiees = {c: base[c]["qualification"] for c in base if base[c].get("qualification")}
ok7 = True
for options in (("--maj-etat",), ("--maj-etat", "--editorial"), ("--maj-etat", "--fond")):
    code, sortie = lancer(copie, *options)
    e7 = etat(copie)
    ok7 = ok7 and code == 0 and all(e7.get(c, {}).get("qualification") == q for c, q in qualifiees.items())
test("T-Q7 sans décision en attente, --maj-etat, --editorial et --fond conservent tout", ok7)
code, sortie = lancer(copie, "--maj-etat", "--editorial", "--fond")
test("T-Q7 --editorial et --fond s'excluent, et rien n'est écrit",
     "s'excluent" in sortie and etat(copie) == e7)
cle7 = sorted(c for c in base if c not in (cle2, cle3, cle5, cle6, "L9.C98", "L9.C99"))[2]
ajouter_au_corps(fichier(copie, cle7), "Ligne ajoutée par test_etat, T-Q7.")
code, sortie = lancer(copie, "--maj-etat", "--editorial")
e7b = etat(copie)
test("T-Q7 --editorial qualifie l'entrée visée, et elle seule",
     code == 0 and qualif(e7b, cle7) == f"editorial, déclaré le {JOUR}"
     and not identiques_sauf(e7, e7b, {cle7}))
test("T-Q7 toutes les qualifications antérieures sont encore là, à l'identique",
     all(e7b.get(c, {}).get("qualification") == q for c, q in qualifiees.items() if c != cle7))

# --- bilan --------------------------------------------------------------------------
shutil.rmtree(copie.parent, ignore_errors=True)
echecs = [n for n, ok in RESULTATS if not ok]
print()
print(f"{len(RESULTATS) - len(echecs)} test(s) passé(s), {len(echecs)} échec(s).")
sys.exit(1 if echecs else 0)
