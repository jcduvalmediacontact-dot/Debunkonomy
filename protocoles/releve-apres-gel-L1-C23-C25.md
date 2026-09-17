# L1.C23 et L1.C25 — gelés pour audit tiers : les empreintes, et ce qui a été décidé depuis

**Relevé du 2026-09-17, non validé par l'auteur. L1.C23 et L1.C25 sont gelés pour audit : rien n'y est modifié.** Préparé par un sous-agent ; ses 108 citations étiquetées ont été retrouvées par la session principale, qui a recalculé elle-même les empreintes des quatre gels.

Ce relevé liste ce qu'il faudra propager **après** le traitement des rapports d'audit tiers, qui n'existent pas encore dans `protocoles/`.

**Convention de lecture.** Les citations étiquetées C de la section 2 renvoient à `corpus/livre-01-monnaie-finance-limites-planetaires/c25-histoire-des-systemes-monetaires-internationaux.md` ; celles de la section 3 à `corpus/livre-01-monnaie-finance-limites-planetaires/c23-l-economie-de-la-robustesse.md`. Les numéros de ligne sont ceux des fichiers au 2026-09-17 ; **le corps de L1.C25 n'ayant pas changé depuis le gel (section 0), ils valent aussi pour l'état gelé, décalage d'en-tête compris : aucune ligne n'a été ajoutée ni retirée.** Les sorts proposés (K, C, R, O, N) sont ceux de la consigne commune, et ils sont proposés pour après l'audit.

## 0. Les empreintes, vérifiées le 2026-09-17

| chapitre | empreinte gelée, donnée par le dossier (l. 7) | empreinte du fichier actuel (`sha256sum`) | verdict |
|---|---|---|---|
| L1.C23 | `5D35853925359ADF64E68A06339016814BE36DC4EC80F63B44787792DA581BB4` | `5D35853925359ADF64E68A06339016814BE36DC4EC80F63B44787792DA581BB4` | **identique : le gel tient** |
| L1.C25 | `E36C67ADC71B0ACD4BCF5796D4FE0BF979DA3B676E93B812BFE853D04363E4AE` | `14BBDF5573D76E9BA9411DB39F537E5F1EA27C52F3EC4514F4660D74B550DF85` | **différente : le fichier n'est plus l'état gelé** |

**Ce qui a changé dans L1.C25, et ce qui n'a pas changé.** Relevé par commandes, non estimé :

- **L'état gelé est la version du dépôt aux commits `e2338595` et `b26e9971`** (`git show … | sha256sum` rend `E36C67AD…`) ; le chapitre embarqué dans le dossier est identique octet pour octet à cette version.
- **Deux commits postérieurs au gel l'ont modifié** : `efad9e33` (2026-09-16, 19 h 27, « Les empreintes d'exemplaire sont complétées ») et `163cd955` (2026-09-16, 20 h 59, « Gourinchas, Rey et Govillot remplacent le texte de 2005 »).
- **Le diff ne touche que l'en-tête** : lignes 21 et 26 (S2 et S3, mention « EMPREINTE D'EXEMPLAIRE COMPLÉTÉE ») et lignes 54 à 57 (S9 rebasée par D63 : nouvelle référence, nouvelle URL, `etat_lecture` passé de `a_requalifier` à `ouverte`, `date_verification` ajoutée).
- **Le corps et le résumé sont intacts** : l'empreinte éditoriale enregistrée par le script dans `corpus/.etat-corpus.json` est la même à `b26e9971` et à `HEAD` (`b7c5b26318052a98`) ; seule l'empreinte des métadonnées a changé (`bca60c70eb92da6c` → `09440230f231bf22`).

**Conséquence pour l'audit.** Le texte soumis (corps et résumé) est toujours celui du dépôt ; l'en-tête soumis ne l'est plus. Le dossier annonce S9 fermée : A«Sources : **12**, dont 7 `ouverte` et datées ; **non ouvertes : S6 (`a_requalifier`), S7 (`a_requalifier`), S9 (`a_requalifier`), S11 (`a_requalifier`), S12 (`a_requalifier`)**» (`protocoles/dossier-audit-tiers-L1-C25.md`). Le fichier en compte aujourd'hui huit ouvertes, S9 comprise. **Une objection de l'auditeur sur l'appui de S9 viserait une entrée déjà rebasée.** Question G1.

**Un écart mineur dans les deux dossiers.** Ils écrivent : A«Base Git locale : `b26e9971087e43003e27e26138076a6add30fa14` — le fichier est modifié depuis cette base et non commité ; **c'est l'empreinte ci-dessus qui fait foi de l'état gelé**» (`protocoles/dossier-audit-tiers-L1-C23.md`). Or les deux versions gelées sont les versions commitées à cette base (même relevé pour L1.C25). L'empreinte fait foi, comme le dossier le dit ; la mention « modifié depuis cette base » est inexacte et sans effet.

## 1. Ce qui a été décidé après le gel

