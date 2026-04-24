# KB — F&O Reservations & RAC   AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Reservations & RAC - AQD.docx`
**Conversiedatum:** 2026-04-24

---

## Batch reservation setup (specific for slats)

- Batch tracking dimension - set on the raw slats

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="2.461038932633421in" height="1.3136811023622048in"}

- Min. available batch er Issue (= MAB)

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="2.5584416010498687in" height="1.1479833770778654in"}

## Reservation allocation center = RAC

The reservation allocation center can be used to get an overview of the reservations of the selected Item and change these If necessary

You can navigate to the reservation allocation center by selecting the correct line and clicking the \'Reservation allocation center\' button. The function Is available on the following places:

- On the sales line

![](media/image4.png){width="6.268055555555556in" height="0.6590277777777778in"}

- On the form sales line \--\> Inventory \--\> reservations

- On the form production order \--\> manage costs \--\> cost transactions \--\> Inventory transactions

- On the form production order \--\> Order details \--\> BOM

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="3.3098807961504813in" height="1.6314720034995625in"}

- On the on-hand list \--\> Transactions

# OVerview tab

At the top an overview of the on-hand and reservation is shown. So, In the example below 6pcs are In stock and all of these are reserved. 11pcs are on order by customers and 5 are ordered from a vendor. That makes a total available of -6 pcs (= Physical inventory - physical reserved - On order + Ordered in total).

![](media/image6.png){width="6.368005249343832in" height="0.5474825021872266in"}

In the example below It Is a batch controlled Item.

![](media/image7.png){width="6.268055555555556in" height="0.7041666666666667in"}

# Issue tab

In the middle all the records are shown in order of their sequence number. This number shows the sequence In which reservations were made. Lower sequence numbers are reserved first.

## Change priority via edit allocation

It Is possible change the priority of the reservations with the function \'Edit allocation\'. This will reassign the sequence number. In some cases new sequence numbers will be created (ex. 0.5 or 2.5) to change the priority.

In the example below, there Is stock reserved for another customer. In case the selected order needs to leave earlier for example, It Is possible to change the priority of the reservations.

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.02384842519685in" height="1.125in"}

The orange checkmark shows the line that will be moved. The line you select (In green here) Is the one you compare with. So, In the following example If you pick \'Allocate before\', the line with the orange checkmark will move In front of the selected line. Another option is to choose \'Switch allocation\' and then the two lines will switch places.

![A screenshot of a computer Description automatically generated](media/image9.png){width="6.715277777777778in" height="1.9527777777777777in"}TIP: Sometimes you need to go out of the RAC and go back In for the changes to be visible.

For example If we choose for the option \'Switch allocation\' It looks like this.

Then just click OK and the reservations will have changed priority

![A screenshot of a computer Description automatically generated](media/image10.png){width="7.659722222222222in" height="2.6977898075240594in"}

**[Modify batch preference]{.underline}** Is available for exceptions In which you manually need to \"override\" the system proposal. There are NO checks or limits by the system on this functionality. Think before you act!

![](media/image11.png){width="6.268055555555556in" height="0.5381944444444444in"}

Issue tab \--\> Select the line for which you want to change the batch

Overview tab \--\> Select the batch you want to choose for the line you selected in the issue tab

## Allocate reservation

Via functions \--\> Allocate reservation

This function recalculates the reservations for the selected Item.

TIP: Sometimes you need to go out of the RAC and go back In for the changes to be visible.

## Reservation type

There are three types of reservations which are shown In the column \'Reservation type\' In the RAC:

1.  **[Hard reservation (Icon:]{.underline}** ![](media/image12.png){width="0.15240923009623797in" height="0.1587587489063867in"}**[) = MANUAL reservation]{.underline}**

- These type of reservations need to be added manually

  - On the sales line via Inventory \--\> Maintain reservation \--\> Reserve lot

> ![A yellow note on a white background Description automatically generated](media/image13.png){width="0.6034722222222222in" height="0.4388888888888889in"}
>
> ![A screenshot of a computer Description automatically generated](media/image14.png){width="4.692563429571304in" height="0.5938320209973753in"}

When you click on the Icon, you see what already happened to the reserved quantity:

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="2.975579615048119in" height="1.043711723534558in"}

- In case there Is sufficient available on-hand the quantity will move from \'On order\' to \'Reserved physical\'

![A screenshot of a computer screen Description automatically generated](media/image16.png){width="2.8416382327209098in" height="1.2271948818897638in"}

- Manual Intervention Is needed to delete these reservations

> ***Procedure to take away a reservation:***
>
> 1\. On the sales line that has the reservation of the item, on the setup tab, change the reservation parameter to \'manual\'
>
> ![A screenshot of a computer Description automatically generated](media/image17.png){width="5.686111111111111in" height="2.59375in"}
>
> ![A screenshot of a computer Description automatically generated](media/image18.png){width="6.268055555555556in" height="1.3631944444444444in"}2. After that, it is possible to take away the reservation via Inventory \--\> Maintain Reservation
>
> 3\. In the following screen, you can then lower the reservation quantity under reservation.
>
> ![A screenshot of a computer Description automatically generated](media/image19.png){width="6.268055555555556in" height="2.165277777777778in"}
>
> 4\. Change the reservation parameter on the sales line to \'Automatic\' again If you want the line to be reserved automatically again

2.  **[Shielded reservation (Icon:]{.underline}** ![](media/image20.png){width="0.13907370953630796in" height="0.1451213910761155in"}**[)]{.underline}**

- These type of reservations are added automatically

- Manual Intervention Is needed to delete the reservation

- If you click on the Icon you can see the details of the reservation. (ex. load nr)

3.  **[Open reservation (No Icon)]{.underline}**

- These type of reservations are automatically added and deleted

# Receipt tab

At the bottom of the reservation allocation center, It Is possible to see what quantity of the Item has been ordered and the expected delivery date. Be careful, this date Is not a confirmed delivery date, so deviations are possible. The physical on-hand line shows what\'s already received from which vendor and how many are already reserved of those.

![A screenshot of a computer Description automatically generated](media/image21.png){width="6.268055555555556in" height="1.1402777777777777in"}
