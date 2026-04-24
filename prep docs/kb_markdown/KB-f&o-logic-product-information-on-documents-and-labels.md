# KB — F&O logic product information on documents and labels

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O logic product information on documents and labels.docx`
**Conversiedatum:** 2026-04-24

---

The following document will give an overview of what is printed on which documents and labels. To notice any differences easier, the same example will be used throughout this document. An overview of the example's product information can be found below:

#### Product name:

![A screenshot of a computer Description automatically generated](media/image1.png){width="6.268055555555556in" height="1.4284722222222221in"}

*[Remark]{.underline}: The product name also equals the en-us translation. If that translation is changed, the product name is also changed*

*For example:*

![A screenshot of a phone Description automatically generated](media/image2.png){width="6.268055555555556in" height="2.5243055555555554in"}

![A screenshot of a product Description automatically generated](media/image3.png){width="4.6045395888014in" height="1.4365583989501312in"}

#### Product [variant]{.underline} name:

![A screenshot of a computer Description automatically generated](media/image4.png){width="6.268055555555556in" height="1.4090277777777778in"}

*[Remark]{.underline}: The product variant name also equals the en-us translation for that variant. If that translation is changed, the product name is also changed*

#### Product translation in French:

![A screenshot of a computer Description automatically generated](media/image5.png){width="5.310346675415573in" height="2.404540682414698in"}

#### Product [variant]{.underline} translation in French (does not exist in this case) :

![A screenshot of a computer Description automatically generated](media/image6.png){width="5.651628390201225in" height="2.585998468941382in"}

#### Product [variant]{.underline} external item description (vend):

![A screenshot of a computer Description automatically generated](media/image7.png){width="6.268055555555556in" height="1.0118055555555556in"}

#### Product [variant]{.underline} external item description (cust):

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.268055555555556in" height="0.9604166666666667in"}

# Documents

## Sales

The following logic applies to [all]{.underline} sales documents:

- Product

  - If an External item description (cust) exists for the related customer 🡪 External item number + External item text is printed on the document

> If not

- If a product name translation exists for the customer's language 🡪 Product name translated text is printed on the document

> If not

- Product name is printed (en-us)

<!-- -->

- Product variant (configuration)

  - If an External item description (cust) exists for the related customer for this [variant]{.underline} 🡪 External item number + External item text of the variant is printed on the document

> If not

- If a product name translation or a product variant name translation exists for the customer's language 🡪 Product (variant) name translated text is printed on the document

> If not

- Product name + Product variant name is printed (en-us)

*Product variant External item number + External item text*

**Example Quotation:**

*Product name translation + Product variant name (en-us)*

![A screenshot of a computer Description automatically generated](media/image9.png){width="3.8879997812773404in" height="1.7963987314085739in"}

![A screenshot of a computer Description automatically generated](media/image10.png){width="3.9055555555555554in" height="1.8555555555555556in"}

*Product name (en-us) + Product variant name (en-us)*

![A screenshot of a computer Description automatically generated](media/image11.png){width="4.406804461942257in" height="1.6388888888888888in"}

![A screenshot of a computer Description automatically generated](media/image12.png){width="3.5759995625546805in" height="1.7056463254593175in"}![A screenshot of a computer Description automatically generated](media/image13.png){width="3.8in" height="1.8875in"}

*Product variant External item number + External item text*

*Product name translation + Product variant name (en-us)*

**Example Confirmation:**

*Product name (en-us) + Product variant name (en-us)*

![A screenshot of a computer screen Description automatically generated](media/image14.png){width="5.2340277777777775in" height="1.6in"}

*Product name translation + Product variant name (en-us)*

*Product variant External item number + External item text*

**Example Packing slip**

![A screenshot of a computer Description automatically generated](media/image15.png){width="3.84in" height="1.643624234470691in"}![A screenshot of a computer Description automatically generated](media/image16.png){width="3.843979658792651in" height="1.6320002187226597in"}

*Product name (en-us) + Product variant name (en-us)*

![A screenshot of a computer screen Description automatically generated](media/image17.png){width="5.58400043744532in" height="1.6648567366579177in"}

*Product variant External item number + External item text*

**Example Invoice**

![*Product name translation + Product variant name (en-us)*](media/image18.png){alt="A close-up of a receipt Description automatically generated" width="3.90042760279965in" height="1.7120002187226597in"}

![A close-up of a document Description automatically generated](media/image19.png){width="3.782638888888889in" height="1.663999343832021in"}

*Product name (en-us) + Product variant name (en-us)*

![A screenshot of a computer screen Description automatically generated](media/image20.png){width="5.673611111111111in" height="1.9184426946631672in"}

## Purchase

The following logic applies to the purchase inquiry:

- Product

  - If an External item description (vend) exists for the related vendor 🡪 External item number + External item text is printed on the document

> If not

- If a product name translation exists for the vendor's language 🡪 Product name translated text is printed on the document

> If not

- Product name is printed (en-us)

<!-- -->

- Product variant (configuration)

  - If an External item description (vend) exists for the related vendor for this variant 🡪 External item number + External item text of the variant is printed on the document

> If not

- If a product name translation or a product variant name translation exists for the vendor's language 🡪 Product (variant) name translated text is printed on the document

> If not

- Product name + Product variant name is printed (en-us)

**Example Purchase inquiry**

*Product variant External item number + External item text*

![A screenshot of a computer Description automatically generated](media/image21.png){width="5.167361111111111in" height="1.7368055555555555in"}

*Product name translation + Product variant name (en-us)*

![A screenshot of a computer Description automatically generated](media/image22.png){width="5.319444444444445in" height="1.6916666666666667in"}

*Product name (en-us) + Product variant name (en-us)*

![A screenshot of a computer Description automatically generated](media/image23.png){width="5.3680008748906385in" height="1.7889370078740157in"}

*[Remarks documents]{.underline}:*

- *For a sister company the AX3 item number and configuration is also printed on the sales and purchase documents*

- *If a translation [only]{.underline} exists for either the product or the product variant, that translation is still printed, as is the case in the examples above*

- *With a small change in setup, it is also possible to print [both]{.underline} the external item descriptions and the product name (translation)*

![*Product variant external item number + product name translation + product variant name (en-us) + poduct variant External item text*](media/image24.png){alt="A screen shot of a computer Description automatically generated" width="5.8in" height="1.853867016622922in"}

Example Confirmation:

# Labels

The following logic applies to the STOCK, MTS & INB labels:

- Product

  - Product name is printed (en-us)

- Product variant (configuration)

  - Product name + product variant name is printed (en-us)

![A close-up of a label Description automatically generated](media/image25.png){width="3.328799212598425in" height="1.5840004374453194in"}[Examples]{.underline}:

![A qr code with a black square Description automatically generated](media/image26.png){width="3.584000437445319in" height="1.6298611111111112in"}

![A close-up of a qr code Description automatically generated](media/image27.png){width="3.631078302712161in" height="1.8220002187226596in"}

The following logic applies to the PRODUCT label:

- Product

  - If an External item description (cust) exists for the related customer 🡪 External item number + External item text is printed on the label

> If not

- If a product name translation exists for the customer's language 🡪 Product name translated text is printed on the document

> If not

- Product name is printed (en-us)

<!-- -->

- Product variant (configuration)

  - If an External item description (cust) exists for the related customer for this variant 🡪 External item number + External item text of the variant is printed on the label

> If not

- If a product name translation or a product variant name translation exists for the customer's language 🡪 Product (variant) name translated text is printed on the label

> If not

- Product name + Product variant name is printed (en-us)

![*Product name translation + Product variant name (en-us)*](media/image28.png){alt="A close-up of a label Description automatically generated" width="3.6975503062117236in" height="1.7280008748906386in"}

**Example PRODUCT label**

![*Product variant External item number + External item text*](media/image29.png){alt="A white background with black text Description automatically generated" width="3.7359995625546807in" height="1.664767060367454in"}

*Product name (en-us) + Product variant name (en-us)*

![A close-up of a label Description automatically generated](media/image30.png){width="4.36in" height="1.7843832020997374in"}

*[Remarks labels:]{.underline}*

- For the PRODUCT label, the external item description is also printed separately at the moment. This means that the external item number is printed twice in case an external item description exists

- *If a translation only exists for either the product or the product variant, that translation is still printed*

- *With a small change in setup, it is also possible to print [both]{.underline} the external item description and the product name (translation)*

Example PRODUCT label:

*Product variant External item number + Product name translation + Product variant name (en-us) + Product variant external item text*

![A close-up of a document Description automatically generated](media/image31.png){width="4.463999343832021in" height="1.914484908136483in"}
