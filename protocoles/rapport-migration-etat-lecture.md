# Rapport de conservation — migration etat_lecture

**Généré par `migrer.py` depuis le même relevé que le manifeste ; le manifeste fait foi.**

| champ | valeur |
|---|---|
| date de migration | 2026-09-10 |
| commit source | `60fa2fa2134a6048941c1baa7c47e4f2828eb36b` — le HEAD courant au moment de la migration, vérifié égal par le script ; le commit de migration n'est pas inscrit ici |
| Python, PyYAML | 3.14.5, 6.0.3 |
| chapitres | 335, dont 323 portant au moins une occurrence |
| occurrences historiques | 1161 — toutes `a_requalifier` |
| file A — orientation vers ouverte | 175 |
| file B — traces contradictoires | 10 |
| file C — orientation vers candidate | 126 |
| file D — sans orientation | 850 |
| bouclage | 175 + 10 + 126 + 850 = 1161 |

## Par chapitre

| chapitre | occurrences | A | B | C | D |
|---|---|---|---|---|---|
| L0.C01 | 1 | 0 | 0 | 0 | 1 |
| L1.C02 | 6 | 0 | 0 | 0 | 6 |
| L1.C03 | 7 | 0 | 0 | 0 | 7 |
| L1.C04 | 9 | 0 | 0 | 0 | 9 |
| L1.C05 | 2 | 0 | 0 | 0 | 2 |
| L1.C06 | 2 | 0 | 0 | 0 | 2 |
| L1.C07 | 3 | 0 | 0 | 0 | 3 |
| L1.C08 | 11 | 1 | 1 | 3 | 6 |
| L1.C09 | 19 | 0 | 0 | 13 | 6 |
| L1.C10 | 22 | 0 | 0 | 11 | 11 |
| L1.C11 | 9 | 0 | 0 | 4 | 5 |
| L1.C12 | 12 | 1 | 0 | 6 | 5 |
| L1.C13 | 16 | 0 | 0 | 8 | 8 |
| L1.C14 | 12 | 0 | 0 | 11 | 1 |
| L1.C15 | 15 | 0 | 0 | 10 | 5 |
| L1.C16 | 12 | 0 | 0 | 12 | 0 |
| L1.C17 | 14 | 0 | 0 | 7 | 7 |
| L1.C18 | 22 | 1 | 0 | 8 | 13 |
| L1.C19 | 9 | 0 | 0 | 3 | 6 |
| L1.C20 | 10 | 0 | 1 | 4 | 5 |
| L1.C21 | 15 | 0 | 3 | 6 | 6 |
| L1.C22 | 14 | 0 | 0 | 0 | 14 |
| L1.C23 | 19 | 0 | 0 | 0 | 19 |
| L1.C24 | 12 | 0 | 0 | 2 | 10 |
| L1.C25 | 12 | 0 | 0 | 3 | 9 |
| L1.C26 | 9 | 0 | 0 | 1 | 8 |
| L1.C27 | 9 | 2 | 0 | 0 | 7 |
| L1.C28 | 7 | 0 | 0 | 0 | 7 |
| L1.C29 | 6 | 1 | 0 | 0 | 5 |
| L1.C30 | 2 | 0 | 0 | 0 | 2 |
| L1.C31 | 2 | 0 | 0 | 0 | 2 |
| L10.C01 | 3 | 1 | 0 | 0 | 2 |
| L10.C02 | 3 | 1 | 0 | 0 | 2 |
| L10.C03 | 3 | 1 | 0 | 0 | 2 |
| L10.C04 | 3 | 1 | 0 | 0 | 2 |
| L10.C05 | 3 | 1 | 0 | 0 | 2 |
| L10.C06 | 3 | 0 | 0 | 0 | 3 |
| L10.C07 | 3 | 1 | 0 | 0 | 2 |
| L11.C01 | 6 | 0 | 0 | 0 | 6 |
| L11.C02 | 5 | 0 | 0 | 1 | 4 |
| L11.C03 | 8 | 0 | 0 | 1 | 7 |
| L11.C04 | 5 | 0 | 0 | 0 | 5 |
| L11.C05 | 7 | 0 | 0 | 1 | 6 |
| L11.C06 | 5 | 0 | 0 | 1 | 4 |
| L11.C07 | 5 | 1 | 0 | 0 | 4 |
| L11.C08 | 5 | 0 | 0 | 0 | 5 |
| L11.C09 | 5 | 0 | 0 | 1 | 4 |
| L11.C10 | 9 | 0 | 0 | 0 | 9 |
| L11.C11 | 6 | 0 | 0 | 0 | 6 |
| L11.C12 | 5 | 0 | 0 | 0 | 5 |
| L11.C13 | 6 | 0 | 0 | 1 | 5 |
| L11.C14 | 5 | 1 | 0 | 1 | 3 |
| L11.C15 | 5 | 0 | 0 | 1 | 4 |
| L11.C16 | 6 | 0 | 0 | 0 | 6 |
| L11.C17 | 4 | 0 | 0 | 0 | 4 |
| L11.C18 | 3 | 0 | 0 | 0 | 3 |
| L11.C19 | 3 | 0 | 0 | 0 | 3 |
| L11.C20 | 3 | 0 | 0 | 0 | 3 |
| L11.C21 | 4 | 0 | 0 | 0 | 4 |
| L11.C22 | 3 | 0 | 0 | 1 | 2 |
| L11.C23 | 4 | 0 | 0 | 0 | 4 |
| L11.C24 | 3 | 0 | 0 | 1 | 2 |
| L11.C25 | 3 | 0 | 0 | 0 | 3 |
| L11.C26 | 4 | 0 | 0 | 0 | 4 |
| L11.C27 | 5 | 0 | 0 | 0 | 5 |
| L11.C28 | 4 | 0 | 0 | 0 | 4 |
| L11.C29 | 5 | 1 | 0 | 0 | 4 |
| L11.C30 | 1 | 0 | 0 | 0 | 1 |
| L12.C01 | 3 | 2 | 0 | 0 | 1 |
| L12.C02 | 1 | 1 | 0 | 0 | 0 |
| L12.C03 | 2 | 1 | 0 | 0 | 1 |
| L13.C01 | 3 | 1 | 0 | 0 | 2 |
| L14.C01 | 2 | 0 | 0 | 0 | 2 |
| L15.C01 | 2 | 1 | 0 | 0 | 1 |
| L15.C02 | 1 | 1 | 0 | 0 | 0 |
| L15.C03 | 1 | 1 | 0 | 0 | 0 |
| L15.C04 | 1 | 1 | 0 | 0 | 0 |
| L16.C01 | 2 | 1 | 0 | 0 | 1 |
| L16.C02 | 1 | 0 | 0 | 0 | 1 |
| L16.C03 | 1 | 1 | 0 | 0 | 0 |
| L16.C04 | 1 | 1 | 0 | 0 | 0 |
| L16.C05 | 1 | 0 | 0 | 0 | 1 |
| L17.C01 | 2 | 1 | 0 | 0 | 1 |
| L17.C02 | 1 | 1 | 0 | 0 | 0 |
| L17.C03 | 1 | 1 | 0 | 0 | 0 |
| L17.C04 | 1 | 1 | 0 | 0 | 0 |
| L17.C05 | 1 | 1 | 0 | 0 | 0 |
| L17.C06 | 1 | 0 | 0 | 0 | 1 |
| L18.C01 | 4 | 4 | 0 | 0 | 0 |
| L18.C02 | 4 | 1 | 0 | 0 | 3 |
| L18.C03 | 3 | 1 | 0 | 0 | 2 |
| L18.C04 | 4 | 1 | 0 | 0 | 3 |
| L18.C05 | 3 | 1 | 0 | 0 | 2 |
| L18.C06 | 3 | 0 | 0 | 0 | 3 |
| L18.C07 | 4 | 0 | 0 | 0 | 4 |
| L18.C08 | 4 | 0 | 0 | 0 | 4 |
| L18.C09 | 3 | 1 | 0 | 0 | 2 |
| L18.C10 | 1 | 1 | 0 | 0 | 0 |
| L18.C11 | 1 | 1 | 0 | 0 | 0 |
| L18.C12 | 1 | 1 | 0 | 0 | 0 |
| L18.C13 | 1 | 1 | 0 | 0 | 0 |
| L18.C14 | 1 | 1 | 0 | 0 | 0 |
| L18.C15 | 1 | 1 | 0 | 0 | 0 |
| L18.C16 | 2 | 1 | 0 | 0 | 1 |
| L18.C17 | 1 | 1 | 0 | 0 | 0 |
| L18.C18 | 1 | 1 | 0 | 0 | 0 |
| L18.C19 | 1 | 1 | 0 | 0 | 0 |
| L18.C20 | 1 | 1 | 0 | 0 | 0 |
| L18.C21 | 1 | 1 | 0 | 0 | 0 |
| L18.C22 | 1 | 1 | 0 | 0 | 0 |
| L18.C23 | 2 | 1 | 0 | 0 | 1 |
| L18.C24 | 1 | 1 | 0 | 0 | 0 |
| L18.C25 | 1 | 1 | 0 | 0 | 0 |
| L18.C26 | 1 | 1 | 0 | 0 | 0 |
| L18.C27 | 1 | 1 | 0 | 0 | 0 |
| L18.C28 | 1 | 1 | 0 | 0 | 0 |
| L18.C29 | 1 | 1 | 0 | 0 | 0 |
| L18.C30 | 1 | 1 | 0 | 0 | 0 |
| L18.C31 | 1 | 1 | 0 | 0 | 0 |
| L19.C01 | 2 | 1 | 0 | 0 | 1 |
| L19.C02 | 1 | 1 | 0 | 0 | 0 |
| L19.C03 | 2 | 1 | 0 | 0 | 1 |
| L19.C04 | 2 | 1 | 0 | 0 | 1 |
| L19.C05 | 2 | 1 | 0 | 0 | 1 |
| L19.C06 | 1 | 1 | 0 | 0 | 0 |
| L19.C07 | 1 | 0 | 0 | 0 | 1 |
| L19.C08 | 1 | 1 | 0 | 0 | 0 |
| L19.C09 | 2 | 1 | 0 | 0 | 1 |
| L19.C10 | 3 | 3 | 0 | 0 | 0 |
| L2.C01 | 4 | 1 | 0 | 0 | 3 |
| L2.C02 | 4 | 1 | 0 | 0 | 3 |
| L2.C03 | 4 | 1 | 0 | 0 | 3 |
| L2.C04 | 4 | 1 | 0 | 0 | 3 |
| L2.C05 | 4 | 1 | 0 | 0 | 3 |
| L2.C06 | 4 | 1 | 0 | 0 | 3 |
| L2.C07 | 5 | 1 | 0 | 0 | 4 |
| L2.C08 | 4 | 0 | 0 | 0 | 4 |
| L2.C09 | 5 | 1 | 0 | 0 | 4 |
| L2.C10 | 4 | 0 | 0 | 0 | 4 |
| L2.C11 | 4 | 1 | 0 | 0 | 3 |
| L2.C12 | 4 | 0 | 0 | 0 | 4 |
| L2.C13 | 4 | 0 | 0 | 0 | 4 |
| L2.C14 | 3 | 0 | 0 | 0 | 3 |
| L2.C15 | 3 | 0 | 0 | 0 | 3 |
| L2.C16 | 4 | 0 | 0 | 0 | 4 |
| L2.C17 | 3 | 0 | 0 | 0 | 3 |
| L2.C18 | 7 | 1 | 0 | 0 | 6 |
| L2.C19 | 3 | 0 | 0 | 0 | 3 |
| L2.C20 | 3 | 0 | 0 | 0 | 3 |
| L2.C21 | 5 | 0 | 0 | 0 | 5 |
| L2.C22 | 5 | 0 | 0 | 0 | 5 |
| L20.C01 | 3 | 0 | 0 | 0 | 3 |
| L20.C02 | 3 | 2 | 0 | 0 | 1 |
| L20.C03 | 3 | 2 | 0 | 0 | 1 |
| L20.C04 | 3 | 2 | 0 | 0 | 1 |
| L20.C05 | 3 | 2 | 0 | 0 | 1 |
| L20.C06 | 4 | 4 | 0 | 0 | 0 |
| L20.C07 | 3 | 2 | 0 | 0 | 1 |
| L20.C08 | 4 | 1 | 0 | 0 | 3 |
| L20.C09 | 3 | 1 | 0 | 0 | 2 |
| L20.C10 | 3 | 1 | 0 | 0 | 2 |
| L20.C11 | 4 | 2 | 0 | 0 | 2 |
| L20.C12 | 3 | 1 | 0 | 0 | 2 |
| L20.C13 | 4 | 2 | 0 | 0 | 2 |
| L20.C14 | 3 | 2 | 0 | 0 | 1 |
| L20.C15 | 2 | 1 | 0 | 0 | 1 |
| L20.C16 | 3 | 1 | 0 | 0 | 2 |
| L20.C17 | 4 | 2 | 0 | 0 | 2 |
| L20.C18 | 3 | 1 | 0 | 0 | 2 |
| L20.C19 | 4 | 1 | 0 | 0 | 3 |
| L20.C20 | 4 | 1 | 0 | 0 | 3 |
| L20.C21 | 3 | 1 | 0 | 0 | 2 |
| L20.C22 | 3 | 0 | 0 | 0 | 3 |
| L20.C23 | 2 | 0 | 0 | 0 | 2 |
| L20.C24 | 3 | 3 | 0 | 0 | 0 |
| L20.C25 | 1 | 1 | 0 | 0 | 0 |
| L20.C26 | 3 | 1 | 1 | 0 | 1 |
| L21.C01 | 3 | 0 | 0 | 0 | 3 |
| L21.C02 | 3 | 0 | 0 | 0 | 3 |
| L21.C03 | 3 | 0 | 1 | 0 | 2 |
| L21.C04 | 5 | 1 | 0 | 1 | 3 |
| L21.C05 | 3 | 1 | 0 | 0 | 2 |
| L21.C06 | 3 | 0 | 0 | 0 | 3 |
| L21.C07 | 2 | 0 | 0 | 0 | 2 |
| L21.C08 | 1 | 1 | 0 | 0 | 0 |
| L22.C01 | 4 | 1 | 0 | 0 | 3 |
| L22.C02 | 2 | 1 | 0 | 0 | 1 |
| L22.C03 | 4 | 0 | 0 | 0 | 4 |
| L22.C04 | 4 | 0 | 0 | 0 | 4 |
| L22.C05 | 3 | 0 | 0 | 0 | 3 |
| L22.C06 | 4 | 0 | 0 | 0 | 4 |
| L22.C07 | 1 | 0 | 0 | 0 | 1 |
| L23.C01 | 4 | 0 | 0 | 0 | 4 |
| L23.C02 | 4 | 1 | 0 | 0 | 3 |
| L23.C03 | 4 | 1 | 0 | 0 | 3 |
| L23.C04 | 3 | 1 | 0 | 0 | 2 |
| L23.C05 | 3 | 1 | 0 | 0 | 2 |
| L23.C06 | 4 | 0 | 0 | 0 | 4 |
| L23.C07 | 3 | 0 | 0 | 0 | 3 |
| L24.C01 | 4 | 1 | 0 | 0 | 3 |
| L24.C02 | 4 | 1 | 0 | 0 | 3 |
| L24.C03 | 4 | 0 | 0 | 0 | 4 |
| L24.C04 | 4 | 1 | 0 | 0 | 3 |
| L24.C05 | 1 | 0 | 0 | 0 | 1 |
| L24.C06 | 1 | 1 | 0 | 0 | 0 |
| L24.C07 | 1 | 1 | 0 | 0 | 0 |
| L25.C01 | 4 | 0 | 0 | 0 | 4 |
| L25.C02 | 4 | 0 | 0 | 0 | 4 |
| L25.C03 | 3 | 0 | 0 | 0 | 3 |
| L25.C04 | 4 | 0 | 0 | 0 | 4 |
| L25.C05 | 3 | 0 | 0 | 0 | 3 |
| L25.C06 | 1 | 0 | 0 | 0 | 1 |
| L25.C07 | 1 | 0 | 0 | 0 | 1 |
| L26.C01 | 2 | 1 | 0 | 0 | 1 |
| L26.C02 | 1 | 1 | 0 | 0 | 0 |
| L26.C03 | 2 | 0 | 2 | 0 | 0 |
| L26.C04 | 1 | 1 | 0 | 0 | 0 |
| L26.C05 | 1 | 1 | 0 | 0 | 0 |
| L26.C06 | 1 | 0 | 0 | 0 | 1 |
| L26.C07 | 2 | 2 | 0 | 0 | 0 |
| L26.C08 | 2 | 1 | 0 | 0 | 1 |
| L26.C09 | 2 | 2 | 0 | 0 | 0 |
| L26.C10 | 2 | 2 | 0 | 0 | 0 |
| L26.C11 | 1 | 1 | 0 | 0 | 0 |
| L26.C12 | 1 | 1 | 0 | 0 | 0 |
| L26.C13 | 1 | 0 | 0 | 0 | 1 |
| L3.C01 | 5 | 0 | 0 | 0 | 5 |
| L3.C02 | 4 | 0 | 0 | 0 | 4 |
| L3.C03 | 3 | 0 | 0 | 0 | 3 |
| L3.C04 | 6 | 0 | 0 | 0 | 6 |
| L3.C05 | 3 | 0 | 0 | 0 | 3 |
| L3.C06 | 4 | 0 | 0 | 0 | 4 |
| L3.C07 | 4 | 0 | 0 | 0 | 4 |
| L3.C08 | 4 | 0 | 0 | 0 | 4 |
| L3.C09 | 3 | 0 | 0 | 0 | 3 |
| L3.C10 | 2 | 0 | 0 | 0 | 2 |
| L5.C01 | 4 | 0 | 0 | 0 | 4 |
| L5.C02 | 3 | 0 | 0 | 0 | 3 |
| L5.C03 | 3 | 0 | 0 | 0 | 3 |
| L5.C04 | 3 | 0 | 0 | 0 | 3 |
| L5.C05 | 3 | 0 | 0 | 0 | 3 |
| L5.C06 | 4 | 0 | 0 | 0 | 4 |
| L5.C07 | 3 | 0 | 0 | 0 | 3 |
| L5.C08 | 3 | 0 | 0 | 0 | 3 |
| L5.C09 | 3 | 0 | 0 | 0 | 3 |
| L5.C10 | 3 | 0 | 0 | 0 | 3 |
| L6.C01 | 4 | 0 | 0 | 0 | 4 |
| L6.C02 | 3 | 0 | 0 | 0 | 3 |
| L6.C03 | 4 | 0 | 0 | 0 | 4 |
| L6.C04 | 4 | 0 | 0 | 0 | 4 |
| L6.C05 | 5 | 0 | 0 | 0 | 5 |
| L6.C06 | 10 | 1 | 0 | 0 | 9 |
| L6.C07 | 7 | 0 | 0 | 0 | 7 |
| L6.C08 | 6 | 0 | 0 | 0 | 6 |
| L6.C09 | 6 | 1 | 0 | 0 | 5 |
| L6.C10 | 7 | 1 | 0 | 0 | 6 |
| L6.C11 | 8 | 0 | 0 | 0 | 8 |
| L6.C12 | 11 | 2 | 0 | 0 | 9 |
| L6.C13 | 6 | 0 | 0 | 0 | 6 |
| L7.C01 | 2 | 0 | 0 | 0 | 2 |
| L7.C02 | 4 | 3 | 0 | 0 | 1 |
| L7.C03 | 2 | 0 | 0 | 0 | 2 |
| L7.C04 | 2 | 0 | 0 | 0 | 2 |
| L7.C05 | 2 | 0 | 0 | 0 | 2 |
| L7.C06 | 3 | 1 | 0 | 0 | 2 |
| L7.C07 | 3 | 1 | 0 | 0 | 2 |
| L7.C08 | 3 | 0 | 0 | 1 | 2 |
| L7.C09 | 3 | 0 | 0 | 0 | 3 |
| L7.C10 | 3 | 0 | 0 | 0 | 3 |
| L7.C11 | 3 | 0 | 0 | 0 | 3 |
| L7.C12 | 3 | 0 | 1 | 0 | 2 |
| L7.C13 | 2 | 0 | 0 | 0 | 2 |
| L7.C14 | 2 | 0 | 0 | 0 | 2 |
| L7.C15 | 2 | 0 | 0 | 0 | 2 |
| L7.C16 | 3 | 1 | 0 | 0 | 2 |
| L7.C17 | 2 | 1 | 0 | 0 | 1 |
| L7.C18 | 2 | 0 | 0 | 0 | 2 |
| L7.C19 | 3 | 1 | 0 | 0 | 2 |
| L7.C20 | 3 | 1 | 0 | 0 | 2 |
| L7.C21 | 4 | 1 | 0 | 0 | 3 |
| L7.C22 | 2 | 0 | 0 | 0 | 2 |
| L8.C01 | 3 | 0 | 0 | 0 | 3 |
| L8.C02 | 1 | 0 | 0 | 0 | 1 |
| L8.C03 | 1 | 0 | 0 | 0 | 1 |
| L8.C04 | 1 | 0 | 0 | 0 | 1 |
| L8.C05 | 1 | 0 | 0 | 0 | 1 |
| L8.C06 | 1 | 0 | 0 | 0 | 1 |
| L8.C07 | 1 | 0 | 0 | 0 | 1 |
| L8.C08 | 1 | 0 | 0 | 0 | 1 |
| L8.C09 | 1 | 0 | 0 | 0 | 1 |
| L8.C10 | 1 | 0 | 0 | 0 | 1 |
| L8.C11 | 2 | 1 | 0 | 0 | 1 |
| L8.C12 | 2 | 1 | 0 | 0 | 1 |
| L8.C13 | 2 | 1 | 0 | 0 | 1 |
| L8.C14 | 1 | 0 | 0 | 0 | 1 |
| L8.C15 | 2 | 1 | 0 | 0 | 1 |
| L8.C16 | 1 | 0 | 0 | 0 | 1 |
| L8.C17 | 2 | 1 | 0 | 0 | 1 |
| L8.C18 | 2 | 1 | 0 | 0 | 1 |
| L8.C19 | 1 | 0 | 0 | 0 | 1 |
| L8.C20 | 1 | 0 | 0 | 0 | 1 |
| L8.C21 | 1 | 0 | 0 | 0 | 1 |
| L8.C22 | 1 | 0 | 0 | 0 | 1 |
| L8.C23 | 1 | 0 | 0 | 0 | 1 |
| L8.C24 | 2 | 1 | 0 | 0 | 1 |
| L8.C25 | 2 | 1 | 0 | 0 | 1 |
| L8.C26 | 2 | 1 | 0 | 0 | 1 |
| L8.C27 | 3 | 0 | 0 | 0 | 3 |
| L8.C28 | 2 | 0 | 0 | 0 | 2 |
| L8.C29 | 3 | 0 | 0 | 0 | 3 |
| L8.C30 | 3 | 0 | 0 | 1 | 2 |
| L8.C31 | 4 | 2 | 0 | 1 | 1 |
| L8.C32 | 1 | 0 | 0 | 0 | 1 |
| L8.C33 | 4 | 0 | 0 | 0 | 4 |
| L8.C34 | 1 | 0 | 0 | 0 | 1 |
| L8.C35 | 1 | 0 | 0 | 0 | 1 |
| L8.C36 | 2 | 1 | 0 | 0 | 1 |
| L8.C37 | 1 | 0 | 0 | 0 | 1 |
| L8.C38 | 1 | 0 | 0 | 0 | 1 |
| L8.C39 | 1 | 0 | 0 | 0 | 1 |
| L8.C40 | 1 | 0 | 0 | 0 | 1 |
| L8.C41 | 2 | 0 | 0 | 0 | 2 |
| L9.C01 | 1 | 0 | 0 | 0 | 1 |

