# KB — F&O Sales order ingeven AQC

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales order ingeven AQC.docx`
**Conversiedatum:** 2026-04-24

---

Ga naar ALL SALES ORDERS.

Klik op +NEW

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="2.6779713473315834in" height="1.359199475065617in"}

Kies de klant.

Kies een leveradres uit de dropdown lijst of maak een nieuw via het + teken.

Vul de klantreferentie in.

Klik OK. Het order wordt nu geopend.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="2.7794346019247596in" height="5.092887139107612in"}

Vul je artikelen In.

Dit kan met:

- het nieuwe D365 artikelnummer (zoekt in Item number)

Je kan dit nummer eerst opzoeken in een apart tabblad \"Released products\" adhv het oude Navision nummer.

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.6611111111111112in"}

- de leveranciersreferentie (zoekt in Search name)

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="1.5569444444444445in"}

- de Product selection tool

Kies de juiste **Mode of delivery**.

COL = afhaal aan de balie

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="1.8180468066491688in" height="1.6266732283464567in"}

Voeg het transport artikel toe in geval dat Aqua.com transport regelt.

Controleer het **Load advice** van de artikelen om te weten of er voldoende beschikbare stock is.

Indien ERROR of PARTIAL dan kan je via **Reservation allocation center** de details bekijken en zien of de stock misschien voor een andere order gereserveerd is.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.2347222222222223in"}

Als je artikelen wil laten picken dan moet je de lijnen toevoegen in een load via:

**Warehouse - Outbound load planning workbench.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="4.645336832895888in" height="4.303087270341208in"}

Hier moet je de lijnen selecteren die in de load moeten.

Als je wil toevoegen aan een bestaande load dan moet je die onderaan selecteren en gebruik je de knop \"To existing load\".

Indien dit een afhaal is dan is het steeds \"To new load\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="3.546527777777778in"}

In dit voorbeeld volgen we het process voor een afhaal dus kies ik voor \"To new load\".

Van het 2de lijntje zijn slechts 9 van de 10 stuks op stock dus moeten we de hoeveelheid aanpassen van 10 naar 9 in onderstaand veld.

Je kan hier ook opmerkingen meegeven voor de load.

Daarna klik je op OK.

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="5.227051618547682in" height="7.647157699037621in"}

De load is aangemaakt en kan je nu terugvinden bij de loads onderaan in het scherm.

(het lijntje bovenaan blijft staan omdat 1 stuk niet op stock is en dus niet werd toegevoegd aan de load)

Klik op het load nummer:

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="6.268055555555556in" height="3.5701388888888888in"}

**Release to warehouse:**

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="2.6791666666666667in"}

Print de **\"Outbound picking list\"**

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="6.268055555555556in" height="1.0638888888888889in"}

Dit document Is nodig In het magazijn voor de picking met scanner.

![A close-up of a receipt AI-generated content may be incorrect.](media/image14.png){width="6.268055555555556in" height="3.5694444444444446in"}

Als ze klaar zijn ga je terug naar de load voor deze stappen:

**Confirm outbound shipment.**

Zodra dit gelukt is zal de knop voor de **\"Packing slip\"** beschikbaar komen. Hiermee kan je de zendnota maken.

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="6.268055555555556in" height="1.386111111111111in"}
