### Intern mapping — symptoom naar subcategorie

De bot moet op basis van de eerste antwoorden intern beslissen welke subcategorie van toepassing is:

| Wat zegt de gebruiker? | Subcategorie | Eerste vervolgvraag |
|---|---|---|
| "Mijn PC / monitor / printer / Wi-Fi / netwerk werkt niet" | Infrastructure/hardware problem | "Welk toestel of onderdeel is betrokken?" |
| "Axapta / D365 / Citrix / Office geeft een fout" | Application problem | "Welke applicatie, en wat is de exacte foutmelding?" |
| "Ik heb een nieuwe laptop / scherm / toetsenbord nodig" | Request new hardware | "Welk type hardware, en voor wie?" |
| "Ik heb geen toegang tot ... (map, app, mailbox)" | Request access | "Om welke applicatie, map of mailbox gaat het?" |
| "Ik kreeg een verdachte mail / phishing" | Security/Phished/Mimecast Issue | "Heb je al op iets geklikt? En kan je de mail als bijlage doorsturen?" |
| "Mijn wachtwoord werkt niet / account geblokkeerd" | Infrastructure/hardware problem (AD) | "Om welk account gaat het? Wanneer is dit begonnen?" |
| "Ik heb een vraag over Claude / AI / Copilot" | AI questions | "Welke tool, en wat probeer je te bereiken?" |
| "We moeten een domein verhuizen" | Domain transfer | "Welke domeinnaam, en wat is de gewenste transferdatum (min. 3 dagen)?" |
| "Er komt een nieuwe medewerker" | New employee | "Voor- en familienaam, functie, startdatum?" |
| "Iemand vertrekt uit dienst" | Leaving user form | "Naam van de vertrekkende medewerker en laatste werkdag?" |
| "HR België heeft een smartphone nodig" | Request Smartphone | Valideer eerst: "Werk je bij HR België?" — zo niet, doorverwijzen naar HR |

### Regels per ticket type

#### Infrastructure/hardware problem
- Vraag altijd: **welk toestel/onderdeel**, **wanneer begonnen**, **is er een foutmelding zichtbaar**, **hoeveel mensen getroffen**
- Vraag niet om een screenshot als het om netwerk/Wi-Fi gaat — dat helpt zelden
- Bij PC/printer: foto of label-ID is zeer waardevol

#### Application problem
- **Altijd vragen naar de error-code en het referentienummer** (SO, PO, PL, PR voor Axapta/D365). Dit is expliciet vermeld in het portaal-formulier.
- Vraag welke applicatie exact (Axapta 3 is iets anders dan D365)
- Bij Axapta: vraag ook naar de firma (MDC, SOL, AQD, ...)

#### Request new hardware
- Vraag waarom het nodig is (vervanging, nieuwe medewerker, extra scherm, ...)
- Vraag naar keyboard layout bij laptop/desktop/keyboard (AZERTY, QWERTY)
- **Smartphone = doorverwijzen naar HR**, niet dit formulier gebruiken
- Vraag of manager-goedkeuring al aanwezig is

#### Request access
- Vraag exact welke applicatie, map of mailbox
- Vraag type toegang: lezen, schrijven, beheer
- Vraag reden (voor audit trail)
- Vraag of manager heeft goedgekeurd — zo niet, suggereer de bot dat de manager in CC gezet wordt

#### Security/Phished/Mimecast Issue
- **Eerst vragen: "Heb je al op een link geklikt of iets gedownload?"** Dit bepaalt de urgentie.
- Vraag om de **originele mail als bijlage** door te sturen — niet alleen de tekst kopiëren
- Bij twijfel: de bot zet prioriteit automatisch op **High**
- Vraag nooit naar wachtwoorden of persoonsgegevens

#### AI questions
- Vraag welke AI-tool (Claude, Copilot, ChatGPT, eigen bot)
- Vraag wat de gebruiker probeert te bereiken (use case)
- Vraag of het een bug is of een functionele vraag

#### Domain transfer
- **Deadline moet minimaal 3 dagen in de toekomst liggen** — valideer dit proactief
- **DNS-dump is verplicht** — als de gebruiker die niet heeft, kan het ticket niet worden ingediend
- Vraag of email enabled is op het domein (MX-records)
- Vraag welke registrar (Combell of andere)

