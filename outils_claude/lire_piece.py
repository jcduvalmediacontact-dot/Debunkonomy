# -*- coding: utf-8 -*-
# Outil de lecture d'un exemplaire PDF : identite, empreinte, couche de texte, et recherche
# des formules citees par le corpus. Controle POSITIF et NEGATIF obligatoires avant tout
# verdict d'absence. Ecrit en fichier, jamais en `python -c` : les accents graves y sont
# substitues par bash et laissent des trous silencieux.
#
#   python lire_piece.py <chemin> [formule] [formule] ...
import io, os, re, sys, hashlib, unicodedata
from pypdf import PdfReader

out = io.open(sys.stdout.fileno(), "w", encoding="utf-8", closefd=False)
IGNORES = "[\\s\\u00ad'’‘“”\"«»‐-―*_`—–-]+"


def norm(s):
    return re.sub(IGNORES, "", unicodedata.normalize("NFKC", s)).lower()


F = sys.argv[1]
requetes = sys.argv[2:]
d = open(F, "rb").read()
out.write("%s\n" % os.path.basename(F))
out.write("  %d octets  SHA-256 %s\n" % (len(d), hashlib.sha256(d).hexdigest().upper()))
r = PdfReader(F)
pages = [(p.extract_text() or "") for p in r.pages]
tot = sum(len(p) for p in pages)
out.write("  %d pages, %d caracteres extractibles\n" % (len(pages), tot))
if tot == 0:
    out.write("  SCAN SANS COUCHE DE TEXTE : ne vaut pas ouverture (convention).\n")
    out.flush()
    sys.exit(0)

tout = "\n".join(pages)
nt = norm(tout)
longues = [l for l in tout.split("\n") if len(l.strip()) > 80]
assert longues, "aucune ligne longue : controle positif impossible"
temoin = longues[0][:70]
assert norm(temoin) in nt, "CONTROLE POSITIF EN ECHEC"
assert norm("phrase temoin absente du corpus xyzzy plugh") not in nt, "CONTROLE NEGATIF EN ECHEC"
out.write("  controles positif et negatif passes (temoin %r)\n" % temoin[:56])
out.write("  --- page 1 ---\n")
for l in [x.strip() for x in pages[0].split("\n") if x.strip()][:8]:
    out.write("    %s\n" % l[:130])

for q in requetes:
    n = nt.count(norm(q))
    ou = ""
    if n:
        for i, p in enumerate(pages):
            if norm(q) in norm(p):
                ou = " (1re page PDF %d)" % (i + 1)
                break
    out.write("  [%s] %-70s %d%s\n" % ("TROUVE" if n else "ABSENT", q[:70], n, ou))
out.flush()
