# KB — F&O Moving load lines

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Moving load lines.docx`
**Conversiedatum:** 2026-04-24

---

Because of various reasons load lines might need to be moved from one load to another. Different scenarios might require different optimal methods to do this. Below these scenarios are summed up. The last part mentions what to do with transport lines in each of these scenarios.

- **[Only one order has not been picked and won\'t be ready]{.underline}**

> In this case, the preferred method Is to move the unpicked lines to a new or existing load.
>
> Loads \--\> Actions \--\> Transfer non-picked load lines
>
> ![](media/image2.png){width="7.350568678915136in" height="3.092590769903762in"}

![A screenshot of a computer Description automatically generated](media/image3.png){width="7.2756944444444445in" height="2.3041666666666667in"}Then you get the following drop-down menu where you can choose an existing load to transfer the lines to. If you don\'t pick any load and you press OK, the lines will be transferred to a new load.

- **[Multiple orders have not yet been picked and none of them will be ready in time (but there are lines which are done already in the load)]{.underline}**

1.  All non-picked lines can be transferred to the same new/existing load

> This requires the same steps as the scenario above

2.  Transfer non-picked lines to different loads

> If you want to move the lines to different loads this won\'t work. In that case, you will have to delete the lines from the load and add them again to another load.
>
> Be careful. If you already clicked the button \'release to warehouse\' before, then you will have to cancel the work first in the following way.
>
> Loads \--\> Related Information \--\> Work

![](media/image4.png){width="6.36994094488189in" height="1.1340168416447944in"}

> In the following screen, select the lines of which you want to cancel the work and click
>
> Work \--\> Cancel work

![](media/image5.png){width="6.796337489063867in" height="2.0729352580927385in"}

Now you can select and delete the lines from the load and add them again on another load

![A screenshot of a computer Description automatically generated](media/image6.png){width="6.268055555555556in" height="1.0645833333333334in"}

- **[Multiple orders have not yet been picked, but only one of these orders won\'t be ready in time]{.underline}**

> When there are multiple orders that are not picked yet, but only one will not be ready in time, you cannot use the button \'transfer non-picked load lines\' since this will move all of the lines, Including the ones that will be picked on time. In this case, the best option Is to cancel the work and delete the lines as in option 2 of the scenario above.

- **[Multiple orders on the load and none of them will be ready in time]{.underline}**

In this case, there\'s the option to just change the date of the load if all the lines will be shipped together at a later moment. Another option is to add all the lines to an existing load and then the current load will disappear.

- **[Picked lines are on the wrong load and need to be moved to another load]{.underline}**

> It Is also possible to move picked lines to a new or existing load. Navigate to \'Outbound load planning workbench\' and go the tab Loads and select the load of which you want to transfer the picked lines.
>
> Via Supply and demand \--\> Add \--\> License plate to new load
>
> OR via Supply and demand \--\> Add \--\> License plate to existing load (In this case you also have to pick a new load on the bottom of the screen)
>
> **Remark:** When you move the last license plate to a new or existing load, and your current load has a transport line, this transport line will move along with the last license plate to the new load. This way, transport does not have to be moved manually.

![A screenshot of a computer Description automatically generated](media/image7.png){width="6.268055555555556in" height="3.18125in"}

You get the following pop-up screen and here you need to choose which license plate(s) you want to move. Select those lines and click OK.

![A screenshot of a computer Description automatically generated](media/image8.png){width="6.268055555555556in" height="0.947826990376203in"}

- **[Transport lines]{.underline}**

> Be careful, when the lines you want to transfer include a transport line, a different approach exists for picked and non-picked load lines.

- **[Non-picked load lines]{.underline}**

After release to warehouse is executed, transport lines need to be moved manually:

1)  Select the transport line

2)  ![](media/image9.png){width="7.802083333333333in" height="2.438888888888889in"}Via Reduce picked quantity

3)  You get to the screen below, fill In NEG In the field \'Move to location\', fill in 1 at \'Inventory quantity to unpick\' and click OK.

![](media/image10.png){width="7.610416666666667in" height="1.43125in"}

> Now the transport line will be gone from the load and needs to be added again from to the new load.

- **[Picked load lines]{.underline}**

Transport will move automatically to a new/existing load along with the last transferred license plate.