## Par occurrence — ancienne date, file, traces et appui

### L0.C01

- `L0.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L1.C02

- `L1.C02/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C02/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C02/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C02/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C02/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C02/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C03

- `L1.C03/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S7` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C03/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C04

- `L1.C04/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S7` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S8` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S9` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C04/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C05

- `L1.C05/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C05/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C06

- `L1.C06/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C06/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C07

- `L1.C07/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C07/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C07/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C08

- `L1.C08/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S2` — ancienne date 2026-09-03 — file A, orientation vers ouverte — traces : T7 (verifications_en_attente[3]) « S2 : numéro de page de la citation de Soddy dans l'édition 1926 ou la réimpression 1983 — l'OCR ne porte pas les folios. »
- `L1.C08/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S10 (Moore 1988), S11 (Gesell 1916), S5 (Lavoie 2014) : ouvrages non ouverts ; confirmer éditions et, pour S5, le chapit »
- `L1.C08/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S7` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « S8 (S&P Global) : le site refuse les requêtes automatiques ; ouvrir la page dans un navigateur et confirmer la phrase «  »
- `L1.C08/S9` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C08/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S10 (Moore 1988), S11 (Gesell 1916), S5 (Lavoie 2014) : ouvrages non ouverts ; confirmer éditions et, pour S5, le chapit »
- `L1.C08/S11` — ancienne date 2026-09-03 — file B, traces contradictoires — traces : T2 (verifications_en_attente[15]) « **S11 EST OUVERT LE 2026-09-08 PAR L16.C01, ET L'OUVERTURE COÛTE UNE INCOMPATIBILITÉ.** La vérification en attente de ce » ; T3 (verifications_en_attente[2]) « S10 (Moore 1988), S11 (Gesell 1916), S5 (Lavoie 2014) : ouvrages non ouverts ; confirmer éditions et, pour S5, le chapit » ; T3 (verifications_en_attente[15]) « **S11 EST OUVERT LE 2026-09-08 PAR L16.C01, ET L'OUVERTURE COÛTE UNE INCOMPATIBILITÉ.** La vérification en attente de ce »

### L1.C09

