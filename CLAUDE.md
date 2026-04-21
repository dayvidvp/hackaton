# Unified AI Workspace Assistant — Microsoft Teams Bot
**AI Hackathon 2026**

## Project Overview

A Microsoft Teams Bot that acts as a single AI-powered interface across Jira, Confluence, Dynamics 365, and Azure AD. Support agents, developers, and sales teams interact in natural language — the bot handles ticket creation, smart assignment, solution lookup, and knowledge publishing.

## Problem Statement

- Support spends 15–30 min/ticket searching Confluence manually
- Jira tickets arrive incomplete — developers lack context and resolution direction
- Customer info is scattered across Dynamics, email, and tickets
- Resolved problems are not documented for future reuse

## Solution — 5 Live Demo Scenarios

1. **Jira Overview** — Bot shows open tickets, flags unassigned ones
2. **Ticket + Smart Assign** — New ticket → history analyzed → correct person assigned
3. **Solution Search** — Claude compares with history → concrete approach with success probability
4. **Auto-Resolve** — Analyze ticket, assign, add solution + status update in one step
5. **Knowledge Capture** — Solution → knowledge article auto-published to Confluence

## Smart Assign Logic

Claude analyzes each new ticket against:
- Ticket content, component, and error type
- History: who solved this type of problem before?
- Average resolution time per person
- Current workload and availability

**Output per ticket:**
- Best candidate with confidence %
- Alternative if first choice unavailable
- Ready-made solution proposal as a comment
- Direct Teams notification to the assignee

## Technical Stack

| Component | Technology |
|---|---|
| AI Engine | Claude API — Anthropic (claude-sonnet-4-6 or claude-opus-4-7) |
| Ticket & Docs | Atlassian MCP — Jira + Confluence (native read/write) |
| sharepoint > MCP? |
| Chat Interface | Microsoft Teams Bot Framework |
| Auth | Azure AD — existing infrastructure |
| CRM | Dynamics 365 connector (or mock data for demo) |

## Key Guidelines for Claude

- Always use the latest Claude model: `claude-sonnet-4-6` for speed, `claude-opus-4-7` for complex reasoning
- Use **prompt caching** for repeated Jira/Confluence context (reduces latency and cost)
- Keep Teams messages concise — max 3–4 bullet points per response
- Smart Assign confidence % must be explainable (show reasoning, not just a number)
- All Jira writes must be confirmed before execution (no silent mutations)
- Dynamics 365 data: use mock data if live connector is unavailable during demo

## Demo Day Target

- Platform: Claude AI — Anthropic
- Team size: 4–5 people
- Date: March 2026
- Format: 5-scenario live demo flow

## Business Value per Department

| Department | Value |
|---|---|
| Support | Faster response times |
| Development | Full context + solution with every ticket |
| CRM / Sales | 360° customer view in seconds |
| IT / Azure | Native Azure AD + MCP integration |
| Management | Fewer silos, shorter lead times |
| Everyone | Knowledge preserved and reusable |
