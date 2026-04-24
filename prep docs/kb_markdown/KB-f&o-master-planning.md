# KB — F&O Master planning

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Master planning.docx`
**Conversiedatum:** 2026-04-24

---

The Master Planning module in D365 uses solvers to generate a proposed plan to meet item demand. The proposed plan can consist of planned purchase orders or planned production orders. The Master Planner can check/approve the proposed plan and convert the planned orders into actual orders (this conversion could be automated if desired).

The Master planning is mostly done by using **Master Planning \> Workspaces \> Master planning** and **Master Planning \> Master Planning \> Planned orders**. Most Master planners will use both screens when working, but the degrees of which both are used depend on personal preferences.

# Master Planning \> Workspaces \> Master planning 

This a workspace containing useful buttons and lists, most of them connecting to a **Planned orders** page with preset filters.

![A screenshot of a computer Description automatically generated](media/image1.jpeg){width="6.268055555555556in" height="4.226388888888889in"}

- **[1. Run-info:]{.underline}**

This box shows when the master plan had its last run. There is also a button to start a new run. Some planners will only use the workspace to check this info.

When starting a new run, a pop-up screen appears where you can select for which items you want to run the solvers. One should be careful when making a selection: though it might decrease the runtime of the solver, there is also the risk that not all demand is taken into account (for example when the selected item is a BOM-component of a different item that is not in the selection). Therefore we advise against it.

![Graphical user interface, application Description automatically generated](media/image2.png){width="2.5916929133858266in" height="3.802249562554681in"}

- **[2. Master plan: Dynamic or Static:]{.underline}**

Usually, we are working in the **Static** masterplan. This plan is created automatically every night. It calculates a supply plan for every need on every item-configuration over all BOM-levels. The Static plan takes quite some time to run, that\'s why we advise to run it automatically at night and not start a run manually during the day.

There is also the **Dynamic** masterplan. This plan can be ran manually ad hoc, there is no scheduled automatic run. Usually, a Dynamic masterplan has some different settings that allow it to run faster than a Static plan (for example shorter time fence. Settings can be checked in **Master planning \> Setup \> Plans**).

The idea behind a Dynamic plan is that it should be used when you cannot wait for the next Static plan to run. For example when there is a sudden spike in demand, you could run a Dynamic plan and compare it with the existing Static plan (that has not yet taken that demand spike in account) to see whether you want to launch extra production/purchase or not.

Most of the time though, the Static plan is sufficient for us, as it runs on a nightly basis. We rarely use the Dynamic plan.

- **[3. Buttons and lists:]{.underline}**

The buttons and lists in the workspace are highly configurable. The default buttons/lists you can see in the printscreen are mostly of little use. However, the more you create custom buttons/lists, the more useful this workspace will get, to the point where most of the Master planning can be done from this screen.

For example: if you purchase from different vendors on fixed days, you could create a button for each day of the week that directs you to a selection of planned orders containing only items ordered with the vendors for that day.

So the number of times you use this workspace really depends on the effort that is put on creating custom buttons/lists that are actually useful for the planner.

# Master Planning \> Master Planning \> Planned orders

This is the page where the master planner has an overview off all the planned orders. It can be accessed directly or through the Master planning workspace.

The master planner can go through the planned orders and convert them to actual orders.

Normally some sort of grouping (e.g. by vendor) or sorting will be necessary to go through the lines in a structured way. If the masterplanner wishes to alter proposed purchase/production quantities, he can do this directly in the lines on this page.

- **[Views:]{.underline}**

It is advisable to create a number of Views with preset filters and sorting to work more efficiently.

Please be aware though that we have encountered some instances where certain views do not seem to work properly (they do not save/load the filters/sorting correctly). So when creating a new view, please doublecheck.

![A screenshot of a computer Description automatically generated](media/image3.jpeg){width="6.268055555555556in" height="2.932638888888889in"}

We recommend using **at least two different views**: one for the **planned purchase orders** and one for the **planned MTS production orders**.

Please note that no planned MTO production orders should appear in the list as there is a batch job running every night that creates those orders automatically for MTO sales lines.

However, many more views can be created and used, it depends on how the master planner prefers to work. For example: by filtering on the SO-column, one can make a view for planned purchase orders for SO\'s and one for planned purchase orders to replete the safety stock levels. You could also filter on quantities, items, vendors, dates...

- **[Requirement profile:]{.underline}**

For every planned order, you can see the demand that causes the order in the Action pane \> **View \>** **Requirement profile**.

If you open the requirement profile in a new screen through the ![](media/image4.png){width="0.3020833333333333in" height="0.28125in"}button in the upper right corner, you have the possibility to see the planned order lines and the net requirements next to each other. Each time you change the planned order line, the requirement profile will change automatically as well in the separate screen. This can be very helpful for the master planner.

![A screenshot of a computer Description automatically generated](media/image5.jpeg){width="6.268055555555556in" height="2.6145833333333335in"}

- **[Coverage group:]{.underline}**

The Coverage group of an item determines how the planned orders will be calculated.

Each coverage group has specific settings.

The Coverage code determines if planned order lines represent 1 or multiple requirements.

Coverage code \"Requirement\" will create separate planned order lines for each requirement.

Coverage code \"Period\" allows you to set a period in days and all the requirements that fall within this period will be combined in 1 planned order line.

![A screenshot of a computer Description automatically generated](media/image6.jpeg){width="4.229166666666667in" height="2.3427701224846893in"}

If you wish to change the coverage group of an item, you can do this from the Planned orders screen by going to Action Pane \> Update item data.

(don\'t change the coverage group directly in the planned order line)

![A screenshot of a computer Description automatically generated](media/image7.jpeg){width="6.268055555555556in" height="2.3201388888888888in"}

A pop-up screen will appear where you can change not only the coverage group but also other settings: minimum inventory, vendor, minimum order quantity, lead time.

Be aware of two things though:

\- Changing and saving item data will not affect the current master plan nor automatically trigger a new MRP run! But the changes will affect future master plans.

\- The \'Update item data\' button changes data on an item level, not on the configuration level. If you want to update data for just one specific configuration, you do this through Action Pane \'View\' \> \'Item data\' \> \'Default order settings\'/\'Item coverage\'.

![](media/image8.png){width="2.904248687664042in" height="3.245382764654418in"}

- **[Status:]{.underline}**

The column \'Status\' can be a useful tool when going through all planned orders.

Planned orders by default have the status \'Unprocessed\'.

When you look into a planned order but decide not to convert it to a purchase or production order, you can put the status on \'Completed\', as a signal to everyone that you have checked the line.

When you do want to convert to an actual order, you can put the status on \'Approved\'. Whenever a line is \'Approved\', it also means that the line is \"frozen\". Meaning that the line will not disappear when a new master plan has run.

Using the \'Status\' column is optional; it is not mandatory to put a line on \'Approved\' before converting it to an actual order. But we do recommend using it as a method for communication (for example: if the master planner gets interrupted a lot, he can quickly see after the interruption which lines he had handled already before he was interrupted).

![A screenshot of a computer Description automatically generated](media/image9.jpeg){width="6.268055555555556in" height="1.9256944444444444in"}

- **[Converting a planned purchase order: Firming:]{.underline}**

The actual conversion of the planned purchase orders happens by clicking the \'**Firm**\' button after a selection of planned orders was made.

![A screenshot of a computer Description automatically generated](media/image10.jpeg){width="6.268055555555556in" height="2.7270833333333333in"}

A pop-up screen will appear: make sure you **Group by vendor**!

Grouping by vendor is necessary to create only 1 PO with multiple PO-lines for the vendor instead of 1 PO per item variant.

Grouping by period, buyer group or planning priority is also possible, but this is something that most companies will never do.

Make sure that \'Update marking\' is also set to \'No\'. Our system is not properly set up to support this use of markings.

![A screenshot of a computer Description automatically generated](media/image11.jpeg){width="2.319047462817148in" height="4.333333333333333in"}

After clicking the OK-button in this pop-up screen, a new purchase order will be created and the planned order lines will have disappeared from the planned orders list.

You can see your newly created purchase orders through **Procurement and sourcing \> Purchase orders \> All purchase orders**.

In the PO-line details under Product \> Planned-order reference, you can see the indication that this PO-line was made through the masterplan.

For further processing of the purchase order(s), please consult [F&O Purchase Process.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Purchase%20Process.docx?d=w885907070dba4d2e8e9c8feeb723794c&csf=1&web=1&e=mHpTgG).

- **[Converting a planned production order: Create and estimate production order:]{.underline}**

**For MTS production, we don\'t use the \'Firm\' button** to convert planned orders into actual orders.

The reason is that the \'Firm\' button doesn\'t work when you have item variants (configurations) in your planned order selection.

Instead, we use Action Pane \> **Create and estimate production order**.

Be aware though that (in contrast to firming planned orders), the planned order will not disappear automatically from the planned orders list. A refresh of the page will be necessary for the line to disappear.

![A screenshot of a computer Description automatically generated](media/image12.jpeg){width="6.268055555555556in" height="2.9208333333333334in"}

You can see your newly created production orders through **Production control \> Production orders \> All production orders**.

In the production order header under References \> Planned-order references, you can see the indication that this production order was made through the masterplan.

For further processing of the purchase order(s), please consult [F&O Production Process.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/PG_CORP_IT/Shared%20Documents/D365/General%20user%20manuals/F%26O%20Production%20Process.docx?d=w8c84f7cb93e9464682fea5fca6b5257e&csf=1&web=1&e=4eVB80).