**Le gel.** Relais du 2026-09-16, 14 h 01 : A«Décision de l'auteur : passe adverse nouvelle par lot, courte, sur l'état gelé, pour C13, C14, C23 et C25, parce que le texte a changé depuis les audits des 3 et 4 septembre (C25 n'en avait jamais eu).» (`coordination/JOURNAL_DES_RELAIS.md`)

**Chronologie, lue sur les horodatages des commits et l'index des décisions :**

| date et heure du commit | décisions | ce qui bouge |
|---|---|---|
| 2026-09-16, 19 h 27 | — | L1.C25 S2 et S3 : empreinte d'exemplaire |
| 2026-09-16, 20 h 59 | D63 (branche B de D54, « Govillot substitution ok ») | L1.C25 S9 rebasée et ouverte |
| 2026-09-16, 22 h 40 | D68 | A43 (3) scindé ; Union européenne des paiements étudiée |
| 2026-09-16, 23 h 21 | D69 | règle de révision des parités |
| 2026-09-17, 07 h 30 | D70, D71 | obligations des excédentaires automatiques ; aucune charge sur les soldes |
| 2026-09-17, 07 h 55 | D72 à D74 | recyclage en prêt ; procédure structurelle |
| 2026-09-17, 08 h 31 | D75, D76 | financement des guichets ; démurrage de reflux maintenu |
| 2026-09-17, 08 h 59 | D77 à D79 | reliquat converti ; démurrage hors compensation ; procédure côté importateur |
| 2026-09-17, 09 h 30 | D80 à D82 | procédure côté importateur instruite |
| 2026-09-17, 12 h 25 | D83 à D85 | seuils du plafond |
| 2026-09-17, 12 h 59 | D86, D87 | jugement d'applicabilité de (3b) |
| 2026-09-17, 13 h 23 | — | L1.C31 § 6 harmonisé |
| 2026-09-17, 16 h 01 | D88 à D91 | sortie des dettes durables ; (3b) rejugée |

**Entrées du registre modifiées entre `b26e9971` et `HEAD`** (diff de `corpus/arbitrages.yaml`) : A32 (liens), A45, A43, EXCEDENT-DU-SYMPOSIUM, F1, COMPENSATION-SYMETRIQUE, et trois entrées créées — PROCEDURE-STRUCTURELLE, DEPENDANCE-ESSENTIELLE, SORTIE-DES-DESEQUILIBRES-DURABLES. **Le registre rattache L1.C25 à A45 et à COMPENSATION-SYMETRIQUE** (champ `chapitres`) ; **il ne rattache L1.C23 à aucune entrée.** Dans `protocoles/falsification.md`, F1 reçoit trois notes et F6 six, toutes du 2026-09-17.

**Antérieurs au gel, nommés par la mission, et absents des deux chapitres** : A46 et A47 (2026-09-09), A32 (2026-09-09), L1.C31 (`verifie` depuis le 2026-09-13). L1.C23 a pourtant reçu une révision de fond le 2026-09-15 sans les intégrer ; aucune ligne de L1.C23 ne nomme A46, A47, A32 ou A43 (recherche mécanique). Ils figurent en section 3, **datés comme antérieurs**, pour que le relevé ne les présente pas comme des nouveautés.

## 2. L1.C25 — ce qu'il faudrait propager après l'audit

### G25-1 — La clause de Keynes : deux versions du texte, et une étiquette de `passe-2.md` qui ne correspond pas à l'entrée S12

- **Passage.** C«A charge of 1 per cent per annum shall be payable to the Reserve Fund of the Clearing Union on the amount of the excess of the average balance of a member state, whether it is a credit or a debit balance, above a quarter of its quota» (l. 185). L'entrée S12 nomme les *Collected Writings* et reste fermée : C«OUVERTE DE PREMIÈRE MAIN : document procuré par l'auteur le 2026-09-04 et lu directement ; aucun intermédiaire, aucune synthèse.» (l. 70)
- **Fondement postérieur au gel.** Les sections du 17 lisent la version d'avril 1943 sur deux reproductions publiques, et la lettre diffère : P«A member State shall pay to the Reserve Fund of the Clearing Union a charge of 1 per cent, per annum on the amount of its average balance in bancor, whether it is a credit or a debit balance, in excess of a quarter of its quota» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 »). Et la section de D88 à D90 attribue à S12 un autre exemplaire que celui que S12 nomme : P«texte du plan publié au *Federal Reserve Bulletin* de juin 1943, p. 511, § 8 [L1.C25, S12]» (section « D87 INSTRUITE — LA SORTIE DES DETTES DURABLES, D88 À D90, 2026-09-17 »).
- **Antérieur au gel, et toujours en attente.** D55 : A«S12 : deux citations de l'entrée ont la lettre d'un projet antérieur reproduit dans les *Collected Writings*, non celle du Livre blanc d'avril 1943 lisible sur FRASER (5.1.2)» (`protocoles/architecture-tranche-2-lot-2.md`).
- **À propager.** **C, conditionné à D55.** Soit S12 est rebasée sur le Livre blanc et les deux citations alignées, et l'étiquette de `passe-2.md` devient exacte ; soit S12 reste sur les *Collected Writings*, et l'étiquette « [L1.C25, S12] » de `passe-2.md` est à corriger.

### G25-2 — Même la charge sur les soldes créditeurs était remissible

- **Passage.** C«La seule contrainte effective pesant sur lui était la charge de 1 à 2 % l'an.» (l. 189) ; et, au paragraphe suivant, C«une charge de un à deux pour cent l'an, assortie d'une obligation de discuter dont l'issue restait à la discrétion du créancier lui-même» (l. 195).
- **Fondement postérieur au gel.** P«The Governing Board may, at its discretion, remit the charges on credit balances» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; P«La seule obligation automatique du créancier était la charge» (même section).
- **À propager.** **N.** La charge était automatique dans son principe et remissible par le conseil : le fait va dans le sens du § 4 (« le seuil de tolérance du créancier … plus bas que ce que le corpus supposait ») et le durcit. À verser avec la source retenue par D55.

### G25-3 — Keynes avait envisagé l'annulation des soldes créditeurs, et l'avait écartée en prévision du refus ; le dispositif l'a adoptée

- **Passage.** C«Troisième fait — Keynes avait prévu le refus et en avait nommé la cause.» (l. 193)
- **Fondement postérieur au gel.** P«For the appropriate provision might be to require the eventual cancellation or compulsory investment of persistent bancor credit balances accumulating in excess of a member’s quota» et P«it might be felt to impose on creditor countries a heavier burden than they can be asked to accept before having had experience of the benefit to them of the working of the plan as a whole.» (section « A43 (3b), CONDITION (4) — QUI FINANCE LES GUICHETS ET LA RECONVERSION, 2026-09-17 ») ; P«In the case of credit balances no rigid maximum has been proposed.» (section « A43 (3b), CONDITION (3) — LES SEUILS DU PLAFOND, D83 À D85, 2026-09-17 »). **Et la conception retient depuis ce que Keynes écartait** : COMPENSATION-SYMETRIQUE R«OBLIGATIONS DES EXCÉDENTAIRES AUTOMATIQUES, sans vote : réévaluation (D69) ; au-delà du plafond, recyclage EN PRÊT, puis reliquat sans destinataire ANNULÉ (D77).» ; F«l'adhésion d'un exportateur de biens essentiels vaut désormais consentement d'avance à l'annulation de ses créances au-delà du plafond.»
- **À propager.** **N.** Un quatrième fait dans le même sens que les trois du § 4 : l'auteur du plan avait lui-même retiré la disposition la plus lourde pour le créancier. Le § 5 doit pouvoir le rapprocher de ce que le dispositif demande désormais (G25-5).

### G25-4 — La règle « la disposition qui contraint le créancier est la disposition qui saute » rencontre deux modes qui ne sont pas « sauter »

- **Passage.** C«Trois configurations, une seule règle : **la disposition qui contraint le créancier est la disposition qui saute.**» (l. 203)
- **Fondements postérieurs au gel.**
  - **Union européenne des paiements, 1950-1958** — adoptée, molle pour le créancier, tenue par un payeur extérieur : P«Without West Germany's politically motivated generosity, the EPU would probably have collapsed by late 1955 or 1956» ; P«C'est l'asymétrie que F6 a relevée chez Keynes : le déficitaire subissait, l'excédentaire délibérait — et l'Union n'a tenu que par la générosité d'un créancier.» (section « A43 (3) SCINDÉ PAR L'AUTEUR — L'EXCHANGE STANDARD À PARITÉS ADMINISTRÉES, 2026-09-16 »). **Rang** : P«RÉSERVE DE RANG : ce sont deux études SECONDAIRES.» (même section).
  - **Procédure européenne des déséquilibres, 2011** — adoptée, jamais activée : P«La disposition qui contraint n'a pas sauté : elle a été adoptée, puis jamais activée.» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; F«C'est le mode d'échec que L23 avait nommé pour un vote, étendu à une règle : **l'adoption n'est pas l'application.**»
  - **Accord de Londres, 1953** — concessions de créanciers publics : P«make important concessions with respect to the priority of their claims for post-war economic assistance [...] and with respect to the total amount of these claims» (section « D87 INSTRUITE — LA SORTIE DES DETTES DURABLES, D88 À D90, 2026-09-17 »). Accord de dettes, non changement de système monétaire : une piste, pas un contre-exemple.
  - **Statuts du Fonds, article VII** — P«La clause de la monnaie rare se déclenche sur les avoirs du Fonds, non sur l'excédent du créancier» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 »). **Lue dans l'édition de 2020 des statuts**, non dans le texte de 1944 : c'est la piste d'une disposition de Bretton Woods visant le créancier, adoptée sous une forme qui ne l'oblige pas, à vérifier sur le texte d'origine avant tout emploi.
- **À propager.** **O.** La règle du § 4 rencontre deux modes documentés qui ne sont pas « sauter » : adoptée molle, adoptée non activée. Branches : amender la règle, la borner par une condition comme l'annotation L23 l'a fait (l. 273), ou la garder en déclarant ces cas hors de son objet (union régionale, procédure interne). **Le contrôle 4 du dossier vise exactement ce point** : A«Un principe de sélection établi sur trois cas choisis par celui qui le formule est-il un résultat ?» (`protocoles/dossier-audit-tiers-L1-C25.md`). À trancher après l'audit, non avant.
- **Numérotation à harmoniser.** F6 nomme la procédure européenne F«UN QUATRIÈME PRÉCÉDENT, ET IL PRÉCISE LE SCHÉMA SANS LE CONTREDIRE.» ; le chapitre a déjà son quatrième : C«Un quatrième cas contredit le schéma tiré par ce chapitre, et le corpus le porte sans l'atténuer» (l. 267).

### G25-5 — Ce que le dispositif demande au créancier n'est plus « renoncer à sa position », mais accepter d'avance l'automaticité et l'annulation

- **Passage.** C«Le dispositif demande à l'émetteur dominant de renoncer à sa position.» (l. 209) ; C«Keynes proposait de pénaliser les excédents ; il perdit. Le dispositif propose de supprimer la position de devise clé, ce qui est davantage.» (l. 211)
- **Fondements postérieurs au gel.** A43 R«(3a) PARITÉS FIXES — non applicable sans transferts permanents des excédentaires. (3b) PARITÉS ADMINISTRÉES en coalition, capitaux réglementés — EXPÉRIMENTABLE : chocs passagers (D86) ; déséquilibres durables sous conditions — inflation, adhésion des créanciers (D91). Remplacement mondial non applicable.» ; P«Mais le créancier doit l'accepter en adhérant, et ce qu'on lui demande d'accepter d'avance est exactement ce qu'il gardait à sa décision en 1943 : la réévaluation.» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; P«(D91) LES DÉSÉQUILIBRES DURABLES DEVIENNENT EXPÉRIMENTABLES EN COALITION, SOUS DEUX CONDITIONS DÉCLARÉES : (1) MESURER L'INFLATION QU'IMPORTERAIT LA DÉVALUATION ; (2) OBTENIR L'ADHÉSION DES CRÉANCIERS À L'ANNULATION.» (section « A43 (3b) REJUGÉE — LES DÉSÉQUILIBRES DURABLES, D91, 2026-09-17 ») ; F«F6 n'est plus une objection parmi d'autres, c'est la condition du verdict.»
- **Antérieur au gel.** L«Le présent test n'utilise donc pas la promesse d'un remplacement mondial comme résultat attendu.» ; et l'annotation du Livre 5 dans le chapitre même : C«Or L3.C09 a établi que le dispositif ne remplace pas le système existant : il s'y ajoute.» (l. 257)
- **À propager.** **C et O.** C : dans la seule forme que le registre déclare expérimentable, les créanciers visés sont les membres excédentaires d'une coalition, qui consentent à l'adhésion à la réévaluation automatique, au recyclage en prêt, à la conversion du reliquat et à l'annulation au-delà d'un quota ; la comparaison avec Keynes du § 5 se réécrit sur ces termes, qui sont précisément ceux que Keynes laissait au créancier ou écartait (G25-3). O : que la position de l'émetteur dominant reste « visée » n'est plus établi, le remplacement mondial étant déclaré non applicable ; le contrôle 8 du dossier conteste en outre la prémisse de la l. 209 : A«Les réserves servent à l'intervention et à la précaution, non à la mécanique de conversion.» (`protocoles/dossier-audit-tiers-L1-C25.md`).

### G25-6 — La question ouverte du § 5 a reçu une pièce historique et une réponse de conception, et aucune ne règle l'adoption

- **Passage.** C«La question que la thèse de la fenêtre laisse entièrement ouverte est celle-ci : par quel mécanisme le pays dont la position est visée pourrait-il accepter, ou ne pas pouvoir empêcher, le dispositif ? Aucun chapitre du corpus n'y a répondu.» (l. 213)
- **Fondements postérieurs au gel.** P«The US used further bilateral payments to induce countries such as Belgium, who expected to end up as structural creditors to the EPU, to participate in the scheme» ; P«C'est la condition (4) de (3b), et le précédent la pose sans la résoudre pour NEMO : qui tient le rôle des États-Unis de 1950 ?» (section « A43 (3) SCINDÉ PAR L'AUTEUR — L'EXCHANGE STANDARD À PARITÉS ADMINISTRÉES, 2026-09-16 ») ; P«l'institution les exécute dans ses comptes, et l'adhésion vaut consentement préalable.» et P«L'AUTOMATICITÉ RÈGLE L'APPLICATION, PAS L'ADOPTION.» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; P«Un créancier structurel ne rejoint pas une union de paiements sans contrepartie» (section « A43 (3b) — L'ACCUMULATION DE L'EXPORTATEUR SOUS CHOC STRUCTUREL, 2026-09-17 »).
- **À propager.** **N et O.** « Aucun chapitre n'y a répondu » reste vrai des chapitres. Mais le corpus tient désormais un mécanisme d'entrée documenté — des paiements d'un tiers pour faire adhérer un créancier structurel, sur deux études secondaires — et une réponse de conception qui déplace la question à l'adhésion sans la résoudre. Le texte aligné expose les deux, sans conclure que l'adoption devient plausible.

### G25-7 — « La seule voie que l'histoire laisse ouverte » ne tient plus sur sa propre source

- **Passage.** C«Il fournit la seule voie que l'histoire examinée ici laisse réellement ouverte : non pas convaincre le détenteur de renoncer à un avantage, mais le moment où la charge excède l'avantage.» (l. 221) ; C«Une stratégie fondée sur le devoir exorbitant [S9] et sur la réversibilité attestée des positions dominantes [S10] serait plus solide, parce qu'elle nomme un mécanisme au lieu d'espérer un moment.» (l. 233)
- **Fondements postérieurs au gel.** L'entrée S9 rebasée le 2026-09-16 le dit elle-même : C«elle n'écrit nulle part que la charge puisse excéder l'avantage, ni que l'émetteur puisse la refuser.» (l. 54) ; F«La jambe de temps calme est une prime ; le devoir exorbitant n'est pas un coût net.» ; A«Ces deux phrases sont des inférences du corpus, balisées `hypothese`, et la source rebasée ne les appuie pas : elle documente la charge, pas son excès.» (`coordination/JOURNAL_DES_RELAIS.md`)
- **Antérieur au gel, et non intégré au texte gelé.** F«La stratégie que le corpus tenait pour la seule plus solide que l'attente d'une […] fenêtre tombe donc pour une raison plus profonde que l'absence de source.» ; et la sortie que F6 retient à la place : F«fragilise l'ordre existant ; **il ne recommande pas NEMO IMS.**»
- **À propager.** **C ou R, à l'auteur — c'est le point le plus lourd des deux chapitres.** La voie que le § 6 présente comme la seule, et sur laquelle le § 7 fonde la stratégie « plus solide », repose sur une inférence que la source rebasée ne porte pas et que F6 tient pour tombée depuis le 2026-09-07. Question G3.

### G25-8 — Ce que le rebasement de S9 laisse intact

- **Passage.** C«L'émetteur de la monnaie de réserve détient des actifs risqués à l'étranger contre des engagements liquides et sûrs ; il est de ce fait l'assureur du reste du monde et supporte des pertes en capital massives sur sa position extérieure nette lors des crises, au moment même où sa devise s'apprécie [S9].» (l. 221)
- **Fondement postérieur au gel.** C«« pertes en capital » est la traduction du corps, fidèle au mécanisme.» (l. 54) ; C«Son chiffre de 19 % du PIB ne mesure pas ces seules pertes.» (l. 54)
- **À propager.** **K.** L'attribution de la phrase descriptive tient sur le texte de 2010 ; la réserve sur les 19 % vise un chiffre que le corps n'emploie pas.

### G25-9 — La pièce que la fiche de refonte associait au chapitre a changé de contenu

- **Fondement de la fiche (2026-09-10).** X«disposition que ce chapitre montre perdue à Bretton Woods : la charge sur les […] excédents. **A45 ne s'applique pas ici** : il porte sur le soutien aux […] importations essentielles, non sur le traitement des soldes persistants.»
- **Fondements postérieurs au gel.** P«Aucune charge n'est prélevée sur les soldes**, ni débiteurs ni créditeurs ; le financement des allocations solidaires passe à l'émission, sous la règle d'émission et le reflux.» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; COMPENSATION-SYMETRIQUE R«AUCUNE CHARGE GRADUÉE SUR LES POSITIONS ; démurrage hors compensation (D76, D78).» ; A45 R«QUI FINANCE (D75, 2026-09-17) : émission au besoin, découvert apuré par l'excédent du reflux ; le besoin structurel, non apuré, est émission permanente (F1).» ; et le précédent de ce financement, lu dans le plan de 1943 : P«Le découvert apuré y figure**, pour les organismes internationaux de secours et de reconstruction» (section « A43 (3b), CONDITION (4) — QUI FINANCE LES GUICHETS ET LA RECONVERSION, 2026-09-17 »).
- **À propager.** **O, et une question de place.** Le corps de L1.C25 ne nomme ni COMPENSATION-SYMETRIQUE ni A45. Si le chapitre désigne un jour la réponse du dispositif à la défaite de 1944, ce ne sera plus « la charge sur les excédents » : D71 l'a retirée au profit de la réévaluation automatique, du recyclage en prêt et de l'annulation. Le registre rattache pourtant A45 à L1.C25, contre la fiche. Question G2.

### G25-10 — La réforme de 1967 (facultatif)

- **Passage.** C«L'émission de droits de tirage spéciaux, décidée en 1967 pour fournir au système une liquidité de réserve qui ne fût pas du dollar, « was too little too late » [S5].» (l. 161)
- **Fondement postérieur au gel.** P«Le précédent couvre l'émission ; il ne couvre ni un versement au besoin d'un pays, ni l'absence de vote.» (section « A43 (3b), CONDITION (4) — QUI FINANCE LES GUICHETS ET LA RECONVERSION, 2026-09-17 »)
- **À propager.** **N, basse priorité.** Les règles d'allocation lues dans les statuts (taux uniformes en pourcentage des quotes-parts, majorité de 85 %) sont une piste pour expliquer « too little » ; lues dans l'édition de 2020, elles ne valent pas fait historique pour 1967.

## 3. L1.C23 — ce qu'il faudrait propager après l'audit

**Réponse directe à la question de la mission.** **Les sections du 17 septembre ne nomment ni la centralisation, ni la polycentricité, ni L1.C23** (recherche de « centralis », « robust », « polycentr », « modularit », « diversit », « uniform », « comité », « autorité » dans `passe-2.md` à partir de la l. 7139). Elles touchent le chapitre **indirectement**, par quatre voies : l'objection des zones monétaires (G23-2, G23-3), le choix de la règle automatique contre la délibération (G23-4), le seul essai de résistance du dispositif à des chocs combinés (G23-5), et un emploi du mot « robuste » dans un autre sens (G23-5). A46 et A47, que la mission nomme, sont **antérieurs au gel** (G23-1, G23-6).

### G23-1 — « La décision d'émission est prise par un organe unique » (A46, antérieur au gel)

- **Passage.** C«La décision d'émission est prise par un organe unique. Et le référentiel d'échange annoncé est un étalon unique.» (l. 380)
- **Fondements (2026-09-09).** A46 R«CINQ CENTRES DE RESPONSABILITÉ INDÉPENDANTS, NON CINQ INSTITUTIONS : l'organisation juridique reste à concevoir.» ; A46 R«NUL N'EST L'UNIQUE NI LE DERNIER JUGE DE SES ACTES — l'autocorrection reste permise.» ; la lecture de la cartographie, qui n'est pas un arbitrage : X«A46 (cinq fonctions séparées) est une […] **réponse partielle** à cette objection : elle décentralise le pouvoir, pas la […] connaissance.»
- **À propager.** **C** sur le second plan de l'objection : l'« organe unique » n'est plus la conception arbitrée. **O** sur la portée : que cinq centres de responsabilité répondent à une objection de diversité et de modularité n'est tranché par aucun arbitrage.

### G23-2 — Le troisième plan et l'objection des zones monétaires, après la scission d'A43

- **Passage.** C«Or le taux de conversion de l'unité émise est fixe, « bien que révisable » (L1.C19 § 6).» (l. 386) ; C«Un territoire frappé reçoit donc une émission calculée sur un barème mondial, convertie à un taux qui ne reflète pas son choc, et il lui reste l'ajustement par les quantités.» (l. 386)
- **Antérieur au gel.** A32 R«Trois propriétés retenues et nommées : PARITÉS STABLES OU ADMINISTRÉES, AUTONOMIE MONÉTAIRE NATIONALE, COMPTE DE CAPITAL RÉGLEMENTÉ.»
- **Fondements postérieurs au gel.** A43 R«(3a) PARITÉS FIXES — non applicable sans transferts permanents des excédentaires.» ; P«De S0 à S3, figer les parités multiplie la contraction du déficitaire par 1.8 à 2.7» avec sa réserve P«Dans ce modèle, la parité est le SEUL canal qui agit sur les volumes échangés : **le sens de l'effet était presque acquis d'avance.**» (section « A43 (3) SCINDÉ PAR L'AUTEUR — L'EXCHANGE STANDARD À PARITÉS ADMINISTRÉES, 2026-09-16 ») ; P«(D89) AU-DELÀ DU SEUIL, LA DETTE DE RECYCLAGE EST ANNULÉE, ET LA PARITÉ DU DÉBITEUR GLISSE, SANS BUTÉE, TANT QUE SES ÉCHANGES DE LA PÉRIODE SONT DÉFICITAIRES.» (section « D87 INSTRUITE — LA SORTIE DES DETTES DURABLES, D88 À D90, 2026-09-17 »)
- **À propager.** **O.** Pour les parités de l'Exchange Standard, le travail postérieur au gel mesure, sous parités figées (3a), le mécanisme que le chapitre décrit, et garde sous parités administrées (3b) un canal de change réglé, expérimentable en coalition seulement. La prémisse « taux fixe » ne décrit plus la seule forme du dispositif. **Mais l'objection du chapitre vise le taux de conversion de l'unité émise, non les parités entre monnaies nationales**, et le dossier le conteste : A«Vérifie que l'objection tient pour une unité de compte convertie puis détruite.» (`protocoles/dossier-audit-tiers-L1-C23.md`). Question G4.

### G23-3 — « Une perturbation locale n'est pas amortie localement » : le corpus a désormais un modèle de chocs asymétriques

- **Passage.** C«**C'est le contraire de la modularité que la robustesse exige** : une perturbation locale n'est pas amortie localement, elle est transmise.» (l. 386)
- **Fondements postérieurs au gel.** P«Des chocs passagers isolés (S0, S1, S3) ne laissent ni anomalie ni dette, même à deux cents périodes.» et P«Mauvaises récoltes toutes les dix : le pays pauvre doit 2,4 quotas» (section « A43 (3b) — LE JUGEMENT D'APPLICABILITÉ, D86 ET D87, 2026-09-17 ») ; corrigé ensuite : P«Elles tenaient surtout au signal masqué.» et P«À quatre cents périodes, les récoltes répétées atteignent aussi le seuil» (section « D87 INSTRUITE — LA SORTIE DES DETTES DURABLES, D88 À D90, 2026-09-17 ») ; limites : P«Le calibrage et l'inflation (F1), l'avantage sur les instruments existants (F10), et un monde de plus de trois pays.» (section « A43 (3b) — LE JUGEMENT D'APPLICABILITÉ, D86 ET D87, 2026-09-17 »)
- **À propager.** **N et O.** Le seul instrument du corpus qui joue des chocs asymétriques, récoltes comprises, est un modèle à trois pays, non calibré, à l'échelle nationale et non territoriale. Il ne confirme ni ne réfute « elle est transmise » ; il donne des branches — absorption par la révision des parités, les guichets et les procédures, puis sortie par dévaluation. À exposer avec son statut de résultat de modèle.

### G23-4 — Règle automatique ou délibération : centralisation de plus, ou veto de moins ?

- **Passage.** C«Sur chacun de ces trois plans, le dispositif choisit l'uniformité là où sa propre littérature de référence recommande la diversité.» (l. 380) ; C«mesuré aux critères de la littérature dont il tire son objectif, le dispositif est centralisé là où cette littérature recommande la diversité et la modularité.» (l. 410)
- **Fondements postérieurs au gel.** P«l'institution les exécute dans ses comptes, et l'adhésion vaut consentement préalable.» et P«Une obligation qu'il faut activer par un vote glisse vers le cas européen.» (section « A43 (3b), CONDITION (2) — LES OBLIGATIONS DES EXCÉDENTAIRES SONT AUTOMATIQUES, ET AUCUNE CHARGE N'EST PRÉLEVÉE, 2026-09-17 ») ; P«Préférer de petits pas et une formule à un comité est un choix de principe» (section « A43 (3b), CONDITION (1) — LA RÈGLE DE RÉVISION DES PARITÉS, CHOISIE PAR L'AUTEUR LE 2026-09-16 ») ; P«the creditors would always have an interest in vetoing a devaluation and the debtors an interest in vetoing an appreciation of the EPU unit» (section « A43 (3) SCINDÉ PAR L'AUTEUR — L'EXCHANGE STANDARD À PARITÉS ADMINISTRÉES, 2026-09-16 »)
- **À propager.** **O.** Depuis le 17, les obligations des créanciers relèvent d'une règle écrite unique, exécutée par une seule institution, sans vote, au motif du veto intéressé. Deux lectures, que le corpus n'a pas de critère pour départager : un quatrième plan d'uniformité (une règle, un exécutant), ou la suppression d'un pouvoir discrétionnaire central (aucun organe ne décide). Le texte aligné expose les deux.

### G23-5 — Le dispositif mesuré à ses propres chocs : une seule condition porte le verdict

- **Passage.** C«C'est l'objection principale de ce chapitre, et elle est d'autant plus sérieuse qu'elle ne vient pas d'une école hostile : elle vient de la littérature dont le livre tire son objectif.» (l. 376)
- **Fondements postérieurs au gel.** P«Le jugement a été instruit en cherchant d'abord ce qui démentirait un verdict favorable : horizon long, chocs combinés et répétés, créancier qui n'adopte pas ses obligations.» ; P«TOUT REPOSE SUR L'AUTOMATICITÉ DES OBLIGATIONS DU CRÉANCIER.» ; P«créancier qui délibère, comme dans tous les précédents, 334 dépassements et 67 masses négatives» (section « A43 (3b) — LE JUGEMENT D'APPLICABILITÉ, D86 ET D87, 2026-09-17 »)
- **À propager.** **N, si l'auteur veut que le § 5 mesure le dispositif sur ses critères.** Le seul essai de résistance conduit sur le dispositif montre, dans le modèle, une tolérance aux chocs combinés et répétés et une dépendance entière à un comportement. **Deux précautions.** La robustesse du chapitre porte sur l'imprévu — C«La **robustesse** ajoute une exigence à la résilience : l'absorption de perturbations **non anticipées**, celles pour lesquelles le système n'a pas été conçu [S3].» (l. 288) —, alors qu'un jeu de scénarios ne couvre que le prévu. Et `passe-2.md` emploie « robuste » dans un autre sens que le concept `robustesse` du vocabulaire : P«LE CORRIDOR N'A PAS D'OPTIMUM ROBUSTE.» (section « A43 (3b), CONDITION (3) — LES SEUILS DU PLAFOND, D83 À D85, 2026-09-17 ») ; à ne pas reprendre tel quel dans le chapitre.

