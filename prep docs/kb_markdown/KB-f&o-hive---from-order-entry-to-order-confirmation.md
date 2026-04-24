# KB — F&O Hive   From Order Entry to Order Confirmation

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Hive - From Order Entry to Order Confirmation.docx`
**Conversiedatum:** 2026-04-24

---

# Add a new distributor in Hive

Important remarks before starting:

1\) Never create a subdistributor this way

2\) Ensure that this is a direct customer of Aquadeck

Log in to D365FO

Go to **Sales and marketing \> Customers \> All customers**

Search the customer you want to create as a distributor in Hive

Open the customer detailed view

Go to the tab **Hive CPQ**

Enable \'Hive CPQ Distributor\'

This automatically synchronizes the customer as a distributor in Hive.

The information of the distributor now has to be completed in Hive. Follow the instructions given in [Complete the (sub)distributor company information](#complete-the-subdistributor-company-information) & Pricing.

Important: the company information in the tab \'Info\' is prefilled by D365FO. 1 element has to be checked carefully: if the format of the website is not \'https://... \' customer details will not be saved.

WRONG - Save is greyed out:

![Afbeelding met tekst, schermopname, Lettertype, nummer Door AI gegenereerde inhoud is mogelijk onjuist.](media/image1.png){width="2.9777176290463694in" height="1.280738188976378in"}

Corrected:

![Afbeelding met tekst, schermopname, Lettertype, nummer Door AI gegenereerde inhoud is mogelijk onjuist.](media/image2.png){width="2.8260301837270343in" height="1.4227602799650043in"}

# Add new subdistributor in Hive

Important remarks before starting:

1\) Never create a distributor this way

2\) Always check that the subdistributor does not exist yet

Log in to Hive

Go to **Address Books \> Companies**

Click \'+ Add\' to create a new company

Fill In the company name

If the company buys trough a distributor (PPG, Niveko, ...):

- click \'Is sub-distributor\'

- fill In the distributor company

Click \'Add\'

![Afbeelding met tekst, nummer, software, Lettertype Door AI gegenereerde inhoud is mogelijk onjuist.](media/image3.png){width="6.268055555555556in" height="2.4243055555555557in"}

A new screen Is opened where the company Information has to be completed.

# Complete the (sub)distributor company information

We\'ll only use the tabs \'Info\' and \'Default addresses\'.

![Afbeelding met schermopname, tekst, nummer, lijn Door AI gegenereerde inhoud is mogelijk onjuist.](media/image4.png){width="6.268055555555556in" height="3.4458333333333333in"}

## Tab info

Fill In the following fields - field names between brackets are optional:

- Company name

- (Description)

- Address line 1

- (Address line 2)

- City

- Postal code

  - IMPORTANT: apply formatting convention D365FO.

> For Netherlands: \'9999 AA\' example: 1276 AN

- Country

- VAT number

  - Remark: the Invoice Information of D365FO will be leading In sales orders and Invoices

- Phone

  - IMPORTANT: Use iso format with country code example +31 495 430 317

- (Website)

  - IMPORTANT: If you add a website, always use the format **https://**www.website.com

- Preferred language

## Tab default addresses

Be careful; this tab has 2 sub-tabs of Its own: \'Invoice\' and \'Delivery\'. Both have to be completed.

![](media/image5.png){width="6.268055555555556in" height="0.66875in"}

### Subtab Invoice

The data In the tab \'Invoice\' will [not]{.underline} be used in D365FO. It is however displayed in the hive order summary and the data is required to place orders in Hive and should be correct to avoid confusion.

Fill In the following fields - field names between brackets are optional:

- Company

  - Identical to \'company name\' in info

- VAT number

  - Identical to \'VAT number\' in info

- Email

  - Identical to \'email\' in info

  - IMPORTANT 1 email address only

- Address line 1

  - Identical to \'Address line 1\' in info

- (Address line 2)

  - Identical to \'Address line 2\' in info

- Country

- ZIP / Postal code

  - Identical to \'Postal code\' In Info

  - IMPORTANT: apply formatting convention D365FO

- City

  - Identical to \'Postal code\' In Info

- Contact person

  - Identical to \'company name\' in info

- Contact phone

  - Identical to \'Phone\' in info

  - IMPORTANT: Use iso format with country code example +31 495 430 317. Only spaces are allowed to separate numbers

IMPORTANT: disable the \'Distributors editing rights\'

![Afbeelding met tekst, schermopname, Lettertype Door AI gegenereerde inhoud is mogelijk onjuist.](media/image6.png){width="3.475300743657043in" height="1.3917869641294838in"}

### Subtab Delivery

The data in the tab \'Delivery\' will be copied into the D365FO delivery address. Insert the information of the [default delivery address]{.underline} in this tab.

Fill In the following fields - field names between brackets are optional:

- Company

  - Enter the delivery name of the default delivery address

- Address line 1

- (Address line 2)

- Country

- ZIP / Postal code

  - IMPORTANT: apply formatting convention D365FO

- City

  - Identical to \'Postal code\' In Info

- Contact person

  - IMPORTANT: will be the delivery name in D365FO ! Fill in company name (and person if known)

- Contact phone

  - IMPORTANT: Use iso format with country code example +31 495 430 317

- Email

  - IMPORTANT 1 email address only

IMPORTANT: set the \'Distributors editing rights\'

![Afbeelding met tekst, schermopname, Lettertype Door AI gegenereerde inhoud is mogelijk onjuist.](media/image7.png){width="3.8253313648293963in" height="1.408455818022747in"}

## Other tabs

Can be Ignored

# Pricing

For the time being, the pricing groups and discounts have to be set by a hive administrator. send following information to PIT in order to complete the pricing information.

- (Sub) distributor link:

![Afbeelding met schermopname, tekst, software, Multimediasoftware Door AI gegenereerde inhoud is mogelijk onjuist.](media/image8.png){width="6.268055555555556in" height="2.301388888888889in"}

- Distributor

  - (only for subdistributors)

<!-- -->

- Currency

  - EUR

  - GBP

- Price group

  - PGC01, ....

- Line discount group

  - D40, .....

Example:

- Subdistributor <https://app.hivecpq.com/#/companies/d11c5a1323ed4b789238e168b803803b?companyA=MyAquadeck>

- Distributor: PPG

- Currency: EUR

- Price group: PGC01

- Line discount group: D40
