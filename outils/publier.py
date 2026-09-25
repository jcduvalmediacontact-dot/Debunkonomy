"""Construit la branche `publication` : le site, et rien que le site.

POURQUOI CETTE BRANCHE EXISTE. Le site est servi depuis la racine de `main` —
`debunkonomy.org/AGENTS.md` répond 200. Une PR de `dev` publierait donc les 364
sources de `corpus/` et les 95 fichiers de `protocoles/` à des URL stables du
domaine, brouillons compris : la porte du § 13 le refuse. La branche
`publication` porte l'état de `dev` **moins** ce qui n'est pas le site, et c'est
elle qui part en PR.

UNE LISTE BLANCHE, ET NON UNE LISTE NOIRE. L'ordre du jour énumère ce qu'il faut
retirer ; ce script énumère ce qu'il faut GARDER. Pour une étape de publication la
différence n'est pas de style : un chemin nouveau qu'aucune liste noire ne
connaît serait publié en silence, alors qu'un chemin nouveau hors de la liste
blanche est simplement absent, et le compte le dit.

LE DISCRIMINANT SOURCE / PAGE ÉMISE, DÉJÀ ÉPROUVÉ DANS `publier_corpus.py` : une
source est ``livre-NN-un-slug``, une page émise ``livre-N`` à chiffres seuls.
C'est le piège de cet ordre : ``corpus/livre-1/`` correspond au motif
``corpus/livre-*/`` qu'il faut retirer, et c'est précisément ce qu'il faut garder.

LES `.md` QUI RESTENT, ET POURQUOI LA GARDE LITTÉRALE NE TIENT PAS. L'ordre
demande de refuser « un chemin `.md` hors `corpus/livre-N/` ». Mais la décision M1
fait entrer `AGENTS.md`, et `main` porte déjà quatre `.md` à sa racine. Une garde
littérale refuserait ce que M1 accorde. Elle refuse donc un `.md` qui n'est **ni**
sous ``corpus/livre-N/`` — le Markdown servi à côté de chaque page, § 13 — **ni
déjà présent sur `main`**. `CLAUDE.md`, lui, n'est pas sur `main` et sort.

L'ARBRE DE TRAVAIL N'EST JAMAIS BASCULÉ. Tout se passe dans un `git worktree`
jetable : une bascule de branche sur un arbre de 1 030 fichiers dont 43 générés
est le genre d'opération qui laisse un arbre à moitié propre.

    python outils/publier.py              # construit et commite la branche
    python outils/publier.py --pousser    # ... et la pousse

Rien n'est poussé sans `--pousser`, et aucune PR n'est ouverte par ce script :
`AGENTS.md` réserve les deux à l'accord de l'auteur.
"""

from __future__ import annotations

import argparse
import io
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

# La console de la plateforme testée est en cp1252 : une flèche suffit à faire
# tomber le script APRÈS le commit, ce qui est le pire moment. On écrit en UTF-8.
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                              errors="replace", line_buffering=True)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from construire_site import SITEMAP, fusionner_sitemaps   # une seule vérité

RACINE = Path(__file__).resolve().parents[1]
BRANCHE = "publication"
SOURCE = "dev-gpt-debunkonomy"

# Ce qui n'est pas le site : aucun de ces premiers niveaux ne passe.
DEHORS = {"protocoles", "outils", "outils_claude", "modeles", "tmp", "Codex",
          ".claude", "coordination"}
# Sous `corpus/`, seuls ces sept fichiers et les livres EMIS restent. L'ordre du
# jour ne nomme que `corpus/index.html` ; retirer le glossaire et le diagnostic
# laisserait cet index avec des liens morts, et le § 13 exige la page de
# diagnostic. Les sept sont donc gardés, et le compte les nomme.
EMIS_RACINE = {"index.html", "index.json", "glossaire.html", "glossaire.json",
               "diagnostic.html", "llms.txt", "sitemap.xml"}
LIVRE_EMIS = re.compile(r"^livre-\d+$")
# Suivis sur `dev`, ABSENTS DE `main`, et qui ne sont pas du site. Les garder
# les publierait pour la première fois, à une URL stable du domaine : ce serait
# une divulgation neuve et non un alignement, et ce ne sont pas les vingt
# fichiers de M1, qui divergent. Le plan directeur fait autorité sur
# `livres.yaml` (CLAUDE.md) ; il n'a rien à faire sur le site.
# Exclus sur décision de l'auteur, le 2026-09-25.
PAS_LE_SITE = {".gitignore", "PLAN-DIRECTEUR-2026-09-04.pdf", "plan-des-livres.xlsx"}


