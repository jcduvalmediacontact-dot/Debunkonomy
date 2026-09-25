# -*- coding: utf-8 -*-
"""Contrôle de l'appel `[Sn]` contre ce que son entrée de source déclare porter.

CE QUE CE CONTRÔLE ÉTABLIT. Cinq fois en trois jours, la réponse était déjà dans
l'entrée de source et personne ne l'a lue : le corps s'appuyait sur la PROSE de
l'entrée — son titre, son édition, son résumé — là où seule sa liste de passages
lus fait autorité. `controle.py` vérifie l'`etat_lecture` de la source appelée ;
rien ne compare l'appel à ce que l'entrée déclare avoir lu.

CE QU'IL N'ÉTABLIT PAS, et il faut le dire : que le passage déclaré porte
réellement l'énoncé. Un passage cité qui parle d'autre chose passe ce contrôle.
Seule une lecture le verrait. Il ne dit pas non plus qu'un passage manquant est
un défaut : une série de données n'a pas de phrase à citer.

TROIS ÉTATS D'ENTRÉE, ET NON UN BOOLÉEN — comme `controle_chiffres.py`, et pour
la même raison : un booléen ferait disparaître en silence les 169 entrées du
Livre 1 qui n'emploient pas le marqueur de lecture, dont beaucoup sont des
séries statistiques légitimes.

    passage_declare   un marqueur de lecture, et une citation après lui.
    sans_marqueur     des citations, mais aucun marqueur : la citation peut
                      n'être qu'un TITRE. C'est le défaut réel visé ici —
                      « l'entrée donne le passage qui porte l'énoncé, ni un
                      titre, ni un mot du résumé » (CLAUDE.md).
    sans_citation     aucune citation du tout : le signal le plus fort.

LE MARQUEUR N'EST PAS UNE FORMULE FIXE. Douze variantes existent dans le Livre 1
— « Passages lus », « Passage employé ici », « passages pertinents lus »,
« passages relus le »… Chercher une seule forme manquerait une entrée sur trois.

L'APPEL SUIT SOUVENT LE POINT. Le corpus écrit « … la règle tient. [S4] » : la
phrase que l'appel couvre est celle qui PRÉCÈDE. L'outil le prend en compte ;
ne pas le faire rendrait un défaut à chaque appel de fin de paragraphe.

LE RECOUVREMENT DE MOTS SE FAIT SUR LES JETONS DISCRIMINANTS, jamais sur tous
les mots : les passages sont en anglais et le corps en français. Ce qui se
partage, ce sont les nombres, les noms propres et les mots longs. Un test naïf
crierait sur presque tous les appels.

AVERTISSEMENTS, JAMAIS BLOCAGES. Cet outil est hors du chemin de publication et
ne touche pas `controle.py`, qui reste l'autorité. Code de sortie : 0 si aucun
appel orphelin ni entrée sans citation, 1 sinon.

    python outils_claude/controle_appels.py
    python outils_claude/controle_appels.py --livre 1
    python outils_claude/controle_appels.py --livre 1 --tout   # toutes les classes
"""
import argparse
import glob
import io
import os
import re
import sys

import yaml

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

