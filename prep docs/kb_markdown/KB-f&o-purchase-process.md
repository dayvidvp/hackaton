# KB — F&O Purchase Process

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase Process.docx`
**Conversiedatum:** 2026-04-24

---

1.  Create PO manually or via MRP and process the PO:

    - Navigate to **All purchase orders.**

    - Add PO lines in correct quantities.

    - Add (requested) receipt date.

    - ![](media/image1.png)Via **Purchase \> Generate:** Send **Purchase Inquiry** to vendor.

2.  Process vendor confirmation in PO:

    - Add confirmed delivery dates.

    - Check quantities.

    - Check prices.

    - ![Hourglass 60% with solid fill](media/image2.png){width="0.20833333333333334in" height="0.20833333333333334in"}Via **Purchase \> Actions: Confirm** the PO.

3.  Process delivery note from vendor: Create inbound load.

    - Navigate to **Inbound load planning workbench.** (Warehouse tab)

    - Select the PO lines that will be in the load. (clear filter for Receipt date if you see nothing)

    - ![Hourglass 60% with solid fill](media/image2.png){width="0.20833333333333334in" height="0.20833333333333334in"}Via **Supply and demand \>** Add **To new load.**

4.  Process delivery arrival:

    - Go in the prepared load and Print the **Inbound load list**.

5.  Process delivery: Register and putaway goods in the warehouse app.

    - Grab[^1] goods on list?

      - Yes \> Registration & Putaway + Complete grabstock reception

      - No \> Go to next

    - Stock/Crossdock[^2] goods on list?

      - Yes \> Register stock Items + Complete reception + Putaway

      - No \> Finished

6.  Finish delivery:

    - Check if everything has been received correctly.

    - Via **Ship and receive \> Confirm \> Inbound shipment.**

    - Via **Ship and receive \> Receive \>** Generate **Product receipt.** (Fill in DN number vendor)

    - **Finish** load Is automatic.

7.  Process the purchase invoice: [F&O Purchase invoicing process.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Purchase%20invoicing%20process.docx?d=wd8ae926ae06b49769af0f5ea165f5782&csf=1&web=1&e=0YtWqz)

**[Remarks:]{.underline}**

- Every significant change made to the purchase order will **change the status** back from Confirmed to Approved.

- Every **PO needs to be confirmed** to generate a product receipt and process the vendor invoice.

- In case you have to **change the price** in the PO, you need to choose the correct **reason code**.

  - CHECK: price needs to be checked by responsible

  - EXCH: difference due to exchange rate

  - FREE: automatically chosen in case you use checkbox Free

  - NEW: when the price you entered will be the new price and we accept it

  - NOPC: no price check needed is for items that always have a different price (ex. transport)

  - ROUND: rounding difference (ex. vendor has 3 decimals and we only have 2)

  - SPEC: one time special price (ex. early buy, big quantity, special discount)

- In case of **direct delivery** you need to create the PO from the SO.

- In case of **overdelivery** you need to add a line to the PO and add this line to the load.

- In case of **underdelivery** you will need to adjust the quantity of your load line (reverse the shipment confirmation if necessary). Then add the remainder of your PO-line to a new load or update the PO-line and set the remainder to zero.

- In case an item in the load is **not delivered** at all you need to remove it from the load lines to be able to confirm the load.

- In case goods are damaged they need to be received under **blocked.**

- In case the warehouse operator forgot to **complete reception** in the scanner, you can change it in the load via the computer.

- During put away, the system always suggests a location. You can choose to **override** the location and propose your own.

- It is possible to register multiple pallets at once (see [F&O Receive multiple pallets.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Receive%20multiple%20pallets.docx?d=wfe2766fe1d5044148dab65935e439a82&csf=1&web=1&e=eHVqUD))

- It might be useful to fill in the DN number from the vendor in the \'Physical posting note\' box when creating the load. That way we can easily copypaste this data when generating the product receipt.

- Via **All preregistrations** we have the option to make preregistrations and link them to inbound loads. Preregistrations contain the carrier info and the number of pallets/colli.

**[Status changes:]{.underline}**

- **Purchase order status**:

![](media/image3.emf)

- **Approval status:**

![](media/image4.emf)

[^1]: Grab goods have fixed locations that can only be used for 1 specific item. These are the blue bins in the production area.

[^2]: Crossdock items are marked as crossdock on the PO line and are send to the crossdock location during inbound.
