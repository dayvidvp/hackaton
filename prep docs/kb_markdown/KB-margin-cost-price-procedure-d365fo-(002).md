# KB — Margin cost price procedure D365FO (002)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `Margin cost price procedure D365FO (002).docx`
**Conversiedatum:** 2026-04-24

---

# How to setup a margin cost price in D365

# Contents {#contents .TOC-Heading}

[How to setup a margin cost price in D365 [1](#how-to-setup-a-margin-cost-price-in-d365)](#how-to-setup-a-margin-cost-price-in-d365)

[Costing version [1](#_Toc156375418)](#_Toc156375418)

[Costing sheet [2](#costing-sheet)](#costing-sheet)

[Manual calculation by item [2](#manual-calculation-by-item)](#manual-calculation-by-item)

[Purchase item [2](#purchase-item)](#purchase-item)

[Production item [4](#production-item)](#production-item)

[Manual calculation for all items [6](#manual-calculation-for-all-items)](#manual-calculation-for-all-items)

[As is situation [6](#as-is-situation)](#as-is-situation)

[To be process [7](#to-be-process)](#to-be-process)

[]{#_Toc156375418 .anchor}

# Costing version 

A custom cost type "Margin cost" is foreseen

![A screenshot of a computer Description automatically generated](media/image1.png){width="6.268055555555556in" height="1.5652777777777778in"}

Based on item type, calculation will be different:

Production item = based on sum of margin cost prices of bom components

Purchase item = based on trade agreement price of the default vendor defined on item

![A screen shot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="1.2569444444444444in"}

If a trade agreement is missing or a bom component does not have a margin cost price 🡺 The calculated margin cost price will be defaulted to zero.

# Costing sheet

The costing sheet contains the components of the margin cost price

Purchase item vs production item

+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Purchase item                                                                    | Production item                                                                  |
+==================================================================================+==================================================================================+
| ![](media/image3.png){width="2.861399825021872in" height="1.7988943569553806in"} | ![](media/image4.png){width="2.832029746281715in" height="1.0069444444444444in"} |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Transport matrix:                                                                |                                                                                  |
|                                                                                  |                                                                                  |
| - By vendor (default vendor)                                                     |                                                                                  |
|                                                                                  |                                                                                  |
| - Transportcharge group defined on item                                          |                                                                                  |
|                                                                                  |                                                                                  |
| ![](media/image5.png){width="4.995705380577427in" height="3.0461614173228346in"} |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Management override (pwg fee):                                                   |                                                                                  |
|                                                                                  |                                                                                  |
| - Currently 5% for items purchased externally                                    |                                                                                  |
|                                                                                  |                                                                                  |
| - 1.85% for items purchased from Pollet Pool                                     |                                                                                  |
|                                                                                  |                                                                                  |
| - Add items separately                                                           |                                                                                  |
|                                                                                  |                                                                                  |
| ![](media/image6.png){width="5.886672134733159in" height="3.19045384951881in"}   |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

# Manual calculation by item

## Purchase item

Default order type = purchase

Margin cost price on released product will be copied to sales order line at the moment of so line creation. When SO invoicing, the margin cost price at invoice date will be saved on sales order invoice journal too.

![A screenshot of a computer Description automatically generated](media/image7.png){width="6.268055555555556in" height="2.979861111111111in"}

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.268055555555556in" height="1.5618055555555554in"}

Purchase order is retrieved from default order type on released product. Can be updated below

![A screenshot of a computer Description automatically generated](media/image9.png){width="4.47538823272091in" height="3.7169892825896764in"}

View calculation:

![A screenshot of a computer Description automatically generated](media/image10.png){width="6.268055555555556in" height="1.367361111111111in"}

If an item should not have a trade agreement , this will be indicated with a "!" in the column "Zero margin price"

Costing sheet view:

![A screenshot of a computer Description automatically generated](media/image11.png){width="5.983851706036745in" height="1.8334919072615923in"}

Calculated price can be activated:

![A screenshot of a computer Description automatically generated](media/image12.png){width="6.268055555555556in" height="0.9222222222222223in"}

## Production item

Default order type = Production

Margin cost price on released product will be copied to sales order line at the moment of so line creation. When SO invoicing, the margin cost price at invoice date will be saved on Sales order invoice journal too.

![A screenshot of a computer Description automatically generated](media/image13.png){width="6.268055555555556in" height="2.9722222222222223in"}

![](media/image14.png){width="6.268055555555556in" height="0.6965277777777777in"}

![A screenshot of a computer Description automatically generated](media/image15.png){width="6.268055555555556in" height="1.6895833333333334in"}

If a BOM component should not have a margin cost price, this will be indicated with a "!" in the column "Zero margin price"

Costing sheet view:

![A screenshot of a computer Description automatically generated](media/image16.png){width="5.492142388451444in" height="1.3417825896762905in"}

Calculated price can be activated:

![A screenshot of a computer Description automatically generated](media/image17.png){width="6.268055555555556in" height="0.8201388888888889in"}

# Manual calculation for all items

Calculate from costing version instead of from item:

![](media/image18.png){width="6.268055555555556in" height="1.7569444444444444in"}

![A screenshot of a calculator Description automatically generated](media/image19.png){width="4.40038167104112in" height="4.383712817147856in"}

Calculated prices will be visible as pending prices which can be activated.

# As is situation

Margin cost prices of purchase item have been copied from Axapta

Margin cost prices of production items still in a pending state (as bom's were reviewed by Lieven during go-live)

- Compare with Axapta cost prices

- Decide to include in BOM review process: calculate and activate?

- How will these be activated? 🡪 Decision to take on activation

Sales order lines without a margin cost price

- [Who will calculate/decide on activation 🡪 Lieven?]{.mark}

- Manually copy activated price and fill on SO line

# To be process

Following steps in order to recalculate:

1.  A daily batch job can be run to recalculate items in margin trigger update table:

![A screenshot of a computer Description automatically generated](media/image20.png){width="4.40038167104112in" height="2.7752405949256342in"}

Not only items in list will be recalculated but also impacted bom's

2.  The calculated prices can be reviewed (manually)

3.  The calculated prices can be activated (manually of via batch)

[Who will be responsible?? When to start using this functionality?]{.mark}

A margin cost price update trigger table is foreseen.

![A screenshot of a computer Description automatically generated](media/image21.png){width="6.268055555555556in" height="1.7131944444444445in"}

![A screenshot of a computer Description automatically generated](media/image22.png){width="6.268055555555556in" height="7.032638888888889in"}

Already included:

- Item get's new trade agreement (trigger date will be the "from date")

- New indirect cost is added in costing sheet (f.e. new transportcharge, new PWG fee,..)

- Parameters to include or exclude items from margin cost calculation (on released product)

![A close-up of a price Description automatically generated](media/image23.png){width="4.783747812773403in" height="1.5001301399825022in"}

- Next update = date which is set as new calculation date. (f.e. new trade agreement active from 1/7/2024 🡺 only the 1st of July, the margin cost price will be recalculated)

- Never recalculate a margin cost price 🡺 item will never appear in trigger table 🡪 [Which items?? (f.e item 11564000026 (ax: 2803010013))]{.mark}

- Allow zero margin cost price 🡪 no margin warning/error on SO line when confirmation/invoicing 🡪 [Which items??]{.mark}

- Calculate margin cost price taken into account a staffel quantity (= TA price quantity field on item) 🡪 [Which items??]{.mark}

Still to be included? (next sprints/releases):

Additional triggers to include an item in the margin cost update trigger table:

- Currency updates

- New trade agreement discounts

- Updates on active bom versions? Impact on linked bom's containing updated bom
