# -*- coding: utf-8 -*-
"""Contrôle final du renommage « sans dette » → nom canonique.

**Version renforcée du 2026-09-20**, sur demande de la passe adverse : le simple
marqueur textuel ne suffisait pas comme exception, car **une phrase neuve pouvait
se cacher derrière lui**. L'exception est désormais une **table structurée par
occurrence** — chapitre, emplacement, nombre, motif — et le contrôle compare le
relevé à la table, zone par zone. Toute dérive, même à l'intérieur d'une note de
renommage, fait échouer le contrôle.

**Trois emplacements comptés séparément :**
  - `tete`  — en-tête hors notes de renommage : métadonnées, resume, entrées de
              source, vérifications autres ;
  - `corps` — le texte du chapitre, **sans masque de citation** : les guillemets
              autour d'un TERME sont un label, pas une citation de source, et
              les masquer laissait passer « la qualification de "sans dette" » ;
  - `notes` — à l'intérieur des entrées de vérification portant le marqueur.

**Exclus du relevé** : les fichiers portant un erratum ou une note terminologique
datée — archives et pages publiées, qui ne sont jamais réécrites.

    python outils_claude/controle_renommage.py [--liste]
"""
import io
import os
import re
import sys
import glob

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
LISTE = "--liste" in sys.argv
MARQUEUR = "RENOMMAGE CANONIQUE DU 2026-09-20"

# ── LA TABLE. Chaque ligne : chapitre -> (tete, corps, notes, statut, motif) ──
# statut : "justifie" = arbitré, le contrôle l'accepte ;
#          "a_traiter" = reliquat connu, le contrôle ÉCHOUE tant qu'il est là.
J, A = "justifie", "a_traiter"
TABLE = {
    "L1.C01":  (0, 0, 2, J, "notes seules"),
    "L1.C08":  (0, 2, 0, J, "canonique et citable — lot public distinct"),
    "L1.C10":  (3, 1, 1, J, "mots de Grandjean et Dufrêne, cités dans [S9] et décrits"),
    "L1.C11":  (0, 1, 0, J, "canonique et citable — lot public distinct"),
    "L1.C18":  (0, 0, 2, J, "notes seules"),
    "L1.C19":  (0, 0, 2, J, "notes seules"),
    "L1.C20":  (0, 0, 5, J, "notes seules — le chapitre porteur analyse l'ancien nom"),
    "L1.C21":  (0, 0, 2, J, "notes seules"),
    "L1.C29":  (1, 2, 0, J, "verrouillé jusqu'à la seconde passe de supervision"),
    "L7.C11":  (1, 0, 1, J, "trace d'un arbitrage daté, attribuée"),
    "L8.C02":  (1, 0, 0, J, "entrée `a_requalifier` — dette inscrite, E-L6 (P4)"),
    "L8.C06":  (1, 0, 0, J, "entrée `a_requalifier` — dette inscrite, E-L6 (P18)"),
    "L8.C38":  (1, 0, 0, J, "entrée `a_requalifier` — dette inscrite, E-L6 (P18)"),
    "L10.C07": (2, 2, 1, J, "trace d'une affirmation retirée"),
    "L11.C01": (2, 5, 1, J, "analyse de l'ancien nom — le chapitre établit ce qu'il coûte"),
    "L11.C02": (0, 1, 1, J, "l'alternative mise en balance"),
    "L19.C01": (2, 3, 1, J, "analyse historique : pourquoi le terme échoue"),
    "L19.C03": (2, 3, 1, J, "analyse historique : pourquoi le terme échoue"),
    "L19.C07": (1, 2, 1, J, "analyse historique : pourquoi le terme échoue"),
    "L25.C03": (1, 0, 1, J, "entrée `a_requalifier` — dette inscrite, E-L6"),
    "L17.C01": (1, 1, 2, J, "citation au mot de la promesse P9 — à migrer avec elle"),
    "L17.C03": (0, 1, 2, J, "citation au mot de la promesse P9 — à migrer avec elle"),
    "L20.C25": (0, 1, 1, J, "titre de section : analyse du terme — le renommer le détruirait"),
}


