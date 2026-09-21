# -*- coding: utf-8 -*-
"""Contrôle des énoncés chiffrés sans appel de source.

POURQUOI CE CONTRÔLE EXISTE. La règle est dans CLAUDE.md : « Un chiffre issu
d'une recherche assistée est une piste. Il n'entre au corps à l'indicatif
qu'avec un appel `[Sn]` vers une pièce lue qui le porte. Un énoncé chiffré sans
appel est INVISIBLE POUR E-L4. » `controle.py` vérifie l'état de lecture des
sources appelées ; il ne peut rien dire d'un chiffre qui n'appelle personne.

TROIS ÉTATS, ET NON UN BOOLÉEN. Règle arrêtée par l'auteur le 2026-09-20 :

    defaut_potentiel  `::etat::` sans appel — un fait est avancé sans pièce.
    a_relire          paragraphe non balisé d'un chapitre `hybride`, et tout
                      nombre sous `::hypothese::` : le nombre peut être un
                      paramètre ou une conséquence du modèle, ce n'est pas un
                      défaut de source, mais cela se signale.
    hors_champ        `::norme::`, millésimes, renvois, identifiants.

Un booléen ferait disparaître en silence les chiffres hypothétiques et ceux des
paragraphes hybrides, qui méritent au moins d'être vus.

L'ORDRE DE DÉCISION COMPTE. Les exclusions de FORME priment sur le régime : un
millésime dans un `::etat::` est un millésime, pas un fait à sourcer.

CE QU'IL NE FAIT PAS. Il ne dit pas si la source appelée porte réellement le
chiffre — seule une lecture le dirait, et l'entrée de source est là pour ça.

Il ne touche à rien. Code de sortie : 0 si aucun `defaut_potentiel`, 1 sinon.

    python outils_claude/controle_chiffres.py --livre 1
    python outils_claude/controle_chiffres.py --livre 1 --etat a_relire
    python outils_claude/controle_chiffres.py --livre 1 --tout
"""
import argparse
import io
import os
import re
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(RACINE, "corpus")

APPEL = re.compile(r"\[S\d+")
MARKDOWN = re.compile(r"\*{1,3}|`")
# Identifiants de chapitre et appels de source : MASQUÉS avant tout relevé.
# Relevé le 2026-09-20 : sans ce masque, « L1.C03 » rendait un nombre « 1 »
# classé defaut_potentiel — le « L » seul n'est pas un acronyme, et le filtre
# par ce qui précède ne pouvait pas l'attraper.
MASQUE = re.compile(r"L\d+\.C\d+(?:\s*§+\s*\d+)?|\[[^\]]*\]")
COUPE = re.compile(r"(?<=[.!?])\s+")
NOMBRE = re.compile(r"\d[\d   ]*(?:[.,]\d+)?")
BALISE = re.compile(r"^::(\w+)::")

DEFAUT, RELIRE, HORS = "defaut_potentiel", "a_relire", "hors_champ"

# --- exclusions de FORME, qui priment sur le régime ------------------------
# Un renvoi : le nombre est un numéro de section, de page, d'article, de livre.
RENVOI_AVANT = re.compile(
    r"(?:§+|section|sections|chapitre|chapitres|livre|livres|partie|"
    r"p\.|pp\.|page|pages|art\.|article|articles|alinéa|point|points|"
    r"tableau|figure|annexe|note|étape|condition|question)\s*$", re.I)
# Un identifiant : acronyme de norme (IPSAS 47, BPM6, SNA 2025, IAS 37), ou
# l'intérieur d'un appel de source, ou un identifiant de chapitre L1.C08.
IDENTIFIANT_AVANT = re.compile(
    r"(?:[A-ZÉÈÀÙÂÊÎÔÛ]{2,}\s*|\[S\d+[^\]]*|L\d+\.C|\bC\d*|/)$")
# Un code normatif complet : 2011/452/UE, ISO 14001, 2017/C 411/04.
CODE = re.compile(r"\d+\s*/\s*[\dA-Z]")


MOIS = (r"janvier|février|mars|avril|mai|juin|juillet|août|septembre|"
        r"octobre|novembre|décembre")
QUANTIEME = re.compile(r"\d{1,2}(?:er)?\s+(?:%s)" % MOIS, re.I)
COLLE = re.compile(r"[A-Za-zÀ-ÿ+]")


def est_quantieme(phrase, deb):
    """« le 13 septembre 2023 » : le 13 est un quantième, pas une grandeur."""
    return bool(QUANTIEME.match(phrase[deb:deb + 24]))


def est_colle(phrase, deb, fin):
    """« Rio+20 », « 21st-Century », « COP21 » : le chiffre appartient à un nom."""
    av = phrase[deb - 1] if deb else " "
    ap = phrase[fin] if fin < len(phrase) else " "
    return bool(COLLE.fullmatch(av) or COLLE.fullmatch(ap))


def est_millesime(phrase, deb, fin, brut):
    """Un nombre de quatre chiffres entre 1500 et 2100, non suivi d'une unité."""
    if not re.fullmatch(r"\d{4}", brut):
        return False
    if not 1500 <= int(brut) <= 2100:
        return False
    # « 1971 tonnes » n'est pas un millésime ; « en 1971 », « de 2023 », si.
    suite = phrase[fin:fin + 24].lstrip()
    if re.match(r"(?:tonnes?|milliards?|millions?|milliers?|km|km2|hectares?|"
                r"dollars?|euros?|%|habitants?|espèces?|points?)\b", suite, re.I):
        return False
    return True


