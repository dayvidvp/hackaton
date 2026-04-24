# KB — F&O Create or update customer

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Create or update customer.docx`
**Conversiedatum:** 2026-04-24

---

All customers must be created or updated in AX3.

When the relation is ACTIVE, the information will be interfaced to D365.

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="3.4833333333333334in"}

When you are activating or creating a customer for MIC in AX3, the customer will become available in D365.

Upon creation or update, ALL the interfaced fields will be updated. Do not make changes directly in D365 because they will be overwritten upon an update from AX3!

Important for correct functionality in D365:

- Sales (order) pool = customer service responsible for the customer, often used as a filter in D365.

- Mode of delivery = please only select modes of delivery that exist in D365, they are important for the creation of correct outbound loads.

- Payment terms = keep in mind that there are credit management rules set up in D365 for specific payment terms.

- Sales line discount group = please only selects groups that exist In D365 (and In the conversion table)

Power BI report with sales representative Information:

The field Purpose In AX Is not Interfaced to D365. After migration to D365, the customer report In Power BI will have the Infor from the Sales group and the Sales order pool In D365. Make sure to transfer the Information from Purpose to Sales group or Sales order pool In AX. These will be Interfaced to D365. Discuss with the Power BI support team how you want to visualize the Info.

The only information that is managed in D365 directly is:

- Document text (ex. Recupel/EURO ACCOUNT)

- Documents texts on order confirmation, invoice, delivery note, etc. (Interfaced only once upon creation!)

- Warnings and notes

- Alt. addresses like delivery address or Invoice address

- Franco (needs to be added in D365 as free shipping threshold)

Specifics can be found here: [Manual Interfaces Relaties.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/MicronD365FOProject/Shared%20Documents/Processen/Relatie%20(MD)/Manual%20Interfaces%20Relaties.docx?d=w887b3e6858024969b476c3ad09267c56&csf=1&web=1&e=eyz9fc)

**[Stopped status conversion AX \> D365]{.underline}**

  -------------------------------------------------------------------------------------------------------------------------------------------------
  **[AX3 ]{.underline}**    **[No ]{.underline}**   **[All ]{.underline}**   **[All but picking list ]{.underline}**   **[Invoice ]{.underline}**
  ------------------------- ----------------------- ------------------------ ----------------------------------------- ----------------------------
  **[D365 ]{.underline}**   **[No ]{.underline}**   **[All ]{.underline}**   **[All ]{.underline}**                    **[Invoice ]{.underline}**

  -------------------------------------------------------------------------------------------------------------------------------------------------

**[Examples Mode of delivery conversion KEN (06/08/2024)]{.underline}**

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

**[Fill in the Sales group (external sales responsible) and the Sales order pool (internal sales responsible)]{.underline}**

![A screenshot of a computer Description automatically generated](media/image3.png){width="3.4594302274715663in" height="2.023096019247594in"}