### G23-6 — « Aucun critère pour trancher » la redondance : A47 fournit une procédure, non un critère (antérieur au gel)

- **Passage.** C«Le dispositif ne fournit aucun critère pour trancher, et il ajoute au barème de qualification (P28) un second gisement de contestation.» (l. 308)
- **Fondements (2026-09-09).** A47 R«Seuils fixés d'avance par l'AUTORITÉ DÉMOCRATIQUE après EXPERTISE PLURALISTE ; qualification MOTIVÉE.» ; USAGE-DES-INCERTITUDES R«Non réductible pour la décision présente et grave : marge de précaution.» ; QUALIFICATION-DU-RISQUE R«LA SEULE PIÈCE OUVERTE DE A47 : horizons sectoriels, seuil de confiance, DÉLAI UTILE et seuils numériques, à fixer PAR DOMAINE selon la procédure d'A47, sans rouvrir son principe.»
- **À propager.** **C.** L'énoncé reste vrai d'un critère ; le texte aligné nomme la procédure qu'A47 arrête, et le fait qu'une marge de précaution est une redondance décidée par procédure. Les seuils restent ouverts. Rien de postérieur au gel.

### G23-7 — Capture et recentralisation (antérieurs au gel)

- **Passage.** C«toute décision administrative qui crée une rente attire des ressources réelles dépensées pour l'obtenir plutôt que pour produire [S13]» (l. 308)
- **Fondements.** L«La recentralisation est un risque institutionnel documenté dans un cas.» ; MODELE-ADVERSAIRE R«Et l'EFFET INSTITUTIONNEL CONTRAIRE — un instrument d'allocation a recentralisé la gouvernance qu'il devait ouvrir.» ; MESURE-EXTERIEURE R«La capture se DÉTECTE et se RÉDUIT, jamais ne s'élimine.»
- **À propager.** **N.** Le corpus tient un cas documenté de recentralisation et deux pièces ouvertes sur la capture, qui touchent l'objection de centralisation du § 5.

