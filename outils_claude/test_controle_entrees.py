# -*- coding: utf-8 -*-
"""Sabotages de `controle_entrees.py`. Chaque cas dit ce qu'il doit rendre, et
un cas qui passerait à tort fait échouer la batterie.

    python outils_claude/test_controle_entrees.py
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_entrees as c  # noqa: E402

RACINE = c.RACINE
CAS = [
    # (nom, texte de l'entrée, classe attendue ou None)
    ("P1 citation seule",
     "X, Titre, 2004 — « capable of performing well at all of its normal tasks » (page PDF 8).",
     None),
    ("P2 absence seule",
     "X, Titre, 2004. La pièce ne porte pas le chiffre.",
     None),
    ("P3 citation et absence, sans alignement",
     "X, 2004 — « capable of performing well at all of its normal tasks ». "
     "CE QUE LA PIÈCE DIT CONTRE : elle ne porte pas le second chiffre.",
     "a_lire"),
    ("P4 la signature du 28 septembre",
     "X, 2004 — « une dotation de 454 milliards du Trésor ». Le communiqué "
     "ne mentionne pas la dotation — le corps est aligné le 2026-09-15.",
     "corps_aligne"),
    ("P5 un titre court entre guillemets n'est pas une citation",
     "X, « Titre », 2004. La pièce ne porte pas le chiffre, le corps est aligné.",
     None),
    ("P6 majuscules",
     "X — « jointly capable of absorbing adverse disturbances ». LA DÉFINITION "
     "N'Y FIGURE PAS. LE CORPS EST ALIGNÉ.",
     "corps_aligne"),
    ("P7 « malignité » ne vaut pas alignement",
     "X — « jointly capable of absorbing adverse disturbances ». La pièce ne "
     "porte pas le mot malignité.",
     "a_lire"),
]


def main():
    echecs = 0
    for nom, texte, attendu in CAS:
        r = c.examiner(texte)
        obtenu = r[0] if r else None
        ok = obtenu == attendu
        echecs += 0 if ok else 1
        print("%-5s %s — attendu %s, obtenu %s" % ("ok" if ok else "ÉCHEC", nom, attendu, obtenu))

    # Le défaut visé, sur l'état réel qui le portait : L1.C23 avant correction.
    import yaml
    sha = "4f83131a"
    chemin = "corpus/livre-01-monnaie-finance-limites-planetaires/c23-l-economie-de-la-robustesse.md"
    p = subprocess.run(["git", "-C", RACINE, "show", "%s:%s" % (sha, chemin)], capture_output=True)
    if p.returncode != 0:
        print("saut  R1 état historique indisponible (%s absent de ce dépôt)" % sha)
    else:
        h = yaml.safe_load(p.stdout.decode("utf-8").split("---", 2)[1])
        rendu = sorted(s["ref"] for s in h["sources_primaires"]
                       if (c.examiner(s["reference"]) or [None])[0] == "corps_aligne")
        ok = rendu == ["S14", "S6", "S9"]
        echecs += 0 if ok else 1
        print("%-5s R1 L1.C23 à %s rend S6, S9, S14 et elles seules — obtenu %s"
              % ("ok" if ok else "ÉCHEC", sha, rendu))

    print()
    print("%d échec(s)." % echecs)
    return 1 if echecs else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
