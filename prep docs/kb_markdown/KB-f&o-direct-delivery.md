# KB — F&O Direct Delivery

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Direct Delivery.docx`
**Conversiedatum:** 2026-04-24

---

Direct deliveries are deliveries that are sent directly from the vendor to your customer.

1.  Create sales order with lines.

2.  Create Direct Delivery purchase order with lines.

3.  Link is automatically created.

4.  Send purchase inquiry to vendor.

5.  Process vendor confirmation.

6.  Process vendor delivery note by posting the product receipt in the PO.

7.  The packing slip in the SO is automatically generated.

8.  Post the sales invoice.

9.  Process the purchase invoice.

 

- **[Sales order]{.underline}**

<!-- -->

- Create a sales order

- Add order lines for goods and for transport!

- Change **warehouse** and **location** to "Direct delivery". The location should update automatically when you change the warehouse.

- Via **Sales order \> New**, select **Direct delivery**.

- **Select the lines** that must be handled as a direct delivery.

- Set any **parameters**.

- It is possible to change the **Vendor** if necessary. For transport, make sure to change the vendor to the same vendor as the goods!

- Click **OK**.

 

- **[Link between SO and PO]{.underline}**

> The **purchase order** can be found in de action pane **General \>** **Related information \> Purchase order** or in the **Order line details** under **Product \> Reference number**.
>
>   
>
> Synchronized between both orders: 

- When you update the Requested receipt date field on the sales order line, the Delivery date field on the corresponding purchase order line is also updated. 

- When you update the Confirmed receipt date on the purchase order line, the Confirmed receipt date and Confirmed ship date fields on the corresponding sales order line are updated. 

- When you create a direct delivery, the customer\'s address is automatically entered as the delivery address. (Set parameter with checkbox) Changes to the address are synchronized. 

> When you try to delete a sales order line that has a delivery type of Direct delivery, a message box states that purchase order lines are attached to the line. If the sales order line has been partially delivered, you can\'t delete the sales order line or the purchase order lines that are attached to it.

 

- **[Process the Purchase order]{.underline}**

<!-- -->

- Via **Purchase \>** Generate, send the **Purchase inquiry** to the Vendor.

- Process the Vendor confirmation.

- Via **Purchase \> Actions \> Confirm** the Purchase order.

- When the Vendor informs you that the goods have been delivered, go to **Receive \> Generate \>** **Product receipt.** (Fill in the Delivery Note number from the Vendor)

- The **Packing slip** in the SO is automatically generated.

**[Remarks:]{.underline}**

- Every significant change made to the purchase order will **change the status** back from Confirmed to Approved.

- Every **PO needs to be confirmed** to generate a product receipt and process the vendor invoice.

- In case you have to **change the price** in the PO, you need to choose the correct **reason code**.

- If all lines in the SO are direct delivery, it\'s easier to change the warehouse in the Header then to do it line by line.

- It is **not possible** to link an existing purchase order line to a sales order as a direct delivery. If you want to follow the \'direct delivery\'-flow, you need to create the purchase order from your sales order, as described in the process in this manual.

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image2.emf)

- **Sales order release status**

![](media/image3.emf)

- **Purchase order status**:

![](media/image4.emf)

- **Purchase order approval status:**

![](media/image5.emf)

# How to change direct delivery to regular sales order

Sometimes goods get delivered in the company\'s warehouse instead of directly to the customer. Here\'s how we can change the sales/purchase order to turn a direct delivery into a regular sales order:

1\) Select the first SO-line and click on **Inventory\>Maintain\>Marking**:

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="6.268055555555556in" height="2.709722222222222in"}

On the Marking page, search for the line that connects to the direct delivery purchase order. Type value 0 in the **Mark now** column and check the box in the column **Set mark now**. Then click OK.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="3.6486111111111112in"}

Repeat this for every SO-line that should be changed.

2\) Hard refresh the SO details-page. Change the **warehouse** on the header or SO-lines to MAIN and blank out the **location** field. Save.

3\) Go into all SO line details and change the Direct delivery-parameter to \"No\". Save. Confirm the sales order.

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="6.268055555555556in" height="3.425in"}

4\) Go to the PO details-page of the PO that was marked against the SO as a direct delivery. Change the **warehouse** on the PO-lines to MAIN and blank out the **location** field. Save.

5\) Go into all PO line details and change the Direct delivery-parameter to \"No\". Save.

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="4.236111111111111in"}

*[Remark]{.underline}: There is also a \"Direct delivery\"-parameter on the Header. It is set to \"Yes\" and you can\'t change it anymore. But that\'s no problem as long as you change the parameter on the SO lines.*

6\) In the PO Header you can change the delivery address to your own warehouse if you want to. If you do that, you will also have to change the e-mail address. Save and a pop-up will appear to update this delivery address to all the PO lines.

Confirm the purchase order.

7\) You can now make an inbound load and receive the purchase order like any other purchase order. On the sales side, you can also make an outbound load to send goods from the warehouse to the customer.
