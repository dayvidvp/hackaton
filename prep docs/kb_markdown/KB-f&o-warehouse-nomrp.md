# KB — F&O Warehouse NOMRP

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Warehouse NOMRP.docx`
**Conversiedatum:** 2026-04-24

---

**Warehouse NOMRP**

Warehouse: NOMRP

Name: For purchasing with long leadtime

**[Situation]{.underline}**

For products of which you buy big quantities with a long lead time from a specific manufacturer, you sometimes run out of stock before the purchase orders are delivered. You have an option to purchase smaller quantities from local vendors or sister companies, but because of settings the Item does not appear In MRP to be purchased.

**[How to make sure you get useful planned orders In master planning?]{.underline}**

[1. Correct settings on the released products that are Involved In this flow.]{.underline}

Example:

- Release product: 10147000004 - Tank 8x17 Blue color with base

- Vendor: 0029910 - CANATURE HOLDINGS HK LTD (Important for costing, based on purchase trade agreements linked to this vendor)

- Coverage Group: MAN (Mainly manual purchasing via planned document In stead of MRP. MAN Is excluded from Master planning)

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="2.6015168416447945in" height="2.8098151793525807in"}

Specific Item coverage settings via:

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="3.337380796150481in" height="1.0604483814523185in"}

- You need 1 line for the minimum stock for the MAIN warehouse which Is purchased via masterplanning (RTS) from the local vendor/sister company.

- You need 1 line for the minimum stock for the NOMRP warehouse which Is purchased via planning document (MAN) from the main vendor with a long lead time.

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="0.9590277777777778in"}

For the first line, to change the coverage group MAN Into RTS-028 (replenish to stock) and to change the vendor, go Into General tab, click the checkmark and make the changes as shown below.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="2.4712751531058617in" height="1.9314566929133858in"}

Add the second line as well.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="6.268055555555556in" height="1.2472222222222222in"}

[2. Correct settings on the purchase orders Involved In this flow.]{.underline}

The bigger quantities are purchased based on a planning document report In which you can calculate how much you need to purchase over a longer period of time. In the purchase order you create, you set the warehouse and location to NOMRP. (In the example a purchase order with Canature Is warehouse NOMRP and a purchase order with Euraqua Is warehouse MAIN)

When the goods from the big PO actually arrive, change the warehouse back to MAIN to receive the goods.

Never receive goods physically In warehouse NOMRP.

Tip: Create a view where the Warehouse Is a column In your Purchase order lines. This way you can easily change It. f you don\'t you have to go to the Line details - Product, for every Item.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="3.3305555555555557in"}

[Extra: Where to find planning document?]{.underline}

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="2.096804461942257in" height="2.230003280839895in"}
