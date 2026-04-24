# KB — Interface trade agreements

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `Interface trade agreements.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[1. Interface trade agreements from external vendors [1](#_Toc168644216)](#_Toc168644216)

[1.1 Create a new or update an existing trade agreement in AX3 [1](#create-a-new-or-update-an-existing-trade-agreement-in-ax3)](#create-a-new-or-update-an-existing-trade-agreement-in-ax3)

[1.2 Manually send trade agreements from AX3 [4](#manually-send-trade-agreements-from-ax3)](#manually-send-trade-agreements-from-ax3)

[1.3 Create a new item (or release to D365) [4](#create-a-new-item-or-release-to-d365)](#create-a-new-item-or-release-to-d365)

[1.4 Create a new vendor [6](#create-a-new-vendor)](#create-a-new-vendor)

[2. Interface cost prices from Axapta sister companies [9](#interface-cost-prices-from-axapta-sister-companies)](#interface-cost-prices-from-axapta-sister-companies)

[2.1 Axapta sister company as default vendor on released product [10](#axapta-sister-company-as-default-vendor-on-released-product)](#axapta-sister-company-as-default-vendor-on-released-product)

[2.2 Purchase order towards an Axapta sister company [12](#purchase-order-towards-an-axapta-sister-company)](#purchase-order-towards-an-axapta-sister-company)

[]{#_Toc168644216 .anchor}

# Interface trade agreements from external vendors

## 1.1 Create a new or update an existing trade agreement in AX3

An item does exist in 2 D365FO legal entities

![A computer screen with a white background Description automatically generated with medium confidence](media/image1.png){width="6.268055555555556in" height="1.225in"}

New TA is added in AX3-MDC

![](media/image2.png){width="6.268055555555556in" height="0.5902777777777778in"}

Based on BusinessProcess "TradeAgreement" which should be active by legal entity

![A screenshot of a computer Description automatically generated](media/image3.png){width="5.008767497812773in" height="1.5251323272090989in"}

2 messages -- one for each legal entity in which the item is released will be processed in D365FO. The message will contain all active trade agreements for the item.

![](media/image4.png){width="6.268055555555556in" height="0.3277777777777778in"}

Message contains all active lines (also line discounts which are \<\> 0):

![A close-up of a computer screen Description automatically generated](media/image5.png){width="6.268055555555556in" height="1.070138888888889in"}

In both 1602 and 2000 the TA's are added:

![A screenshot of a computer Description automatically generated](media/image6.png){width="6.268055555555556in" height="0.9361111111111111in"}

![A screenshot of a computer Description automatically generated](media/image7.png){width="6.268055555555556in" height="1.0020833333333334in"}

Some remarks:

- Interfaced lines are indicated with an icon:

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.268055555555556in" height="2.127083333333333in"}

- Staffels in AX3 don't have a "To quantity" but find next is used. No logic is foreseen in D365FO to fill "To quantity" but all AX3 fields are copied. Find next functionality will set correct price when creating a purchase order.

![](media/image9.png){width="6.268055555555556in" height="0.5902777777777778in"}

![A screenshot of a computer Description automatically generated](media/image10.png){width="6.268055555555556in" height="1.0020833333333334in"}

See for more detailed scenario testing: [[Purchase trade agreements staffel scenario testing axapta vs d365.docx]{.underline}](https://polletgroupintranet.sharepoint.com/:w:/r/sites/MicronD365FOProject/Shared%20Documents/Processen/Aankoop/Onderzoek/Purchase%20trade%20agreements%20staffel%20scenario%20testing%20axapta%20vs%20d365.docx?d=w5a644afa485b4f56b2417b0fafa4889e&csf=1&web=1&e=q3rG3j)

- If a trade agreement in MDC exists for a vendor which is not active in a specific legal entity, this will be added as a remark in the message towards this entity, f.e.:

![A screen shot of a computer Description automatically generated](media/image11.png){width="5.692159886264217in" height="2.066846019247594in"}

- If a new TA is created in AX3, but the old line with same characteristics (vendor, item) did not get a "to date", at import in D365FO the old line will get a "to date".

Although it's better always to fill a "to date" in AX3 which is done via:

- Old line is automatically closed when uploading a new line

- Old line should be closed manually if new line is added manually

![A screenshot of a computer Description automatically generated](media/image12.png){width="6.268055555555556in" height="2.467361111111111in"}

![](media/image13.png){width="6.268055555555556in" height="0.35in"}

![A screenshot of a computer Description automatically generated](media/image14.png){width="6.268055555555556in" height="0.7965277777777777in"}

Potential sync issues:

- Deleted lines in AX3 will not be interfaced

- An existing TA in AX3 is updated with a "to date" in the past. This update won't be interfaced as line is not active any more. In D365FO the TA will still be active.

  - Line will be disactivated in D365FO if a new TA is added in AX3 🡺 New line will be interfaced and will set an end date to old line.

## 1.2 Manually send trade agreements from AX3

A button is foreseen in AX3 which will send the TA's from MDC towards **all** D365FO legal entities for which business process "TradeAgreement" is active.

![A screenshot of a computer Description automatically generated](media/image15.png){width="6.268055555555556in" height="2.186111111111111in"}

![](media/image16.png){width="6.268055555555556in" height="0.3909722222222222in"}

## 1.3 Create a new item (or release to D365)

In AX3 the item is sent towards a D365FO legal entity. Item is set to "Active"

![A screenshot of a computer Description automatically generated](media/image17.png){width="6.268055555555556in" height="2.317361111111111in"}

Item is sent to D365FO via business process "ProductStaging"

![](media/image18.png){width="6.268055555555556in" height="0.6131944444444445in"}

Now the product will be created in D365FO via the product staging form:

![](media/image19.png){width="2.975258092738408in" height="0.3416961942257218in"}

This will trigger a new "Command" from D365FO

![](media/image20.png){width="6.268055555555556in" height="0.7597222222222222in"}

This command will trigger following business processes (only if these are "active"):

![](media/image21.png){width="6.268055555555556in" height="0.6451388888888889in"}

- ProductExternalItemDescriptions: From AX3 MDC to D365FO (Shared for all entities)

- TradeAgreement: From AX3 MDC to D365FO legal entity where item is released: one message with all TA records for the concerned item

Vendors which are not active in the D365FO legal entity will be indicated with a message "Vendor x is set to passive"

![A screenshot of a computer program Description automatically generated](media/image22.png){width="4.409359142607174in" height="5.500200131233596in"}

## 1.4 Create a new vendor

In AX3 the vendor is sent towards a D365FO legal entity. Vendor is set to "Active"

![A screenshot of a computer Description automatically generated](media/image23.png){width="6.268055555555556in" height="2.8in"}

Vendor is sent to D365FO via business process "Suppliers"

![A screenshot of a computer Description automatically generated](media/image24.png){width="6.268055555555556in" height="0.9125in"}

![](media/image25.png){width="6.268055555555556in" height="0.3375in"}

This will trigger a new "Command" from D365FO

![](media/image26.png){width="6.268055555555556in" height="0.7631944444444444in"}

This command will trigger following business processes (only if these are "active"):

- ProductExternalItemDescriptions**Vend**: From AX3 MDC to D365FO (Shared for all entities)

![A screenshot of a computer Description automatically generated](media/image27.png){width="6.268055555555556in" height="0.9076388888888889in"}

Items which are not active in the D365FO legal entity will be indicated with a message "No item mapping found"

![A screen shot of a computer Description automatically generated](media/image28.png){width="6.268055555555556in" height="3.0527777777777776in"}

- TradeAgreement: From AX3 MDC to D365FO legal entity where vendor is created: one message with all TA records for the concerned vendor

![](media/image29.png){width="6.268055555555556in" height="0.6840277777777778in"}

Items which are not active in the D365FO legal entity will be indicated with a message "No item mapping found"

> ![A screenshot of a computer program Description automatically generated](media/image30.png){width="4.194444444444445in" height="4.713521434820647in"}

Class to request all TA's from Axapta for active D365FO items:

<https://pwg-xxxx.xxxxxxx.operations.dynamics.com/?cmp=1011&mi=SysclassRunner&cls=>PWGInterface_RequestAllAX3Tradeagreements

# Interface cost prices from Axapta sister companies

Some general remarks:

Activate business process "CostPriceInquiry" for all D365FO requesting companies:

![A screenshot of a computer Description automatically generated](media/image31.png){width="5.942181758530184in" height="1.4584601924759406in"}

"Axapta sister company" is defined by vendor group:

![A screenshot of a computer Description automatically generated](media/image32.png){width="6.268055555555556in" height="1.8819444444444444in"}

Axapta menu item:

![A screenshot of a computer Description automatically generated](media/image33.png){width="6.268055555555556in" height="1.8520833333333333in"}

This is data retrieved from the table "PWGInterfaceCostPriceInquiry"

![A screenshot of a computer Description automatically generated](media/image34.png){width="6.268055555555556in" height="1.9111111111111112in"}

A daily batch job based will be set on a job "PWGInterfaceCostPriceInquiryUpdate" to verify cost price updates in the related sister companies. If this is the case: the field "SendUpdate" will be checked for the record and a new price will be sent towards D365FO.

In practice, the batch job will create in the background a temporary PO in Axapta from the requesting company in order to retrieve the current price of the items. Updated prices will be withhold, the PO will be deleted during batch execution.

Updated prices will be sent towards D365FO in one message grouped by legal entity.

The batch job will be setup together with Support team to make sure not to intervene with other batch jobs: [How to schedule a job as batch in Axapta.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Internal/AX3/Manuals%20Axapta%203/Batch%20job/How%20to%20schedule%20a%20job%20as%20batch%20in%20Axapta.docx?d=wf74b816bc1264f319ccf2938276488fe&csf=1&web=1&e=33WYHL)

An initial upload to "PWGInterfaceCostPriceInquiry" can be done via a text (tab separated) file via job "PWGImportInterfaceCostPriceInquiry". Following fields have to be filled:

- Itemid = axapta number

- Configid = axapta number

- OriginAx3company = Purchasing ax3 entity

- DestinationAx3Company = Selling ax3 entity

- Ax3vendor = selling ax3 vendor

- Unit1 -- purchase unit

- Unit2 -- inventory unit

- Unit3 -- purchase order unit

If no purchase price is available (price = 0 eur) then this will not be sent towards D365FO. This way, we also avoid that real trade agreements from Axapta sisters who don't have stock management in Axapta (Cappers, Herco,..) will be overwritten with a 0 price record.

## 2.1 Axapta sister company as default vendor on released product

Create new Released Product from product staging with default vendor = sister company

- [Still to be foreseen (ticket 9782 in sprint 10)]{.mark}

Update released product default vendor:

![A screenshot of a computer Description automatically generated](media/image35.png){width="6.268055555555556in" height="2.7256944444444446in"}

A "Command" "CostPriceInquiry" is sent from D365FO towards AX3

![](media/image36.png){width="6.268055555555556in" height="0.6736111111111112in"}

In AX3, the item is added in the Cost price inquiry table:

![A screenshot of a computer Description automatically generated](media/image37.png){width="6.268055555555556in" height="2.21875in"}

In the background, in AX3, a temporary sales order from sister company is made towards requesting company. This sales price is retrieved to update the new record. Sales order will be deleted immediately once price is saved in the table.

The price is sent back towards D365FO for all units and saved as a trade agreement. This is done via the "CostPriceInquiry" business process

![](media/image38.png){width="6.268055555555556in" height="0.5118055555555555in"}

![A screenshot of a computer program Description automatically generated](media/image39.png){width="3.724300087489064in" height="3.503253499562555in"}

![A screenshot of a computer Description automatically generated](media/image40.png){width="6.268055555555556in" height="0.7819444444444444in"}

An interface icon ![](media/image41.png){width="0.6833923884514436in" height="0.40836832895888014in"} is shown for interfaced records.

## 2.2 Purchase order towards an Axapta sister company

A purchase order is created towards an Axapta sister. As soon as the **purchase inquiry** is sent, the items will be sent towards AX3

![A screenshot of a computer Description automatically generated](media/image42.png){width="6.268055555555556in" height="2.089583333333333in"}

An outgoing "Command -- CostPriceInquiry" is sent towards Axapta.

[Remark that we will only include items when purchase order unit \<\> purchase and inventory unit of the released product (as these should be included already in the inquiry table when item was created) 🡪 currently all items are included but this filter will be included with ticket 9782 in sprint 10]{.mark})

![](media/image43.png){width="6.268055555555556in" height="0.7576388888888889in"}

The item is added in the cost price inquiry table.

![](media/image44.png){width="6.268055555555556in" height="0.7576388888888889in"}

Axapta sends back the cost price for the requested item with Business process "CostPriceInquiry"

![](media/image45.png){width="6.268055555555556in" height="0.4777777777777778in"}

In the message, the record is split by unit that is stored in the cost price inquiry table.

![A screen shot of a computer program Description automatically generated](media/image46.png){width="3.983678915135608in" height="7.825678040244969in"}

For both units, a trade agreement is added. Remark that the unit conversion is applied as the cost price in the message is based on the cost price unit of Axapta legal entity.

In this example: Axapta inventory unit = PCS 🡺 cost price = 8.53 🡺 Conversion (1box = 24 pcs) in D365FO when creation the trade agreement 🡺 TA for 1 box = 8.53 x 24 = 204.72 eur

![](media/image47.png){width="6.268055555555556in" height="0.7576388888888889in"}

(remark, a record for pcs for 8.53 eur is also added but not visible on printscreen)
