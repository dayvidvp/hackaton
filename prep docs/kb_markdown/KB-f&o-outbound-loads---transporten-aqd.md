# KB — F&O Outbound loads   Transporten AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Outbound loads - Transporten AQD.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[1.1 Collection/Afhaal door klant [1](#collectionafhaal-door-klant)](#collectionafhaal-door-klant)

[1.2 DPD [3](#dpd)](#dpd)

[1.3 Tinie Manders [4](#tinie-manders)](#tinie-manders)

[1.4 Export with customs [6](#export-with-customs)](#export-with-customs)

[1.5 Zendingen verplaatsen uit een load [6](#zendingen-verplaatsen-uit-een-load)](#zendingen-verplaatsen-uit-een-load)

## Collection/Afhaal door klant

**[In sales order]{.underline}**

Pas mode of delivery aan naar COL-STD.

Indien alle goederen op stock kan je ze toevoegen aan een load om te picken en klaar te zetten.

- Via **Warehouse \> Outbound load planning workbench.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.268055555555556in" height="3.879861111111111in"}

- Selecteer de lijnen die je wil toevoegen aan de load.

- Bekijk de loads en ga na of er reeds een afhaal lading is voor die specifieke klant op dezelfde gewenste dag van afhaal of niet.

- Indien niet: klik op **Supply and demand \> To new load.**

> *Na aanmaken van de load klik je door op het load nummer en vul je de cut-off date aan.*

- Indien wél: selecteer de load en klik op **Supply and demand \> To existing load.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="3.357638888888889in"}

**[Ga naar Active outbound loads (warehouse)]{.underline}**

Selecteer jouw zending. Deze is momenteel nog \"Incomplete\" en je kan nog geen picking list printen.

Klik op **Release to warehouse** om werk aan te maken voor deze zending. De highest deliverystatus wijzigt hierdoor naar \"In progress\". (Je moet een grote refresh doen om dit te zien)

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.4895833333333333in"}

Print **Outbound picking list**.

Indien dringend: bezorg aan magazijnier

Indien niet dringend: leg in bakje

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="6.268055555555556in" height="1.476388888888889in"}

Als de picking gedaan is bezorgt de magazijnier de picklist terug naar kantoor. In het systeem zie je de highest deliverystatus nu ook op \"Picked\".

Indien de klant onmiddellijk de goederen meeneemt (balie order), kan de magazijnier onmiddellijk \"Load to truck\" doen na de picking.

Indien nog niet zeker is wanneer de klant zal ophalen print je een \"Outbound load list\" en die leg je klaar aan de balie voor wanneer de klant komt opdagen. Deze kan de magazijnier dan gebruiken om \"Load to truck\" te doen.

De packing list kan je ook al printen en klaarleggen als document om te ondertekenen en om mee te geven aan de klant.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="6.268055555555556in" height="2.2993055555555557in"}

De highest deliverystatus verandert hierdoor naar \"Loaded\".

Nu moet de packing slip gemaakt worden. Deze wordt gemaild naar de klant.

## DPD

**[In sales order]{.underline}**

Pas mode of delivery aan naar DPD-STD.

Voeg transportartikel toe.

Indien alle goederen op stock kan je ze toevoegen aan een load om te picken en te versturen.

- Via **Warehouse \> Outbound load planning workbench**

- Selecteer de lijnen die je wil toevoegen aan de load.

- Bekijk de loads en ga na of er reeds een DPD lading is voor de gewenste dag van vertrek of niet.

- Indien niet: klik op **Supply and demand \> To new load.**

> *Na aanmaken van de load klik je door op het load nummer en vul je de cut-off date aan.*

- Indien wél: selecteer de load en klik op **Supply and demand \> To existing load.**

**[Boek transport bij DPD en print label]{.underline}**

**[Ga naar Active outbound loads (warehouse)]{.underline}**

Selecteer jouw zending. Deze is momenteel nog \"Incomplete\" en je kan nog geen picking list printen.

Klik op **Release to warehouse** om werk aan te maken voor deze zending. De highest deliverystatus wijzigt hierdoor naar \"In progress\". (Je moet een grote refresh doen om dit te zien)

Print **Outbound picking list**. Bevestig aan DPD label.

Indien dringend: bezorg aan magazijnier

Indien niet dringend: leg in bakje

Na picken en verpakken worden ook afmetingen en gewicht toegevoegd via de scanner. Daarna print de magazijnier de packing list en hangt deze samen met DPD label aan zending. In het systeem zie je de highest deliverystatus nu ook op \"Weighed\".

De magazijnier zal \"Load to truck\" doen en het pakje op de kar voor DPD leggen. De highest deliverystatus verandert hierdoor naar \"Loaded\".

Alle zendingen in de load moeten \"loaded\" zijn om de packing slip te kunnen maken.

Deze wordt gemaild naar de klanten.

## Tinie Manders

**[In sales order]{.underline}**

Pas mode of delivery aan naar TIN-STD.

Voeg transportartikel toe indien rechtstreekse klant van AQD die transport moet betalen.

Indien alle goederen op stock kan je ze toevoegen aan een load om te picken en te versturen.

- Via **Warehouse \> Outbound load planning workbench**

- Selecteer de lijnen die je wil toevoegen aan de load.

- Bekijk de loads en ga na of er reeds een TIN-STD lading is voor de gewenste dag van vertrek of niet.

- Indien niet: klik op **Supply and demand \> To new load.**

> *Na aanmaken van de load klik je door op het load nummer en vul je de cut-off date aan.*

- Indien wél: selecteer de load en klik op **Supply and demand \> To existing load.**

Afdekkingen kunnen pas worden toegevoegd aan een load na productie. Dit gebeurt vanuit de SALES LINE AVAILABILITY.

Indien je extra goederen toevoegd in een Sales order met een afdekking dan moet je het vinkje \"complete order\" aanzetten indien je wil dat deze samen verstuurd worden met de afdekking.

**[Ga naar Active outbound loads (warehouse)]{.underline}**

Selecteer jouw zending met stockgoederen. Deze is momenteel nog \"Incomplete\" en je kan nog geen picking list printen.

Klik op **Release to warehouse** om werk aan te maken voor deze zending. De highest deliverystatus wijzigt hierdoor naar \"In progress\". (Je moet een grote refresh doen om dit te zien)

Print **Outbound picking list**.

Indien dringend: bezorg aan magazijnier

Indien niet dringend: leg in bakje

Na picken en verpakken worden ook afmetingen en gewicht toegevoegd via de scanner. Daarna print de magazijnier de packing list en hangt deze aan zending. In het systeem zie je de highest deliverystatus nu ook op \"Weighed\".

**[Ga naar Sales line availability]{.underline}**

Selecteer de query met **Mode of delivery TIN-STD** en klik **OK.**

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="3.3849792213473315in" height="1.5488549868766404in"}

Bekijk welke lijnen er allemaal in de lijst komen.

In de kolom **Load ID** kan je zien welke reeds toegevoegd zijn aan ene load. Filter in deze kolom op \"Does not contain: L\". Nu zie je enkel nog lijnen die niet aan een load toegevoegd zijn.

In de kolom **Load advice** filter je op \"Is exactly: ok\". Nu Zie je nog alle lijnen die klaar zijn om toe te voegen aan een load. (productie is uitgevoerd, goederen zijn op stok, betalingsstatus is ok)

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="1.460566491688539in" height="1.733834208223972in"}

Controleer nog eens in de kolom van de **delivery name** of dit effectief klanten zijn die via Manders beleverd worden. (Bij twijfel over afhaal moet het HIVE order gecontroleerd worden)

Selecteer alle gewenste lijnen en voeg ze toe via **Warehouse - Outbound load planning workbench.**

**[Ga naar de load door te klikken op het loadnummer.]{.underline}**

Klik op **\"Release to warehouse\".**

Print de **outbound picking list.** Als hier nog iets op staat dan moet er nog picking werk gebeuren. Pas als alle picking werk gedaan is kan je de volgende stap doen.

Print de **outbound load list**. Hierop staan alle afgewerkte license plates.

**[Maak \"Het Manders lijstje\"]{.underline}**

**STAP 1**: Ga naar Active outbound loads (warehouse), selecteer de speciale view, selecteer de gewenste load, exporteer naar excel, download file. Open de excel [Transport Aquadeck D365.xlsx](https://polletgroupintranet.sharepoint.com/:x:/r/sites/Aquadeck2.0/Shared%20Documents/General/Transport/Transport%20Aquadeck%20D365.xlsx?d=wc0425b2cd3734d85b377965ecd5b3f4e&csf=1&web=1&e=XAUkx8) en plak het resultaat In het eerste tabblad.

**STAP 2**: Ga in de load en open de license plate summary, selecteer de speciale view, exporteer naar excel, download file. Open de excel [Transport Aquadeck D365.xlsx](https://polletgroupintranet.sharepoint.com/:x:/r/sites/Aquadeck2.0/Shared%20Documents/General/Transport/Transport%20Aquadeck%20D365.xlsx?d=wc0425b2cd3734d85b377965ecd5b3f4e&csf=1&web=1&e=XAUkx8) en plak het resultaat in het 2de tabblad. Sorteer nu op customer name kolom. (Sommige zendingen kunnen bestaan uit meerdere LPs)

**STAP 3**: Ga in de excel naar het derde tabblad. Kopieer dit resultaat nu naar een nieuwe sheet die je de datum van vandaag geeft. Van daaruit kan je nu filteren en knippen en plakken voor de verschillende lijstjes.

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="1.7506944444444446in"}

Bezorg de outbound list list en het excel overzichtje aan de magazijnier.

De magazijnier zal \"Load to truck\" doen zodra de goederen in de vrachtwagen geladen worden. De highest deliverystatus verandert hierdoor naar \"Loaded\".

Alle zendingen in de load moeten \"loaded\" zijn om de packing slip te kunnen maken.

Deze wordt gemaild naar de klanten.

## Export with customs

**[In sales order]{.underline}**

Customs = Yes

Carrier service = EXP

Indien alle goederen op stock kan je ze toevoegen aan een load om te picken en te versturen.

- Via **Warehouse \> Outbound load planning workbench**

- Selecteer de lijnen die je wil toevoegen aan de load.

- Bekijk de loads en ga na of er reeds een bestaande lading is voor de gewenste dag van vertrek of niet.

- Indien niet: klik op **Supply and demand \> To new load.**

> *Na aanmaken van de load klik je door op het load nummer en vul je de cut-off date aan.*

- Indien wél: selecteer de load en klik op **Supply and demand \> To existing load.**

Afdekkingen kunnen pas worden toegevoegd aan een load na productie. Dit gebeurt vanuit de SALES LINE AVAILABILITY.

Indien je extra goederen toevoegd in een Sales order met een afdekking dan moet je het vinkje \"complete order\" aanzetten indien je wil dat deze samen verstuurd worden met de afdekking.

**[Ga naar Active outbound loads (warehouse)]{.underline}**

Selecteer jouw zending met stockgoederen. Deze is momenteel nog \"Incomplete\" en je kan nog geen picking list printen.

Klik op **Release to warehouse** om werk aan te maken voor deze zending. De highest deliverystatus wijzigt hierdoor naar \"In progress\". (Je moet een grote refresh doen om dit te zien)

Print **Outbound picking list**.

Indien dringend: bezorg aan magazijnier

Indien niet dringend: leg in bakje

Na picken en verpakken worden ook afmetingen en gewicht toegevoegd via de scanner. Daarna print de magazijnier de packing list en hangt deze aan zending. In het systeem zie je de highest deliverystatus nu ook op \"Weighed\".

**[Ga naar Sales line availability]{.underline}**

Kies een query (bijvoorbeeld op basis van \'customer name\' en klik **OK**.

Bekijk welke lijnen er allemaal in de lijst komen.

In de kolom **Load ID** kan je zien welke reeds toegevoegd zijn aan ene load. Filter in deze kolom op \"Does not contain: L\". Nu zie je enkel nog lijnen die niet aan een load toegevoegd zijn.

In de kolom **Load advice** filter je op \"Is exactly: ok\". Nu Zie je nog alle lijnen die klaar zijn om toe te voegen aan een load. (productie is uitgevoerd, goederen zijn op stok, betalingsstatus is ok).

Selecteer alle gewenste lijnen en voeg ze toe via **Warehouse - Outbound load planning workbench.**

**[Ga naar de load door te klikken op het loadnummer.]{.underline}**

Klik op **\"Release to warehouse\".**

Print de **outbound picking list.** Als hier nog iets op staat dan moet er nog picking werk gebeuren. Pas als alle picking werk gedaan is kan je de volgende stap doen.

Export moet gefactureerd worden voor het vertrekt. In D365 moet er echter eerst geladen en een packing slip gegenereerd worden voor er gefactureerd kan worden.

**[Ga naar de warehouse app]{.underline}**

Log in op de warehouse app. Navigeer naar **Outbound** **-** **Load in truck**

Vul het **Load ID** In. Nu kunnen alle license plates \'geladen\' worden. Ga naar de **license plate summary**. Kopieer de license plates en plak die in de warehouse app. *Let op, begin met multipallet license plates indien deze aanwezig zijn*

Het vinkje in de kolom **\'Loaded\'** moet overal geactiveerd zijn voor er verder kan gegaan worden. in de warehouse app kan je ook zien hoeveel license plates er al geladen werden.

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="4.334022309711286in" height="2.6399792213473314in"}

Daarna kan de packing slip gegenereerd worden. Ga naar **Ship and receive - Generate \'Packing slip\'**. Een mail moet op dit moment niet verstuurd worden naar de klant.

Load status = Shipped op dit moment, deze status verandert niet meer!

Nu kan er gefactureerd worden. na het factureren zal het vinkje \'loaded\' weer uitstaan. Nu kan er effectief geladen worden door het magazijn wanneer de vrachtwagen komt.

## Zendingen verplaatsen uit een load

Gepickte license plates verzetten

Ga naar **Outbound load planning workbench**

Selecteer de load vanuit welke je een LP wil verzetten. Indien dit naar een nieuwe load is kies je voor \"License plate to new load\".

Indien dit naar een bestaande load is selecteer je onderaan ook de bestaand load en kies je voor \"License plate to existing load\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="5.639270559930009in" height="3.5018963254593176in"}

Selecteer de LP(s) die je wil verzetten en klik ok.

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="2.1512248468941384in" height="1.6660553368328959in"}

De nieuwe load is nu beschikbaar:

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="6.268055555555556in" height="2.308333333333333in"}

Transportlijn terugdraaien in load:

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="6.268055555555556in" height="1.8555555555555556in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="6.268055555555556in" height="1.0277777777777777in"}

Refresh in load

Nu kan je de lijnen deleten uit de load of verplaatsen naar een andere load.
