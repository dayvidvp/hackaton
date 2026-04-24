# KB — F&O Sales line availability

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales line availability.docx`
**Conversiedatum:** 2026-04-24

---

The sales line availability Is a tool where you can get an overview of whatever open sales lines you choose to see depending on the filters In your query.

To use it, you need to run a "query" and then you will get all the open sales order lines for the choices you made in the query.

**Example 1: All open SO lines for 1 specific SO**

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="5.281346237970253in" height="2.6997714348206476in"}

**Example 2: All open SO lines for 1 specific customer**

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="5.465622265966754in" height="3.306258748906387in"}

**Example 3: All open SO lines for 1 specific sales taker**

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="2.79375in"}

You can save the "query" under a name so you can use it again the next time.

- **Step 1: Save as**

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="3.8645833333333335in" height="1.7395833333333333in"}

- **Step 2: Choose a name for the query**

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="2.375in" height="1.53125in"}

- **Step 3: Select the query next time you need it**

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="2.465294181977253in" height="1.277694663167104in"}

- **[Filters]{.underline}**

![](media/image8.png){width="0.27200021872265967in" height="0.24in"}there are multiple filters to choose from, so that you only retrieve the Information that you want. The filter Icon can be found on the top right.

![A screenshot of a computer screen Description automatically generated](media/image9.png){width="1.1118055555555555in" height="1.5395833333333333in"}

- **[Load advice]{.underline}**

In the load advice columns you can see If a line Is fully reserved or not and can consequentially be put on a load or not.

- Error: This line cannot be put on a load e.g.; there Is no stock

- OK: The complete line can be put on a load

- Partial: Only part of the line can be put on a load eg; only part of the wanted quantity Is In stock

- ![A screenshot of a computer Description automatically generated](media/image10.png){width="2.3715277777777777in" height="1.3791666666666667in"}Warning: You can see the warning(s) by hovering over the yellow rectangle. In this example, the customer Is In credit management and the line Is not fully reserved as well.

> Lines with a load advice \'Error\' or \'Warning\' will give an error If you try to put those on a load.
>
> If you use a setting in the sales order "complete order", the load advice will only be OK when all the lines are in stock. If you don't use this setting, the lines that are in stock will have a positive load advice and the lines that are not in stock will have a negative load advice.

- **[Sales orders]{.underline}**

All the different lines of a sales order are shown on the sales line availability. For example, SO2400229-1011 counts 6 lines. So, you have an overview of the whole sales order. It Is also possible to filter per SO If wanted, either In the column or with the filter on the top right.

You can reach an SO as well, by clicking on the SO-number

![A screenshot of a computer Description automatically generated](media/image11.png){width="2.490972222222222in" height="1.3118055555555554in"}

- **[Deliver remainder]{.underline}**

It Is also possible to change or close off deliver remainders on the sales line availability.

![A screenshot of a computer Description automatically generated](media/image12.png){width="6.268055555555556in" height="2.7118055555555554in"}Select the line of which you want to change the deliver remainder and via Sales orders \--\> Update line \--\> Deliver remainder, you can update the quantity that still has to be delivered.

> ![A white background with black text Description automatically generated](media/image13.png){width="1.9520833333333334in" height="0.7277777777777777in"}For example, only 3pcs need to be delivered anymore, then you just fill In 3 In Deliver remainder and click OK.
>
> Now the line Is updated to a deliver remainder of 3.
>
> ![A screenshot of a computer Description automatically generated](media/image14.png){width="6.268055555555556in" height="1.28125in"}

- **[Load]{.underline}**

You can also see If a line Is already on a load or not In the column \'Load advice\'. The load number Is shown here In case the line Is on a load already. It Is possible to reach the load Immediately by clicking on the load number.

Via Warehouse \--\> Outbound load planning workbench you can put the selected lines on a load.

- **[Other useful Information]{.underline}**

<!-- -->

- Item number with the associated configuration

- Production: If a sales line needs production, this can also be seen from the sales line availability. In the column \'Is production\' an Icon shows If the line production or not. If yes, other columns show more Information about the production order In case one exists already (Status, component reservation, Production delivery date, production)

- Bundle: In the column \'Bundle\' It Is visible whether or not an Item Is a bundle (component).

- The columns \'Physical reserved\' and \'Available physical\' show, respectively, the quantity reserved for that line and the amount of stock that Is available for reservation.

- Line amount

- Delivery name of the customer

**[Where can you find it?]{.underline}**

Via Modules:

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="2.252587489063867in" height="3.802612642169729in"}
