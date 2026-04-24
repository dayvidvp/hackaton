# KB — F&O Sales invoicing   Verkoopfacturatie AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales invoicing - Verkoopfacturatie AQD.docx`
**Conversiedatum:** 2026-04-24

---

Basisprincipes voor Aquadeck:

- Elk nieuw sales order is automatisch geblokkeerd voor facturatie via de knop **Block invoice**.

  - De sales person die het order behandelt moet de order vrijgeven voor facturatie.

  - Orders die manueel gefactureerd moeten worden vanwege toegevoegde service artikelen zoals kortingen of werk moeten geblokkeerd blijven.

- Elke dag om 16u loopt een batch voor facturatie. Alle zendnota\'s van de dag ervoor worden dan gefactureerd indien de documentvalidatie positief is.

  - Voorwaardes voor positieve documentvalidatie?

    - **Block invoice** knop in het sales order staat op NO.

    - Kostprijs is ingevuld of speciaal artikel waarbij kostprijs 0 mag zijn.

    - Verkoopprijs is ingevuld of gratis.

    - Mark-up is ok en goedgekeurd of indien niet ok, manueel goedgekeurd.

- Dagelijks moet iemand controleren of de facturatie correct verloopt. In de menu **Make invoices** zouden enkel mogen packing slips staan die 1 dag oud zijn of die intentioneel geblokkeerd worden.

1.  Ga naar **Make invoices.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="2.606009405074366in" height="2.106894138232721in"}

2.  Sorteer de packing slips chronologisch volgens de **Ship date**.

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="1.791796806649169in" height="2.003923884514436in"}

3.  Indien niet alle lijnen een groen vinkje hebben \> Selecteer alle packing slips via het knopje bovenaan links. En ga dan naar **Lines**.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="1.9754101049868766in" height="1.6309798775153106in"}

4.  Selecteer alle lijnen via het knopje bovenaan links en klik op \"Document validation\". Alle orders die nu positief gevalideerd zijn voor facturatie krijgen een groen vinkje. Alle orders waar minstens 1 probleem mee is krijgen een rood kruisje.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="1.9530468066491689in" height="1.8153641732283465in"}

5.  Je kan nu zien in de lijnen wat het probleem is/zou kunnen zijn. Klik op het SO nummer om het probleem op te lossen.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.9118055555555555in"}

[Voorbeeld PS2500106:]{.underline} Prijzen zijn ingevuld en markup is ok en approved dus alles lijkt ok. Enige optie is dat **Block invoice** nog steeds aan staat. Bij doorklikken naar SO blijkt het een order met extra korting te zijn. Zie verder in manual bij **[Sales orders met administratieve artikelen]{.underline}** hoe dit op te lossen.

*Het is mogelijk dat de Block invoice opzettelijk aanstaat omdat er effectief geen factuur geboekt mag worden. Zet dit dus niet zomaar af zonder te checken met de verantwoordelijke sales persoon.*

[Voorbeeld PS2500120:]{.underline} Markup is veel te koog en is niet ok en niet goedgekeurd. Indien kost of verkoopprijs verkeerd moet die aangepast worden in de SO, indien prijzen oké zijn moet de uitzonderlijke markup goedgekeurd worden. In dit geval is de kostprijs foutief en moet die manueel aangepast worden. Daarna klik je op SAVE en zal het systeem opnieuw bekijken of de markup oké is of niet.

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="5.448565179352581in" height="3.4661712598425196in"}

Na aanpassen van kostprijs + SAVE.

![A screenshot of a computer screen AI-generated content may be incorrect.](media/image9.png){width="2.4784514435695537in" height="1.1552110673665792in"}

6.  Als de problemen opgelost zijn in de sales orders ga je terug naar **Make invoices** en laat je de **Document validation** nog eens lopen. Als alles groen in kan je deze laten staan voor batchfacturatie.

7.  Indien je manueel de factuur wil genereren (in plaats van deze te laten meegaan in de batch) selecteer dan de gewenste packing slip(s) in de overview en klik dan op **Make invoices.** De eerste keer moet je ervoor zorgen dat je printerinstellingen aangezet worden. (Use print management).

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="6.268055555555556in" height="2.203472222222222in"}

**[Sales orders met administratieve artikelen]{.underline}** (bvb Extra korting) worden niet op packing slip gezet en moeten dus manueel vanuit het sales order gefactureerd worden. Zodra alle lijnen correct zijn toegevoegd zet je **Block invoice** op **No** en klik dan op **Invoice, Generate Invoice.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="6.268055555555556in" height="2.2847222222222223in"}

- Zorg ervoor dat je de **Quantity** dan aanpast naar \"All\" en in **Lines delete** je eventueel de lijnen die je niet wil factureren.

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="4.313194444444444in"}

**[Prijzen refreshen in sales order]{.underline}**

Kostprijs refreshen:

Indien de kostprijs ingevuld is maar foutief lijkt, verwijder dan eerst de huidige kostprijs (EDIT mode via potloodje). Vervolgens kan je via **Update line** klikken op **Refresh cost price**.

Klik dan op **SAVE** zodat de markup validatie kan werken.

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="6.268055555555556in" height="3.546527777777778in"}

Verkoopprijs refreshen:

Indien de verkoopprijs ontbreekt of fout lijkt, selecteer dan de lijn en klik op **Refresh prices**. Pas de referentiedatum aan indien nodig en klik op OK.

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="5.935602580927384in" height="3.2518897637795274in"}