def releve(F):
    t = io.open(F, encoding="utf-8").read()
    if "ERRATUM TERMINOLOGIQUE DU" in t or "NOTE TERMINOLOGIQUE DU" in t:
        return None
    m = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    if not m:
        return None
    ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
    tete, corps = t[:m.end()], t[m.end():]
    zones = [(x.start(), x.end()) for x in re.finditer(r'(?ms)^  - "(.*?)"$', tete)
             if MARQUEUR in x.group(1)]
    nt = nn = 0
    ctx = []
    for s in re.finditer("sans dette", tete, re.I):
        if any(a <= s.start() < b for a, b in zones):
            nn += 1
        else:
            nt += 1
            ctx.append(("tete", re.sub(r"\s+", " ",
                                       tete[max(0, s.start() - 80):s.start() + 50])))
    nc = 0
    for s in re.finditer("sans dette", corps, re.I):
        nc += 1
        ctx.append(("corps", re.sub(r"\s+", " ",
                                    corps[max(0, s.start() - 80):s.start() + 50])))
    return ch, nt, nc, nn, ctx


releves = {}
for F in sorted(glob.glob(os.path.join(RACINE, "corpus", "livre-*", "c*.md"))):
    r = releve(F)
    if r and (r[1] or r[2] or r[3]):
        releves[r[0]] = r[1:]

out.write("CONTRÔLE FINAL DU RENOMMAGE — table structurée par occurrence\n")
out.write("=" * 78 + "\n")
out.write("Emplacements : tête (hors notes) · corps (sans masque de citation) · notes\n")
out.write("Exclus : fichiers portant un erratum ou une note terminologique datée.\n\n")
out.write("%-9s %5s %6s %6s  %-10s %s\n"
          % ("chapitre", "tête", "corps", "notes", "statut", "motif"))

echecs, derives, inconnus = [], [], []
for ch in sorted(releves):
    nt, nc, nn, ctx = releves[ch]
    if ch not in TABLE:
        out.write("%-9s %5d %6d %6d  %-10s **HORS TABLE**\n" % (ch, nt, nc, nn, "?"))
        inconnus.append(ch)
        continue
    et, ec, en, statut, motif = TABLE[ch]
    if (nt, nc, nn) != (et, ec, en):
        out.write("%-9s %5d %6d %6d  %-10s **DÉRIVE** (attendu %d/%d/%d) — %s\n"
                  % (ch, nt, nc, nn, statut, et, ec, en, motif))
        derives.append(ch)
    else:
        out.write("%-9s %5d %6d %6d  %-10s %s\n" % (ch, nt, nc, nn, statut, motif))
    if statut == A:
        echecs.append(ch)
    if LISTE and (statut == A or ch in derives):
        for zone, c in ctx:
            out.write("            [%s] …%s…\n" % (zone, c))

manquants = [c for c in TABLE if c not in releves]
if manquants:
    out.write("\nDans la table et absents du relevé : %s\n" % ", ".join(sorted(manquants)))

out.write("\n")
if inconnus:
    out.write("HORS TABLE : %s — toute occurrence doit être déclarée.\n"
              % ", ".join(inconnus))
if derives:
    out.write("DÉRIVE : %s — le compte a bougé sans que la table soit mise à jour. "
              "**Une phrase neuve ne peut pas se cacher derrière le marqueur.**\n"
              % ", ".join(derives))
if echecs:
    out.write("RELIQUATS NON TRAITÉS : %s\n" % ", ".join(echecs))

if inconnus or derives or echecs:
    out.write("\nÉCHEC. Le contrôle ne passera que lorsque la table ne portera plus de "
              "reliquat, aucune dérive et aucun chapitre hors table.\n")
    sys.exit(1)
out.write("\nCONTRÔLE PASSÉ : chaque occurrence est déclarée, comptée et justifiée.\n")
