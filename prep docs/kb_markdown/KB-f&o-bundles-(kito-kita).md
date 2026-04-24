# KB — F&O Bundles (KITO KITA)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Bundles (KITO-KITA).docx`
**Conversiedatum:** 2026-04-24

---

A bundle item represents a fixed set of items that are sold or purchased together.

**[Setup in D365]{.underline}**

- Defined by **Released product details \> General \> Bundles \> YES** 

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="5.3735378390201225in" height="3.028494094488189in"}

- A bundle item always has its Production type (**Released product details \> Engineer \> Production type**) set to BOM, with an active BOM version defined that contains the items making up the bundle.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="5.516724628171478in" height="1.2963626421697287in"}

- In case of a sales bundle, the vendor is your own company. In case of a purchase bundle, the vendor will be the actual supplier.

> ![A screenshot of a website AI-generated content may be incorrect.](media/image4.png){width="3.6702088801399824in" height="1.8703937007874016in"}

- A bundle should always have its Default order type (**Released product details \> Manage inventory \> Default order settings**) set to \'Production\'. 

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="1.8902777777777777in"}

- For the bundle to work properly the released product needs to be linked to an active BOM.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="3.5358475503062117in" height="1.3922451881014872in"}
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.5451388888888888in"}
>
> There is a separate manual on how to create BOMs.

- A bundle item in a sales or purchase order is always exploded to show the underlying items. The column Isbundle shows if the items is a parent (bundle item) or a child (bundle item component). 

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="5.144224628171479in" height="2.474653324584427in"}
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="0.8763888888888889in"}

- Bundle items are never kept on stock, only their components are kept on stock. Therefore bundle items themselves are never used in warehouse flows. Pick work is generated for bundle item components (child) but not for bundle items (parent). 

<!-- -->

- System checks are set up so that all bundle components are added to the same load and in the correct proportional quantities. 

- Any changes regarding quantity or price that you want to make to a Bundle after explosion need to be done on the parent code via the separate Bundle button.

![A screenshot of a product AI-generated content may be incorrect.](media/image10.png){width="4.2679133858267715in" height="1.4351607611548556in"}

![A screenshot of a computer screen AI-generated content may be incorrect.](media/image11.png){width="4.867884951881015in" height="2.4145264654418197in"}

To cancel the order lines you need to cancel the deliver remainder via de bundle parent.

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="1.625in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="2.241609798775153in" height="0.9906266404199475in"}

![](media/image14.png){width="6.268055555555556in" height="0.7611111111111111in"}
