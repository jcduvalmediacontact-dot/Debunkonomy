# Voie hors ligne — artefact PyYAML pour le contrôle du corpus

Ce répertoire conserve **une roue PyYAML**, obtenue par la voie normale
(`pip download` depuis l'index PyPI, le 2026-09-10, sur la machine de travail),
pour installer la dépendance unique du contrôle **sans accès réseau**. Elle est
redistribuée telle quelle, sans modification, avec sa licence.

| champ | valeur |
|---|---|
| fichier | `pyyaml-6.0.3-cp314-cp314-win_amd64.whl` |
| taille | 156 429 octets |
| SHA-256 | `4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac` |
| paquet, version | PyYAML 6.0.3 |
| étiquette | `cp314-cp314-win_amd64` — CPython 3.14, Windows x86-64, **la seule plateforme couverte** |
| licence | MIT — `LICENSE-PyYAML`, copie du fichier `licenses/LICENSE` contenu dans la roue |
| origine | https://pypi.org/project/PyYAML/6.0.3/ — source : https://github.com/yaml/pyyaml |

**Installation hors ligne** :

```
python -m pip install --no-index --find-links corpus/hors-ligne -r corpus/requirements.txt
```

**Vérification de l'empreinte avant installation.** Le fichier `SHA256SUMS`
porte l'empreinte de chaque roue conservée, au format « empreinte, deux
espaces, nom du fichier ». `test_environnement_propre.py` la recalcule et
**refuse d'installer** toute roue absente de ce fichier ou d'empreinte
différente. À la main, sous PowerShell :

```
Get-FileHash corpus\hors-ligne\pyyaml-6.0.3-cp314-cp314-win_amd64.whl -Algorithm SHA256
```

**Ce qui n'est pas revendiqué.** Aucune compatibilité avec une autre version de
Python ni un autre système : sur toute autre plateforme, `python
corpus/test_environnement_propre.py` rapporte « plateforme non couverte par
l'artefact hors ligne » (code 3), et la voie connectée reste la seule. Une roue
pour une autre plateforme s'ajoute ici avec son empreinte, sa taille et sa
licence, et une ligne dans cette table — jamais sans.

**Notice de redistribution.** PyYAML est distribué sous licence MIT,
Copyright (c) 2017-2021 Ingy döt Net, Copyright (c) 2006-2016 Kirill Simonov.
Le texte de la licence, qui exige d'être joint à toute copie, est
`LICENSE-PyYAML`. Le corpus Debunk'Onomy n'est pas l'auteur de ce logiciel et
n'y a rien changé.
