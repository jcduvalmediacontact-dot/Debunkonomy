# -*- coding: utf-8 -*-
"""Contrôle final du renommage « sans dette » → nom canonique.

**Version par ancrage, du 2026-09-20**, seconde demande de la passe adverse.

La version précédente comptait par **chapitre et zone**. Elle avait un trou, que
la passe a nommé : *si une ancienne occurrence disparaît et qu'une autre apparaît
ailleurs dans le même corps, avec le même total, le contrôle passe.* Une
substitution à total constant n'était pas détectée.

Chaque occurrence déclarée porte donc un **ancrage stable** : l'empreinte d'un
contexte normalisé — casse, espaces, apostrophes et guillemets écrasés — pris
autour du terme. Le contrôle compare les **multi-ensembles d'ancrages**, pas les
nombres. Une occurrence déplacée, une phrase réécrite autour d'elle, une phrase
neuve : les trois changent l'ancrage et font échouer le contrôle.

**Contrepartie assumée** : toute retouche éditoriale au voisinage d'une occurrence
déclarée casse son ancrage. C'est voulu — la remise à jour est alors un acte
délibéré, et non un silence.

RÈGLE DE GOUVERNANCE, ARRÊTÉE PAR L'AUTEUR LE 2026-09-20 ET RENDUE CONTRAIGNANTE
ICI. La première version de `--generer-ancrages` attribuait AUTOMATIQUEMENT le
motif du chapitre à toute occurrence nouvelle dans ce chapitre : une phrase neuve
en voix propre héritait de la justification d'une citation. L'approbation était
par chapitre ; elle est désormais **par ancrage**. Une occurrence nouvelle n'entre
au registre que nommée par son empreinte et accompagnée de son propre motif :

    --generer-ancrages --admettre <ancrage>[,<ancrage>] --motif "..."

Le motif peut être partagé par plusieurs ancrages — le défaut fermé le 2026-09-20
était le SILENCE, pas le partage : un motif frappé à la main après lecture des
extraits est une affirmation attribuable, là où le motif de chapitre s'appliquait
tout seul. Mais **quatre ancrages au plus par admission** (`PLAFOND`) : au-delà,
l'affirmation cesse d'être lisible d'un coup d'œil et redevient un tampon. Le lot
se scinde alors, et chaque part se motive séparément.

**L'admission est PARTIELLE depuis le 2026-09-25**, décision de l'auteur. Ce que
le paragraphe ci-dessus décrit — scinder le lot, motiver chaque part — était
impossible jusque-là : une seule occurrence neuve non admise faisait échouer le
lot **avant toute écriture**, de sorte que la seconde passe retrouvait les mêmes
neuves. Au-delà de quatre, l'outil ne pouvait plus aboutir du tout. Constaté le
2026-09-25 sur L1.C01 et L1.C10, avec six occurrences neuves.

Désormais une passe écrit **les ancrages admis, et eux seuls**. Les autres restent
non déclarés : le contrôle ordinaire continue de les signaler et le code de sortie
reste 1 — le registre a avancé, il n'est pas à jour. Le plafond est intact, et
aucune occurrence ne reçoit un motif qu'on ne lui a pas donné.

Les motifs déjà approuvés sont **conservés tels quels** : `MOTIFS` ci-dessous n'est
plus appliqué, il ne sert qu'à rappeler au relecteur ce que le chapitre justifiait
déjà. Une disparition ne demande aucune admission — elle réduit les exceptions.

    python outils_claude/controle_renommage.py [--liste]
    python outils_claude/controle_renommage.py --generer-ancrages   # après revue
"""
import hashlib
import io
import json
import os
import re
import sys
import glob
import unicodedata
from collections import Counter

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANCRAGES = os.path.join(RACINE, "outils_claude", "ancrages-renommage.json")
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
LISTE = "--liste" in sys.argv
GENERER = "--generer-ancrages" in sys.argv
MARQUEUR = "RENOMMAGE CANONIQUE DU 2026-09-20"
LARGEUR = 70      # signes de contexte de part et d'autre du terme
PLAFOND = 4       # ancrages par admission — au-delà, le lot se scinde (2026-09-20)


def options(nom):
    v = []
    for i, a in enumerate(sys.argv):
        if a == nom and i + 1 < len(sys.argv):
            v.append(sys.argv[i + 1])
        elif a.startswith(nom + "="):
            v.append(a[len(nom) + 1:])
    return v


