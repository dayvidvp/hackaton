# Ticket Creation Wizard per Department — Design Spec
**Date:** 2026-04-21
**Project:** Pollet AI — Sterima/Pollet Hackathon

---

## Overview

A guided ticket creation wizard that walks users through department-specific questions inline in the chat. Each department (ITS, OPS, etc.) has its own question script stored as a markdown file. Admins can manage these scripts via the admin page without touching code.

---

## 1. Data & Storage

Department scripts live in `docs/departments/` — one `.md` file per department:

```
docs/departments/
  ITS.md
  OPS.md
  ...
```

**File format:**
```markdown
# ITS — Ticket vragen

1. Wat is het betrokken systeem of de applicatie?
2. Beschrijf het probleem zo concreet mogelijk.
3. Sinds wanneer doet het probleem zich voor?
4. Hoeveel gebruikers worden getroffen?
5. Is er al iets geprobeerd om het op te lossen?
```

- The display name is read from the first `#` heading.
- The file name is the department name in lowercase + `.md` (e.g. `its.md`).
- No database required — plain files, editable by admins.

---

## 2. Wizard Flow

### Trigger
- **Button:** A "Nieuw ticket" button in the chat header always available.
- **Claude detection:** When Claude detects ticket creation intent and calls `create_ticket` without the wizard having run, the backend returns `{"type": "start_wizard"}` instead of executing the tool. The frontend starts the wizard with the detected department pre-selected if available.

### Step-by-step (inline in chat)
```
Bot:  "Voor welke afdeling is dit ticket?"
      [ITS]  [OPS]  [...]   ← clickable chips

User clicks "ITS"

Bot:  "Vraag 1/5: Wat is het betrokken systeem of de applicatie?"
      [Annuleren]
User: types answer → Enter

Bot:  "Vraag 2/5: Beschrijf het probleem zo concreet mogelijk."
...

Bot:  "Vraag 5/5: Is er al iets geprobeerd?"
User: types answer

→ Frontend collects all answers, sends ONE request to Claude:
  "Maak een ticket aan voor ITS met de volgende informatie:
   - Systeem: [answer 1]
   - Probleem: [answer 2]
   - Sinds: [answer 3]
   - Getroffen gebruikers: [answer 4]
   - Al geprobeerd: [answer 5]"

Claude: shows summary + confirmation dialog (requires_confirmation=true)
User confirms → ticket created in Jira
```

### Wizard state (in `chat.js`)
```js
wizardState = {
  active: false,
  department: null,
  questions: [],   // parsed from markdown
  answers: [],
  currentStep: 0
}
```

During an active wizard:
- The send button processes wizard answers, not normal chat messages.
- An "Annuleren" chip is shown after each question.
- Cancelling resets `wizardState` and returns to normal chat.

---

## 3. Backend API

New routes added to `app.py`:

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/api/departments` | List all department names (from `docs/departments/*.md`) |
| `GET` | `/api/departments/<name>` | Return markdown content of one department script |
| `POST` | `/admin/departments/save` | Save/create a department script (admin only) |
| `DELETE` | `/admin/departments/<name>` | Delete a department script (admin only) |

**Helper function** `parse_questions(markdown: str) -> list[str]` extracts numbered questions (lines matching `^\d+\.`). Used by the frontend after fetching the department script.

**Claude intent detection:** If Claude calls `create_ticket` during normal chat (wizard was not active), the `/chat` endpoint checks whether the wizard should have run first. If so, it returns:
```json
{"type": "start_wizard", "suggested_department": "ITS"}
```
The frontend catches this and starts the wizard with `ITS` pre-selected.

---

## 4. Admin Page — "Afdelingen" Tab

A new tab added to `admin.html` alongside the existing "Prompts" tab.

**Tab layout:**
```
[ Prompts ]  [ Afdelingen ]

Afdelingen:
  ITS    [Bewerken]  [Verwijderen]
  OPS    [Bewerken]  [Verwijderen]
  [+ Nieuwe afdeling]

Inline editor (on Bewerken):
  Naam: [ ITS          ]
  ┌─────────────────────────────────┐
  │ # ITS — Ticket vragen           │
  │                                 │
  │ 1. Wat is het systeem?          │
  │ 2. Beschrijf het probleem.      │
  └─────────────────────────────────┘
  [Opslaan]  [Annuleren]
```

- Admin-only: non-admin users cannot access `/admin`.
- The file name is derived from the "Naam" field (lowercase, spaces → underscores).
- "Verwijderen" shows a confirmation prompt before deleting.

---

## 5. Error Handling

- If `docs/departments/` is empty: the department selection step shows "Geen afdelingen geconfigureerd — contacteer een admin."
- If a department file is malformed (no numbered questions found): fallback to a single open-ended question: "Beschrijf het probleem."
- Network error during wizard: show error message, keep wizard state so user can retry.
- Cancel at any step: reset wizard, post "Ticketaanmaak geannuleerd." as bot message.

---

## 6. Files Changed

| File | Change |
|------|--------|
| `app.py` | Add `/api/departments`, `/admin/departments/save`, `/admin/departments/<name>` routes |
| `static/chat.js` | Add wizard state machine, department chip UI, question flow, answer collection |
| `templates/chat.html` | Add "Nieuw ticket" button in header |
| `templates/admin.html` | Add "Afdelingen" tab with inline editor |
| `docs/departments/*.md` | New directory with initial department scripts (ITS, OPS) |
| `claude_client.py` | No changes needed — wizard sends a normal `create_ticket` call at the end |
