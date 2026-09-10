---
chapitre: L14.C01
titre: "Ce que ce livre doit établir"
livre: 14
langue: fr
licence: CC-BY-SA-4.0
type: chapitre
statut: brouillon
revision_de_fond: 2026-09-08
autorite: preparatoire
citable: false
regime: hybride
sources_primaires:
  - ref: S1
    nature: theorie
    reference: "**`corpus/livres.yaml`, matricule 14** — projection du plan directeur de l'auteur. **Titre** : Gouverner la preuve — méthodes, vérification et traçabilité. **Collection** : cahier-disciplinaire. **Fonction assignée** : rendre publique, reproductible et contestable **la méthode de vérification, de provenance et de révision DU CORPUS**. **Note du registre** : « Ce livre porte sur le corpus lui-même. La convention, les protocoles d'audit et de sourçage, le registre des promesses et ce registre en sont la matière première. » **Ce livre n'instruit donc pas le dispositif : il instruit la machine qui instruit le dispositif.**"
    etat_lecture: a_requalifier
  - ref: S2
    nature: theorie
    reference: "**Le corpus lui-même, mesuré le 2026-09-08** : `corpus/convention.md` en révision r11 (2026-09-07) ; `corpus/controle.py` ; `corpus/vocabulaire.yaml` ; `corpus/livres.yaml` ; et les cinq protocoles — `falsification.md`, `passe-2.md`, `registre-des-promesses.md`, `sources-a-ouvrir.md`, `inventaire-entropie.md`. **Les comptages rapportés dans ce chapitre sont établis par relevé direct sur ces fichiers à la date indiquée**, et sont reproductibles par toute personne disposant du dépôt."
    etat_lecture: a_requalifier
verifications_en_attente:
  - "**LES COMPTAGES DE CE CHAPITRE SONT DATÉS ET PÉRISSABLES.** Ils décrivent
     l'état du corpus au 2026-09-08. **Toute reprise de ce chapitre doit les
     refaire** ; aucun ne doit être cité sans sa date. **C'est la première
     exigence que ce livre s'applique à lui-même.**"
  - "**AUCUNE MÉTHODOLOGIE EXTERNE N'EST OUVERTE, ET C'EST LE DÉFAUT QUE CE LIVRE
     DEVRA CORRIGER EN PREMIER.** Le corpus s'examine ici avec ses propres
     catégories. **Il n'a ouvert ni norme d'audit, ni littérature sur la
     reproductibilité, ni travail sur la revue par les pairs, ni méthodologie de
     revue systématique.** **Un livre sur la gouvernance de la preuve qui ne
     tient aucune source sur la gouvernance de la preuve reproduit exactement le
     défaut qu'il devrait détecter.**"
  - "**LE CHAPITRE MESURE UN APPAREIL ; IL N'ÉVALUE PAS LA QUALITÉ DE CE QU'IL
     PRODUIT.** Compter les sources ouvertes, les régimes de droits et les
     vérifications en attente ne dit rien de la justesse des chapitres. **Aucun
     échantillon n'a été relu contre ses sources par un tiers**, et le corpus n'a
     donc aucune mesure de son propre taux d'erreur."
resume: "Ce chapitre remplace l'amorce et ouvre le livre qui porte sur le corpus lui-même plutôt que sur le dispositif. Il mesure d'abord l'appareil existant, à savoir une convention en onzième révision, un script de contrôle qui refuse la publication en cas de blocage, un vocabulaire contrôlé qui bloque tout concept non défini, et cinq protocoles tenant les falsifieurs, les arbitrages, les promesses, les sources et un inventaire terminologique. Il relève ensuite le résultat le plus dur que ce relevé produise, à savoir que sur deux cent quatre-vingt-quatorze chapitres, aucun n'a jamais franchi le goulot de vérification, aucun ne porte une autorité autre que préparatoire et aucun n'est citable, de sorte que le corpus n'a jamais complété son propre cycle une seule fois. Il établit ensuite ce que l'appareil détecte et ce à quoi il est aveugle, en s'appuyant sur la journée du huit septembre comme cas d'essai. La machine bloque l'absence, la non-conformité et l'inconnu, mais elle ne peut rien contre une conclusion tirée au-delà de ce qu'une source établit, et les quatre excès de conclusion produits ce jour-là ont tous été détectés par l'auteur et aucun par le script, deux d'entre eux figurant dans des chapitres que le contrôle avait acceptés. Il en tire que l'appareil est construit pour la détection du manque et non pour celle de l'excès. Il enregistre enfin les règles de méthode produites dans la journée, dont trois portent sur la comparaison des quantités, le décompte des sources par auteurs et l'inventaire préalable du fonds, et il fixe la grille du livre en huit questions."
concepts: [robustesse, indicateur_de_progres]
renvois: [L1.C15, L8.C34, L12.C01, L13.C01, L18.C10, L26.C07, L26.C09, L26.C10]
---

# Ce que ce livre doit établir

::etat:: **Ce livre ne porte pas sur le dispositif. Il porte sur la machine qui instruit le dispositif** [S1]. Sa matière première est la convention, les protocoles, les registres — **et l'appareil se juge ici sur ce qu'il a produit, non sur ce qu'il promet.**

