# KB — F&O Currency changes

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Currency changes.docx`
**Conversiedatum:** 2026-04-24

---

13/11/2024

In AX, when you have a trade agreement in a certain currency and a sales order in a different currency, the system will automatically recalculate the price using the exchange rates. This automation was tailor made in AX. In D365, this doesn't work automatically so we will have to build some functionality ourselves.

An automatic solution will not be functional anytime soon so until then this is what you can do:

Situation: You create a sales order which is automatically in EUR currency, but trade agreements are in GBP so you don't get sales prices for your items.

# Workaround

1.  Update Currency on sales order header to GPB, click on a sales order line to get this pop-up:

![](media/image2.png){width="4.020833333333333in" height="1.96875in"}

This will update the price to GPB

![](media/image3.png){width="6.268055555555556in" height="0.4486111111111111in"}

2.  Revert the currency on sales order header back to EUR, click on the sales order line to get the popup. Select "exchange rate only" as we actually don't have a TA in EUR:

![A screenshot of a computer Description automatically generated](media/image4.png){width="4.1875in" height="2.03125in"}

GBP price will now be converted to EUR:

![](media/image5.png){width="6.268055555555556in" height="0.4534722222222222in"}

# Currency exchange rates

The applied rate can be found in "General ledger -- Currencies -- Currency exchange rates":

![A screenshot of a currency exchange rate Description automatically generated](media/image6.png){width="6.268055555555556in" height="3.8131944444444446in"}

The rates are alligned with the Axpata rates and are updated by Boekan every quarter
