# KB — F&O Returns

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Returns.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[1 Required setup [2](#required-setup)](#required-setup)

[2 General [3](#general)](#general)

[3 Creditnote without return of goods [3](#creditnote-without-return-of-goods)](#creditnote-without-return-of-goods)

[4 Repair by company [3](#repair-by-company)](#repair-by-company)

[5 Repair by vendor [4](#repair-by-vendor)](#repair-by-vendor)

[6 Stock return to company [4](#stock-return-to-company)](#stock-return-to-company)

[7 Dismantle to stock [5](#dismantle-to-stock)](#dismantle-to-stock)

[8 Stock return to vendor [5](#stock-return-to-vendor)](#stock-return-to-vendor)

[9 Rejected stock return [5](#rejected-stock-return)](#rejected-stock-return)

[10 Stock return to scrap [6](#stock-return-to-scrap)](#stock-return-to-scrap)

[11 Refurbish to resell (Same Item nr) [6](#refurbish-to-resell-same-item-nr)](#refurbish-to-resell-same-item-nr)

[[12]{.mark} [ReFURBISH to STOCK (different Item nr)]{.mark} [6](#refurbish-to-stock-different-item-nr)](#refurbish-to-stock-different-item-nr)

[13 Investigate [7](#investigate)](#investigate)

[14 Return to vendor from stock [7](#return-to-vendor-from-stock)](#return-to-vendor-from-stock)

[15 Cn from vendor without return [7](#cn-from-vendor-without-return)](#cn-from-vendor-without-return)

[16 Workspace returns [8](#workspace-returns)](#workspace-returns)

**\**

# Required setup

- Set up a location CREDITONLY In the MAIN warehouse.

- Make sure the MAIN warehouse Is set up correctly.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image1.png){width="5.506825240594925in" height="2.846758530183727in"}

- Set up a warehouse for RETURNS which does not work via scanning!

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.010570866141732in" height="3.2763134295713034in"}

- Set up locations within the warehouse RETURNS. You only need locations for the flows you need to use. The locations are not physical locations in the warehouse. You will need to group the goods In the warehouse on a location that you know, It Is not tracked in the system.

Examples: ![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="2.053842957130359in" height="1.085541338582677in"}

# General

- There is a special workspace dedicated to the follow up of returns \> RETURNS (request from Marie)

- If you don\'t want the packing slip to be invoiced you can use the \"block invoice\" checkbox on the header of the sales order.

- In the SCRAP flow you don\'t post a packing slip, you immediately post the invoice. For all other flows you post the packing slip, which can be invoiced later.

- There will be no labels printed to if you need labels you need to do a reprint of a stock label via the scanner.

- The return goods for which you manually post a packing slip will not be part of a load so you need to add the manually in the transport.

- If you create a new purchase order for a return please fill in the RMA number. If you are still waiting on a reply fill in: WAITING, when you received the number fill in the number. This will also be used in the workspace.

# Creditnote without return of goods

**[WAREHOUSE MAIN + LOCATION CREDIT ONLY + CHECKBOX SCRAP]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Add a negative line with the item in the quantity to be credited.

<!-- -->

1.  Fill in the correct price and cost price (as was invoiced to the customer).

<!-- -->

3.  Go to **Line details \> Product** and choose the **location** \"CreditOnly\".

4.  Go to **Line Details \> Setup** and tick the checkbox for SCRAP.

5.  Add \"SCRAP\" in the Customer requisition to make it clear for follow up in the Returns workspace.

6.  Generate the invoice (credit note).

# Repair by company

**[WAREHOUSE RETURN + LOCATION REPAIR CUS]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be repaired.

4.  Change price to free.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR CUS.**

6.  Generate the **Packing slip**.

7.  Add a positive line with the item in the quantity that was repaired.

8.  Add all the components that were used for the repair, go to **Line details \> Product** and fill in the correct location in the MAIN warehouse.

9.  Generate the **Packing slip** and send back the goods to the customer.

10. Generate the Sales **Invoice**.

# Repair by vendor

**[WAREHOUSE RETURN + LOCATION REPAIR VEN]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be repaired.

4.  Change price to free.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

6.  Generate the **Packing slip**.

7.  Navigate to **All Purchase Orders** and create a new PO.

8.  Add a negative line with the item in the quantity to be repaired.

9.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

10. Generate the **Product receipt** and send the goods to the vendor.

11. When you receive the goods back from the vendor: Navigate to the PO.

12. Add a positive line with the item in the quantity that was repaired.

13. Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

14. Confirm the PO and generate the **Product receipt** to process the purchase invoice.

15. Go to the original SO.

16. Add a positive line with the item in the quantity that was repaired.

17. Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

18. Generate the **Packing slip** and send back the goods to the customer.

19. Generate the Sales **Invoice**.

# Stock return to company

**[WAREHOUSE MAIN + LOCATION IN THE WAREHOUSE]{.underline}**

2.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

3.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}(optional)

4.  Add a negative line with the item in the quantity to be credited and put back in stock.

5.  Fill in the correct price and cost price (as was invoiced to the customer).

6.  Go to **Line details \> Product** and change the **Location** to the specific warehouse location in MAIN.

7.  Generate the **Packing slip**.

8.  Generate the **Invoice**.

# Dismantle to stock

When a customer returns a produced Item that needs to be dismantled to go back In stock. (Ex. Aquadeck cover project)

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Add a negative line with the project item in the quantity that will be returned.

3.  Check if price is correct.

4.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **DISMANTLE.**

5.  Generate the **Packing slip**.

6.  Generate the **Invoice (CN).**

7.  Via **Inventory adjustment** you create a journal with reason code \"Conversion of Items\". Add a negative line of the project Item and positive lines for alle the components that go back In stock. Make sure correct locations are filled In + cost prices are ok.

# Stock return to vendor

**[WAREHOUSE RETURN + LOCATION RETURN VEN]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be returned.

4.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **RETURN VEN.**

5.  Generate the **Packing slip**.

6.  Navigate to **All Purchase Orders** and create a new PO.

7.  Add a negative line with the item in the quantity to be returned.

8.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **RETURN VEN.**

9.  Confirm the PO and generate the **Product receipt** and send the goods to the vendor.

# Rejected stock return

**[WAREHOUSE RETURN + LOCATION REJECT]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity that was returned.

4.  Fill in the correct price.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REJECT.**

6.  Generate the **Packing slip**.

7.  Add a positive line with the item in the quantity that was returned.

8.  Fill in the correct price.

9.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REJECT.**

10. Generate the **Packing slip** and send the goods back to the customer.

11. Generate the **Invoice** of both packing slips.

# Stock return to scrap

**[WAREHOUSE MAIN + LOCATION CREDIT ONLY + CHECKBOX SCRAP]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be credited.

4.  Fill in the correct price.

5.  Go to **Line details \> Product** and choose the **location** \"CreditOnly\".

6.  Go to **Line Details \> Setup** and tick the checkbox for SCRAP.

7.  Add \"SCRAP\" in the Customer requisition to make it clear for follow up in the Returns workspace.

8.  Generate the invoice (credit note).

# Refurbish to resell (Same Item nr)

**[WAREHOUSE RETURN + LOCATION REFURBISH]{.underline}**

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be refurbished.

4.  Check if price is correct.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REFURBISH.**

6.  Generate the **Packing slip**.

7.  Generate the **Invoice.**

8.  Repair the item and put it back in stock via an **Inventory Adjustment Journal:**

    a.  Transfer the refurbished item from Return - Refurbish to the MAIN warehouse.

    b.  Book away the used components from the MAIN warehouse.

# [ReFURBISH to STOCK (different Item nr)]{.mark}

*Example \'Revision tubular motor\' (AQUADECK)*

*Customer returns broken motor. Customer buys new motor. Broken motor goes to vendor. Repaired motor Is returned to stock under revision Item code. Customer receives CN for original motor In case of warranty. Revision motor can be sold to a different customer In the future.*

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity to be repaired.

4.  Change price to free.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

6.  Generate the **Packing slip**.

7.  Navigate to **All Purchase Orders** and create a new PO.

8.  Add a negative line with the item in the quantity to be repaired. (price filled In)

9.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **REPAIR VEN.**

10. Generate the **Product receipt** and send the goods to the vendor.

11. When you receive the goods back from the vendor: Navigate to the PO.

12. Add a positive line with the item in the quantity that was repaired. REVISION CODE. (price filled In)

13. Go to **Line details \> Product** and select the **Warehouse MAIN.** Fill In the actual location or process Inbound via load.

14. Confirm the PO and generate the **Product receipt** to process the purchase invoice.

15. Process purchase Invoice (0 value).

# Investigate

1.  Navigate to **All Sales Orders** and find the original SO or create a new SO.

2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign.

![A black and white image of a number Description automatically generated](media/image4.png){width="0.9638713910761155in" height="0.2799814085739283in"}

3.  Add a negative line with the item in the quantity that will be returned.

4.  Check if price is correct.

5.  Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **INVESTIGAT.**

6.  Generate the **Packing slip**.

7.  Depending on the decision what needs to happen, use an Inventory adjustment to book the Item In the correct location and proceed with the correct flow.

# Return to vendor from stock

**[WAREHOUSE MAIN + LOCATION FROM WAREHOUSE]{.underline}**

1.  Navigate to **All Purchase Orders** and create a new PO.

2.  Navigate to **Header \> General** and fill in the RMA Number from the vendor if you have one. If you don\'t have one yet, fill in \"WAITING\".

3.  Add a negative line with the item that needs to be returned.

4.  Check if the price is correct.

5.  Go to **Line details \> Product** and fill in the **Location** in the warehouse from where you will take the item.

6.  Generate the **Product receipt** and return the goods to the vendor.

7.  Generate the **Invoice.**

# Cn from vendor without return

**[WAREHOUSE MAIN + LOCATION FROM WAREHOUSE]{.underline}**

1.  Navigate to **All Purchase Orders** and create a new PO.

2.  Navigate to **Header \> General** and fill in the RMA Number. If you don\'t have one yet, fill in \"WAITING\".

3.  Add a negative line with the item that will be credited.

4.  Check if the price is correct.

5.  Go to **Line details \> Product** and fill in the **Location** in the warehouse from where you will take the item.

6.  Generate the **Product receipt** and throw away the goods.

7.  Generate the **Invoice.**

# Workspace returns

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="3.7881944444444446in"}
