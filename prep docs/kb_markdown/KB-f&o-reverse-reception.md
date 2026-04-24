# KB — F&O Reverse reception

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Reverse reception.docx`
**Conversiedatum:** 2026-04-24

---

*\*Only possible if the purchase order lines of the load are not invoiced yet.*

- **[Reception = done, putaway = not done, \'Product receipt\' not posted]{.underline}**

<!-- -->

- Via **Load details \> Loads \> Work**

- Select all work ID-lines that need to be reversed and press **Work \> Cancel work**

- By cancelling the work, you will basically undo the receipt and allow for the item to be registered again or removed from the load.

<!-- -->

- **[Reception = done, putaway = done, \'Product receipt\' not posted]{.underline}**

<!-- -->

- Search the original license plate number(s) that was created for the item on DOCK-IN (via **Load details \> Loads \> Work**)

- Use an adjustment journal (via **Inventory management \> Inventory adjustment**) to book away the goods from the put-location and to book them onto their original DOCK-IN license plate(s).

> (If you can\'t post the adjustment journal because the items are already reserved by a SO, then check Appendix A in [F&O End of year count.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20End%20of%20year%20count.docx?d=w4390fafce7fc4a40a16a5b641c743002&csf=1&web=1&e=aGp7gt) to switch the reservations.)

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.339130577427822in" height="2.279727690288714in"}

- Undo the original registration of the goods (via **Purchase order \> Update line \> Registration**)

> Select all registered lines and click on **Add registration line.** At the bottom of the screen, new lines are created with a negative quantity. Select these lines and press the **Confirm registration** button. The registration lines will be gone now.
>
> (If you can\'t confirm the registration because the items are reserved by a SO, then check
>
> Appendix B in [F&O End of year count.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20End%20of%20year%20count.docx?d=w4390fafce7fc4a40a16a5b641c743002&csf=1&web=1&e=aGp7gt) to remove the reservation.)

![A screenshot of a computer Description automatically generated](media/image3.png){width="5.036941163604549in" height="2.49168416447944in"}

- At this point you have reversed the reception and you can continue with registering the goods again or removing the line from the load.

> If you receive the error message *\'Load line cannot be deleted because there is work associated to it\' or \'Can not post product receipt, load line Is not entirely registered\'* when trying to remove the line from the load or trying to post the product receipt, go to **Warehouse management \> Periodic tasks \> Clean up \> Cancel work**. Fill in the work ID, select all lines and click OK. Then click Yes to confirm that you want to cancel the work. The Work status has now been changed from \'Closed\' to \'Cancelled\' and you can remove it from the load.
>
> \- It might be possible that you have to refresh the page before deleting the load line.
>
> \- Not everyone has access to the \"Cancel work\", you might have to contact IT Support or an IT analyst or BPO to do this.

- **[\'Product receipt\' posted]{.underline}**

<!-- -->

- Find the Product receipt that need to be reversed in the Product receipt journal. Via **Accounts payable \> Inquiries and reports \> Product receipt**. Check the preview. All the PO-lines from the journal will have to be reversed.

- Go to your Inbound load. Via **Load details \> Loads \> Work**, check if there are any open work lines (meaning putaway is not done yet) from the journal in here. Select those open work ID-lines and cancel them via **Work \> Cancel work**

- List the load lines from your product receipt that have already been put in the warehouse. They will have to be booked back on their original DOCK-IN license plate(s).

> Do this through an adjustment journal (via **Inventory management \> Inventory adjustment**).
>
> (If you can\'t post the adjustment journal because the items are already reserved by a SO, then check Appendix A in [F&O End of year count.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20End%20of%20year%20count.docx?d=w4390fafce7fc4a40a16a5b641c743002&csf=1&web=1&e=aGp7gt) to switch the reservations.)

![A screenshot of a computer Description automatically generated](media/image2.png){width="6.431769466316711in" height="2.313043525809274in"}

- Go back to the Product receipt journal. Select the product receipt that you want to reverse and click \'Cancel\'. A warning will appear to tell you that all lines from the product receipt will be reversed. Click \'Yes\'.

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="2.5597222222222222in"}

- Go to the **Load details** page of the load or go to the **All loads** page and select the load there. Then click Action Pane **Ship and receive \> Reverse \> Cancel product receipt** and then click **Ship and receive \> Reverse \> Reverse shipment confirmation**.

> It is possible that you only have to click the second button. Depends on if the first button is greyed out or not.
>
> It is also possible that you don\'t have these buttons in your View. In that case you have to unhide them first (via Action Pane **Options \> Personalize \> Personalize this page**).

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="4.991666666666666in" height="3.2750557742782154in"}

- Now the product receipt is reversed and all lines can be received again. You can make the necessary changes before receiving the lines again.

> If you don\'t want to receive the loadlines again and instead you want to remove them from your load, just select the loadlines and click \'Delete\'. If you receive an error about work that is associated to the lines, you\'ll first have to cancel that work via **Warehouse management \> Periodic tasks \> Clean up \> Cancel work**.
>
> (If you don\'t have access to this button, contact a BPO or BA or IT Support and ask them to do it for you)
