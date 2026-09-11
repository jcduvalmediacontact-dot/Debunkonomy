# Architecture conceptuelle de L1.C07 — proposition soumise à validation

**Établie le 2026-09-11 par Claude, sur la directive de l'auteur, selon la
méthode éprouvée sur L1.C08.** Ce document précède la réécriture : le chapitre
n'est pas modifié, rien n'est commité. Il porte les sources ouvertes avec
leurs éditions et leurs passages, la vérification séparée des cinq
propositions de la Banque d'Angleterre, ce que Withers et Schumpeter
établissent et n'établissent pas, la matrice affirmation-source du chapitre
actuel, la structure proposée, la liste des retraits et reformulations, et la
trace des deux sections de travail à retirer du corps. Toutes les citations
ont été retrouvées mécaniquement dans les textes acquis (vérificateur de
session), sauf mention contraire.

## 1. État du chapitre et décisions éditoriales de l'auteur

**État au 2026-09-11.** Statut `brouillon`, `revision_de_fond` 2026-09-07,
trois sources toutes `a_requalifier` (Banque d'Angleterre 2014, Withers,
Schumpeter), douze entrées en `verifications_en_attente` dont quatre
critiques, et deux sections de travail annexées au corps (« Balayage du
Livre 6 » et « Révision du 2026-09-07 »), que le lecteur et l'auditeur lisent
comme du texte.

**Décisions de l'auteur (2026-09-11).**
1. « 92 % de monnaie commerciale » : retirer, sauf périmètre, date, pays et
   agrégat précis ; « la majorité de la monnaie » suffit.
2. « Quatre-vingt-dix pour cent des manuels » : retirer, sans recherche.
3. Withers et Schumpeter : jalons historiques seulement, après vérification
   de l'édition, de la page et du passage exact ; ils ne portent pas la
   démonstration. La vérité du mécanisme ne dépend pas de l'antériorité de la
   formule « loans make deposits ».
4. Banque d'Angleterre 2014 : source principale de la description
   contemporaine, chaque proposition vérifiée séparément ; ne pas transformer
   « les prêts créent les dépôts » en « tous les dépôts proviennent
   exclusivement des prêts ».
5. Préciser que les banques créent aussi des dépôts en achetant certains
   actifs, en cohérence avec L1.C08.
6. Conséquence pour NEMO limitée à : « Le crédit bancaire sélectionne les
   emprunteurs capables de présenter une perspective de remboursement et,
   selon les cas, des garanties. Cela ne signifie pas que chaque crédit
   finance une activité productive rentable, ni que toute création bancaire
   impose à elle seule la croissance. »
7. Déplacer les deux sections de travail vers ce dossier, conservées comme
   trace (§ 8).

**Corrections de l'auteur à la validation de l'architecture (2026-09-11),
intégrées avant la réécriture.**
1. Titre et périmètre : « Comment les banques commerciales créent la monnaie
   de dépôt » ; le chapitre n'explique ni toutes les formes de monnaie ni
   toute l'activité des banques centrales.
2. Bilan bancaire : tout dépôt est un passif de la banque envers son
   détenteur ; la contrepartie à l'actif est la créance sur l'emprunteur lors
   d'un crédit, l'actif acquis lors d'un achat à un agent non bancaire ; ne
   jamais écrire que les dépôts nés d'achats d'actifs seraient sans
   contrepartie ; distinguer la dette de la banque envers son client (le
   dépôt) et la dette de l'emprunteur envers la banque (créée par le seul
   crédit) ; abandonner « toute monnaie a pour contrepartie une dette privée ».
3. « Ex nihilo » : défini par la seule absence de transfert du dépôt
   préexistant d'un épargnant au moment de l'écriture ; ni création sans
   contrepartie comptable, ni capacité illimitée de prêter ; la création ne
   dispense ni du règlement interbancaire, ni de la liquidité, ni des
   contraintes de capital, de risque et de réglementation.
4. Destruction : trois énoncés séparés (remboursement du principal au moyen
   d'un dépôt ; revente d'un actif à un agent non bancaire ; solde agrégé
   déterminé par les refinancements, nouveaux crédits et autres opérations
   simultanées) ; « rembourser toutes les dettes ramènerait la masse
   monétaire à zéro » reste retiré.
5. Portée géographique : le cadre et le chiffre de 97 % sont britanniques et
   datés ; formulation retenue : « Dans les économies contemporaines où les
   dépôts bancaires constituent l'essentiel de la monnaie au sens large,
   comme au Royaume-Uni étudié par la Banque d'Angleterre, les banques
   commerciales créent de la monnaie de dépôt notamment lorsqu'elles
   accordent des crédits ou achètent certains actifs à des agents non
   bancaires » ; le chiffre de 97 % n'est pas repris dans le corps.
6. Manuels : toute affirmation sur les manuels actuels est retirée, même
   comme hypothèse ; le chapitre dit seulement que l'article de 2014 présente
   comme une idée reçue la représentation où les banques prêtent des dépôts
   collectés et multiplient la monnaie centrale.
7. Portée politique : « le levier monétaire principal est hors du champ de
   la décision publique » et « aucun mandat démocratique explicite » sont
   retirés ; l'allocation résulte de décisions bancaires décentralisées dans
   un cadre juridique, prudentiel et monétaire public, que des instruments
   publics peuvent influencer (Deyris, en L1.C08) ; la question de la
   légitimité démocratique est posée comme question normative renvoyée aux
   chapitres de gouvernance et d'orientation du crédit.
