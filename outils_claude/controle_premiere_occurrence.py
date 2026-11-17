# -*- coding: utf-8 -*-
"""Contrôle du champ `premiere_occurrence` du vocabulaire, contre les chapitres.

CE QUE CE CONTRÔLE ÉTABLIT. Le § 9 de la convention définit
`premiere_occurrence` comme « le premier chapitre, dans l'ordre du corpus —
numéro de livre, puis numéro de chapitre —, hors livre 0, qui rapporte sans
démontrer, dont le champ `concepts` déclare le terme ». Trois conditions, donc,
et ce script les vérifie une par une pour chaque terme de
`corpus/vocabulaire.yaml` :

    1. le chapitre nommé EXISTE ;
    2. il DÉCLARE le terme dans son champ `concepts` ;
    3. il est bien le PREMIER à le déclarer, hors livre 0.

Pour chaque écart, il donne aussi le chapitre qui serait juste — celui qui
déclare le terme le premier —, ou « aucun » si personne ne le déclare hors
livre 0. L'écart devient ainsi réparable sans relire le corpus.

POURQUOI IL EXISTE. Ni `controle.py` ni `generer.py` ne lisent ce champ :
`emettre_glossaire` imprime sa valeur telle quelle sur la page publique du
glossaire. Un `premiere_occurrence` faux traverse donc tous les contrôles et
paraît en toutes lettres sur le site. Les onze termes du Livre 6 entrés le
2026-11-17 (ordre 53) portent cet écart, l'auteur l'ayant tranché en
connaissance de cause : « Les onze, et corriger après ». Ce script est ce qui
rend la dette impossible à oublier.

CE QU'IL N'ÉTABLIT PAS. Qu'un terme soit bien nommé, bien défini, ou employé à
propos. Il ne dit rien du corps des chapitres : le champ `concepts` d'un
en-tête est sa seule matière, et un concept employé dans un corps sans être
déclaré dans l'en-tête lui est invisible. Il ne signale pas non plus un concept
employé hors du vocabulaire : c'est `controle.py` qui bloque là-dessus, et ce
script ne réimplémente aucune de ses règles.

IL NE BLOQUE RIEN ET NE MODIFIE RIEN. `controle.py` reste l'autorité ; ce
script est hors du chemin de publication, lit les fichiers et n'en écrit aucun.
Mais il rend un CODE DE SORTIE NON NUL dès qu'il trouve un écart : un contrôle
qui ne rend qu'un rapport laisse continuer, et un écart qu'aucun script ne
regarde traverse les contrôles — ce qui s'est vu sur trois cycles.

    0   aucun écart
    1   au moins un écart
    2   le contrôle n'a pas pu être mené (fichier manquant, YAML invalide,
        identifiant dupliqué) — ce n'est pas un verdict sur le corpus

    python outils_claude/controle_premiere_occurrence.py
    python outils_claude/controle_premiere_occurrence.py --tout
    python outils_claude/controle_premiere_occurrence.py --corpus <dossier>
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

RE_ID = re.compile(r"^L(\d+)\.C(\d+)$")
# Les pages ÉMISES vivent sous un dossier à chiffres seuls (`livre-6/c05/`) ;
# les sources sous `livre-06-un-slug/`. Le motif ci-dessous écarte les
# premières, qui ne sont pas des chapitres.
RE_DOSSIER_EMIS = re.compile(r"^livre-\d+$")

# Les six verdicts. Un seul est conforme ; les cinq autres sont des écarts.
CONFORME = "conforme"
VERDICTS = [
    CONFORME,
    "champ_absent",      # pas de `premiere_occurrence`, ou valeur hors forme
    "livre_0",           # nomme un chapitre du livre 0, que le § 9 exclut
    "chapitre_absent",   # nomme un chapitre qui n'existe pas
    "non_declare",       # le chapitre existe mais ne déclare pas le terme
    "pas_le_premier",    # il le déclare, mais un chapitre antérieur aussi
]


def rang(identifiant):
    """Ordre du corpus : numéro de livre, puis numéro de chapitre."""
    m = RE_ID.match(str(identifiant))
    return (int(m.group(1)), int(m.group(2))) if m else None


def charger_chapitres(corpus):
    """{identifiant: (rang, nom de fichier, ensemble des concepts déclarés)}.

    Même famille de fichiers que `controle.py` : `livre-*/*.md`, en-tête YAML
    ouvert et refermé par `---`.
    """
    chapitres, obstacles = {}, []
    motif = os.path.join(corpus, "livre-*", "*.md")
    for chemin in sorted(glob.glob(motif)):
        dossier = os.path.basename(os.path.dirname(chemin))
        if RE_DOSSIER_EMIS.match(dossier):
            continue
        nom = os.path.relpath(chemin, corpus).replace(os.sep, "/")
        brut = io.open(chemin, encoding="utf-8").read()
        if not brut.startswith("---"):
            obstacles.append("%s : en-tête YAML absent" % nom)
            continue
        bouts = brut.split("---", 2)
        if len(bouts) < 3:
            obstacles.append("%s : en-tête YAML non refermé" % nom)
            continue
        try:
            entete = yaml.safe_load(bouts[1])
        except yaml.YAMLError as e:
            obstacles.append("%s : YAML invalide : %s" % (nom, e))
            continue
        if not isinstance(entete, dict):
            obstacles.append("%s : en-tête vide ou mal formé" % nom)
            continue
        if entete.get("partie", 1) != 1:
            continue
        cle = entete.get("chapitre")
        if not cle:
            obstacles.append("%s : champ « chapitre » absent" % nom)
            continue
        if rang(cle) is None:
            obstacles.append("%s : identifiant hors forme Lx.Cy : %r" % (nom, cle))
            continue
        if cle in chapitres:
            obstacles.append("%s : identifiant dupliqué : %s, déjà porté par %s"
                             % (nom, cle, chapitres[cle][1]))
            continue
        concepts = entete.get("concepts") or []
        if not isinstance(concepts, list):
            obstacles.append("%s : champ « concepts » n'est pas une liste" % nom)
            concepts = []
        chapitres[cle] = (rang(cle), nom, set(concepts))
    return chapitres, obstacles


def charger_vocabulaire(corpus):
    chemin = os.path.join(corpus, "vocabulaire.yaml")
    contenu = yaml.safe_load(io.open(chemin, encoding="utf-8").read())
    if not isinstance(contenu, list):
        raise ValueError("%s : liste attendue" % chemin)
    entrees = []
    for e in contenu:
        if isinstance(e, dict) and "terme" in e:
            entrees.append(e)
    return entrees


def premiers_declarants(chapitres):
    """{terme: identifiant du premier chapitre, hors livre 0, qui le déclare}.

    Hors livre 0 : le § 9 l'écarte parce qu'il rapporte sans démontrer. Le
    livre 0 est donc absent du calcul, et non pas rangé après les autres.
    """
    premier = {}
    for cle, (r, _nom, concepts) in chapitres.items():
        if r[0] == 0:
            continue
        for terme in concepts:
            if terme not in premier or r < chapitres[premier[terme]][0]:
                premier[terme] = cle
    return premier


def juger(entree, chapitres, premier):
    """Rend (verdict, déclaré, attendu). `attendu` est le chapitre qui serait
    juste, ou None si aucun chapitre hors livre 0 ne déclare le terme."""
    terme = entree["terme"]
    attendu = premier.get(terme)
    declare = entree.get("premiere_occurrence")

    if declare is None or rang(declare) is None:
        return "champ_absent", declare, attendu
    if rang(declare)[0] == 0:
        return "livre_0", declare, attendu
    if declare not in chapitres:
        return "chapitre_absent", declare, attendu
    if terme not in chapitres[declare][2]:
        return "non_declare", declare, attendu
    if declare != attendu:
        return "pas_le_premier", declare, attendu
    return CONFORME, declare, attendu


def main():
    p = argparse.ArgumentParser(
        description="Contrôle de `premiere_occurrence` (convention, § 9). "
                    "Ne bloque rien, ne modifie rien ; code non nul si écart.")
    p.add_argument("--corpus", default=CORPUS,
                   help="dossier du corpus (défaut : corpus/ du dépôt) ; "
                        "sert à éprouver le script sur une copie")
    p.add_argument("--tout", action="store_true",
                   help="lister aussi les termes conformes")
    args = p.parse_args()

    corpus = os.path.abspath(args.corpus)
    if not os.path.isdir(corpus):
        print("ARRÊT : dossier introuvable : %s" % corpus)
        return 2
    try:
        entrees = charger_vocabulaire(corpus)
    except (IOError, OSError, ValueError, yaml.YAMLError) as e:
        print("ARRÊT : vocabulaire illisible : %s" % e)
        return 2

    chapitres, obstacles = charger_chapitres(corpus)
    if not chapitres:
        print("ARRÊT : aucun chapitre sous %s/livre-*/" % corpus)
        return 2
    if obstacles:
        print("ARRÊT : le corpus ne se lit pas entièrement ; un verdict rendu")
        print("        sur une lecture partielle dirait « premier » à tort.")
        for o in obstacles:
            print("  %s" % o)
        return 2

    premier = premiers_declarants(chapitres)

    hors_l0 = sum(1 for c in chapitres.values() if c[0][0] != 0)
    print("corpus    : %s" % corpus)
    print("chapitres : %d lus, dont %d hors livre 0 (seuls comptés, § 9)"
          % (len(chapitres), hors_l0))
    print("vocabulaire : %d termes" % len(entrees))
    print("")

    resultats = [(e["terme"],) + juger(e, chapitres, premier) for e in entrees]
    comptes = {v: 0 for v in VERDICTS}
    for _terme, verdict, _d, _a in resultats:
        comptes[verdict] += 1

    print("COMPTE PAR CATÉGORIE")
    for v in VERDICTS:
        marque = " " if v == CONFORME else "!"
        print("  %s %-16s %3d" % (marque, v, comptes[v]))
    ecarts = sum(comptes[v] for v in VERDICTS if v != CONFORME)
    print("  %s %-16s %3d" % ("!", "TOTAL DES ÉCARTS", ecarts))
    print("")

    if ecarts:
        print("ÉCARTS, UN PAR UN")
        print("  %-42s %-16s %-10s %s"
              % ("terme", "verdict", "déclaré", "attendu (§ 9)"))
        for terme, verdict, d, a in resultats:
            if verdict == CONFORME:
                continue
            print("  %-42s %-16s %-10s %s"
                  % (terme, verdict, d if d is not None else "(aucun)",
                     a if a else "aucun chapitre hors livre 0 ne le déclare"))
        print("")

    if args.tout:
        print("TERMES CONFORMES")
        for terme, verdict, d, _a in resultats:
            if verdict == CONFORME:
                print("  %-42s %s" % (terme, d))
        print("")

    if ecarts:
        print("VERDICT : %d écart(s). `controle.py` reste l'autorité : ce "
              "script ne bloque rien," % ecarts)
        print("          mais il ne rendra 0 que lorsque le champ sera juste "
              "pour tous les termes.")
        return 1
    print("VERDICT : aucun écart ; les %d termes satisfont les trois "
          "conditions du § 9." % len(entrees))
    return 0


if __name__ == "__main__":
    sys.exit(main())
