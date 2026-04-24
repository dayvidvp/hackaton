# KB — F&O Margin cost price calculation production items AQC

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Margin cost price calculation production items AQC.docx`
**Conversiedatum:** 2026-04-24

---

# existing Production Item

Go to released products - Manage costs - Item price

![](media/image2.png){width="5.432404855643044in" height="1.2729385389326333in"}

In the tab Active prices you can see the cost and Margin cost prices that are/were active. You clearly see the type, the activation date, the configuration and the price.

![](media/image3.png){width="6.268055555555556in" height="1.3993055555555556in"}

In Pending prices we see that there was an automatic calculation that ended up with empty prices. Via View calculation details you can check what the Issue was.

![](media/image4.png){width="6.268055555555556in" height="1.0965277777777778in"}

Issue are marked with !

In this case 2 components of the BOM didn\'t have an activate MCP at the moment of the calculation (12/3/2026).

![](media/image5.png){width="6.0446555118110235in" height="2.2983891076115484in"}

When you go to those Items, and also check the Item price, you see that a MCP was calculated 19/3. So It will now be possible to recalculate the MCP of the BOM.

![](media/image6.png){width="6.268055555555556in" height="1.2138888888888888in"}

![](media/image7.png){width="6.268055555555556in" height="1.304861111111111in"}

![](media/image8.png){width="6.268055555555556in" height="1.270138888888889in"}

![](media/image9.png){width="6.268055555555556in" height="1.5020833333333334in"}

First we delete the 2 pending MCP that were empty.

![](media/image10.png){width="6.268055555555556in" height="1.13125in"}

Now we can calculate the new MCP.

![](media/image11.png){width="3.946761811023622in" height="1.758591426071741in"}

![](media/image12.png){width="4.307720909886264in" height="6.305518372703412in"}

You need to do It for every configuration separately. Once you have the prices, you can activate them.

![](media/image13.png){width="6.268055555555556in" height="1.5888888888888888in"}

Now the MCP are activated for both configurations.

![](media/image14.png){width="6.268055555555556in" height="2.0284722222222222in"}

# New production Item

When you create a new configuration for a production Item, you also need to calculate the MCP. These are printscreens of the entire flow.

![](media/image15.png){width="6.268055555555556in" height="3.709722222222222in"}

Fill In the new configuration code and click on create.

![](media/image16.png){width="3.9115605861767277in" height="1.958814523184602in"}

Click on the configuration number.

![](media/image17.png){width="6.268055555555556in" height="0.9118055555555555in"}

Add a name for the configuration.

![](media/image18.png){width="6.268055555555556in" height="1.45in"}

Go back to the SO and now click on the Item number to go to the Released product.

![](media/image19.png){width="4.462847769028872in" height="1.6034798775153105in"}

Go to Bom versions en create a new Bom and Bom version.

![](media/image20.png){width="3.789620516185477in" height="2.5336734470691162in"}

Set Copy to YES.

![](media/image21.png){width="1.428814523184602in" height="1.9026913823272091in"}

After clicking OK, the pop up menu changes to this one:

![](media/image22.png){width="1.7260662729658793in" height="5.508720472440945in"}

Make changes to the BOM where needed. I changed 2 quantities In this example.

Go to the header.

![](media/image23.png){width="6.268055555555556in" height="3.0944444444444446in"}

Make sure the correct configuration Is selected. Then you have 3 steps:

1\. Do the Approval

2\. Activate the BOM

3\. Calculate the MCP.

![](media/image24.png){width="6.268055555555556in" height="1.7458333333333333in"}

![](media/image25.png){width="1.7001727909011373in" height="1.5394291338582677in"}

![](media/image26.png){width="4.133877952755905in" height="3.4299365704286964in"}

After you calculate, you\'re sent to a different menu.

Activate the pending price.

![](media/image27.png){width="6.268055555555556in" height="1.5527777777777778in"}

Then you can go back to the sales order and refresh the cost price In the sales order line.
