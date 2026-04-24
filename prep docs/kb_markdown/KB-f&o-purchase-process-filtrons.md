# KB — F&O Purchase Process FILTRONS

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase Process FILTRONS.docx`
**Conversiedatum:** 2026-04-24

---

1.  Create PO manually or via MRP and process the PO:

    - Navigate to **All purchase orders.**

    - Add PO lines in correct quantities.

    - Add (requested) delivery date.

    - Change **Inventory status** to FILTRON.

    - Via **Line details \> Documents,** Add **Item reception remarks**: FILTRONS

    - ![](media/image2.png)Via **Purchase \> Generate:** Send **Purchase Inquiry** to vendor.

2.  Process vendor confirmation in PO:

    - Add confirmed delivery dates.

    - Check quantities.

    - Check prices.

    - ![Hourglass 60% with solid fill](media/image3.png){width="0.20833333333333334in" height="0.20833333333333334in"}Via **Purchase \> Actions: Confirm** the PO.

3.  Process delivery note from vendor: Create inbound load.

    - Navigate to **Inbound load planning workbench.**

    - Select the PO lines that will be in the load. (clear filter for Receipt date if you see nothing)

    - ![Hourglass 60% with solid fill](media/image3.png){width="0.20833333333333334in" height="0.20833333333333334in"}Via **Supply and demand \>** Add **To new load.**

4.  Process delivery arrival:

    - Go in the prepared load and Print the **Inbound load list**.

5.  Process delivery:

    - Register FILTRON goods

    - Complete reception

    - Putaway goods

6.  Finish delivery:

    - Check if everything has been received correctly.

    - Via **Ship and receive \> Confirm \> Inbound shipment.** (automated)

    - Via **Ship and receive \> Receive \>** Generate **Product receipt.** (Fill in DN number vendor)

    - Go back to the loads overview, select the load, via **Loads \> Finish** load. (automated)

7.  Process the purchase invoice

**[In the sales order line you also need to choose the Inventory status FILTRON !]{.underline}**
