# -*- coding: utf-8 -*-
"""Contrôle du `resume` contre le corps : ce que l'en-tête annonce et qu'on ne
trouve pas.

CE QUE CE CONTRÔLE ÉTABLIT. Le `resume` est la partie du chapitre qu'une IA
extraira le plus souvent, et c'est la seule que personne ne relit après une
réécriture du corps. Deux fois en trois jours, un corps corrigé a laissé son
résumé affirmer ce que le corps venait de retirer — une fois sur L1.C10, dont le
résumé disait encore Wörgl interdit au nom du monopole quatre sweeps après que le
corps avait cessé de le dire. La règle est dans ma mémoire de travail :
« balayer l'en-tête autant que le corps ; un contrôle qui ne lit que le corps
mente ». Rien ne le faisait.

ICI LA COMPARAISON DE MOTS EST VALIDE, et c'est ce qui distingue ce contrôle de
`controle_appels.py`. Là-bas les pièces sont en anglais et en allemand : les mots
ne se rencontrent pas, et le test a dû être abandonné. Ici le `resume` et le
corps sont du même auteur, dans la même langue, à quelques heures d'écart.

DEUX RELEVÉS, ET LE SECOND EST LE PLUS SÛR :

    enonce_sans_appui   un énoncé du résumé dont AUCUN mot discriminant
                        n'apparaît au corps. Un résumé reformule : c'est donc un
                        signal faible, à lire, jamais un verdict.
    chiffre_absent      un nombre du résumé absent du corps. Signal fort : un
                        résumé ne doit porter aucun chiffre que le corps ne
                        porte pas.

CE QU'IL N'ÉTABLIT PAS : qu'un énoncé retrouvé au corps y soit encore VRAI. Le
résumé de L1.C10 employait les mêmes mots que son corps tout en lui faisant dire
l'inverse. Seule une lecture le verrait.

Les règles d'extraction — élisions, formules `CO2`, dates ISO, quantièmes,
granularité décimale — sont importées de `controle_appels.py` plutôt que
réécrites : deux écritures de la même règle divergent, et `test_generer.py` en a
fourni la démonstration le 2026-09-25.

AVERTISSEMENTS, JAMAIS BLOCAGES. Hors du chemin de publication ; ne touche pas
`controle.py`. Code de sortie : 0 si aucun chiffre absent, 1 sinon.

    python outils_claude/controle_resume.py --livre 1
    python outils_claude/controle_resume.py --livre 1 --tout
"""
import argparse
import glob
import io
import os
import re
import sys

import yaml

from controle_appels import HORS_CHAMP, chiffres_de, lire, tetes  # une seule vérité

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

# Mots outils : leur présence au corps ne prouve rien.
OUTILS = set("""a afin ainsi alors apres au aucun aucune aussi autre autres aux
avant avec car ce cela ces cet cette ceux chaque comme dans de des deux donc dont
du elle elles en encore entre est et eux fait faire ici il ils la le les leur
leurs lui mais meme mieux moins ne ni non nos notre nous on ou par parce pas
peut plus plutot pour pourquoi puis quand que quel quelle qui quoi sa sans se
selon ses seul seule si sinon soit son sont sous sur ta tandis tant te tel telle
toi ton tous tout toute toutes trois tu un une va vers vos votre vous y
chapitre corpus propose expose examine montre etablit second premiere""".split())


def vocabulaire():
    """Les noms du vocabulaire : un concept nommé au résumé doit l'être au corps."""
    chemin = os.path.join(CORPUS, "vocabulaire.yaml")
    if not os.path.exists(chemin):
        return set()
    termes = set()
    for e in yaml.safe_load(io.open(chemin, encoding="utf-8").read()) or []:
        for cle in ("terme", "libelle"):
            v = str(e.get(cle) or "").strip().lower()
            if v:
                termes.add(v.replace("_", " "))
    return termes


