# KB — F&O Purchase  Over & underdelivery

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase_ Over & underdelivery.docx`
**Conversiedatum:** 2026-04-24

---

In case the delivered quantities differ from the expected quantities, it is advisable to communicate with your supplier in order to have the same data in your respective systems to avoid problems with invoice matching later on.

This manual does not describe how this communication should go nor how PO & SO changes should be coordinated between supplier/customer nor how backorders/recollects should be arranged.

It just describes from a warehousing point of view how over/underdeliveries in loads can be received and completed in the system in order to make these goods asap available for outbound flows.

**1. Overdelivery**

### [Receive with settings:]{.underline}

It is possible to set up the product masterdata so that overdeliveries are allowed by default.

Firstly, you set the overdelivery-parameter correct via **Procurement and sourcing \> Setup \> Procurement and sourcing parameters:**

![A screenshot of a product delivery box Description automatically generated](media/image2.jpeg){width="3.933333333333333in" height="1.3240923009623797in"}

Secondly, you go to **Product information management \> Released product details \> Purchase**. You enter an allowed overdelivery percentage on this particular item:

![A screenshot of a product Description automatically generated](media/image3.jpeg){width="1.6123589238845144in" height="1.7083333333333333in"}

If you make a purchase order for this item, you\'ll see that the overdelivery percentage on the PO-line is by default copied from the released product masterdata.

However, you can still always change this percentage in every PO-line.

![A screenshot of a computer Description automatically generated](media/image4.jpeg){width="3.15in" height="1.525in"}

If you add the PO-line to a load, the overdelivery percentage will also be copied to the load line. This will allow you to overreceive with the scanner. Beware, the load line will not automatically take over any changes you make to the percentage in the PO-line. So if you want to make changes, it\'s easiest to just delete the old load line and create a new one.

![A screenshot of a computer Description automatically generated](media/image5.jpeg){width="6.298611111111111in" height="1.2173611111111111in"}

With the scanner, you will now be able to receive a larger quantity than you had ordered (within the margins of the overdelivery percentage of course). You will not get errors during the reception process.

During the posting of the product receipt, the quantity of the load line will be automatically increased to the delivered quantity.

### [Receive without settings:]{.underline}

You can also choose not to allow overdeliveries by default and therefore keep the overdelivery percentage on 0% on the released product level.

In case an overdelivery then happens, you can just add an extra line to the PO representing the quantity that is overdelivered. Then add this line to the line, and receive the overdelivered quantity with the scanner on this load line.

**2. Underdelivery**

### [Receive with settings:]{.underline}

It is possible to set up the product masterdata so that underdeliveries are allowed by default.

Firstly, you set the underdelivery-parameter correct via **Procurement and sourcing \> Setup \> Procurement and sourcing parameters:**

![A screenshot of a product delivery box Description automatically generated](media/image2.jpeg){width="3.933333333333333in" height="1.3240923009623797in"}

Secondly, you go to **Product information management \> Released product details \> Purchase**. You enter an allowed underdelivery percentage on this particular item:

![A screenshot of a phone Description automatically generated](media/image6.jpeg){width="1.1083333333333334in" height="2.3102252843394577in"}

If you make a purchase order for this item, you\'ll see that the underdelivery percentage on the PO-line is by default copied from the released product masterdata.

However, you can still always change this percentage in every PO-line.

![A screenshot of a computer Description automatically generated](media/image7.jpeg){width="6.298611111111111in" height="1.2965277777777777in"}

If you add the PO-line to a load, the underdelivery percentage will also be copied to the load line. This will allow you to underreceive with the scanner. Beware, the load line will not automatically take over any changes you make to the percentage in the PO-line. So if you want to make changes, it\'s easiest to just delete the old load line and create a new one.

![A screenshot of a computer Description automatically generated](media/image8.jpeg){width="6.298611111111111in" height="0.94375in"}

With the scanner, you will now be able to receive a smaller quantity than you had ordered (within the margins of the underdelivery percentage of course). You will not get errors during the reception process.

During the posting of the product receipt, the quantity of the load line will be automatically decreased to the delivered quantity.

Be aware that the remainder on the PO will remain open!

### [Receive without settings:]{.underline}

You can also choose not to allow underdeliveries by default and therefore keep the underdelivery percentage on 0% on the released product level.

In case an underdelivery then happens, you need to adjust the quantity of your load line to the quantity received (reverse the shipment confirmation if necessary). Then finish the load as usual.

Next, adjust your PO-line:

\- Add the remainder of the PO-line to a new load

\- or select the PO-line, then click **Update line \> Deliver remainder**. Now set the remainder to zero

REMARK: Do not change the remainder of the PO-line before generating the product receipt of the load. Otherwise you can receive an error message when generating the product receipt. In that case you\'ll have to change the underdelivery percentage of the PO-line before you\'ll be able to generate the product receipt.