- `L1.C09/S1` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C09/S3` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C09/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S13` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S14` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S15` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « S1, S3, S5, S6, S7, S9, S10, S11, S12, S13, S14, S15 : localisés (pages ou chapitres) par Deep Research, non ouverts par »
- `L1.C09/S16` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C09/S17` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C09/S18` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C09/S19` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune

### L1.C10

- `L1.C10/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S2` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « I believe that the future will learn more from the spirit of Gesell than from that of Marx » [S3] »
- `L1.C10/S4` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[3]) « WIR [S4] [S5] : 60 000 à 65 000 entreprises au pic 1995-2005, 30 000 à 40 000 clientes en 2024 ; volume WIR : 2,52 Md CH »
- `L1.C10/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[3]) « WIR [S4] [S5] : 60 000 à 65 000 entreprises au pic 1995-2005, 30 000 à 40 000 clientes en 2024 ; volume WIR : 2,52 Md CH »
- `L1.C10/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « the new money must not be freely convertible into gold, for that would require that gold reserves should be held again »
- `L1.C10/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S8` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S13` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S14` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »
- `L1.C10/S15` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « étaient sans aucun doute des signes monétaires », et leur émission violait le monopole de la Nationalbank [S15] »
- `L1.C10/S16` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S17` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S18` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S19` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « the digital euro would never be programmable money […]. That would be tantamount to a voucher. And central banks issue »
- `L1.C10/S20` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[1]) « ÉCARTÉ — Référence « Marshall & O'Neill, IJCCR, 2022 » proposée pour le Bristol Pound : introuvable sur Crossref. Rempla »
- `L1.C10/S21` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C10/S22` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S2, S7, S9, S10, S11, S12 (rouvrir pour ce chapitre), S14, S22 : à ouvrir par un humain ; confirmer éditions et passages »

### L1.C11

- `L1.C11/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C11/S2` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « S2 (PNUE 2026) : page PNUE et dépôt wedocs refusent les requêtes automatiques (403). Valeurs recoupées sur plusieurs rep » ; T3 (verifications_en_attente[13]) « S2, S6, S9 : à ouvrir. S7 : ouvert pour L1.C07. »
- `L1.C11/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C11/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « facteurs des catégories de risque existantes » — risque de crédit, de marché, opérationnel [S4] »
- `L1.C11/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C11/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S2, S6, S9 : à ouvrir. S7 : ouvert pour L1.C07. »
- `L1.C11/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S2, S6, S9 : à ouvrir. S7 : ouvert pour L1.C07. »
- `L1.C11/S8` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C11/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[4]) « Olson 1965, Axelrod 1984 [S9] : ajoutés à la demande de l'audit pour donner une base formelle aux « dilemmes sociaux » ; » ; T3 (verifications_en_attente[13]) « S2, S6, S9 : à ouvrir. S7 : ouvert pour L1.C07. »

### L1.C12

- `L1.C12/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C12/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C12/S3` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[1]) « CRITIQUE — Le texte source déduisait de MV = PT que « plus de monnaie égale plus de transactions égale plus de pression  »
- `L1.C12/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C12/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C12/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE). »
- `L1.C12/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE). »
- `L1.C12/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE). »
- `L1.C12/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE). »
- `L1.C12/S10` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C12/S11` — ancienne date 2026-09-03 — file A, orientation vers ouverte — traces : T2 (verifications_en_attente[8]) « S11 : ouvrir le rapport NGFS 2019 ; le discours de Carney est ouvert pour L1.C09. »
- `L1.C12/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S12 : ouvrage non ouvert ; cité pour l'objection de la dématérialisation, à confirmer. » ; T3 (verifications_en_attente[13]) « S7, S8, S12 : ouvrages non ouverts. S6 : ouvert pour L1.C11. S9 : à ouvrir (page PNUE). »

### L1.C13

- `L1.C13/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S8` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S9` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « Nous nous obligeons à creuser des trous de plus en plus profonds dans la nature pour combler des trous de plus en plus »
- `L1.C13/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S13` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S14` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »
- `L1.C13/S15` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C13/S16` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S7, S10, S11, S12, S13, S14, S16 : ouvrages et articles non ouverts (DOI confirmés pour S12, S13, S14, S16). S5 : rappor »

### L1.C14

- `L1.C14/S1` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « chaque effort pour rembourser ne fait que préparer la prochaine chute » [S2] »
- `L1.C14/S3` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S4` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »
- `L1.C14/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S1, S5, S6, S9, S10, S11, S12 : ouvrages non ouverts (Deep Research affirme les avoir ouverts ; non confirmé). S3, S4, S »

### L1.C15

- `L1.C15/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : T4 (corps) « « Les communs ? C'est ce que tout le monde bousille parce que ça rapporte et que personne ne répare parce que ça coûte ! »
- `L1.C15/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C15/S3` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S4` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S5` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C15/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S7` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C15/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S9` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C15/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S13` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S14` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »
- `L1.C15/S15` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S3, S6, S8, S11, S12, S14, S15 : ouvrages non ouverts. S4, S10, S13 : DOI confirmés, non ouverts. »

### L1.C16

- `L1.C16/S1` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S2` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S3` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S4` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[1]) « S6 : ouvrir les formulaires 10-K de Gilead sur EDGAR (CIK 0000882095) et confirmer les cinq valeurs annuelles ; le prix  » ; T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S7` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « S9 : ouvrir le communiqué DGCCRF du 7 février 2020 (site economie.gouv.fr, refuse les requêtes automatiques) et confirme » ; T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S10` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S11` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »
- `L1.C16/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S1 : article et livre ouverts pour L1.C15. S2, S4, S7, S8, S11, S12 : ouvrages et articles non ouverts. S5 : DOI confirm »

### L1.C17

- `L1.C17/S1` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S2` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S3` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S5` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S6` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S7` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S8` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S9` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S10` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S11` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C17/S12` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S13` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »
- `L1.C17/S14` — ancienne date 2026-09-03 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S5, S6, S8, S9, S12, S13, S14 : ouvrages non ouverts. »

### L1.C18

- `L1.C18/S1` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[23]) « S1 : ouvrir les sections du chapitre 7 non lues ici — « S'affranchir de la concurrence des devises », « Révolution du tr » ; T4 (corps) « « un organisme qui définit ce qui constitue une activité régénérative et qui décide dans le même temps du montant qu'ell »
- `L1.C18/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C18/S5` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  »
- `L1.C18/S6` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  »
- `L1.C18/S7` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  » ; T4 (corps) « « inscrits dans la délégation elle-même plutôt que laissés à une décision discrétionnaire » [S7] »
- `L1.C18/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S9` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T7 (verifications_en_attente[2]) « LIMITE — La légitimité de l'Assemblée des Communs repose sur une chaîne de délégation mince : les parlements nationaux n »
- `L1.C18/S10` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  »
- `L1.C18/S11` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  »
- `L1.C18/S12` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[22]) « S5, S6, S7, S10, S11, S12 : ouvrages et articles non ouverts ; références issues du rapport documentaire, à confrontrer  »
- `L1.C18/S13` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S14` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C18/S15` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S16` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S17` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[17]) « S17 : DOI à confirmer — Science 357(6348), 2017, non ouvert. »
- `L1.C18/S18` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S19` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S20` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S21` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C18/S22` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L1.C19

- `L1.C19/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « Qui dit deux finances différentes ne veut pas dire deux monnaies différentes, mais plutôt deux orientations différente »
- `L1.C19/S2` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[10]) « S2 : Musgrave 1959 non ouvert. » ; T3 (verifications_en_attente[11]) « S2, S3, S6 : articles et ouvrages non ouverts ; DOI vérifiés pour S2 et S3. »
- `L1.C19/S3` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S2, S3, S6 : articles et ouvrages non ouverts ; DOI vérifiés pour S2 et S3. »
- `L1.C19/S4` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C19/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C19/S6` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[6]) « S6 : le rapport documentaire situe le critère DC5 à la page 569 de Tucker, là où le rapport précédent le situait au chap » ; T3 (verifications_en_attente[11]) « S2, S3, S6 : articles et ouvrages non ouverts ; DOI vérifiés pour S2 et S3. »
- `L1.C19/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C19/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C19/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L1.C20

- `L1.C20/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « Rueff avait probablement raison sur ce point : si la création monétaire n'est pas compensée par une destruction, un dé »
- `L1.C20/S2` — ancienne date 2026-09-04 — file B, traces contradictoires — traces : T3 (verifications_en_attente[6]) « S2 : les citations de Rueff sont rapportées par le rapport documentaire avec pagination, non vérifiées. Ouvrir L'Âge de  » ; T7 (verifications_en_attente[6]) « S2 : les citations de Rueff sont rapportées par le rapport documentaire avec pagination, non vérifiées. Ouvrir L'Âge de  »
- `L1.C20/S3` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[13]) « S3 : Fisher 1911 non ouvert. »
- `L1.C20/S4` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[11]) « S4 : Gurley et Shaw 1960 non ouvert. La distinction inside/outside money est standard, la formulation exacte reste à vér »
- `L1.C20/S5` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S5 : Buiter, « Can Central Banks Go Broke? », n'est pas indexé par Crossref — il s'agit d'une note CEPR Policy Insight,  »
- `L1.C20/S6` — ancienne date 2026-09-03 — file D, sans orientation — traces : aucune
- `L1.C20/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C20/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C20/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C20/S10` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[9]) « S10 : Goodhart 1975 non ouvert ; vérifier la référence exacte et la paternité de la formulation courante, souvent attrib »

### L1.C21

- `L1.C21/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « Une taxe sur l'échange freine l'échange ; une taxe sur la détention l'accélère. Les confondre revient à se priver de l »
- `L1.C21/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « à définir progressivement selon les paramètres du système NEMO IMS déployé » [S2] »
- `L1.C21/S3` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[15]) « S3 : Gesell 1916 non ouvert ; vérifier l'étymologie maritime du terme demurrage et la description de l'expérience de Wör »
- `L1.C21/S4` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[16]) « S4 : Keynes 1936 non ouvert. Vérifier en particulier le chapitre 23, section VI, où Keynes traite de Gesell — le livre s » ; T4 (corps) « « une longue série de substituts prendra leur place — monnaie de banque, créances à vue, monnaie étrangère, bijoux et mé »
- `L1.C21/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C21/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C21/S7` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[17]) « S7, S8 : non ouverts. Vérifier que le mécanisme de déduction de la TVA évite bien l'effet de cascade au sens où le livre »
- `L1.C21/S8` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[17]) « S7, S8 : non ouverts. Vérifier que le mécanisme de déduction de la TVA évite bien l'effet de cascade au sens où le livre »
- `L1.C21/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C21/S10` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[14]) « S10 : Bovenberg et de Mooij 1994, Fullerton et Metcalf 1997, non ouverts. »
- `L1.C21/S11` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[12]) « S11 : Umlauf 1993, DOI donné mais article non ouvert ; vérifier les 60 % et le périmètre des onze valeurs. »
- `L1.C21/S12` — ancienne date 2026-09-04 — file D, sans orientation — traces : T5 (L20.C21) « même référence marquée T1 ailleurs »
- `L1.C21/S13` — ancienne date 2026-09-04 — file B, traces contradictoires — traces : T2 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de » ; T3 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de »
- `L1.C21/S14` — ancienne date 2026-09-04 — file B, traces contradictoires — traces : T2 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de » ; T3 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de » ; T5 (L8.C31) « même référence marquée T1 ailleurs »
- `L1.C21/S15` — ancienne date 2026-09-04 — file B, traces contradictoires — traces : T2 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de » ; T3 (verifications_en_attente[0]) « iedman, Lucas et Kydland-Prescott de première main [S13], [S14], [S15]. Les trois références portent le § sur le mode de » ; T5 (L8.C31) « même référence marquée T1 ailleurs »

### L1.C22

- `L1.C22/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « de nombreux défis doivent être relevés » [S1] »
- `L1.C22/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S10` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S11` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S12` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S13` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C22/S14` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L1.C23

- `L1.C23/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « une aspiration coincée dans un moteur conçu pour accélérer » [S2] »
- `L1.C23/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « ce constat reste vrai même lorsque des exigences de fonds propres et de liquidité sont imposées aux banques » [S7] »
- `L1.C23/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S10` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S11` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S12` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S13` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S14` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S15` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S16` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S17` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C23/S18` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « jusqu'à ce que les contradictions deviennent insurmontables, comme en 1929, dans les années 1970 ou en 2007 » [S18] »
- `L1.C23/S19` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « le taux de croissance requis des investissements doit progressivement s'élever au cours d'une phase de croissance »**  »

### L1.C24

- `L1.C24/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « développer son économie sans accumuler des dettes extérieures insoutenables » [S1] »
- `L1.C24/S2` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « S2 et S12 — CLOS le 2026-09-04 sans recourir à un rapport tiers. Les parts de Mehrling (début des années 2010) sont déso »
- `L1.C24/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « SDRs can be used to settle debts to governments and the IMF itself, but not for other purposes [...]. They cannot be u »
- `L1.C24/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « un pur nombre notionnel qui sert d'unité de référence pour les taux de change entre monnaies nationales », et **« il n »
- `L1.C24/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S10` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S11` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C24/S12` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « S2 et S12 — CLOS le 2026-09-04 sans recourir à un rapport tiers. Les parts de Mehrling (début des années 2010) sont déso »

### L1.C25

- `L1.C25/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « À chaque fois que le monde a changé de système monétaire international, cela ne s'est fait qu'à la sortie d'une grande »
- `L1.C25/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « n'ont jamais été le fruit d'une planification sereine — elles ont été arrachées à des moments de crise aiguë, lorsque  »
- `L1.C25/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « exactement la dynamique qui a présidé à la naissance de la zone euro » [S3] »
- `L1.C25/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « Le dollar, c'est notre monnaie, mais c'est votre problème » [S4] »
- `L1.C25/S5` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[3]) « Despres, Kindleberger et Salant de première main [S6]. L'article de 1966 n'a pas été ouvert ; il est connu par la note d » ; T4 (corps) « « When the US unilaterally broke the connection with gold, even the weak discipline of the gold anchor was lost », et le »
- `L1.C25/S6` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[3]) « Despres, Kindleberger et Salant de première main [S6]. L'article de 1966 n'a pas été ouvert ; il est connu par la note d »
- `L1.C25/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C25/S8` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[4]) « Le traité de Maastricht et le calendrier de l'union monétaire [S8]. Dates et jalons écrits de mémoire dans cette passe,  »
- `L1.C25/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C25/S10` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C25/S11` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C25/S12` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « thus, only a country which keeps as nearly as possible in a state of international balance on the average of the year  »

