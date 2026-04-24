# KB — F&O Changing BOM component in production

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Changing BOM-component in production.docx`
**Conversiedatum:** 2026-04-24

---

# How to DELETE A BOM COMPONENT IN A PRODUCTION ORDER (MTO or MTS)

- **[Production order has status \'Reported as Finished\']{.underline}**

<!-- -->

- It\'s too late, you can\'t change the BOM anymore.

<!-- -->

- **[Production order status = \'Started\' or \'Released\' and at least one component is picked and put on PSTAGE]{.underline}**

<!-- -->

- Pick all components (also the bad component).

- In Tulip, Start your production order and register the Produced goods.

- In Tulip, go in the \'Declare consumed goods\' screen. In the lower half of the screen, select the item that you want to see deleted from the BOM. Click on the \'Adjust Product\' button. In the following screen, enter the amount you have picked of this item in the \'Rest\' box and click on \'Continue\'. Now click on the \'Post\' button.

> ![A screenshot of a computer Description automatically generated](media/image2.png){width="5.451327646544182in" height="3.081395450568679in"}
>
> ![A screenshot of a computer Description automatically generated](media/image3.png){width="3.813934820647419in" height="2.6333333333333333in"}

- A new RAW label is printed for a newly created license plate that contains the deleted BOM-component. In the scanner, go to \'Production\>Return components to stock\'. Scan the label to put the deleted BOM-component back on stock.

> ![A screenshot of a computer Description automatically generated](media/image4.png){width="4.0116272965879265in" height="2.9452449693788276in"}

- **[Production order status = \'Released\' or lower and no components are picked yet]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled, then to Estimated and then to Created.

- Go in the BOM of the production order and delete the bad component.

- Estimate & Schedule again.

- Release the load again (in case of MTO production) or the production order (in case of MTS production). You can now continue to pick and produce.

# How to ADD A BOM COMPONENT IN A PRODUCTION ORDER (MTO or MTS)

- **[Production order has status \'Reported as Finished\']{.underline}**

<!-- -->

- It\'s too late, you can\'t change the BOM anymore.

<!-- -->

- **[Production order status = \'Started\' or \'Released\' and at least one component is picked and put on PSTAGE]{.underline}**

<!-- -->

- In Tulip, Start your production order.

- In Tulip, in the production order details, click the \'Material Request\' button.

> Select an existing raw material if you want to pick extra of an existing BOM-component or enter a new item by scanning the stock label with the designated Shopfloor-scanner (the new item should appear in the Product ID box).

![](media/image5.png){width="6.268055555555556in" height="3.545138888888889in"}

- Enter your quantity in the \'Update Quantity\' box. Click the \'Adjust Quantity\' button.

- Your item should have appeared in the raw materials list now with the quantity in the column \'Reserved With Work\'.

> If the item is not immediately visible, then exit the \'Material Request\' screen and enter again.
>
> If the quantity is in another column than \'Reserved With Work\', then click on the \'Generate all work\' button. It should switch columns after clicking that button.

- You can now pick this component (and other components that were not picked yet) using the normal picking process with your picking scanner.

> You can start the picking by scanning the barcode on your picking list or by clicking the \'Show Barcode\' button in Tulip and scan that barcode.

- After picking is finished, you can continue the normal production process. The added BOM-component will get consumed properly.

<!-- -->

- **[Production order status = \'Released\' or lower and no components are picked yet]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled, then to Estimated and then to Created.

- Go in the BOM of the production order and add the new component.

- Estimate & Schedule again.

- Release the load again (in case of MTO production) or the production order (in case of MTS production). You can now continue to pick and produce.
