# KB — F&O Sales orders

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales orders.docx`
**Conversiedatum:** 2026-04-24

---

# Create sales order

+----------------------------------------------+----------------------------------------------------+
| **2 different ways to create a sales order** | **3 different ways to add lines to a sales order** |
+==============================================+====================================================+
| - Confirming a quotation                     | - Automatic lines from quotation confirm           |
|                                              |                                                    |
| - Creating a new SO manually                 | - Adding lines manually                            |
|                                              |                                                    |
|                                              | - Copying lines from an existing SO                |
+----------------------------------------------+----------------------------------------------------+

Direct delivery has a different process, which is explained in a separate document.

- **[Create new sales order manually]{.underline}**

  - Navigate to **All sales orders.**

  - Click on **+New**.

  - Select the **Customer account.**

  - Set the correct Delivery address. You can create a new delivery address by clicking on +.

  - Fill in the **Customer requisition** and **Customer reference.**

  - Verify the **Mode of delivery. (important to choose correct load)**

  - Click **OK.**

+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
| **Add lines manually**                                                    | **Copy lines from an existing SO**                                        |
+===========================================================================+===========================================================================+
| - **+Add line** if you know the item number.                              | Go to **Sales order \> Copy** and click on **From all**.                  |
|                                                                           |                                                                           |
| - **+Product selection** to search for the item.                          | - Select from the headers.                                                |
|                                                                           |                                                                           |
| - Don\'t forget the **Configuration** if it applies.                      | - Select the lines you want to copy.                                      |
|                                                                           |                                                                           |
| <!-- -->                                                                  | - Set the **Parameters**.                                                 |
|                                                                           |                                                                           |
| - Fill in the **Quantity.**                                               | - Click on **OK**.                                                        |
|                                                                           |                                                                           |
| - Check/fill in/edit/refresh the **Unit price, Cost price and Discount.** | - Check/fill in/edit/refresh the **Unit price, Cost price and Discount.** |
|                                                                           |                                                                           |
| - Add the **confirmed ship date.**                                        | - Add the **confirmed ship date.**                                        |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+

**[Remarks:]{.underline}**

- Always add a line **Transport cost (Transport SLS)**, when the goods have to be delivered.

- The **load advice** clearly shows if an item is available.

- Via the **Reservation allocation center** it is possible to re-allocate stock from one SO to another.

- When you want to lift the stock reservation of a SO-line without deleting the SO-line, you need to go to **Line details \> Setup \> Reservation** and set it to \'Manual\'. Also, make sure the reservation is set to 0 for the SO-line via **Inventory \> Maintain Reservation.**

- Via **Header \> Setup \> Hide prices on the confirmation**, you can make sure the customer does not see the prices on the confirmation.

- Via **Bundle** in the sales order lines, you have to explode a sales bundle to proceed. Via this menu you can also make changes to the price or deliver remainder.

- In case there is a Production MTO item in the SO, you need to create a production order via **Product and supply \> New \> Production order**. The PC needs to be estimated and scheduled to put in a load.

- Via **Inventory** in the SO lines, you can easily access the **on-hand** and **transactions** of the selected item.

- Via **Sales order \> View \> Totals**, you can easily access the total value of the SO.

- Via **General \> Customer \> Trade agreements**, you can easily access all trade agreements.

- **Sales tax**: for each customer there is a default sales tax group based on their country. Thanks to the new RCS system, the sales tax group will automatically be changed in the lines when you choose a delivery address in a different country.

- Checkbox **Complete order** guarantees that the lines can only be sent together when everything is in stock.

- Checkbox **Block shipment** can be used to make sure a specific SO cannot be processed in a load.

- Checkbox **PWGPackPerOrder** can be used to make sure that a sales order is packaged completely separately from other orders going to the same customer.

- In the **Free shipping threshold** you can see the franco amount of a customer. (1= always franco)

# Send confirmation

It is very important to generate the order confirmation. This will enable the system to do a price and mark-up validation. At this moment, the system will also check if there are any blocking rules that put the SO in credit management.

Via **Sell \> Generate \> Confirm sales order** you will be able to choose the printer setting. If there is no need for that just go to **Sell \> Actions \> Confirm**.

Any remarks regarding the price and mark-up validation are just a warning. They only become blocking upon invoicing.

Any remarks regarding credit management are blocking and have to be resolved to proceed with the order.

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image2.emf)

- **Sales order release status**

![](media/image3.emf)

# How to delete SO-line with marked MTO-production

There are basically 4 different scenarios:

1\) [No production quantities have been reported as finished]{.underline}:

Delete the production order by following the steps in manual [F&O Production cancellation.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Production%20cancellation.docx?d=w5e6896cab8304e2b8939d583b5e7ec8c&csf=1&web=1&e=bGihYg)

Then delete the load line and the SO-line.

2\) [Part of the full production quantity has been reported as finished (Prod order status = Started)]{.underline}:

Decrease the quantity of the production order so that it matches the produced quantity. Report the production order as finished.

Decrease the quantity of the load line so that it matches the produced quantity.

Unpick the produced LP\'s.

Remove the load line (hard refresh might be necessary beforehand).

Select the SO line and go to **Inventory \> Maintain \> Marking**. Undo the marking with the Prod. order.

Remove the SO line.

3\) [The full production quantity has been reported as finished (Prod. order status = Started or RAF)]{.underline}:

If not yet the case, report the production order as finished.

Unpick the produced LP\'s.

Remove the load line (hard refresh might be necessary beforehand).

Select the SO line and go to **Inventory \> Maintain \> Marking**. Undo the marking with the Prod. order.

Remove the SO line.

4\) [Production order status = Ended]{.underline}:

Unpick the produced LP\'s.

Remove the load line (hard refresh might be necessary beforehand).

Select the SO line and go to **Update line \> Update \> Deliver remainder.** Set the remainder to 0 and click OK. The line status will be \'Canceled\'. It is however not possible anymore to delete the line.
