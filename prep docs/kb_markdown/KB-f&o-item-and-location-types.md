# KB — F&O Item and Location Types

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Item and Location Types.docx`
**Conversiedatum:** 2026-04-24

---

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Item type**                   **Product type**   **Storage dimension**   **Item model group**   **Inventory Unit**             **WH pick work**   **fixed loc.**   **Flushing principle**
  ------------------------------- ------------------ ----------------------- ---------------------- ------------------------------ ------------------ ---------------- ------------------------
  **Item stock**                  Item               Warehouse               ITM ST                 pcs, bag, box, ltr...          Y                  Y/N              Manual

  **Item grabstock**              Item               Warehouse               ITM ST                 pcs                            Y                  Y                Manual

  **Item replenish-ment stock**   Item               Warehouse               ITM ST                 decimals: m, ltr, kg, CFT...   Y/N                Y                Finish

  **Item multipallet**            Item               Warehouse               ITM ST                 PCS+                           Y                  N                Manual

  **Item bundle**                 Item               Warehouse               ITM ST                 pcs                            Y/N                N                Manual

  **Item phantom**                Item               Warehouse               ITM ST                 pcs                            N                  N                Manual

  **Item neg stock**              Item               Warehouse               ITM NEG ST             pcs                            N                  N                Manual

  **Item consumable stock**       Item               Service                 CON ST                 pcs, box...                    N                  N                Finish

  **Service no stock**            Service            Service                 SRV NO ST              pcs, km                        N                  N                Finish

  **Service stock**               Service            Service                 SRV ST                 pcs, min                       N                  N                Finish
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Item stock:

    - Regular items, kept in stock locations across the warehouse

    - Can have a fixed location, but is not required

    - Examples: vessel, valves...

2.  Item grabstock:

    - Mostly small, low-value items, kept in specific grabstock locations

    - Defined by **Released product details \> Warehouse \> Product filter codes \> Code 1 \> GRABSTOCK**

    - Requires at least 1 fixed grabstock location per item/item variant

    - INB: Grabstock items are received through a separate menu on the scanner. No labels are printed after reception

    - It is possible to store or receive grabstock items on stock locations as well, for example if there is no more room in the fixed grabstock location.

    - Examples: spare parts, small parts (injectors, flow washers, screws, Orings...)

3.  Item replenishment stock:

    - Also called bulk stock. Is kept in decimal inventory units (kg, l, m, CFT...) in a limited number of stock locations

    - Defined by **Released product details \> Engineer \> Production \> Flushing principle \> Finish** and by **Released product details \> Warehouse \> Replenishment \> Replenishment item \> Yes**

    - Requires exactly 1 fixed stock location per item/item variant. Should not be kept in other locations than its fixed location (as the flushing only consumes stock from the fixed location).

    - Production picking: No picking work on scanner is created

> Sales picking: Picking work on scanner is created

- Each replenishment item has to be added to the appropriate work policy for bulk items via **Warehouse management \> Setup \> Work \> Work policies.**

- Examples: sand, resin, tubes, liquids...

4.  Item multipallet:

    - Partible items of which one piece can possibly be packaged and shipped on multiple LP\'s, which means that decimal quantities can be stored on those LP\'s

    - Is only produced for specific customer orders (MTO) and is therefore never kept in stock. Should only be placed in locations PSTAGE or STAGE.

    - Defined by **Released product details \> Manage inventory \> Inventory \> Unit \> PCS+** and by **Released product details \> Warehouse \> Physical Dimension \> Unit sequence group ID \> PCS+**

    - Sales & purchase unit are also set to PCS+

    - A sales order line containing a multipallet item should be put in its entirety in 1 load line

    - System checks are in place so that multipallet items can never be partially shipped to customers

    - Non-multipallet items can become multipallet items at any time through **Warehouse management \> Periodic tasks \> Change inventory unit to multipallet unit**.

    - Multipallet items can never become non-multipallet items once transactions were registered on the item.

    - Examples: duo bloc, duplex softeners...

5.  Item bundle:

    - A bundle item represents a fixed set of items that are sold or purchased together

    - Defined by **Released product details \> General \> Bundles \> YES**

    - A bundle item always has its Production type (**Released product details \> Engineer \> Production type**) set to BOM, with an active BOM version defined that contains the items making up the bundle. These items can be stock, grabstock & replenishment items

    - A bundle should always have its Default order type (**Released product details \> Manage inventory \> Default order settings**) set to \'Production.

    - A bundle item in a sales or purchase order is always exploded to show the underlying items. The column Isbundle shows if the items is a parent (bundle item) or a child (bundle item component).

    - Bundles items are never kept on stock, only their components are kept on stock. Therefore bundle items themselves are never used in warehouse flows. Pick work is generated for bundle item components (child) but not for bundle items (parent).

    - System checks are set up so that all bundle components are added to the same load and in the correct proportional quantities.

6.  Item phantom:

    - Items that are never kept on stock, sold or bought

    - Defined by **Released product details \> Engineer \> Phantom \> Yes**

    - Phantom items always have BOM\'s. They are used in BOM\'s themselves in order to represent a set of choices one has when making a production order.

    - When a phantom item is used in a BOM, the **Line type of the BOM-line must be set as \'Phantom\'**. Otherwise the use of the phantom item will not work properly.

    - Phantom items themselves do not appear on production reports or picking lists. Only their BOM-components appear on those documents.

7.  Item neg stock:

    - Services that have to be categorized as Items so they can be on the same delivery note as the goods.

    - Defined by item model group = ITM NEG ST

    - Are never kept on stock

    - Example: Transport cost

8.  Item consumable stock:

    - Stocked items but without financial values/bookings/integration

    - Defined by item model group = CON ST

    - Items are never scanned

    - Are kept on stock but all stock changes have to be booked manually

    - Items are not used in BOM\'s

    - Example: Packaging materials (Euro pallet, stretch foil), workwear, tools

9.  Service no stock:

    - Services that cannot be put in BOM\'s nor in Loads

    - Defined by item model group = SRV NO ST

    - As they cannot be put in Loads, a separate delivery note or product receipt should be booked for these items when they are in a SO or PO

    - Example: Custom costs

10. Service stock:

    - Services that can be put in BOM\'s and Loads

    - Defined by item model group = SRV ST

    - Example: Work For Assembly (BOM\'s)

Location types

  -------------------------------------------------------------------------------------------------------------------------------
  **Location type**   **Inventory statusses allowed**   **Scan location barcode**   **LP-controlled**   **Mixed items allowed**
  ------------------- --------------------------------- --------------------------- ------------------- -------------------------
  Stock               Available                         Y                           N                   Y

  Grabstock           Available                         Y                           N                   N

  Blocked             Blocked                           Y                           Y                   Y

  Crossdock           Available                         Y                           Y                   Y

  Dock-in             Available & Blocked               N                           Y                   Y

  Prodin              Available                         N                           Y                   Y

  Prodout             Available                         N                           Y                   Y

  Pstage              Available                         Y                           Y                   Y

  Stage               Available                         Y                           Y                   Y

  User                Available & Blocked               N                           Y                   Y

  Salesreturn         Available & Repair                Y                           Y                   Y
  -------------------------------------------------------------------------------------------------------------------------------

1.  Stock locations:

    - Occupy the most space in the warehouse. Filled with stock & replenishment & consumable items.

    - Barcode location labels are visible for all stock locations.

    - Stock locations can be attached as fixed location to stock items, replenishment and consumable items.

    - Example: N, SP, BT, A, BURO, ZOL-A-5, KAST3, CLACK-000, upper row blue bins

2.  Grabstock locations:

    - Small locations in the production room. They contain only grabstock items.

    - Barcode location labels are visible for all grabstock locations.

    - Can only contain 1 grabstock item/item variant per location.

    - If the location contains stock, then it must be defined in F&O as a fixed location to the item it contains.

    - A grabstock location fixed to a grabstock item cannot be fixed to another item

    - The fixed grabstock location must contain a barcode with the grabstock item number

    - Examples : SIATA, AUTO, PVC, MESS, KAST2, CLACK, FLECK1-2 (except 000 locations and some upper rows)

3.  Blocked location:

    - Only 1 location in Micron, location \'BLOCKED\'.

    - Can contain stock, grabstock, replenishment and consumable items but the stock needs to be on a license plate with inventory status \'Blocked\'.

    - No physical location in warehouse. Instead A4-pages with a BLOCKED barcode are available that need to be attached to the blocked stock.

    - Specific LP label is printed when moving stock to location BLOCKED

4.  Crossdock location:

    - Only 1 location in Micron, location \'CROSS\'.

    - Can contain stock, grabstock & replenishment items. Items arrive in crossdock location during the inbound process if the crossdock checkbox is marked on the PO-line.

    - Crossdock locations are supposed to be close to the INB/OUTB gate.

    - Regular INB labels are printed during crossdock inbound.

5.  Dock-in location:

    - Only 1 location in Micron, location \'DOCK-IN\'.

    - Can contain stock & replenishment items.

    - Although there is no barcode location label for scanning, we generally receive goods through the inbound gate, and therefore this location is mostly associated with the Dock-in location.

    - In the inbound process, stock arrives on the Dock-in location after registration and it leaves the location during putaway. This is the only moment where stock can be found on the Dock-in location.

6.  Prodin location:

    - Only 1 location in Micron, location \'PRODIN\'.

    - Can contain stock & grabstock items.

    - Although there is no barcode location label for scanning, we generally associate the areas near the workbenches with the PRODIN location.

    - After picking raw materials for production, we put them on the PSTAGE location. At this moment, a RAW label is printed and the license plate is moved automatically from PSTAGE to PRODIN.

    - After the \"Declare consumed goods\" step in Shopfloor, the stock on the PRODIN location associated with that production order is automatically deleted (except when remainder stock is declared in Shopfloor).

7.  Prodout location:

    - Only 1 location in Micron, location \'PRODOUT\'.

    - Can only contain stock items.

    - Although there is no barcode location label for scanning, we generally associate the areas near the workbenches with the PRODOUT location.

    - When produced MTS goods are registered in Shopfloor, a MTS label is printed and the goods are stored in the PRODOUT location.

    - After production, produced goods are moved from PRODOUT to stock locations.

8.  PStage location:

    - Only 1 location in Micron, location \'PSTAGE\'.

    - Physically, the PSTAGE location is in the production room, near the workbenches. Barcode location labels are visible on all workbenches.

    - Can contain stock, grabstock, replenishment & multipallet items.

    - Goods can arrive on the PSTAGE location in 3 ways:

> \- Put on PSTAGE as \"special sales picking\" during the production picking process.
>
> \- Registered on PSTAGE as produced MTO product
>
> \- Merged from the STAGE location through Staging menu on scanner
>
> Each time products arrive on PSTAGE, an OUTB label will be printed

- Goods can be loaded in trucks directly from PSTAGE, as well as from STAGE.

9.  Stage location:

    - Only 1 location in Micron, location \'STAGE\'.

    - Physically, the STAGE location is near the gate, where a barcode location label is also visible (but barcode location labels are also visible near weighing instruments in the production room for license plate weighing purposes).

    - Can contain stock, grabstock, replenishment & multipallet items.

    - After sales picking (without production), goods are put on the STAGE location, where OUTB labels are printed and goods wait to be loaded in the truck.

10. User locations:

    - Administrative locations, one location for each warehouse worker.

    - User locations will only hold stock during a pick-put process in the warehouse. More precisely, after the pick-step and before the put-step.

    - User locations should only hold stock very briefly. If they hold stock for a longer period of time, it probably means that a warehouse process was abrupted.

11. Salesreturn locations:

    - Different locations for different situations in separate warehouse \'RETURN\'.

    - 1 rack near the gate is foreseen to hold all return stock (and only return stock).

    - Stock on these locations must be attached to a RMA-number.

    - All inbound in salesreturn locations is done manually in D365, not with the scanner.

    - Outbound flows are done manually in D365, not with the scanner.

    - More info on the return flow in [F&O Returns.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Returns.docx?d=wad343899f5fc41fca0813b13a552cf3b&csf=1&web=1&e=ze848Q)

![A screenshot of a computer Description automatically generated](media/image3.jpeg){width="4.989583333333333in" height="1.65625in"}