### L1.C26

- `L1.C26/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « un référentiel de comptabilité universel, autour duquel toutes les devises du monde se convertiront directement entre  »
- `L1.C26/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « un étalon, neutre et non-national, dont la valeur n'est pas fixée par les marchés mais par des critères écologiques et »
- `L1.C26/S3` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « MUNDELL 1963 OUVERT DE PREMIÈRE MAIN le 2026-09-05, tirage JSTOR procuré par l'auteur, et dépouillé en L11.C04. **L'obje »
- `L1.C26/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C26/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C26/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « un pur nombre notionnel [...]. Il ne remplace aucune monnaie » [S6] »
- `L1.C26/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C26/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C26/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « the first private entity issuing an SDR bond or deposit incurred extra costs as a result of the instrument's illiquidi »

### L1.C27

- `L1.C27/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « si NEMO IMS repose sur l'adhésion souveraine des nations, une question se pose : pourquoi un État renoncerait-il à res »
- `L1.C27/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « il convient donc de le reconnaître franchement : NEMO IMS comporte un seuil d'activation en dessous duquel il ne fonct »
- `L1.C27/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « ce sont les émissions de NEMO Green SDR [...] qui rééquilibreront et stabiliseront les économies nationales. Autrement »
- `L1.C27/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C27/S5` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T2 (verifications_en_attente[0]) « Barrett 1994 et Nordhaus 2015 de première main [S5], [S6]. Le § 5 leur fait porter à la fois l'objection au seuil affirm »
- `L1.C27/S6` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T2 (verifications_en_attente[0]) « Barrett 1994 et Nordhaus 2015 de première main [S5], [S6]. Le § 5 leur fait porter à la fois l'objection au seuil affirm » ; T5 (L7.C16, L7.C17) « même référence marquée T1 ailleurs »
- `L1.C27/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : T5 (L20.C20) « même référence marquée T1 ailleurs »
- `L1.C27/S8` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C27/S9` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L1.C28

- `L1.C28/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « les économistes ne s'émerveillent que de la grandeur des chiffres sans jamais tenir de discours critiques sur la teneu »
- `L1.C28/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « une boussole visuelle qui remplace l'objectif de croissance infinie par celui d'un équilibre dynamique », bornée par u »
- `L1.C28/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « les révisions seraient probablement soumises à des critères objectifs et transparents, potentiellement basés sur des i »
- `L1.C28/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « le tableau de bord multidimensionnel présenté à l'épisode 28 de la série principale trouve dans le cahier technique sa »
- `L1.C28/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C28/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « une boussole visuelle qui remplace l'objectif de croissance infinie par celui d'un équilibre dynamique », bornée par u »
- `L1.C28/S7` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L1.C29

- `L1.C29/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « par convention, les Banques centrales pourront augmenter la taille de leur bilan [...]. La différence est que la contr »
- `L1.C29/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « L'émission des NGDTS s'inscrit au passif du bilan du GES. Face à ce passif, deux contreparties apparaissent à l'actif  »
- `L1.C29/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « la formulation comptable définitive de la contrepartie des NGDTS » [S3] »
- `L1.C29/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C29/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L1.C29/S6` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T2 (verifications_en_attente[0]) « Stella 1997 et Buiter 2008 de première main [S6]. Le § 5 leur fait porter l'issue qu'il propose — assumer des fonds prop »

### L1.C30

- `L1.C30/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « Leur argent [...] ne pouvait naître qu'en abîmant quelque chose. Chaque fois qu'un morceau de monnaie était créé, quel »
- `L1.C30/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « ce livre est une invitation à commencer » [S2] »

### L1.C31

- `L1.C31/S1` — ancienne date 2026-09-09 — file D, sans orientation — traces : aucune
- `L1.C31/S2` — ancienne date 2026-09-09 — file D, sans orientation — traces : aucune

### L10.C01

- `L10.C01/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) «  refonte**, JO L 347/37 du 20 décembre 2016 — **OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L10.C02

- `L10.C02/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « tion et règles de valorisation du bilan »** — **OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « sauf dans les cas relevant des règles particulières spécifiées à l'annexe IV », et a déclaré cette annexe non instruit »

### L10.C03

- `L10.C03/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « Weiss e.a.*, C-493/17, ECLI:EU:C:2018:1000** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « titres de créance NÉGOCIABLES éligibles »** [S2] »
- `L10.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L10.C04

- `L10.C04/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « uweiler e.a.*, C-62/14, ECLI:EU:C:2015:400** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « la certitude qui fait marcher le dispositif est celle que la Cour interdit »** [S3] »

### L10.C05

- `L10.C05/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « 3 et 125 TFUE), JO L 332 du 31 décembre 1993 — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **transformer ultérieurement ces créances en titres négociables et à des conditions de marché** » [S2] »
- `L10.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « l'acquisition la plus urgente de ce livre, devant toutes les autres »** [S3] »

### L10.C06

- `L10.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L10.C07

- `L10.C07/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « 23 décembre 1913, 38 Stat. 264, tel qu'amendé. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L10.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L10.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L11.C01

- `L11.C01/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « ne sont pas des destructions monétaires au sens propre, mais des mécanismes de reflux comptables vers la comptabilité  »
- `L11.C01/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « NEMO IMS n'invente pas une comptabilité radicalement nouvelle » [S2] »
- `L11.C01/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « la création monétaire n'est pas un problème si elle s'accompagne d'une destruction monétaire équivalente par ailleurs  »
- `L11.C01/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C01/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C01/S6` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C02

- `L11.C02/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C02/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C02/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « les soldes de fin de mois des **réserves bancaires déposées à la banque centrale** », à un taux de l'ordre de 0,1 % me »
- `L11.C02/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C02/S5` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « L'analogie TARGET2 [S5]. Elle porte le § 4, qui est le résultat le plus lourd du chapitre, et elle n'est adossée à aucun »

### L11.C03

- `L11.C03/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « the values to be chosen for the target values have to satisfy these conditions **if the problem of policy is to be sol » ; T6 (git) « date 2026-09-06 postérieure à la création 2026-09-05 »
- `L11.C03/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S6` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S7` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C03/S8` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[4]) « Carré et Couppey-Soubeyran, Revue économique 66, 2015, sur la coordination monétaire et macroprudentielle — relevée dans »

### L11.C04

- `L11.C04/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « ne peut pas maintenir un taux d'intérêt différent du niveau général qui prévaut à l'étranger » [S1] »
- `L11.C04/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C04/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C04/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « un taux d'intérêt négatif sur les réserves, tel que le pratiquait la Banque centrale européenne » [S4] »
- `L11.C04/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L11.C05

- `L11.C05/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C05/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « un micro-impôt de 0,5 % prélevé sur chaque paiement », plus une taxe de 0,05 à 0,2 % sur les flux financiers [S2] »
- `L11.C05/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C05/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C05/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C05/S6` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[6]) « Read 1958 et Hayek 1945 [S6], non ouverts. Le corpus emploie la prémisse de l'essai et récuse sa conclusion ; il doit vé »
- `L11.C05/S7` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C06

- `L11.C06/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C06/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C06/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C06/S4` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[3]) « Le coût de la certification rapporté à la taille de l'entreprise. Le § 5 soutient que la procédure de révision engendre  »
- `L11.C06/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C07

