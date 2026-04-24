# KB — F&0 Ibanity certificate creation

**Systeem:** Pollet Group IT
**Bron:** Automatisch geconverteerd van `F&0 Ibanity certificate creation.docx`
**Conversiedatum:** 2026-04-24

---

**Ibanity certificate creation**

![Personalized Content Solution \| Content Personalization \| PathFactory \...](media/image1.png){width="2.6770833333333335in" height="2.6770833333333335in"}

# Contents {#contents .TOC-Heading}

[1 Introduction [3](#introduction)](#introduction)

[1.1 Create Active Certificate [4](#create-active-certificate)](#create-active-certificate)

#  

# Introduction

**Why does this document exist?**

Ibanity is an API tool that is used to connect the payment service \"Isabel\" with D365FO. A certificate is used in order to maintain valid connection between both systems. Certificates are only valid for a certain period of time and needs renewal on a yearly basis.

This document is also includeed in manual created by 9A on this topic: [9A IsabelConnector Boekan.docx](https://polletgroupintranet.sharepoint.com/:w:/r/sites/D365FOFinance/Shared%20Documents/General/Manuals/9A%20IsabelConnector%20Boekan.docx?d=w6894888f2d5a45dfb64fee6abe34e1b0&csf=1&web=1&e=C6UE9u)

In the Ibanity portal (https://developer.ibanity.com/) 2 accounts are registered, one for Production environment and another for TEST purposes (can be linked to TEST, BOEKAN or ACC environments):

![A screenshot of a computer AI-generated content may be incorrect.](media/image2.png){width="6.298611111111111in" height="3.3340277777777776in"}

By environment, 2 certificates have to be foreseen so both have to be renewed each time previous gets expired

- Active certificate

- Active signature certificates

For the creation of certificates, SSL software need to be installed. This one can be installed: https://slproweb.com/products/Win32OpenSSL.html

![A screenshot of a computer AI-generated content may be incorrect.](media/image3.png){width="6.298611111111111in" height="2.091666666666667in"}

Some IT remarks:

- Installation can only be executed if you have admin rights (or by an IT administrator) so probably you need to contact IT support

- Use MSI to install (Microsoft installer)

Save the software on your computer, f.e. C:\\Program Files\\OpenSSL-Win64\\bin

## Create Active Certificate

Select the Environment (Test in these printscreens) and go to \"Credentials\".

Click \"Generate\" in the Ibanity platform:

![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png){width="5.308326771653543in" height="3.821176727909011in"}

Below screen will be opened:

![A screenshot of a computer AI-generated content may be incorrect.](media/image5.png){width="4.817084426946631in" height="6.117197069116361in"}

1.  Fill a proper certificate name

2.  Open the \"Command prompt\" as an administrator.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png){width="3.9674978127734035in" height="4.030488845144357in"}

Enter the directory (where the openssl application is saved + command \"2\" to create a private key file.

(Remark, to retain only \"C:\\\", use cd.. to go back to a folder above)

![A screenshot of a computer AI-generated content may be incorrect.](media/image7.png){width="6.298611111111111in" height="1.8902777777777777in"}

Enter PEM pass phrase and validate again. The typed phrase is not visible (f.e typ 12345678). Keep in mind this key as it\'s needed further in the creation process:

![A black screen with white text AI-generated content may be incorrect.](media/image8.png){width="5.783834208223972in" height="0.7917355643044619in"}

This step has created a private_key.pem file

3.  Execute the command of \"step 3\", use the pass phrase of \"step 2\"

![](media/image9.png){width="6.298611111111111in" height="0.3125in"}

A new file \"ibanity.csr\" is now created:

![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png){width="6.298611111111111in" height="3.486111111111111in"}

4.  Upload the ibanity.csr file (or copy/paste the file content in the foreseen field)

![A screenshot of a computer AI-generated content may be incorrect.](media/image11.png){width="4.7254090113735785in" height="2.858581583552056in"}

5.  Click Generate and download

A popup will be shown:

![A screenshot of a certificate Description automatically generated](media/image12.png){width="2.2919860017497813in" height="1.4064457567804025in"}

And a is now saved in the downloads folder:

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png){width="6.298611111111111in" height="2.8493055555555555in"}

6.  Unzip the folder and move the files to the initial folder where the private key file is stored:

![A screenshot of a computer AI-generated content may be incorrect.](media/image14.png){width="6.298611111111111in" height="2.4375in"}

7.  Generate a certificate file that will be uploaded in D365FO afterwards. Go back to the Command window and execute the following command:

openssl pkcs12 -inkey private_key.pem -in certificate.pem -export -out **ACTestv20250411.pfx**

*(adjust the name so it\'s clear which type of certificate file is created)*

![](media/image15.png){width="6.298611111111111in" height="0.6541666666666667in"}

The phrase key of step 2 has to be filled again and a new password has to be entered (will be needed when uploading the file to d365fo):

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png){width="6.298611111111111in" height="3.5388888888888888in"}

8.  Repeat steps 2-7 to create an Active signature certificate:

![A screenshot of a computer AI-generated content may be incorrect.](media/image17.png){width="4.033496281714785in" height="2.9826531058617674in"}

![A screenshot of a computer AI-generated content may be incorrect.](media/image18.png){width="4.50872375328084in" height="6.100528215223097in"}

It can be good to move the created files to a new folder, as those will be overwritten:

![A screenshot of a computer AI-generated content may be incorrect.](media/image19.png){width="6.298611111111111in" height="1.5958333333333334in"}

New private key and ibanity files are generated:

![A screenshot of a computer AI-generated content may be incorrect.](media/image20.png){width="6.298611111111111in" height="4.622222222222222in"}

An active signature certificate requires approval from Isabel. This can take a day. If urgent, ICSSupport@isabelgroup.eu can be contacted.

![A screenshot of a computer AI-generated content may be incorrect.](media/image21.png){width="6.298611111111111in" height="1.9680555555555554in"}

An email is sent when certificate is approved:

Copy the download (extracted files) to the ssl folder:

![A screenshot of a computer AI-generated content may be incorrect.](media/image22.png){width="6.298611111111111in" height="2.854861111111111in"}

Execute script:

openssl pkcs12 -inkey private_key.pem -in **signature\_**certificate.pem -export -out **ASCTestv20250411.pfx**

*(adjust the name so it\'s clear which type of certificate file is created)*

New certificate Is added and can be uploaded In d365fo:

![A screenshot of a computer AI-generated content may be incorrect.](media/image23.png){width="3.9674267279090114in" height="4.117024278215223in"}

Add the certificate file in your custom file:

![A screenshot of a computer AI-generated content may be incorrect.](media/image24.png){width="6.298611111111111in" height="2.0902777777777777in"}

After approval: upload In d365fo:
