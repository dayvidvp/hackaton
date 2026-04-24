# KB — F&O Sales Process

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales Process.docx`
**Conversiedatum:** 2026-04-24

---

**Sales Process**

1.  Create SO manually or from quotation and process the SO:

    - Navigate to **All sales orders** and click on **+New.**

    - Add SO lines in correct quantities.

    - Add a transport line if there is delivery.

    - Add confirmed ship date.

    - Explode any bundles.

    - Create any production orders.

2.  Estimate / Schedule **production order** if applicable.

3.  Send **order confirmation** to the customer. (Validation of credit status & markups)

4.  Process **credit management hold list** if necessary.

5.  Add sales lines to an **outbound load**:

    - Starting from SO or from **Sales line availability**

    - Via **Warehouse \> Outbound load planning workbench**

    - NEW: Select the lines and click on **Supply and demand \> To new load**

    - EXISTING: Select the lines and the load and click on **Supply and demand \> To existing load**

6.  Prepare picking/production:

    - Add cut-off date in the load.

+-----------------------------+-------------------------------+---------------------------------+
| **Only normal picking**     | **Only production**           | **Production & normal picking** |
+=============================+===============================+=================================+
| Release to warehouse        | Release to warehouse          | Release to warehouse            |
|                             |                               |                                 |
| Print outbound picking list | Print production picking list | Print production picking list   |
|                             |                               |                                 |
|                             |                               | Print outbound picking list     |
+-----------------------------+-------------------------------+---------------------------------+
|                             | Assign production             | Assign production               |
+-----------------------------+-------------------------------+---------------------------------+

7.  Process picking & assembly via scanner. Add measurements In case of transport.

8.  Prepare outbound load:

    - If needed, change shipments to the correct load.

    - In case of transport:

      - Book transport based on measurements in **License plate summary**.

      - Print transport labels

      - Print packing list(s)

      - Add Transport cost & price in Sales order.

    <!-- -->

    - Print **Outbound load list**.

9.  Load to truck via scanner (when goods are picked up).

10. Finish delivery:

    - Via **Ship and receive \> Confirm \> Outbound shipment.** Automated if all LP\'s from the load are loaded in truck with the scanner.

    - Via **Ship and receive \> Generate \>** **Packing slip.** This step can be automated.

    - Go back to the loads overview, select the load, via **Loads \> Finish** load. This step also happens automatically.

11. Generate invoice

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image1.emf)

- **Sales order release status**

![](media/image2.emf)

- **Outbound load status**

![](media/image3.emf)

![A close up of a text Description automatically generated](media/image4.jpeg){width="2.4833333333333334in" height="0.3864107611548556in"}

![A white box with black text Description automatically generated](media/image5.jpeg){width="3.6041666666666665in" height="0.5687182852143482in"}
