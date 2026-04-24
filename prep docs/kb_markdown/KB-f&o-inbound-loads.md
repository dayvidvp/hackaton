# KB — F&O Inbound loads

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Inbound loads.docx`
**Conversiedatum:** 2026-04-24

---

**Inbound loads**

1.  Create an inbound load:

    - Add PO lines to the load via the **Inbound load planning workbench** (Warehouse tab on header)

    - Go in the load via **All loads** or **Active inbound loads (warehouse)** and Print the **Inbound load list**.

2.  Register inbound goods: crossdock & stock goods

    - Scan the load ID on the inbound load list (via **Reception \> Register stock items**).

    - Scan the first item on the list, confirm the action \'move to stock\' and select the quantity on the pallet/box. Confirm everything.

    - Paste the printed INB label on the pallet/box.

    - Repeat for all crossdock/stock items on the load list.

    - Press the **Complete reception** button in the \'Register stock items\' menu.

3.  Register & putaway inbound goods: grabstock goods

    - Scan the load ID on the inbound load list (via **Reception \> Register and put away grab items**).

    - Scan the first grabitem on the list, confirm the action \'move to grab\' and select the quantity you wish to put away.

    - Scan the location proposed by the system for putaway. It is possible to override the proposed location. Put the grab goods on the location.

    - Repeat for all grabstock items on the load list.

    - Press the **Complete reception** button in the \'Register & put away grab items\' menu.

4.  Putaway inbound goods: crossdock & stock goods

    - Scan the INB LP label (via **Reception \> Put away items**). Confirm the values.

    - Scan the location proposed by the system for putaway (crossdock-location will be proposed for crossdock goods). It is possible to override the proposed location. Put the goods on the location.

    - Repeat for all crossdock/stock INB LP\'s of the load.

5.  Finish delivery:

    - Via **Ship and receive \> Confirm \> Inbound shipment.**

> This will only work if:
>
> ▪ Everything on the load is received and
>
> ▪ In the **Load details** page, both the \'Grab reception completed\' and \'Other reception completed\' fields have values \'Yes\' or \'Not available\'. (triggered by the \'Complete reception\' buttons on the scanner)

- Via **Ship and receive \> Receive \>** Generate **Product receipt.**

> For every PO, we need to fill in the DN number from the vendor in the \'Product receipt\' column.

- Via **Loads \> Finish** load.

**[Remarks:]{.underline}**

- A common issue is the impossibility to generate a Product receipt after the Inbound shipment is confirmed. Most of the time this is caused by an **incorrect Approval status of one of the PO\'s**. Be sure to confirm all PO\'s in the load before starting to receive the inbound load.

- In case of **overdelivery** you need to add a line to the PO and add this line to the load.

- In case of **underdelivery** you will need to adjust the quantity of your load line (reverse the shipment confirmation if necessary). Then add the remainder of your PO-line to a new load or update the PO-line and set the remainder to zero.

- In case an item in the load is **not delivered** at all you need to remove it from the load lines to be able to confirm the load.

- In case goods are damaged they need to be received under **blocked.**

- In case the warehouse operator forgot to **complete reception** in the scanner, you can change it in the load via the computer.

- In case the warehouse operator received all grab items as regular stock (via the **Reception \> Register stock items** menu), the \'Complete reception\' button in the grab menu (via **Reception \>** **Register and put away grab items**) should still be pushed. As this is often forgotten, we can change it in the computer as well (see previous remark).

- It is possible to register multiple pallets at once (see [F&O Receive multiple pallets.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Receive%20multiple%20pallets.docx?d=wfe2766fe1d5044148dab65935e439a82&csf=1&web=1&e=eHVqUD))

- It might be useful to fill in the DN number from the vendor in the \'Physical posting note\' box when creating the load. That way we can easily copypaste this data when generating the product receipt.

- Via **All preregistrations** we have the option to make preregistrations and link them to inbound loads. Preregistrations contain the carrier info and the number of pallets/colli.

**[Status changes:]{.underline}**

- **PO: Purchase order status**:

![](media/image2.emf)

- **PO: Approval status:**

![](media/image3.emf)

- **Load: Inbound load status**:

![A white rectangular box with black text Description automatically generated](media/image4.png){width="4.608732502187227in" height="1.633474409448819in"}

- **Load: Work status**:

![](media/image5.png){width="5.48380905511811in" height="1.5167979002624672in"}
