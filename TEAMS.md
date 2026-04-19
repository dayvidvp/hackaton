# Team Breakdown — Unified AI Workspace Assistant

## Team Overzicht (4–5 personen)

---

## Team 1 — AI & Claude Integratie
**Verantwoordelijkheid:** Het brein van de bot — Claude API, Smart Assign logica, prompts

### Taken
- [ ] Claude API setup met prompt caching
- [ ] Smart Assign prompt engineering (confidence %, alternatief, oplossingsvoorstel)
- [ ] Solution Search: Claude vergelijkt nieuw ticket met historiek
- [ ] Auto-Resolve flow: één prompt die analyseert, assigned én oplossing schrijft
- [ ] Kennisartikel generatie vanuit opgeloste tickets
- [ ] Model keuze bewaken: `claude-sonnet-4-6` (snelheid) vs `claude-opus-4-7` (complexe redenering)

### Output
- Werkende Claude API client met caching
- Prompt templates voor alle 5 demo-scenario's
- Smart Assign module met explainability

---

## Team 2 — Atlassian Integratie (Jira + Confluence)
**Verantwoordelijkheid:** Lezen en schrijven naar Jira en Confluence via MCP

### Taken
- [ ] Atlassian MCP server configureren
- [ ] Jira: ophalen van open tickets, filteren op niet-toegewezen
- [ ] Jira: nieuw ticket aanmaken met juiste velden
- [ ] Jira: assignee instellen + comment toevoegen (oplossing)
- [ ] Jira: status updaten (bijv. "In Progress" → "Resolved")
- [ ] Confluence: zoeken in kennisbank voor Solution Search
- [ ] Confluence: nieuw kennisartikel schrijven na Auto-Resolve
- [ ] Confirmation flow implementeren (geen silent writes)

### Output
- Atlassian MCP connectie operationeel
- CRUD operaties op Jira tickets
- Read/Write op Confluence pagina's

---

## Team 3 — Microsoft Teams Bot & Azure AD
**Verantwoordelijkheid:** De chatinterface en authenticatie

### Taken
- [ ] Teams Bot registreren via Azure Bot Service
- [ ] Bot Framework SDK setup (Node.js of Python)
- [ ] Conversatie flow implementeren (gebruiker typt → bot reageert)
- [ ] Azure AD Single Sign-On integreren
- [ ] Adaptive Cards opmaken voor ticket overzichten en smart assign resultaten
- [ ] Notificaties sturen naar assignee via Teams
- [ ] Foutafhandeling en fallback messages

### Output
- Werkende Teams Bot in testkanaal
- Azure AD authenticatie
- Geformatteerde Adaptive Card responses

---

## Team 4 — Dynamics 365 & Demo Data
**Verantwoordelijkheid:** Klantdata en demo-voorbereiding

### Taken
- [ ] Dynamics 365 connector onderzoeken / mock data voorbereiden
- [ ] 360° klantview samenstellen (naam, contract, openstaande tickets, laatste interactie)
- [ ] Realistische testdata aanmaken in Jira (tickets met historiek, verschillende assignees)
- [ ] Confluence testpagina's aanmaken voor kennisbank
- [ ] Demo script schrijven voor alle 5 scenario's
- [ ] Fallback mock responses voorbereiden als live systemen uitvallen
- [ ] Demo presentatie slide deck (optioneel)

### Output
- Mock klantdata klaar voor demo
- Volledige Jira + Confluence testomgeving
- Demo script en fallback plan

---

## Gedeelde Verantwoordelijkheden

| Taak | Wie |
|---|---|
| GitHub repo beheer | Team 1 + Team 3 |
| Code reviews | Iedereen (PR per team) |
| Demo dry run | Alle teams samen |
| Documentatie in CLAUDE.md bijhouden | Team 1 |

---

## Tijdlijn Hackathon

| Fase | Activiteit |
|---|---|
| Uur 1–2 | Setup: repos, credentials, MCP config |
| Uur 3–5 | Core integraties bouwen (parallel per team) |
| Uur 6–7 | End-to-end koppeling: bot → Claude → Jira/Confluence |
| Uur 8 | Demo scenario's testen + debuggen |
| Uur 9 | Dry run demo flow |
| Uur 10 | Buffer + presentatie voorbereiding |

---

## Definition of Done (per scenario)

- [ ] **Scenario 1:** Bot toont Jira-overzicht met niet-toegewezen tickets gemarkeerd
- [ ] **Scenario 2:** Nieuw ticket → Smart Assign met confidence % zichtbaar in Teams
- [ ] **Scenario 3:** Bot geeft oplossingsvoorstel met slaagkans op basis van historiek
- [ ] **Scenario 4:** Auto-Resolve voltooit ticket end-to-end in één Teams-bericht
- [ ] **Scenario 5:** Oplossing gepubliceerd als kennisartikel in Confluence
