# -*- coding: utf-8 -*-
"""Produit le DOSSIER COMPACT d'un chapitre pour une passe de supervision Codex.

Contrat arrete le 2026-09-19, RESSERRE le meme jour : le chapitre gele existe
deja dans le depot, et le dossier NE LE REPRODUIT PAS. Il porte :

  1. empreinte et chemin du chapitre
  2. resume des changements et EXTRAITS STRICTEMENT TOUCHES
  3. sources et controles CONCERNES
  4. faiblesses soumises expressement

Le superviseur lit le chapitre dans le depot si, et seulement si, une faiblesse
ou un extrait le rend necessaire. Le dossier lui donne le chemin et l'empreinte
pour qu'il lise le BON etat.

CE QUE CET OUTIL NE FAIT PAS : il ne juge pas. Il rassemble. La piece sur les
faiblesses est la seule que la machine ne peut pas produire, et le dossier REFUSE
de se fermer sans elle.

    python outils_claude/dossier_codex.py L1.C29 \\
        --depuis HEAD~3 --faiblesses notes.md --sortie dossier.md
"""
import argparse
import difflib
import hashlib
import io
import os
import re
import subprocess
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAFOND_EXTRAIT = 2400   # signes par section touchee, au-dela on coupe


def git(*args):
    """Renvoie la sortie de git, ou une ligne d'erreur lisible. N'echoue jamais."""
    try:
        r = subprocess.run(["git", "-C", RACINE] + list(args),
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        return (r.stdout or "").rstrip("\n") if r.returncode == 0 else \
            "(git a refusé : %s)" % (r.stderr or "").strip().split("\n")[0]
    except Exception as e:
        return "(git indisponible : %s)" % type(e).__name__


def fichier_du_chapitre(ident):
    """Retrouve le .md d'un identifiant L<n>.C<nn>, sans supposer le nom du dossier."""
    livre, chap = ident.split(".")
    n = int(livre[1:])
    trouves = glob.glob(os.path.join(RACINE, "corpus", "livre-%02d-*" % n, "%s*.md"
                                     % chap.lower()))
    if not trouves:
        trouves = [f for f in glob.glob(os.path.join(RACINE, "corpus", "livre-*", "c*.md"))
                   if re.search(r"(?m)^chapitre: %s$" % re.escape(ident),
                                io.open(f, encoding="utf-8").read())]
    if len(trouves) != 1:
        sys.exit("chapitre %s : %d fichier(s) trouvé(s), il en faut exactement un"
                 % (ident, len(trouves)))
    return trouves[0]


def scinde(texte):
    """Sépare un document en (en-tête, corps)."""
    m = re.search(r"(?ms)\A---\n.*?\n---\n", texte)
    return (texte[:m.end()], texte[m.end():]) if m else ("", texte)


def sections(corps):
    """Découpe un corps en sections `## `, en gardant le chapeau sous la clé '(chapeau)'."""
    bornes = [(m.start(), m.group(0).strip()) for m in re.finditer(r"(?m)^## .*$", corps)]
    if not bornes:
        return {"(chapeau)": corps.strip()}
    out = {"(chapeau)": corps[:bornes[0][0]].strip()}
    for i, (deb, titre) in enumerate(bornes):
        fin = bornes[i + 1][0] if i + 1 < len(bornes) else len(corps)
        out[titre] = corps[deb:fin].strip()
    return out


def controles():
    """Exécute le contrôle et les trois tests, et rend leur VERDICT, pas leur bruit."""
    sorties = []
    for nom, cmd in (("controle.py", ["corpus/controle.py"]),
                     ("test_etat.py", ["corpus/test_etat.py"]),
                     ("test_lecture.py", ["corpus/test_lecture.py"]),
                     ("test_generer.py", ["corpus/test_generer.py"])):
        try:
            # Sous Windows, l'enfant écrit dans l'encodage de la console (cp1252) et la
            # sortie arrive en mojibake. On lui impose UTF-8, sinon le verdict est illisible.
            env = dict(os.environ, PYTHONIOENCODING="utf-8")
            r = subprocess.run([sys.executable] + cmd, cwd=RACINE, capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=900,
                               env=env)
            lignes = [l for l in (r.stdout or "").rstrip("\n").split("\n") if l.strip()]
            sorties.append((nom, r.returncode, lignes[-1] if lignes else "(aucune sortie)"))
        except Exception as e:
            sorties.append((nom, -1, "(non exécuté : %s)" % type(e).__name__))
    return sorties


def construire(ident, depuis, faiblesses, resume_libre=None):
    F = fichier_du_chapitre(ident)
    rel = os.path.relpath(F, RACINE).replace("\\", "/")
    t = io.open(F, encoding="utf-8").read()
    tete, corps = scinde(t)
    if not tete:
        sys.exit("en-tête YAML introuvable dans %s" % rel)

    def champ(nom, defaut="(absent)"):
        mm = re.search(r"(?m)^%s: (.+)$" % re.escape(nom), tete)
        return mm.group(1).strip() if mm else defaut

    if not depuis:
        hist = git("log", "-2", "--format=%H", "--", rel).split("\n")
        depuis = hist[1] if len(hist) > 1 and re.fullmatch(r"[0-9a-f]{40}", hist[1]) else None

    ancien_tete, ancien_corps = ("", "")
    if depuis:
        brut = git("show", "%s:%s" % (depuis, rel))
        if not brut.startswith("(git"):
            ancien_tete, ancien_corps = scinde(brut)

    o = []
    w = o.append
    w("# Dossier de supervision — %s" % ident)
    w("")
    w("**État gelé, et le chapitre n'est pas reproduit ici.** Il est dans le dépôt, au")
    w("chemin et à l'empreinte ci-dessous. Ce dossier donne les changements, les extraits")
    w("touchés, les sources et contrôles concernés, et les faiblesses soumises. **Lire le")
    w("chapitre entier seulement si une faiblesse ou un extrait le rend nécessaire.**")
    w("")

    # ── 1. Identite ───────────────────────────────────────────────────────────
    w("## 1. Identité et empreinte")
    w("")
    w("| | |")
    w("|---|---|")
    w("| chapitre | `%s` — %s |" % (ident, champ("titre")))
    w("| **chemin** | `%s` |" % rel)
    w("| **empreinte du corps** | `sha256:%s` |"
      % hashlib.sha256(corps.encode("utf-8")).hexdigest())
    w("| taille du corps | %d mots |" % len(corps.split()))
    w("| statut / régime | **%s** / %s |" % (champ("statut"), champ("regime")))
    w("| autorité / citable | %s / %s |" % (champ("autorite"), champ("citable")))
    w("| revision_de_fond | %s |" % champ("revision_de_fond"))
    w("| commit de gel | `%s` |" % git("rev-parse", "--short", "HEAD"))
    propre = not git("status", "--porcelain", "--", rel).strip()
    w("| arbre de travail | %s |"
      % ("**PROPRE** — le dépôt porte bien cet état" if propre
         else "**SALE — le dépôt ne porte PAS cet état ; dossier non fiable**"))
    w("")

    # ── 2. Changements et extraits touches ────────────────────────────────────
    w("## 2. Les changements, et les extraits strictement touchés")
    w("")
    if not depuis:
        w("**Aucune passe précédente repérable** : premier dossier pour ce chapitre.")
        w("Le corps n'est pas reproduit ; le lire au chemin du § 1.")
        w("")
    else:
        w("Référence de la passe précédente : `%s`" % depuis[:12])
        w("")
        av, ap = sections(ancien_corps), sections(corps)
        inchangees, touchees, ajoutees, retirees = [], [], [], []
        for k in ap:
            if k not in av:
                ajoutees.append(k)
            elif av[k] != ap[k]:
                touchees.append(k)
            else:
                inchangees.append(k)
        for k in av:
            if k not in ap:
                retirees.append(k)

        w("| | sections |")
        w("|---|---|")
        w("| **modifiées** | %s |" % (", ".join("`%s`" % s for s in touchees) or "—"))
        w("| **ajoutées** | %s |" % (", ".join("`%s`" % s for s in ajoutees) or "—"))
        w("| **retirées** | %s |" % (", ".join("`%s`" % s for s in retirees) or "—"))
        w("| inchangées | %d |" % len(inchangees))
        w("")
        delta = len(corps.split()) - len(ancien_corps.split())
        w("Corps : %d mots, soit %+d depuis la passe précédente." % (len(corps.split()), delta))
        w("")
        if resume_libre:
            w("### Résumé des changements")
            w("")
            w(resume_libre.strip())
            w("")

        bouge = touchees + ajoutees
        if not bouge:
            w("**Aucune section du corps n'a bougé.** Les changements sont dans l'en-tête,")
            w("donnés au § 3.")
            w("")
        elif len(bouge) >= max(3, int(0.7 * len(ap))):
            w("### Réécriture en bloc")
            w("")
            w("**%d sections sur %d ont bougé : le corps a été réécrit, non retouché.**"
              % (len(bouge), len(ap)))
            w("Donner ici les extraits reviendrait à recopier le chapitre. **Le lire au")
            w("chemin du § 1**, à l'empreinte indiquée. Les faiblesses du § 5 pointent les")
            w("passages qui appellent un examen.")
            w("")
        else:
            w("### Extraits touchés")
            w("")
            for k in bouge:
                w("#### %s" % k)
                w("")
                if k in ajoutees:
                    w("*Section ajoutée.*")
                    w("")
                    bloc = ap[k]
                else:
                    d = list(difflib.unified_diff(
                        av[k].split("\n"), ap[k].split("\n"), lineterm="", n=1))
                    bloc = "\n".join(d[2:]) if len(d) > 2 else "(différence non isolable)"
                w("````diff" if k not in ajoutees else "````markdown")
                w(bloc if len(bloc) <= PLAFOND_EXTRAIT
                  else bloc[:PLAFOND_EXTRAIT] + "\n[… extrait coupé à %d signes]"
                  % PLAFOND_EXTRAIT)
                w("````")
                w("")

    # ── 3. Sources concernees ─────────────────────────────────────────────────
    w("## 3. Les sources concernées")
    w("")
    rx_bloc = (r"(?ms)^  - ref: (S\d+)$((?:\n(?!  - ref:|verifications_en_attente:)"
               r"[^\n]*)*)")
    anciens = {m.group(1): m.group(2) for m in re.finditer(rx_bloc, ancien_tete)} \
        if ancien_tete else {}
    lignes, fermees, total = [], 0, 0
    for s in re.finditer(rx_bloc, tete):
        ref, bloc = s.group(1), s.group(2)
        total += 1
        et = re.search(r"etat_lecture: (\w+)", bloc)
        et = et.group(1) if et else "?"
        if et != "ouverte":
            fermees += 1
        if anciens:
            mouvement = ("**NOUVELLE**" if ref not in anciens
                         else ("**MODIFIÉE**" if anciens[ref] != bloc else ""))
        else:
            mouvement = ""
        if not mouvement and et == "ouverte":
            continue                      # source ni touchee ni bloquante : hors dossier
        dt = re.search(r"date_verification: (\S+)", bloc)
        rf = re.search(r'reference: [">|]?\s*(.{0,80})', bloc, re.S)
        rf = re.sub(r"\s+", " ", rf.group(1)) if rf else "?"
        lignes.append("| **%s** | %s%s | %s | %d | %s… |"
                      % (ref, "**%s**" % et if et != "ouverte" else et,
                         " (%s)" % dt.group(1) if dt else "", mouvement or "—",
                         len(re.findall(re.escape("[%s]" % ref), corps)),
                         rf.replace("|", "\\|")))
    if lignes:
        w("Ne sont listées que les sources **touchées par cette passe** ou **non ouvertes**.")
        w("")
        w("| réf | état de lecture | mouvement | appels | référence (début) |")
        w("|---|---|---|---|---|")
        for l in lignes:
            w(l)
    else:
        w("Aucune source touchée par cette passe, et aucune source non ouverte.")
    w("")
    disparues = [r for r in anciens if not re.search(r"(?m)^  - ref: %s$" % r, tete)]
    if disparues:
        w("**Sources RETIRÉES depuis la passe précédente : %s.**" % ", ".join(sorted(disparues)))
        w("")
    w("**%d source(s) déclarée(s) au total, dont %d non ouverte(s).**%s"
      % (total, fermees,
         " Une source non ouverte interdit le passage à `verifie` (E-L4)." if fermees else ""))
    w("")

    # ── 4. Controles ──────────────────────────────────────────────────────────
    w("## 4. Les contrôles exécutés")
    w("")
    w("| contrôle | code | verdict |")
    w("|---|---|---|")
    for nom, code, verdict in controles():
        w("| `%s` | %s | %s |" % (nom, code, verdict.replace("|", "\\|")))
    w("")

    # ── 5. Faiblesses ─────────────────────────────────────────────────────────
    w("## 5. Les faiblesses soumises expressément")
    w("")
    w(faiblesses.strip())
    w("")
    w("---")
    w("")
    w("**Ce qui est demandé :** attribution, solidité logique, cohérence avec le corpus,")
    w("régressions, erreurs mécaniques. **Corrections ciblées seulement.** Si une source")
    w("manque ou si une recherche nouvelle est nécessaire, la renvoyer au lieu de la")
    w("conduire.")
    return "\n".join(o) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("chapitre", help="identifiant, par exemple L1.C29")
    p.add_argument("--depuis", default=None, help="référence git de la passe précédente")
    p.add_argument("--faiblesses", default=None, help="fichier des faiblesses (OBLIGATOIRE)")
    p.add_argument("--resume", default=None, help="fichier d'un résumé libre des changements")
    p.add_argument("--sortie", default=None, help="fichier de sortie (défaut : stdout)")
    a = p.parse_args()

    if not a.faiblesses:
        sys.exit("REFUS : la pièce « faiblesses soumises » est obligatoire.\n"
                 "        Un dossier sans elle fait croire au superviseur qu'il n'y a rien\n"
                 "        à signaler, ce qui est toujours faux. Écrire le fichier, puis\n"
                 "        relancer avec --faiblesses.")
    if not os.path.exists(a.faiblesses):
        sys.exit("fichier de faiblesses introuvable : %s" % a.faiblesses)
    faiblesses = io.open(a.faiblesses, encoding="utf-8").read().strip()
    if not faiblesses:
        sys.exit("REFUS : le fichier de faiblesses est vide.")
    resume = None
    if a.resume:
        if not os.path.exists(a.resume):
            sys.exit("fichier de résumé introuvable : %s" % a.resume)
        resume = io.open(a.resume, encoding="utf-8").read()

    texte = construire(a.chapitre, a.depuis, faiblesses, resume)
    if a.sortie:
        io.open(a.sortie, "w", encoding="utf-8", newline="\n").write(texte)
        sys.stderr.write("dossier écrit : %s (%d mots)\n" % (a.sortie, len(texte.split())))
    else:
        io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False).write(texte)


if __name__ == "__main__":
    main()