### G23-8 — « La monnaie émise ne crée aucune capacité physique » et la formulation vérifiée de L1.C31 (antérieure au gel)

- **Passage.** C«La monnaie émise ne crée aucune capacité physique : elle redistribue l'accès à celles qui existent.» (l. 322)
- **Fondement.** L«Il ne peut provenir que de capacités inutilisées effectivement mobilisées, d'une réallocation depuis d'autres usages, d'un gain d'organisation ou d'un accès supplémentaire aux importations.»
- **À propager.** **C**, sur la forme de L1.C31, qui fait place aux capacités inutilisées. Recoupe le contrôle 6 du dossier : A«Le § 3 suppose le plein emploi des facteurs.» (`protocoles/dossier-audit-tiers-L1-C23.md`).

### G23-9 — Les trois traits : un balayage postérieur au gel (constat documentaire, non décision)

- **Passage.** C«Le même résultat s'énonce dans les trois traits du § 2 : redondance, diversité, modularité.» (l. 378)
- **Fondement.** Relevé du 2026-09-16 (18 h 28) porté dans la vérification de L1.C28 : A«« redundan » ZÉRO occurrence, « modular » ZÉRO ; l'article parle de diversité, quatorze fois, et de CAPACITÉ DE RÉSERVE, vingt-quatre fois.» (`corpus/livre-01-monnaie-finance-limites-planetaires/c28-au-dela-du-pib.md`)
- **À propager.** **À décider après l'audit.** Le balayage porte sur S5 (Ulanowicz et al.) et S4 (Holling), non sur S6 (Goerner, Lietaer, Ulanowicz), que le § 5 invoque ; il recoupe le contrôle 2 du dossier. S6 reste à balayer avant toute correction.

