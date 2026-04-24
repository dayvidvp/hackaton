# KB — F&O Rebuilds (NEW FLOW)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Rebuilds (NEW FLOW).docx`
**Conversiedatum:** 2026-04-24

---

# Settings necessary for the flow

1\) [Production type]{.underline}:

In **Released product details** tab \'Engineer\', the **Production type** for a rebuild item has to be put on \'BOM\'.

![](media/image1.png){width="6.268055555555556in" height="3.2020833333333334in"}

2\) [Item coverage]{.underline}:

In **Released product details** go to Plan\>**Item coverage**:

![](media/image2.png){width="6.268055555555556in" height="2.7194444444444446in"}

Click on 'New to add a new line.

In the new line, add a configuration if applicable.

Put the Inventory status on REBUILD. Choose an MTO Coverage group.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="1.6791666666666667in"}

In the \'General\' tab, put the Planned order type on \'Production\'. Click Save.

You\'ll see in the \'Overview\' tab that the Planned order type is now changed to \'Production\'

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="4.908333333333333in" height="2.520510717410324in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="1.7055555555555555in"}

Mind you, adding an Item coverage with Planned order type = Production for the Inventory status REBUILD does not mean that item becomes a "real" production item. The default order setting for this item is still "Purchase" and Masterplanning will still propose to purchase this item for sales order lines with status AVAILABLE.

3\) [Accelerated production]{.underline}:

Two parameters regarding 'Accelerated production' need to be switched on:

- On the **Mobile device menu item** that you use to pick your rebuild components a parameter needs to be switched on:

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="6.268055555555556in" height="1.8590277777777777in"}

- In the **Released product details** tab \'Engineer\' a parameter needs to be switched on:

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="2.4090277777777778in"}

4\) [Release to warehouse]{.underline}:

In the **Released product details** tab \'Engineer\', the **Release to warehouse** parameter needs to be set to \'Require full reservation\':

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="6.268055555555556in" height="1.7715277777777778in"}

5\) [Flushing principle]{.underline}:

In the **Released product details** tab \'Engineer\', the **Flushing principle** parameter needs to be set to \'Finish\':

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="3.3805555555555555in"}

6\) [Inventory status:]{.underline}

On the page **Inventory statuses**, check the box in the column **Update fixed product information** for the status REBUILD:

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="6.268055555555556in" height="2.9430555555555555in"}

7\) [BOM]{.underline}:

Through the **Release product details** page of the rebuild item, go to the **BOM versions** in the Engineer Action pane. Then create a BOM version and approve & activate it. You don\'t necessarily need to create a new BOM, you can choose the existing BOM with BOM ID = \'Empty\'. That is a BOM with no BOM-lines in it.

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="4.508333333333334in" height="2.0129166666666665in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="3.691666666666667in" height="1.8785531496062993in"}

![](media/image13.png){width="6.268055555555556in" height="3.2916666666666665in"}

8\) [Worker]{.underline}:

When the automatic "report as finished" of the production order happens during picking, the system will report as finished following the settings of the User to which the Worker (the one logged in on the scanner) is linked.

This can be tricky, as not all Users may have the correct default values in their "Report as finished" settings. Especially the BOM consumption can have the wrong default value.

Therefore we advise to link all the Workers to the User that usually finishes production orders in the system. So normally the Production Manager. This User should for sure have the correct default values in his/her "Report as finished" settings.

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="6.268055555555556in" height="3.6256944444444446in"}

# Execute the rebuilds flow

Create a sales order line and enter the Rebuild item.

> *Fyi: It might be possible that you run into this error when choosing a configuration of an item:*

![](media/image15.png){width="3.591666666666667in" height="0.48333333333333334in"}

> *This error might happen when entering a SO-line or later in the flow when entering BOM-components. When seeing this error, it's not possible to choose a configuration from the dropdown in the Configuration-field. But you still can manually type in the configuration in the field directly, so you should do this.*

Set the quantity to rebuild on your sales order line.

Change the Inventory status of the line to Rebuild and click Save.

The Line advice will now change to 'MTO Production'.

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png){width="6.268055555555556in" height="2.4305555555555554in"}

Select the SO line and click on **Product and supply \> New \> Production order**.

Then click on 'Create' in the 'Create production order' screen that pops up on the right side.

![A screenshot of a computer AI-generated content may be incorrect.](media/image17.png){width="6.268055555555556in" height="2.71875in"}

In the **Production order (details)** page, go to the BOM of the production order:

![A screenshot of a computer screen AI-generated content may be incorrect.](media/image18.png){width="4.15in" height="1.9444214785651794in"}

In the BOM, click +New to add BOM lines.

If you add a new BOM line, enter an item number and adjust the quantity if needed

![A screenshot of a computer AI-generated content may be incorrect.](media/image19.png){width="3.283333333333333in" height="1.925080927384077in"}

**[IMPORTANT]{.mark}**: When you add a BOM-line with a negative quantity, you will need to enter a **Location** in the BOM-line. This is the location where you want the operators to put the item on stock. If you don't enter a location, you will get stuck later in the flow.

![A screenshot of a computer AI-generated content may be incorrect.](media/image20.png){width="4.123327865266842in" height="4.791666666666667in"}

When your BOM is ready, go back to the **Production order (details)**.

**Estimate** the production order and then go back to the sales order details.

![A screenshot of a computer AI-generated content may be incorrect.](media/image21.png){width="4.091666666666667in" height="2.7380533683289587in"}

In the **Sales order details** page, click on Save or refresh the page to recalculate the Load advice. If all the positive BOM-lines of your production order are on stock, you will get a positive load advice. Now you can go to the **Outbound load planning workbench** and add your sales order line to a load.

![A screenshot of a computer AI-generated content may be incorrect.](media/image22.png){width="6.268055555555556in" height="3.217361111111111in"}

In your load, click the 'Release to warehouse button' to create picking work.

Print the production picking list. On the list, there is a 'REBUILD' indication in the header.

The negative BOM lines can be found at the bottom of the picking list. The location is visible where we need to put the items back on stock.

![A close-up of a product list AI-generated content may be incorrect.](media/image23.png){width="6.268055555555556in" height="3.848611111111111in"}

Now you pick the goods with the scanner as you would do for a regular MTO production order. After you have picked everything and put it on PSTAGE, an outbound license plate label is printed automatically.

If you go to the production order details, you will see that the production order already has status 'Reported as finished'. So by just picking the components for the rebuild, we have also automatically Started & Reported as finished the production order.

![A screenshot of a computer AI-generated content may be incorrect.](media/image24.png){width="6.268055555555556in" height="1.7944444444444445in"}

You can now just continue finishing your load.
