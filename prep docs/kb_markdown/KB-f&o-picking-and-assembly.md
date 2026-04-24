# KB — F&O Picking and Assembly

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Picking and Assembly.docx`
**Conversiedatum:** 2026-04-24

---

1.  Print picking list once the release to warehouse (see **F&O Sales/Production Process**) is done:

    - Sales picking: **All loads \> Loads \> Print \> Outbound picking list**

    - MTO-production picking: **All loads \> Loads \> Print \> Production picking list**

    - MTO-production picking + sales picking (special sales picking):

> **All loads \> Loads \> Print \> Production picking list**

- MTO-production picking + sales picking (no special sales picking):

> **All loads \> Loads \> Print \> Production picking list** + **Outbound picking list**

- MTS-production picking: **All production orders \> View \> Documents \> Production picking list**

**[Remarks:]{.underline}**

- Instead of **All loads**, picklists can also be printed from the **Outbound load planning workbench** or the **Active outbound loads (warehouse)** pages.

- In a SO, we can assign SO-lines as \"special sales picking\" to other SO lines that require MTO-production. Those SO-lines will appear on the MTO production picking list and are picked together with the raw materials for the MTO-order. Thus arriving in PStage instead of going directly to Stage.

To assign an SO-line as special picking, go to **Sales order details** and then in the column **Production ID MTO**, choose the production order number you want to assign the line to. (Be aware that this implies that both SO lines will be added to the same load, as they need to be picked together.)

2.  Give picking list to the operator:

    - Normally a customer file will be given to the operator, possibly containing multiple picking lists + production reports

3.  Get a picking pallet and start picking by scanning the Pick key on the pick list:

    - Sales/MTO-production picking =\> Scanner: **Outbound \> Picking sales & production**

    - MTS-production picking =\> Scanner: **Production \> Picking for production**

4.  Pick all items proposed by the scanner one by one:

    - The scanner will propose to pick location per location. The order of those locations is determined by the **location directives** + **sort code** in D365

    - First the location label (check digits) needs to be scanned, then the item number needs to be scanned. When multiple pick items are on the same location, the location label only has to be scanned once.

    - It is possible to skip a proposed pick location if it doesn\'t fit in the optimal pick flow. The skipped location will appear again at the end of the picking list on the scanner.

    - The paper picking list will also show all items to be picked (although not necessarily in the exact order as the scanner), but without the picking locations. Replenishment/Bulk items are also shown at the bottom of the paper pick list, but they will not appear on the scanner

5.  Put the picked items on the PStage/Stage:

    - Stage location will be proposed if there is no production required, otherwise the PStage location will be proposed

    - Raw materials will be put on the PStage (label will be scanned) but in the background they will be automatically moved to Prodin location (no scanning required). Only special sales items will stay on PStage.

    - A RAW label will be printed for production raw materials, an OUTB label will be printed for sales items

6.  **MTO**: Assemble items if applicable:

    - See [F&O Production Process.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Production%20Process.docx?d=w8c84f7cb93e9464682fea5fca6b5257e&csf=1&web=1&e=jYrO1T)

7.  Weigh/measure picked/produced goods if necessary:

    - See load remark on picklist

8.  Give picklists back to Customer Service:

    - That way they will know the goods are ready for loading and they can finish the outbound load + print the Outbound load list

# Options

- **[Staging]{.underline}**: After picking goods and putting them on Stage or Pstage, we can still merge or split LP\'s or move items from one LP to another. This can be done across all stage locations, meaning that goods can flow from LP\'s on Stage to LP\'s on Pstage and vice versa. New OUTB labels can be printed after stage actions. Keep in mind that LP\'s must have the same pack key in order to be able to transfer or merge LP\'s.

> Via the scanner: **Outbound \> Stage**

- **[Unpick LP\'s]{.underline}:** After goods are already picked & staged, it can happen that the sales order is cancelled and the picked items should be sent to stock locations. STOCK labels will be printed when putting these items back in stock. (fyi, you can unpick specific items and quantities on a LP, it is not necessary to unpick the entire LP)

Via the scanner: **Outbound \> Unpick license plate**

- **[Transfer picked LP\'s to other loads]{.underline}:** See [F&O Moving load lines.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Moving%20load%20lines.docx?d=w01c7aee1cd78457a81ffa26bfedd2e96&csf=1&web=1&e=7K4vYX)

- **[Multiple LP\'s during picking]{.underline}:** During picking, we can already split the picking list in multiple LP\'s. That way we can already print multiple OUTB labels instead of printing only one and having to transfer goods via the Stage menu after picking is completed.

> Three buttons are useful for building LP\'s during picking via the scanner:

- **Skip**: Skips the proposed item and moves to the next item on the pick list. The skipped item reappears at the end of the picking list.

- **Full**: With this button we can split the picking quantity of the item that is proposed on the screen. So we split one pickwork line into two pickwork lines. The scanner will continue with a proposal to pick the first line followed by a proposal to pick the second line (followed by all the other items that aren\'t picked yet).

- **Done**: With this button we can stop our picking and drop off the already picked goods at the stage location. An OUTB label will be printed for those picked goods. Afterwards, we need to rescan the pick key in order to continue and pick the remainder of the goods.

<!-- -->

- **[Picking interrupted]{.underline}:** Our picking can be interrupted when we leave the pick flow on the scanner without properly stopping the picking with the **Done** button. In that case, we have already done the pick-step for an item, but we have not done the put-step yet. This is visible in D365 F&O in the work details for the load/production order we are picking.

We cannot finish the interrupted picking through the Outbound menu on the scanner. Instead we need to go to another menu: Scanner: **Utilities \> Execute in process work.**

In this menu, we can complete the put-step, either by entering the workID or the LP number.

Afterwards, we can rescan the pick key to continue our picking of the other items.

- **[Consolidated picking]{.underline}:** It is possible to pick multiple production orders at once. We can pick multiple MTS orders together and we can pick multiple MTO orders together (even with special sales lines linked) as long as they have the same packkey.

> We need to define a consolidated pick key in order to pick production orders together. This can be done through **All production orders \> Schedule \> Production consolidation**. Orders with the same consolidation key will be picked together.
>
> There is also an automated flow to give MTO production orders from the same load a shared consolidation key when releasing the load. This works by defining a consolidation group (**Production control \> Setup \> Production \> Consolidation group**) and then linking this group to specific articles (via **Released product details \> Warehouse \> Production consolidation**). All articles with the same consolidation group will have the same consolidation key when the load is released.
>
> Consolidated picking must happen through a separate menu: Scanner: **Production \> Multiple PRO picking.** That way we still maintain the option to pick orders separately (via **Outbound \> Picking sales & production**) even if orders have a consolidation key.