## 4. Ce que ce relevé a trouvé et qui ne se propage pas dans ces deux chapitres

- **L'entrée F6 du registre n'a pas suivi `falsification.md`** : F6 R«Une objection lui est versée par L17.C03.» (mise à jour du 2026-09-08), quand le falsifieur a reçu six notes le 2026-09-17. Correction du registre, non des chapitres.
- **L1.C31 § 6 attend toujours sa correction** : D«la phrase qui dit les déséquilibres durables « non applicable en l'état », leurs dettes sans règle de sortie, est inexacte depuis D89 et D91 ; l'auteur a choisi de l'amender plus tard.» Elle ne touche ni L1.C23 ni L1.C25.
- **A4**, que L1.C23 désigne comme l'objet de la décision de conception (l. 390 et 412), **n'est pas une entrée du registre** : c'est un relevé de `passe-2.md` § 7, partiellement tranché selon la vérification de la l. 257. Antérieur au gel ; à signaler au traitement.

## 5. Questions à l'auteur

**G1 — Le gel de L1.C25 est rompu sur l'en-tête, non sur le texte.** Options : **(a)** tenir l'audit pour valide, le corps et le résumé étant inchangés (empreinte éditoriale identique), et traiter comme dépassée toute objection portant sur S2, S3 ou S9 ; **(b)** si le dossier n'est pas encore soumis, le régénérer sur l'état actuel, sous la nouvelle empreinte, sans toucher au chapitre ; **(c)** le soumettre tel quel et joindre au traitement le constat de la section 0. Conséquences : (a) et (c) laissent l'auditeur objecter sur une S9 « non ouverte » qui ne l'est plus ; (b) coûte une régénération, qui est mécanique. **Recommandation : (b) si le dossier n'est pas parti, (a) s'il l'est**, parce que l'objet de l'audit est le texte, et que le texte n'a pas bougé.

