# -*- coding: utf-8 -*-
"""Contrôle des ancres « Lx.Cy § n » contre les titres du chapitre cible.

CE QUE CE CONTRÔLE ÉTABLIT. Une réécriture déplace les sections sans prévenir :
un renvoi écrit « L1.C08 § 4 » reste lisible longtemps après que le § 4 a changé
de sujet ou cessé d'exister. Le contrôle ouvre le chapitre cible et vérifie que
la section existe.

CE QU'IL N'ÉTABLIT PAS, et il faut le dire : que la section parle bien de ce que
le renvoi lui fait dire. Un § 4 qui existe et qui traite d'autre chose passe ce
contrôle. Seule une lecture le verrait.

DEUX CLASSES D'ANCRE :
  QUALIFIÉE    « L1.C08 § 4 » — chapitre nommé, résolu dans tout le corpus.
  INTERNE      « § 4 » seul   — renvoi du chapitre à lui-même.

Il ne touche à rien et ne remplace aucune règle de controle.py, qui reste
l'autorité. Code de sortie : 0 si aucune ancre morte, 1 sinon.

    python outils_claude/controle_ancres.py            # tout le corpus
    python outils_claude/controle_ancres.py --livre 1  # un livre
"""
import argparse
import io
import os
import re
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

# « L1.C08 § 4 », avec espace insécable ou non, et « §§ » toléré au relevé.
ANCRE_QUALIFIEE = re.compile(r"(L\d+\.C\d+)\s*§+\s*(\d+)")
# « § 4 » qui ne suit PAS un identifiant de chapitre : renvoi interne PRÉSUMÉ.
ANCRE_INTERNE = re.compile(r"(?<!\d)(?<![\.\w])§\s*(\d+)")
# Ce qui, juste avant un « § n », désigne un AUTRE document : une norme citée
# (IPSAS 47 § 19, BPM6 § 5.35), ou l'intérieur d'un appel de source.
# Relevé le 2026-09-20 : sans ce filtre, le contrôle rendait quatre défauts qui
# n'en étaient pas — trois paragraphes d'IPSAS et une section de [S10].
AUTRE_DOCUMENT = re.compile(
    r"(?:\[S\d+[^\]]*|[A-ZÉÈÀÙÂÊÎÔÛ]{2,}\s*\d*(?:[/-]\d+)?\s*|"
    r"article\s+[\w\.]+\s*|section\s+[\d\.]+,?\s*)$")
TITRE = re.compile(r"^##\s+(\d+)\.\s*(.*)$", re.M)


def chapitres():
    """id -> (chemin, {numéro de section: titre})."""
    index = {}
    for f in sorted(glob.glob(os.path.join(CORPUS, "livre-*", "c*.md"))):
        txt = io.open(f, encoding="utf-8").read()
        m = re.search(r"(?m)^chapitre:\s*(L\d+\.C\d+)\s*$", txt)
        if not m:
            continue
        lignes = txt.split("\n")
        bornes = [i for i, l in enumerate(lignes) if l.strip() == "---"]
        corps = "\n".join(lignes[bornes[1] + 1:]) if len(bornes) > 1 else txt
        index[m.group(1)] = (f, {int(n): t.strip() for n, t in TITRE.findall(corps)})
    return index


def regions(chemin):
    """Rend (nom de région, texte) — l'en-tête porte des renvois comme le corps."""
    lignes = io.open(chemin, encoding="utf-8").read().split("\n")
    b = [i for i, l in enumerate(lignes) if l.strip() == "---"]
    if len(b) < 2:
        return [("fichier", "\n".join(lignes))]
    return [("en-tête", "\n".join(lignes[b[0] + 1:b[1]])),
            ("corps", "\n".join(lignes[b[1] + 1:]))]


def contexte(txt, i, large=58):
    d = max(0, i - large)
    return re.sub(r"\s+", " ", txt[d:i + large]).strip()


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--livre", type=int, help="ne contrôler qu'un livre")
    p.add_argument("--muet", action="store_true", help="n'afficher que les défauts")
    a = p.parse_args()

    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
    index = chapitres()
    out.write("%d chapitre(s) indexé(s), %d section(s) numérotée(s).\n\n"
              % (len(index), sum(len(s) for _, s in index.values())))

    vises = sorted(index) if a.livre is None else sorted(
        c for c in index if c.startswith("L%d." % a.livre))
    if a.livre is not None:
        out.write("Contrôle restreint au livre %d : %d chapitre(s).\n\n"
                  % (a.livre, len(vises)))

    morts, total, internes_morts, total_int = [], 0, [], 0
    for cid in vises:
        chemin, _ = index[cid]
        for region, txt in regions(chemin):
            for m in ANCRE_QUALIFIEE.finditer(txt):
                cible, num = m.group(1), int(m.group(2))
                total += 1
                if cible not in index:
                    morts.append((cid, region, m.group(0), "chapitre inexistant",
                                  contexte(txt, m.start())))
                elif num not in index[cible][1]:
                    dispo = sorted(index[cible][1])
                    morts.append((cid, region, m.group(0),
                                  "le chapitre cible n'a pas de § %d (il a %s)"
                                  % (num, ", ".join(map(str, dispo)) or "aucune section numérotée"),
                                  contexte(txt, m.start())))
            if region != "corps":
                continue
            for m in ANCRE_INTERNE.finditer(txt):
                # écarter ce qui est déjà couvert par une ancre qualifiée
                avant = txt[max(0, m.start() - 12):m.start()]
                if re.search(r"L\d+\.C\d+\s*$", avant):
                    continue
                if AUTRE_DOCUMENT.search(txt[max(0, m.start() - 40):m.start()]):
                    continue        # « IPSAS 51 § 10 » : paragraphe d'une norme
                num = int(m.group(1))
                total_int += 1
                if num not in index[cid][1]:
                    internes_morts.append((cid, m.group(0).strip(), num,
                                           sorted(index[cid][1]),
                                           contexte(txt, m.start())))

    out.write("ANCRES QUALIFIÉES « Lx.Cy § n » : %d relevée(s), %d morte(s).\n"
              % (total, len(morts)))
    for cid, region, anc, motif, ctx in morts:
        out.write("\n  %s [%s] — %s\n      %s\n      … %s …\n"
                  % (cid, region, anc, motif, ctx))

    out.write("\nRENVOIS INTERNES « § n » : %d relevé(s), %d À LIRE.\n"
              % (total_int, len(internes_morts)))
    if internes_morts:
        out.write("  AVERTISSEMENT — ceux-ci ne sont PAS comptés comme défauts.\n"
                  "  « § n » sans chapitre nommé peut désigner la section du chapitre\n"
                  "  OU un paragraphe d'un texte cité dont le nom est plus haut dans la\n"
                  "  phrase. Aucun motif ne départage les deux : il faut lire.\n")
    for cid, anc, num, dispo, ctx in internes_morts:
        out.write("\n  %s — « %s » : ce chapitre n'a pas de § %d (il a %s)\n      … %s …\n"
                  % (cid, anc, num, ", ".join(map(str, dispo)) or "aucune", ctx))

    # Seules les ancres QUALIFIÉES font échouer : elles seules sont sans ambiguïté.
    n = len(morts)
    out.write("\n" + ("CONTRÔLE PASSÉ : toutes les ancres pointent sur une section\n"
                      "existante. Le contrôle ne dit RIEN de ce que la section porte.\n"
                      if not n else
                      "%d ANCRE(S) MORTE(S). Chacune est à corriger ou à retirer.\n" % n))
    out.flush()
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
