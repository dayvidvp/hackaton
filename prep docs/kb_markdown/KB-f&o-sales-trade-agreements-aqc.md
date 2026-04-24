# KB — F&O Sales trade agreements AQC

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&O Sales trade agreements AQC.docx`
**Conversiedatum:** 2026-04-24

---

# Contents {#contents .TOC-Heading}

[1 How to set up Sales prices [2](#how-to-set-up-sales-prices)](#how-to-set-up-sales-prices)

[1.1 Define customer price groups [2](#define-customer-price-groups)](#define-customer-price-groups)

[1.2 Select price group for every customer [2](#select-price-group-for-every-customer)](#select-price-group-for-every-customer)

[1.3 Upload price agreements for the price groups [3](#upload-price-agreements-for-the-price-groups)](#upload-price-agreements-for-the-price-groups)

[1.4 Upload any price agreements for specific customers [4](#upload-any-price-agreements-for-specific-customers)](#upload-any-price-agreements-for-specific-customers)

[2 How to set up Sales discounts [6](#how-to-set-up-sales-discounts)](#how-to-set-up-sales-discounts)

[2.1 Define customer discount groups [6](#define-customer-discount-groups)](#define-customer-discount-groups)

[2.2 Select discount group for every customer [8](#select-discount-group-for-every-customer)](#select-discount-group-for-every-customer)

[2.3 Define Item discount groups [9](#define-item-discount-groups)](#define-item-discount-groups)

[2.4 Select discount group for every Item [11](#select-discount-group-for-every-item)](#select-discount-group-for-every-item)

[2.5 Upload discount agreements [12](#upload-discount-agreements)](#upload-discount-agreements)

[2.5.1 All customers -- Specific item -- 0% discount [13](#all-customers-specific-item-0-discount)](#all-customers-specific-item-0-discount)

[2.5.2 Customer group -- Specific item -- 30% discount & 31% discount [13](#customer-group-specific-item-30-discount-31-discount)](#customer-group-specific-item-30-discount-31-discount)

[2.5.3 Customer group - Item group - 40% discount [14](#customer-group---item-group---40-discount)](#customer-group---item-group---40-discount)

[2.5.4 Specific customer - Item group - 27% discount [15](#specific-customer---item-group---27-discount)](#specific-customer---item-group---27-discount)

[2.5.5 Specific customer - Specific Item - 33% discount [15](#specific-customer---specific-item---33-discount)](#specific-customer---specific-item---33-discount)

[3 How to check trade agreements for specific Items [16](#where-to-find-the-existing-trade-agreements-for-specific-items)](#where-to-find-the-existing-trade-agreements-for-specific-items)

# How to set up Sales prices

## Define customer price groups

Price groups represent your price lists.

So If you have a price list which Is followed by multiple customers, you create a price group and link the customer to that price group. When you put the prices In the system for that price group, every customer linked to that price group will get those prices.

The standard price group for Aqua.com Is \"10\".

## Select price group for every customer

If you need to do this for 1 customer, you can go to the customer via \"All customers\" and then look for this field and change the price group manually by selecting it from the dropdown.

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="4.561185476815398in" height="2.2194466316710413in"}

If you have this view, you will find the field In the last column to the right. If you change to EDIT mode, you can also change It here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.268055555555556in" height="1.0805555555555555in"}

If you need to do this for multiple customers, you can select the customers In the table and then click on the 3 dots at the right to use \"Edit selected lines\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="6.268055555555556in" height="1.2479166666666666in"}

Select the field you want to change and the value to which you want to change It. In this case It Is easiest to filter on \"Price group\" so you only get the options that fit here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="4.249204943132108in" height="1.6768963254593177in"}

When you have made your choice, click on \"Apply\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="3.3933366141732284in" height="1.0673589238845145in"}

## Upload price agreements for the price groups

In Navision there were 1973 price agreements for \'Sales type - 2\", which represented your standard prices.

I was able to upload 1318 agreements because the Item could be linked to a D365 code. This means that 655 price agreements were not uploaded because the Items were not created In D365.

In Navision there were 2837 price agreements for \'Sales type - 0\', which represented your customer specific prices. I was able to upload 2196 agreements because both the Items and the customer could be linked to a D365 Item and customer. This means that 641 price agreements were not uploaded because either the Item or the customer could not be linked.

Go to the menu \"Trade agreement journals\".

Click on \"+New\".

Select the Name (which Is the type of journal so In this case Sales price) and elaborate In the description for your own clarification. Then click on \"Lines\" at the top.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.4013888888888888in"}

As we are currently discussing price for a specific price group, this Is the example shown In the printscreen. The \"Party code type\" needs to be \"Group\" and then you can choose \"10\" In the \"Account selection\". The \"Product code type\" Is \"Table\" because we want to be able to select specific Items from the Item table.

The first line Is just a fixed price for an Item. The second and third line are based on a specific quantity. In the second line which has a \"to-quantity\" It Is Important to activate the checkmark \"Find next\" from No to Yes at the bottom. (For other lines this should remain on No).

The \"From date\" Is always mandatory, the \"To date\" Is optional.

You can add as many lines as you want. Once you are ready just \"Post\" the journal and this will activate the agreements.

![A screenshot of a computer AI-generated content may be incorrect.](media/image8.png){width="6.268055555555556in" height="2.55625in"}

## Upload any price agreements for specific customers

Whether or not a customer belongs to a price group or not, It Is always possible to create customer specific price agreements. These will always overrule group prices. So when the group price Is 5€ and the customer price Is 4,5€, the customer specific price will be used.

Go to the menu \"Trade agreement journals\".

Click on \"+New\".

Select the Name (which Is the type of journal so In this case Sales price) and elaborate In the description for your own clarification. Then click on \"Lines\" at the top.

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.268055555555556in" height="1.4013888888888888in"}

As we are currently discussing price for specific customers, this Is the example shown In the printscreen. The \"Party code type\" needs to be \"Table\" and then you can choose the customer In the \"Account selection\". The \"Product code type\" Is \"Table\" because we want to be able to select specific Items from the Item table.

The first line Is just a fixed price for an Item. The second and third line are based on a specific quantity. In the second line which has a \"to-quantity\" It Is Important to activate the checkmark \"Find next\" from No to Yes at the bottom. (For other lines this should remain on No).

The \"From date\" Is always mandatory, the \"To date\" Is optional.

You can add as many lines as you want. Once you are ready just \"Post\" the journal and this will activate the agreements.

![A screenshot of a computer AI-generated content may be incorrect.](media/image9.png){width="6.268055555555556in" height="2.6125in"}

# How to set up Sales discounts

## Define customer discount groups

These groups have currently been defined for Aqua.com.

1719 customers have been analyzed and groups were created based on their discounts. These 1719 customers have all been put into a group. (35041 trade agreements from Navision were replaced by 3899 trade agreements In D365)

517 customers with a total of 21687 related discount agreements still need to be added to a group. It Is possible more groups will be created. This job Is not yet finished!

  ---------------------------------------------------------
  0             0% Discount (default)
  ------------- -------------------------------------------
  FIL-CART15    15% for FIL-CART

  FIL-CART20    20% for FIL-CART

  FIL-CART25    25% for FIL-CART

  FIL-CART30    30% for FIL-CART

  HOUS-SP25     25% for HOUS-SP

  HOUS-SP30     30% for HOUS-SP

  NO GROUP      No group, all customer specific discounts

  P25W15        Pool 25% - Water 15%

  P30W30        Pool 30% - Water 30%

  P35W15        Pool 35% - Water 15%

  P35W20        Pool 35% - Water 20%

  P35W25        Pool 35% - Water 25%

  P35W30        Pool 35% - Water 30%

  P40W20        Pool 40% - Water 20%

  P40W25        Pool 40% - Water 25%

  P40W27        Pool 40% - Water 27%

  P40W30        Pool 40% - Water 30%

  P40W33        Pool 40% - Water 33%

  P40W35        Pool 40% - Water 35%

  P45W20        Pool 45% - Water 20%

  P45W25        Pool 45% - Water 25%

  P45W30        Pool 45% - Water 30%

  P45W35        Pool 45% - Water 35%

  P48W32        Pool 48% - Water 32%

  P50W20        Pool 50% - Water 20%

  P50W25        Pool 50% - Water 25%

  P50W30        Pool 50% - Water 30%

  P50W35        Pool 50% - Water 35%

  P53W35        Pool 53% - Water 35%

  POOL15A       Pool customers 15% - A

  POOL20A       Pool customers 20% - A

  POOL25A       Pool customers 25% - A

  POOL30A       Pool customers 30% - A

  POOL30B       Pool customers 30% - Isolatie 25%

  POOL35A       Pool customers 35% - A

  POOL35B       Pool customers 35% - Isolatie 25%

  POOL40A       Pool customers 40% - A

  POOL40B       Pool customers 40% - Isolatie 25%

  POOL45A       Pool customers 45% - A

  POOL45B       Pool customers 45% - Isolatie 25%

  POOL48A       Pool customers 48% - A

  POOL48B       Pool customers 48% - Isolatie 25%

  POOL50A       Pool customers 50% - A

  POOL50B       Pool customers 50% - Isolatie 25%

  WATER10A      Water customers 10% - A

  WATER15A      Water customers 15% - A

  WATER20A      Water customers 20% - A

  WATER25A      Water customers 25% - A

  WATER25B      Water customers 25% +extra discounts

  WATER27A      Water customer 27% - A

  WATER30A      Water customers 30% - A

  WATER30B      Water customers 30% +extra discounts

  WATER31,5A    Water customers 31,5% - A

  WATER33A      Water customers 33% - A

  WATER34A      Water customers 34% - A

  WATER34B      Water customers 34% +extra discounts

  WATER35A      Water customers 35% - A

  WATER35B      Water customers 35% +extra discounts

  ZERO          0% Discount
  ---------------------------------------------------------

## Select discount group for every customer

If you need to do this for 1 customer, you can go to the customer via \"All customers\" and then look for this field and change the Line discount group manually by selecting it from the dropdown.

![](media/image10.png){width="4.248465660542432in" height="1.9783180227471566in"}

If you have this view, you will find the field in the table. If you change to EDIT mode, you can also change It here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="6.268055555555556in" height="0.9666666666666667in"}

If you need to do this for multiple customers, you can select the customers In the table and then click on the 3 dots at the right to use \"Edit selected lines\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png){width="6.268055555555556in" height="1.4368055555555554in"}

Select the field you want to change and the value to which you want to change It. In this case It Is easiest to filter on \"Module = Customer\" so you only get the options that fit here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="4.442839020122484in" height="1.7016283902012248in"}

When you have made your choice, click on \"Apply\".

## Define Item discount groups

These groups have currently been defined for Aqua.com. It Is always possible to add more groups. It can be confusing that groups of other companies are also visible In the dropdown list.

  --------------------------------------------------------------------
  **Code Navision**   **Code D365**   **Omschrijving**
  ------------------- --------------- --------------------------------
  0101                SOFTMONO        Compact ontharders

  0102                SOFTSIMPL       Simplex ontharders

  0103                SOFTTWIN        Twin ontharders

  0104                SOFTDUPL        Duplex ontharders

  0106                FIL-EVOLVE      Evolve filter units

  0201                FLEXIBLES       Flexibels

  0202                FIL-ARION       arion filters

  0205                FIL-CINTROPUR   cintropur filters

  0207                FIL-PURO        Puro filters

  0209                FIL-CART        inline filters & cartridges

  0211                CLACK-ADAP      Clack adapters

  0301                TESTKITS        testkits

  0301                RO-UNITS        complete ro units

  0304                DHMET           DH metering

  0405                RESIN-LAN       Lanxess harsen

  0406                RESIN-DUP       Dupont harsen

  0407                RESIN-PUR       Purolite harsen

  0409                RESIN-CH        Chinese harsen

  0501                VESS-RESID      Residential tanks

  0502                VESS-IND-T      industrial tanks 4\" draad

  0503                VESS-IND-F      industrial tanks 6\" flens

  0506                VESS-SPEC       special tanks

  0507                VESS-VINYL      vinylester/polyester tanks

  0508                DISTRI-SYS      verdeelsystemen

  0509                DISTRI-SP       onderdelen verdeelsystemen

  0511                VESS-WELLM      wellmate tanks

  0515                VESS-CALPL      Calplas tanks

  0521                VESS-WC         Wave Cyber tanks

  0600                AUTO-VALV       Autotrol kleppen

  0603                CLACK-VALV      Clack kleppen

  0604                CAPP-VALV       Cappers kleppen

  0605                AQUAM-VALV      Aquamatic kleppen

  0607                EWS             EWS sturingen

  0608                FOBR-VALV       Fobrite kleppen

  0702                FLECK2750       2750 fleck fleppen

  0703                FLECK2850       2850 fleck fleppen

  0704                FLECK2910       2910 fleck fleppen

  0705                FLECK3150       3150 fleck fleppen

  0706                FLECK3900       3900 fleck fleppen

  0707                FLECKDOMEST     Huishoudelijke Fleck kleppen

  0709                FLECKTWIN       twin Fleck kleppen

  0710                FLECKSPARE      Fleck onderdelen

  0711                FLECKACC        Fleck accessoires

  0800                SIATA           Siata kleppen

  0801                SIATA           Siata kleppen

  0901                BRINETANKS      zoutbakken & bodems

  0902                STOR.TANKS      storage tanks

  0903                BRINEVALVES     pekelbuizen en -kleppen

  0904                CABINETS        cabinets

  1000                MEDIA           media

  1101                FILTER          cart. en zandfilters - kleppen

  1102                POMPEN          frequentie en std pompen

  1103                TEGENSTR        tegenstroominstallaties

  1104                INBOUWST        inbouwdelen

  1105                PVC             pvc fittings en buizen

  1106                STURINGEN       sturingskasten en transfo\'s

  1107                WARMTEP         warmtepompen

  1108                POOL BREEZE     chemicaliën

  1109                LADDERS         ladders std & 2-delig

  1110                ONDERHOUD       accessoires

  1111                ISOLATIE        polystryeen blokken en foam

  1112                ROBOTS          automatische stofzuigers

  1113                TEGELS          boordst. & terrastegels

  1114                SOLAR           zonnepanelen

  1115                DESINFECTIE     dosseersystemen

  1116                AFDEKKINGE      bubbel & winterafdekkingen

  1117                LED             lampen en sturingen

  1118                ALKORPLAN       liners & zwemvijver liners

  1119                COUVERTURE      automatische afdekkingen

  1302                MEM-HYDR        Hydranautics ro membranen

  1303                HOUS-SP         onderdelen drukbuizen

  1304                EDI             EDI units

  1305                AQUALINE        Aqualine microfiltratie

  1306                UV-SITA         uv units

  13021               MEM-M&H         Oltremare membranen

  13022               MEM-DUPONT      Filmtec membranen

  13032               HOUS-CODEL      Drukbuizen CodeLine

  13033               HOUS-BEL        Drukbuizen Bel

  13035               HOUS-RVS        Drukbuizen Stainless Steel

  13036               HOUS-WAVE       Drukbuizen Wave Cyber

  0606.H              HEYL            Heyl Neomeris

  13022UF             UF-DUPONT       Dupont uf membranen

  13025UF             UF-PENTAIR      X-Flow uf membranen

  1302UF              UF-HYDRA        Hydranautics uf membranes
  --------------------------------------------------------------------

## Select discount group for every Item

If you need to do this for 1 Item, you can go to the Item via \"Released products\" and then look for this field and change the Line discount group manually by selecting it from the dropdown.

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="3.0593930446194224in" height="1.9089402887139109in"}

If you have this view, you will find the field in the table. If you change to EDIT mode, you can also change It here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png){width="6.268055555555556in" height="1.3222222222222222in"}

If you need to do this for multiple Items, you can select the items In the table and then click on the 3 dots at the right to use \"Edit selected lines\".

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png){width="6.268055555555556in" height="1.3423611111111111in"}

Select the field you want to change and the value to which you want to change It. In this case It Is easiest to filter on \"Module = Inventory\" so you only get the options that fit here.

![A screenshot of a computer AI-generated content may be incorrect.](media/image17.png){width="4.74959208223972in" height="1.9096237970253718in"}

When you have made your choice, click on \"Apply\".

## Upload discount agreements

You can add discounts for the following parties in any possible combination. The more specific option will always overrule a more general option.

  -----------------------------------------------------------------------
  Specific customer                   Specific item
  ----------------------------------- -----------------------------------
  Customer discount group             Item discount group

  All customers                       All items
  -----------------------------------------------------------------------

In Navision there were 69800 discount trade agreements for Item groups (chapters). 56728 agreements could be matched to a customer and Item created In D365. Those 56728 agreements are for 2236 customers. 1719 customers have been analyzed and groups were created based on their discounts. These 1719 customers have all been put into a discount group. (35041 trade agreements from Navision were replaced by 3899 trade agreements In D365)

517 customers with a total of 21687 related discount agreements still need to be added to a group. It Is possible more groups will be created. (This job Is not yet finished but every customer has to be checked one at a time and I noticed I can only do between 20-30 per hour and I have run out of hours.)

In Navision there were also 9823 discount agreements for specific Items. I was able to upload 4752 of those agreements because they could be linked to a customer and Item In D365. This means that 5071 agreements were not uploaded because either the customer or the Item couldn\'t be linked.

Go to the menu \"Trade agreement journals\".

Click on \"+New\".

Select the Name (which Is the type of journal so In this case Sales Discount) and elaborate In the description for your own clarification. Then click on \"Lines\" at the top.

![A screenshot of a computer AI-generated content may be incorrect.](media/image18.png){width="6.268055555555556in" height="1.7347222222222223in"}

Below I will show printscreens of multiple examples. Once you have added the lines In the journal you just need to \"Post\" It with the button at the top.

### All customers -- Specific item -- 0% discount

![A screenshot of a computer AI-generated content may be incorrect.](media/image19.png){width="6.268055555555556in" height="2.217361111111111in"}

### Customer group -- Specific item -- 30% discount & 31% discount

![A screenshot of a computer AI-generated content may be incorrect.](media/image20.png){width="6.268055555555556in" height="2.7402777777777776in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image21.png){width="6.268055555555556in" height="2.571527777777778in"}

### Customer group - Item group - 40% discount

![A screenshot of a computer AI-generated content may be incorrect.](media/image22.png){width="6.268055555555556in" height="2.879861111111111in"}

### Specific customer - Item group - 27% discount

![A screenshot of a computer AI-generated content may be incorrect.](media/image23.png){width="6.268055555555556in" height="2.829861111111111in"}

### Specific customer - Specific Item - 33% discount

![A screenshot of a computer AI-generated content may be incorrect.](media/image24.png){width="6.268055555555556in" height="2.933333333333333in"}

# where to find the existing trade agreements for specific Items

Go to \"Released products\", select your Item and click on \"Sell - View - Sales price or Line discount\".

![A screenshot of a computer screen AI-generated content may be incorrect.](media/image25.png){width="4.299609580052493in" height="2.2750863954505687in"}

**[Sales price:]{.underline}**

You can see there Is a general sales price for price group 10 and there are 2 customer specific prices.

![A screenshot of a computer AI-generated content may be incorrect.](media/image26.png){width="6.268055555555556in" height="2.2354166666666666in"}

**[Line discount:]{.underline}**

There are many discount agreements because the Item Is part of discount group DISTRI-SP and there are a lot of agreements for this Item group. As It Is a part of multiple new customer discount groups and there are also customer specific discounts.

![A screenshot of a computer AI-generated content may be incorrect.](media/image27.png){width="6.268055555555556in" height="6.540277777777778in"}
