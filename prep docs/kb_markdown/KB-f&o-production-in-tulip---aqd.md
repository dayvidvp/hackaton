# KB — F&O Production in Tulip   AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production in Tulip - AQD.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[1 General apps [1](#general-apps)](#general-apps)

[1.1 Overview screen [1](#overview-screen)](#overview-screen)

[1.2 Production order - Details [2](#production-order---details)](#production-order---details)

[**Production order info** [2](#production-order-info)](#production-order-info)

[**Material request** [3](#material-request)](#material-request)

[**Register produced goods** [7](#register-produced-goods)](#register-produced-goods)

[2 Production In Tulip - Zabo app [10](#production-in-tulip---zabo-app)](#production-in-tulip---zabo-app)

[2.1 Overview screen [10](#overview-screen-1)](#overview-screen-1)

[2.2 ZABO Details [10](#zabo-details)](#zabo-details)

[**PICK TUBE** [10](#pick-tube)](#pick-tube)

[**ZABO 1 & ZABO 2** [11](#zabo-1-zabo-2)](#zabo-1-zabo-2)

# General apps

## Overview screen

After logging in released production orders are shown In the overview list In Tulip

- Sorting In the overview screen Is based on **scheduled date + time**. This means that the production that has to be done first will be at the top of the list

- At the top of the overview screen it is shown which user is currently logged in. This Is Important to know on which printer labels will be printed![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.268055555555556in" height="1.4701388888888889in"}

<!-- -->

- At some stations multiple kind of productions can be done. These are divided by the boxes on the top right

See the example below:

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="1.3756944444444446in"}

- A production order Is shown In green when all the needed picking has been done and the production can be started. (Column Picked = Yes in that case)

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.3in"}

## Production order - Details

By selecting a production order and clicking the green details button at the bottom right, the selected production order can be processed.

### **Production order info**

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="5.013999343832021in" height="2.799751749781277in"}

- Files list:

Documents and drawings that are uploaded through Raptor In Dynamics can be retrieved via the files list

- Production parameters:

> The relevant production parameters are shown In the little table. If you want to access all parameters this can be done through \'View all\'

- Quality validation

> ![A screenshot of a computer screen AI-generated content may be incorrect.](media/image6.png){width="2.285770997375328in" height="2.0670155293088364in"}An **optional** quality validation can be done at the SLAT1 & SLAT2 stations. The \'quality validation\' button turns green when the validation Is considered OK by the machine operator. This can be done by badging or clicking \'Submit\'.
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="5.325234033245844in" height="3.296264216972878in"}

### **Material request**

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="4.845904418197725in" height="2.6930041557305335in"}

- Show barcode:

> The pickkey can be retrieved by the \'Show barcode\' button. This barcode can then be scanned to start the picking with the scanner.
>
> In case not all picking work has been created for some reason, the error below Is shown. The error mentions what Item causes the problem.
>
> ![A screenshot of a computer error AI-generated content may be incorrect.](media/image9.png){width="3.3960214348206472in" height="1.9516021434820647in"}
>
> *Remark: Please check what location the mentioned Item Is on. Often this error Is shown due to the Item being on an OUT location that does not allow picking.*
>
> [List of OUT locations where picking Is not allowed:]{.underline}

- ASM.C1.OUT

- ASM.C2.OUT

- ASM.L.OUT

- ASM.M1.OUT

- ASM.M2.OUT

- FIN.OUT

- LASC.C.OUT

<!-- -->

- Register serial number:

> Sometimes a serial number has to be entered. For these Items the button \'Register serialnumber\' becomes available. The entered serial number Is afterwards shown
>
> This functionality Is available for the following stations:

- ZABO CONSTRUCTION

- END ASSEMBLY

> A check Is done when finishing the order. When a mandatory serial number hasn't been entered, an error Is shown.
>
> ![A screenshot of a computer error AI-generated content may be incorrect.](media/image10.png){width="2.5930107174103236in" height="1.6185487751531058in"}

- Change picking:

> Sometimes extra material Is needed to execute a production. This can be done by the functionality called \'change picking\'
>
> There are 2 possibilities:

- Extra quantity Is needed for an **existing** BOM component

1.  Select the line of the Item for which you want to create extra work. The Item number should now appear in the \'Product ID\' box

2.  Pick a quantity by means of typing or using the + button

3.  Click \'Adjust quantity\'

4.  Work Is automatically created and the extra quantity can now be picked

- Extra quantity Is needed for a **new** BOM component

  1.  Get the green Tulip scanner ready

  2.  Scan the label of the Item you want to add. The Item number should now appear In the \'Product ID\' box

> *Remark: Important Is that you scan the label with a barcode as shown below. Other barcodes will not be recognized by Tulip*
>
> ![A close-up of a qr code AI-generated content may be incorrect.](media/image11.png){width="4.440548993875765in" height="2.0638265529308835in"}

3.  Pick a quantity by means of typing or using the + button

4.  Click \'Adjust quantity\'

5.  Work Is automatically created and the extra quantity can now be picked

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="3.1770833333333335in"}

*Remark: The functionality Is only available for production orders that have status = \'Started\'*

The button **Generate all pickings** can be used to release the complete production again. This Is useful when slats just got moved to a pickable location for example. This way, It Is not necessary to contact someone at a desk to release the production order again.

- Declare remains:

It Is possible not all components were used during the production. The consumption can in those cases be adapted via **Declare remains**

*Remark: These actions are only possible when the status of the production order Is equal to \'Started\'*

There are 2 options:

- Declare complete license plate(s)

> At the top half of the screen license plates are shown that were used to bring the picked components to the PRODIN location. Default, all components are consumed.
>
> To change this, select a license plates at the left. This license plate Is then filled In the white box and can now be handled
>
> Click \'Full\' \--\> None of the Items on this license plate will be consumed (status = Full)
>
> Click \'Empty\' \--\> The Items on this license plate will be consumed (status = Empty)
>
> After the production Is finished, the components can be put back Into stock with the scanner through the same license plate
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="6.268055555555556in" height="3.2083333333333335in"}

- Declare specific Items

> At the bottom half of the screen, specific Items can be declared
>
> ![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="5.397240813648294in" height="2.7512412510936133in"}

1.  Select the Item you do not want to consume. This Item Is then filled In In the grey box as shown above

2.  Click \'Adjust Product\'

3.  There are 2 options now

    a.  Rest for warehouse: Quantity Is not used for this production, but can be put back Into stock after the production was finished

    b.  Scrap: The quantity of this Item cannot be consumed and Is not usable anymore for other productions either

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="2.609775809273841in" height="1.9745330271216097in"}

*Remark: Via \'Reset All\' the action can be undone (In case of a mistake for example)*

*Remark: In case **of rest for warehouse** The not-consumed Item Is put on a new license plate after production Is finished. This matters when putting this Item back Into stock. This new license plate Is shown In Tulip In the first column at the bottom half of the \'Declare remains\' screen*

*Remark: In case of **scrap** the Item Is put on the Inventory status called scrap after production. This will have to be taken out of stock by someone In dynamics*

### **Register produced goods**

After the picking Is completely done, the production can be started and finished products can be registered

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png){width="4.828120078740158in" height="2.6874004811898513in"}

[Steps:]{.underline}

1.  Start order

    a.  This can only be done after all the picking has been completely done (all material lines are green)

> For some stations, an extra production parameter confirmation Is needed before starting

- SLATS1 & SLATS2

  1.  Sawing length

  2.  The number of needed mats

  3.  Batch number

  4.  Cap color

- ZABO

  1.  Tube dimension

  2.  Sawing length

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image17.png){width="6.601899606299213in" height="2.898662510936133in"}

2.  All done:

    a.  Enter how many license plates you want to put the produced good(s) on

    b.  Enter the quantity that you produced

> [Only relevant for the following apps:]{.underline}

- Assembly slats In box (R-A-BOX & R-A-SLATS)

- Assembly sets (R-A-SETS)

- ![](media/image18.png){width="3.017361111111111in" height="2.326388888888889in"}Assembly construction (R-A-FIN & R-A-LASC & R-A-MTS)

  a.  A label Is now printed per license plate

3.  Finish order:

    a.  The picked Items are now consumed and the production order disappears from the list

[Quantity:]{.underline}

- Remaining: Quantity that still has to be produced

- Total quantity: Total quantity that has to be produced for this production order

# Production In Tulip - Zabo app

In theory, three ZABO production orders can be In process at the same time. One tube Is being drilled, one Is being sawn and one Is being picked. To have a better overview of these actions, a separate station has been created for these production orders.

## Overview screen

In general, the overview screen has the same functionalities as the other apps. Check part 1.1 where these are explained.

The difference with the other apps Is an extra button called \'ZABO details\'

![A screenshot of a computer AI-generated content may be incorrect.](media/image19.png){width="6.268055555555556in" height="3.504166666666667in"}

## ZABO Details

When navigating to ZABO details through the new button the released and active production orders can be processed.

### **PICK TUBE**

- Scroll buttons:

> Only one of the **released** productions Is shown at the left-hand side of the screen. It Is possible to scroll between released production orders In order of **scheduled date and time**, however
>
> Example below:
>
> 14: There are 14 released production orders In total
>
> 2: Right, now the released production order with the second oldest scheduled date and time Is shown
>
> ![](media/image20.png){width="5.698494094488189in" height="2.93132217847769in"}

- Pick key:

To start picking the tube of the current production order the pickkey barcode can be scanned

In case not all work has been created, the error below Is shown. The error mentions what Item causes the problem

![A screenshot of a computer error AI-generated content may be incorrect.](media/image21.png){width="3.38499343832021in" height="1.9476727909011373in"}

- Material request:

The tube to be picked Is shown In the middle of the screen.

When AllPicked = Yes and the line becomes green, the picking has been executed and production can be started.

*Remark: A refresh with the refresh button might be necessary before these changes are showing*

### **ZABO 1 & ZABO 2**

- Starting production order(s):

1.  After the tube has been picked, the production order can be started by clicking **Start order**

    a.  An extra confirmation regarding the production parameters Is necessary

2.  The production order moves to ZABO 1 \--\> Sawing can start

    a.  Status = Started

    b.  The relevant production parameters are shown

![](media/image22.png){width="6.639364610673666in" height="3.349106517935258in"}

3.  The next released production order In the list Is now shown In **pick tube**. This order can now easily be picked while order 1 Is being sawn

4.  After the tube has been picked, the second production order can be started as well by clicking **start order** again

5.  2 orders with status = Started

    a.  The order at ZABO 1 moves to ZABO 2 \--\> Drilling can start for this order

    b.  The order that just got picked and started moves to ZABO 1 \--\> Sawing can start

![A screenshot of a computer AI-generated content may be incorrect.](media/image23.png){width="6.268055555555556in" height="3.479861111111111in"}

6.  The next released production order In the list now shown In **pick tube**. This order can now easily be picked while order 1 Is being drilled and order 2 Is being sawn

> *Remark: The \'Start order\' button Is greyed out at this point since only 2 orders can be processed at the same time*

Using the method described above, **three** orders can be processed at the same time while also having an overview of what Is being processed and which order Is currently at what step In this process

- Finish order

  1.  When the order at ZABO 2 Is done drilling, click **finish order**. The production disappears from ZABO 2 and a label Is printed. Now another order can be started again

Repeat all the steps to keep processing 3 orders at the same time
