# KB — F&O Purchase invoice approval

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase invoice approval.docx`
**Conversiedatum:** 2026-04-24

---

# Inhoud {#inhoud .TOC-Heading}

[Purchase invoice approval [1](#purchase-invoice-approval)](#purchase-invoice-approval)

[1 Price difference on a specific line [3](#price-difference-on-a-specific-line)](#price-difference-on-a-specific-line)

[2 packaging cost is missing in the PO [4](#packaging-cost-is-missing-in-the-po)](#packaging-cost-is-missing-in-the-po)

[3 Transport cost is missing in the PO [6](#transport-cost-is-missing-in-the-po)](#transport-cost-is-missing-in-the-po)

[4 there is no product receipt yet [6](#there-is-no-product-receipt-yet)](#there-is-no-product-receipt-yet)

[5 the selected lines do not match [7](#the-selected-lines-do-not-match)](#the-selected-lines-do-not-match)

[6 Procedures for credit note [7](#procedures-for-credit-note)](#procedures-for-credit-note)

# Purchase invoice approval 

Navigate to **Invoices assigned to me**.

For each invoice you can check the **subject** and the **work item instructions**.

![A screenshot of a computer Description automatically generated](media/image1.png){width="6.268055555555556in" height="1.4624343832020998in"}

Click on the invoice number that you want to process.

The system will open **Pending vendor invoices**.

The **variance status** is failed because there is a difference.

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.24298665791776in" height="0.8253149606299213in"}

Click on the invoice number again to open the **Vendor invoice**.

![A screenshot of a computer Description automatically generated](media/image3.png){width="6.268055555555556in" height="1.849309930008749in"}

Select the line and open the original invoice via the **Raptor** icon.

In the tab **view** you can see the entire invoice. Via the icon on the top right, you can open the invoice in a separate screen.

![A screenshot of a computer Description automatically generated](media/image4.png){width="6.268055555555556in" height="1.405660542432196in"}

In the **vendor invoice matching** you can see the value difference between the selected lines in the PO('s) and the registered total invoice amount.

![A screenshot of a computer screen Description automatically generated](media/image5.png){width="6.268055555555556in" height="2.0256944444444445in"}

It is now up to you to see what causes the difference.

**[Important general information:]{.underline}**

Refresh your page to see the result of changes you made. Only after refreshing and when all the differences are solved the **variance status** will change to **passed**.

When you are finished, you must approve via the **Workflow** button at the top:

![A screenshot of a computer Description automatically generated](media/image6.png){width="1.6036789151356081in" height="0.9648151793525809in"}

Always add a comment to help the next responsible with the follow-up:

![A screenshot of a computer screen Description automatically generated](media/image7.png){width="3.193168197725284in" height="1.4447233158355206in"}

# Price difference on a specific line

**[1st responsible is not sure if the invoiced price is correct, the 2nd responsible needs to check.]{.underline}**

1^st^ responsible: Change the unit price to what is on the invoice and select the reason code **CHECK**.

The invoice will then be assigned to the next responsible who will have to decide if the new price is approved or not.

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.268055555555556in" height="2.870138888888889in"}

- 2nd responsible agrees with new invoice price:

> Change the reason code to NEW TA. After approval of the invoice, there will be a new line in the menu **Update purchase prices.** In the follow-up of this menu, a new TA can be created in D365 by choosing **New.**

- 2nd responsible does not agree with new invoice price:

> Change the price back to the original and start the procedure for a **credit note for price difference**.

**[1st responsible is sure the invoiced price is correct, 2nd responsible only needs to approve.]{.underline}**

1^st^ responsible: Change the unit price to what is on the invoice and select the reason code **NOPC** (no price check needed) or **SPEC** (one-time special price) or **ROUND** (round-off).

The invoice will then be assigned to the next responsible can just approve the invoice.

- 2nd responsible agrees with new invoice price:

> After approval of the invoice, there will be a new line in the menu **Update purchase prices.** In the follow-up of this menu, you can just close the line with **Do not update price**.

**[1st responsible is sure the invoiced price is correct, 2nd responsible needs to make a new TA.]{.underline}**

1^st^ responsible: Change the unit price to what is on the invoice and select the reason code **NEW or NEWTA.**

The invoice will then be assigned to the next responsible can just approve the invoice.

- 2nd responsible agrees with new invoice price:

> After approval of the invoice, there will be a new line in the menu **Update purchase price.** In the follow-up of this menu, a new TA can be created in D365 by choosing **New.**

**[1st responsible is sure the invoiced price is not correct.]{.underline}**

1^st^ responsible: Leave the price as it is and start the procedure for a **credit note for price difference**.

Add the fitting **Reason code** in the **Vendor invoice header.**

![A screenshot of a computer Description automatically generated](media/image9.png){width="6.268055555555556in" height="1.417361111111111in"}

You can also see it in the **invoices assigned to me** menu what makes it easier for a follow-up.

![A screenshot of a computer Description automatically generated](media/image10.png){width="6.268055555555556in" height="0.8493055555555555in"}

# packaging cost is missing in the PO

First go to the PO and add the packaging cost mentioned on the invoice.

- Add a line for **99101000007: Packing and carriage cost**.

- Add the quantity and unit price and **Save.**

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.

Go back to the Vendor invoice matching and add the extra delivery note.

Click on **the + sign** next to the product receipt to select the added lines in the PO.

Now the line is added and you saved, there is no more price difference, and the **variance status** is passed.

When you approve the workflow, the invoice will not go to a 2^nd^ responsible because the issue was not a price difference.

![A screenshot of a computer Description automatically generated](media/image11.png){width="5.873244750656168in" height="4.2341251093613295in"}

# Transport cost is missing in the PO

First go to the PO to add the transport cost mentioned on the invoice.

- Add a line for **99101000003: Purchased Transport For Purchasing.**

- Add the unit price and **Save.**

<!-- -->

- Even when the line is in the same PO, you must link it. (for the transport matrix calculations):

  - Select the line and click on **Transport related orders**.

  - Select the vendor account.

  - Select the load of the goods received with this transport and click on +.

  - Select the load line at the bottom and click on OK.

![A screenshot of a computer Description automatically generated](media/image12.png){width="6.268055555555556in" height="3.3152777777777778in"}

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.

Go back to the Vendor invoice matching and add the extra delivery note.

Then click on **the + sign** next to the product receipt to select the added transport line in the PO.

Now the line is added, and you have saved, there is no more price difference, and the **variance status** is passed.

When you approve the workflow, the invoice will not go to a 2^nd^ responsible because the issue was not a price difference.

# there is no product receipt yet

1st responsible: Change the **Reason code** to **WaitForPR (Wait for Product Receipt)** and check frequently if the goods have arrived.

# the selected lines do not match

**[The wrong lines are selected, or lines are missing.]{.underline}**

1st responsible:

Click on **the + sign** next to the purchase order or product receipt to select the correct lines you need to match the invoice. Make sure you select the correct lines from the correct PO's.

When the lines are added and you have saved, check if there are any other differences. When there is no more price difference, the **variance status** is passed.

When you approve the workflow, the invoice will not go to a 2^nd^ responsible because the issue was not a real price difference.

**[The quantity of the invoice is higher than what is received.]{.underline}**

1st responsible: Start the procedure for **CN For Quantity Difference**.

# Procedures for credit note

**[Credit note for price difference:]{.underline}**

Go to the PO to generate a product receipt for the price difference.

- Add a positive line for **99115000001: CN For Price Difference**

> Add the quantity (of items with wrong price) and unit price (difference between accepted PO price and not accepted invoice price)

- Add a negative line for **99115000001: CN For Price Difference** identical to the positive one.

- **Save** and **Confirm** the PO

- Generate the **product receipt** only for the positive line! You need it to post the initial wrong invoice.

- Later, you will need the negative line to post the credit note.

Go back to the Vendor invoice matching and add the extra delivery note.

Click on **the + sign** next to the product receipt to select the added credit note line in the PO.

Now the line is added, and you have saved, there is no more price difference, and the **variance status** is passed.

When you approve the workflow, the invoice will not go to a 2^nd^ responsible because you are waiting for a CN so there is no price difference to approve.

**[Credit note for quantity difference:]{.underline}**

Go to the PO to generate a product receipt for the quantity difference.

- Add a positive line for **99115000002: CN For Quantity Difference**

> Add the quantity (of items not received) and unit price.

- Add a negative line for **99115000002: CN For Quantity Difference** identical to the positive one.

- **Save** and **Confirm** the PO

- Generate the **product receipt** only for the positive line! You need it to post the initial wrong invoice.

- Later, you will need the negative line to post the credit note.

Go back to the Vendor invoice matching and add the extra delivery note.

Click on **the + sign** next to the product receipt to select the added credit note line in the PO.

Now the line is added, and you have saved, there is no more price difference, and the **variance status** is passed.

When you approve the workflow, the invoice will not go to a 2^nd^ responsible because you are waiting for a CN so there is no price difference to approve.
