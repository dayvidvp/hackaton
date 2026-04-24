# KB — F&O Outbound loads

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Outbound loads.docx`
**Conversiedatum:** 2026-04-24

---

1.  Add sales lines to an **outbound load**:

    - Starting from SO or from **Sales line availability**

    - Via **Warehouse \> Outbound load planning workbench**

    - NEW: Select the lines and click on **Supply and demand \> To new load**

    - EXISTING: Select the lines and the load and click on **Supply and demand \> To existing load**

2.  Prepare picking/production:

    - Add cut-off date in the load. (optional)

    - Set the Scheduled load shipping date. (optional)

    - Change carrier if needed.

    - Set the \'Load complete\' parameter to \'Yes\' if applicable. (optional)

    - Add load/warehouse picking remarks if needed

    - In case of production orders: Schedule production order (optional) & assign work place

3.  Release load to warehouse:

    - Via **Loads \> Release to warehouse**

    - Release to warehouse creates the picking work, visible via **Loads \> Work**

    - Print picking list(s) **via Loads \> Print**

+-----------------------------+-------------------------------+---------------------------------+
| **Only normal picking**     | **Only production**           | **Production & normal picking** |
+=============================+===============================+=================================+
| Release to warehouse        | Release to warehouse          | Release to warehouse            |
|                             |                               |                                 |
| Print outbound picking list | Print production picking list | Print production picking list   |
|                             |                               |                                 |
|                             |                               | Print outbound picking list     |
+-----------------------------+-------------------------------+---------------------------------+

4.  Process picking & assembly via scanner (see [F&O Picking and Assembly.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Picking%20and%20Assembly.docx?d=w674f982cd3494a34baf84728c8711d70&csf=1&web=1&e=NmRNC1)).

5.  Prepare outbound load:

    - Check if everything is picked correctly.

    - In case of transport:

      - Book transport based on measurements in **License plate summary**.

      - Print transport labels

      - Print packing list(s)

      - Add Transport cost & price in Sales order.

    <!-- -->

    - Print **Outbound load list**.

    - Give the file with all the documents to the warehouse operator.

6.  Load to truck via scanner (when goods are picked up, see [F&O Load to truck.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Load%20to%20truck.docx?d=w2e92cf14334f4cf09b9dd49b5b6040d2&csf=1&web=1&e=CfvdUI)).

7.  Finish delivery:

    - Check if everything has been loaded correctly.

    - Via **Ship and receive \> Confirm \> Outbound shipment.** This step happens automatically if all LP\'s from the load are loaded in truck with the scanner.

    - Via **Ship and receive \> Generate \>** **Packing slip.** This step will be automated in the future.

    - Go back to the loads overview, select the load, via **Loads \> Finish** load. This step also happens automatically.

8.  Generate invoice

**[Remarks:]{.underline}**

- Work lines (Loads \> Work) can only be created during load release if the item is on a pickable location. If the item is not on a pickable location (DOCK-IN for example), no work line is created and the \'print picking list\' buttons will remain greyed out (in order to overrule this, go to **Load details \> Header \> Documents \> Allow printing picking lists**).

- Work lines can be cancelled (Work \> Cancel work). This is necessary sometimes if you want to remove items from a released load.

- If you add items to a released load, you can release the load again to create work lines for them. You can release a load as many times as you wish, new work will be created for items that do not yet have work lines (or if their previous work lines were cancelled). No additional work will be created for items that have work lines with work status \'Open\' or \'Closed\'.

- It is possible to change the customer account in a Sales Order up until the packing slip is booked. If the SO lines are already in a load, the loadlines will be updated automatically. But beware, there might be documents (OUTB label, packing list) already attached to the picked pallets that show the old customer info .

- If we stop or interrupt the picking process with the scanner, we might have a situation were goods are picked from their warehouse location, but not put on their destination (Stage location). This is reflected in the work lines (Work type \'Pick\' = Closed, work type \'Put\' = Open). We can only finish an interrupted work line through the scanner: **Utilities \> Execute in process work.**

- Sometimes we want to initiate picking or MTO-production without knowing the final specifics of the outbound load (shipping date/carrier is not yet known, other SO-lines/customers will be added to the load).

In these cases, companies can use temporary \"dummy loads\". They release a dummy load and might leave the cut off date/scheduled date/carrier blank.

Once the items are picked/produced, we can transfer the license plates to the final \"real\" load, see [F&O Moving load lines.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Moving%20load%20lines.docx?d=w01c7aee1cd78457a81ffa26bfedd2e96&csf=1&web=1&e=bfrihV). The dummy load will be empty and automatically deleted.

- Picked license plates can always be merged and divided or items on these license plates can always be transferred to other license plates before we load them in the truck. This happens through the Staging-flow: scanner: **Outbound \> Stage**

- We can always unload a truck as long as the packing slip is not generated. This happens through scanner: **Outbound \> Unload truck**. Similarly, we can also unpick certain goods from a picked license plates. This happens through scanner: **Outbound \> Unpick license plate.**

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image2.emf)

- **Sales order release status**

![](media/image3.emf)

- **Outbound load status**

![](media/image4.emf)

![A close up of a text Description automatically generated](media/image5.jpeg){width="2.3916666666666666in" height="0.37214676290463694in"}

![A white box with black text Description automatically generated](media/image6.jpeg){width="3.6041666666666665in" height="0.5687182852143482in"}
