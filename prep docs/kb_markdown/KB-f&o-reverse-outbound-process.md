# KB — F&O Reverse outbound process

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Reverse outbound process.docx`
**Conversiedatum:** 2026-04-24

---

# How to Cancel TRANSPORT LINE in Load

- **[Load is not yet released]{.underline}**

<!-- -->

- Select load line and click **Delete**.

![A screenshot of a website Description automatically generated](media/image2.jpeg){width="6.268055555555556in" height="2.395138888888889in"}

- **[Load is released]{.underline}**

<!-- -->

- Select load line and click **Reduce picked quantity**.

![A screenshot of a computer Description automatically generated](media/image3.jpeg){width="6.268055555555556in" height="2.423611111111111in"}

- Set **Move to location** to \'NEG\' and **Inventory quantity to unpick** to \'1\'. Click **OK.**

![A screenshot of a computer Description automatically generated](media/image4.jpeg){width="6.268055555555556in" height="1.6583333333333334in"}

- Refresh the load details screen to see the transport item disappear.

# How to Cancel stocked item LINE in load

- **[Load is not yet released]{.underline}**

<!-- -->

- Select load line and click **Delete**.

![A screenshot of a computer Description automatically generated](media/image5.jpeg){width="6.268055555555556in" height="2.4145833333333333in"}

- **[Load is released but not yet picked]{.underline}**

<!-- -->

- Go in the Work details of the load.![A screenshot of a computer Description automatically generated](media/image6.jpeg){width="4.694444444444445in" height="2.629861111111111in"}

- Select all work lines that you want to cancel (the work status has to be \'Open\'). Then click on **Cancel work.** Go back to the load details.

![A screenshot of a computer Description automatically generated](media/image7.jpeg){width="6.268055555555556in" height="4.309722222222222in"}

- Select load line and click **Delete**.

<!-- -->

- **[Load is released and picked but not loaded]{.underline}**

<!-- -->

- Unpick the picked goods with the scanner via **Outbound \> Unpick license plate.**

> Scan the OUTB license plate label with the picked goods on and put one or more goods back in a warehouse location.

![A screenshot of a computer Description automatically generated](media/image8.jpeg){width="4.462962598425197in" height="2.8060389326334207in"}

- In the load details in D365, select the load lines that were unpicked and click **Delete**.

<!-- -->

- **[Load is released, picked and loaded]{.underline}**

<!-- -->

- If the packing slip is already booked, it\'s too late, you cannot reverse the process. You need to follow the Return-flow ([F&O Returns.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Returns.docx?d=wad343899f5fc41fca0813b13a552cf3b&csf=1&web=1&e=CpP1QI)).

- If the outbound shipment is already confirmed, you need to click the **Reverse shipment confirmation** button first.

![A screenshot of a computer Description automatically generated](media/image9.jpeg){width="5.083333333333333in" height="1.4909722222222221in"}

- Unload the loaded license plates with the scanner via **Outbound \> Unload truck**

![A screenshot of a computer Description automatically generated](media/image10.jpeg){width="4.370370734908136in" height="3.0499628171478563in"}

- Unpick the picked goods with the scanner via **Outbound \> Unpick license plate**.

- In the load details in D365, select the load lines that were unpicked and click **Delete**.

# How to Cancel item with production in load

- **[Load is not yet released]{.underline}**

<!-- -->

- Select load line and click **Delete**.

- (If you want to remove the SO-line: go to the production order and reset the status to Created and then delete it. Now you can delete the SO-line as well.)

<!-- -->

- **[Load is released, picking of BOM-components not yet started]{.underline}**

<!-- -->

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled. The open work will be cancelled.

- Select load line and click **Delete**.

- (If you want to remove the SO-line: go to the production order and reset the status to Created and then delete it. Now you can delete the SO-line as well.)

<!-- -->

- **[Load is released, picking of BOM-components is ongoing]{.underline}**

<!-- -->

- With the scanner, stop the picking process by clicking the \'Done\' button. The scanner will ask you to put all picked goods on the PSTAGE location.

> ![A screenshot of a computer Description automatically generated](media/image11.png){width="3.723663604549431in" height="3.8170286526684163in"}

- Go in the Work details of the production order.

> ![A screenshot of a computer Description automatically generated](media/image12.png){width="4.907487970253718in" height="2.186046587926509in"}

- Select all work lines that still have work status \'Open\'. Then click on **Cancel work.** Go back to the production order.

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled.

- Via **Production order (details) \> Warehouse \> Stop and Unpick**.

- Via **Production order (details) \> Warehouse \> Remove Stop**.

- Return the raw materials on Prodin to the stock locations with the scanner via **Production \> Return components to stock**.

- Go back to the load. Select load line and click **Delete**.

- (If you want to remove the SO-line: go to the production order and reset the status to Created and then delete it. Now you can delete the SO-line as well.)

<!-- -->

- **[Load is released, picking of BOM-components is finished, no produced goods are registered yet in Tulip]{.underline}**

<!-- -->

- In Tulip, click the \'Undo Start\' button (only if the production order was already started).

- Via **All production orders**/**Production order (details) \> Production order \> Reset status**. Reset the status to Scheduled.

- Via **Production order (details) \> Warehouse \> Stop and Unpick**.

- Via **Production order (details) \> Warehouse \> Remove Stop**.

- Return the raw materials on Prodin to the stock locations with the scanner via **Production \> Return components to stock**.

- Go back to the load. Select load line and click **Delete**.

- (If you want to remove the SO-line: go to the production order and reset the status to Created and then delete it. Now you can delete the SO-line as well.)

<!-- -->

- **[Load is released, production is finished, goods are not yet loaded]{.underline}**

<!-- -->

- Unpick the produced goods with the scanner via **Outbound \> Unpick license plate.**

> Scan the OUTB license plate label with the produced goods on and put them back in a warehouse location.

![A screenshot of a computer Description automatically generated](media/image8.jpeg){width="4.462962598425197in" height="2.8060389326334207in"}

- Go to the sales order. Select the sales order line and click **Inventory \> Maintain \> Marking**.

- Break the mark between SO line and production order by entering the negative quantity of the produced goods in the \'Mark now\' column. Check the box in the \'Set mark now\' column. Now click \'OK\'.

> ![A screenshot of a computer Description automatically generated](media/image13.png){width="6.268055555555556in" height="4.529861111111111in"}

- Go back to the load. Select load line and click **Delete**.

<!-- -->

- **[Load is released, production is finished, goods loaded]{.underline}**

<!-- -->

- If the packing slip is already booked, it\'s too late, you cannot reverse the process. You need to follow the Return-flow ([F&O Returns.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Returns.docx?d=wad343899f5fc41fca0813b13a552cf3b&csf=1&web=1&e=CpP1QI)).

- If the outbound shipment is already confirmed, you need to click the **Reverse shipment confirmation** button first.

![A screenshot of a computer Description automatically generated](media/image9.jpeg){width="5.083333333333333in" height="1.4909722222222221in"}

- Unload the loaded license plates with the scanner via **Outbound \> Unload truck**

![A screenshot of a computer Description automatically generated](media/image10.jpeg){width="4.370370734908136in" height="3.0499628171478563in"}

- To proceed, see chapter \"HOW TO CANCEL ITEM WITH PRODUCTION IN LOAD\", \"Load is released, production is finished, goods are not yet loaded\".
