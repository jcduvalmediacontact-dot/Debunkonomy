# Consignes de travail — Debunk'Onomy

## Routine de publication

Pour toute modification destinée au site :

1. Travailler directement dans le dépôt local Debunk'Onomy.
2. Vérifier les modifications et prévisualiser le résultat localement avant toute publication.
3. Ne jamais publier, créer de commit de publication ni pousser vers GitHub sans validation explicite préalable de l'utilisateur.
4. Après validation explicite de l'utilisateur :
   - créer un commit au message clair et descriptif ;
   - pousser ce commit vers GitHub ;
   - créer une archive ZIP datée dont le contenu correspond exactement au commit publié, sans modifications locales supplémentaires ni fichiers propres à Git ;
   - déposer cette archive dans le dossier Google Drive `SITE Debunk’Onomy` lorsque l'accès à Google Drive est disponible.
5. Si l'accès à Google Drive n'est pas disponible, conserver l'archive localement et signaler clairement que son dépôt dans `SITE Debunk’Onomy` reste à effectuer.

## Contrôles avant tout commit

À exécuter sur **l'ensemble du dépôt**, et non sur les seuls fichiers modifiés.
Un contrôle conduit sur le périmètre du commit n'est pas ce contrôle, et ne doit
pas être rapporté comme tel.

1. **`python corpus/controle.py` ne signale aucun blocage.**
2. **Aucune source bibliographique n'est traitée comme une voix unique avec une
   autre.** Ne jamais attribuer à un auteur ce qu'un autre a écrit ; ne jamais
   faire reposer l'affirmation portée par un nom sur la citation d'un autre nom
   comme si elle la corroborait ; ne jamais construire un argument d'antériorité
   ou de convergence qui traverse deux signatures sans le dire. Chaque auteur
   est cité pour ce qu'il a signé, et pour cela seul.
3. **Aucun fait rapporté à l'oral par l'auteur, hors du texte des sources, n'est
   inscrit dans le dépôt** — l'historique Git est permanent et le dépôt est
   destiné au public.