- `L11.C07/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C07/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C07/S3` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T1 (reference) « C-37/20 et C-601/20, ECLI:EU:C:2022:912, 25 p. — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (EUR » ; T4 (corps) « « doivent être accessibles, **dans tous les cas, aux autorités compétentes** et aux cellules de renseignement financier, »
- `L11.C07/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C07/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « ne peut pas maintenir un taux d'intérêt différent du niveau général qui prévaut à l'étranger » [S5] »

### L11.C08

- `L11.C08/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « Il faudra cependant envisager des mécanismes de dérogations. Je ne souhaite pas que des gens soient soumis au demurrag »
- `L11.C08/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « monnaie de banque, créances à vue, monnaie étrangère, bijoux et métaux précieux » [S2] »
- `L11.C08/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C08/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C08/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L11.C09

- `L11.C09/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C09/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C09/S3` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « L'incidence du prélèvement sur les réserves bancaires [S3]. Si le nœud retenu était celui des voisins, toute la question »
- `L11.C09/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C09/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L11.C10

- `L11.C10/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « Il convient, je pense, d'appuyer l'idée d'une progressivité de la mise en place de ces dispositifs. De sorte que les i »
- `L11.C10/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : T5 (L8.C31) « même référence marquée T1 ailleurs »
- `L11.C10/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : T5 (L8.C31) « même référence marquée T1 ailleurs »
- `L11.C10/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C10/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C10/S6` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C10/S7` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C10/S8` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C10/S9` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C11

- `L11.C11/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C11/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C11/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C11/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C11/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C11/S6` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L11.C12

- `L11.C12/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « The values of the instrument variables are **dependent on those of the data**, i.e. they must vary with the data. As s »
- `L11.C12/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : T5 (L8.C31) « même référence marquée T1 ailleurs »
- `L11.C12/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « quand le substitut est effectivement disponible — capacité et prix constatés — et non à une date fixée d'avance » [S3] »
- `L11.C12/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C12/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C13

- `L11.C13/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C13/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « the values of the instrument variables are dependent, generally speaking, **on all the targets set and cannot be consi »
- `L11.C13/S3` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « HAYEK 1945 [S3], toujours non ouvert, alors que P19b est qualifiée dans le registre d'objection la plus forte adressée a »
- `L11.C13/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C13/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C13/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L11.C14

- `L11.C14/S1` — ancienne date 2026-09-04 — file A, orientation vers ouverte — traces : T2 (verifications_en_attente[1]) « LE TEXTE EXACT DU CAHIER sur les six familles [S1]. Le corpus travaille sur une restitution faite en L1.C28 § 4 et n'a p » ; T4 (corps) « « les indicateurs qui modulent les instruments macroprudentiels » [S1] »
- `L11.C14/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L11.C14/S3` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « STIGLITZ-SEN-FITOUSSI [S3], non ouvert, alors que l'alternative qu'il pose est la charnière du § 2 et de toute la promes »
- `L11.C14/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C14/S5` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L11.C15

- `L11.C15/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « potentiellement basées sur des indicateurs économiques clés tels que l'inflation, **la croissance du PIB**, ou la bala »
- `L11.C15/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C15/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « **as far as not under the command of the authority considered** » [S3] »
- `L11.C15/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C15/S5` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « BALASSA 1964 et SAMUELSON 1964 [S5], non ouverts. Le § 6 propose d'indexer la révision des parités sur un observable, et »

### L11.C16

- `L11.C16/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « ce sont les émissions de NEMO Green SDR qui **rééquilibreront et stabiliseront les économies nationales** » [S1] »
- `L11.C16/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « a single governmental unit to solve global collective action problems is **inherently weak because of free-rider probl »
- `L11.C16/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C16/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « a technical expression of a “sound policy” » [S4] »
- `L11.C16/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C16/S6` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « never exists in concentrated or integrated form » [S6] »

### L11.C17

- `L11.C17/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C17/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « the values of the instrument variables are dependent [...] **on all the targets set and cannot be considered in isolat »
- `L11.C17/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C17/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C18

- `L11.C18/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C18/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « certain proportionalities between the sacrifices of different social groups » [S2] »
- `L11.C18/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C19

- `L11.C19/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C19/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « certain proportionalities between the sacrifices of different social groups » [S2] »
- `L11.C19/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C20

- `L11.C20/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C20/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « indicate how the political parameters have to be **varied in relation to the changing data** » [S2] »
- `L11.C20/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C21

- `L11.C21/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « le mécanisme de perception existe sous la forme de la taxe sur la valeur ajoutée » [S1] »
- `L11.C21/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C21/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **a single governmental unit to solve global collective action problems is inherently weak because of free-rider probl »
- `L11.C21/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L11.C22

- `L11.C22/S1` — ancienne date 2026-09-04 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « FRIEDMAN 1968 N'EST TOUJOURS PAS OUVERT [S1], et ce chapitre repose sur lui plus que tout autre. Le résultat des délais  »
- `L11.C22/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L11.C22/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L11.C23

- `L11.C23/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « corréler l'ensemble à la politique macroprudentielle »** [S1] »
- `L11.C23/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C23/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « **priority is given to a single objective** » [S3] »
- `L11.C23/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « not in itself an element of well-being but rather a technical expression of a “sound policy” » [S4] »

### L11.C24

- `L11.C24/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « NEMO IMS comporte un seuil d'activation en dessous duquel il ne fonctionne pas » [S1] »
- `L11.C24/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C24/S3` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « LE RÈGLEMENT (UE) 2023/956 ET SES ACTES D'EXÉCUTION NE SONT PAS OUVERTS [S3]. **C'est la lacune principale et elle est p »

### L11.C25

- `L11.C25/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C25/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « affects few and therefore is less costly », l'efficacité recommande la seconde [S2] »
- `L11.C25/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **a single governmental unit to solve global collective action problems is inherently weak because of free-rider probl »

### L11.C26

- `L11.C26/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L11.C26/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « only become “active” [...] if their fulfilment is threatened » [S2] »
- `L11.C26/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L11.C26/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L11.C27

- `L11.C27/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « plus l'empreinte écologique cumulée d'un bien ou d'un actif est élevée, plus le taux appliqué à l'achat est fort » [S1 »
- `L11.C27/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C27/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « le droit à déduction de la TVA amont est **réservé aux seuls assujettis**. Dès lors, l'application d'une même règle ** »
- `L11.C27/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C27/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « un prélèvement modulé sur **les transactions monétaires** » [S5] »

### L11.C28

- `L11.C28/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C28/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C28/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C28/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L11.C29

- `L11.C29/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « Act de 1991**, édition 2023 du code américain. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** (g »
- `L11.C29/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C29/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C29/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L11.C29/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L11.C30

- `L11.C30/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L12.C01

- `L12.C01/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L12.C01/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ork, révision d'août 2025, Sales No. E.25.I.4.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L12.C01/S3` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e par Pacte mondial Réseau France, juillet 2024. OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  » ; T4 (corps) « « Promouvoir une croissance économique soutenue, partagée et durable, le plein emploi productif et un travail décent pou » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L12.C02

- `L12.C02/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « septembre 2015, distribuée le 21 octobre 2015.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »

### L12.C03

- `L12.C03/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « 2015 — VERSION FRANÇAISE OFFICIELLE, 44 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « Nous ménagerons, en particulier pour les États en développement, **une marge de manœuvre nationale** pour des politiqu »
- `L12.C03/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L13.C01

- `L13.C01/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L13.C01/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « and monetary policy », version d'octobre 2016.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L13.C01/S3` — ancienne date 2026-09-08 — file D, sans orientation — traces : T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L14.C01

- `L14.C01/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L14.C01/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L15.C01

- `L15.C01/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ervation work for climate change mitigation ».** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L15.C01/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « la santé biologique des sols et la biodiversité sous canopée échappent aux capteurs orbitaux et exigent des relevés de » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L15.C02

- `L15.C02/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « rbonne*, n° 2010.71, ISSN 1955-611X, 14 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « of the VAT extortion on the carbon market at **1.3 billion euros** »* [S1] »

### L15.C03

- `L15.C03/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  Letters*, vol. 10, n° 114005, 2015, 11 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **detected if the vehicle was undergoing emissions testing and modified operation of the emission control system** »*  »

### L15.C04

- `L15.C04/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « blie en application de la loi publique 111-21.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu »

### L16.C01

- `L16.C01/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  1916 ; préface de la troisième édition, 1918) — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **Free-Money loses ONE-THOUSANDTH of its face value WEEKLY, or about 5 % annually, at the expense of the holder** » [S » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L16.C01/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « **S10 (Moore 1988), S11 (GESELL 1916), S5 (Lavoie 2014) : OUVRAGES NON OUVERTS** » [S2] » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L16.C02

- `L16.C02/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « **the rent so received goes to the public treasury and is DISTRIBUTED MONTHLY IN EQUAL SHARES TO MOTHERS according to  »

### L16.C03

- `L16.C03/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « hi Company, New York, 1933, chapitres IV à VII — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **sold by the town, and the proceeds used [...] for the enlargement of the town's welfare work** » [S1] »

### L16.C04

- `L16.C04/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ntrale sous l'égide du conseil des gouverneurs — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **ability to control the amount of digital euro in circulation. The digital euro should be an attractive means of paym »

### L16.C05

- `L16.C05/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L17.C01

- `L17.C01/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « al Research Letters*, vol. 15, n° 065003, 2020 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **primary energy can be decoupled from GDP LARGELY TO THE EXTENT to which the conversion of primary energy to useful e » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L17.C01/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « comparer les théories et expériences de l'après-croissance, du Bonheur national brut à la décroissance, puis DE TESTER » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L17.C02

- `L17.C02/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « *, European Environmental Bureau, juillet 2019 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **Cheaper options are generally used first, the extraction of remaining stocks then becoming a more resource- and ener »

### L17.C03

- `L17.C03/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  n° 2676, 2021, DOI 10.1038/s41467-021-22884-9 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « rely on combinations of CONTROVERSIAL NEGATIVE EMISSIONS and UNPRECEDENTED TECHNOLOGICAL CHANGE, while ASSUMING CONTIN »

### L17.C04

- `L17.C04/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « semblée nationale du pays de Galles, 56 pages — OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu »

### L17.C05

- `L17.C05/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « nd Social Progress*, septembre 2009, 291 pages — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **a monetary index of sustainability has its place in such a dashboard but, under the current state of the art, IT SHO »

### L17.C06

- `L17.C06/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L18.C01

- `L18.C01/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « eur public*, éd. 2023** (recueil IPSAS 2026) — **OUVERT PAR TÉLÉCHARGEMENT DIRECT**, source fournie  »
- `L18.C01/S2` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « eld for Conservation*** (recueil IPSAS 2026) — **OUVERT PAR TÉLÉCHARGEMENT DIRECT**, même provenance »
- `L18.C01/S3` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « r Expenses*** (mai 2023, recueil IPSAS 2026) — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, m »
- `L18.C01/S4` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « tion d'informations en matière de durabilité — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »

### L18.C02

- `L18.C02/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « tem Accounting* (SEEA EA), version blanche** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT**, source fournie  » ; T4 (corps) « « **Sections A to C comprise THE INTERNATIONAL STATISTICAL STANDARD** describing the accounting framework and physical a »
- `L18.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C02/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C03

- `L18.C03/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « an Entity's Finances*** (recueil IPSAS 2026) — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, s » ; T4 (corps) « « Long-term fiscal sustainability is the ability of an entity to **meet service delivery and financial commitments both  »
- `L18.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « it was decided NOT TO DEVELOP ED 34 INTO AN IPSAS »** [S2] »
- `L18.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C04

- `L18.C04/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « essources, *Global Resources Outlook 2024*** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, s »
- `L18.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « shows that it is both POSSIBLE and PROFITABLE to decouple economic growth from environmental impacts and resource use  »
- `L18.C04/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C05

- `L18.C05/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « **IPSAS 47, *Revenue*** (recueil IPSAS 2026) — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, s »
- `L18.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C06

- `L18.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C07

- `L18.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Les deux autres capitaux **ne sont que des moyens utilisés par le CF** : de simples actifs ou ressources figurant à l' »
- `L18.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « il y a donc ici autant de “coûts carbone” que d'entreprises et PAS DE MARCHÉ MONDIAL BASÉ SUR UN PRIX DU CARBONE »** [ »
- `L18.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C07/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « doit refléter le contexte institutionnel courant » et reflète « diverses imperfections de marché »** [S4] »

### L18.C08

- `L18.C08/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C08/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **The allocation is ALWAYS A TOPIC OF NEGOTIATION within the collective.** »

::etat:: **À défaut d'unité d'œuvre, les »
- `L18.C08/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C08/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C09

- `L18.C09/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « trillion dollar nature transition economy*** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, p »
- `L18.C09/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L18.C09/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L18.C10

- `L18.C10/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « A EA)*, ST/ESA/STAT/SER.F/124, New York, 2024.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »

### L18.C11

- `L18.C11/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  the New Millennium*, Washington, 2011, 148 p.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « Substitutability among Different Types of Capital »**, et l'ouvre ainsi [S1] »

### L18.C12

- `L18.C12/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « edge, 4 décembre 2023, ISBN 978-1-032-03737-0.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « Le corpus n'a ouvert aucune critique de cette norme, et il en existe. »* **Elle est ouverte** [S1] »

### L18.C13

- `L18.C13/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « l of valuation », 170 pages, version anglaise.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **More than 50 clearly distinct valuation methods** are identifiable from the last four decades of valuation research  »

### L18.C14

- `L18.C14/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ater to the Changing Wealth of Nations*, 2024.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « firmly establishes COMPREHENSIVE WEALTH AS A MEASURE OF SUSTAINABILITY* and a key component of country analytics »***  »

### L18.C15

- `L18.C15/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ecision-making », 141 pages, version anglaise.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **Despite public commitment** to environmental and social causes, **MARKET VALUES COMMONLY PREVAIL where economic trad »

### L18.C16

- `L18.C16/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  WORKING PAPER n° 103, février 1973, 42 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « Only the Cobb-Douglas will do among CES functions. **If the elasticity of substitution between resources and other fac »
- `L18.C16/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T5 (L18.C11) « même référence marquée T1 ailleurs »

### L18.C17

- `L18.C17/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ute Discussion Paper* TI 2006-061/3, 25 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « include an income effect and therefore represent economic substitution potential »* [S1] »

### L18.C18

- `L18.C18/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ward Elgar Publishing, ISBN 978-1-03532-789-8.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « a persuasive case can be made that there is **no need for preserving natural resources as an input into the production »

### L18.C19

- `L18.C19/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ring strong sustainability », pages 146 à 170.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C20

- `L18.C20/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ural capital substitutable? », pages 50 à 105.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L » ; T4 (corps) « « The only thing we do know is that they are not certain. »*

::etat:: **L'auteur écarte explicitement la solution par l »

### L18.C21

- `L18.C21/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « uncertainty, and ignorance », pages 107 à 124.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C22

- `L18.C22/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « suring weak sustainability », pages 125 à 145.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C23

- `L18.C23/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « le pour la reconstruction et le développement.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L » ; T4 (corps) « « is likely an **underestimate**, as data and conceptual concerns limit the ability to measure and value this component. »
- `L18.C23/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L18.C24

- `L18.C24/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « 2.4.5 « The Real Controversy », pages 41 à 46.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C25

- `L18.C25/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « ue), Tuyeni H. Mwampamba (Tanzanie / Mexique).** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **R » ; T4 (corps) « « Aggregation of values held by individuals to inform collective decisions is **central to valuations (well established) »

### L18.C26

- `L18.C26/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « n (Norvège), Rebecca Chaplin-Kramer et autres.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **R »

### L18.C27

- `L18.C27/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « donnatrice Eszter Kelemen (Hongrie) et autres.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **R »

### L18.C28

- `L18.C28/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « scussion Paper* 07-37, juillet 2007, 24 pages.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-09 depu »

### L18.C29

- `L18.C29/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « et réglementaires), pages 19 à 25 du chapitre.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C30

- `L18.C30/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « aison entre types), pages 28 à 34 du chapitre.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L18.C31

- `L18.C31/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) «  (les huit étapes), pages 81 à 90 du chapitre.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L »

### L19.C01

- `L19.C01/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « le troisième des cinq objets à verrouiller : le passif », et ajoute que « sans lui, ni A30 ni A35 ne peuvent se clore  » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L19.C01/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  *System of National Accounts 2008*, 719 pages — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L19.C02