## 1. L'appareil existe, et il est mesurable

::etat:: **Une convention en onzième révision** [S2], qui fixe le schéma des en-têtes, les statuts, les régimes de discours, les empreintes et la procédure de contrôle. **Un script qui refuse la publication en cas de blocage** — et qui bloque sur un champ manquant, un champ inconnu, un régime hors liste, une nature de source hors liste, un concept absent du vocabulaire, un en-tête invalide. **Un vocabulaire contrôlé de cinquante concepts**, dont l'absence d'une entrée suffit à interdire la publication d'un chapitre. **Cinq protocoles** tenant les falsifieurs, les arbitrages, les promesses, les sources et un inventaire terminologique.

::etat:: **Ce que l'appareil a produit au 2026-09-08** [S2]. **294 chapitres.** **117 mentions d'ouverture de source par téléchargement direct.** **Soixante-neuf régimes de droits déclarés** — vingt et un `libre`, dix-neuf `citation_seule`, vingt-neuf `a_verifier`. **Quatorze falsifieurs, quarante-deux arbitrages, cinquante-sept promesses.** **Et environ mille quatre cent cinquante entrées de vérification en attente.**

::hypothese:: **Ce sont les chiffres d'un appareil qui fonctionne.** Un corpus de cette taille qui déclare ses droits source par source, tient un registre de ses objections et refuse la publication sur défaut structurel **est un objet rare**, et le livre doit commencer par le dire.

## 2. Le résultat le plus dur du relevé, et il tient en trois nombres

::etat:: **Sur 294 chapitres : 285 en `brouillon`, 9 en `audit_contradictoire`, ZÉRO en `verifie`** [S2].

::etat:: **Sur 294 chapitres : 294 en `autorite: preparatoire`. Aucun autre.**

::etat:: **Sur 294 chapitres : 294 en `citable: false`. Aucun n'est citable.**

::hypothese:: **Le corpus n'a jamais franchi son propre goulot d'étranglement, pas une seule fois.** Le contrôle en mode publication refuse les 294 chapitres, **et il a raison de les refuser** : c'est le dispositif volontaire prévu par la convention, qui exige que les sources soient effectivement vérifiées et datées avant qu'un chapitre change de statut.

::hypothese:: **Mais un goulot que rien n'a jamais traversé n'est pas un goulot : c'est un mur.** **Le corpus ne sait donc pas si sa procédure de vérification FONCTIONNE** — il sait seulement qu'elle n'a jamais été exécutée jusqu'au bout. **C'est le premier objet de ce livre : faire passer un chapitre, un seul, à travers toute la procédure, et enregistrer ce qui casse.**

## 3. Ce que l'appareil détecte, et ce à quoi il est aveugle

::etat:: **Ce que la machine bloque est d'une seule espèce** [S2] : un champ manquant, un champ inconnu, une valeur hors d'une liste fermée, un concept non défini, un en-tête illisible. **Autrement dit : l'ABSENCE, la NON-CONFORMITÉ et l'INCONNU.**

::etat:: **La journée du 2026-09-08 fournit un cas d'essai, et il est concluant.** **Quatre excès de conclusion ont été produits ce jour-là**, tous de même forme — une inférence tirée au-delà de ce que la source établissait. **Une émission monétaire présentée comme augmentant mécaniquement le produit intérieur brut. Deux sources déclarées contradictoires alors qu'elles portaient sur des objets différents. Deux quantités de nature différente comparées comme si elles l'étaient. Une exigence d'indicateur qui aurait supprimé la notion qu'elle prétendait mesurer.**

::etat:: **LES QUATRE ONT ÉTÉ DÉTECTÉS PAR L'AUTEUR. AUCUN PAR LE SCRIPT.** **Et deux figuraient dans des chapitres que le contrôle structurel avait acceptés sans réserve.**

::hypothese:: **L'appareil est donc construit pour la détection du MANQUE et il est aveugle à l'EXCÈS.** **Il vérifie qu'une source est déclarée ; il ne peut pas vérifier que la conclusion tirée d'elle y tient.** **C'est une propriété de sa nature — un script lit une structure, pas un raisonnement — et non un défaut de rédaction.**

::hypothese:: **Ce que le livre doit en tirer n'est pas qu'il faut un meilleur script.** **C'est que la seule instance capable de détecter l'excès est une LECTURE CONTRADICTOIRE**, et que le corpus n'en a qu'une : l'auteur. **Un examen dont l'unique contrôleur est aussi le commanditaire n'est pas indépendant**, et le livre doit le dire avant de dire autre chose.

## 4. Les règles produites en une journée, et leur statut

::etat:: **Trois règles de méthode ont été versées le 2026-09-08**, chacune après une faute.

::etat:: **VÉRIFIER LA NATURE DES QUANTITÉS AVANT DE LES COMPARER.** Une borne inférieure n'est pas une moyenne ; un plafond n'est pas une valeur ; un périmètre n'est pas un autre. **Née d'une comparaison fautive entre une borne et deux moyennes portant sur d'autres périmètres.**

