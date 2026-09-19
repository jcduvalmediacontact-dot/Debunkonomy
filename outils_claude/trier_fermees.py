# -*- coding: utf-8 -*-
# Releve les sources encore fermees du Livre 1, avec pour chacune : le chapitre, le nombre
# d'appels dans le corps, l'etat de lecture, et la premiere ligne de la reference.
# AUCUN VERDICT N'EST REND ICI sur l'acquerabilite : le script RELEVE, le tri est humain.
import io, re, sys, glob, os
out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
R = r"C:\Users\jcduv\Documents\GitHub\debunkonomy"
lignes = []
for F in sorted(glob.glob(os.path.join(R, "corpus", "livre-01-*", "c*.md"))):
    t = io.open(F, encoding="utf-8").read()
    ch = re.search(r"(?m)^chapitre: (\S+)", t).group(1)
    tete = re.search(r"(?ms)\A---\n.*?\n---\n", t)
    corps = t[tete.end():]
    for m in re.finditer(r"(?ms)^  - ref: (S\d+)$((?:\n(?!  - ref:|verifications_en_attente:)"
                         r"[^\n]*)*)", t):
        ref, b = m.group(1), m.group(2)
        et = re.search(r"etat_lecture: (\w+)", b)
        if not et or et.group(1) == "ouverte":
            continue
        r = re.search(r'reference: [">|]?\s*(.{0,190})', b, re.S)
        txt = re.sub(r"\s+", " ", r.group(1)) if r else "???"
        n = len(re.findall(re.escape("[%s]" % ref), corps))
        lignes.append((ch, ref, et.group(1), n, txt))
out.write("%-8s %-5s %-14s %5s  %s\n" % ("chap", "ref", "etat", "appels", "reference"))
for l in lignes:
    out.write("%-8s %-5s %-14s %5d  %s\n" % l)
out.write("\n%d entree(s) fermee(s) dans le Livre 1\n" % len(lignes))
out.flush()