- `L19.C02/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e mondiale, *System of National Accounts 2008* — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »

### L19.C03

- `L19.C03/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e mondiale, *System of National Accounts 2008* — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « **When the value of the principal is indexed to an indicator [...] the payment owing to indexation SHOULD BE RECORDED  »
- `L19.C03/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « un prélèvement sur la détention est un rendement négatif » [S2] »

### L19.C04

- `L19.C04/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e mondiale, *System of National Accounts 2008* — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « **may represent an asset to the holder WHEN THE AGREEMENT RESTRICTS THE GENERAL USE OR SUPPLY OF PRODUCTS covered by t »
- `L19.C04/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L19.C05

- `L19.C05/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e mondiale, *System of National Accounts 2008* — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »
- `L19.C05/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L19.C06

- `L19.C06/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e mondiale, *System of National Accounts 2008* — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « **Even though a corporation is wholly owned by its shareholders collectively, it is seen to have A NET WORTH (WHICH CO »

### L19.C07

- `L19.C07/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L19.C08

- `L19.C08/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  endossement par la Commission de statistique.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »

### L19.C09

- `L19.C09/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  mondiale, *System of National Accounts 2008*.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 (cf. »
- `L19.C09/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : T5 (L19.C08, L19.C10) « même référence marquée T1 ailleurs »

### L19.C10

- `L19.C10/S1` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « onal Accounts 2025*, version pour endossement.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 par  »
- `L19.C10/S2` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « onal, *Statuts*, article XIX, sections 4 et 5.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-09 — `e »
- `L19.C10/S3` — ancienne date 2026-09-09 — file A, orientation vers ouverte — traces : T1 (reference) « ions*, Policy Papers, volume 2025, numéro 032.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-09 — `e »

### L2.C01

- `L2.C01/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C01/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C01/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « , **BIS Working Papers n° 128, février 2003**. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (b » ; T4 (corps) « « La macroprudence est apparue comme discipline institutionnelle distincte **après la crise financière de 2007-2008**. A »
- `L2.C01/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C02

- `L2.C02/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « isks of individual institutions; BOTTOM-UP »). **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L2.C02/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C02/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « closer to its origin, when the main concern was the disruption to the economic life of a country »**, et l'éloignerait »
- `L2.C02/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « est apparue comme discipline institutionnelle distincte après la crise financière de 2007-2008 »** [S4] »

### L2.C03

- `L2.C03/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ancial system has FIRST-ORDER EFFECTS on it. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « measures risk in terms of the dispersion of an economy's output »** [S1] »
- `L2.C03/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C03/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C03/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C04

- `L2.C04/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C04/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « **Toute politique macroprudentielle qui inverse cet ordre est structurellement condamnée.** »

::etat:: **Épisode 12** »
- `L2.C04/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « tialist would find this possibility NATURAL. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L2.C04/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C05

- `L2.C05/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « *CEPII Working Paper n° 2016-10, avril 2016**. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (c »
- `L2.C05/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C05/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « qualitative mandatory reserves at the central bank »** [S3] »
- `L2.C05/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « l'orientation implicite carbonée actuelle finance mécaniquement l'aggravation des risques systémiques »** [S4] »

### L2.C06

- `L2.C06/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « note de l'Institut Veblen, juin 2022**, 42 p. **OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (v »
- `L2.C06/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « recense vingt-cinq estimations dans cinq études réalisées entre 2014 et 2018, dont la majeure partie évalue **entre −0 »
- `L2.C06/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C06/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « ont prévalu jusque dans les années 1980, sous la forme de règles d'encadrement du crédit, de fléchage sectoriel, taux  »

### L2.C07

- `L2.C07/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  Aglietta**, C. Goodhart et T. Padoa-Schioppa. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (c »
- `L2.C07/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C07/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C07/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « L'architecture politique monétaire-politique macro-prudentielle doit être bâtie sur le **principe d'affectation des in »
- `L2.C07/S5` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L2.C08

- `L2.C08/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C08/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C08/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C08/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C09

- `L2.C09/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C09/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C09/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « in terms of the dispersion of an economy's output »** [S3] »
- `L2.C09/S5` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « Financial Stability Report*, **octobre 2023**. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (f » ; T2 (verifications_en_attente[1]) « LE *FINANCIAL STABILITY REPORT* A ÉTÉ OUVERT EN COURS DE RÉDACTION et la vérification est faite : voir S5. **La paginati » ; T4 (corps) « « An Approach to Assessing Climate-Related Financial Risks »** [S5] » ; T7 (verifications_en_attente[1]) « LE *FINANCIAL STABILITY REPORT* A ÉTÉ OUVERT EN COURS DE RÉDACTION et la vérification est faite : voir S5. **La paginati »
- `L2.C09/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C10

- `L2.C10/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C10/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C10/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « in part endogenous with respect to the behaviour of the financial system »** [S3] »
- `L2.C10/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C11

- `L2.C11/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « la Banque de France n° 229/8, mai-juin 2020**. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (p »
- `L2.C11/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « Une sécheresse majeure affecte simultanément l'agriculture, l'énergie hydroélectrique, la logistique fluviale, la sant »
- `L2.C11/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « **le concept de risque lui-même doit être réinterprété** » pour saisir la dimension systémique des risques climatiques »
- `L2.C11/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C12

- `L2.C12/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C12/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C12/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C12/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C13

- `L2.C13/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « capture par les intérêts établis, rigidité face aux changements de circonstances, désincitation à l'innovation » [S1] »
- `L2.C13/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C13/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C13/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C14

- `L2.C14/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C14/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « "**, autrement dit à agir **de manière préventive**. »

::etat:: **Et le rapport documente le renversement** [S2] »
- `L2.C14/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C15

- `L2.C15/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « une banque prudentiellement conforme **dans un territoire fragile** n'est pas prudentiellement solide » [S1] »
- `L2.C15/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C15/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C16

- `L2.C16/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « nulle ou négative — c'est-à-dire une création monétaire additionnelle »** [S1] »
- `L2.C16/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C16/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C16/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C17

- `L2.C17/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « et simultanément comme émetteur international [...] banque centrale néguentropique intrinsèquement multilatérale »** [ »
- `L2.C17/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C17/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C18

- `L2.C18/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C18/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « Le triangle de Mundell [...] **est contourné puisque le référentiel fixe une référence stable sans exiger la fixité de »
- `L2.C18/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C18/S5` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C18/S6` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C18/S7` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « exercise controls** » à peine d'inéligibilité. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (v »
- `L2.C18/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « action collective et des efforts de coordination sans précédent » sont requis** [S4] »

### L2.C19

- `L2.C19/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C19/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C19/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C20

- `L2.C20/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C20/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L2.C20/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L2.C21

- `L2.C21/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « " est le slogan qui résume la doctrine de la monnaie externe.** »

::etat:: **Pour la seconde** [S1] »
- `L2.C21/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C21/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C21/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C21/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L2.C22

- `L2.C22/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C22/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C22/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L2.C22/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « pour s'aligner sur les ratios déjà appliqués en moyenne » [S4] »
- `L2.C22/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L20.C01

- `L20.C01/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C01/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « à trancher avant tout exposé du mécanisme d'émission »** [S2] »
- `L20.C01/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C02

- `L20.C02/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « nt que les établissements privés de crédit] ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06**, P »
- `L20.C02/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « or the entities referred to in Article 21.1. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** * »
- `L20.C02/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C03

- `L20.C03/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  Communauté, tels que définis à l'article 2. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C03/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  **ARTICLE 3.1** : les missions fondamentales. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R » ; T4 (corps) « « **L'objectif principal** du SEBC est de maintenir **la stabilité des prix**. **Sans préjudice de** l'objectif de stabi »
- `L20.C03/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L20.C04

- `L20.C04/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « nale, avec le présent traité et les statuts. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C04/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  compatibilité sous le renvoi à l'article 109. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R »
- `L20.C04/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C05

- `L20.C05/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « BATION, PAR LA BCE, DU VOLUME DE L'ÉMISSION. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « sous réserve de l'approbation, par la BCE, du volume de l'émission »** [S1] »
- `L20.C05/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « status of LEGAL TENDER within the Community. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C05/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C06

- `L20.C06/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « leurs règles constitutionnelles respectives. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C06/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « HE N'EXIGE PAS L'AVIS CONFORME DU PARLEMENT.** **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C06/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  RATIFICATION PAR TOUS LES ÉTATS CONTRACTANTS. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « Le présent traité est conclu pour une **durée illimitée**. »

::etat:: **Article O** [S3] »
- `L20.C06/S4` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « nseil des gouverneurs à la majorité qualifiée. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « si elles imposent des obligations à des tiers »** [S4] »

### L20.C07

- `L20.C07/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  LA COMMUNAUTÉ, LA BCE ET LES ÉTATS MEMBRES. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « Par dérogation à l'article 228, au cas où des accords sur des questions se rapportant au **régime monétaire ou de chan »
- `L20.C07/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  À L'UNANIMITÉ, DÉCIDE DE SA REPRÉSENTATION. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C07/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C08

- `L20.C08/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « 'écarter de la parité de plus de UN POUR CENT. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** (F »
- `L20.C08/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C08/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C08/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C09

- `L20.C09/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « cation unless a shorter period is specified. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R »
- `L20.C09/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C09/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C10

- `L20.C10/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ALL BE MADE BY A MAJORITY OF THE VOTES CAST. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R » ; T4 (corps) « « Each member shall have **two hundred fifty votes plus one additional vote for each part of its quota equivalent to one »
- `L20.C10/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C10/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C11

- `L20.C11/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « tions, controls and moratoria of any nature ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C11/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C11/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  — **PROTOCOLE QUE LE CORPUS NE DÉTIENT PAS.** **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C11/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C12

- `L20.C12/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « S THAN TWO-THIRDS of the total voting power ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C12/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C12/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C13

- `L20.C13/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « vert à la signature jusqu'au 31 décembre 1945. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C13/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C13/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ch written notice of withdrawal is received. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** » ; T4 (corps) « « Any member may withdraw from the Fund **at any time** by transmitting a notice in writing [...] **Withdrawal shall bec »
- `L20.C13/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C14

- `L20.C14/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « HE PERMANENT COURT OF INTERNATIONAL JUSTICE. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C14/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « e pour les litiges entre la BCE et ses agents. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C14/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C15

- `L20.C15/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « de base géographique aussi large que possible. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C15/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C16

- `L20.C16/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « regulations and procedures of the Authority. » **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** —  » ; T4 (corps) « « **The Area and its resources are the common heritage of mankind.** »

::etat:: **Article 137 § 1** [S1] »
- `L20.C16/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « The Authority shall have **international legal personality** and such legal capacity as may be necessary for the exerc »
- `L20.C16/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C17

- `L20.C17/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « tention aux autres parties par le dépositaire. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R »
- `L20.C17/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C17/S4` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « E UNIVERSAL PARTICIPATION IN THE CONVENTION ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06**, R » ; T4 (corps) « « The provisions of this Agreement and Part XI shall be **interpreted and applied together as a single instrument**. **I »
- `L20.C17/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C18

- `L20.C18/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « eptés**, après acceptation par les deux tiers. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06** »
- `L20.C18/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « **This paragraph shall not be used in a manner that would undermine the amendment provisions in Article X.** »

::etat »
- `L20.C18/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C19

- `L20.C19/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « TO AFFORD PROTECTION TO DOMESTIC PRODUCTION ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06.** R »
- `L20.C19/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C19/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C19/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C20

- `L20.C20/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « s pièces jusqu'à la fin de la quatrième année. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06**, 2 »
- `L20.C20/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C20/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C20/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C21

- `L20.C21/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ous les cas à tout membre du grand public** ». **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06**, t » ; T4 (corps) « « **soient accessibles dans tous les cas à tout membre du grand public** » [S1] »
- `L20.C21/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « susceptible de justifier des ingérences, mêmes graves »** dans les droits en cause [S2] »
- `L20.C21/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C22

- `L20.C22/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C22/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C22/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C23

- `L20.C23/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L20.C23/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L20.C24

- `L20.C24/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ous le n° 20, *Recueil des traités*, volume 2.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu »
- `L20.C24/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « 20 dans la bibliothèque électronique du Fonds.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « Settlement of accounts with members withdrawing »** [S2] »
- `L20.C24/S3` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « blié sur le site officiel de la Banque mondiale. OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »

### L20.C25

- `L20.C25/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « E DES STATUTS DU FONDS ET SOUS LE MÊME NUMÉRO.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »

### L20.C26

- `L20.C26/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « blié sur le site officiel de la Banque mondiale. OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  »
- `L20.C26/S2` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune
- `L20.C26/S3` — ancienne date 2026-09-08 — file B, traces contradictoires — traces : T1 (reference) « ENTION « as amended effective June 27, 2012 ».** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T3 (verifications_en_attente[0]) « **L'ARTICLE IV EST LU DANS SES SECTIONS 1 ET 2, ET LE RESTE NE L'EST PAS** [S3]. Le corpus tient donc ce qui DÉCLENCHE u »

### L21.C01

- `L21.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « par quels bilans et quelles infrastructures une transaction mondiale devient-elle définitive »** [S3] »

### L21.C02

- `L21.C02/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L21.C03

- `L21.C03/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L21.C03/S2` — ancienne date 2026-09-07 — file B, traces contradictoires — traces : T1 (reference) « **PFMI, avril 2012, OUVERT PAR TÉLÉCHARGEMENT DIRECT — quatre principes » ; T3 (verifications_en_attente[2]) « **LE MOMENT LÉGALEMENT DÉFINI DU CARACTÈRE DÉFINITIF.** Le principe 8 renvoie à un moment défini par le droit [S2, note  »
- `L21.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « le prestataire est payé en monnaie nationale et n'en détient aucune » [S3] »

### L21.C04

- `L21.C04/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Banks must include ALL BALANCE SHEET ASSETS in their leverage ratio exposure measure** » [S1] »
- `L21.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C04/S3` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « sclosure requirements », janvier 2014, bcbs270 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07 depu »
- `L21.C04/S4` — ancienne date 2026-09-07 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[1]) « **LE RATIO DE LEVIER EST-IL LA CONTRAINTE MORDANTE, ET POUR QUI ?** Le § 4 établit que les réserves ne consomment pas de »
- `L21.C04/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L21.C05

- `L21.C05/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « *CLS Bank International Rules, 21 juillet 2025 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07 depu » ; T4 (corps) « « only if such currency satisfies **EACH** of the following criteria » [S1] »
- `L21.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L21.C06

- `L21.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « dès lors [qu'ils] considèrent que la désignation d'un tel système est justifiée **pour des raisons de risque systémiqu »
- `L21.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L21.C07

- `L21.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L21.C07/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L21.C08

- `L21.C08/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « rastructures*, avril 2012, ISBN 92-9131-108-1.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »

### L22.C01

- `L22.C01/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « ermediation 2025 », 16 décembre 2025, 91 pages — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07 depu » ; T4 (corps) « « **growing at DOUBLE THE PACE OF THE BANKING SECTOR** » [S1] »
- `L22.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Common asset holdings and overlapping portfolios exposes banks and non-bank financial institutions to CORRELATED VAL »
- `L22.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L22.C02

- `L22.C02/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « , 16 décembre 2025 — MÊME SOURCE QU'EN L22.C01, OUVERTE PAR TÉLÉCHARGEMENT DIRECT, données au 31 déc »
- `L22.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « n'appartiennent à aucun particulier dont la vie privée serait en cause »** [S2] »

### L22.C03

- `L22.C03/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **la protection et la RESTAURATION des écosystèmes terrestres et marins** » [S1] »
- `L22.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C03/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **la nécessité éventuelle de modifier le présent règlement** » [S4] »

### L22.C04

- `L22.C04/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **au moins une fois tous les dix ans** », à onze rubriques [S2] »
- `L22.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « À la suite de la vérification, le certificateur PUBLIE un rapport d'audit. »**

::etat:: **QUATRIÈME — LA GARANTIE DE  »
- `L22.C04/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L22.C05

- `L22.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **is ongoing even in countries that used to have a significant share of assets in DB plans** » [S2] »
- `L22.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L22.C06

- `L22.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **les critères régissant le choix des actifs sous-jacents, y compris, s'il y a lieu, TOUT CRITÈRE D'EXCLUSION D'ACTIFS »
- `L22.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **tout en garantissant la confidentialité et la protection des savoir-faire et des informations commerciales non divul »
- `L22.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L22.C06/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L22.C07

- `L22.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L23.C01

- `L23.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « qui peut lever le reflux et comment les capitaux peuvent l'éviter »** [S1] »
- `L23.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « L'alignement d'intérêts qui fait tenir l'instrument existant est exactement ce que le dispositif retire. »**

::etat:: »
- `L23.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L23.C02

- `L23.C02/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « opération internationale en matière fiscale**. **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** pa »
- `L23.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C02/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « l'adversaire ne s'oppose pas au texte : il en négocie les remèdes »** [S4] »

### L23.C03

- `L23.C03/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « nvention on International Tax Cooperation*** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** su »
- `L23.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C03/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L23.C04

- `L23.C04/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « es C-37/20 et C-601/20, ECLI:EU:C:2022:912** — **OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L23.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « sur quelle assiette RÉELLEMENT ATTEIGNABLE ? »**, en nommant les bénéficiaires effectifs parmi les objets à instruire  »

### L23.C05

- `L23.C05/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « e l'Union**, JO L 424/1 du 15 décembre 2020 — **OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, t »
- `L23.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L23.C06

- `L23.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C06/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L23.C07

- `L23.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L23.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « qui peut lever le reflux ET COMMENT LES CAPITAUX PEUVENT L'ÉVITER »** [S2] »
- `L23.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C01

- `L24.C01/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) «  Advances, vol. 9, eadh2458, 13 septembre 2023 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07 depu » ; T4 (corps) « « **delineate and quantify levels of anthropogenic perturbation that, if respected, would allow Earth to remain in a “Ho »
- `L24.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L24.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « if sufficiently transgressed, could, ON ITS OWN, alter Earth system state »** [S3] »
- `L24.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C02

- `L24.C02/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « , Nature, vol. 619, p. 102-111, 6 juillet 2023 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07 depu » ; T4 (corps) « « The STRICTER of the safe or just boundaries sets the integrated safe and just ESB. »** [S1] »
- `L24.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « The STRICTER of the safe or just boundaries sets the integrated safe and just ESB. »** [S1]

::etat:: **Trois critères »
- `L24.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L24.C02/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C03

- `L24.C03/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L24.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **far exceeding what is required to meet essential human needs for all in line with the SDGs** » [S2] »
- `L24.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « a core element of any global sustainability effort »** [S3] »
- `L24.C03/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C04

- `L24.C04/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « 11, 6 juillet 2023 — MÊME SOURCE QU'EN L24.C02, OUVERTE PAR TÉLÉCHARGEMENT DIRECT, CC BY 4.0, régime »
- `L24.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **the REDISTRIBUTION of nutrients from OVER-FERTILIZED to UNDER-FERTILIZED regions** » [S2] »
- `L24.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T5 (L24.C01) « même référence marquée T1 ailleurs »
- `L24.C04/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C05

- `L24.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L24.C06

- `L24.C06/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  Resources*, volume 45, 2020, pages 497 à 521.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L » ; T4 (corps) « « who is deciding on the precise values of boundaries that are to be protected ? »*

::etat:: **Et l'enjeu est identifié »

### L24.C07

- `L24.C07/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « tsdam pour la recherche sur l'impact climatique. OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, **L » ; T4 (corps) « « translate Planetary Boundaries to the scale of specific products, services, and systems, and convert quantified resour »

### L25.C01

- `L25.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **In no case may a people be deprived of its own means of subsistence** » [S1] »
- `L25.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « the essential importance of international co-operation based on free consent » [S2] »
- `L25.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C02

- `L25.C02/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « in which **any significant number of individuals is deprived of essential foodstuffs, of essential primary health care »
- `L25.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C02/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C03

- `L25.C03/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **eu égard à la nécessité de prévoir des ressources d'origine PUBLIQUE et SOUS FORME DE DONS pour l'adaptation** » [S1 »
- `L25.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C04

- `L25.C04/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **le manque d'accès aux services énergétiques essentiels au maintien d'un niveau décent de vie et de santé** » [S2] »
- `L25.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C04/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C05

- `L25.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L25.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C06

- `L25.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L25.C07

- `L25.C07/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L26.C01

- `L26.C01/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T4 (corps) « « identifier les critiques adressées à l'application du second principe à l'économie, notamment sur le statut de la Terr » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »
- `L26.C01/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « l Resources, Fontainebleau, mai 1998, 10 pages — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **The “fourth law” has no status in physics** » [S2] » ; T6 (git) « date 2026-09-08 postérieure à la création 2026-09-07 »

### L26.C02

- `L26.C02/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « , février 2026, 233 pages, DOI 10.3133/mcs2026 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **that part of the reserve base that could be ECONOMICALLY extracted or produced AT THE TIME OF DETERMINATION** » [S1] »

### L26.C03

- `L26.C03/S1` — ancienne date 2026-09-08 — file B, traces contradictoires — traces : T1 (reference) «  9 juin 2022, 19 pages, DOI 10.3390/su14127098 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T2 (verifications_en_attente[0]) « **UNE CONTESTATION EXISTE ET LE CORPUS N'EN A PAS OUVERT LE TEXTE.** Le groupe de recherche auteur de S2 a publié une no » ; T3 (verifications_en_attente[0]) « **UNE CONTESTATION EXISTE ET LE CORPUS N'EN A PAS OUVERT LE TEXTE.** Le groupe de recherche auteur de S2 a publié une no » ; T4 (corps) « « **as the energy “cost” of the processes to get most thermal fuels from extraction to point of use DRASTICALLY LOWERS t »
- `L26.C03/S2` — ancienne date 2026-09-08 — file B, traces contradictoires — traces : T1 (reference) « 12 juin 2020, 43 pages, DOI 10.3390/en13123036 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T2 (verifications_en_attente[0]) « **UNE CONTESTATION EXISTE ET LE CORPUS N'EN A PAS OUVERT LE TEXTE.** Le groupe de recherche auteur de S2 a publié une no » ; T3 (verifications_en_attente[0]) « **UNE CONTESTATION EXISTE ET LE CORPUS N'EN A PAS OUVERT LE TEXTE.** Le groupe de recherche auteur de S2 a publié une no » ; T3 (verifications_en_attente[1]) « **BROCKWAY ET AL. (2019) N'EST PAS OUVERT DIRECTEMENT.** Cette étude est l'estimation mondiale du rendement énergétique  » ; T4 (corps) « « **Only large hydroelectricity would currently have a high EROIext ~ 6.5:1, while the rest of variable RES would be BEL »

### L26.C04

- `L26.C04/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ble Energy Reviews*, vol. 141, n° 110781, 2021 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **relies upon few a-priori assumptions** » [S1] »

### L26.C05

- `L26.C05/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « hèse, ISSN 2978-0950, © Energy Institute 2026 — OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu » ; T4 (corps) « « **Total energy supply EXCEEDED 600 EJ in 2025, a rise of 1.7 % over 2024, continuing the LONG-TERM UPWARD TREND in ene »

### L26.C06

- `L26.C06/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L26.C07

- `L26.C07/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « nal*, vol. 41, n° 3, janvier 1975, p. 347-381.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »
- `L26.C07/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  4, 2009, p. 1195-1225, doi:10.3390/su1041195.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  » ; T4 (corps) « « the generic, but vague or ill-defined, application of entropy to various kinds of disorder »* [S2] »

### L26.C08

- `L26.C08/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : T5 (L26.C03) « même référence marquée T1 ailleurs »
- `L26.C08/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « , *Sustainability*, 3(10), 2011, p. 1796-1809.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »

### L26.C09

- `L26.C09/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « urce Efficiency Rebound Effects*, 2026, 118 p.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »
- `L26.C09/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « arch Centre, octobre 2007, ISBN 1-903144-0-35.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »

### L26.C10

- `L26.C10/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ssible? », *PLoS ONE*, 11(10), e0164733, 2016.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »
- `L26.C10/S2` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « ronmental Research Letters*, 15, 063002, 2020.** OUVERT PAR TÉLÉCHARGEMENT DIRECT, lu dans le texte  »

### L26.C11

- `L26.C11/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) « e de la British Institute of Energy Economics.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08, lu  » ; T4 (corps) « « La quatrième frontière demandée — le service final — n'est couverte par aucune des deux sources, qui s'arrêtent au poi »

### L26.C12

- `L26.C12/S1` — ancienne date 2026-09-08 — file A, orientation vers ouverte — traces : T1 (reference) «  vol. 48, p. 9874−9881, DOI 10.1021/es501217t.** OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-08 depu »

### L26.C13

- `L26.C13/S1` — ancienne date 2026-09-08 — file D, sans orientation — traces : aucune

### L3.C01

- `L3.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « réserver l'étude institutionnelle détaillée des banques centrales au Livre 10 »** [S1] »
- `L3.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Il n'existe aucun canal de création monétaire qui ne soit gagé, à un niveau ou à un autre, sur une promesse de rembo »
- `L3.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C01/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C02

- `L3.C02/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C02/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « such controls as are necessary to **regulate international capital movements** » [S3] »
- `L3.C02/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C03

- `L3.C03/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « instauration de **l'étalon de change dollar-or** », création du Fonds [S1] »
- `L3.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « parce qu'elle commande la position de l'émetteur pivot, **qui est le seul à devoir régler en or et le seul à pouvoir m »

### L3.C04

- `L3.C04/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L3.C04/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L3.C04/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L3.C04/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « ne désigne pas l'argument quantitatif *plus de monnaie, plus d'extraction*, que les séries monétaires réfutent » [S5] »
- `L3.C04/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C04/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « identifier le moment où la charge excède l'avantage », tenue pour **la seule plus solide que l'attente d'une fenêtre** »

### L3.C05

- `L3.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C06

- `L3.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « les règles et les mécanismes assurant la fourniture de liquidités en devises en cas de besoin », que la source nomme l »
- `L3.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Un pays qui ne détient plus de réserves de change suffisantes rencontre des difficultés, par exemple pour payer ses im »
- `L3.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C06/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C07

- `L3.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C07/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C08

- `L3.C08/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C08/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C08/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C08/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C09

- `L3.C09/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C09/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C09/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L3.C10

- `L3.C10/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L3.C10/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C01

- `L5.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C01/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C01/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C01/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C02

- `L5.C02/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C02/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C02/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « une monnaie doit être acceptée pour valoir, **un rail doit seulement être joignable** » [S3] »

### L5.C03

- `L5.C03/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C03/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C03/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **objective, risk-based, and publicly disclosed** », permettant « **fair and open access** » [S3] »

### L5.C04

- `L5.C04/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C04/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « la convention de 1998 sur le même objet n'est jamais entrée en vigueur. »**

::etat:: **Le troisième** [S2] »
- `L5.C04/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C05

- `L5.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C06

- `L5.C06/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C06/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C07

- `L5.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C08

- `L5.C08/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C08/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C08/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L5.C09

- `L5.C09/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C09/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C09/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « well-founded, clear, transparent, and enforceable [...] IN ALL RELEVANT JURISDICTIONS »** [S3] »

### L5.C10

- `L5.C10/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C10/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L5.C10/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C01

- `L6.C01/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C01/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C01/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C01/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « C'est le livre qui doit établir ce que L1.C18 ne fait qu'énoncer. »

::etat:: **Et il a contracté une dette le jour mê »

### L6.C02

- `L6.C02/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « **Le récit ne doit jamais fondre ces cinq strates en un chiffre unique.** »

::etat:: **Avec deux précisions qui montr »
- `L6.C02/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C02/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L6.C03

- `L6.C03/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C03/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C03/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C03/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L6.C04

- `L6.C04/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C04/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C04/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L6.C04/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L6.C05

- `L6.C05/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C05/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C05/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C05/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C05/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C06

- `L6.C06/S1` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) «  2017, entrée en vigueur le 13 décembre 2017. **OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** —  » ; T4 (corps) « « considerato come comproprietà inter-generazionale »** [S1] »
- `L6.C06/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S10` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S8` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S9` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S7` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C06/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C07

- `L6.C07/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « le maintien, la conservation, la gestion ou la restauration d'éléments de la biodiversité **ou de services écosystémiq »
- `L6.C07/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C07/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C07/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « incluant le cas échéant la démolition de l'ensemble des installations, **y compris celles réalisées par le preneur** » »
- `L6.C07/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Si la procédure d'expropriation s'accompagne d'une indemnisation du propriétaire, **son objet principal est de priver  »
- `L6.C07/S7` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C07/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C08

- `L6.C08/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « les substances dites de mine sont **concédables par l'État indépendamment de la propriété du sol** », tandis que les s »
- `L6.C08/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « ne peut être contestée à l'appui d'un recours dirigé contre l'acte accordant la dérogation »** [S2] »
- `L6.C08/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C08/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C08/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C08/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C09

- `L6.C09/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « le peuple autochtone ou la communauté locale ayant fourni le savoir traditionnel associé »** [S1] »
- `L6.C09/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C09/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C09/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « tardé à engager la délimitation foncière et la révision de sa législation minière »** [S4] »
- `L6.C09/S6` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « ditionnels associés, Genève, 24 mai 2024 — TEXTE OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07**, d »
- `L6.C09/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C10

- `L6.C10/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « le législateur est fondé à tenir compte des effets que les activités exercées en France peuvent porter à l'environneme »
- `L6.C10/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Distinguer le but d'intérêt général, qui JUSTIFIE UNE ATTEINTE, de l'objectif de valeur constitutionnelle, qui ENTRE »
- `L6.C10/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C10/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C10/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « pour des raisons tenant au droit de la concurrence, **l'étude n'intègre ni les prix des contrats ni la surprime** » [S »
- `L6.C10/S7` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « n des industries de la protection des plantes*. OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** —  »
- `L6.C10/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C11

- `L6.C11/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C11/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « d'agir de manière à préserver autant que possible les systèmes écologiques et la biodiversité indigènes, à valoriser e »
- `L6.C11/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Les gardiens participent au contrôle ; ils ne poursuivent pas. »** [S3] »
- `L6.C11/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C11/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Un représentant est tenu par l'intérêt de son représenté et **lui rend compte**. Un demandeur habilité poursuit **son  »
- `L6.C11/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Le droit des personnes morales la pratique couramment sous le nom de **mandataire ad hoc**, chaque fois qu'un dirigean »
- `L6.C11/S8` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C11/S7` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L6.C12

- `L6.C12/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C12/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Vingt ans, en matière climatique, n'est plus une durée acceptable. C'est la durée du problème lui-même.** » [S2] »
- `L6.C12/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C12/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C12/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « Au 29 août 2026, **l'engagement d'une nouvelle procédure est documenté ; son enregistrement formel ne l'est pas.** » [ »
- `L6.C12/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **ce qui ne prouve pas qu'il n'y en ait pas** » — et interdit de retenir « 300 millions » comme valeur unique [S6] »
- `L6.C12/S7` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C12/S11` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C12/S10` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) «  Lisbonne, 17 décembre 1994 — TEXTE AUTHENTIQUE. OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** :  »
- `L6.C12/S9` — ancienne date 2026-09-07 — file A, orientation vers ouverte — traces : T1 (reference) « e Vienne sur le droit des traités, 23 mai 1969. OUVERTE PAR TÉLÉCHARGEMENT DIRECT le 2026-09-07** —  »
- `L6.C12/S8` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « pèse plus lourd, dans la marche des choses, que les rares condamnations qui la nourrissent »** [S8] »

### L6.C13

- `L6.C13/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C13/S2` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « **Ne jamais écrire que la révision a supprimé l'accès aux preuves. Elle a supprimé le régime de responsabilité qui l'e »
- `L6.C13/S3` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C13/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C13/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune
- `L6.C13/S6` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

### L7.C01

- `L7.C01/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L7.C01/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C02

- `L7.C02/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  Nations unies, Bretton Woods, 22 juillet 1944 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (tir »
- `L7.C02/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « mondiale du commerce, Marrakech, 15 avril 1994 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (wto »
- `L7.C02/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  centrales et de la Banque centrale européenne — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (ecb »
- `L7.C02/S4` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L7.C03

- `L7.C03/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L7.C03/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C04

- `L7.C04/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C04/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C05

- `L7.C05/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « définit les catégories d'activités régénératives éligibles » — **D1** — et elle « **fixe le barème des impacts** » [S1 »
- `L7.C05/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C06

- `L7.C06/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C06/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C06/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « commerce, Marrakech, 15 avril 1994, article IX — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06, dép »

### L7.C07

- `L7.C07/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C07/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « l'écart entre l'indicateur et l'effet est **plus grand**, puisqu'il n'existe pas de métrologie établie de la régénérat »
- `L7.C07/S3` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  of Political Economy, 85(3), 1977, p. 473-492 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06, dép »

### L7.C08

- `L7.C08/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « réunit les représentants des banques centrales participantes »** [S1] »
- `L7.C08/S2` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[0]) « ROGOFF 1985 N'EST PAS OUVERT. Le corpus n'en tient que la mention faite par [S2], qui est une synthèse pédagogique de ra »
- `L7.C08/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C09

- `L7.C09/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « est le seul mécanisme qui protège simultanément les petits et les nombreux »** [S1] »
- `L7.C09/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L7.C09/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C10

- `L7.C10/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C10/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L7.C10/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C11

- `L7.C11/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C11/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L7.C11/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « une dotation pluriannuelle sanctuarisée, soustraite au vote budgétaire annuel » [S3] »

### L7.C12

- `L7.C12/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C12/S2` — ancienne date 2026-09-06 — file B, traces contradictoires — traces : T1 (reference) « u Fonds monétaire international, texte de 1944 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06, dép » ; T2 (verifications_en_attente[1]) « AUCUN PRÉCÉDENT DE FINANCEMENT D'AMORÇAGE D'ORGANISATION INTERNATIONALE N'EST OUVERT — souscriptions initiales, contribu » ; T3 (verifications_en_attente[1]) « AUCUN PRÉCÉDENT DE FINANCEMENT D'AMORÇAGE D'ORGANISATION INTERNATIONALE N'EST OUVERT — souscriptions initiales, contribu »
- `L7.C12/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C13

- `L7.C13/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C13/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C14

- `L7.C14/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C14/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C15

- `L7.C15/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « l'océan, les forêts primaires, la biodiversité, et même l'atmosphère » [S1] »
- `L7.C15/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C16

- `L7.C16/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « en dessous duquel il ne fonctionne pas »** [S1] »
- `L7.C16/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « licy », American Economic Review, 105(4), 2015 — ACQUIS PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (98  »
- `L7.C16/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C17

- `L7.C17/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  2015, p. 1339-1370 (DOI 10.1257/aer.15000001) — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06, tex »
- `L7.C17/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C18

- `L7.C18/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « est déformé par l'annonce même du barème qu'il doit servir à calibrer » [S1] »
- `L7.C18/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C19

- `L7.C19/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « sanctionne les manquements des trois chambres » et ses décisions « s'imposent à l'ensemble des organes du GES » [S1] »
- `L7.C19/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « lubs », American Economic Review, 105(4), 2015 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06, dép »
- `L7.C19/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L7.C20

- `L7.C20/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  commerce, Marrakech, 15 avril 1994, article X — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06. RÉG »
- `L7.C20/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C20/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « to become effective only after a 2-year delay », ce qui rend « discretionary policy all but impossible » [S3] »

### L7.C21

- `L7.C21/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « réunit les représentants des banques centrales participantes »** [S1] »
- `L7.C21/S4` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « are [...] associated with **net wealth transfers to the rest of world in global crisis times** [...] These wealth tran » ; T6 (git) « date 2026-09-07 postérieure à la création 2026-09-06 »
- `L7.C21/S5` — ancienne date 2026-09-07 — file D, sans orientation — traces : T4 (corps) « « with **the decline of the relative size of the United States in the world economy**, [...] **a new Triffin dilemma may » ; T6 (git) « date 2026-09-07 postérieure à la création 2026-09-06 »
- `L7.C21/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « orld Venture Capitalist », NBER WP 11563, 2005 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 : «  »

### L7.C22

- `L7.C22/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L7.C22/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C01

- `L8.C01/S1` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L8.C01/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune
- `L8.C01/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C02

- `L8.C02/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C03

- `L8.C03/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C04

- `L8.C04/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C05

- `L8.C05/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C06

- `L8.C06/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C07

- `L8.C07/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C08

- `L8.C08/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C09

- `L8.C09/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C10

- `L8.C10/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C11

- `L8.C11/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ture and Causes of the Wealth of Nations, 1776 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro »
- `L8.C11/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C12

- `L8.C12/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ciples of Political Economy and Taxation, 1817 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro » ; T4 (corps) « « ORIGINAL AND INDESTRUCTIBLE POWERS OF THE SOIL »** [S1] »
- `L8.C12/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C13

- `L8.C13/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  An Essay on the Principle of Population, 1798 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro » ; T4 (corps) « « **Population, when unchecked, increases in a GEOMETRICAL ratio** », les subsistances n'augmentant que dans un rapport  »
- `L8.C13/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C14

- `L8.C14/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « une expression technique d'une politique saine » [S1] »

### L8.C15

- `L8.C15/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « S. Mill, Principles of Political Economy, 1848 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro » ; T4 (corps) « « Stationary state of wealth and population **dreaded by some writers, but NOT IN ITSELF UNDESIRABLE** » [S1] »
- `L8.C15/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C16

- `L8.C16/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C17

- `L8.C17/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « ion to the Critique of Political Economy, 1859 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro » ; T4 (corps) « « **the abstract and general form of all antagonisms with which the capitalistic system of labor is pregnant** » [S1] »
- `L8.C17/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C18

- `L8.C18/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) «  Veblen, The Theory of the Leisure Class, 1899 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (Pro » ; T4 (corps) « « **conspicuous consumption of valuable goods is a means of reputability** » [S1] »
- `L8.C18/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C19

- `L8.C19/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune

### L8.C20

- `L8.C20/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C21

- `L8.C21/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « arrêtée par décision et non par un marché » [S1] »

### L8.C22

- `L8.C22/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « the values of the instrument variables are dependent, generally speaking, **on all the targets set and cannot be consi »

### L8.C23

- `L8.C23/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C24

- `L8.C24/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « , Econometrica, 1(4), octobre 1933, p. 337-357 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (tir » ; T4 (corps) « « THE MORE THE DEBTORS PAY, THE MORE THEY OWE. »** [S1] »
- `L8.C24/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C25

- `L8.C25/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L8.C25/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « 'exécution portant sur les VALEURS PAR DÉFAUT — OUVERTS PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (EUR »

### L8.C26

- `L8.C26/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « Theory of Employment, Interest and Money, 1936 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (tir »
- `L8.C26/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C27

- `L8.C27/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **whether it is a credit or a debit balance** » [S1] »
- `L8.C27/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L8.C27/S3` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L8.C28

- `L8.C28/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « in the form of **conditions** [...] since they are **not in themselves elements of well-being but rather technical exp »
- `L8.C28/S2` — ancienne date 2026-09-05 — file D, sans orientation — traces : T4 (corps) « « will ultimately lead to the breakdown of the fixed exchange system » [S2] »

### L8.C29

- `L8.C29/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **the knowledge of the circumstances of which we must make use never exists in concentrated or integrated form, but so »
- `L8.C29/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **a single governmental unit to solve global collective action problems is inherently weak because of free-rider probl »
- `L8.C29/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C30

- `L8.C30/S1` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[2]) « ROGOFF 1985 EST CITÉ PAR [S1] ET N'EST PAS OUVERT, alors que le « banquier central conservateur » est exactement la form » ; T4 (corps) « « si les cycles d'activité sont courts et si les délais d'efficacité de la politique monétaire sont longs, alors une pol »
- `L8.C30/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : T4 (corps) « « indicate how the political parameters have to be varied in relation to the changing data » [S2] »
- `L8.C30/S3` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C31

- `L8.C31/S1` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « olitical Economy, 85(3), juin 1977, p. 473-492 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (tir » ; T4 (corps) « « In effect this is an argument for rules rather than discretion, but, **unlike Friedman's (1948) argument, it does not  »
- `L8.C31/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « nce Series on Public Policy, 1, 1976, p. 19-46 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06 (tir » ; T2 (verifications_en_attente[0]) « LE TIRAGE DE LUCAS 1976 EST UNE RECONNAISSANCE OPTIQUE FAUTIVE [S2]. Le titre sort en « ECONOMETRIC POEICY EVALUATION »  » ; T4 (corps) « « **For the question of the short-term forecasting, or tracking ability of econometric models, we have seen that this co »
- `L8.C31/S3` — ancienne date 2026-09-05 — file C, orientation vers candidate — traces : T3 (verifications_en_attente[1]) « LA LITTÉRATURE EMPIRIQUE POSTÉRIEURE À 1990 N'EST PAS TOUCHÉE. [S3] établit que le débat empirique a eu lieu dans les an » ; T4 (corps) « « All you have to do in this country right now is scream mindlessly, *Lucas critique !* and the conversation ends » [S3] »
- `L8.C31/S4` — ancienne date 2026-09-05 — file D, sans orientation — traces : aucune

### L8.C32

- `L8.C32/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C33

- `L8.C33/S1` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L8.C33/S2` — ancienne date 2026-09-04 — file D, sans orientation — traces : T4 (corps) « « **single policies adopted only at a global scale are unlikely to generate sufficient trust among citizens and firms so »
- `L8.C33/S3` — ancienne date 2026-09-04 — file D, sans orientation — traces : aucune
- `L8.C33/S4` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C34

- `L8.C34/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C35

- `L8.C35/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C36

- `L8.C36/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L8.C36/S2` — ancienne date 2026-09-06 — file A, orientation vers ouverte — traces : T1 (reference) « olitical Economy, 85(3), juin 1977, p. 473-492 — OUVERT PAR TÉLÉCHARGEMENT DIRECT le 2026-09-06. Ret »

### L8.C37

- `L8.C37/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C38

- `L8.C38/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C39

- `L8.C39/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C40

- `L8.C40/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L8.C41

- `L8.C41/S1` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune
- `L8.C41/S2` — ancienne date 2026-09-06 — file D, sans orientation — traces : aucune

### L9.C01

- `L9.C01/S1` — ancienne date 2026-09-07 — file D, sans orientation — traces : aucune

