# KB — F&O Purchase orders

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase orders.docx`
**Conversiedatum:** 2026-04-24

---

# Create purchase order

+--------------------------------------------------+----------------------------------------------------------+
| **3 different ways to create a purchase order**  | **4 different ways to add lines to a purchase order**    |
+==================================================+==========================================================+
| - firming planned orders (master planning)       | - planned orders from master planning                    |
|                                                  |                                                          |
| - creating a new PO manually                     | - adding lines manually                                  |
|                                                  |                                                          |
| - creating a PO from an SO (for direct delivery) | - copying lines from an existing PO                      |
|                                                  |                                                          |
|                                                  | - copying lines from the linked SO (for direct delivery) |
+--------------------------------------------------+----------------------------------------------------------+

Direct delivery has a different process, which is explained in a separate document.

- **[Firm planned order]{.underline}**

<!-- -->

- Run the master planning.

- Select/change planned purchase orders and **firm** them.

- Purchase orders with all the lines are created automatically.

- Via **All purchase** orders, go to the PO\'s and process following the normal purchase process.

<!-- -->

- **[Create new purchase order manually]{.underline}**

<!-- -->

- Navigate to **All purchase orders**

- Click on **+New**.

- Choose the **Vendor account**.

- Add a **Reference.**

- Click on **OK.**

- Add the (requested) **Delivery date** in the header.

- Add purchase order lines.

+---------------------------------------------------------------------------+-------------------------------------------------------------+
| **Add lines manually**                                                    | **Copy lines from an existing PO**                          |
+===========================================================================+=============================================================+
| - **+Add line** if you know the item number.                              | Go to **Purchase order \> Copy** and click on **From all**. |
|                                                                           |                                                             |
| - **+Product selection** to search for the item.                          | - Select from the headers.                                  |
|                                                                           |                                                             |
| - Don\'t forget the **Configuration** if it applies.                      | - Select the lines you want to copy.                        |
|                                                                           |                                                             |
| For each line:                                                            | - Set the **Parameters**.                                   |
|                                                                           |                                                             |
| - Fill in the **Quantity.**                                               | - Click on **OK**.                                          |
|                                                                           |                                                             |
| - Check/fill in/edit/refresh the **Unit price, Cost price and Discount.** |                                                             |
+---------------------------------------------------------------------------+-------------------------------------------------------------+

**[Remarks:]{.underline}**

- Via **Header \> Setup \> Prices on purchase order**, you can add the unit prices to the purchase inquiry.

- In both the header and the lines, you can add specific document texts.

- Via **Line details \> Delivery**, you can set an allowance % for under delivery.

- Via **Bundle** in the purchase order lines, you can explode a purchase bundle and make changes to the price or deliver remainder.

- Via **Inventory** in the PO lines, you can easily access the **on-hand** and **transactions** of the selected item.

- Via **Purchase order \> View \> Totals**, you can easily access the total value of the PO.

- Via **General \> vendor \> Trade agreements**, you can easily access all trade agreements for the vendor.

# Send Purchase inquiry

- Navigate to **Purchase \> generate** and click on **Purchase inquiry**.

- Make sure printer settings are correct and click **OK.**

The approval status changes from \"Approved\" to \"In external review\".

# Process vendor confirmation

**[Quantities]{.underline}**

Because the PO is not yet \"confirmed\", you can change the quantity easily in the line.

If the vendor changes it because of a **minimum order quantity** or **order multiple**, you can also change this on the **Released product**.

If it is not possible to change the quantity, you can change the **Deliver remainder** via **Update line.**

**[Prices]{.underline}**

If the purchase price is not the same or was missing in the PO, there are several options:

- You don\'t agree with the vendor and contact them, you don\'t change the price in the PO.

<!-- -->

- You have to **change the price** in the PO, so you need to choose the correct **reason code**:

  - CHECK: price needs to be checked by responsible

  - EXCH: difference due to exchange rate

  - FREE: automatically chosen in case you use checkbox Free

  - NEW: when the price you entered will be the new price and we accept it

  - NOPC: no price check needed is for items that always have a different price (ex. transport)

  - ROUND: rounding difference (ex. vendor has 3 decimals and we only have 2)

  - SPEC: one-time special price (ex. early buy, big quantity, special discount)

**[Search names and item references]{.underline}**

If you notice a discrepancy in the vendor reference/search name, check this thoroughly. It is possible the Vendor made a mistake but, it is also possible that an item has changed and is no longer in use.

**[Delivery dates]{.underline}**

You have to add the **Confirmed delivery date** in the PO:

- Fill in the date in the header, **Save** and **Update the order lines**. In the pop-up menu, change the checkbox **Update confirmed delivery date** to **Yes.**

- Fill in the date in the lines separately.

- In rare cases, the vendor will split up the quantity in multiple deliveries. You can split up the purchase order line with a delivery schedule:

  - Go to **Purchase order line** and click on **Delivery schedule.**

  - A new window opens with the existing line. You can change that quantity and add extra lines. Add the **Confirmed delivery date** for each line. Click **OK.**

  - In the PO, you will now see the original line and the 2 split-lines with special icons.

- If the Vendor can\'t confirm the delivery date, leave it empty and still \"**Confirm**\" the PO.

**[Transport cost]{.underline}**

In some cases, the transport cost is not included in the purchase price and has to be added to a separate purchase order line. Use the item \"**Purchased transport for purchasing\"**.

When you are done, **Confirm** the PO via **Purchase \> Actions** \> **Confirm.** The **Approval status** is now \"Confirmed\". This shows to other users that the Vendor confirmation has been processed.

**[Remarks:]{.underline}**

- Every significant change made to the purchase order will **change the status** back from Confirmed to Approved.

- Every **PO needs to be confirmed** to generate a product receipt and process the vendor invoice.

- In case of **overdelivery** you will need to add a line to the PO and add this line to the load. Confirm the PO again.

- In case of **underdelivery** you will need to adjust the quantity of your load line (reverse the shipment confirmation if necessary). Then add the remainder of your PO-line to a new load or update the PO-line and set the remainder to zero.

- In the SO Line details, you can check the line as a crossdock line. This means that during inbound, it will be send to the crossdock location, instead of another location in the warehouse.

**[Status changes:]{.underline}**

- **Purchase order status**:

![](media/image2.emf)

- **Approval status:**

![](media/image3.emf)