ADMIS = {x.strip().lower() for s in options("--admettre") for x in s.split(",") if x.strip()}
MOTIF = (options("--motif") or [None])[-1]

# Motifs par chapitre. NE SONT PLUS APPLIQUÉS : rappel au relecteur, rien de plus.
# L'autorité est le motif inscrit sur CHAQUE ancrage, dans le fichier des ancrages.
MOTIFS = {
    "L1.C01": "notes seules",
    "L1.C08": "canonique et citable — lot public distinct",
    "L1.C10": "mots de Grandjean et Dufrêne, cités dans [S9] et décrits",
    "L1.C11": "canonique et citable — lot public distinct",
    "L1.C18": "notes seules",
    "L1.C19": "notes seules",
    "L1.C20": "notes seules — le chapitre porteur analyse l'ancien nom",
    "L1.C21": "notes seules",
    "L1.C29": "verrouillé jusqu'à la seconde passe de supervision",
    "L7.C11": "trace d'un arbitrage daté, attribuée",
    "L8.C02": "entrée `a_requalifier` — dette inscrite, E-L6 (P4)",
    "L8.C06": "entrée `a_requalifier` — dette inscrite, E-L6 (P18)",
    "L8.C38": "entrée `a_requalifier` — dette inscrite, E-L6 (P18)",
    "L10.C07": "trace d'une affirmation retirée",
    "L11.C01": "analyse de l'ancien nom — le chapitre établit ce qu'il coûte",
    "L11.C02": "l'alternative mise en balance",
    "L17.C01": "citation au mot de la promesse P9 — à migrer avec elle",
    "L17.C03": "citation au mot de la promesse P9 — à migrer avec elle",
    "L19.C01": "analyse historique : pourquoi le terme échoue",
    "L19.C03": "analyse historique : pourquoi le terme échoue",
    "L19.C07": "analyse historique : pourquoi le terme échoue",
    "L20.C25": "titre de section : analyse du terme — le renommer le détruirait",
    "L25.C03": "entrée `a_requalifier` — dette inscrite, E-L6",
}
IGNORES = re.compile("[\\s'’‘“”\"«»*_`—–-]+")


def empreinte(txt, i):
    """Empreinte d'un contexte normalisé : casse, espaces et ponctuation écrasés."""
    ctx = txt[max(0, i - LARGEUR):i + LARGEUR]
    n = IGNORES.sub("", unicodedata.normalize("NFKC", ctx)).lower()
    return hashlib.sha256(n.encode("utf-8")).hexdigest()[:16]


def releve():
    """Toutes les occurrences vivantes, avec leur ancrage. Aucun jugement."""
    trouve = []
    for F in sorted(glob.glob(os.path.join(RACINE, "corpus", "livre-*", "c*.md"))):
        t = io.open(F, encoding="utf-8").read()
        if "ERRATUM TERMINOLOGIQUE DU" in t or "NOTE TERMINOLOGIQUE DU" in t:
            continue
        m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
        if not m:
            continue
        ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
        tete, corps = t[:m.end()], t[m.end():]
        zones = [(x.start(), x.end()) for x in re.finditer(r'(?ms)^  - "(.*?)"$', tete)
                 if MARQUEUR in x.group(1)]
        for s in re.finditer("sans dette", tete, re.I):
            z = "notes" if any(a <= s.start() < b for a, b in zones) else "tete"
            trouve.append({"chapitre": ch, "zone": z, "ancrage": empreinte(tete, s.start()),
                           "extrait": re.sub(r"\s+", " ",
                                             tete[max(0, s.start() - 55):s.start() + 40])})
        for s in re.finditer("sans dette", corps, re.I):
            trouve.append({"chapitre": ch, "zone": "corps",
                           "ancrage": empreinte(corps, s.start()),
                           "extrait": re.sub(r"\s+", " ",
                                             corps[max(0, s.start() - 55):s.start() + 40])})
    return trouve


def charger():
    if not os.path.exists(ANCRAGES):
        return []
    return json.loads(io.open(ANCRAGES, encoding="utf-8").read())


def ligne(o):
    return "  %-18s %-9s %-6s …%s…\n" % (o["ancrage"], o["chapitre"], o["zone"],
                                                 o["extrait"][:64])


