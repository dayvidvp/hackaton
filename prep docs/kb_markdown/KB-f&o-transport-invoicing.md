# KB — F&O Transport invoicing

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Transport invoicing.docx`
**Conversiedatum:** 2026-04-24

---

# invoice from transport company for SO\'s only

- Create a PO with the transport company as account.

- Add a line for **99101000002: Purchased Transport For Sales**.

- Add the unit price and **Save.**

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.

- Write the PO number on the invoice and send it to the KOFAX email address.

# invoice from transport company for pO\'s only

- Create a PO with the transport company as account.

- Add a line for **99101000003: Purchased Transport For Purchasing** for each different transport.

- Add the unit price(s) and **Save.**

- You must link each transport line to the corresponding PO from the vendor (for the transport matrix calculations):

  - Select the line and click on **Transport related orders**.

  - Select the vendor account.

  - Select the load of the goods received with this transport and click on +.

> (TIP: if you go to a PO of goods, you can find the load in which they were received in the load lines)

- Select the load line at the bottom and click on OK.

<!-- -->

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.

- Write the PO number on the invoice and send it to the KOFAX email address.

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.268055555555556in" height="3.3152777777777778in"}

# invoice from transport company for SO\'s and PO\'s

- Create a PO with the transport company as account.

- Add a line for **99101000002: Purchased Transport For Sales** for the total amount of transport cost related to sales.

- Add the unit price.

- Add a line for **99101000003: Purchased Transport For Purchasing** for each different transport related to purchasing.

- Add the unit price(s) and **Save.**

- You must link each transport line **99101000003** to the corresponding PO from the vendor (for the transport matrix calculations):

  - Select the line and click on **Transport related orders**.

  - Select the vendor account.

  - Select the load of the goods received with this transport and click on +.

> (TIP: if you go to a PO of goods, you can find the load in which they were received in the load lines)

- Select the load line at the bottom and click on OK.

<!-- -->

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.

- Write the PO number on the invoice and send it to the KOFAX email address.

# Transport cost together with invoice from vendor

The invoice will be sent to KOFAX to be processed in the matching flow.

Because the transport cost is not in the PO there will be a difference and the first approver will have to fix this.

- Go to the PO.

- Add a line for **99101000003 : Purchased Transport For Purchasing.**

- Add the unit price and **Save.**

<!-- -->

- Even when the line is in the same PO, you must link it. (for the transport matrix calculations):

  - Select the line and click on **Transport related orders**.

  - Select the vendor account.

  - Select the load of the goods received with this transport and click on +.

  - Select the load line at the bottom and click on OK.

- Via **Purchase - Actions - Confirm** the PO.

- Via **Receive - Generate the product receipt**.
