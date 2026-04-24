# KB — F&O Purchase invoicing process

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Purchase invoicing process.docx`
**Conversiedatum:** 2026-04-24

---

# Digitize & import invoice

- **Scan invoice & Email to KOFAX (= OCR).**

- KOFAX recognizes information.

- OCR-responsible in Boekan validates & correct information + release.

- Invoice image is automatically saved in RAPTOR. (= Document warehouse)

- Invoice becomes visible in D365.

# Prepare, post & submit for approval

- Non PO-related:

  - The responsible in Boekan opens **Invoice journal** + Adds lines + Checks/adjusts VAT info.

  - The responsible in Boekan submits for approval flow.

  - The invoice is posted automatically (not yet payable).

- PO-related:

  - The system automatically posts the invoice on temporary account and tax code.

  - The system automatically submits the invoice for matching.

# Match & approve for payment

- Non PO-related:

  - **Via [Invoices assigned to me]{.underline} \> Approval flow: Local responsible approves invoice.**

  - Boekan can pay the invoice.

- PO-related:

  - **Via [Invoices assigned to me]{.underline} \> Approval flow:**

    - **Perfect match? No approval needed.**

    - **Differences? The local responsible does the necessary changes and approves invoice. In some cases, the group responsible has to approve the invoice afterwards.**

  - VAT-check: VAT = 0? Responsible in Boekan checks/adjusts VAT info.

  - Boekan can pay the invoice & the PO status will change to invoiced.

**[Remarks:]{.underline}**

- A PO-number on the invoice is essential for KOFAX to recognize it as a PO-invoice!

- Each **vendor type** has a specific **approval flow** that is copied to all of the vendors within the group. On a vendor level it is possible to make changes to the **Approval levels** on the tab **Responsibilities**.

**[How to process matching differences:]{.underline}**

- Quantity differences:​

> Are the correct product receipts linked to the invoice?
>
> Have the goods actually been received in D365? Is there a product receipt?
>
> Is the product receipt not linked to another invoice?
>
> Are there lines missing in the PO? (Transport, Packaging, Request for CN,...)​

- Price differences:​

> Does the price need to be added or changed? (+ add reason code)​
>
> Is the cash discount calculated correctly? We need to match what is on the invoice!

**[Cash discount scenarios in detail:]{.underline}**

1.  **Cash discount code correct on vendor & cash discount calculated correctly on vendor invoice.**

  -------------------------------------------------------------
                        Vendor invoice   D365 calculation in PO
  ------------------- ---------------- ------------------------
  Nett amount                 100,00 €                 100,00 €

  Discount                          2%                       2%

  VAT amount                   20,58 €                  20,58 €

  Total amount                120,58 €                 120,58 €
  -------------------------------------------------------------

- **Automatic approval**

2.  **Cash discount code correct on vendor & cash discount [not correct]{.underline} on vendor invoice.**

  -------------------------------------------------------------
                        Vendor invoice   D365 calculation in PO
  ------------------- ---------------- ------------------------
  Nett amount                 100,00 €                 100,00 €

  Discount                          2%                       2%

  VAT amount                   21,00 €                  20,58 €

  Total amount                121,00 €                 120,58 €
  -------------------------------------------------------------

- **Matching error!**

<!-- -->

- The local responsible will have to change the **actual sales tax** to 21 € instead of 20,58 €.

- Upon payment we can still deduct the cash discount because it was added to the register booking and it is default information on the vendor.

3.  **Cash discount code not correct on vendor & cash discount calculated on vendor invoice.**

  -------------------------------------------------------------
                        Vendor invoice   D365 calculation in PO
  ------------------- ---------------- ------------------------
  Nett amount                 100,00 €                 100,00 €

  Discount                          2%                       2%

  VAT amount                   20,58 €                  21,00 €

  Total amount                120,58 €                 121,00 €
  -------------------------------------------------------------

- **Matching error!**

<!-- -->

- The local responsible needs to:

  - Navigate to the **PO** to add the **cash discount.**

  - Navigate to **pending vendor invoice** to re-link the PO to the invoice via +.

  - Verify if **actual sales tax** has changed to 20,58 € instead of 21 €.

- Upon payment we will deduct the cash discount.

- The vendor responsible needs to add a cash discount on the vendor and any existing purchase orders, to ensure easy matching for future invoices

**[Purchase invoice approval flow checklist]{.underline}**

1.  **Are there Invoices assigned to you?**

> You can see this on your HOME page.
>
> If there are, go to the menu **\"Invoices assigned to me\"**
