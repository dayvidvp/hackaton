# KB — F&O JSC&EWC flow KENNET

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O JSC&EWC flow KENNET.docx`
**Conversiedatum:** 2026-04-24

---

Example item:

> **X. Coral MK2 10L Cabinet Assy**

A.  10L Coral MK2 Cab C/W Lid (RX102 Marble)

B.  Q1012 2½\'\' Top Hole Pole-Less No Base (A8)

C.  PC Overflow set White

D.  Joint Rubber 2mm 3/4\'\'

# Create purchase order for Item a

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="3.575in"}

Fill In warehouse EXTERNAL & location of vendor.

Generate purchase Inquiry and mail to vendor.

Confirm with confirmed receipt date.

# Create Inventory adjustment to send components B,C & D to vendor

![A screenshot of a computer Description automatically generated](media/image3.png){width="6.268055555555556in" height="1.6479166666666667in"}

Use special reason code: **15: Components to vendor for production**

![A screenshot of a computer Description automatically generated](media/image4.png){width="6.268055555555556in" height="2.3333333333333335in"}

Components B, C & D go out of MAIN stock and go Into EXTERNAL stock with correct vendor location.

Post journal.

Print journal & give to people In warehouse for picking and shipping.

![A screenshot of a computer Description automatically generated](media/image5.png){width="6.268055555555556in" height="2.8444444444444446in"}

# receive purchase order for Item a

When the goods arrive In the warehouse, go to the original PO.

Go to **Receive - Generate - Product receipt**. (PO must be confirmed!)

Make sure quantity Is \"**Ordered quantity**\".

Fill In a **Product receipt** (= delivery note reference from vendor).

Check If the correct lines & quantities are taken Into account.

Click **OK**.

![A screenshot of a computer Description automatically generated](media/image6.png){width="6.268055555555556in" height="3.2993055555555557in"}

# Create Inventory adjustment to \"build\" Item X

![A screenshot of a login Description automatically generated](media/image7.png){width="2.732043963254593in" height="1.7461964129483813in"}Use special reason code: **40:** **Conversion of Items**

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.6561843832021in" height="1.6386034558180227in"}

Components A, B, C & D go out of EXTERNAL stock and finished product X goes In MAIN stock.
