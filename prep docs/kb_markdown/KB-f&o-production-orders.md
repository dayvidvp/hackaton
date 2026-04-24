# KB — F&O Production orders

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production orders.docx`
**Conversiedatum:** 2026-04-24

---

[**MTS**-production]{.underline}: Make-to-stock. Produce MTS-items when the stock levels dip below the minimum inventory levels. The produced quantities are sent to stock locations in the warehouse. MTS-production orders are not linked to SO-lines.

[**MTO**-production]{.underline}: Make-to-order. Produce MTO-items for specific sales orders in the exact quantity the customer orders. The produced quantities are sent to the staging location for outbound delivery. MTO-production orders are always linked to SO-lines. MTO-items have no minimum inventory levels defined.

**[Remarks:]{.underline}**

- A MTS-item can also undergo MTO-production, if the requested quantity of the sales order is larger than the current stock level.

- A MTO-item can also undergo MTS-production, if the requested quantity of the sales order is smaller than the optimal production batch size. In that case two production orders will be made for the same item: one MTO-production that equals the size of the SO-line and one MTS-production that equals the optimal production batch size minus the size of the SO-line.

- Both of the remarks above should be rare events and the question should be asked if the MTO/MTS status of the item should be changed.

# Create production order

+------------------------------------------------------+
| **3 different ways to create a production order**    |
+======================================================+
| - firming planned orders (master planning) (**MTS**) |
|                                                      |
| - creating a new order manually (**MTS**)            |
|                                                      |
| - creating an order from a SO-line (**MTO**)         |
+------------------------------------------------------+

- **[Firm planned order (MTS)]{.underline}**

<!-- -->

- Run the master planning (via **Master planning \> Workspaces \> Master planning**).

- Select/change planned production orders and **firm** them (via **Master planning \> Master planning \> Planned orders**). The **Sales order** column shows which planned orders are MTO and which ones are MTS.

- Production orders for all the lines are created automatically.

- Via **All production orders**, go to the production orders and process following the normal production process.

> **[Remark:]{.underline}**

- We advise to use the Master planning only for MTS-production. MTO-production orders are more time-sensitive and should be made ad hoc when entering SO-lines.

<!-- -->

- **[Create new production order manually (MTS)]{.underline}**

<!-- -->

- Navigate to **All production orders**

- Click on **+New**.

- Choose the **Item number**.

- Choose the **Configuration** if applicable.

- Choose the production **Quantity**.

- Choose a **Delivery** date.

- Click on **Create.**

- Process further following the normal production process.

<!-- -->

- **[Create new production order from a SO-line (MTO)]{.underline}**

<!-- -->

- Navigate to **Sales order details**

- Select a SO-line.

> The column **Line Advice** will inform you If this Item Is defined as MTO

- Click on **Product and supply \> Production order**.

- The **Create production order** page appears with all fields automatically filled in. The delivery date equals the confirmed ship date of the SO-line. Click on **Create**.

- Process further following the normal production process.

**[Status changes:]{.underline}**

- **Production order status:**

![A diagram of a flowchart Description automatically generated](media/image2.png){width="6.268055555555556in" height="1.7881944444444444in"}
