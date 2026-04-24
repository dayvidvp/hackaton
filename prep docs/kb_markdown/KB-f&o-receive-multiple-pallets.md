# KB — F&O Receive multiple pallets

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Receive multiple pallets.docx`
**Conversiedatum:** 2026-04-24

---

## Option 1: Default = receive 1 pallet at a time. Overrule default to receive multiple pallets at once

- **[Setup]{.underline}**

<!-- -->

- **Mobile device menu items:** Set License plate grouping policy to \"User defined\"

![A screenshot of a computer Description automatically generated](media/image2.jpeg){width="6.268055555555556in" height="2.3375in"}

- Define new **Unit sequence group**

![A screenshot of a computer Description automatically generated](media/image3.jpeg){width="6.268055555555556in" height="1.6548611111111111in"}

- Define **Unit conversion** for article

![A screenshot of a computer Description automatically generated](media/image4.jpeg){width="6.268055555555556in" height="2.0527777777777776in"}

- Define Unit sequence group ID for article in **Released product details\>Warehouse**

![A screenshot of a computer Description automatically generated](media/image5.jpeg){width="6.268055555555556in" height="1.6631944444444444in"}

- **[Reception]{.underline}**

When we receive the item with the scanner, the default reception quantity will be PCS. You need to change this to PAL in order to be able to receive multiple pallets at once.

After you have changed the unit to PAL and you have chosen the amount of pallets, you can see the unit conversion in the confirmation screen.

After confirmation, a LP number will be created for every pallet + a label will be printed for every pallet.

When receiving in pallets, make sure that the quantity on every pallet is always the same as the quantity defined in the unit conversions!

![A screenshot of a phone Description automatically generated](media/image6.jpeg){width="2.2083333333333335in" height="3.8627121609798776in"} ![A screenshot of a phone Description automatically generated](media/image7.jpeg){width="2.2032961504811897in" height="3.857622484689414in"} ![A screenshot of a phone Description automatically generated](media/image8.jpeg){width="2.175in" height="3.8452241907261593in"}

## Option 2: Default = receive multiple pallets at once. Overrule default to receive 1 pallet at a time

- **[Setup]{.underline}**

<!-- -->

- **Mobile device menu items:** Set License plate grouping policy to \"License plate grouping\"

![A screenshot of a computer Description automatically generated](media/image9.jpeg){width="6.268055555555556in" height="2.6770833333333335in"}

- Define new **Unit sequence group**

![A screenshot of a computer Description automatically generated](media/image10.jpeg){width="6.268055555555556in" height="1.6909722222222223in"}

- Define **Unit conversion** for article

![A screenshot of a computer Description automatically generated](media/image4.jpeg){width="6.268055555555556in" height="2.0527777777777776in"}

- Define Unit sequence group ID for article in **Released product details\>Warehouse**

![A screenshot of a computer Description automatically generated](media/image5.jpeg){width="6.268055555555556in" height="1.6631944444444444in"}

- **[Reception]{.underline}**

When we receive the item with the scanner, the default reception quantity will be PAL. You need to enter the amount of pallets you wish to receive and a LP number will be created for every pallet + a label will be printed for every pallet.

Just make sure that the quantity on every pallet is always the same as the quantity defined in the unit conversions!

You can always change the unit back to PCS of you want to receive separate pallets that have quantities on them that differ from the unit conversion.

![A screenshot of a phone Description automatically generated](media/image11.jpeg){width="2.1559776902887138in" height="3.8in"} ![A screenshot of a phone Description automatically generated](media/image12.jpeg){width="2.2224048556430445in" height="3.797222222222222in"} ![A screenshot of a phone Description automatically generated](media/image13.jpeg){width="2.125in" height="3.771330927384077in"}