::etat:: **COMPTER LES SOURCES PAR AUTEURS ET NON PAR RÉFÉRENCES.** Deux travaux partageant un auteur ne valent pas deux confirmations pleinement indépendantes. **Née de la découverte qu'un auteur était commun à deux sources que le corpus comptait séparément.**

::etat:: **VÉRIFIER QU'UNE MÉTHODE N'EST PAS DÉJÀ DANS LE FONDS AVANT DE LA DÉCLARER MANQUANTE.** **Née d'un cas où le corpus a recommandé une famille de modèles dont un exemplaire dormait dans son propre dossier documentaire.**

::hypothese:: **Ces trois règles ont un trait commun qui définit le programme de ce livre : AUCUNE N'EST AUTOMATISABLE.** Elles supposent de savoir ce qu'une quantité mesure, qui a écrit quoi, et ce que le fonds contient. **Le livre doit donc traiter le cas général : quelles vérifications un script peut porter, et lesquelles exigent un lecteur.**

## 5. Ce que l'appareil fait bien, et qu'il faut compter aussi

::etat:: **La discipline des droits fonctionne et se mesure.** Soixante-neuf régimes déclarés, et la règle — **lire la mention DANS le document, jamais dans un registre** — a corrigé deux entrées d'un registre externe le 2026-09-08, **et maintenu en `a_verifier` deux documents dont le corpus n'a trouvé aucune licence.**

::etat:: **La règle de l'ouverture directe fonctionne aussi.** 117 mentions d'ouverture par téléchargement direct, chacune datée. **Et le corpus a déclaré ses échecs d'acquisition sans les maquiller** — serveurs répondant par une page HTML, connexions expirées, murs anti-robot jamais franchis.

::etat:: **Et l'appareil a détecté des fautes de fond que rien ne l'obligeait à chercher.** Que le corpus se réclamait d'une tradition dont il n'avait lu aucun texte. Que le fondateur de cette tradition ne propose aucun instrument monétaire. Que deux sources comptées comme indépendantes partageaient un auteur. **Ces trois-là ne viennent pas du script : elles viennent de la règle d'ouverture de première main, qui est une règle de méthode et non un contrôle automatique.**

## 6. La grille de ce livre

::etat:: **1. Faire passer UN chapitre à travers toute la procédure de vérification**, et enregistrer ce qui casse. **Sans cela, le corpus ne sait pas si sa procédure fonctionne.**

::etat:: **2. Établir ce qu'un contrôle automatique peut porter et ce qu'il ne peut pas.** Le partage entre l'absence et l'excès.

::etat:: **3. Traiter l'indépendance du contrôleur.** **L'auteur est aujourd'hui la seule instance capable de détecter un excès, et il est aussi le commanditaire.**

::etat:: **4. Définir ce qui rend un chapitre CITABLE**, puisque aucun ne l'est et que le corpus ne dit nulle part ce qu'il faudrait pour qu'un le devienne.

::etat:: **5. Traiter le statut des modèles tiers.** La règle en vigueur — un résumé de modèle est une piste, jamais une vérification — **a été éprouvée trois fois le 2026-09-08 et a tenu les trois fois**, mais elle n'est écrite nulle part dans la convention.

::etat:: **6. Traiter la péremption.** **Les comptages, les régimes de droits et les états d'application vieillissent** ; le corpus n'a aucune règle de revalidation.

::etat:: **7. Rendre la méthode REPRODUCTIBLE**, ce que la fonction assignée demande explicitement : un tiers disposant du dépôt doit pouvoir refaire chaque relevé.

::etat:: **8. Rendre la méthode CONTESTABLE.** **C'est le mot le plus exigeant de la fonction assignée**, et il suppose une voie par laquelle un tiers puisse attaquer un résultat du corpus. **Aucune n'existe.**

## 7. Ce que ce chapitre n'établit pas

::etat:: **Il mesure un appareil ; il n'évalue pas ce que l'appareil produit.** **Aucun échantillon de chapitres n'a été relu contre ses sources par un tiers**, et le corpus n'a donc aucune mesure de son taux d'erreur — seulement quatre fautes connues parce que l'auteur les a trouvées en un jour.

::etat:: **Il n'ouvre aucune source extérieure.** Ni norme d'audit, ni littérature sur la reproductibilité, ni méthodologie de revue systématique. **Un livre sur la gouvernance de la preuve qui ne tient aucune source sur la gouvernance de la preuve reproduit exactement le défaut qu'il devrait détecter**, et c'est la première acquisition de rang 1 de ce livre.

::hypothese:: **Le livre s'ouvre donc sur un constat que le corpus doit porter avant tout autre : il a produit deux cent quatre-vingt-quatorze chapitres, ouvert cent dix-sept sources de première main, posé quatorze falsifieurs et quarante-deux arbitrages — ET IL N'A VÉRIFIÉ AUCUN CHAPITRE, N'EN A RENDU AUCUN CITABLE, ET N'A JAMAIS EXÉCUTÉ SA PROPRE PROCÉDURE JUSQU'AU BOUT.** **L'examen a été mené avec rigueur ; il n'a pas encore été mené jusqu'à la preuve.**
