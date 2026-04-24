# KB — F&O Production cancellation AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production cancellation AQD.docx`
**Conversiedatum:** 2026-04-24

---

When an order is set on hold / cancelled, we need to block production asap.

\> You cannot \"just cancel\" the sales line because the linked production order will NOT be cancelled

automatically.

\> You cannot \"just cancel\" the production order because the automatic batch jobs will re-create a new production order

\> You cannot \"just cancel\" the production order if the production order was already (partly) produced - ALWAYS check with production before cancelling

# SALES

1.  Open \'All sales orders\' and open the concerned sales order 

![Picture 1, Afbeelding](media/image2.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

2.  Open the sales order and select the line you want to cancel 

![Picture 2, Afbeelding](media/image3.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

3.  Go to \'line details\' and open the tab \'Product\' 

![Picture 3, Afbeelding](media/image4.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

4.  Note the linked production order \"Production orders\" \
    **[Email the production order number and the AQDT number to the production planner.]{.mark}** \
    Example: SO2510513-1300 AQDT-00000331 cancelled production order PC01001808 

![Picture 4, Afbeelding](media/image5.jpeg){width="6.268055555555556in" height="3.5in"} 

5.  IF ORDER CANCELLED: \
    Now cancel the line by setting the deliver remainder = 0 \
    Click \"Update line\" 

![Picture 5, Afbeelding](media/image6.jpeg){width="6.268055555555556in" height="3.5in"} 

a.  Click here 

![Picture 6, Afbeelding](media/image7.jpeg){width="6.268055555555556in" height="3.4944444444444445in"} 

b.  Click here 

![Picture 7, Afbeelding](media/image8.jpeg){width="6.268055555555556in" height="3.5in"} 

c.  Verify the \"Line status\" which is now \'Canceled\' - Congrats! you\'re done :-) 

![Picture 8, Afbeelding](media/image9.jpeg){width="6.268055555555556in" height="3.5in"} 

6)  IF ORDER ON HOLD: 

    a)  Verify you\'re in edit mode 

![Picture 9, Afbeelding](media/image10.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

b)  Set complete order = No 

![Picture 10, Afbeelding](media/image11.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

c)  Click \"Save\" 

![Picture 11, Afbeelding](media/image12.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

d)  Click \"Block production creation\" 

> ![](media/image13.emf){width="4.502837926509186in" height="3.537516404199475in"}

 

e)  Click \"Save\" \
    Congrats! you\'re done :-) \
    There won\'t be an automatic production order creation until you unset the \'block production creation\' on the salesline 

![Picture 13, Afbeelding](media/image14.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

# PRODUCTION

**[Status changes:]{.underline}**

- **Production order status:**

![A diagram of a flowchart Description automatically generated](media/image15.png){width="6.268055555555556in" height="1.7881944444444444in"}

## How to Cancel production orders

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

- Beware when cancelling or reducing MTO-production orders. We still have load lines and sales lines that might require new production or that have to be cancelled/reduced as well.

- There is no fast way to transfer picked raw materials from one production order to another production order. We have to unpick everything and then pick everything.
