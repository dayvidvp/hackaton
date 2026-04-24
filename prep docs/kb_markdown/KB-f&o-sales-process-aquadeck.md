# KB — F&O Sales Process Aquadeck

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales Process Aquadeck.docx`
**Conversiedatum:** 2026-04-24

---

**Sales Process AQUADECK**

![](media/image1.png){alt="Personalized Content Solution | Content Personalization | PathFactory ..." width="0.84375in" height="0.84375in"}

1.  **Process the SO** created from Hive or create SO manually (**All sales orders** and click on **+New)**:

    - Check mode of delivery\*: Important for outbound load.

    - Change VAT code\*\* If needed.

    - Add ordered Items in correct quantities.(manual orders)

    - Add a transport with cost and sales price. (Easy to do by typing \"TP\" In Item number field)

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.298611111111111in" height="1.9854166666666666in"}

- Add confirmed ship date based on load advice and customer wishes.

2.  Hive project: **Create and Estimate production** order : automatic batch every 10 minutes

3.  Hive project: **Schedule production** order in **Production planning hub**: automatic batch today +15 days. to make sure there Is a stock requirement for purchasing In MRP.

    - Run specific Aquadeck logic for reservations via Sequence \> Re-sort sequence & batch *(Button will be renamed)*

    - Schedule via manual batch. All sub-production orders will be scheduled as well based on capacity and worktime.

4.  **Release production** orders for different resources + provide lists to warehouse people

- BOX: All boxes that will be consolidated In the report need to be released. (Ex. 1 week)

- SLAT1/SLAT2: Everything released will be consolidated in the picking. Only release Is you want the slates to be picked and put at the LAM-IN.

- MAN: Can be released at the same time as the SLAT1/SLAT2 but the physical slats first need to go through SLAT1/SLAT2 before they can be used at MAN.

- SLATS: Assembly in the box. Automatic release after first steps are ready.

- ZABO: Anything you want to produce needs to be released. No need to wait for other productions.

- TUBE: Automatic release after ZABO.

- LASC: Anything you want to produce needs to be released. No need to wait for other productions.

- FINCON: Anything you want to produce needs to be released. No need to wait for other productions.

- OUT: Automatic release after all the sub-productions are finished.

5.  **Send order confirmation** to the customer. (Validation of credit status & markups)

    - Check scheduled date on resource A-OUT (main Hive project Item) to confirm the estimated delivery date to the customers. Who? How? Communication?

    - Immediately manual or at specific moment In batch based on checkbox \"Send confirmation\"

6.  Process **credit management hold list** if a customer is blocked/overdue/PP.

7.  **Production** of HIVE project Item:

    - Process production orders In the warehouse via Tulip:

      - Work station 1.1: BOX (Total list for week)

      - Work station 2: SLAT1

      - Work station 3: SLAT2

      - Work station 4: MAN

      - Work station 1.2: SLATS

      - Work station 5.1: ZABO

      - Work station 5.2: TUBE

      - Work station 6.1: LASC (Welding)

      - Work station 6.2: FINCON

      - Work station 8: OUT = Final Assembly

        - All done \> Attach A4 label to crate.

        - Finish \> At the same time the production is \"Reported as finished\" D365 sends a completion document to the customer. *Still In development 07/05/2025. Temporarily covered by email packing list.*

        <!-- -->

        - Measurements via scanner

    - Physically put away boxes together based on MOD on the A4 label.

8.  **Create outbound load** based on ship date & mode of delivery:

    - Starting from SO or from **Sales line availability**

    - Via **Warehouse \> Outbound load planning workbench**

    - NEW: Select the lines and click on **Supply and demand \> To new load**

    - EXISTING: Select the lines and the load and click on **Supply and demand \> To existing load**

    - Open the load and fill In the cut-off date. (Indicates when a load Is supposed to leave)

9.  **Prepare picking**: When the shipments Include stocked goods and not only projects, the picking still needs to be done in the warehouse.

    - Open the outbound load and **Release to warehouse** to create work In D365.

    - Print **Outbound picking list**.

10. **Process picking** via scanner.

11. Add measurements and weight via scanner for picked items.

12. **Prepare outbound load**:

    - **In case of transport organized by Aquadeck:**

      - Book transport based on measurements in **License plate summary**.

      - Print transport labels & attach to goods.

      - Print packing list(s) & attach to goods.

      - Print Outbound load list.

    <!-- -->

    - **In case of transport organized by customer via Manders:**

      - Print packing list(s) & attach to goods.

      - Packing list will be emailed to customer to Inform them the goods are ready so they can arrange transport. *(will be replaced by \"Reported as finished\" document)*

      - Customers need to use Information available on A4 label to organize transport.

      - Print Outbound load list.

    - **In case of collection by customer:**

      - Print packing list(s) & attach to goods.

      - Packing list will be emailed to customer to Inform them the goods are ready so they can arrange transport. (will be replaced by \"Reported as finished\" document)

      - Print Outbound load list. Optional, can also be found In scanner. Where to keep It If printed?

13. **Load to truck** via scanner (when goods are picked up).

14. **Finish** delivery:

    - **Confirm Outbound shipment =** Automatic when all LP\'s from the load are loaded in truck with the scanner.

    - **Generate** **Packing slip.** *This step will be automated after first days. Email In the evening.*

    - **Finish** load = Automatic.

15. Generate **invoice**

    - Via **Make Invoices**. *This step will be automated after first days. Email In the evening.*

**[\*Mode of delivery]{.underline}**

- Mode of delivery = Shipping carrier + service.

- The MOD Is used to put the correct shipments together In the correct outbound load.

- Always choose the MOD with the specific carrier that will transport the goods. Even If transport Is arranged by the customers.

- When the carrier doesn\'t exist, you can use a general MOD (DIV/EXW).

- When the goods are picked up by the customer Itself at the AQD warehouse then use COL.

- When there Is real export, make sure to choose a service EXP.

- The MOD Is a customer setting which Is Interfaced from AX. If you want to change It, you need to change It In AX and It will automatically be changed In D365. This Is the conversion table:

  ----------------------------------------------------------------
  **D365 MOD**   **AXAPTA MOD**   **AXAPTA MOD Description**
  -------------- ---------------- --------------------------------
  COL-STD        2                Enlèvement / Collect / Recoger

  COL-STD        AFH              Afhaling

  DIV-EXP        DIV-EXP          Divers Export

  DIV-STD        DIV              Delivery/Livraison/Entregar

  DPD-24H        198              DPD 24HR

  DPD-BAG        199              DPD BAG

  DPD-EXP        DPD-EXP          DPD Export

  DPD-STD        3                DPD

  DPD-TIM        323              DPD Timed

  EXW-EXP        EXW-EXP          Exworks Export

  EXW-STD        EXWORKS          ExWorks \|

  HAT-EXP        HAT-EXP          Hatrans Export

  HAT-STD        36               Hatrans

  PGE            999              Pollet Group Employee

  SCH-EXP        SCH-EXP          SCHNEIDER Export

  SCH-STD        209              SCHNEIDER

  TIN-STD        221              POM Tinie Manders Transport

  TIN-STD        227              AQD Tinie Manders Transport

  TIN-STD        TIN-STD          Tinie Manders Standard
  ----------------------------------------------------------------

  -----------------------------------------------------------------------------------------
  **PWGTopReferenceCustomerName**          **Mode of delivery**   **Kleur product label**
  ---------------------------------------- ---------------------- -------------------------
  PPG BELGIUM NV                           TIN-STD                Rood

  POMAZ BV                                 TIN-STD                Blauw

  T E P SRL                                TIN-STD                Oranje

  !PPG BELGIUM NV, !POMAZ BV, !T E P SRL   TIN-STD                Zwart

  (Maakt niet uit)                         !TIN-STD               Groen
  -----------------------------------------------------------------------------------------

**[\*\*VAT code]{.underline}**

Green = Yes

Red = No![A diagram of a tree AI-generated content may be incorrect.](media/image3.png){width="6.692648731408574in" height="3.7536384514435697in"}

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image4.emf)

- **Sales order release status**

![](media/image5.emf)

**[Labels]{.underline}**

+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **RAW label: printed after picking with scanner**                                |                                                                                                                                         |
+==================================================================================+=========================================================================================================================================+
| ![](media/image6.png){width="4.029861111111111in" height="1.9701388888888889in"} | - Only used when there is actual picking. Not if the goods are backflushed.                                                             |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - In case the picking is done in multiple rounds, there will be multiple RAW labels. This is the case for SLAT and SLAT                 |
+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **MTS label: printed after clicking on \"All done\" in Tulip work station**      | .                                                                                                                                       |
+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ![](media/image7.png){width="4.097222222222222in" height="2.0743055555555556in"} | - Used at every work station except OUT (final product gets A4 label) .                                                                 |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - One label per license plate.                                                                                                          |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - Needs to be scanned when picking the overlying production order.                                                                      |
+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| **OUTB label: Printed after picking Items already In a load**                    |                                                                                                                                         |
+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ![](media/image8.png){width="4.201388888888889in" height="1.9777777777777779in"} | - Will be printed when there is picking of stock items (not related to production).                                                     |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - There is a license plate for every pallet/box that leaves the warehouse.                                                              |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - License plates can be merged together via staging if the goods fit together.                                                          |
|                                                                                  |                                                                                                                                         |
|                                                                                  | - In the license plate summary you can find all the measurements and weights per license plate if they were registered via the scanner. |
+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

![A close up of a card AI-generated content may be incorrect.](media/image9.png){width="6.298611111111111in" height="4.4875in"}

**[\]{.underline}**

**[Sales order confirmation]{.underline}**

![A screenshot of a document AI-generated content may be incorrect.](media/image10.png){width="5.86540135608049in" height="8.209479440069991in"}

**[Outbound picking list]{.underline}**

![A close-up of a receipt AI-generated content may be incorrect.](media/image11.png){width="6.298611111111111in" height="2.7256944444444446in"}

**[Packing list]{.underline}**

![A screenshot of a document AI-generated content may be incorrect.](media/image12.png){width="5.771639326334208in" height="8.282405949256344in"}

**[Outbound load list]{.underline}**

![A load list with bar code AI-generated content may be incorrect.](media/image13.png){width="6.298611111111111in" height="4.336111111111111in"}

The sales order number is only printed when \"Group packing per order\" is set to YES. This is the default setting defined on a customer level.

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="6.298611111111111in" height="2.1375in"}

**[Packing slip]{.underline}**

![A document with text and numbers AI-generated content may be incorrect.](media/image15.png){width="5.729966097987751in" height="7.438537839020123in"}

**[Sales invoice]{.underline}**

![A white document with black text AI-generated content may be incorrect.](media/image16.png){width="5.729966097987751in" height="6.323799212598425in"}