APPEL = re.compile(r"\[S(\d+)(?:,[^\]]*)?\]")
# Douze variantes relevees dans le Livre 1 : on cherche le mot `passage` suivi,
# dans la meme proposition, d'un verbe de lecture ou d'emploi.
MARQUEUR = re.compile(r"(?i)\bpassages?\b.{0,60}?\b(lus?|lue|employ|relus?|pertinent)")
CITATION = re.compile("«([^»]{3,})»")
# UNE GRAMMAIRE, ET NON UNE CLASSE DE SEPARATEURS. La premiere version etait
# `\d[\d   ,.]*\d`, qui avalait « 2015, 53,2 » d'un seul trait et
# rendait `2015532` : un nombre inexistant, absent de toute piece, donc signale
# a coup sur. Les milliers se separent par une espace fine ou insecable, la
# decimale par une virgule ou un point — mais « virgule espace » separe DEUX
# nombres, et c'est ce que l'ancienne classe confondait.
NOMBRE = re.compile(r"\d+(?:[   ]\d{3})*(?:[.,]\d+)?")
# LES NOMBRES ECRITS EN MOTS SONT EXCLUS, et c'est une decision, non un oubli.
# La deuxieme ecriture les prenait : sur cinq cas tires au sort, TROIS etaient
# des faux positifs dus a eux seuls — « une planete » rendait 1, « deux
# operations differentes » rendait 2. En francais l'article indefini est un
# nombre ecrit en mots. Dans ce corpus un fait chiffre s'ecrit en chiffres ;
# un nombre en mots est de la prose.
#
# Ce qui n'est pas un fait chiffre : renvoi, section, page, folio, article.
HORS_CHAMP = re.compile(
    r"L\d+\.C\d+(?:\s*§\s*\d+)?"          # renvoi L1.C08 § 4
    r"|§\s*\d+"                            # § 4
    r"|(?i:p\.|pages?|folios?|art\.|articles?|section|chapitre)\s*[\dxivl]+"
    r"(?:\s*[-–]\s*[\dxivl]+)?"
    # QUANTIEME : « le 11 mars 2020 » rendait 11, et 11 n'est pas un fait.
    r"|\d{1,2}(?:er)?\s+(?i:janvier|février|mars|avril|mai|juin|juillet"
    r"|août|septembre|octobre|novembre|décembre|january|february|march"
    r"|april|june|july|august|september|october|november|december)"
    # DATE ISO : `2026-09-23` rendait 9 et 23, et le corpus en est plein.
    r"|\d{4}-\d{2}-\d{2}"
    # FORMULE OU IDENTIFIANT : un chiffre COLLE a une lettre n'est jamais une
    # quantite en francais. `CO2` rendait 2 — et ce corpus l'ecrit a chaque
    # page. Emporte aussi CH4, N2O, SO2, B1GQ, CLV10_MEUR.
    r"|[A-Za-z]+\d+[A-Za-z_]*")


def tetes(valeurs):
    """Les trois premiers chiffres significatifs — la granularité ne trahit pas.

    Le corps écrit « 4 311,9 milliards », le passage « 4,311,911 » : c'est le
    MEME nombre, et les deux jetons diffèrent. De même « 2 344 milliards »
    contre « up to $2.3 trillion ». On compare donc les têtes, sur la longueur
    de la plus courte des deux, plutôt que les chaînes entières.
    """
    return {v[:3] for v in valeurs} | {v[:2] for v in valeurs}


def lire(chemin):
    t = io.open(chemin, encoding="utf-8").read()
    if not t.startswith("---"):
        return None, None
    entete, corps = t.split("\n---\n", 1)
    return yaml.safe_load(entete.split("---", 1)[1]), corps


def passages_de(reference):
    """Les citations qui suivent un marqueur de lecture, et l'état de l'entrée."""
    citations = [m.group(1).strip() for m in CITATION.finditer(reference)]
    marque = MARQUEUR.search(reference)
    if not citations:
        return "sans_citation", []
    if not marque:
        return "sans_marqueur", citations
    # Seules les citations POSTERIEURES au marqueur sont des passages ; celle
    # qui le precede est le titre de la piece.
    apres = [m.group(1).strip() for m in CITATION.finditer(reference)
             if m.start() > marque.start()]
    return ("passage_declare", apres) if apres else ("sans_marqueur", citations)


def chiffres_de(texte):
    """Les nombres d'un texte, sous une forme comparable d'une langue à l'autre.

    POURQUOI LES NOMBRES ET NON LES MOTS. La première écriture comparait les
    mots de la phrase à ceux des passages. Sur cinq cas tirés au sort, CINQ
    ÉTAIENT DES FAUX POSITIFS : `productivité` contre `productivity`,
    `atmosphère` contre `Atmospheric`, `idéaux-types` contre `idéaltype`, un
    passage en allemand, et un `six` que le filtre de longueur jetait. Un
    contrôle qui crie sur tout obtient un sans-faute.

    Les nombres, eux, traversent les langues intacts. Et c'est la règle que le
    projet écrit : un chiffre n'entre au corps « qu'avec un appel `[Sn]` vers
    une pièce lue QUI LE PORTE ».
    """
    out = set()
    texte = HORS_CHAMP.sub(" ", texte)
    for n in NOMBRE.findall(texte):
        brut = re.sub(r"[^\d]", "", n)
        if not brut:
            continue
        val = brut.lstrip("0") or "0"
        if len(val) == 4 and 1500 <= int(val) <= 2100:
            continue                      # millésime : ce n'est pas un fait chiffré
        out.add(val)
    return out


