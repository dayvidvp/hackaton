# KB — F&O Production specific manuals   AQD

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Production specific manuals - AQD.docx`
**Conversiedatum:** 2026-04-24

---

# Production planning

## Daily basis

Dagelijkse taken van de productieplanning omvatten:

- maken van de uitwerkprogramma\'s

- overzicht producties aanvullen

- geschatte leverdata doorgeven naar sales

- \"releasen\" van productie orders naar de werkplaats

### Uitwerkprogramma's

HAHA kidding, over het maken van de uitwerkprogramma\'s ga ik je echt geen manual geven, dit is bedrijfsspecifieke kennis die jij veel beter beheert.

Uitwerkprogramma\'s blijven de leidende factor aan de machines. De productiemapjes - geel voor het L-gebouw en groen voor het CM-gebouw - worden nagekeken en bieden de productiemedewerkers alle nodige informatie om de producties uit te voeren.

**DOEL**: we willen alle info van de uitwerkprogramma\'s zo snel mogelijk verwerken in de hive parameters zodat deze taak te vervallen komt voor reguliere orders. Orders waarvoor een manuele uitwerking nodig is, zullen gevlagd worden.

### Overzicht producties aanvullen

Elk sales order wordt bijgehouden in een excel om een overzicht tussen de systemen te bewaren. Op termijn moet dit vervangen worden door de D365FO planning.

Excel: [Geplande orders AX3 vs Hive](https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/Geplande%20orders%20AX3%20vs%20Hive.xlsx?web=1)

#### Voorbereiding

Update 20/06/2025: De data-entiteiten in de excel \"breken\" sinds kort. Voorlopig nog geen verklaring en \"opgelost\" door de data-entiteiten in een aparte excel te zetten. 2 extra manuele stappen.

> Stap 1: open excel met de data-entiteiten [ProdplanningDataEntiteiten](https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/20250621%20ProdplanningDataEntiteiten.xlsx?web=1)
>
> De laatste data wordt automatisch opgehaald
>
> Stap 2:

- Kopieer en plak de laatste data van de **sales orders** uit de data-entiteit naar onze planningsXls

  - Open de tab \"SO Header\"

  - Kopieer de data uit de tabel

  - Plak de data in de \"Geplande orders AX3 vs Hive\" tab \"SO\"

- Kopieer en plak de data van de **productieorders** uit de data-entiteit naar onze planningsXls

  - Open de tab \"PC PWG\"

  - Kopieer de data uit de tabel

  - **Plak** de data in de \"Geplande orders AX3 vs Hive\" tab \"PC PWG\" **ALS WAARDEN**

#### Aanvullen van de xls

Nieuwe sales orders moeten aangevuld worden in de planningsxls

- Blijf in excel [Geplande orders AX3 vs Hive](https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/Geplande%20orders%20AX3%20vs%20Hive.xlsx?web=1)

- tab \'Nieuwe sales orders\'

- Vernieuw de draaitabel

  - Rechtermuisklik op de draaitabel

  - Klik \'Vernieuwen\'

> ![Afbeelding met tekst, schermopname, software, Multimediasoftware Door AI gegenereerde inhoud is mogelijk onjuist.](media/image1.png){width="2.381877734033246in" height="2.002518591426072in"}

- Kopieer de lijst van SO-nummers

- Plak de lijst onderaan in de tab \'AX3 vs Hive\' in de kolom \'So D365FO\'

- Trek de formule in kolom \'configuratie\' door naar de nieuwe lijnen

- De overige velden worden automatisch opgehaald

Vul de voorziene productie datum in in kolom A

Geef de geschatte leverdatum door geven naar sales

### Releasen van productie orders

Bij release worden de orders zichtbaar in de tulip stations. Dit kunnen we doen vanuit \'All production orders\' of vanuit de \'Production planning hub\'. Onderstaande uitleg loopt via de production planning hub.

Om het releasen te vereenvoudigen werden 2 overzichtsviews gemaakt:

1.  To release M-SLAT

    a.  Bevat alle orders van het L-gebouw die gereleased moeten worden (MAN en M-SLAT)

    b.  waarvan de Status nog scheduled is

    c.  Startdatum kleiner dan vandaag + 7 dagen

        i.  [BELANGRIJK]{.mark}: doordat Martijn lamellen geconsolideerd klaarzet aan de machine, mogen we de orders per kleur telkens maar vrijgeven [per productierun.]{.underline} Voorbeeld: zo lang Emerald 4000mm nog niet geproduceerd is, mogen de producties voor Emerald 4000mm voor volgende week NIET gereleased worden. Anders zal Martijn in zijn picking opdracht krijgen om het materiaal voor volgende week eveneens klaar te zetten

2.  To release other (14 days)

    a.  Bevat alle orders van het M-gebouw die gereleased moeten worden (geen MAN of M-SLAT)

    b.  waarvan de Status nog scheduled is

    c.  Startdatum kleiner dan vandaag + 14 dagen

Ga na wat de materiaalstatus is door de kolom \'Component reservation\' na te kijken.

- Component reservation = OK \--\> Release de productie orders (in batch)

- Component reservation = Partial of Error -\> Ga na wat er tekort is in de BOM en pas eventueel reservaties aan

#### Releasen van productie orders (detail)

- Selecteer de productieorders met status ok

- Action menu \> Production order \> Process \> Release

![](media/image2.png){width="3.4608694225721783in" height="1.3741699475065616in"}

- Om de release op de achtergrond te doen - zodat je niet hoeft te wachten: open de tab \'Run in background\'

- Activeer \'Batch processing\'

![Afbeelding met tekst, schermopname, Lettertype Door AI gegenereerde inhoud is mogelijk onjuist.](media/image3.png){width="1.6215649606299212in" height="1.3311351706036745in"}

- OK

#### Tekorten nagaan

## Weekly basis

### Planning T + 3 weken 

#### Algemeen 

Op donderdag: Maak de planning voor vandaag + 3 weken

Deze is al voorbereid door op dagelijkse basis de voorziene datum in te vullen in de planningsxls, nu gaan we deze ook verwerken in D365FO.

Stappen:

- Planningsexcel ([Geplande orders AX3 vs Hive](https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/Geplande%20orders%20AX3%20vs%20Hive.xlsx?web=1)):

  - Indien nog niet gedaan: Sorteer de xls op (Voorziene productiedatum, LamKleur, Zaagmaat)

  - Kopieer de **D365FO** sales order nummers

- D365FO:

  - ga naar de planningshub

  - Merk op: We beginnen altijd met de slatorders. open dus op de view \"Slats - planning group 1\"

  - Open de view Filter op kolom \'Top reference level\'

  - Selecteer alle lijnen

  - Open de tab sequence

  - Custom sort om op kleur en lengte te zetten

  - Eventueel: up, down om de volgorde aan te passen

  - Schedule

  - Indien van toepassing: Haal de filter weg van de \"planning type 1\" en herhaal voor de non-slat orders.

#### Detail stappenplan: Plan slat orders for one production day [scribe](https://scribehow.com/shared/Plan_slat_orders_for_one_production_day__6vwpKxHySV-s6QWhKbhsyw)

** **

1.  Planningsexcel: Sorteer op voorziene productiedatum, lamkleur en zaagmaat 

![Picture 1, Afbeelding](media/image4.jpeg){width="6.268055555555556in" height="3.4944444444444445in"} 

2.  Click \"OK\" 

![Picture 2, Afbeelding](media/image5.jpeg){width="6.268055555555556in" height="3.5in"} 

3.  Kopieer de D365FO sales orders voor de gewenste dag \
    Press \[\[Ctrl\]\] + \[\[C\]\] 

![Picture 3, Afbeelding](media/image6.jpeg){width="6.268055555555556in" height="3.5in"} 

4.  D365FO Open de productie planning hub 

![Picture 4, Afbeelding](media/image7.jpeg){width="6.268055555555556in" height="3.5in"} 

5.  We planning eerst de slats: controleer de view 

![Picture 5, Afbeelding](media/image8.jpeg){width="6.268055555555556in" height="3.5in"} 

6.  Filter op de kolom \"Top reference number\" 

![Picture 6, Afbeelding](media/image9.jpeg){width="6.268055555555556in" height="3.5in"} 

7.  Controleer de filtersetting  \"is one of\" 

![Picture 7, Afbeelding](media/image10.jpeg){width="6.268055555555556in" height="3.5in"} 

8.  Plak de gekopieerde sales orders uit onze planningsxls \
    Press \[\[Ctrl\]\] + \[\[V\]\] 

![Picture 8, Afbeelding](media/image11.jpeg){width="6.268055555555556in" height="3.5in"} 

9.  Click \"Select all rows\" 

![Picture 9, Afbeelding](media/image12.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

10. Click \"Sequence\" 

![Picture 10, Afbeelding](media/image13.jpeg){width="6.268055555555556in" height="3.5in"} 

11. Custom sort om te sorteren op kleur, lengte, batchnummer, zaagmaat 

![Picture 11, Afbeelding](media/image14.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

12. indien nodig: gebruik de functies up & down om aanpassingen te doen 

![Picture 12, Afbeelding](media/image15.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

13. Selecteer de lijnen die je wil vastleggen in de productieplanning \
    Click \"Select all rows\" 

![Picture 13, Afbeelding](media/image16.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

14. Click schedule \
    MERK op: ENKEL de geselecteerde lijnen worden hiermee gepland 

![Picture 14, Afbeelding](media/image17.jpeg){width="6.268055555555556in" height="3.504861111111111in"} 

15. Click \"Scheduling date\" en vul de datum in waarop je de producties wil voorzien 

![Picture 15, Afbeelding](media/image18.jpeg){width="6.268055555555556in" height="3.5in"} 

16. Belangrijke andere parameters: 

- Scheduling direction = Forward from scheduling date 

<!-- -->

- Optimize performance (PWG) = Yes 

<!-- -->

- Finite capacity = Yes 

<!-- -->

- Schedule reference = Yes 

<!-- -->

- Synchronize references = Yes 

<!-- -->

- Sync production plan group = Yes 

<!-- -->

- Update main production delivery date = Yes 

![Picture 16, Afbeelding](media/image19.jpeg){width="6.268055555555556in" height="3.5in"} 

17. Click \"OK\" 

![Picture 17, Afbeelding](media/image20.jpeg){width="6.268055555555556in" height="3.5in"} 

### Detailplanning week +1

#### Algemeen

**+- elke Donderdag**

- Overloop de gemaakte planning voor de week die komt.

- Ga na of alle materiaal aanwezig is

- Ga na of de lamelreservaties \"efficiënt\" toegewezen zijn

  - Merk op: dit is een tijdelijk stap omdat de orders niet in dezelfde volgorde in het systeem komen als ze uitgeleverd worden

- Indien gewijzigde reservaties: sorteer de productieorders opnieuw in de planning hub

  - Nieuwe sequentie kan nl leiden tot nieuwe productievolgorde

#### Overloop de planning voor de week die komt

- Selecteer alle betreffende sales orders in de planningsxls [Geplande orders AX3 vs Hive](https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/Geplande%20orders%20AX3%20vs%20Hive.xlsx?web=1)

- ga naar de planningshub

- Merk op: We beginnen altijd met de slatorders. open dus op de view \"Slats - planning group 1\"

- Open de view Filter op kolom \'Top reference level\'

- Selecteer alle lijnen

- Open de tab sequence

- Custom sort om op kleur en lengte te zetten

- Eventueel: up, down om de volgorde aan te passen

- Schedule

- Indien van toepassing: Haal de filter weg van de \"planning type 1\" en herhaal voor de non-slat orders.

### Aanleg voorraad boxen week + 1

**+- elke vrijdag**

OUD : Overzicht wordt opgemaakt in excel via data-entiteiten

Sinds 17/07/2025: via power bi rapport

#### Aantal boxen -- overzicht & productieorders

##### Overzicht: Power bi -- Boxes Totals

Open in power bi de Aquadeck app - Production - Boxes - Totals ( [link](https://app.powerbi.com/groups/me/reports/9b83f954-275d-4ad0-ac5f-660cccc3d440/db79a7620794e8e60c07?ctid=ce90b01e-b55e-4d71-9a12-0c57fa10e1ee&pbi_source=shareVisual&visual=0d08a7e79a6a3ac56e41&height=615.06&width=1280.00&bookmarkGuid=65b2009d-3b02-4407-800d-848015c5f1bc) )

\--\> Deze tab geeft het totaal aantal boxen weer voor de ganse week

Selecteer correcte week in de filters bovenaan

Druk deze lijst af voor Yordi

Belangrijk: deze data wordt enkel \'nachts bijgewerkt

![](media/image21.png){width="6.268055555555556in" height="4.225in"}

##### Productieorders

Bovenstaande lijst bevat zowel boxen die aangekocht als geproduceerd worden.

Voor de boxen die we produceren moet manueel een productieorder aangemaakt worden.

  -----------------------------------------------
  Verpakking             Aanvulling
  ---------------------- ------------------------
  Standard packaging     Productie

  Export packaging       Productie

  Koker                  Aankoop

  Niveko create          Aankoop

  Pallet                 Aankoop
  -----------------------------------------------

In bovenstaande lijst zijn er dus 6 artikelen waarvoor we een productieorder moeten aanmaken.

[Aanmaak productieorder]{.underline}

Open **All production orders**

Klik **New production order**

Vul het **artikelnummer** uit de lijst in

Merk op: heel wat data wordt automatisch ingevuld

Vul de **Quantity** in

OK

[Estimate]{.underline}

Lint \> Production order \> Process \> **Estimate**

> Merk op: uitvoeren kan even duren in systeem. kan ook voor meerdere orders en in batch uitgevoerd worden

[Schedule]{.underline}

Lint \> Schedule \> Schedule jobs

Parameters:

- forward from scheduling date

- scheduling date: vandaag

[Release]{.underline}

Lint \> Production order \> Process \> **Release**

> Merk op: uitvoeren kan even duren in systeem. kan ook voor meerdere orders en in batch uitgevoerd worden

Door het releasen zullen de productieorders zichtbaar worden in Tulip en kunnen de dozen geschoten worden.

#### Volgorde boxen

Open rapport Boxes - Supply in power bi ( [link](https://app.powerbi.com/groups/me/reports/9b83f954-275d-4ad0-ac5f-660cccc3d440/6de75a2cac15651e7d08?ctid=ce90b01e-b55e-4d71-9a12-0c57fa10e1ee&pbi_source=shareVisual&visual=8f956e407a85b4a1299e&height=322.64&width=1272.27&bookmarkGuid=06b6cd65-5b36-488d-aa69-f3e317d3ca6e) )

Pas filter aan op de tab \'Boxes - supply\' naar benodigde week

Print deze lijst en geef deze af aan magazijn (Jordi + Martijn) zodat ze de boxes klaar kunnen zetten + in de correcte volgorde

#### ~~OLD: Detail stappenplan productieoverzichten boxen en manueel werk via excel -- scribe~~

1.  ~~Open het xls bestand \"20250623 Report Manueel werk en Boxes\" \
    <https://polletgroupintranet.sharepoint.com/sites/Aquadeck2.0/Shared%20Documents/General/6.%20Cutover/ProductiePlanning/20250623%20Report%20Manueel%20werk%20en%20Boxes.xlsx?web=1> ~~

<!-- -->

2.  ~~Open de tab \"Production components (PWG)\" ~~

![Picture 1, Afbeelding](media/image22.jpeg){width="6.268055555555556in" height="3.504861111111111in"}~~ ~~

3.  ~~Vernieuw de data-entiteit: Click \"Refresh\" ~~

![Picture 2, Afbeelding](media/image23.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

4.  ~~3 output tabbladen gebruiken deze informatie:  ~~

    a)  ~~\"Boxes - totalen\": weekoverzicht voor benodigd aantal dozen ~~

    b)  ~~\"Boxes - aanvoer\": volgorde van de dozen op de lamelmachines \
        belangrijk: pas uitprinten nadat de batch van de lamellen vast ligt - anders kan de volgorde nog wijzigen~~

    c)  ~~\"Manueel werk\": weekoverzicht van het handwerk~~

<!-- -->

5.  ~~Start bij de \"Boxes - totalen\" en zet daar de gewenste **weekfilter **\
    -\> deze weekfilter wordt doorgetrokken op de andere 2 output-tabbladen ~~

> ~~\
> Click \"Boxes - totalen\" ~~

![Picture 3, Afbeelding](media/image24.jpeg){width="6.268055555555556in" height="3.504861111111111in"}~~ ~~

6.  ~~Selecteer de gewenste week uit het overzicht \
    \--\> deze selectie wordt doorgetrokken op de 3 output tabbladen \
    Voorbeeld om de aantallen en order voor week 28 te zien: Click \"28\" ~~

![Picture 4, Afbeelding](media/image25.jpeg){width="6.268055555555556in" height="3.504861111111111in"}~~ ~~

7.  ~~Click de gewenste tabbladen en print af waar nodig ~~

![Picture 5, Afbeelding](media/image26.jpeg){width="6.268055555555556in" height="3.504861111111111in"}

#### ~~OLD: Productie order boxen via MRP~~

~~Belangrijk: Orders worden vooraf door MRP gegenereerd voor de volgende 7 werkdagen (coverage group RTS-007). We doen dit dus idealiter op donderdag.~~

- ~~Ga naar de planned orders: [Planned orders \-- Finance and Operations](https://pwg-prod.operations.eu.dynamics.com/?cmp=1300&mi=ReqPOGridView)~~

- ~~Open de view \"Boxes - Production\"~~

- ~~Selecteer de gewenste regels~~

- ~~Klik \'Firm\' om de productie orders te maken en schedulen~~

- ~~Ga naar all production orders~~

- ~~Selecteer de gemaakte productie orders~~

- ~~Release~~

~~Detailstappen:~~

**~~Generate production order boxes ~~**

1.  ~~Navigate to <https://pwg-prod.operations.eu.dynamics.com/?cmp=1300&mi=ReqPOGridView> ~~

![Picture 1, Afbeelding](media/image27.jpeg){width="6.268055555555556in" height="3.504861111111111in"}~~ ~~

2.  ~~Verify the view: should be \"Boxes - production\" ~~

![Picture 2, Afbeelding](media/image28.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

3.  ~~Select all required lines ~~

![Picture 3, Afbeelding](media/image29.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

4.  ~~Firm ~~

![Picture 4, Afbeelding](media/image30.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

![Picture 5, Afbeelding](media/image31.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

5.  ~~Required parameters: ~~

![Picture 6, Afbeelding](media/image32.jpeg){width="6.268055555555556in" height="3.4944444444444445in"}~~ ~~

6.  ~~Click \"OK\" ~~

![Picture 7, Afbeelding](media/image33.jpeg){width="6.268055555555556in" height="3.5in"}~~ ~~

# Change machine parameters

Example case: zaagmaat van klant moet gewijzigd worden zonder dat er iets wijzigt in de stuklijst. Machine parameters in de tulip stations komen voort uit de \"product attributes\". De manual hieronder legt uit waar je deze kan vinden en hoe je deze kan wijzigen.

## Search for Product Attributes in D365FO

Attributes are always in the project item (22480000001 ) on the specific variant

1.  Open the product variant

    a)  To open the product variant - Navigate to \'Released products\'

> <https://pwg-prod.operations.eu.dynamics.com/?cmp=1300&mi=EcoResProductDetailsExtended> 

 

b)  Action pane \> Click \"Product\" \> Click \"Released product variants\" 

![Picture 3, Afbeelding](media/image34.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

c)  Zoek de betreffende configuratie - in ons geval AQDT\*415 \
    Filter in \"Product number\" op \*415\* \
    selecteer de lijn

 

2.  Machine parameters worden opgeslaan in de product attributes van de variant \
    Om deze te openen: Click \"Product attributes\" 

![Picture 6, Afbeelding](media/image35.jpeg){width="4.34375in" height="1.625in"} 

## Change parameters

1.  Zoek de betreffende parameter. Voor de zaagmaat van de lamellen is dit SlatMachDeckSaw 

 

![Picture 8, Afbeelding](media/image36.jpeg){width="6.268055555555556in" height="3.50625in"} 

2.  Pas de waarde aan naar de nieuwe zaagmaat & klaar !

![Picture 9, Afbeelding](media/image37.jpeg){width="6.268055555555556in" height="3.502083333333333in"} 

# Masterdata

## Change route

Scenario 1: the production order is scheduled and no workplace is assigned

Scenario 2: the production order Is scheduled and a wrong workplace is assigned

It is possible to change the route after scheduling a production order.

- If the route has to be changed for each new production order:

> 🡪 change it on the released product
>
> This will only apply for [new]{.underline} production orders. If existing production orders have to be updated, you\'ll have to update these one by one.

- If the route has to be changed once

> 🡪 change it on the production order.

### On the released product

1.  Go the released item by clicking on the item number

![A screenshot of a computer AI-generated content may be incorrect.](media/image38.png){width="6.274178696412949in" height="2.013076334208224in"}

2.  Go to the tab engineer \> view \> Route

![A screenshot of a computer AI-generated content may be incorrect.](media/image39.png){width="6.152110673665792in" height="1.8989337270341207in"}

3.  If there is no route version, add a route version

![A screenshot of a computer AI-generated content may be incorrect.](media/image40.png){width="3.7897681539807526in" height="2.2946620734908136in"}

4.  Select the correct route and enter the site

![A screenshot of a computer AI-generated content may be incorrect.](media/image41.png){width="5.727830271216098in" height="2.3524343832020995in"}

Remark: a route has been created for each operation and runtime, select the correct one.

5.  Don't change anything else!

6.  Approve and activate the route version

![A screenshot of a computer AI-generated content may be incorrect.](media/image42.png){width="5.670509623797026in" height="1.6384536307961506in"}

### On an existing production order

1.  Go to the production order route

![A screenshot of a computer AI-generated content may be incorrect.](media/image43.png){width="5.861111111111111in" height="1.6993055555555556in"}

2.  In the route, click the operation number to view details

![Afbeelding met tekst, schermopname, Lettertype, nummer Door AI gegenereerde inhoud is mogelijk onjuist.](media/image44.png){width="4.414610673665792in" height="1.5876159230096238in"}

3.  Change the operation

![A screenshot of a computer AI-generated content may be incorrect.](media/image45.png){width="5.62351268591426in" height="1.8535290901137358in"}

4.  Change the resource that must execute the operation

![A screenshot of a computer AI-generated content may be incorrect.](media/image46.png){width="5.46615813648294in" height="2.7288385826771653in"}

5.  Click on NO

![A screenshot of a computer AI-generated content may be incorrect.](media/image47.png){width="3.4990594925634295in" height="1.5170745844269466in"}

6.  If you clicked on yes, make sure you check the run time

![A screenshot of a computer AI-generated content may be incorrect.](media/image48.png){width="5.8186876640419944in" height="2.4567957130358704in"}

7.  **IMPORTANT !** Reschedule the production order for the route to apply

8.  

# Reporting

# Problem solving

## Production orders

### The production order has no workplace

**Cause** the Item has no (active) route

**Solution** assign a route to the Item, assign a route to the production order and reschedule the production order(s)

### no calendars / working times

**Cause** The production / shipping calendars are not set up

**Solution** Compose working times

Open de kalender in \'Working time calendars\'

Klik **Working times**

![Afbeelding met tekst, schermopname, Lettertype, software Door AI gegenereerde inhoud is mogelijk onjuist.](media/image49.png){width="5.520143263342082in" height="2.3017957130358706in"}

Klik **Compose working times**

Kies from date en To date

Selecteer working time template

Zoek de template die overeenkomt met de uren die je wil toewijzen

Voor de ship kalender kozen we in 06/01/2026 de working template \'OTHER\'

Klik OK

\--\> nu zijn de dagen gegenereerd

To do:

1\) zet de collectieve verlofdagen op control = closed

2\) Dagen dat de bezetting niet volledig is, kan je spelen met de productiviteit door de efficienty te verlagen

LET OP: doe dit enkel op de productiekalender

![Afbeelding met tekst, schermopname, nummer, Lettertype Door AI gegenereerde inhoud is mogelijk onjuist.](media/image50.png){width="3.684035433070866in" height="3.445262467191601in"}

Belangrijk:

- SHIP kalender genereren

- SHIP verlofdagen aanduiden dmv control = closed te zetten

- SLAT 2 apart generen en verlofdagen apart ingeven omwille van afwijkende working times

  - Merk op: hier dus ook manueel de control = closed zetten voor verlofdagen

> ![Afbeelding met tekst, schermopname, nummer, software Door AI gegenereerde inhoud is mogelijk onjuist.](media/image51.png){width="3.222089895013123in" height="1.9007075678040244in"}

- Al de rest: genereren met \'use base calendar\'

  - Uren komen overeen met de base calendar

  - Sluitingsdagen enkel invullen op de ship calendar
