# KB — Handleiding (Het verwijderen en het heraanmaken van een artikel in D365)

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `Handleiding (Het verwijderen en het heraanmaken van een artikel in D365).docx`
**Conversiedatum:** 2026-04-24

---

# Inhoudsopgave {#inhoudsopgave .TOC-Heading}

[Handleiding: Artikel vanuit AX3 aanmaken in D365 [2](#handleiding-artikel-vanuit-ax3-aanmaken-in-d365)](#handleiding-artikel-vanuit-ax3-aanmaken-in-d365)

[Stap 1: Bespreek de scenario's en artikeltypes [2](#stap-1-bespreek-de-scenarios-en-artikeltypes)](#stap-1-bespreek-de-scenarios-en-artikeltypes)

[Stap 2: Kies het type artikel om aan te maken [2](#stap-2-kies-het-type-artikel-om-aan-te-maken)](#stap-2-kies-het-type-artikel-om-aan-te-maken)

[Stap 3: Controleer of het artikel al bestaat in D365 [2](#stap-3-controleer-of-het-artikel-al-bestaat-in-d365)](#stap-3-controleer-of-het-artikel-al-bestaat-in-d365)

[Stap 4: Maak een nieuwe lijn aan in Interface Lines [3](#stap-4-maak-een-nieuwe-lijn-aan-in-interface-lines)](#stap-4-maak-een-nieuwe-lijn-aan-in-interface-lines)

[Stap 5: Product Staging [4](#stap-5-product-staging)](#stap-5-product-staging)

[Stap 6: Afronding [4](#stap-6-afronding)](#stap-6-afronding)

[Handleiding: Het opnieuw aanmaken van een artikel in D365 [4](#handleiding-het-opnieuw-aanmaken-van-een-artikel-in-d365)](#handleiding-het-opnieuw-aanmaken-van-een-artikel-in-d365)

[Redenen voor het opnieuw aanmaken van een artikel [4](#redenen-voor-het-opnieuw-aanmaken-van-een-artikel)](#redenen-voor-het-opnieuw-aanmaken-van-een-artikel)

[Stap 1: Controleer op bestaande transacties (Analyse) [5](#stap-1-controleer-op-bestaande-transacties-analyse)](#stap-1-controleer-op-bestaande-transacties-analyse)

[Stap 2-a: Procedure voor het verwijderen van een artikel met lopende of voltooide transacties [5](#stap-2-a-procedure-voor-het-verwijderen-van-een-artikel-met-lopende-of-voltooide-transacties)](#stap-2-a-procedure-voor-het-verwijderen-van-een-artikel-met-lopende-of-voltooide-transacties)

[Stap 2-b: Procedure voor het verwijderen van een artikel zonder transacties [6](#stap-2-b-procedure-voor-het-verwijderen-van-een-artikel-zonder-transacties)](#stap-2-b-procedure-voor-het-verwijderen-van-een-artikel-zonder-transacties)

[Stap 3: Opnieuw aanmaken van het artikel [7](#stap-3-opnieuw-aanmaken-van-het-artikel)](#stap-3-opnieuw-aanmaken-van-het-artikel)

# Handleiding: Artikel vanuit AX3 aanmaken in D365

Inleiding: In deze handleiding gaan we stap voor stap het proces doorlopen om een artikel dat reeds bestaat in AX3 aan te maken in D365. Het is belangrijk dat het artikel in AX3 al bestaat voordat het in D365 wordt overgezet. Dit proces bestaat uit verschillende stappen, waarbij we beslissen wat voor type artikel we willen aanmaken en controleren of het artikel al in D365 bestaat. Deze handleiding biedt een gestructureerd overzicht van het proces van het opnieuw aanmaken van een artikel in D365, met aandacht voor transacties en het correct verwijderen en opnieuw interfacen van artikelen.

## Stap 1: Bespreek de scenario's en artikeltypes

In AX3 bestaan er twee types artikelen:

- Individueel artikel: Een enkele, unieke artikel.

- Configureerbaar artikel: Een product waarbij verschillende configuraties mogelijk zijn.

- Configuratie: Een configuratie van een configureerbaar artikel

In D365 zijn er ook drie types artikelen:

- Distinct Product: Een individueel artikel dat ook in AX3 als individueel artikel bestaat.

- Product Master: Een configureerbaar artikel, hetzelfde als een configureerbaar artikel in AX3.

- Distinct Product Variant: Een configuratie van een product master

## Stap 2: Kies het type artikel om aan te maken

Voordat we een artikel in D365 aanmaken, moeten we bepalen welk type artikel we willen overzetten vanuit AX3. De vier types artikelen in D365 zijn:

- Distinct Product

- Product Master

- Distinct Product Variant

- [Distinct Product (Config): Dit is een scenario waarbij een configuratie (AX3) wordt aangemaakt als een individueel artikel in D365]{.mark}

## Stap 3: Controleer of het artikel al bestaat in D365

1.  In AX3 kun je in de tab 'AX3 -- D365 Interface nagaan of het artikel reeds bestaat in D365.

2.  Controleer of het artikel al in D365 bestaat en in welke legale entiteiten het actief is.

3.  Als het artikel al bestaat, maar niet binnen jouw legale entiteit, moet je het alsnog aanmaken binnen jouw entiteit. (De LE waarin het artikel aangemaakt is, kan je zien in de kolom 'Company' -- *Zie screenshot*)

![](media/image1.png){width="6.260416666666667in" height="3.6354166666666665in"}

## Stap 4: Maak een nieuwe lijn aan in Interface Lines

- Als het artikel nog niet bestaat in jouw legale entiteit, klik op '**Items to interface with D365'**.

- Voeg een nieuwe lijn toe voor het artikel.

- Klik op \'Opslaan\' of gebruik de sneltoets \'Ctrl+S\' om het artikel op te slaan.

- Wacht een paar seconden (kan tot één minuut duren) totdat het artikel verschijnt in de Product Staging.

![](media/image2.png){width="6.25in" height="2.8645833333333335in"}

**Let op**: bij het toevoegen van een configureerbaar artikel moet je aangeven of je het als een configuratie of als een individueel artikel wilt doorgeven. Kies je voor \'No\', dan wordt het artikel als een niet-configureerbaar artikel doorgegeven. Kies je voor \'Yes\', dan wordt het artikel als een configureerbaar artikel doorgegeven met de door jou gekozen configuratie.

## Stap 5: Product Staging

Wanneer een artikel in de Product Staging terechtkomt:

- Het artikel krijgt de status \'new\'.

- Vul de nodige velden in die van toepassing zijn voor het artikel. Na het aanpassen krijgt het artikel de status \'in review\'.

  - Selecteer een Product Staging Template. Dit zorgt ervoor dat enkele financiële en magazijn-gerelateerde velden automatisch worden ingevuld.

  - Selecteer de productgroepen. Je bent verplicht om alle vier productgroepen te selecteren. Als bepaalde productgroepen (zoals productgroep 4) niet bestaan, kies dan een lege productgroep voor dat veld.

  - Vul alle overige verplichte velden in

- Als alle vereiste velden zijn ingevuld, klik op \'Validate\' om het artikel de status \'Validated\' te geven.

![A screenshot of a computer Description automatically generated](media/image3.png){width="6.268055555555556in" height="1.9479166666666667in"}

## Stap 6: Afronding

Wanneer alle velden correct zijn ingevuld en het artikel gevalideerd is, wordt het definitief aangemaakt in D365. Hiervoor moet je op \'Create\' klikken.

Dit is het volledige proces voor het aanmaken van artikelen in D365 vanuit AX3.

# Handleiding: Het opnieuw aanmaken van een artikel in D365

Het opnieuw aanmaken van een artikel in D365 kan nodig zijn om verschillende redenen. Hieronder worden de stappen uitgelegd om een bestaand artikel opnieuw op te zetten, inclusief de procedures voor het omgaan met transacties en het verwijderen van oude artikelen.

## Redenen voor het opnieuw aanmaken van een artikel

Een artikel kan om diverse redenen opnieuw aangemaakt moeten worden, bijvoorbeeld:

1.  De gebruiker wil de producttype van het artikel wijzigen, zoals het omzetten van een configuratie van een configureerbaar artikel naar een niet-configureerbaar artikel of vice versa.

2.  Het artikel heeft verkeerde productgroepen toegewezen gekregen, wat heraanmaak vereist, omdat de productgroep invloed heeft gehad op het artikelnummer.

3.  ...

## Stap 1: Controleer op bestaande transacties (Analyse)

Voordat je een artikel opnieuw aanmaakt, moet je nagaan of er lopende of voltooide transacties zijn gekoppeld aan het artikel in D365. Dit is belangrijk omdat:

1.  **Als er transacties zijn**, mag het artikel niet zomaar opnieuw aangemaakt worden.

2.  **Als er geen transacties zijn**, kan het artikel zonder problemen verwijderd en opnieuw aangemaakt worden.

Wanneer er lopende of voltooide transacties zijn voor het artikel in D365, moet de medewerker die de aanvraag doet om het artikel opnieuw aan te maken, moet zich ervan bewust zijn dat het nieuwe artikel in de volgende processen moet worden aangepast:

1.  Het is cruciaal om eerst te bepalen in welke orders het artikel is opgenomen. Voordat de koppeling tussen AX3 en D365 wordt verbroken, moeten de lopende orders geanalyseerd worden. Dit is van belang omdat het oude artikel na het opnieuw aanmaken vervangen moet worden door het nieuwe, zolang de orders nog niet zijn afgehandeld.

2.  Voorraad moet worden overgeboekt naar het nieuwe artikel.

3.  BOM's (stuklijsten) moeten worden aangepast nadat het nieuwe artikel wordt vrijgegeven in D365.

## Stap 2-a: Procedure voor het verwijderen van een artikel met lopende of voltooide transacties

1.  Nadat de analyse is uitgevoerd, mag je de koppeling tussen AX3 en D365 verwijderen.

    a.  Dit doe je door te navigeren naar: Setup \> Interface product code mapping.

    b.  Schakel de parameter \'Remove\' in.

    c.  Klik op \'Ok\'.

> Hierdoor wordt de link met AX3 verbroken en wordt de mapping tussen D365 en AX3 opgeheven.

![](media/image4.png){width="6.25in" height="1.8125in"}

2.  Hierna ken je het artikel de status 'Obsolete' (OBS) toe. Een artikel dat verbonden is met transacties kan niet verwijderd worden. In dit geval moet het artikel de status 'Obsolete' (OBS) krijgen.

    a.  Dit doe je door naar het veld Product Lifecycle State te navigeren en de status hiervan naar 'OBS' (Obsolete) te wijzigen

    b.  Sla de wijzigen op

3.  **Daarna moet je ook de parameter 'Visible in webshop' uitzetten**.

    a.  Als het een Product Master is met Configuraties, vergeet niet om deze uit te zetten ook op de Configuraties.

![](media/image5.png){width="6.260416666666667in" height="5.052083333333333in"}

## Stap 2-b: Procedure voor het verwijderen van een artikel zonder transacties

Als er geen transacties aan het artikel zijn gekoppeld, kan het direct verwijderd worden. Volg deze stappen:

1.  Verbreek de koppeling tussen D365 en AX3:

<!-- -->

a.  Dit doe je door te navigeren naar: Setup \> Interface product code mapping.

b.  Schakel de parameter \'Remove\' in.

c.  Klik op \'Ok\'.

<!-- -->

2.  Verwijder het artikel:

    a.  Klik op \'Delete\' om het artikel volledig uit het systeem te verwijderen.

    b.  Confirmeer dat je het artikel effectief wilt verwijderen.

![A screenshot of a computer Description automatically generated](media/image6.png){width="6.268055555555556in" height="4.930555555555555in"}

Verwijder configureerbare artikelen:

**Opmerking:** Voor configureerbare artikelen wordt bij dit procedure zowel de product master als de configuraties worden verwijderd.

Als je alleen een specifieke configuratie wilt verwijderen, volg dan dezelfde stappen voor de desbetreffende configuratie.

## Stap 3: Opnieuw aanmaken van het artikel

Nadat het artikel is verwijderd of de OBS-status heeft gekregen ken je het artikel opnieuw meegeven vanuit AX3.

Vervolgens kun je het artikel opnieuw vrijgeven in D365 met de correcte informatie en productgroepen. (Zie handleiding: Artikel vanuit AX3 aanmaken in D365)

**OPGELET: Vergeet zeker niet om vervolgens het heraangemaakte artikel ook te vervangen in de BOMs en in de lopende transacties. Dit is zeker belangrijk.\
*(Best laat je de werknemers zelf deze toevoegen aan de BOMs en de configuratiekeuzes)***