def classer(phrase, deb, fin, brut, regime, regime_chapitre):
    """Rend un des trois états, et le motif en clair.

    L'ordre est celui des exclusions de forme d'abord, du régime ensuite :
    c'est ce qui empêche un millésime de `::etat::` de devenir un défaut.
    """
    avant = phrase[max(0, deb - 32):deb]
    autour = phrase[max(0, deb - 8):fin + 8]

    if est_millesime(phrase, deb, fin, brut):
        return HORS, "millésime"
    if est_quantieme(phrase, deb):
        return HORS, "quantième de date"
    if est_colle(phrase, deb, fin):
        return HORS, "chiffre d'un nom propre"
    if RENVOI_AVANT.search(avant):
        return HORS, "renvoi"
    if IDENTIFIANT_AVANT.search(avant):
        return HORS, "identifiant"
    if CODE.search(autour):
        return HORS, "code normatif"

    # Un paragraphe non balisé porte le régime du chapitre (convention § 8).
    effectif = regime_chapitre if regime == "défaut" else regime
    if effectif == "norme":
        return HORS, "régime ::norme::"
    if effectif == "etat" or effectif == "descriptif":
        if regime == "défaut":
            return DEFAUT, "non balisé, chapitre « %s »" % regime_chapitre
        return DEFAUT, "::etat:: sans appel"
    if effectif == "hypothese":
        return RELIRE, ("::hypothese::" if regime != "défaut"
                        else "non balisé, chapitre « hypothese »")
    if effectif == "conception":
        return HORS, "chapitre de régime « conception »"
    # `hybride` n'est défini nulle part dans la convention : hériter de ce
    # défaut-là ne tranche rien, donc on relit.
    return RELIRE, ("non balisé, chapitre « hybride »" if regime == "défaut"
                    else "régime « %s »" % effectif)


def entete_et_corps(chemin):
    lignes = io.open(chemin, encoding="utf-8").read().split("\n")
    b = [i for i, l in enumerate(lignes) if l.strip() == "---"]
    tete = "\n".join(lignes[b[0] + 1:b[1]]) if len(b) > 1 else ""
    corps = lignes[b[1] + 1:] if len(b) > 1 else lignes
    m = re.search(r"(?m)^regime:\s*(\w+)\s*$", tete)
    rc = m.group(1) if m else "inconnu"
    paras = []
    for l in corps:
        s = l.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        mb = BALISE.match(s)
        paras.append((mb.group(1) if mb else "défaut", BALISE.sub("", s).strip()))
    return rc, paras


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--livre", type=int)
    p.add_argument("--etat", choices=[DEFAUT, RELIRE, HORS],
                   help="n'afficher qu'un état (défaut : defaut_potentiel)")
    p.add_argument("--tout", action="store_true", help="afficher les trois états")
    a = p.parse_args()
    out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)

    motif = os.path.join(CORPUS, "livre-%s*" % ("%02d" % a.livre if a.livre else ""),
                         "c*.md")
    releve, avec_appel, examines = [], 0, 0
    for f in sorted(glob.glob(motif)):
        cid = os.path.basename(f)
        examines += 1
        rc, paras = entete_et_corps(f)
        for regime, para in paras:
            clair = MARKDOWN.sub("", para)
            # Le masque garde la LONGUEUR : les positions restent justes, et
            # les crochets deviennent atomiques — « [S5, p. 393-394] » contient
            # le point de « p. », qui coupait la phrase et faisait compter des
            # numéros de PAGE comme des grandeurs sans appel.
            masq = MASQUE.sub(lambda x: "·" * len(x.group(0)), clair)
            bornes = [0]
            for c in COUPE.finditer(masq):
                if clair[c.end():c.end() + 2] == "[S":
                    continue          # l'appel suit le point : même phrase
                bornes.append(c.end())
            bornes.append(len(masq))
            for i in range(len(bornes) - 1):
                d, f = bornes[i], bornes[i + 1]
                ph_clair, ph = clair[d:f], masq[d:f]
                if not ph.strip():
                    continue
                porte_appel = bool(APPEL.search(ph_clair))
                for m in NOMBRE.finditer(ph):
                    brut = m.group(0).strip()
                    if porte_appel:
                        avec_appel += 1
                        continue
                    etat, motif_c = classer(ph, m.start(), m.end(), brut, regime, rc)
                    releve.append((cid, rc, regime, brut, etat, motif_c,
                                   re.sub(r"\s+", " ", ph_clair)[:170]))

    par_etat = {e: [r for r in releve if r[4] == e] for e in (DEFAUT, RELIRE, HORS)}
    out.write("%d chapitre(s) balayé(s). %d nombre(s) écarté(s) d'office : leur "
              "phrase porte un appel [Sn].\n\n" % (examines, avec_appel))
    out.write("RELEVÉ — %d nombre(s) sans appel de source\n" % len(releve))
    for e in (DEFAUT, RELIRE, HORS):
        out.write("  %-18s %5d\n" % (e, len(par_etat[e])))
    out.write("\n")

    montres = ([DEFAUT, RELIRE, HORS] if a.tout else [a.etat or DEFAUT])
    for e in montres:
        out.write("\n" + "=" * 78 + "\n%s — %d\n" % (e.upper(), len(par_etat[e]))
                  + "=" * 78 + "\n")
        for cid, rc, regime, brut, _, motif_c, ctx in par_etat[e]:
            out.write("  %-44s « %s »  [%s]\n      … %s …\n"
                      % (cid[:44], brut, motif_c, ctx))

    n = len(par_etat[DEFAUT])
    out.write("\n%s\n" % ("CONTRÔLE PASSÉ : aucun énoncé de fait chiffré sans appel."
                          if not n else
                          "%d défaut(s) potentiel(s). Le contrôle NE DIT PAS qu'ils sont\n"
                          "faux : il dit qu'aucune pièce n'est appelée pour les porter." % n))
    out.flush()
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
