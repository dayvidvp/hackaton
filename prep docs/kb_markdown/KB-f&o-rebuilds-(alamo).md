# KB — F&O Rebuilds (ALAMO)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Rebuilds (ALAMO).docx`
**Conversiedatum:** 2026-04-24

---

# Rebuild specifically for a sales order via inventory adjustment journal 

During order entry the sales person notices that an Item Is not In stock but could be rebuilt.

Because It Is Impossible to add sales order lines to a load that are not In stock, the \"to be built\" Item needs to be booked In stock before adding the lines to a load.

The sales person creates a new Inventory adjustment journal with Reason code 40 (Conversion of items).

[Inventory adjustment \-- Finance and Operations](https://pwg-prod.operations.eu.dynamics.com/?cmp=1400&mi=InventJournalTableLossProfit)

In the journal the sales person adds the \"to be built\" Item In the needed quantity on the location REBUILD and with the Inventory status REBUILD. Plus he also adds all the lines for alle the Items needed to do the build. The journal needs to be printed and posted.

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.268055555555556in" height="2.2131944444444445in"}

In the sales order line, the **[Inventory status]{.underline}** for this Item also needs to be changed from Available to REBUILD.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="3.35625in"}

Only then, the load advice will become OK and It will be possible to add the lines to a load. Then the load lines can be \"Released to warehouse\" and the Outbound picking list can be printed.

Give the printed journal to a warehouse employee together with the picklist of the load.

The Inventory status is indicated as a comment on the Outbound picking list. The warehouse employee know by seeing this that he first has to rebuild this item. Because the journal Is attached, the warehouse employee knows It Is not with the scanner (option 1).

# Pro-actively rebuild multiple pieces via inventory adjustment journal

Create an inventory adjustment journal and add all the item transaction lines to rebuild the items you want. They are not meant for a specific sales order so the location is back in to stock with Inventory status AVAILABLE, not REBUILD.

Pay attention to the cost price that always needs to be filled it!

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="2.113888888888889in"}

# EXTRA: How to copy inventory adjustment journals

Go to the Inventory adjustment journal that you want to copy. Via Functions \> Copy.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="5.372096456692914in" height="2.039681758530184in"}

Then Click ok In the pop-up menu.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="1.1232622484689414in" height="1.974413823272091in"}

Go back to the overview of the journals and find your new journal.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.8805555555555555in"}

You can still make changes and then print the journal to give to the warehouse. Don\'t forget to post It!

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="6.268055555555556in" height="3.3555555555555556in"}

# NOT IN USE - Rebuild specifically for a sales order via rebuild functionality in scanner

During order entry the sales person notices that an Item Is not In stock but could be rebuilt easily by someone In the warehouse.

Because It Is Impossible to add sales order lines to a load that are not In stock, the \"to be built\" Item needs to be booked In stock before adding the lines to a load.

The sales person creates a new Inventory adjustment journal (Reason code 40 - Conversion of items) In which he adds the \"to be built\" Item In the needed quantity on the location REBUILD and with the Inventory status REBUILD. The journal needs to be posted.

     ![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="1.9340277777777777in"}

In the sales order line, the Inventory status for this Item also needs to be changed from Available to REBUILD.

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="4.129855643044619in" height="1.5359995625546807in"}

Only then, the load advice will become OK and It will be possible to add the lines to a load. Then the load lines can be \"Released to warehouse\" and the Outbound picking list can be printed.

![A close-up of a receipt AI-generated content may be incorrect.](media/image11.png){width="4.184000437445319in" height="1.936246719160105in"}

The Inventory status is indicated as a comment on the Outbound picking list. The warehouse employee know by seeing this that he first has to rebuild this item. This is by using the REBUILD menu in the scanner:

- **[Pick the items from stock that you need to do the build:]{.underline}**

<!-- -->

- Click on Rebuilds

- Click on Items OUT

- Scan the location of the item you're picking

- Confirm the item number that you're picking

- Fill in the quantity that you're picking

<!-- -->

- **[Put the items back in stock that are leftover from the build: (not the actual built item)]{.underline}**

<!-- -->

- Click on Rebuilds

- Click on Items IN

- Scan the location of the leftover item you're putting back in stock

- Confirm the item number that you're putting back in stock

- Fill in the quantity that you're putting back in stock

![A screenshot of a phone AI-generated content may be incorrect.](media/image12.png){width="1.3132633420822397in" height="2.155844269466317in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image13.png){width="1.29753937007874in" height="2.15286854768154in"}  ![A screenshot of a phone AI-generated content may be incorrect.](media/image14.png){width="1.3170002187226597in" height="2.1451574803149605in"}  ![A screenshot of a phone AI-generated content may be incorrect.](media/image15.png){width="1.2857141294838146in" height="2.1333759842519684in"}               ![A screenshot of a phone AI-generated content may be incorrect.](media/image16.png){width="1.2792202537182853in" height="2.1188834208223972in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image17.png){width="1.2727274715660541in" height="2.067487970253718in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image18.png){width="1.2545067804024497in" height="2.0593886701662294in"}           

- **[Print the number of labels you need for finished REBUILD item(s):]{.underline}**

![A screenshot of a phone AI-generated content may be incorrect.](media/image12.png){width="1.255634295713036in" height="2.0584416010498687in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image19.png){width="1.2592322834645668in" height="2.0649343832021in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image20.png){width="1.2558125546806649in" height="2.05216426071741in"}   ![A screenshot of a phone AI-generated content may be incorrect.](media/image21.png){width="1.2299682852143483in" height="2.0506824146981626in"}               ![A screenshot of a phone AI-generated content may be incorrect.](media/image22.png){width="1.2555555555555555in" height="2.04576334208224in"}  ![A screenshot of a login screen AI-generated content may be incorrect.](media/image23.png){width="1.2492235345581801in" height="2.041999125109361in"}    ![A screenshot of a phone AI-generated content may be incorrect.](media/image24.png){width="1.2377941819772529in" height="2.0191021434820646in"}

              

After the build, the real picking of the picklist can be done and this built item can also be picked for the order.