def git(*a, cwd=None, muet=False):
    r = subprocess.run(["git"] + list(a), cwd=str(cwd or RACINE),
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode and not muet:
        raise SystemExit("git %s : %s" % (" ".join(a), (r.stderr or "").strip()))
    return r.returncode, (r.stdout or "")


def garde(chemin: str) -> bool:
    """Ce chemin appartient-il au site publié ?"""
    parts = chemin.split("/")
    if parts[0] in DEHORS or chemin == "CLAUDE.md" or chemin in PAS_LE_SITE:
        return False
    if parts[0] != "corpus":
        return True
    if len(parts) == 2 and parts[1] in EMIS_RACINE:
        return True
    return len(parts) > 2 and bool(LIVRE_EMIS.match(parts[1]))


def main() -> int:
    p = argparse.ArgumentParser(description="Construit la branche `publication`.")
    p.add_argument("--pousser", action="store_true",
                   help="pousse la branche (accord de l'auteur requis)")
    a = p.parse_args()

    # ── Préalables : on ne publie pas depuis un arbre douteux ────────────────
    _, sale = git("status", "--porcelain")
    sale = [l for l in sale.split("\n") if l and not l.startswith("??")]
    if sale:
        raise SystemExit("Arbre de travail modifié — publier suppose un arbre propre :\n  "
                         + "\n  ".join(sale))
    _, branche = git("rev-parse", "--abbrev-ref", "HEAD")
    if branche.strip() != SOURCE:
        raise SystemExit("La branche courante est « %s » et non « %s »."
                         % (branche.strip(), SOURCE))
    _, tete = git("rev-parse", "HEAD")
    tete = tete.strip()
    if not (RACINE / "corpus" / "livre-1").is_dir():
        raise SystemExit("`corpus/livre-1/` absent : lancer outils/publier_corpus.py d'abord.")

    tous = [x for x in git("ls-files")[1].split("\n") if x]
    gardes = [x for x in tous if garde(x)]
    retires = [x for x in tous if not garde(x)]
    print("Sur %s : %d fichier(s) suivis — %d gardés, %d retirés."
          % (tete[:8], len(tous), len(gardes), len(retires)))

    # ── La branche, dans un worktree jetable ─────────────────────────────────
    atelier = Path(tempfile.mkdtemp(prefix="publication-"))
    arbre = atelier / "arbre"
    try:
        git("worktree", "add", "--detach", str(arbre), tete)
        code, _ = git("rev-parse", "--verify", BRANCHE, muet=True)
        git("checkout", "-B", BRANCHE, tete, cwd=arbre)
        print("Branche `%s` %s sur %s."
              % (BRANCHE, "remise" if code == 0 else "créée", tete[:8]))

        if retires:
            for i in range(0, len(retires), 200):     # la ligne de commande a une limite
                git("rm", "-r", "-q", "--", *retires[i:i + 200], cwd=arbre)

        # ── Le sitemap fusionné : 225 URL du site + 20 du corpus ─────────────
        avant = len(ET.parse(arbre / "sitemap.xml").getroot())
        fusionner_sitemaps(arbre, arbre / "corpus")
        racine_sm = ET.parse(arbre / "sitemap.xml").getroot()
        urls = [e.findtext("{%s}loc" % SITEMAP) for e in racine_sm]
        git("add", "sitemap.xml", cwd=arbre)

        # ── GARDES : avant le commit, jamais après ───────────────────────────
        reste = [x for x in git("ls-files", cwd=arbre)[1].split("\n") if x]
        assert sorted(reste) == sorted(gardes), (
            "l'arbre de la branche ne correspond pas à la liste gardée : "
            "%d contre %d" % (len(reste), len(gardes)))

        sur_main = {x for x in git("ls-tree", "-r", "--name-only", "origin/main")[1]
                    .split("\n") if x.endswith(".md")}
        fautifs = [x for x in reste if x.endswith(".md")
                   and not (x.startswith("corpus/") and LIVRE_EMIS.match(x.split("/")[1]))
                   and x not in sur_main]
        if fautifs:
            raise SystemExit("REFUS : %d `.md` ni sous corpus/livre-N/ ni déjà sur "
                             "main :\n  %s" % (len(fautifs), "\n  ".join(fautifs)))

        interdits = [x for x in reste
                     if x.split("/")[0] in DEHORS or x == "CLAUDE.md"
                     or (x.startswith("corpus/") and not garde(x))]
        if interdits:
            raise SystemExit("REFUS : %d chemin(s) hors du site subsistent :\n  %s"
                             % (len(interdits), "\n  ".join(interdits[:20])))
        # CE QUE LA BRANCHE AJOUTE À `main` NE PEUT ÊTRE QUE DU CORPUS ÉMIS.
        # Garde née d'un défaut : la première construction ajoutait `.gitignore`,
        # `PLAN-DIRECTEUR-2026-09-04.pdf` et `plan-des-livres.xlsx` — suivis sur
        # `dev`, absents de `main`. Ils auraient été publiés pour la première
        # fois, à une URL stable du domaine, sans que rien ne le dise.
        sur_main_tous = {x for x in git("ls-tree", "-r", "--name-only",
                                        "origin/main")[1].split("\n") if x}
        neufs = [x for x in reste if x not in sur_main_tous and not x.startswith("corpus/")]
        if neufs:
            raise SystemExit(
                "REFUS : %d fichier(s) seraient AJOUTÉS à `main` hors du corpus.\n"
                "        Ce n'est pas un alignement, c'est une publication neuve :\n"
                "  %s" % (len(neufs), "\n  ".join(neufs)))

        for indispensable in ("index.html", "CNAME", ".nojekyll", "sitemap.xml"):
            if indispensable not in reste:
                raise SystemExit("REFUS : `%s` manque à la racine." % indispensable)
        if len(urls) != len(set(urls)) or None in urls:
            raise SystemExit("REFUS : sitemap à URL en double ou sans <loc>.")
        if racine_sm.tag != "{%s}urlset" % SITEMAP:
            raise SystemExit("REFUS : sitemap hors de l'espace officiel.")

        # ── Le commit ───────────────────────────────────────────────────────
        message = (
            "Le site seul, pour publication — dix-sept pages du Livre 1\n\n"
            "Construit par outils/publier.py depuis %s. Ce qui n'est pas le site\n"
            "est retiré : %d fichier(s). Ce qui reste : %d, dont %d pages émises\n"
            "sous corpus/livre-1/ et %d fichiers émis à la racine de corpus/.\n\n"
            "Le sitemap est fusionné ici, et nulle part ailleurs : %d URL du site\n"
            "plus celles du corpus font %d URL uniques, dans l'espace officiel.\n\n"
            "Ce commit ne contient aucune source du corpus, aucun protocole,\n"
            "aucun outil, aucun .py. La garde le vérifie avant d'écrire.\n"
            % (tete[:8], len(retires), len(reste),
               sum(1 for x in reste if x.startswith("corpus/livre-1/")),
               sum(1 for x in reste if x.startswith("corpus/") and x.count("/") == 1),
               avant, len(urls)))
        git("commit", "-q", "-m", message, cwd=arbre)
        _, sha = git("rev-parse", "HEAD", cwd=arbre)
        sha = sha.strip()

        # ── Le compte, par catégorie ────────────────────────────────────────
        cat = {}
        for x in reste:
            if x.startswith("corpus/livre-1/"):
                c = "pages émises corpus/livre-1/"
            elif x.startswith("corpus/"):
                c = "émis à la racine de corpus/"
            elif "/" in x:
                c = x.split("/")[0] + "/"
            else:
                c = "(racine)"
            cat[c] = cat.get(c, 0) + 1
        print("\nBranche `%s` : %s" % (BRANCHE, sha))
        print("  %d fichier(s) — sitemap %d → %d URL uniques" % (len(reste), avant, len(urls)))
        for c in sorted(cat, key=lambda k: -cat[k]):
            print("    %-34s %4d" % (c, cat[c]))

        if a.pousser:
            git("push", "-u", "origin", BRANCHE + ":" + BRANCHE, cwd=arbre)
            print("\nBranche poussée. AUCUNE PR OUVERTE : l'ordre 1 de Codex d'abord.")
        else:
            print("\nNON POUSSÉE. `--pousser` la pousse ; AGENTS.md réserve ce geste\n"
                  "à l'accord de l'auteur. Aucune PR n'est ouverte par ce script.")
        return 0
    finally:
        git("worktree", "remove", "--force", str(arbre), muet=True)
        shutil.rmtree(atelier, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
