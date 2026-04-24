# KB — F&O HIVE   Sync masterdata to Hive

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O HIVE - Sync masterdata to Hive.docx`
**Conversiedatum:** 2026-04-24

---

Masterdata which can be synced to hive

- Customers

- Products

- Prices

[Customers]{.underline}

1.  Enable the customer as Hive CPQ Distributor

- Via **Customers (details) \> Hive CPQ \> Hive CPQ Distributor**

- The customer will be synced to Hive automatically

- Masterdata will be synced upon creation and manual synchronization

  - Info:

    - Company name

    - Address line 1

    - City

    - Postal code

    - Country

    - VAT number

    - Phone

    - Preferred language

[Products]{.underline}

1.  Enable the released product as Hive CPQ Distributor

- Via **Release product details \> Hive CPQ \> Sync record with Hive**

- NO automatic sync

2.  Sync product to hive

    - Via **Hive CPQ \> Periodic tasks \> Synchronize components**

      - Parameters: none

      - Records to include: restrict sync by item number as much as possible

[Prices]{.underline}

1.  Sync prices to hive

    - Via **Hive CPQ \> Periodic tasks \> Synchronize price agreements**

    - **REMARK:** Hive has no logic to use [active]{.underline} prices

    - **IMPORTANT:** adapt query to include only active prices

      - **Records to include**

      - Add filter on From date and to date

        1.  From date: (lessThanDate(1))

        2.  To date: (greaterThanDate(-1))

        3.  To date: 01/01/1900

> ![](media/image2.png){width="6.268055555555556in" height="2.428472222222222in"}

- Restrict the sync a much as possible by adding a filter on the item relation
