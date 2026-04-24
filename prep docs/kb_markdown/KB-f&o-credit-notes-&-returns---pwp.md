# KB — F&O Credit notes & Returns   PWP

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Credit notes & Returns - PWP.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[General [1](#general)](#general)

[1 Creditnote without return of goods [2](#creditnote-without-return-of-goods)](#creditnote-without-return-of-goods)

[2 Stock return to PWP [2](#stock-return-to-pwp)](#stock-return-to-pwp)

[3 Stock return via PWP to vendor [3](#stock-return-via-pwp-to-vendor)](#stock-return-via-pwp-to-vendor)

[4 Repair by PWP [3](#repair-by-pwp)](#repair-by-pwp)

[5 Repair by vendor [5](#repair-by-vendor)](#repair-by-vendor)

[6 Refurbish to resell [6](#refurbish-to-resell)](#refurbish-to-resell)

[7 Return to vendor from stock [6](#return-to-vendor-from-stock)](#return-to-vendor-from-stock)

[8 Bonus/Discount for customer [7](#bonusdiscount-for-customer)](#bonusdiscount-for-customer)

[9 CN to Correct wrong Item price [7](#cn-to-correct-wrong-item-price)](#cn-to-correct-wrong-item-price)

[10 Correct wrong invoice [8](#correct-wrong-invoice)](#correct-wrong-invoice)

[11 How to deal with Bundles [9](#how-to-deal-with-bundles)](#how-to-deal-with-bundles)

# General

- The return goods for which you manually post a \"purchase return note\" are not part of a load so you need to add them manually in the transport. You can\'t use the outbound load planning workbench.

- There will be no labels printed to if you need labels you need to do a reprint of a stock label via the scanner.

- Positive and negative lines can never be Invoices together.

- Every pick up of goods needs to be organized with a FREE TEXT TRANSPORT DOCUMENT. Because we don\'t know beforehand If an Item can be posted In stock via the SO (return) or not (repair).

- If the original SO or PO was In AXAPTA, then you need to create a new SO/PO and add the Item manually. You then have to go to **References**, click +NEW, check \"Correction\", choose the Reason code, choose Reference \"Others\" and fill In the Reference Number and Date manually.

![A screenshot of a computer Description automatically generated](media/image1.png){width="6.268055555555556in" height="1.2291666666666667in"}

# Creditnote without return of goods

*Example: goods are damaged upon delivery*

+-------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE MAIN + LOCATION CREDIT ONLY + CHECKBOX SCRAP**                                                              |
+=====================================+===================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                    |
|                                     |                                                                                   |
|                                     | 2.  In the action pane Sell, click on **Credit note**.                            |
|                                     |                                                                                   |
|                                     | 3.  Select the Invoice/line/quantity you want to credit.                          |
|                                     |                                                                                   |
|                                     | 4.  In the **Reason code** field, select **Return.**                              |
|                                     |                                                                                   |
|                                     | 5.  Click OK. The line(s) will be added In the SO.                                |
|                                     |                                                                                   |
|                                     | 6.  Print Order Confirmation, write CREDIT ONLY on it and give to Isabel.         |
+-------------------------------------+-----------------------------------------------------------------------------------+
| *Isabel*                            | 7.  Approve and give to Teresa                                                    |
+-------------------------------------+-----------------------------------------------------------------------------------+
| *Teresa*                            | 8.  Go to the SO. Select your negative line, click on **References.**             |
|                                     |                                                                                   |
|                                     | 9.  In the Reason code field, check if the reason code is filled In correctly.    |
|                                     |                                                                                   |
|                                     | 10. Go back to the SO.                                                            |
|                                     |                                                                                   |
|                                     | 11. Click in the Header tab.                                                      |
|                                     |                                                                                   |
|                                     | 12. In Setup, select the **Number sequence group [SALESNeg.]{.underline}**        |
|                                     |                                                                                   |
|                                     | 13. Click Save.                                                                   |
|                                     |                                                                                   |
|                                     | 14. Go to **Line details \> Product** and choose the **location** \"CreditOnly\". |
|                                     |                                                                                   |
|                                     | 15. Go to **Line Details \> Setup** and tick the checkbox for SCRAP.              |
|                                     |                                                                                   |
|                                     | 16. Generate the **Invoice (= sales credit note).**                               |
+-------------------------------------+-----------------------------------------------------------------------------------+

# Stock return to PWP

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE MAIN + LOCATION IN THE WAREHOUSE**                                                                                                                                   |
+=====================================+============================================================================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                                                                             |
|                                     |                                                                                                                                            |
|                                     | 2.  In the action pane Sell, click on **Credit note**.                                                                                     |
|                                     |                                                                                                                                            |
|                                     | 3.  Select the Invoice/line/quantity you want to return to stock and credit.                                                               |
|                                     |                                                                                                                                            |
|                                     | 4.  In the **Reason code** field, enter or select **Return**.                                                                              |
|                                     |                                                                                                                                            |
|                                     | 5.  Click OK. The line(s) will be added In the SO.                                                                                         |
|                                     |                                                                                                                                            |
|                                     | 6.  Print the order confirmation and give to Isabel.                                                                                       |
|                                     |                                                                                                                                            |
|                                     | 7.  Make a **Free text transport document** for the transport company if needed.                                                           |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| *Isabel*                            | 8.  Approve and give order confirmation to Warehouse people                                                                                |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 9.  Put the return back In the warehouse and write the location on the OC. Give the OC to Teresa.                                          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| *Teresa*                            | 10. Go to the SO. Select your negative line, click on **References.**                                                                      |
|                                     |                                                                                                                                            |
|                                     | 11. In the Reason code field, check if the reason code is filled In correctly.                                                             |
|                                     |                                                                                                                                            |
|                                     | 12. Go to the SO. Click in the Header tab.                                                                                                 |
|                                     |                                                                                                                                            |
|                                     | 13. In Setup, select the **Number sequence group** [**SALESNeg**.]{.underline}                                                             |
|                                     |                                                                                                                                            |
|                                     | 14. Click Save.                                                                                                                            |
|                                     |                                                                                                                                            |
|                                     | 15. Go back to the SO.                                                                                                                     |
|                                     |                                                                                                                                            |
|                                     | 16. Go to **Line details \> Product** and change the **Location** to the specific warehouse location in MAIN. (written on OC by warehouse) |
|                                     |                                                                                                                                            |
|                                     | 17. Generate the **Packing slip (=Sales return note)**.                                                                                    |
|                                     |                                                                                                                                            |
|                                     | 18. Fill In Shipping Information If needed.                                                                                                |
|                                     |                                                                                                                                            |
|                                     | 19. Generate the **Invoice (= sales credit note)**.                                                                                        |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

# Stock return via PWP to vendor

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE RETURN + LOCATION RETURN VEN**                                                                                                                               |
+=====================================+====================================================================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                                                                     |
|                                     |                                                                                                                                    |
|                                     | 2.  In the action pane Sell, click on **Credit note**.                                                                             |
|                                     |                                                                                                                                    |
|                                     | 3.  Select the Invoice/line/quantity you want to return to stock and credit.                                                       |
|                                     |                                                                                                                                    |
|                                     | 4.  In the **Reason code** field, enter or select **Return**.                                                                      |
|                                     |                                                                                                                                    |
|                                     | 5.  Click OK. The line(s) will be added In the SO.                                                                                 |
|                                     |                                                                                                                                    |
|                                     | 6.  Print the order confirmation, write RETURN TO VENDOR on It and give to Isabel.                                                 |
|                                     |                                                                                                                                    |
|                                     | 7.  Make a **Free text transport document** for the transport company.                                                             |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| *Isabel*                            | 8.  Approve and give the confirmation to the warehouse people.                                                                     |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 9.  Receive the goods from the customer. Put them on a specific location to return to vendor.                                      |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| *Teresa*                            | 10. Go to the SO. Select your negative line, click on **References.**                                                              |
|                                     |                                                                                                                                    |
|                                     | 11. In the Reason code field, check if the reason code is filled In correctly.                                                     |
|                                     |                                                                                                                                    |
|                                     | 12. Go to the SO. Click in the Header tab.                                                                                         |
|                                     |                                                                                                                                    |
|                                     | 13. In Setup, select the **Number sequence group** [**SALESNeg**.]{.underline}                                                     |
|                                     |                                                                                                                                    |
|                                     | 14. Click Save.                                                                                                                    |
|                                     |                                                                                                                                    |
|                                     | 15. Go back to the SO.                                                                                                             |
|                                     |                                                                                                                                    |
|                                     | 16. Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **RETURN VEN.**                     |
|                                     |                                                                                                                                    |
|                                     | 17. Generate the **Packing slip (=Sales return note)**.                                                                            |
|                                     |                                                                                                                                    |
|                                     | 18. Generate the **Invoice (= sales credit note)**.                                                                                |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| *Paulo/Miguel*                      | 19. Navigate to **All Purchase Orders** and create a new PO.                                                                       |
|                                     |                                                                                                                                    |
|                                     | 20. Add a negative line with the item in the quantity to be returned.                                                              |
|                                     |                                                                                                                                    |
|                                     | 21. In Setup, select the Number sequence group **PurchRET**.                                                                       |
|                                     |                                                                                                                                    |
|                                     | 22. Go to **Line details \> Product** and select the **Warehouse RETURN** and the **Location** **RETURN VEN.**                     |
|                                     |                                                                                                                                    |
|                                     | 23. Confirm the PO and generate the **Product receipt (=Purchase return packing slip)** manually and send the goods to the vendor. |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 24. Send the goods to the vendor with the Purchase return packing slip.                                                            |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

# Repair by PWP

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE RETURN + LOCATION REPAIR CUS**                                                                                                                                                                                                                                                       |
+=====================================+============================================================================================================================================================================================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign. ![A black and white image of a number Description automatically generated](media/image2.png){width="0.9638713910761155in" height="0.2799814085739283in"} |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 3.  Add a negative line with the item in the quantity to be repaired.                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 4.  In **Line details \> Product,** select **Warehouse RETURN** and **Location** **REPAIR CUS.**                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 5.  Print the order confirmation and give to Isabel.                                                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 6.  Make a **Free text transport document** for the transport company if needed.                                                                                                                                                                           |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Isabel*                            | 7.  Approve and give order confirmation to Warehouse people                                                                                                                                                                                                |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 8.  Receive goods. Put the return in the location for repairs and give the OC to Paulo.                                                                                                                                                                    |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Paulo & Teresa*                    | **[Stock needed for repair & Warranty]{.underline}**                                                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 9.  Repair the product.                                                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 10. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 11. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Add components needed for repair and put on **FREE**.                                                                                                                                                                                                  |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. For each component, go to **Line details \> Product** and select the **location** where the component was on-hand In het warehouse.                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. Add work and or transport (location NEG) put on **FREE**.                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Generate the **Packing slip** (don\'t forget the Shipping information) manually.                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 17. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 18. Teresa Is allowed to generate the Invoice even If It Is 0 €!                                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | **[Stock needed for repair & No warranty]{.underline}**                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 10. Repair the product.                                                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 11. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. Add components needed for repair.                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. For each component, go to **Line details \> Product** and select the **location** where the component was on-hand In het warehouse.                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Add work and or transport (location NEG).                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Generate the **Packing slip** (don\'t forget the Shipping information) manually.                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 17. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 18. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 19. Terese generates the sales Invoice.                                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | **[No stock needed for repair & Warranty]{.underline}**                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 10. Repair the product.                                                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 11. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. Add work and or transport (location NEG) put on **FREE**.                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Generate the **Invoice** manually form the SO. (0 € Invoice Is allowed)                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | **[No stock needed for repair & No Warranty]{.underline}**                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 10. Repair the product.                                                                                                                                                                                                                                    |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 11. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. Add work and or transport (location NEG).                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Generate the **Invoice** manually form the SO.                                                                                                                                                                                                         |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Repair by vendor

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE RETURN + LOCATION REPAIR VEN**                                                                                                                                                                                                                                                       |
+=====================================+============================================================================================================================================================================================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 2.  Navigate to **Header \> General** and generate a **Return number** by clicking on the + sign. ![A black and white image of a number Description automatically generated](media/image2.png){width="0.9638713910761155in" height="0.2799814085739283in"} |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 3.  Add a negative line with the item in the quantity to be repaired.                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 4.  In **Line details \> Product,** select **Warehouse RETURN** and **Location** **REPAIR VEN.**                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 5.  Print the order confirmation and give to Isabel.                                                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 6.  Make a **Free text transport document** for the transport company if needed.                                                                                                                                                                           |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Isabel*                            | 7.  Approve and give order confirmation to Warehouse people                                                                                                                                                                                                |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 8.  Receive goods. Put the return in the location for repairs and give the OC to Paulo.                                                                                                                                                                    |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Paulo*                             | 9.  Create **Free text transport document** to return to the vendor.                                                                                                                                                                                       |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 10. Send goods to vendor.                                                                                                                                                                                                                                  |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 11. After some time, receive goods back from vendor. Give Paulo the delivery note.                                                                                                                                                                         |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Paulo, Warehouse & Teresa*         | **[Warranty]{.underline}**                                                                                                                                                                                                                                 |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Go to PO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. Process the delivery note from the vendor with as little postings as possible. If you need to receive components/work, put them on location **REPAIR VEN.**                                                                                            |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. Post the product receipt.                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 17. Add components needed for repair and put on **FREE**.                                                                                                                                                                                                  |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 18. For each component, select the **location REPAIR VEN.**                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 19. Add work and or transport (location NEG) put on **FREE**.                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 20. Generate the **Packing slip** (don\'t forget the Shipping information) manually.                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 21. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 22. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 23. Teresa Is allowed to generate the Invoice even If It Is 0 €!                                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | **[No warranty]{.underline}**                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 12. Go to PO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 13. Process the delivery note from the vendor with as little postings as possible. If you need to receive components/work, put them on location **REPAIR VEN.**                                                                                            |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 14. Post the product receipt.                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 15. Go to SO.                                                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 16. Cancel the deliver remainder for the negative line for the repaired product.                                                                                                                                                                           |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 17. Add components needed for repair.                                                                                                                                                                                                                      |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 18. For each component, select the **location REPAIR VEN.**                                                                                                                                                                                                |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 19. Add work and or transport (location NEG).                                                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 20. Generate the **Packing slip** (don\'t forget the Shipping information) manually.                                                                                                                                                                       |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 21. Make a **Free text transport document** for the complete repaired product.                                                                                                                                                                             |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 22. Send back the goods to the customer and give papers to Teresa to Invoice.                                                                                                                                                                              |
|                                     |                                                                                                                                                                                                                                                            |
|                                     | 23. Terese generates the sales Invoice.                                                                                                                                                                                                                    |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

# Refurbish to resell

+---------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE RETURN + LOCATION REFURBISH**                                                                                       |
+=====================================+===========================================================================================+
| *Sales person*                      | 1.  Navigate to **All Sales Orders** and find the original SO.                            |
|                                     |                                                                                           |
|                                     | 2.  In the action pane Sell, click on **Credit note**.                                    |
|                                     |                                                                                           |
|                                     | 3.  Select the Invoice/line/quantity you want to return to stock and credit.              |
|                                     |                                                                                           |
|                                     | 4.  In the **Reason code** field, enter or select **Return**.                             |
|                                     |                                                                                           |
|                                     | 5.  Click OK. The line(s) will be added In the SO.                                        |
|                                     |                                                                                           |
|                                     | 6.  Print the order confirmation and give to Isabel.                                      |
|                                     |                                                                                           |
|                                     | 7.  Make a **Free text transport document** for the transport company if needed.          |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| *Isabel*                            | 8.  Approve and give order confirmation to Warehouse people                               |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| *Warehouse*                         | 9.  Put the return with the repairs and give the OC to Paulo.                             |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| *Paulo*                             | 10. Check if OK for Refurbish.                                                            |
|                                     |                                                                                           |
|                                     | 11. Go to the SO and fill in the **Warehouse RETURN** and the **Location** **REFURBISH.** |
|                                     |                                                                                           |
|                                     | 12. Select your negative line, click on **References.**                                   |
|                                     |                                                                                           |
|                                     | 13. In the Reason code field, check if the reason code is filled In correctly.            |
|                                     |                                                                                           |
|                                     | 14. Go to the SO. Click in the Header tab.                                                |
|                                     |                                                                                           |
|                                     | 15. In Setup, select the **Number sequence group** [**SALESNeg**.]{.underline}            |
|                                     |                                                                                           |
|                                     | 16. Generate the **Packing slip**. **(=Sales return note)**.                              |
|                                     |                                                                                           |
|                                     | 17. Give to Teresa for invoicing.                                                         |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| *Paulo*                             | 18. Repair the item and put it back in MAIN stock via 1 **Inventory Adjustment:**         |
|                                     |                                                                                           |
|                                     |     - Transfer the refurbished item from Return - Refurbish to the MAIN warehouse.        |
|                                     |                                                                                           |
|                                     |     - Book away the used components from the MAIN warehouse.                              |
+-------------------------------------+-------------------------------------------------------------------------------------------+
| *Teresa*                            | 19. Generate the **Invoice (= sales credit note)**.                                       |
+-------------------------------------+-------------------------------------------------------------------------------------------+

# Return to vendor from stock

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **WAREHOUSE MAIN + LOCATION FROM WAREHOUSE**                                                                                                                    |
+=====================================+===========================================================================================================================+
| *Paulo/Miguel*                      | 1.  Navigate to **All Purchase Orders** and create a new PO.                                                              |
|                                     |                                                                                                                           |
|                                     | 2.  Add a negative line with the item in the quantity to be returned.                                                     |
|                                     |                                                                                                                           |
|                                     | 3.  Check if the price is correct.                                                                                        |
|                                     |                                                                                                                           |
|                                     | 4.  In Setup, select the Number sequence group **PurchRET**.                                                              |
|                                     |                                                                                                                           |
|                                     | 5.  Navigate to **Header \> General** and fill in the RMA Number (from the vendor).                                       |
|                                     |                                                                                                                           |
|                                     | 6.  Go to **Line details \> Product** and fill in the **Location** in the warehouse from where you will take the item.    |
|                                     |                                                                                                                           |
|                                     | 7.  Confirm the PO and generate the **Product receipt (=Purchase return packing slip)** and send the goods to the vendor. |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| *Warehouse*                         | 8.  Send the goods to the vendor with the Purchase return packing slip.                                                   |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

# 

# Bonus/Discount for customer

+------------------+----------------------------------------------------------------------------+
| *Isabel/Finance* | 1.  Navigate to **All free text invoices** and click on +NEW.              |
|                  |                                                                            |
|                  | 2.  Select Customer account.                                               |
|                  |                                                                            |
|                  | 3.  Change Number sequence group to **SALESNeg**.                          |
|                  |                                                                            |
|                  | 4.  Select the necessary product code for a bonus.                         |
|                  |                                                                            |
|                  | *OM: outside EU*                                                           |
|                  |                                                                            |
|                  | *EU: inside EU*                                                            |
|                  |                                                                            |
|                  | *MN: in Portugal*                                                          |
|                  |                                                                            |
|                  | 5.  Quantity -1. Add Unit price.                                           |
|                  |                                                                            |
|                  | 6.  Change \"Invoice text\" In the line details with a useful description. |
|                  |                                                                            |
|                  | 7.  Select your negative line, click on **References.**                    |
|                  |                                                                            |
|                  | 8.  In the **Reason code** field, select **Bonus.**                        |
|                  |                                                                            |
|                  | 9.  In the **Reference** field, select **Invoice period**.                 |
|                  |                                                                            |
|                  | 10. Fill In the **from and to date.** Save.                                |
|                  |                                                                            |
|                  | 11. Go back to the SO.                                                     |
|                  |                                                                            |
|                  | 12. Post & generate the **Free text credit note.**                         |
+==================+============================================================================+

# CN to Correct wrong Item price

+-----------------------+----------------------------------------------------------------------------------------------+
| *Sales person/Teresa* | 1.  Navigate to **All Sales Orders** and find the original SO.                               |
|                       |                                                                                              |
|                       | 2.  In the action pane Sell, click on **Credit note**.                                       |
|                       |                                                                                              |
|                       | 3.  Select the Invoice/line/quantity you want to credit (partially).                         |
|                       |                                                                                              |
|                       | 4.  In the **Reason code** field, select **PriceError**.                                     |
|                       |                                                                                              |
|                       | 5.  Click OK. The line(s) will be added In the SO.                                           |
|                       |                                                                                              |
|                       | 6.  Fill in the unit price. (= the difference between the wrong price and the correct price) |
|                       |                                                                                              |
|                       | 7.  Fill in the cost price: 0,01€.                                                           |
|                       |                                                                                              |
|                       | 8.  Print the order confirmation and give to Isabel.                                         |
+=======================+==============================================================================================+
| *Isabel*              | 9.  Approve and give to Teresa                                                               |
+-----------------------+----------------------------------------------------------------------------------------------+
| *Teresa*              | 10. Select your negative line, click on **References.**                                      |
|                       |                                                                                              |
|                       | 11. In the Reason code field, check if the reason code is ok.                                |
|                       |                                                                                              |
|                       | 12. Go back to the SO.                                                                       |
|                       |                                                                                              |
|                       | 13. Click in the Header tab.                                                                 |
|                       |                                                                                              |
|                       | 14. In Setup, select the Number sequence group **SALESNeg**.                                 |
|                       |                                                                                              |
|                       | 15. Click Save.                                                                              |
|                       |                                                                                              |
|                       | 16. Go to **Line details \> Product** and choose the **location** \"CreditOnly\".            |
|                       |                                                                                              |
|                       | 17. Go to **Line Details \> Setup** and tick the checkbox for SCRAP.                         |
|                       |                                                                                              |
|                       | 18. Generate the **Invoice (= sales credit note)**.                                          |
+-----------------------+----------------------------------------------------------------------------------------------+

# 

# Correct wrong invoice

+-----------+--------------------------------------------------------------------------------------------+
| *Teresa*  | A.  **Credit wrong invoice**                                                               |
|           |                                                                                            |
|           |     1.  Navigate to **All Sales Orders** and find the original SO.                         |
|           |                                                                                            |
|           |     2.  In the action pane Sell, click on **Credit note**.                                 |
|           |                                                                                            |
|           |     3.  Select the lines you want to credit.                                               |
|           |                                                                                            |
|           |     4.  In the **Reason code** field, select **Voided. (=Cancel)**                         |
|           |                                                                                            |
|           |     5.  Click OK. The line(s) will be added In the SO.                                     |
|           |                                                                                            |
|           |     6.  Select your negative line(s), click on **References.**                             |
|           |                                                                                            |
|           |     7.  In the Reason code field, check if the reason code is ok.                          |
|           |                                                                                            |
|           |     8.  Go back to the SO.                                                                 |
|           |                                                                                            |
|           |     9.  Click in the Header tab.                                                           |
|           |                                                                                            |
|           |     10. In Setup, select the Number sequence group **SALESNeg**.                           |
|           |                                                                                            |
|           |     11. Click Save.                                                                        |
|           |                                                                                            |
|           |     12. Go to **Line details \> Product** and choose the warehouse and location **ADMIN**. |
|           |                                                                                            |
|           |     13. Generate the **Invoice (= sales credit note)**.                                    |
+===========+============================================================================================+
| *Isabel*  | 14\. Give a copy to Isabel to inform (no approval, it is necessary CN and invoice)         |
+-----------+--------------------------------------------------------------------------------------------+
| *Teresa*  | B.  **Generate new correct invoice**                                                       |
|           |                                                                                            |
|           |     1.  Create new SO with correct Information.                                            |
|           |                                                                                            |
|           |     2.  Copy all CN lines from original SO.                                                |
|           |                                                                                            |
|           |     3.  Check if warehouse and location are set to **ADMIN**.                              |
|           |                                                                                            |
|           |     4.  Generate invoice.                                                                  |
+-----------+--------------------------------------------------------------------------------------------+

# How to deal with Bundles

The transaction for bundles are posted on their components. However, It Is not possible to explode a bundle with a negative quantity. Use the following steps Instead for bundle Items.

![A screenshot of a computer Description automatically generated](media/image3.png){width="7.917361111111111in" height="1.1597222222222223in"}1. Add all the bundle components with a negative quantity

![A screenshot of a computer Description automatically generated](media/image4.png){width="3.6180555555555554in" height="1.8736111111111111in"}

2\. Change warehouse and location depending on the situation

Change location to **Creditonly** In case of a wrong price

Change **warehouse and location** to **ADMIN** In case of a wrong Invoice account or VAT group

3\. Generate Invoice.

In case a new correct Invoice has to be generated:

4\. Add bundle components with correct VAT group.

5\. Change warehouse and location to ADMIN.

6\. Check If prices are OK.

8\. Generate Invoice.

9\. The components will be printed on the document In this case, so some extra Information towards the customer In the email might be necessary.