def phrase_de(corps, debut, fin):
    """La phrase que l'appel couvre — celle d'AVANT si l'appel suit le point."""
    avant = corps[:debut]
    if re.search(r"[.!?]\s*$", avant):
        avant = re.sub(r"[.!?]\s*$", "", avant)
        d = max(avant.rfind(". "), avant.rfind("\n\n"), avant.rfind("! "),
                avant.rfind("? "))
        return avant[d + 1:]
    d = max(avant.rfind(". "), avant.rfind("\n\n"))
    reste = corps[fin:]
    f = re.search(r"[.!?](\s|$)|\n\n", reste)
    return avant[d + 1:] + (reste[:f.start()] if f else reste[:160])


def main():
    p = argparse.ArgumentParser(description="L'appel [Sn] contre les passages "
                                            "que son entrée déclare avoir lus.")
    p.add_argument("--livre", type=int, help="un livre seulement")
    p.add_argument("--tout", action="store_true",
                   help="montre aussi les classes sans_marqueur")
    a = p.parse_args()
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)

    motif = "livre-%02d-*" % a.livre if a.livre else "livre-*"
    fichiers = sorted(glob.glob(os.path.join(CORPUS, motif, "c*.md")))
    if not fichiers:
        out.write("Aucun chapitre pour ce filtre.\n")
        return 2

    bilan = {"appel_orphelin": [], "sans_citation": [], "sans_marqueur": [],
             "chiffre_non_porte": []}
    n_appels = n_entrees = n_chap = 0

    for chemin in fichiers:
        entete, corps = lire(chemin)
        if not entete:
            continue
        n_chap += 1
        cid = str(entete.get("chapitre"))
        entrees = {}
        for s in (entete.get("sources_primaires") or []):
            n_entrees += 1
            ref = str(s.get("ref") or "")
            etat, passages = passages_de(str(s.get("reference") or ""))
            entrees[ref] = (etat, passages)
            if etat == "sans_citation":
                bilan["sans_citation"].append((cid, ref))
            elif etat == "sans_marqueur":
                bilan["sans_marqueur"].append((cid, ref))

        vus = set()
        for m in APPEL.finditer(corps):
            n_appels += 1
            ref = "S" + m.group(1)
            if ref not in entrees:
                bilan["appel_orphelin"].append((cid, ref, m.group(0)))
                continue
            etat, passages = entrees[ref]
            if etat != "passage_declare":
                continue          # deja signale au titre de l'entree
            phrase = phrase_de(corps, m.start(), m.end())
            # L'appel lui-meme porte parfois une page : `[S1, p. 393]`. Ce
            # nombre-la n'est pas un fait du corps, on le retire de la phrase.
            sans_appel = APPEL.sub(" ", phrase)
            du_corps = chiffres_de(sans_appel)
            portes = tetes(chiffres_de(" ".join(passages)))
            manquants = {v for v in du_corps
                         if v[:3] not in portes and v[:2] not in portes}
            if manquants and (cid, ref) not in vus:
                vus.add((cid, ref))
                bilan["chiffre_non_porte"].append(
                    (cid, ref, "%s | %s" % (",".join(sorted(manquants)[:4]),
                                            phrase.strip()[:88])))

    out.write("%d chapitre(s), %d entrée(s) de source, %d appel(s) [Sn]\n\n"
              % (n_chap, n_entrees, n_appels))

    def bloc(cle, titre, avec_detail=True, montre=True):
        liste = bilan[cle]
        out.write("%s  [%d]\n" % (titre, len(liste)))
        if not montre:
            out.write("    (--tout pour les voir)\n\n")
            return
        for entree in liste:
            if avec_detail and len(entree) == 3:
                out.write("    %-9s %-4s %s\n" % (entree[0], entree[1], entree[2]))
            else:
                out.write("    %-9s %s\n" % (entree[0], entree[1]))
        out.write("\n" if liste else "    aucun\n\n")

    bloc("appel_orphelin", "APPELS ORPHELINS — aucune entrée de ce nom")
    bloc("sans_citation", "ENTRÉES SANS AUCUNE CITATION", avec_detail=False)
    bloc("sans_marqueur", "ENTRÉES DONT LA CITATION PEUT N'ÊTRE QU'UN TITRE",
         avec_detail=False, montre=a.tout)
    bloc("chiffre_non_porte",
         "APPELS DONT LA PHRASE PORTE UN CHIFFRE QU'AUCUN PASSAGE NE PORTE")

    out.write("Avertissements seulement. `corpus/controle.py` reste l'autorité ;\n"
              "aucun de ces points ne refuse une publication.\n")
    out.flush()
    return 1 if (bilan["appel_orphelin"] or bilan["sans_citation"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
