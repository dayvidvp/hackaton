# KB — F&O Item is missing during sales picking

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Item is missing during sales picking.docx`
**Conversiedatum:** 2026-04-24

---

We distinguish between 3 different scenarios:

1\) Item is completely missing from the warehouse

2\) Item is only partially found in the warehouse

3\) Item is found but is at least partially on a different location that the one shown on the scanner

# 1) Item is completely missing

[WAREHOUSE OPERATOR]{.mark}:

When you encounter an item on the scanner during picking that is not there, just continue as if it was there.

That means scan the location and type in the item number and then proceed to the next item.

After picking is finished and a LP label is printed, go to menu **Outbound \> Unpick license plate** on the scanner.

Scan the license plate from which you want to unpick or select it on the scanner.

Scan the missing item that you want to unpick or select it on the scanner.

Fill in the quantity that you want to unpick (which is the full quantity of this item on the LP).

Scan the Target location where you want to put it. Choose any warehouse location, it doesn\'t really matter much since we\'re going to book away this stock in the next steps.

Go to the Warehouse Manager and inform him about the missing item and the location you\'ve put it in with the unpick process.

[WAREHOUSE MANAGER]{.mark}:

Go to the **Load details** in D365. Search for the load line that was missing. Copy-paste the SO-number somewhere that you can later inform the sales taker that this item is missing. Delete the load line.

Go to the **On-hand list** and filter on this item. All stock in warehouse locations where **Physical inventory** \> 0 will have to be removed. At least part of this stock if of course reserved by at least 1 sales order line.

So first we will have to remove all reservations on the stock before we can remove the stock.

![](media/image2.png){width="6.268055555555556in" height="0.7381944444444445in"}

On the **On-hand list**, select the line at the top with Warehouse = MAIN, Inventory status = AVAILABLE and Location = blank.

Then click on **Transactions** on top of the screen.

On the next page, click on **Reservation allocation center**.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.033333333333333in" height="2.264671916010499in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.033333333333333in" height="2.1784437882764656in"}

In the **Reservation allocation center** you can see all the SO\'s that are reserving stock on this item. We will have to go in the **Sales order details** page of each of them to take away the reservation.

It\'s important that we take a screenshot of all the SO numbers that reserve stock on this item. We will need it later after we took away the reservations.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.108333333333333in" height="2.713762029746282in"}

Removing sales order line reservations

When taking away the reservations of sales orders, we consider 2 distinct methods, depending on the state of the SO-line:

A\) The SO line is not yet in a load.

B\) The SO line is already in a load but not yet picked

**[A) The SO line is not yet in a load:]{.underline}**

These SO lines are easily recognized in the **Reservation allocation center** because the column \"Physical reserved\" is filled in but the column \"Reservation type\" is blank.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="6.268055555555556in" height="2.515972222222222in"}

To remove the reservation, first enter the **Sales order details** page and select the SO-line contained the item. In the **Line details** at the bottom, choose **Setup** and change the field \"Reservation\" from \"Automatic\" to \"Manual\". Save this change.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="5.025in" height="5.185893482064742in"}

Next, select the SO-line again and click on **Inventory \> Maintain \> Reservation**.

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="6.268055555555556in" height="2.6881944444444446in"}

On the **Reservation** page, we type value \"0\" in the \"Reservation\" column and then just click the Return-arrow. (If you get an error-message at this point, it means that the SO-line is already in a load)

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="2.5625in"}

Continue to return to the **Reservation allocation center** page. Notice that this SO number now has a blank value in the \"Physical reserved\" column.

Repeat these past steps to remove all reservations on the stock of this item.

**[B) The SO line is already in a load but not yet picked]{.underline}**

These SO lines that are already in a Load are easily recognized in the **Reservation allocation center** because the column \"Physical reserved\" is filled in and the column \"Reservation type\" shows a Shield-icon.

However, from this page it is not yet visible if the item is already picked or not.

![A screenshot of a computer screen AI-generated content may be incorrect.](media/image10.png){width="6.268055555555556in" height="3.058333333333333in"}

To remove the reservation, first enter the **Sales order details** page and select the SO-line containing the item. In the **Line details** at the bottom, choose **Load** to find the Load ID that contains the SO line.

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="6.268055555555556in" height="4.093055555555556in"}

Click on the Load ID to go to the **Load details** page.

Here you can select the loadline and see in the line details if the item is already picked or not.

**Work status** \"100,00% of initial pick work completed\" means that picking is done already for this line.

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="2.904861111111111in"}

If It\'s already picked, then there is no need to unpick it and remove the reservation. Just go back to the **Reservation allocation center** and remove the reservation of other SO\'s.

If the **Work status** in the line details says \"0,00% of initial pick work completed\", it means that picking work exists for the item and we have to cancel the picking work

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="5.158333333333333in" height="1.2910115923009624in"}

> *=\> To cancel this picking work, go to **Loads \> Related information \> Work**:*
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="3.3916666666666666in" height="2.3700798337707787in"}
>
> *Then select the correct workID for the missing item with work status \"Open\" and click the \"Cancel\"-button. Go back to the **Load details** afterwards. Now you will be able to delete the loadline.*
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="4.475in" height="3.0144028871391075in"}

If the **Work status** in the line details says \"Work not yet created.\", we can just select the load line and delete it.

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png){width="4.933333333333334in" height="1.7916535433070866in"}

After this, return to the **Sales order details** page and follow the same steps as in ***[A) The SO line is not yet in a load.]{.underline}***

Removing STOCK from the warehouse

After taking away all SO line reservations, it is now possible to remove the missing stock from the system.

There are two ways to remove the stock, which one you choose depends on your company policy.

A\) Clear the stock from the system

B\) Move the stock to BLOCKED location

**[A) Clear the stock from the system:]{.underline}**

Go to **Inventory management \> Journal entries \> Items \> Inventory adjustment**.

Click on **+New** to create a new journal.

Choose an appropriate \"Reason code (PWG)\" and click on OK.

Under **Journal lines**, click on **+New** to create a new journal line. Fill in the missing item number, the location and the Quantity (negative number!) that you want to remove.

Click **Post**.

Check on the **On-hand list** to make sure all stock of the item is deleted properly.

**[B) Move the stock to BLOCKED location:]{.underline}**

On the scanner go to the menu **Stock movement \> Move to blocked**.

Scan the location where to stock is situated and Confirm.

Scan the item that you want to remove.

Confirm the quantity (the full quantity on the location is proposed). Confirm the overview.

Scan the BLOCKED location.

The stock is now moved to the BLOCKED location and its inventory status is automatically changed from AVAILABLE to BLOCKED. This makes sure that sales order lines can no longer reserve the stock.

Keep in mind that the stock is unavailable, but it\'s not gone. So periodically an authorized person will have to book away the stock on BLOCKED through an inventory adjustment journal.

aftermath

2 important tasks remain:

1\) For every SO-line where we\'ve put the Reservation on \"Manual\", we have to put it back to \"Automatic\". This makes sure that as soon as new stock of the missing item arrives, the SO line will automatically reserve that stock.

You can use the screenshot you took earlier of the reservation allocation center to find back all the SO-lines where you took away the reservation.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="4.925622265966754in" height="5.083333333333333in"}

2\) Inform all the sales people involved that they\'ve lost their reservations on this item and that they will have to remove/postpone their SO lines.

# 2) Item is only partially found

[WAREHOUSE OPERATOR]{.mark}:

The warehouse operator can follow the same steps from chapter ***1) Item is completely missing***. The only difference is that he does not need to unpick the full quantity of the item, only the quantity that was missing.

[WAREHOUSE MANAGER]{.mark}:

The warehouse manager needs to contact the sales taker of the incomplete sales order line and inform him about the missing stock.

The sales taker then needs to decide whether to send the picked quantity to the customer (which is only part of the demanded quantity) or to delete the SO line altogether from the load.

**[A) Sales taker decides to remove the SO line from the load entirely]{.underline}:**

The Warehouse manager instructs the Warehouse operator to also unpick the partially picked quantity from the load.

Then, similar steps as in chapter ***1) Item is completely missing*** need to be followed. Just keep the following differences in mind:

\- Don\'t remove the full quantity on stock of the item. Only remove the quantity that is actually missing.

\- It might not be necessary to remove all SO line reservations as we still have some stock left. The warehouse manager can ask the sales people which SO-line(s) can keep the reservations.

**[B) Sales taker decides to ship the partially picked quantity]{.underline}:**

The Warehouse manager asks the sales taker to go to the **Load details** page and reduce the load line to the picked quantity. It\'s also best practice to go into the SO and split up the partially picked SO line into two SO lines (with one fully picked and one not picked at all).

Then, similar steps as in chapter ***1) Item is completely missing*** need to be followed to take away reservations on the remaining stock and book away the remaining stock.

# 3) Item is found on another location

[WAREHOUSE OPERATOR]{.mark}:

The Warehouse operator finishes the picking as requested on the scanner. He does write down the item with the incorrect location and the location on which he did find it.

Then he informs the manager about this.

[WAREHOUSE MANAGER]{.mark}:

The Warehouse manager can do a thorough check/stock count of this item if he wants to but at least he needs to transfer the stock in the system from the incorrect location to the location where the item can actually physically be found.

In order to transfer the stock, it\'s best to first open the **Reservation allocation center** of the wrongly placed item (see an explanation in chapter ***1) Item is completely missing*** to get the this page). Opening the **On-hand list** is also useful.

There are 2 different flows to transfer the stock between locations, depending on the level of reservation of the stock. It might be possible to need a mix of both flows to transfer the stock fully to another location.

**[A) The stock on a location is not reserved for sales orders or it is reserved for sales orders but no picking work has been created yet on the location.]{.underline}**

This type of stock is characterized by a blank value in the \"Physically reserved\" column in the **On-hand list** on the location.

![A screenshot of a computer AI-generated content may be incorrect.](media/image17.png){width="6.268055555555556in" height="1.275in"}

It is possible to move the stock to another location using the menu **Stock movement \> Move items** on the scanner.

**[B) The stock on a location is reserved for sales orders and picking work already exists on the location.]{.underline}**

This type of stock is characterized by a non-blank value in the \"Physically reserved\" column in the **On-hand list** on the location.

![A screenshot of a computer AI-generated content may be incorrect.](media/image18.png){width="6.268055555555556in" height="1.2618055555555556in"}

We first need to cancel the picking work on the location as explained in chapter ***1) Item is completely missing/REMOVE SALES ORDER LINES RESERVATIONS***.

Then we can move the stock between locations using the menu **Stock movement \> Move items** on the scanner.

Then we need to release the loads again to recreate the cancelled picking work, but this time on the right location.
