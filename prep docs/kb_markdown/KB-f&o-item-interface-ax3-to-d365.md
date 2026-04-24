# KB — F&O Item Interface AX3 to D365

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Item Interface AX3 to D365.docx`
**Conversiedatum:** 2026-04-24

---

# checks before interface

- Necessary units and unit conversions exist in AX. (PCS+)

- Weight is not 0.

- Brief description for configurations is filled in.

- Vendor Is correct.

# DISTINCT PRODUCT

**[In AXAPTA]{.underline}**

1.  Go to the item table in AX3. Select the item and click on the button: Items to interface with D365.

A new window opens.

2.  As the item does not need to be configurable, leave Product master (D365) on \"No\".

3.  Click CTRL+N.

A new line will appear.

4.  Save by clicking on the disk icon.

The item will now be interfaced to D365.

**[In D365]{.underline}**

1.  Navigate to **Product staging**. The item will be on the list with the Status NEW.

2.  Click on the **AX3 product code** to open the detail page.

3.  Choose the **Product staging template** that fits the item.

4.  Fill in all the missing information.

5.  Click on **Validate** to check if everything has been filled in.

6.  Click on **Create** after validation to create and release the product in D365.

# PRODUCT MASTER with configuration

**[In AXAPTA]{.underline}**

1.  Go to the item table in AX3. Select the item and click on the button: Items to interface with D365.

A new window opens.

2.  As the item needs to be configurable, set Product master (D365) on \"Yes\".

3.  Click CTRL+N.

A new line will appear.

4.  Select the configuration(s) you want to activate. (Make sure the brief description exists in AX)

5.  Save by clicking on the disk icon.

The item and configuration will now be interfaced to D365.

**[In D365]{.underline}**

1.  Navigate to **Product staging**. The item will be on the list with the Status NEW.

2.  If it was the first time you activated this configurable item, you will have a line for the product master and a line for the variant.

3.  Click on the **AX3 product code** to open the detail page of the product master.

4.  Choose the **Product staging template** that fits the item.

5.  Fill in all the missing information.

6.  Click on **Validate** to check if everything has been filled in.

7.  Click on **Create** after validation to create and release the product in D365.

8.  Now go back to the overview of the product staging and select the line of the product variant.

9.  Click on **Product variant staging** in the top menu.

10. Fill in all the missing information.

11. Click on **Validate** to check if everything has been filled in.

12. Click on **Create** after validation to create and release the product variant in D365.

# Configuration for product master

**[In AXAPTA]{.underline}**

1.  Go to the item table in AX3. Select the item and click on the button: Items to interface with D365.

A new window opens.

2.  As the item already exist in D365, the Product master (D365) is already set on \"Yes\".

3.  Click CTRL+N.

A new line will appear.

4.  Select the configuration(s) you want to activate. (Make sure the brief description exists in AX)

5.  Save by clicking on the disk icon.

The configuration will now be interfaced to D365.

**[In D365]{.underline}**

1.  Navigate to **Product staging**. The item will be on the list with the Status NEW.

2.  Select the line of the product variant.

3.  Click on **Product variant staging** in the top menu.

4.  Fill in all the missing information.

5.  Click on **Validate** to check if everything has been filled in.

6.  Click on **Create** after validation to create and release the product variant in D365.

# delete a wrongly created product

**[In D365]{.underline}**

1.  Navigate to **Released products**.

2.  Go to **Manage inventory** and check if there have been **Transactions**.

If there have been transactions, contact D365 support.

If there haven\'t been any transactions, continue with the next steps.

3.  Select the item and click on **Delete.**

4.  Navigate to **All products and product masters**.

5.  Select the item and click on **Delete.**

6.  Navigate to **Product staging** and **delete** the item (status created).

**[In AXAPTA]{.underline}**

1.  Go to the item table in AX3. Select the item and click on the button: Items to interface with D365.

A new window opens.

2.  The line used for the previous creation still exists.

3.  Save by clicking on the disk icon.

The item will now be interfaced again to D365.

# interface the bom from ax to D365

- You need the Item (and configuration) number to exist In AX and D365 before you can send through a bill of materials.

- A BOM Is not an Item! A BOM Is a bill of materials linked to an Item.

## There Is no BOM In D365 yet for the Item or any of the configurations: 

Check If the released product In AX has been set up correctly. If not, change It now!

- Production type = BOM

- Default order type (via \"Default order settings\" via \"Plan\") = Production order

Go to the Item in Axapta for which you want to send the BOM to D365.

After the item is selected and the **\'Item to interface with D365\'** button is pressed, you will see two more buttons on the right side of the new window.

If you need to check if all components already have a D365 number:

- First press the **\'Export BOM with D365FO Codes to file\'** button and export your \'txt-file\'. *(Don\'t forget to mention \'.txt\' as the extension when exporting your file).*

<!-- -->

- Then open the txt-file in Excel and see if there are any warnings in the BOM lines. *(The warnings are indicated by an exclamation mark)*.

If there are warnings that indicate, for example, that a certain item has not yet been sent to D365, it is recommended to do this first. It should be noted that the warnings must relate to the item configuration that you have already provided to D365. You will also see warnings for other item configurations that you have not provided to D365, but these are not relevant.

After you determine that there are no warnings, you can send the BOM to D365 by pressing the **\'Send BOM to D365\'** button.

**Be careful:** The system will only send the BOM for the configurations that are released to D365. If you need other configurations later on, you\'ll no longer be able to send the BOM again. Be sure to release all the configurations you need before Interfacing the BOM.

Now go In D365 to **Released products**.

Go to **Engineer** - **BOM versions.** Check If the BOM Is ok.

Go to the **Header** tab and **Approve**. In the pop-up menu you need mark the checkbox **\"Do you also want to approve the bill of materials\"** on YES. Click **OK**.

Now **Activate** the BOM!

Now go to **Maintain Configurations** and check for each of the configurations If all components are there.

**Important:** If a configuration group only has 1 Item In there, you have to choose this configuration group In every configuration. If you don\'t need that specific Item for the configuration, you\'ll need to add the Item \"No\" In that configuration group. By adding this to the main BOM of the Item, you don\'t have to add the configuration group to the configuration anymore.

## There Is already a BOM In D365 for the product master and some of the configurations

If you\'re creating a new configuration, you need to make sure you first have the Item number both In AX and In D365.

As the product master already has a BOM In D365, you can\'t send It from AX to D365 anymore. There Is no point In working In AX on the BOM.

Just go In D365 to **Released products**.

Now go to **Maintain Configurations** and add everything manually.

**Important:** If a configuration group only has 1 Item In there, you have to choose this configuration group In every configuration. If you don\'t need that specific Item for the configuration, you\'ll need to add the Item \"No\" In that configuration group. By adding this to the main BOM of the Item, you don\'t have to add the configuration group to the configuration anymore.

# General remarks:

- In D365 we only choose for a configurable item (product master with variants) if the item is produced by a company in the group. So, it is possible that an item has configurations in AX but doesn't have them in D365. Every configuration is released as a distinct product.

- Product group 1 & 2 determine the product number in D365. They can\'t be changed anymore. If the groups you need don't exist, contact D365 support. All 4 groups need to be filled in, even if the choice is \"blank\".

- Product staging templates explained:

  - **Item grabstock**: item that will have a fixed location in the blue bins in production. This setting can also be changed later. You will have to add the fixed location after creation of the product and in the warehouse, the label must be put on the location.

  - *([only for Portugal]{.underline}: In PWP the **Item** **grabstock** template was split up into **Item** **grabstock** **no SerialNum** and **Item grabstock SerialNum sales**. Depending if you want to record the serial number of the item during sales picking with the scanner or not)*

  - *[(only for Aquadeck:]{.underline} the template item grabstock is replaced with Item Bufferstock. Use the template **\'Item bufferstock\'** for all backflushed items)*

  - **Item neg stock**: item that is theoretically stocked to be used in the warehouse management flow, but the stock can go under 0. Ex. Transport used in sales orders.

  - **Item replenishment stock**: item that is used in production and has a unit in decimals. Special settings needed after creation. Fixed location needed after creation. Ex. Resin.

  - **Item stock**: standard stock item.

  - *([only for Portugal]{.underline}: In PWP the **Item** **stock** template was split up **Item stock SerialNum prod.**, **Item stock SerialNum sales** and **Item** **stock** **no SerialNum.** Depending if you want to record the serial number of the item after production (in case it\'s a production item) or if you want to record the serial number of the item during sales picking or if you don\'t want to record a serial number at all.*

  - *[(only for Aquadeck:]{.underline} In AQD the **Item** **stock** template was split up **Item stock batch, Item stock SerialNum and Item** **stock** **no batch/serial.** Depending if you want to record the serial number or batch of the item. Use Item stock batch for the raw slats.*

  - **Service no stock**: service item that is not used in BOMs.

  - **Service stock:** service item that is used in BOMs.

  - **Consumable Item**: Item that is received In a PO, but not sold In SO or used In BOM, so the stock needs to be consumed automatically (ex. wrapping foil, tape, glue, etc)

- The configuration name is not mandatory in AX3, but it is in D365. So it is possible that it is blank in AX3 and you have to fill something in for use in D365 during the product staging.

- The search name for a configuration does not exist in AX3, but it does in D365. The current interface fills in the Brief description (from the configuration) from AX3 as the Search name in D365. The search name is mandatory, so if it is blank in the product staging, you will have to fill it in.

- When an item needs to have a BOM, the **production type** is BOM and the **planned order type** is Production order.

- The unit sequence group is the same as the inventory unit.

- You can only select units for which there is an existing unit conversion in AX3.

- **Multipallet** items need the unit PCS+. (This unit first needs to be added to the item in AX3 before interfacing the item!)

- If you choose a coverage group RTS (replenish to stock), you will have to add the settings for the minimum stock after creation of the product.

- Item groups explained:

  - G-TRANS: Transport item for sales orders, is stocked so it can be added in the load.

  - G-TRD: All standard stock items.

  - S-BOM: Service items in BOMs.

  - S-CN: Credit note related service items.

  - S-CUS-PUR: Service items for customs cost related to purchasing.

  - S-CUS-SLS: Service items for customs cost related to sales.

  - S-DISC: Service items for discounts.

  - S-DISCYE: Service items for yearend bonus discounts.

  - S-TRA-PUR: Service items for transport costs related to purchasing.

  - S-TRA-SLS: Service items for transport costs related to sales.

  - S-WORK: Service items for work hours (not in BOM).

- For costing purposes, following must be configured (currently done manually by IT department)

  - Transportcharge group to be filled on released product (tab purchase) based on the transport matrix to include the right transport charge into the cost price of the item.

  - For items which are purchased externally (vendor = third party), an indirect cost of 5% (cfr pwg fee) must be added to the margin cost price. This is done by adding the concerned item in the indirect cost table linked to the costing version CP_MA.

- If you interfaced your item correctly in AX3 but it doesn\'t appear in the Product Staging in D365, there is probably an issue with one of the AX3-fields. A frequent issue is the vendor being a PWGVendor in AX3. This is a problem, as that PWGVendor does not exist in D365.
