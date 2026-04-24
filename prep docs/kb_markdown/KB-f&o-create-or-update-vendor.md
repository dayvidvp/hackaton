# KB — F&O Create or update vendor

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Create or update vendor.docx`
**Conversiedatum:** 2026-04-24

---

All vendors must be created or updated in AX3.

When the relation is ACTIVE, the information will be interfaced to D365.

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="3.4833333333333334in"}

When you are activating or creating a vendor for MIC in AX3, the vendor will become available in D365.

Upon creation or update, ALL the interfaced fields will be updated. Do not make changes directly in D365 because they will be overwritten upon an update from AX3!

The only information that is managed in D365 directly is:

- Document text (ex. Recupel)

- Documents texts on purchase order and reception journal. (Interfaced only once upon creation!)

- Warnings and notes

- Delivery addresses

- Responsibilities for purchase invoice approval

(pushed by Vendor type but can be changed on Vendor level)

![](media/image3.png){width="6.268055555555556in" height="1.1868055555555554in"}

Specifics can be found here: [Manual Interfaces Relaties.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/MicronD365FOProject/Shared%20Documents/Processen/Relatie%20(MD)/Manual%20Interfaces%20Relaties.docx?d=w887b3e6858024969b476c3ad09267c56&csf=1&web=1&e=eyz9fc)

**[Stopped status conversion AX \> D365]{.underline}**

  -------------------------------------------------------------------------------------------------------------------------------------------------
  **[AX3 ]{.underline}**    **[No ]{.underline}**   **[All ]{.underline}**   **[All but picking list ]{.underline}**   **[Invoice ]{.underline}**
  ------------------------- ----------------------- ------------------------ ----------------------------------------- ----------------------------
  **[D365 ]{.underline}**   **[No ]{.underline}**   **[All ]{.underline}**   **[All ]{.underline}**                    **[Invoice ]{.underline}**

  -------------------------------------------------------------------------------------------------------------------------------------------------

**[Mode of delivery conversion KEN (06/08/2024)]{.underline}**

+---------------------------------------------+---------------------------------------------+
| AX3                                         | D365 1601 KEN                               |
+:=====================+:=====================+:=====================+:=====================+
| **Mode of delivery** | **Description**      | **Mode of delivery** | **Description**      |
+----------------------+----------------------+----------------------+----------------------+
| 3                    | DPD                  | DPD-STD              | DPD STD              |
+----------------------+----------------------+----------------------+----------------------+
| 17                   | Post                 | PST-STD              | POST STANDARD        |
+----------------------+----------------------+----------------------+----------------------+
| 128                  | TNT 24hr             | TNT-24H              | TNT 24H              |
+----------------------+----------------------+----------------------+----------------------+
| 130                  | TNT Timed            | TNT-TIM              | TNT TIMED            |
+----------------------+----------------------+----------------------+----------------------+
| 198                  | DPD 24HR             | DPD-24H              | DPD 24H              |
+----------------------+----------------------+----------------------+----------------------+
| 199                  | DPD BAG              | DPD-BAG              | DPD BAG              |
+----------------------+----------------------+----------------------+----------------------+
| 302                  | Divers \|            | DIV-STD              | DIV-STD DIVERS       |
+----------------------+----------------------+----------------------+----------------------+
| 304                  | Exworks \|           | EXW-STD              | EXWORKS STD          |
+----------------------+----------------------+----------------------+----------------------+
| COLLECTION           | Collection \|        | COL-STD              | COLLECTION STD       |
+----------------------+----------------------+----------------------+----------------------+
| 323                  | DPD Timed            | DPD-TIM              | DPD TIMED            |
+----------------------+----------------------+----------------------+----------------------+
| 324                  | Post Recorded        | PST-REC              | POST RECORDED        |
+----------------------+----------------------+----------------------+----------------------+
| 325                  | Pallet Network Timed | PAL-TIM              | PALLET NETWORK TIMED |
+----------------------+----------------------+----------------------+----------------------+
| 326                  | Pallet Network 24H   | PAL-24H              | PALLET NETWORK 24H   |
+----------------------+----------------------+----------------------+----------------------+
| 327                  | Pallet Network 48H   | PAL-48H              | PALLET NETWORK 48H   |
+----------------------+----------------------+----------------------+----------------------+
| DIV-EXP              | Divers Export        | DIV-EXP              | Divers Export        |
+----------------------+----------------------+----------------------+----------------------+
| EXW-EXP              | Exworks Export       | EXW-EXP              | Exworks Export       |
+----------------------+----------------------+----------------------+----------------------+
