# KB — F&O Credit notes (admin)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Credit notes (admin).docx`
**Conversiedatum:** 2026-04-24

---

# Bonus

1.  Create SO

2.  Add item: Bonus on sales.

3.  Quantity = -1

4.  Fill in unit price.

5.  Cost price = 0 €

6.  Generate invoice.

![](media/image2.png){width="5.942199256342957in" height="4.884689413823272in"}

# Commercial discount

1.  Create SO

2.  Add item: Commercial discount.

3.  Quantity = -1

4.  Fill in unit price.

5.  Cost price = 0 €

6.  Generate invoice.

# Invoice correction due to administrative mistake

- **[Wrong price on item or transport]{.underline}**

  1.  Go to original SO.

  2.  Add item: Item number of which price was wrong.

  3.  Fill in negative quantity corresponding with the invoiced quantity.

  4.  Fill in the unit price = difference between wrong and correct price.

  5.  Cost price = 0.01 €.

  6.  In the line details **Product**, change the location to : **CreditOnly**.

  7.  In the line details **Setup**, put the checkbox **SCRAP** on YES.

  8.  Generate the invoice.

> ![](media/image3.png){width="5.599847987751531in" height="4.109905949256343in"}

\*In case this includes bundle lines, check 3.1

- **[Wrong invoice account]{.underline}**

A.  **Credit wrong invoice**

    1.  Go to the original SO.

    2.  Copy all lines, invert sign.

    3.  Change warehouse and location to ADMIN.

    4.  Generate invoice.

B.  **Generate new correct invoice**

    1.  Create new SO with correct invoice account!

    2.  Copy all CN lines from original SO, invert sign.

    3.  Check if warehouse and location are set to ADMIN.

    4.  Generate invoice.

![](media/image4.png){width="5.374745188101487in" height="1.132846675415573in"}

\*In case this includes bundle lines, check 3.1

- **[Wrong VAT group]{.underline}**

A.  ![](media/image5.png){width="1.210356517935258in" height="2.815699912510936in"}**Credit wrong invoice**

    1.  Go to the original SO.

    2.  Copy all lines, invert sign.

    3.  Change warehouse and location to ADMIN.

    4.  Generate invoice.

B.  **Generate new correct invoice**

<!-- -->

1.  Create new SO with correct VAT group and delivery address!

2.  Copy all CN lines from original SO, invert sign.

3.  Check if warehouse and location are set to ADMIN.

4.  Check the VAT group on the lines.

5.  Generate invoice.

![](media/image6.png){width="5.121738845144357in" height="1.2421325459317585in"}

\*In case this includes bundle lines, check 3.1

## Bundles

The transaction for bundles are posted on their components. However, It Is not possible to explode a bundle with a negative quantity. Use the following steps Instead for bundle Items.

![A screenshot of a computer Description automatically generated](media/image7.png){width="7.917361111111111in" height="1.1597222222222223in"}1. Add all the bundle components with a negative quantity

![A screenshot of a computer Description automatically generated](media/image8.png){width="3.6180555555555554in" height="1.8736111111111111in"}

2\. Change warehouse and location depending on the situation

Change location to Creditonly In case of a wrong price

Change warehouse and location to ADMIN In case of a wrong Invoice account or VAT group

3\. Generate Invoice.

In case a new correct Invoice has to be generated:

4\. Add bundle components with correct VAT group.

5\. Change warehouse and location to ADMIN.

6\. Check If prices are OK.

8\. Generate Invoice.

9\. The components will be printed on the document In this case, so some extra Information towards the customer In the email might be necessary.

# Invoice correction due to logistical mistake (check Sales returns!)