8. Schumpeter : aucune citation à page seulement déduite ; la phrase
   centrale n'est pas reproduite ; seules les attributions des pages 1111 et
   1115, données par l'index, sont conservées ; Newcomb, Fisher et Macleod
   restent rapportés par Schumpeter.
9. Structure : sept mouvements substantiels, puis un encadré historique et
   une conclusion sur la portée et les limites.
10. Conséquence pour NEMO IMS : la phrase de la décision 6, complétée d'une
    seule phrase : « NEMO IMS cherche à ouvrir un canal complémentaire pour
    des activités essentielles qui échouent à cette sélection, sans prétendre
    que tout refus de crédit constitue une défaillance ni que la monnaie
    puisse remplacer les ressources réelles. »
11. Séquence : réécriture ; sections de travail retirées du corps ; matrice
    mise à jour sur le texte réécrit ; correction séparée des pages 16
    devenues 17 dans C08 ; aucun commit avant présentation du nouveau C07 et
    de son diff ; audit contradictoire du texte réécrit ; `verifie` distinct
    de `citable`.

## 2. Sources ouvertes

| Réf | Édition effectivement ouverte | Acquisition et empreinte | Périmètre lu | Compétence |
|---|---|---|---|---|
| S1 | M. McLeay, A. Radia, R. Thomas, « Money creation in the modern economy », *Bank of England Quarterly Bulletin*, 2014 Q1, p. 14-27 (PDF de l'article) | PDF acquis le 2026-09-07 (`BoE-Money-creation-2014.pdf`, `cfc4a626…992b62b2`), texte extrait `BoE-2014.txt` (`43c2823c…831fbabf`), lu pour L1.C08 les 2026-09-10 et 11, relu pour L1.C07 le 2026-09-11 ; l'entrée actuelle de C07 pointe la page HTML, l'entrée à venir pointera le PDF | p. 14-18 (points clés, idées reçues, création par le prêt, autres voies de création et de destruction, limites) | écritures et mécanismes de la monnaie bancaire, Royaume-Uni « en temps normal » ; rien au-delà |
| S2 | H. Withers, *The Meaning of Money*, London, Smith, Elder & Co., **1909**, première édition (exemplaire de la Cornell University Library, cote HG221 .W82 1909) | archive.org `cu31924030178663`, OCR `withers-1909-cu31924030178663_djvu.txt` (`ff27a048…70ec6955`), téléchargé le 2026-09-11 | chapitre V « The Manufacture of Money » (p. 57 et suiv.), p. 63-65 ; chapitre sur les crédits de la Banque d'Angleterre, p. 203 | témoignage d'un journaliste financier sur la pratique bancaire anglaise de 1909 ; jalon historique, non fondement |
| S3 | J. A. Schumpeter, *History of Economic Analysis*, éd. Elizabeth Boody Schumpeter, London, George Allen & Unwin, 1954 (exemplaire de la seconde impression, 1955, numérisé par la Digital Library of India) ; texte de contrôle : réimpression Routledge, Taylor & Francis e-Library 2006, « First published in Great Britain in 1954 by Allen & Unwin » | archive.org `dli.ernet.505700`, OCR `schumpeter-1954-dli-505700_djvu.txt` (`b89795d1…a67ff63b`, OCR imparfait, pagination de 1954) ; archive.org `joseph-a.-schumpeter-history-of-economic-analysis-routledge-1987`, texte `schumpeter-1954-routledge1987_djvu.txt` (`b3beed9f…54c15fc7`, texte propre, pagination propre à l'e-book), téléchargés le 2026-09-11 | Part IV, chapitre 8 « Money, Credit, and Cycles », section sur la théorie bancaire et la création de crédit ; index (Withers, Hartley, 1111, 1115) | histoire de l'analyse économique ; attributions et antériorités |

| S4 | Deutsche Bundesbank, « The role of banks, non-banks and the central bank in the money creation process », *Monthly Report*, avril 2017, p. 13-33, version anglaise | PDF téléchargé le 2026-09-11 depuis bundesbank.de (`bundesbank-2017-04-money-creation.pdf`, `68902f22…bc91702`), texte extrait du PDF chiffré et vérifié contre les passages paginés ; pagination imprimée = page PDF + 12 | p. 13-18 (résumé, réserves, exemples 1a, 1b, 2), 21 (remboursement), 27-28 (exemple 3a, achat par la banque centrale) | écritures et contraintes de la création de monnaie scripturale dans la zone euro, cadre de l'Eurosystème |
| S5 | J. Deyris, thèse de 2023, même fichier que S21 de L1.C08 | fourni par l'auteur, `ca17b188…78f355c7` ; téléchargé le 2026-09-11 depuis le dépôt institutionnel de l'Université Paris Nanterre (thèse 2023PA100055), empreinte identique ; notice publique de la Chaire Économie du Climat (titre et soutenance en 2023) ; pagination imprimée = page PDF − 2 | p. 21, 53, 59, 63, 68 (instruments publics : information, incitation, quantité ; cadres de collatéral et achats d'actifs ; taux préférentiels ; encadrement du crédit) | instruments publics susceptibles d'orienter l'allocation du crédit ; aucune mesure d'effet |

Newcomb (1885), Fisher (1911) et Macleod sont **rapportés par Schumpeter**,
non ouverts ; ils n'entrent pas comme sources. S4 et S5 ont été ajoutées le
2026-09-11 en réponse à l'audit contradictoire de l'auteur (§ 10).

## 3. Les cinq propositions de la Banque d'Angleterre, vérifiées séparément

| Proposition | Passage exact | Page |
|---|---|---|
| L'octroi d'un prêt crée simultanément une créance bancaire et un dépôt | « Whenever a bank makes a loan, it simultaneously creates a matching deposit in the borrower's bank account, thereby creating new money » ; « the act of lending creates deposits — the reverse of the sequence typically described in textbooks » | p. 14 ; p. 15 |
| Le remboursement du principal détruit la monnaie correspondante | « Just as taking out a new loan creates money, the repayment of bank loans destroys money » | p. 16 |
| Les banques peuvent aussi créer des dépôts en achetant certains actifs | « Deposit creation or destruction will also occur any time the banking sector (including the central bank) buys or sells existing assets from or to consumers, or, more often, from companies or the government » ; « Banks buying and selling government bonds is one particularly important way in which the purchase or sale of existing assets by banks creates and destroys money » | p. 17 |
| Les réserves ne sont pas un stock prêté préalablement aux clients | « banks do not act simply as intermediaries, lending out deposits that savers place with them, and nor do they 'multiply up' central bank money to create new loans and deposits » ; « Bank deposits are simply a record of how much the bank itself owes its customers. So they are a liability of the bank, not an asset that could be lent out. A related misconception is that banks can lend out their reserves. Reserves can only be lent between banks, since consumers do not have access to reserves accounts at the Bank of England » ; « In no way does the aggregate quantity of reserves directly constrain the amount of bank lending or deposit creation » ; réserves demandées « to meet withdrawals by the public, make payments to other banks, or meet regulatory liquidity requirements » | p. 14 ; p. 16 ; p. 16 ; p. 15 |
| La création reste contrainte : coût du crédit, demande solvable, risques, capital, liquidité, réglementation, règlement interbancaire | « Although commercial banks create money through their lending behaviour, they cannot in practice do so without limit. In particular, the price of loans — that is, the interest rate (plus any fees) charged by banks — determines the amount that households and companies will want to borrow » ; « there are three main sets of constraints that restrict the amount of money that banks can create » : « Market forces constrain lending because individual banks have to be able to lend profitably in a competitive market » ; « Lending is also constrained because banks have to take steps to mitigate the risks associated with making additional loans » ; « Regulatory policy acts as a constraint on banks' activities in order to mitigate a build-up of risks that could pose a threat to the stability of the financial system » ; « Money creation is also constrained by the behaviour of the money holders — households and businesses » ; « The ultimate constraint on money creation is monetary policy » ; capital : « Banks manage their liabilities to ensure that they have at least some capital and longer-term debt liabilities to mitigate certain risks and meet regulatory requirements » ; banque individuelle contre système : « But that does not mean that any given individual bank can freely lend and create money without limit » | p. 17 ; p. 17 ; p. 17 ; p. 18 |

La première citation, issue de l'encadré des points clés, est coupée en deux
colonnes par l'extraction du PDF ; elle est vérifiée par fragments, comme pour
L1.C08. Deux constats annexes. « Majorité » est le mot de la source : « the majority of
money in the modern economy is created by commercial banks making loans »
(p. 14) ; le seul chiffre est britannique et daté : « Of the two types of broad
money, bank deposits make up the vast majority — 97% of the amount currently in
circulation » (p. 15), part des dépôts bancaires dans la monnaie au sens large
au Royaume-Uni au moment de l'article. Et l'entrée S1 de L1.C08 situe p. 16 les
deux citations sur les achats de titres publics, qui sont p. 17 : correction à
porter dans un prochain commit correctif de C08.

## 4. Withers et Schumpeter : ce que les textes établissent

**Withers, 1909.** La date de première édition est 1909, non 1901 : page de
titre « London: Smith, Elder & Co. », cote 1909 ; Schumpeter cite la seconde
édition, elle aussi de 1909. Le chapitre V s'intitule « The Manufacture of
Money ». La formule est à la page 63 : « The greater part of the banks'
deposits is thus seen to consist, not of cash paid in, but of credits
borrowed. For every loan makes a deposit » ; l'exemple de l'avance pour
l'achat d'une automobile conclut p. 64 « and the loan has clearly created a
deposit » ; « LOANS MAKE DEPOSITS » est le titre courant des pages 65 et 67.
Withers note déjà, p. 203, que l'achat de titres crée un dépôt : « When the
latter make an advance against any kind of security or buy stock for
investment, they create a deposit and give a right to draw a cheque », et que
« the loans of one bank create the deposits of another, except when the loans
are raised with one bank for repaying another ». Le passage p. 65 décrit le
règlement entre banques par leurs comptes à la Banque d'Angleterre.

**Schumpeter, 1954.** Trois passages. P. 1111 (index) : « Our other instance
is the not less brilliant book by Hartley Withers, The Meaning of Money (2nd
ed., 1909), whose chief merit consists, as we shall presently see, in having
boldly spoken of the 'manufacture' of money by banks. But this should not have
surprised anyone. Yet it was considered as a novel and somewhat heretical
doctrine. » Entre les deux mentions de l'index, donc p. 1112-1114 de
l'édition de 1954, la formulation propre de Schumpeter : « It is much more
realistic to say that the banks 'create credit,' that is, that they create
deposits in their act of lending, than to say that they lend the deposits that
have been entrusted to them » — **phrase non reproduite dans le chapitre**,
par décision de l'auteur, sa page n'étant que déduite. P. 1115 (index) : « Newcomb in 1885 gave an
elementary description of the process by which deposits are created through
lending. Toward the end of the period (1911) Fisher did likewise. He also
emphasized the obvious truth that deposits and banknotes are fundamentally the
same thing. And Hartley Withers espoused the notion that bankers were not
middlemen but 'manufacturers' of money » ; et « the first—though not wholly
successful—attempt at working out a systematic theory that fits the facts of
bank credit adequately, which was made by Macleod ». La page de la phrase
centrale n'a pas pu être lue sur l'OCR de 1954 ; elle est déduite de la
position et reste à confirmer sur un exemplaire imprimé.

**Conséquences pour le § 3 actuel de C07.**
- « dès le début du XXe siècle » : exact (1909) ; « 1901 » : faux, à corriger.
- « La paternité de la formule appartient à Withers, non à Joseph
  Schumpeter » : Schumpeter n'a jamais revendiqué la formule ; il attribue à
  Withers le mot « manufacture », à Newcomb (1885) et Fisher (1911) la
  description élémentaire des dépôts créés par le prêt, à Macleod la première
  théorie systématique. La formule anglaise « loans make deposits » est bien
  celle de Withers (titre courant, 1909) ; l'idée ne l'est pas.
- « attribuée sur la foi de son Histoire de l'analyse économique… longtemps
  erronée dans la littérature francophone » : aucune source ; à retirer.
- « en s'appuyant explicitement sur les travaux antérieurs — dont ceux de
  Withers » : exact pour Withers (p. 1111, 1115), et Schumpeter nomme aussi
  des antérieurs du XIXe siècle, ce qui répond à la vérification en attente
  sur « aucun antérieur ».
- Ni l'un ni l'autre ne porte la description contemporaine : jalons.

## 5. Matrice affirmation-source du chapitre actuel

Qualification : **F** fait sourcé (passage lu) ; **J** jalon historique lu ;
**D** déduction ; **H** hypothèse ; **N** choix normatif ; **—** sans appui.

| § | Affirmation actuelle | Qual. | Source, périmètre | Décision proposée |
|---|---|---|---|---|
| intro | L'essentiel de la monnaie n'est pas émis par la Banque centrale mais créé par les banques commerciales à l'occasion de chaque crédit, par double écriture | F | S1 p. 14-15 (« majority ») | conserver, en écrivant « la majorité » et en ajoutant les achats d'actifs |
| intro | Description formulée dès le début du XXe siècle, reconnue publiquement par la Banque d'Angleterre en 2014 | J + F | S2 1909 ; S1 | conserver (1909) |
| intro | Ces propositions ne sont pas discutées dans la littérature spécialisée, mais le restent dans le débat public et une part des manuels | — | aucune | réduire à une hypothèse déclarée, ou retirer |
| § 1 | Modèle du multiplicateur tel qu'enseigné ; « enseignée du lycée aux écoles de commerce » | — | S1 p. 15 décrit l'idée reçue (« the reverse of the sequence typically described in textbooks ») | conserver la description de l'idée reçue en l'adossant à S1 ; retirer « du lycée aux écoles de commerce » |
| § 1 | Le multiplicateur inverse l'ordre chronologique ; dispositif pédagogique, non description | F | S1 p. 14-16 | conserver |
| § 2 | Double écriture, aucune monnaie préexistante mobilisée ; ex nihilo au sens comptable | F | S1 p. 14-16 | conserver |
| § 2 | Le remboursement efface la monnaie créée | F | S1 p. 16 | conserver |
| § 2 | « la monnaie moderne est faite de dettes. Elle naît par le crédit. Elle disparaît par le remboursement » | trop large | S1 p. 17 : achats d'actifs ; monnaie centrale | reformuler : la monnaie de dépôt naît d'un crédit ou d'un achat d'actif par une banque et s'éteint à leur dénouement |
| § 3 | Withers formule « loans make deposits » « dès le début du XXe siècle » ; « 1901 » | J | S2 p. 63-65 | conserver comme jalon ; 1909 |
| § 3 | Paternité de la formule à Withers, non à Schumpeter ; confusion francophone | — | S3 p. 1111, 1115 dit autre chose | retirer ; reformuler d'après Schumpeter (§ 4) |
| § 3 | École de la monnaie endogène : Kaldor, Moore, Lavoie, post-keynésiens ; « raffiné et étayé empiriquement » | — | aucune source ; L1.C23 cartographie la littérature | réduire à une phrase renvoyant à L1.C23, sans « étayé empiriquement » |
| § 3 | « restée controversée dans le débat académique jusqu'à… 2014 » | — | aucune | retirer ou réduire à une hypothèse |
| § 4 | Publication de mars 2014, trois économistes, écarte le multiplicateur | F | S1 p. 14-16 | conserver |
| § 4 | Portée institutionnelle ; « l'argument d'autorité… perd son fondement » | D | — | conserver comme déduction déclarée |
| § 4 | « Onze années après » ; « une part importante des manuels » ; « majoritairement » | — | aucun relevé | reformuler : « plus d'une décennie après » ; « une part des manuels », hypothèse déclarée |
| § 4 | Trois hypothèses (inertie, charge politique, coût cognitif) | H | énoncées comme telles | conserver, `::hypothese::` |
| § 5, un | « À chaque unité monétaire en circulation correspond… une créance bancaire d'égal montant » ; « Le remboursement de l'ensemble des dettes contracterait la masse monétaire à zéro » | trop large | S1 p. 17 ; L1.C08 § 1 (toutes les formes de monnaie n'ont pas pour contrepartie une dette privée) | reformuler : symétrie création-destruction pour la monnaie née du crédit ; retirer la contraction « à zéro » |
| § 5, deux | L'orientation des crédits décide de l'orientation de l'économie ; critère : solvabilité anticipée ; lien avec L1.C01 | F + D | S1 p. 15 (« Banks first decide how much to lend depending on the profitable lending opportunities available to them »), p. 17-18 (contraintes) | réduire à la phrase de l'auteur (§ 1, décision 6) |
| § 5, trois | « 92 % » ; pouvoir monétaire privé sans mandat démocratique explicite | — / H | S1 p. 14 (« majority »), p. 15 (97 %, Royaume-Uni) | « la majorité » (ou le chiffre britannique daté) ; le mandat comme `::hypothese::` |
| § 5, quatre | La politique monétaire ne décide pas de la composition sectorielle du crédit | D + F | S1 p. 17-18 (politique monétaire, prix du crédit) | conserver comme déduction |
| § 5 | « le levier monétaire principal est aujourd'hui hors du champ de la décision publique » | H | — | conserver, `::hypothese::`, ton réduit |
| annexes | Balayage du Livre 6 ; Révision du 2026-09-07 | trace | L6.C06, L6.C07 ; S1 | déplacer ici (§ 8) |

## 6. Structure proposée

Le chapitre distingue sept objets, dans cet ordre, chacun avec sa source et
sa qualification, puis place séparément un encadré historique et une
conclusion sur la portée et les limites (correction 9 de l'auteur) :

1. **L'écriture de création : prêt et dépôt** — S1 p. 14-15 ; Withers p. 63-64
   comme jalon.
2. **Le remboursement et la destruction monétaire** — S1 p. 16.
3. **Les achats d'actifs créateurs de dépôts** — S1 p. 17 ; Withers p. 203 ;
   cohérence avec L1.C08 § 1 : toutes les formes de monnaie n'ont pas pour
   contrepartie une dette privée portant intérêt.
4. **La banque individuelle et le système bancaire** — S1 p. 18 : l'agrégat
   crée des dépôts par le prêt, une banque isolée ne prête pas sans limite et
   peut perdre les dépôts qu'elle crée.
5. **Les réserves et le règlement interbancaire** — S1 p. 15-16 : les réserves
   ne sont ni prêtées aux clients ni multipliées ; elles servent aux retraits,
   aux paiements entre banques et aux exigences de liquidité, et sont fournies
   à la demande en temps normal ; Withers p. 65 sur la compensation à la
   Banque d'Angleterre.
6. **Les contraintes effectives de l'octroi** (« contraintes réelles » désigne ailleurs dans le corpus les ressources et les limites physiques) — S1 p. 17-18 : prix du crédit et
   demande, rentabilité en concurrence, risques, capital et passifs longs,
   réglementation, comportement des détenteurs de monnaie, politique
   monétaire comme contrainte ultime.
7. **La sélection économique produite par ces contraintes** — S1 p. 15, 17-18 ;
   concept `solvabilite_anticipee` ; conséquence pour NEMO limitée à la phrase
   de l'auteur : « Le crédit bancaire sélectionne les emprunteurs capables de
   présenter une perspective de remboursement et, selon les cas, des
   garanties. Cela ne signifie pas que chaque crédit finance une activité
   productive rentable, ni que toute création bancaire impose à elle seule la
   croissance. »
Hors des sept mouvements :
- **Encadré historique** (§ 8 du chapitre) — Withers 1909, Schumpeter 1954,
  Newcomb, Fisher et Macleod rapportés par Schumpeter ; deux paragraphes.
- **Portée et limites** (§ 9 du chapitre) — une source monétaire pour le
  mécanisme, deux jalons pour l'histoire ; cadre britannique de la source ;
  ce que le chapitre n'établit pas ; deux conditions de réfutation.

### Matrice affirmation-source sur le texte réécrit (2026-09-11)

| § | Affirmation du texte réécrit | Statut | Source, page |
|---|---|---|---|
| 1 | Un crédit crée simultanément une créance à l'actif et un dépôt au passif ; prêter crée un dépôt | F | S1 p. 14, 15 |
| 1 | L'article de 2014 présente comme idée reçue le prêt de dépôts collectés et la multiplication de la monnaie centrale | F | S1 p. 14, 15 |
| 1 | « Ex nihilo » = absence de transfert d'un dépôt préexistant au moment de l'écriture ; ne dispense d'aucune contrainte | N (définition du corpus, formulation de l'auteur) | — |
| 1 | Deux sens de « dette » : dépôt (dette de la banque), créance (dette de l'emprunteur) | D | S1 p. 14-16 |
| 2 | Le remboursement du principal au moyen d'un dépôt détruit la monnaie de dépôt | F | S1 p. 16 |
| 2 | La revente d'un actif à un agent non bancaire peut détruire un dépôt | F | S1 p. 17 |
| 2 | Le solde agrégé dépend des refinancements, nouveaux crédits et autres opérations ; pas de règle générale | H + F | S1 p. 17 (détenteurs remboursant) |
| 3 | Les banques créent des dépôts en achetant des actifs à des agents non bancaires ; contrepartie = l'actif acquis ; aucune dette d'emprunteur | F + D | S1 p. 17 |
| 3 | « Toute monnaie a pour contrepartie une dette privée » est trop général | D | S1 p. 17 ; L1.C08 § 1 |
| 4 | L'agrégat crée des dépôts par le prêt, une banque isolée ne prête pas sans limite, elle peut perdre les dépôts créés | F | S1 p. 18 |
| 5 | Réserves pour retraits, paiements interbancaires, liquidité réglementaire, fournies à la demande ; non prêtées aux clients ; quantité agrégée sans contrainte directe | F | S1 p. 15, 16 |
| 6 | Prix du crédit et demande ; rentabilité, risques, réglementation, capital ; détenteurs ; politique monétaire | F | S1 p. 17 |
| 7 | Les banques déterminent leurs prêts selon les occasions rentables et limitent les risques | F | S1 p. 15, 17 |
| 7 | « Solvabilité anticipée » : évaluation par le prêteur des flux de remboursement et, selon les cas, des garanties | N (définition du corpus, non attribuée à S1) | vocabulaire |
| 7 | Allocation par décisions décentralisées dans un cadre public ; instruments publics pouvant l'influencer ; question normative renvoyée | H (formulation de l'auteur) | L1.C08 (Deyris), L2.C06, L2.C13 |
| 7 | Conséquence limitée pour NEMO IMS, phrase de l'auteur plus une phrase | N | L1.C15, L1.C08 |
| 8 | Withers 1909 : formule p. 63, exemple p. 64, titre courant p. 65 ; achats de titres p. 203 | J | S2 |
| 8 | Schumpeter 1954 : Withers et la « manufacture » p. 1111 ; Newcomb, Fisher, Macleod p. 1115 | J | S3 (pages de l'index) |
| 9 | Portée limitée au cadre de la source ; ce qui n'est pas établi ; conditions de réfutation | D | — |

En-tête proposé : S1 `ouverte` sur le PDF (URL du PDF, date 2026-09-11,
passages p. 14-18) ; S2 `ouverte` (édition 1909, passages p. 63-65, 203) ; S3
`ouverte` (édition 1954, passages p. 1111, 1112-1114, 1115, texte de contrôle
Routledge) ; `verifications_en_attente` réduite à ce qui reste factuel ;
renvois complétés par L1.C08 et L1.C23 ; concepts inchangés sauf vérification
de `neutralite_monetaire` et `monnaie_comme_registre` dans le vocabulaire.

## 7. Retraits et reformulations

**Retraits.**
- « environ 92 % de la monnaie en circulation en Europe en 2024 » : aucun
  périmètre, date, pays ni agrégat ; remplacé par « la majorité de la monnaie
  moderne est créée par les banques commerciales » (S1 p. 14). Option précise
  si l'auteur la veut : « 97 % de la monnaie au sens large au Royaume-Uni au
  moment de l'article » (S1 p. 15), part des dépôts bancaires, non des seuls
  dépôts nés de prêts.
- « quatre-vingt-dix pour cent des manuels » : retiré, sans recherche.
- « 1901 » : 1909.
- « La paternité de la formule appartient à Withers, non à Joseph
  Schumpeter… longtemps erronée dans la littérature francophone » : retiré ;
  remplacé par ce que Schumpeter écrit (§ 4).
- « restée controversée dans le débat académique jusqu'à ce que… 2014 » et
  « Ces deux propositions ne sont pas discutées dans la littérature
  contemporaine spécialisée » : retirés ou réduits à une hypothèse déclarée.
- « raffiné et étayé empiriquement » pour l'école de la monnaie endogène :
  retiré ; les noms sont renvoyés à L1.C23.
- « Le remboursement de l'ensemble des dettes contracterait la masse
  monétaire à zéro » : retiré.
- Les deux sections annexées : déplacées ici (§ 8).

**Reformulations.**
- « la monnaie moderne est faite de dettes… » → la monnaie de dépôt naît d'un
  crédit ou d'un achat d'actif par une banque et s'éteint à leur dénouement ;
  la monnaie centrale n'en relève pas.
- « À chaque unité monétaire… une créance bancaire d'égal montant » → la
  symétrie création-destruction vaut pour la monnaie née du crédit ; les
  dépôts nés d'achats d'actifs et la monnaie centrale n'ont pas cette
  contrepartie (cohérence avec L1.C08 § 1).
- Conséquence deux → la phrase de l'auteur (§ 1, décision 6), sans plus.
- « Onze années après » → « plus d'une décennie après » ; « une part
  importante des manuels », « majoritairement » → « une part des manuels »,
  hypothèse déclarée.
- « aucun mandat démocratique explicite » → `::hypothese::`.
- § 1 : l'idée reçue est décrite d'après S1 p. 15 (« lending out the deposits
  that savers place with them ») plutôt que d'après « ce qui est enseigné ».

## 8. Trace des deux sections de travail à retirer du corps

Reproduites telles quelles depuis le chapitre au 2026-09-11, pour la passe 2.

### 8.1 Balayage du Livre 6 — 2026-09-07

::etat:: **Annotation portée à la clôture de la passe 1 du Livre 6.** Ce que ce chapitre reçoit n'a pas été instruit ici et **ne modifie pas ce qui précède** : il est versé pour que la passe 2 le trouve.

::hypothese:: **Le créancier ne décide pas seulement de ce qui se finance : il décide de ce qui peut être PROTÉGÉ** [L6.C07]. L'obligation réelle environnementale du droit français — article L. 132-3 du code de l'environnement, charge écologique attachée au bien jusqu'à quatre-vingt-dix-neuf ans — **est subordonnée en pratique à l'accord du créancier hypothécaire, qui n'a pas intérêt à consentir puisque la charge déprécie l'assiette de sa sûreté.**

::hypothese:: **Le mécanisme est propre et sans mauvaise foi** : la sûreté est un droit acquis, la dépréciation est réelle, le refus est rationnel. **La solvabilité anticipée qu'établit ce chapitre a donc une portée que ce chapitre n'énonce pas** — elle filtre non seulement les projets, mais les engagements de conservation.

::etat:: **RÉSERVE PORTÉE PAR LE REGISTRE DU LIVRE 6** : ce verrou est une **pratique notariale, non une règle légale explicite**, et aucune décision judiciaire ne l'a tranché.

::hypothese:: **ET UNE SORTIE EXISTE, versée en L6.C06 après lecture de l'arrêt italien n° 119 de 2023.** Les usages civiques italiens ne se heurtent pas au créancier : leur opposabilité « opera a prescindere dal rispetto di oneri pubblicitari » et survit à la vente forcée. **La différence est de nature : une charge inscrite vient après le créancier et lui demande permission ; une charge inhérente au fonds était là avant et ne la demande pas.** **Le corpus ne peut pas obtenir par convention ce que l'antériorité donne.**

### 8.2 Révision du 2026-09-07 — source de banque centrale

::etat:: **Ce chapitre est confirmé par une source de banque centrale que le corpus ne détenait pas** : McLeay, Radia et Thomas, « **Money creation in the modern economy** », *Bank of England Quarterly Bulletin*, 2014 Q1. « **Whenever a bank makes a loan, it simultaneously creates a matching deposit in the borrower's bank account, thereby creating new money.** » Et : « banks do not act simply as intermediaries, lending out deposits that savers place with them, **nor do they 'multiply up' central bank money** ».

::etat:: **ET UNE PHRASE VISE DIRECTEMENT LA PROMESSE P23, dont le corpus tenait la réponse pour probable** : « **Just as taking out a new loan creates money, the repayment of bank loans DESTROYS money.** »

::hypothese:: **Le corpus enregistre l'asymétrie que cela révèle, et elle n'est pas à son avantage.** Dans le régime de crédit, **le remboursement détruit** — la symétrie création/destruction y est exacte. Or l'arbitrage du 2026-09-05 pose que le reflux du dispositif « **n'est PAS une annulation** » et que la monnaie « **quitte la circulation sans être détruite** ».

::hypothese:: **Les deux régimes ne sont donc pas symétriques, et le dispositif est le moins symétrique des deux.** Le régime qu'il critique **ferme son circuit** ; le sien **déplace un encours vers l'actif d'une institution.** **Ce n'est pas une objection nouvelle — c'est P23 et P26 — mais le corpus disposait de l'énoncé sans en tenir la source, et la source est une banque centrale.**

Ce que la trace 8.2 apporte au chapitre réécrit : la citation « nor do they
'multiply up' central bank money » y est tronquée ; le texte complet est « and
nor do they 'multiply up' central bank money to create new loans and deposits »
(S1 p. 14). L'asymétrie entre remboursement et reflux relève de L1.C21 et des
promesses P23 et P26, non de C07.

## 9. Séquence

1. Validation de cette architecture par l'auteur : **acquise le 2026-09-11,
   sous les onze corrections du § 1.**
2. Réécriture de C07 sur la structure du § 6, avec les retraits et
   reformulations du § 7 ; en-tête requalifié ; sections de travail retirées :
   **faite le 2026-09-11, soumise avec son diff, puis corrigée sur cinq
   points de l'auteur** : le dépôt n'est pas qualifié d'exigible à vue ; le
   remboursement est décrit à l'échelle du système, avec le cas de deux
   banques et le transfert de réserves ; la banque prêteuse règle en monnaie
   centrale le dépôt transféré, sans « le plus souvent » ; le § 6 s'intitule
   « contraintes effectives » ; le § 7 sépare le fait établi par la Banque
   d'Angleterre et la définition du corpus de la solvabilité anticipée. Statut
   `audit_contradictoire`, sans passage à `verifie`. Les deux citations de la
   Banque d'Angleterre situées page 16 dans L1.C08 sont corrigées en page 17,
   dans le chapitre, son audit factuel et son architecture, dans un commit
   correctif séparé.
3. Audit contradictoire par un modèle tiers sur le texte réécrit (le dossier
   déjà transmis porte le brouillon ; il reste utilisable pour une première
   passe, mais la méthode audite le texte réécrit).
4. Synthèse, arbitrage, fiches s'il reste des affirmations sans appui, puis
   `verifie`, enregistrement de l'état, commits séparés, aucun push.

## 10. Audit contradictoire du 11 septembre 2026 : synthèse et traitement

Audit contradictoire conduit le 11 septembre 2026 par Codex, modèle tiers par
rapport au rédacteur Claude, à la demande de l'auteur, sur le texte réécrit et
les sources locales ; objections transmises par l'auteur et traitements relus
par Codex. L'auteur reste celui qui arbitre ; il n'a pas lui-même produit le
rapport. Huit objections ; toutes traitées le jour même, sans commit, puis
validées par l'auteur.

| N | Objection | Examen contre les textes | Traitement | Statut proposé |
|---|---|---|---|---|
| 1 | L'achat d'actifs par une banque commerciale et par une banque centrale est confondu (§ 3) | Fondée : le passage de S1 englobe « including the central bank ». S1 p. 24 décrit l'achat à un fonds de pension par l'intermédiaire de sa banque (dépôt crédité par la banque, réserves créditées par la Banque d'Angleterre) ; S4 p. 27-28 décrit la même opération dans l'Eurosystème (exemple 3a : titres chez la banque centrale, réserves à l'actif de la banque du vendeur, dépôt à son passif) | § 3 scindé en deux paragraphes ; les trois positions comptables sont écrites et sourcées | corrigée |
| 2 | « il n'y a pas d'emprunteur » efface le cas d'un actif qui est une créance préexistante | Fondée | remplacé par « aucune nouvelle dette du vendeur envers la banque… mais l'actif acquis peut être lui-même une créance préexistante, un titre de dette publique ou privée déjà émis », avec S4 p. 18 | corrigée |
| 3 | Réserves « fournies à la demande » sans contrepartie ni cadre | Fondée : S1 p. 16 dit « in exchange for other assets on their balance sheets » | phrase complète citée ; « en échange d'autres actifs et selon le cadre opérationnel de la banque centrale » ; S4 p. 17 sur l'acquisition différée des réserves | corrigée |
| 4 | « sans qu'aucune de ces contraintes passe par un stock préalable » trop général | Fondée | remplacé par la phrase de l'auteur sur le stock équivalent de dépôts de clientèle | corrigée |
| 5 | Définition de la solvabilité anticipée trop étroite (« produire ») | Fondée | « pourra disposer des flux monétaires nécessaires au remboursement ou les obtenir » | corrigée |
| 6 | Généralisation géographique sur une seule source | Fondée ; l'auteur préfère une seconde source institutionnelle | S4 Bundesbank 2017 acquise et lue : chacune des sept propositions y trouve son passage pour la zone euro ; introduction, § 9 et résumé délimitent la portée aux deux cadres documentés et aux systèmes comparables, avec la diversité des cadres opérationnels dite explicitement | corrigée ; la limite reste écrite |
| 7 | Faits sous marqueur d'hypothèse au § 7 (instruments publics) | Fondée | paragraphe scindé : instruments en `::etat::` sourcés par S5 (Deyris p. 21, 53, 59, 63, 68), effet non mesuré dit tel ; question normative en `::hypothese::` | corrigée |
| 8 | Conditions de réfutation formulées sur une « source » | Fondée | reformulées sur un mécanisme démontré ou un contre-exemple documenté, phrase de l'auteur reprise | corrigée |

Points relevés par l'audit hors objections : aucune affirmation quantitative
non sourcée ne subsiste ; « la forme dominante » de L1.C08 est désormais
rapportée « dans les cadres documentés ici » ; la diversité des cadres
opérationnels est écrite au § 9. Statut du chapitre : `audit_contradictoire`
maintenu ; passage à `audit_factuel` puis `verifie` à la décision de l'auteur
après lecture du diff.

Empreintes complètes des fichiers cités :

```
68902f228b3767746cb9656f59e9dc66ddaa9cf0712bd89924a6f5627bc91702  bundesbank-2017-04-money-creation.pdf
ca17b1884ae59034df3dcb741ee40ef0972f88efa130506f91cc605078f355c7  deyris-these-2023.pdf
cfc4a6262631e7b5582a427aec1215c1568f240c45d54696bb9a2093992b62b2  BoE-Money-creation-2014.pdf
43c2823ccde52f804d3c5b15ebcf9aa661746ab03816d68336e9f8cb831fbabf  BoE-2014.txt
ff27a04846430eb2045431f7d26659012802287168e643f34a15ee5470ec6955  withers-1909-cu31924030178663_djvu.txt
b89795d193f36e22031755da6956c5bb89eed5d22f2144d8bea1b169a67ff63b  schumpeter-1954-dli-505700_djvu.txt
b3beed9fd1d43817f771854c4368f70fdd163a410335e4c8bf13e9dc54c15fc7  schumpeter-1954-routledge1987_djvu.txt
```