def radical(mot):
    """Coupe les finales pour que singulier et pluriel se rencontrent.

    LA PREMIERE VERSION NE CONVERGEAIT PAS : elle retirait UNE finale parmi
    `s`, `e`, `x`, de sorte que `catégories` donnait `catégorie` et `catégorie`
    donnait `catégori` — deux radicaux différents pour le même mot. Le contrôle
    déclarait donc absent du corps un mot qui y était. On retire d'abord la
    marque du pluriel, ensuite le `e` muet, pour que les deux tombent au même
    endroit.
    """
    if len(mot) > 5 and mot[-1] in "sx":
        mot = mot[:-1]
    if len(mot) > 5 and mot[-1] == "e":
        mot = mot[:-1]
    return mot


def mots_de(texte):
    """Les mots discriminants : ni outils, ni trop courts, élisions découpées."""
    out = set()
    texte = HORS_CHAMP.sub(" ", texte)
    for brut in re.findall(r"[A-Za-zÀ-ɏ][A-Za-zÀ-ɏ'’-]*", texte):
        for mot in re.split(r"['’]", brut):
            bas = mot.lower().strip("-")
            if len(bas) < 5 or bas in OUTILS:
                continue
            out.add(radical(bas))
    return out


def enonces(resume):
    """Les énoncés du résumé : une phrase, ou un membre séparé par « : » ou « ; »."""
    morceaux = re.split(r"(?<=[.!?])\s+|\s*[;:]\s+", str(resume))
    return [m.strip() for m in morceaux if len(m.strip()) > 25]


def main():
    p = argparse.ArgumentParser(description="Le resume d'un chapitre contre son corps.")
    p.add_argument("--livre", type=int)
    p.add_argument("--tout", action="store_true",
                   help="montre aussi les énoncés sans appui")
    a = p.parse_args()
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)

    motif = "livre-%02d-*" % a.livre if a.livre else "livre-*"
    fichiers = sorted(glob.glob(os.path.join(CORPUS, motif, "c*.md")))
    if not fichiers:
        out.write("Aucun chapitre pour ce filtre.\n")
        return 2

    voc = vocabulaire()
    sans_appui, chiffres = [], []
    n_chap = n_enonces = 0

    for chemin in fichiers:
        entete, corps = lire(chemin)
        if not entete or not entete.get("resume"):
            continue
        n_chap += 1
        cid = str(entete.get("chapitre"))
        resume = str(entete["resume"])
        mots_corps = mots_de(corps)
        chiffres_corps = tetes(chiffres_de(corps))

        for manquant in sorted(chiffres_de(resume)):
            if manquant[:3] not in chiffres_corps and manquant[:2] not in chiffres_corps:
                chiffres.append((cid, manquant, resume[:0] or ""))

        for enonce in enonces(resume):
            n_enonces += 1
            mots = mots_de(enonce)
            # Un terme du vocabulaire nommé au résumé compte pour un mot.
            cles = {m for m in mots if m in mots_corps}
            nommes = {t for t in voc if t in enonce.lower()}
            if not cles and not (nommes & {t for t in voc if t in corps.lower()}):
                sans_appui.append((cid, enonce[:104], len(mots)))

    out.write("%d chapitre(s) à résumé, %d énoncé(s) relevé(s)\n\n"
              % (n_chap, n_enonces))

    out.write("CHIFFRES DU RÉSUMÉ ABSENTS DU CORPS  [%d]\n" % len(chiffres))
    for cid, v, _ in chiffres:
        out.write("    %-9s %s\n" % (cid, v))
    out.write("\n" if chiffres else "    aucun\n\n")

    out.write("ÉNONCÉS DU RÉSUMÉ SANS AUCUN MOT AU CORPS  [%d]\n" % len(sans_appui))
    if a.tout:
        for cid, e, n in sans_appui:
            out.write("    %-9s (%d mots) %s\n" % (cid, n, e))
        out.write("\n" if sans_appui else "    aucun\n\n")
    else:
        out.write("    (--tout pour les voir)\n\n")

    out.write("Avertissements seulement. `corpus/controle.py` reste l'autorité.\n")
    out.flush()
    return 1 if chiffres else 0


if __name__ == "__main__":
    raise SystemExit(main())
