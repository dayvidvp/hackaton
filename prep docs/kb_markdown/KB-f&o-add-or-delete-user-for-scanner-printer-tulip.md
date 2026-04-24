# KB — F&O Add or delete user for scanner printer Tulip

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Add or delete user for scanner-printer-Tulip.docx`
**Conversiedatum:** 2026-04-24

---

Go to **Warehouse management \> Setup \> Worker**.

Usually a Work user is created for people who have a D365 account and need a scanner account.

Operators who don\'t have a D365 account but need a scanner account are usually entered as users (eg. \'Arthur Hayes\' in the screenshot) under the umbrella of a Work user like the Warehouse manager (eg. \'Don Heaver\' in the screenshot).

Click the \'New\' or \'Delete\' button to add/delete scanner users. Fill in all columns. You\'ll be asked to enter a password. Don't forget to also do the settings under the \'Work\' tab.

Click \'Save\' afterwards.

When you want to replace a certain user with a new one, it\'s best to first create the new user and then follow the steps in chapter *\'Add/delete a user for the label printer\'*. Then afterwards, you can delete the old user.

![](media/image2.png){width="6.268055555555556in" height="4.170138888888889in"}

Add/delete a user for the label printer

*All existing printers (both labelprinter and regular A4 printers) connected directly to D365 are visible in **Organization administration \> Setup \> Network printers**. Contact IT Support if you want to add a new label printer to the network.*

*Be sure to put the column \'Active\' to \'Yes\' for the labelprinter.*

Go to **Warehouse management \> Setup \> Document routing.**

For every Work order type, multiple document routings can exist.

In the screenshot, we have 2 unique document routings for Work order type \'Purchase orders\'. These are called \'INB Blocked\' and \'INB\'.

These two document routings are copied a number of times, each time they are connected to a different scanner user. The document routing in my screenshot is connected to scanner user \'atu\'.

Every document routing can be connected to 1 or multiple labelprinters, those are visible under the \'Document routing printers\' tab.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="2.321527777777778in"}

When you want to add a new user, you need to click the \'New\' button to create new document routings for the extra user. Create as many as necessary and connect them all to the new scanner user. Add the correct label printer in the tab \'Document routing printers\'. Make sure all parameters are set exactly like they are on an existing document routing. Even click the \'Edit query\' button on top of the screen to set the query correct for the new document routing.

In the example in my screenshot, I would need to create 2 new document routings (\'INB Blocked\' and \'INB\') for work order type \'Purchase orders\'. Then I would have to see if I need to create new document routings for all other work order types.

Replacing an old user with a new user is much easier. Just look up all existing document routings connected to the old user and replace the user-ID in the \'Mobile device user ID\' field.

If you want to delete an existing user, just look up and delete all his document routings.

Add/delete a user for Tulip

Go to **Production control \> Setup \> Work places**.

Click the \'New\' button to create a new work place. Be sure to connect the new work place to the right User ID and Printer name. Other columns can be copied from existing work places.

If you want the new user to have a badge, then click on the \'Edit\' button and place your cursor in the empty \'Tag\' field. Now scan a badge using the RFID reader. The badge ID will be read in and appear in the \'Tag\' column. You can then click the \'Save\' button.

To delete existing work places, just select them and click on the \'Delete\' button.

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.9277777777777778in"}