cle = lambda o: (o["chapitre"], o["zone"], o["ancrage"])
vivantes = releve()
declarees = charger()
# MULTI-ensemble, et non ensemble : deux occurrences au contexte identique dans la
# même zone comptent pour deux. Sinon la disparition de l'une passerait inaperçue,
# ce qui est le défaut même que cette version corrige.
d_cnt, v_cnt = Counter(map(cle, declarees)), Counter(map(cle, vivantes))
disparues = [o for o in declarees if (d_cnt - v_cnt)[cle(o)]]
neuves = [o for o in vivantes if (v_cnt - d_cnt)[cle(o)]]

# ── Génération : l'admission est PAR ANCRAGE, jamais par chapitre ────────────
if GENERER:
    fantomes = sorted(ADMIS - {o["ancrage"] for o in neuves})
    if fantomes:
        sys.exit("REFUS : ancrage(s) admis mais absent(s) du relevé — %s.\n"
                 "        On n'admet que ce que le relevé vient de trouver ; un ancrage\n"
                 "        recopié d'une session antérieure ne désigne plus rien."
                 % ", ".join(fantomes))
    if len(ADMIS) > PLAFOND:
        couvre = sum(1 for o in neuves if o["ancrage"] in ADMIS)
        sys.exit("REFUS : %d ancrages admis en une fois, le plafond est de %d.\n"
                 "        Le motif partagé tient parce qu'il est UN ACTE, lu d'un coup d'œil\n"
                 "        et attribuable. Au-delà de %d il redevient un tampon : scinder le\n"
                 "        lot, et motiver chaque part séparément.%s"
                 % (len(ADMIS), PLAFOND, PLAFOND,
                    "\n        (ces ancrages couvrent %d occurrences.)" % couvre
                    if couvre != len(ADMIS) else ""))
    refuses = [o for o in neuves if o["ancrage"] not in ADMIS]
    if refuses:
        out.write("REFUS : %d occurrence(s) nouvelle(s), non admise(s).\n\n" % len(refuses))
        out.write("L'APPROBATION EST PAR ANCRAGE, ET NON PAR CHAPITRE. Une occurrence neuve\n")
        out.write("dans un chapitre déjà déclaré n'hérite plus de son motif : elle doit\n")
        out.write("être nommée, et porter le sien.\n\n")
        for o in refuses:
            out.write(ligne(o))
            rappel = MOTIFS.get(o["chapitre"])
            if rappel:
                out.write("  %18s   le chapitre justifiait déjà : %s\n" % ("", rappel))
        tous = sorted({o["ancrage"] for o in refuses})
        out.write("\nRelire ces passages, puis — si et seulement si l'exception tient :\n")
        out.write("  --generer-ancrages --admettre %s --motif \"...\"\n"
                  % ",".join(tous[:PLAFOND]))
        if len(tous) > PLAFOND:
            out.write("  … puis les %d suivant(s), SÉPARÉMENT : le plafond est de %d\n"
                      "  ancrages par admission, pour qu'un motif partagé reste un acte.\n"
                      % (len(tous) - PLAFOND, PLAFOND))
        # ADMISSION PARTIELLE — décision de l'auteur du 2026-09-25.
        #
        # Jusqu'ici la sortie etait ici, quoi qu'il arrive. Le message
        # ci-dessus promettait pourtant << puis les N suivant(s), SEPAREMENT >>,
        # une sequence que ce sys.exit rendait impossible : la premiere passe
        # n'ecrivait rien, donc la seconde retrouvait les memes N neuves. Avec
        # six neuves et un plafond de quatre, l'outil ne pouvait plus aboutir du
        # tout -- constate le 2026-09-25 sur L1.C01 et L1.C10.
        #
        # Ce qui est ecrit maintenant : les ancrages ADMIS, et eux seuls. Les
        # autres restent NON DECLARES, donc le controle ordinaire continue de
        # les signaler, et le code de sortie reste 1. Le plafond est intact, et
        # aucun ancrage ne recoit un motif qu'on ne lui a pas donne.
        if not ADMIS:
            out.flush()
            sys.exit(1)
    if neuves and not (MOTIF or "").strip():
        sys.exit("REFUS : --admettre exige --motif.\n"
                 "        Un ancrage ne s'écrit pas sans sa raison, et la raison du\n"
                 "        chapitre n'est pas celle de l'occurrence.")
    reste = {}
    for o in declarees:
        reste.setdefault(cle(o), []).append(o)
    sortie = []
    for o in vivantes:
        garde = reste.get(cle(o))
        if garde:
            o["motif"] = garde.pop(0).get("motif", "")
        elif o["ancrage"] in ADMIS:
            o["motif"] = MOTIF
        else:
            # Neuve et NON ADMISE : elle n'entre pas au registre. Lui donner
            # MOTIF ici ferait exactement ce que le plafond interdit — un motif
            # tamponne sur une occurrence que personne n'a nommee.
            continue
        sortie.append(o)
    muets = [o for o in sortie if not (o.get("motif") or "").strip()]
    if muets:
        out.write("REFUS : %d ancrage(s) sans motif — registre non écrit.\n" % len(muets))
        for o in muets:
            out.write(ligne(o))
        out.flush()
        sys.exit(1)
    io.open(ANCRAGES, "w", encoding="utf-8", newline="\n").write(
        json.dumps(sorted(sortie, key=lambda o: (o["chapitre"], o["zone"], o["ancrage"])),
                   ensure_ascii=False, indent=2) + "\n")
    out.write("%d ancrage(s) dans %s — %d admis, %d disparu(s).\n"
              # `neuves` compte des OCCURRENCES, `ADMIS` des ancrages, et deux
              # occurrences peuvent partager un ancrage : on compte ce qui est
              # réellement entré, soit les neuves moins les refusées.
              % (len(sortie), os.path.relpath(ANCRAGES, RACINE),
                 len(neuves) - len(refuses), len(disparues)))
    if refuses:
        out.write("ADMISSION PARTIELLE : %d occurrence(s) restent NEUVES et non\n"
                  "déclarées. Le contrôle continue de les signaler, et ce code de\n"
                  "sortie est 1 : le registre a avancé, il n'est pas à jour.\n"
                  % len(refuses))
    sys.exit(1 if refuses else 0)