#### New employee
- Verzamel alle persoonsdata in één gestructureerde reeks vragen
- Vraag naar bedrijf én stad — voor groepen met meerdere vestigingen cruciaal
- Vraag type: Employee / Freelance / Student
- Vraag Blue Collar (arbeider) vs White Collar (bediende)
- Vraag of er specifieke software-toegangen nodig zijn (buiten de standaard onboarding)

#### Leaving user form
- **Vraag altijd eerst naar de laatste werkdag** — dit bepaalt de timing van alle acties
- Leg de GDPR-regels uit: "Na vertrek kan IT geen mailbox-toegang, forward of OneDrive-data delen zonder de toestemming van de vertrekkende gebruiker."
- Vraag expliciet: mailbox/OOO status, software-toegang, mobiele telefoon, badge, PC
- Vraag wat er met de PC moet gebeuren (wipen, hergebruiken, doorgeven)

#### Request Smartphone
- **Eerste vraag: "Werk je bij HR België?"** Zo niet → beleefd doorverwijzen
- Vraag nieuw of bestaand abonnement
- Vraag standaard smartphone of specifiek model
- Excel-bijlage met abonnementsinfo is vereist

### Prioriteitslogica

De gebruiker kiest geen prioriteit rechtstreeks — de bot leidt deze af uit impact + urgentie:

| Scope | Urgentie | → Prioriteit |
|---|---|---|
| Meerdere afdelingen / heel bedrijf | Kritisch | **Critical** |
| Hele afdeling | Kritisch / Hoog | **High** |
| Klein team (2–5) | Hoog / Normaal | **High** / **Medium** |
| Alleen ikzelf | Normaal | **Medium** |
| Alleen ikzelf | Laag | **Low** |

Bij security-incidenten of phishing waar geklikt werd → altijd minimaal **High**.

### Samenvatting-template

Voordat de bot het ticket indient, toont hij altijd deze samenvatting:

```
📋 TICKET SAMENVATTING
──────────────────────────────────────────
Categorie:      [Common IT requests / Employee related requests]
Subcategorie:   [specifiek ticket type]
Prioriteit:     [Critical / High / Medium / Low]
Samenvatting:   [1 zin: SYSTEEM — Probleem — Impact]

Beschrijving:
  WAT:              [concrete omschrijving]
  WANNEER:          [datum/tijdstip]
  SYSTEEM:          [betrokken systeem/toestel]
  FOUTMELDING:      [exact of 'geen']
  AL GEPROBEERD:    [acties + resultaat of 'niets']
  IMPACT:           [aantal personen / scope]

Aanvrager:      [naam] | [e-mail] | [bedrijf]
Bijlagen:       [aantal + type]
──────────────────────────────────────────
Klopt alles? Wil je nog iets aanpassen?
```

### Foutafhandeling

- **Onvolledig antwoord?** → Vraag door, ga nooit verder met vage informatie
- **Buiten IT-scope?** → "Daar kan ik je helaas niet mee helpen — mijn taak is enkel IT-supporttickets aanmaken."
- **Gebruiker wil stoppen?** → "Geen probleem! Kom gerust later terug."
- **Gebruiker heeft geen goedkeuring manager?** → Suggereer om manager in CC te zetten ("Share with") zodat die kan bevestigen

### Integratie met Smart Assign

De bot hoeft **zelf geen assignee te kiezen** — Smart Assign doet dit automatisch na indiening op basis van:
- Ticketcategorie en -inhoud
- Historische resolutie-patronen
- Huidige workload van agents
- Specialisatie (zie `ITS_assignees_reporters.md`)

De bot kan wel aan de gebruiker laten weten dat deze routing automatisch gebeurt en dat hij/zij een Teams-notificatie krijgt zodra de assignee is bepaald.

---

## Referenties

| Document | Doel |
|---|---|
| `SYSTEM_PROMPT_IT_HELPDESK_BOT.md` | System prompt voor de Claude chatbot (intake-gedrag) |
| `KB-TICKET-CREATION-FLOW.md` | Gebruikershandleiding voor ticketaanmaak |
| `ITS_assignees_reporters.md` | Lijst van alle Jira assignees en reporters |
| `top10_infra_tickets.md` | Meest voorkomende infra-ticketcategorieën |
| `KB-AX3-Errors-Troubleshooting.md` | Axapta 3 error codes en oplossingen |
| `KB-D365-Errors.md` | Dynamics 365 error codes en oplossingen |

| URL | Doel |
|---|---|
| https://polletgroup.atlassian.net/servicedesk | Pollet Group Support Portal |
| https://polletgroup.atlassian.net | Jira Service Management (ITS-project) |

---