# KB — F&O Sales Process Kennet

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales Process Kennet.docx`
**Conversiedatum:** 2026-04-24

---

![**Sales Process KENNET**](media/image2.png){alt="Personalized Content Solution | Content Personalization | PathFactory ..." width="0.84375in" height="0.84375in"}

p

**[Create SO manually or confirm a quotation and process the SO]{.underline}**

- Navigate to **All sales orders** and click on **+New.**

- Select the correct **customer account.**

- Select or create the correct **delivery address.**

- Click **OK.**

- Add Items in correct quantities. Choose configuration If needed.

- Explode any bundles.

![A close up of text Description automatically generated](media/image3.png){width="0.27155074365704285in" height="0.2139271653543307in"}= Bundle parent (will be cancelled after explosion, will be on external docs)

![A close up of text Description automatically generated](media/image3.png){width="0.2261253280839895in" height="0.1971347331583552in"}= Bundle component (will be on Internal docs like picking list)

- Check via Max. Report as finished If all components for production Items are In stock.

> ![](media/image4.png){width="0.20836286089238845in" height="0.27087160979877517in"}= MTS (Make To Stock, should be In stock, If not, production needed)
>
> ![](media/image1.png) = MTO (Make To Order, only produced when there is an SO)

- Add a **transport line 99101000001** if there is delivery.

- Change **Mode of Delivery** according to next steps:

  - Pick a specific carrier If you know with whom It will leave (DPD, PAL, TNT, etc).

  - Pick PREP-STD If production needs to be scheduled.

+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+
| **Situation**                              | > **Fill in confirmed ship date** | > **Confirm now** | > **Print confirmation** | > **Put in bin Mark** | > **Add to load** | > **Print outbound picking list** | > **Put in bin warehouse** |
+:===========================================+:=================================:+:=================:+:========================:+:=====================:+:=================:+:=================================:+:==========================:+
| All Items In stock                         | Y                                 | Y                 |                          |                       | Y                 | Y                                 | Y                          |
+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+
| Not all Items In stock - Partial shipment  | Y                                 | Y                 | Yx2                      | Y                     | Y                 | Y                                 | Y                          |
+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+
| Not all Items In stock - Complete order    |                                   | Y                 | Y                        | Y                     |                   |                                   |                            |
+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+
| Production Items - all components In stock |                                   | Y                 | Y                        | Y                     |                   |                                   |                            |
+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+
| Production Items - missing components      |                                   | Y                 | Y                        | Y                     |                   |                                   |                            |
+--------------------------------------------+-----------------------------------+-------------------+--------------------------+-----------------------+-------------------+-----------------------------------+----------------------------+

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+------------------------------------+------------------------------------+-----------------------+---------------------------+
| **In case the SO goes In credit management after trying to confirm the order.**                                                                                                    | > **Send Pro forma invoice** | > **Print pro forma confirmation** | > **Hand over papers to accounts** | > **Check with Neil** | > **Release by accounts** |
|                                                                                                                                                                                    |                              |                                    |                                    |                       |                           |
| *You can check the reason If you go to \"Credit management\", click on \"Credit management hold list\", select the line and go to the right to the column \"credit hold reason\".* |                              |                                    |                                    |                       |                           |
+:===================================================================================================================================================================================+:============================:+:==================================:+:==================================:+:=====================:+:=========================:+
| In credit management - Payment terms                                                                                                                                               | Y                            |                                    | Y                                  |                       | Y                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+------------------------------------+------------------------------------+-----------------------+---------------------------+
| In credit management - Overdue                                                                                                                                                     |                              | Y                                  | y                                  |                       | Y                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+------------------------------------+------------------------------------+-----------------------+---------------------------+
| In credit management - Sales order                                                                                                                                                 |                              |                                    |                                    | Y                     | Y                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------+------------------------------------+------------------------------------+-----------------------+---------------------------+

**[Add sales lines to an outbound load:]{.underline}**

- Via **Warehouse \> Outbound load planning workbench**

- NEW: Select the lines and click on **Supply and demand \> To new load**

> Go In the load and add the cut-off date.

- EXISTING: Select the lines and the load and click on **Supply and demand \> To existing load**

In the top screen you see all the lines from the SO that can be added Into a load.

You will not see any lines If the order Is In credit management.

You will not see lines of Items that are not In stock.

You will not see any lines If the parameter \"Complete order\" Is on Yes (In the sales order) and not everything Is In stock.

If an Item Is only partially In stock, you\'ll see the complete quantity, you\'ll need to change It to the correct available quantity In the load.

In the bottom screen you see all loads that are In progress somehow. Decide If you can add It to an existing load or If you need to make a new load. Check the carrier and the cut-off date to make a decision.

A load = All shipments that leave at the same moment In time with the same person. (A collection by a customer Is 1 load. All the parcels for different customers leaving with DPD on a specific day are In 1 load)

**[Print Outbound picking list]{.underline}**

- Go to **Active outbound loads (warehouse).**

- Select your shipment.

- Via **Loads - Release - Release to warehouse** to create work.

- Via **Loads - Documents** - Print the **Outbound picking list.**

**[Rest of the sales flow]{.underline}**

**Creation & scheduling of production orders** Is done by Mark.

**Picking, packing and production** Is done In the warehouse.

When goods have left all shipments appear as loaded In the active outbound loads screen. The shipments are then confirmed and **the packing slips are posted and emailed** by Ed.

Ed brings up all the paperwork of all the shipments that have left and puts them In the office for Invoicing.

**Invoicing** Is done the next day by accounts.

**[Status changes:]{.underline}**

- **Sales order status**

![](media/image5.emf)

- **Sales order release status**

![](media/image6.emf)

- **Outbound load status**

![](media/image7.emf)

![A close up of a text Description automatically generated](media/image8.jpeg){width="2.4833333333333334in" height="0.3864107611548556in"}

![A white box with black text Description automatically generated](media/image9.jpeg){width="3.6041666666666665in" height="0.5687182852143482in"}
