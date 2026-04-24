# KB — F&O Planning document for purchasing

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Planning document for purchasing.docx`
**Conversiedatum:** 2026-04-24

---

# Where to find It In D365

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="2.5378488626421696in" height="2.689067147856518in"}

# How to run the report

This report runs based on the criteria you set In the query.

When you open the query for the first time, the number of fields Is limited. You have to option to add as many fields as you wish to add criteria.

Typically you will run a planning document based on a specific vendor or on a specific product(group).

In this example I have added a line In the query to be able to select a vendor. I\'ve selected a vendor from the drop-down menu. As always, It Is possible to save your queries If you plan on using them regularly.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="2.354861111111111in"}

# What to do with the results

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="5.6137357830271215in" height="1.615207786526684in"}

The first result Is a table with all the Information the planning document can provide. It will show this Information for all of the Items that fit the query. So In this example, all the Items that have the vendor 0029910.

Now It Is easy to export this table to excel to use some simple math formulas to determine which Items you want to purchase and In what quantities.

These are all the columns that are automatically available In a planning document:

  -------------------------------------------------------------------------------------
  Item number               Open prod
  ------------------------- -----------------------------------------------------------
  Configuration             Physical inventory

  Product name              Physical reserved

  Configuration name        Available physical

  Search name               [Ordered in total = CONFIRMED in purchase order]{.mark}

  Site                      [On order = in sales order but no available stock]{.mark}

  Warehouse                 Total available

  Inventory unit            Last transaction

  Purchase unit             First consumption 3M

  Coverage group            Total consumed 3M

  Lead time                 First sales 3M

  Minimum                   Total sold 3M

  Maximum                   First consumption 12M

  Min. order qty            Total consumed 12M

  Standard order quantity   First sales 12M

  Multiple                  Total sold 12M

  Vendor                    Coverage ordered total
  -------------------------------------------------------------------------------------
