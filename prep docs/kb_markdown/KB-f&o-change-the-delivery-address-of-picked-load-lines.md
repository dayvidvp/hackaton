# KB — F&O Change the delivery address of picked load lines

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Change the delivery address of picked load lines.docx`
**Conversiedatum:** 2026-04-24

---

In order to change the delivery address of picked load lines, we will need to unpick the load lines, delete them from the load, change the delivery address on the sales order lines and then put them back in a load and pick them.

Follow the steps below in order to do this.

1.  Create a temporary location to store the unpicked goods briefly before you pick them again from this location :

> Go to **Warehouse management \> Setup \> Warehouse \> Locations**. Create a new location that will come first if you put all locations in alphabetical order, for example location \'AAA\'. Make sure this location is in the MAIN warehouse and has location profile ID = STOCK. Don\'t fill in check digits for this location. The sort code is irrelevant and can be anything.

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.268055555555556in" height="1.8465277777777778in"}

2.  Unpick the selected load lines with the Warehouse App :

    - Go to the **Load details** of the load holding the load lines with the wrong delivery address.

    - On the Action Pane in **Load details**, you can click on **Transportation \> Related information \> Licenseplate summary**. This page helps to find the correct license plate number that you want to unpick in case there are multiple license plates on the load.

> If it\'s still unclear, you can click on the license plate number and then you\'ll be able to click on a \'On-hand list\' button to see exactly what is on this license plate.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="4.65in" height="2.2555030621172354in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.0645833333333334in"}

- Log in to the Warehouse App. It\'s important that you log in with a user that is connected to a mobile labelprinter, as we\'ll need to have a label printed at the end.

- In the Warehouse App, go to **Outbound \> Unpick license plate**. Enter the license plate number that you want to unpick or choose the load from the list and then choose the license plate from the list.

- Choose the item from the list that you want to unpick. Confirm the item. Enter the quantity that you want to unpick. Enter the location that you made in the first step of this manual (\'AAA\'). Then choose one of the options to unpick other items or to finish the unpicking.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="2.691666666666667in" height="2.779773622047244in"} ![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="2.675in" height="2.7800732720909886in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="2.691666666666667in" height="2.792988845144357in"} ![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="2.625553368328959in" height="2.7333333333333334in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="2.9198654855643045in" height="3.025in"} ![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="2.941666666666667in" height="3.047413604549431in"}

> You have to repeat this process for all items that you wish to change the delivery address for. There is no way to unpick an entire license plate at once.
>
> (It is possible that STOCK labels are printed when you unpick goods, I\'m unsure of that.)

3.  Delete lines from load:

    - Via **Load details**. Select all lines that you want to delete and click on the \'Delete\' button.

> (if you get an error, just refresh the page and try again).
>
> Click \'Delete\' again in the pop-up screen on the right-hand side.

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="3.275in" height="2.7981135170603673in"}

4.  Change the delivery address of the sales order lines:

    - Go to the **Sales order details**. Change the delivery address in the sales order header, click Save and then in the pop-up screen confirm that you want to push the change to all lines of the sales order.

> If you only want to change the delivery address of specific lines, you can do this in the line details.

5.  Put the sales order lines back in a load:

    - Via **Outbound load planning workbench**. Select the sales order lines and either add them to an existing load or add them to a new load.

6.  Pick the items.

    - Go to the **Load details** and click the \'Release to warehouse\' button in the Action pane. Confirm. Picking work is now created for all the sales order lines in the \'AAA\' location. You can see this in the Work details of the load.

> Open the **Outbound picking list**.

- In the Warehouse app, go to **Outbound \> Picking sales & production**. Scan or copypaste the pick key from the picking list in the Warehouse app to start the picking.

- Follow the steps on the Warehouse app to pick all the goods from location \'AAA\'.

- After you\'ve put everything on location \'STAGE\' and thus finished the picking, an OUTB label will be printed. Put this license plate label on the picked goods and remove the old label.

7.  Delete the temporary location:

    - Go to **Warehouse management \> Setup \> Warehouse \> Locations**. Select the location that you\'ve created in the first step of this manual and click to \'Delete\' button. Confirm the deletion of this location.

**[Remarks:]{.underline}**

- If the license plate is already loaded onto the truck, then you\'ll have to go through the **Outbound \> Unload truck** menu in the Warehouse app first before you\'ll be able to unpick.

In **Load details** \> **Transportation \> Related information \> Licenseplate summary** you can see if a license plate is already \'Loaded\' or not.

- Creating and deleting the location is not a necessary step in itself. But it ensures that the picking work that you create will be on the same location where you\'ve unpicked the goods. It is in my experience the easiest way to keep the stock situation clean and correct during this process.
