# KB — F&O Transport in Sales orders

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Transport in Sales orders.docx`
**Conversiedatum:** 2026-04-24

---

# Add transport immediately in load with goods

Create new SO.

Add items in SO.

Add transport line in SO.

Add all available items + transport line in load. (Via Warehouse - Outbound load planning workbench)

Transport line will automatically be \"picked\" when you click on **Release to warehouse** in the load.

The line is [not]{.underline} visible on the picking list and the packing list.

Then you **confirm outbound shipment** and generate the **packing slip**.

The line is visible on the packing slip.

You can still add cost and sales price until you generate the **invoice.**

# Add transport after goods were released to warehouse, before \"confirm outbound shipment\"

When you notice that you have forgotten to add a transport line to a load and you have not yet **confirmed outbound shipment,** you can still add the transport to the same load.

Go to an SO in the load.

Add transport line in SO.

Add the transport line to the existing load. (Via Warehouse - Outbound load planning workbench)

Transport line will automatically be \"picked\" when you click on **Release to warehouse** in the load.

Then you can follow the normal steps for your load. When you get back the outbound load list from the warehouse, you **confirm outbound shipment** and generate the **packing slip**.

# Add transport after goods were sent and packing slips already made

Go to the SO of the goods that have been sent.

Add transport line with cost and sales price.

Add line to new load. (Via Warehouse - Outbound load planning workbench)

Transport line will automatically be \"picked\" when you click on **Release to warehouse** in the load.

Then you **confirm outbound shipment** and generate the **packing slip**.

The line is visible on the packing slip.

If you want to manually choose the packing slip date, you have to generate the packing slip from the SO and not the load. So, after you **confirm outbound shipment**, go back to the SO and generate the **packing slip.** The picture below shows where you can change the date:

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="3.15in"}

![A screenshot of a computer screen Description automatically generated](media/image3.png){width="6.268055555555556in" height="3.536111111111111in"}