if not os.path.exists(ANCRAGES):
    sys.exit("fichier d'ancrages absent : lancer --generer-ancrages après revue.")

out.write("CONTRÔLE FINAL DU RENOMMAGE — par ancrage\n")
out.write("=" * 78 + "\n")
out.write("Chaque occurrence déclarée porte l'empreinte de son contexte normalisé,\n")
out.write("et son propre motif. Une substitution à total constant est donc détectée.\n\n")
out.write("%d occurrence(s) déclarée(s), %d vivante(s), dans %d chapitre(s).\n"
          % (len(declarees), len(vivantes), len({o["chapitre"] for o in vivantes})))

if LISTE:
    out.write("\n%-9s %-6s %-18s %s\n" % ("chapitre", "zone", "ancrage", "extrait"))
    for o in sorted(vivantes, key=cle):
        out.write("%s%-8s %-6s %-18s …%s…\n"
                  % (" " if d_cnt[cle(o)] else "+", o["chapitre"], o["zone"],
                     o["ancrage"], o["extrait"][:78]))

muets = [o for o in declarees if not (o.get("motif") or "").strip()]
if muets:
    out.write("\nSANS MOTIF — déclaré(s) sans raison inscrite (%d) :\n" % len(muets))
    for o in muets:
        out.write(ligne(o))
if disparues:
    out.write("\nDISPARUES — déclarées et introuvables (%d) :\n" % len(disparues))
    for o in disparues:
        out.write(ligne(o))
if neuves:
    out.write("\nNEUVES — vivantes et non déclarées (%d) :\n" % len(neuves))
    for o in neuves:
        out.write(ligne(o))

if disparues or neuves or muets:
    out.write("\nÉCHEC. Le jeu d'ancrages a bougé. **Un total inchangé ne suffit plus** :\n")
    out.write("une occurrence déplacée ou une phrase réécrite autour d'elle change son\n")
    out.write("empreinte. Relire, arbitrer, puis admettre chaque ancrage nouveau AVEC SON\n")
    out.write("PROPRE MOTIF — l'approbation est par ancrage, pas par chapitre.\n")
    sys.exit(1)
out.write("\nCONTRÔLE PASSÉ : chaque occurrence vivante est déclarée à sa place exacte,\n")
out.write("et chacune porte son propre motif.\n")
