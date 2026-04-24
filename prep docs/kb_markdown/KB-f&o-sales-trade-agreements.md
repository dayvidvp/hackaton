# KB — F&O Sales trade agreements

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales trade agreements.docx`
**Conversiedatum:** 2026-04-24

---

# setup & Hierarchy

![](media/image2.png){width="6.5625in" height="4.374757217847769in"}

![](media/image3.png){width="2.9791666666666665in" height="2.0708278652668417in"}

![](media/image4.png){width="6.268055555555556in" height="4.178472222222222in"}

![](media/image5.png){width="6.268055555555556in" height="3.5277777777777777in"}

Customer discount and price group are determined in AX. You can find them here in D365:

![](media/image6.png){width="3.2636701662292213in" height="0.9922933070866141in"}

![](media/image7.png){width="4.714665354330709in" height="0.9195844269466317in"}

An item can be added to a line discount group directly in D365. This is not interfaced from AX.

![](media/image8.png){width="2.894375546806649in" height="1.6052788713910762in"}

# view trade agreements

Trade agreements can be accessed from different points in D365: sales order, customer, released product...

![A screenshot of a computer Description automatically generated](media/image9.png){width="1.8125in" height="1.6472725284339458in"}You can choose to view :

- All TA

- TA specific for Sales price

- TA specific for Line discount

# Create new trade agreements

**[Single item]{.underline}**

1.  Navigate to **Trade agreement journals.**

2.  Click on **+New.**

3.  Choose the correct **Name** for your journal: SalesD (for discounts) or SalesP (for prices).

4.  Change the **Description** to something clear for you.

5.  Click on **Lines** and fill in all the necessary information.

![A screenshot of a computer Description automatically generated](media/image10.png){width="3.0289654418197727in" height="1.191165791776028in"}

+-----------------------+------------------------------------+
| **Party code type**   | **Account selection**              |
+=======================+====================================+
| Table                 | Specific customer                  |
|                       |                                    |
| Group                 | 10/IC                              |
|                       |                                    |
| All                   | All customers                      |
+-----------------------+------------------------------------+
| **Product code type** | **Item relation**                  |
+-----------------------+------------------------------------+
| Table                 | Specific item                      |
|                       |                                    |
| Group                 | Line discount group (Fleck-SP,...) |
|                       |                                    |
| All                   | All items                          |
+-----------------------+------------------------------------+

6.  Fill in the **Start date**.

7.  Set the checkbox **Find next** to \"**No\".**

8.  When you are ready you can **Validate** the journal and when there are no errors, you can **Post** the journal.

![A screenshot of a computer Description automatically generated](media/image11.png){width="6.268055555555556in" height="2.15625in"}

**[Bulk upload]{.underline}**

1.  Navigate to **Trade agreement journals.**

2.  Click on **+New.**

3.  Choose the correct **Name** for your journal: SalesD (for discounts) or SalesP (for prices).

4.  Change the **Description** to something clear for you.

5.  Click on **Lines** and fill in the information for 1 item.

![](media/image12.png){width="6.260416666666667in" height="1.2916666666666667in"}

If you have a large amount of prices/discount to upload, it is easier to use the Excel download via the Microsoft Office icon in the top right corner.

![](media/image13.png){width="6.260416666666667in" height="2.2395833333333335in"}

Because you filled in 1 item via lines, you have an example in the excel that shows where you have to put everything.

![](media/image14.png){width="1.7785279965004375in" height="1.5002099737532808in"}

The Excel file will open in your web browser. Now click on Download file.

![](media/image15.png){width="5.671274059492563in" height="2.0722200349956257in"}

Now the file will be downloaded to your PC and you can open it again. (You can close the excel in the web browser.)

![](media/image16.png){width="2.8702668416447943in" height="1.0359339457567804in"}

Click on Enable editing!

![](media/image17.png){width="4.089449912510936in" height="1.1263429571303587in"}

You will also see the line that you had already entered in D365.

Now add the other trade agreements and click on Publish.

![](media/image18.png){width="6.260416666666667in" height="3.1979166666666665in"}

Then you can go back to your journal in D365 and refresh. All the published data will appear.

Then validate and post your journal. In the popup screen just click OK.

![](media/image19.png){width="6.260416666666667in" height="2.3229166666666665in"}

# Edit existing trade agreements

When you need to make changes to an existing trade agreement, you can easily click on **Edit trade agreement.**

D365 will ask you to fill in the name of the new TA journal and immediately put in all the information that is already known.

You can then, make the necessary changes and **Post** the journal.

# Entire new setup

![](media/image20.png){width="6.268055555555556in" height="3.8270833333333334in"}
