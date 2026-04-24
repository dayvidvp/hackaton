# KB — F&O Credit management

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Credit management.docx`
**Conversiedatum:** 2026-04-24

---

- **[General set-up ​]{.underline}**

<!-- -->

- 'Check credit limit on sales order' in Credit and collection parameters = NO​

- 'Mandatory credit limit' on customer = No or Yes (this will determine if blocking rules based on credit limits will work or not)

- Stopped:

  -----------------------------------------------------------------
  **AX3**    No         All        All but picking list   Invoice
  ---------- ---------- ---------- ---------------------- ---------
  **D365**   No         All        All                    Invoice

  -----------------------------------------------------------------

- **[Payment terms in use per type​ (Examples Micron)]{.underline}**

<!-- -->

- PP = Prepayment 'transport' customer (Ex Send pro forma, payment before sending goods)​

- 000D = Prepayment 'collection' customer (Ex Payment in the office - Payconiq idea) ​

- 000Z = Sister companies​

- 008D = Customers that get 1 open invoice​

- 014D + 030D + 030E + 030E15 + 045D + 045E + 060D + 060E + 060E15​

- 090D + 090 E​

<!-- -->

- **[Blocking rules​ (Examples Micron)]{.underline}**

<!-- -->

- PP = Prepayment 'transport' customer (Send pro forma, payment before sending goods)​

- All customers get 15 "extra" overdue days on top of the payment terms. When the customer exceeds the 15 days, sales order will be blocked. The order hold can be removed. ​

> Exceptions: ​

- Customer 0126511 Soft Water Solutions BV gets 30 days extra. ​

- 4 Customers with payment terms of 90D do not get any extra days. They must be added 1 by 1 in the blocking rules. ​

Every sales order that complies with one of these rules gets an order hold. **[The SO can be released manually. ​]{.underline}**

> ​

1.  ​Create sales order​.

2.  Confirm sales order and get notification of credit management order hold. At this moment, the order cannot be added to a load! ​

3.  PP? Send pro forma invoice to customer​.

> Overdue? Send payment reminder to customer.

4.  If you want to add to a load, you have to release the order hold via 'Credit management' -- 'Credit order hold list'.

5.  Select the credit hold and select the release reason "APPROVE" and click on Release.​

6.  ​When you release the credit hold, the system automatically reconfirms the sales order, you can choose if you send it to the customer.​

7.  Now you can add the order lines to a load following the normal sales process.

8.  There will be no more automatic check if the due amount was paid. If you choose to release the credit hold before the actual payment, you need to follow up manually.