**G2 — Où verser la chaîne A43 ?** Options : **(a)** dans L1.C25, les précédents qui touchent F6 (version d'avril 1943, Union européenne des paiements, procédure européenne, Londres 1953) ; dans L1.C26, les pièces de conception (D69 à D91), avec un renvoi depuis le § 5 de L1.C25 ; **(b)** tout dans L1.C25 ; **(c)** tout hors du Livre 1, dans un livre spécialisé, L1.C25 et L1.C26 renvoyant. Conséquences : (b) alourdit un chapitre dont la fonction est X«Chronologie, et thèse stratégique de l'adoption.» ; (c) retire du Livre 1 ce qui conditionne son seul verdict favorable. **Recommandation : (a)**, parce que le registre ne rattache les entrées créées le 17 (PROCEDURE-STRUCTURELLE, DEPENDANCE-ESSENTIELLE, SORTIE-DES-DESEQUILIBRES-DURABLES) qu'à L1.C26, et que la cartographie veut un Livre 1 lisible : X«Les développements techniques, juridiques et documentaires **restent […] dans leurs livres spécialisés**, avec renvois précis.» La même décision dira si le rattachement d'A45 à L1.C25 dans le registre est voulu.

**G3 — Le § 6 de L1.C25 (G25-7).** Options : **(a) C** — garder la voie en la déclarant conjecture du corpus, non appuyée par S9, tenue pour tombée par F6 depuis le 2026-09-07, et nommer la sortie que F6 retient avec ses réserves ; **(b) R** — retirer « la seule voie » et la stratégie du § 7 ; **(c)** attendre ce que l'audit en dit. Conséquences : (a) garde la trace du raisonnement et de sa chute ; (b) rend le chapitre plus court et plus sombre, sans voie ouverte ; (c) diffère un point qui ne dépend d'aucune objection nouvelle. **Recommandation : (a)**, parce que la condition d'échec de F6 porte précisément sur l'existence d'un tel mécanisme : l'effacer ferait disparaître la branche au lieu de dire qu'elle n'est pas documentée.

**G4 — Quel taux vise l'objection des zones monétaires de L1.C23 (G23-2) ?** Options : **(a)** le taux de conversion de l'unité émise (L1.C19 § 6) — A43 (3b) ne la touche pas, et le contrôle 7 décide ; **(b)** les parités de l'Exchange Standard — la scission d'A43 la gouverne, et elle devient une branche ouverte ; **(c)** les deux, séparées. Conséquences : (a) peut faire tomber la troisième voie de l'objection centrale, donc le « résultat » des trois traditions (contrôle 8 du dossier) ; (b) la maintient sous une forme conditionnelle ; (c) oblige à deux paragraphes. **Recommandation : attendre le rapport sur le contrôle 7, puis (c)**, parce que L1.C19 § 6 rattache lui-même le taux de conversion au triangle d'incompatibilité, que A32 et A43 tranchent pour les parités.

## 6. Ce que ce relevé ne vérifie pas

- **Aucun rapport d'audit tiers de L1.C23 ou de L1.C25 n'est dans `protocoles/`** ; ce relevé ne sait pas si les dossiers ont été soumis.
- **Les pièces nouvelles ne sont pas relues ici** : les citations de Keynes, de l'Union européenne des paiements, de la procédure européenne, de l'Accord de Londres et des statuts du Fonds sont prises dans `passe-2.md`, qui les dit vérifiées ; les sources primaires de l'Union restent à acquérir, et l'article VII est lu dans l'édition de 2020.
- **Les résultats du modèle `nemo_soldes.py` ne sont pas rejoués** ; ce sont des résultats de modèle à trois pays, non calibrés, qui ne valent pas preuve.
- **Le lien entre les sections du 17 septembre et L1.C23 est une lecture de ce relevé** : aucune de ces sections ne nomme le chapitre.
- **Les modifications postérieures au gel des chapitres voisins** (L1.C19, L1.C22, L1.C24, L1.C26, L1.C28) ne sont pas contrôlées pour leur effet sur les renvois de L1.C23 et L1.C25, hors le balayage de L1.C28 cité en G23-9.
- **Le statut de D55** : la feuille du lot 2 ne lui porte aucune marque d'application et S12 n'a pas changé ; le recomptage du 2026-09-16 ne la range pourtant pas parmi les dix-neuf décisions restantes. L'écart n'est pas résolu ici.
