---
chapitre: L0.C01
titre: "Comment lire le Livre 0"
livre: 0
langue: fr
licence: CC-BY-SA-4.0
type: synthese
statut: brouillon
revision_de_fond: 2026-09-27
autorite: preparatoire
citable: false
regime: descriptif
sources_primaires: []
chapitres_sources: [L0.C02, L0.C03, L0.C04, L0.C05, L0.C06, L0.C07, L0.C08,
                    L0.C09, L0.C10, L0.C11]
verifiee_le: 2026-09-27
verifications_en_attente:
  - "BROUILLON DU 2026-09-27, qui REMPLACE l'amorce déposée le 7 septembre 2026.
     L'ancien texte reste dans `git`. Il enregistrait ce que le registre assigne
     au matricule 0 et déclarait lui-même qu'il serait remplacé, non complété."
  - "LA SOURCE S1 DE L'AMORCE EST SORTIE, ET LE MANIFESTE N'A PAS ÉTÉ TOUCHÉ.
     Elle portait `etat_lecture: a_requalifier` sur autorisation de
     `corpus/manifeste-etat-lecture.json`. Cette introduction ne s'appuie pas
     sur l'entrée du registre : la déclarer serait déclarer une source que le
     corps n'emploie pas. L'occurrence du manifeste devient donc une entrée sans
     occurrence — alerte A-L3, non blocage. Le manifeste ne s'édite jamais
     (CLAUDE.md) : l'écart est inscrit ici plutôt que contourné."
  - "AUCUN CONCEPT N'EST DÉCLARÉ, et ce n'est pas un oubli : ce chapitre décrit
     une manière de lire, il n'emploie aucun concept du vocabulaire. Un concept
     déclaré sans être employé serait un faux. Le champ devra être rempli si le
     corps change, `controle.py` l'exigeant pour atteindre `verifie`."
  - "LE NOM DU FICHIER DIT ENCORE « ce que ce livre doit établir », titre de
     l'amorce. L'ordre 4 impose le même fichier ; le renommer relève d'une
     décision de l'auteur. L'URL publique ne dérive que de l'identifiant
     (convention § 3, révision 14), donc l'écart ne touche que la lecture du
     dépôt."
resume: "Ce chapitre explique comment lire le Livre 0 et ce que le Livre 0 ne fait pas. Le Livre 0 est une couche de réponse : on y entre par la question plutôt que par le plan, et chaque entrée répond brièvement à une question avant de renvoyer au chapitre qui démontre. Chaque entrée se lit en trois temps — une réponse courte, une limite explicite qui dit où le chapitre source s'arrête, et un renvoi à la section qui porte la démonstration. Ce chapitre rappelle enfin ce que la couche ne fait pas : elle ne démontre rien, n'ouvre aucune source, n'ajoute aucun chiffre qui ne soit dans le chapitre qu'elle résume, et ne peut donc rien affirmer que ce chapitre n'établisse. Il remplace l'amorce déposée le 7 septembre 2026, qui enregistrait la fonction assignée au matricule 0 et déclarait elle-même qu'elle serait remplacée."
concepts: []
renvois: []
---

# Comment lire le Livre 0

::etat:: Le Livre 0 est une **couche de réponse**, non une table des matières.
On y entre par la question plutôt que par le plan : chaque entrée porte une
question en titre, y répond brièvement, et renvoie au chapitre qui démontre.

## 1. Une entrée se lit en trois temps

::etat:: **La réponse** dit ce que le corpus établit sur cette question, en
quelques lignes, dans les termes du chapitre qui l'établit.

::etat:: **La limite** dit où ce chapitre s'arrête. Elle n'est pas une
précaution de style : elle est reprise de la section où le chapitre borne
lui-même sa portée, et elle est aussi importante que la réponse.

::etat:: **Le renvoi** nomme la section qui porte la démonstration. C'est là
qu'il faut aller pour savoir sur quelles pièces elle repose.

## 2. Ce que cette couche ne fait pas

::etat:: **Elle ne démontre rien.** Les chapitres démontrent ; les entrées
rapportent ce qu'ils ont établi et renvoient à eux.

::etat:: **Elle n'ouvre aucune source**, ne déclare aucune pièce, et n'ajoute
aucun chiffre qui ne soit dans le chapitre qu'elle résume.

::etat:: **Elle ne peut donc rien affirmer que le chapitre source n'établisse.**
Là où celui-ci refuse de conclure, l'entrée refuse avec lui.

## 3. Ce chapitre remplace une amorce

::etat:: Une amorce déposée le 7 septembre 2026 occupait cette place pour que
le dossier du matricule 0 existe dans l'arborescence. Elle enregistrait la
fonction que le registre assigne à ce matricule et déclarait qu'elle serait
remplacée, non complétée. **Son texte reste dans `git`.**
