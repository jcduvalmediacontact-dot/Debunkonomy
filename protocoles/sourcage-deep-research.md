# Sourçage des vérifications en attente — texte à coller

À utiliser avec **Gemini Deep Research** (ou tout outil de recherche
documentaire). Coller ce texte, puis le fichier `.md` complet du chapitre à la
suite : la liste `verifications_en_attente` et les `sources_primaires` déjà
posées sont dans son en-tête.

Ce que l'outil rapporte est une **piste**, jamais une source vérifiée. Aucune
`date_verification` ne s'écrit dans le corpus avant qu'un humain ait ouvert la
source réelle et constaté qu'elle dit ce qu'on lui prête.

---

## Tâche

Le fichier qui suit est un chapitre d'un corpus documentaire. Son en-tête YAML
contient une liste `verifications_en_attente` : des points que l'auteur sait
devoir sourcer, corriger ou trancher. Ta tâche est de traiter **chaque
élément de cette liste, un par un, dans l'ordre**, en cherchant la source
primaire qui permet de le clore.

Traite aussi les entrées de `sources_primaires` dont la référence est
incomplète (mention « à préciser », « édition à préciser », absence d'éditeur
ou d'année).

## Ce qu'est une source primaire ici

Par ordre de préférence :

1. le texte original (loi, traité, arrêt, article scientifique, ouvrage
   d'auteur, rapport institutionnel) ;
2. la série de données de l'institution productrice (Eurostat, FMI, BRI, IIF,
   Banque mondiale, PNUE, GIEC…), avec l'identifiant de la série ;
3. seulement à défaut : une source secondaire de qualité, signalée comme telle.

Un article de presse, un billet de blog, une encyclopédie en ligne ou un
manuel qui cite la source ne sont pas la source. Ils peuvent servir à la
trouver ; ils ne la remplacent pas.

Chaque source relève d'une nature, à indiquer : `normatif` (texte de droit),
`jurisprudence` (décision), `donnees` (série statistique), `actualite` (fait
rapporté daté), `theorie` (travaux académiques, ouvrage).

## Format de sortie

Un tableau ou une fiche par élément de la liste, dans l'ordre de la liste,
avec ces champs :

- **N°** et rappel court de l'élément.
- **Source primaire proposée** : auteur, titre, éditeur ou institution, année,
  édition ; pour une série de données, l'identifiant exact ; pour un ouvrage,
  la page ou le chapitre si tu l'as.
- **Nature** : `normatif` / `jurisprudence` / `donnees` / `actualite` /
  `theorie`.
- **URL** si la source est en ligne, vers la source elle-même (pas vers un
  article qui en parle).
- **Extrait ou valeur** : la phrase exacte, ou le chiffre avec son unité, son
  année et son périmètre. Entre guillemets si c'est une citation.
- **Confiance** : haute / moyenne / basse, avec un mot sur ce qui la fonde.
- **Remarques** : divergences entre sources, éditions qui donnent des valeurs
  différentes pour la même année, chiffre introuvable sous la forme citée,
  attribution douteuse, controverse connue.

## Règles

- **N'invente jamais une référence.** Si tu ne trouves pas, écris « non
  trouvé » et dis ce que tu as cherché. Un « non trouvé » honnête vaut plus
  qu'une référence plausible.
- Ne reformule pas les chiffres : recopie-les avec leur unité, leur année et
  leur périmètre tels que la source les donne.
- Quand deux éditions d'une même publication donnent des valeurs différentes
  pour la même année, signale-le et indique les deux.
- Quand un élément de la liste demande une décision éditoriale plutôt qu'une
  source (« aligner deux chapitres », « reformuler »), dis-le et passe au
  suivant : ce n'est pas ta tâche.
- Réponds en français. Les titres d'ouvrages restent dans leur langue.

---

*Coller ici le fichier `.md` complet du chapitre.*
