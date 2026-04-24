# KB — F&O Production cancellation

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production cancellation.docx`
**Conversiedatum:** 2026-04-24

---

**[Status changes:]{.underline}**

- **Production order status:**

![A diagram of a flowchart Description automatically generated](media/image2.png){width="6.268055555555556in" height="1.7881944444444444in"}

# How to Cancel production orders

- **[Status = Created]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Delete**

<!-- -->

- **[Status = Estimated]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Created.

- Via **All production orders**/**Production order (details) \> Delete**

<!-- -->

- **[Status = Scheduled]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Estimated and then to Created.

- Via **All production orders**/**Production order (details) \> Delete**

<!-- -->

- **[Status = Released, picking not yet started]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled, then to Estimated and then to Created.

- Via **All production orders**/**Production order (details) \> Delete**

<!-- -->

- **[Status = Released, picking in process]{.underline}**

<!-- -->

- Stop the picking process. On the scanner, click on **Done** and put the already picked goods on PSTAGE.

- Go to **All production orders**/**Production order (details) \> Warehouse \> Work details**. Select the Work ID\'s that still have Work status \'Open\' and cancel them (via Work \> Cancel work).

- Process further in the step \'Status = Released, picking finished\'

<!-- -->

- **[Status = Released, picking finished]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled and then to Estimated.

- Via **Production order (details) \> Warehouse \> Stop and Unpick**.

- Via **Production order (details) \> Warehouse \> Remove Stop**.

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Created.

- Via **All production orders**/**Production order (details) \> Delete**

<!-- -->

- Return the raw materials on Prodin to the stock locations with the scanner via **Production \> Return components to stock**.

<!-- -->

- **[Status = Started, no produced goods registered]{.underline}**

<!-- -->

- In Shopfloor, press the **Undo Start** button.

- Process further in the step \'Status = Released, picking finished\'.

<!-- -->

- **[Status = Started, some produced goods registered]{.underline}**

<!-- -->

- **[Remark]{.underline}**: At this point it is no longer possible to cancel the production order. We can only reduce the production order quantity to the produced quantity that is already registered. Via **Production order (details) \> Edit** and then search for the production quantity and adjust it. Save afterwards. Don\'t forget to declare the remaining raw materials in Shopfloor and return them with the scanner.

<!-- -->

- **[Status = Started, all goods produced and registered]{.underline}**

- **[Status = Reported as finished]{.underline}**

<!-- -->

- No longer possible at this point to cancel or reduce production.

**[Remarks:]{.underline}**

- When you want to delete a production order you might come across an error similar to this one:

![](media/image3.png){width="6.260416666666667in" height="0.3229166666666667in"}

> This error means that your production order is a MTO production order for a customer and one or more SO lines are connected to the production order via the \'Production ID MTO\'-column (special sales picking). We need to do some additional steps in order to delete the production order.
>
> Select the SO line with the MTO-production order and click on \'Inventory\'\>\'Maintain Marking\':

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.7944444444444445in"}

> Break the mark between SO line and production order by entering the negative quantity of the production quantity in the \'Mark now\' column. Check the box in the \'Set mark now\' column. Now click \'OK\'.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="3.376388888888889in"}

> Now you will be able to delete the production order.

- Beware when cancelling or reducing MTO-production orders. We still have load lines and sales lines that might require new production or that have to be cancelled/reduced as well.

- There is no fast way to transfer picked raw materials from one production order to another production order. We have to unpick everything and then pick everything.
