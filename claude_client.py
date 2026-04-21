import os
import httpx
import anthropic
from pathlib import Path
from dotenv import load_dotenv
from tool_definitions import TOOLS
from tools import dispatch_tool

load_dotenv(Path(__file__).parent / ".env", override=True)

SYSTEM_PROMPT = """Je bent een AI-assistent voor het Sterima support team. Je helpt medewerkers met:
- Jira tickets onderzoeken, aanmaken en toewijzen
- Oplossingen zoeken in Confluence
- Kennisartikelen schrijven

Richtlijnen:
- Antwoord altijd in het Nederlands, beknopt (max 3-4 bullet points)
- Bij ALLE schrijfacties (create_ticket, assign_ticket, add_comment, update_status, create_confluence_page): zet ALTIJD requires_confirmation=true
- Toon bij Smart Assign altijd een confidence % met uitleg
- Vermeld altijd de bron (ticket ID, Confluence URL) bij je antwoord

Oplossing zoeken:
- Zoek altijd in BEIDE bronnen: search_jira (opgeloste tickets) én search_confluence (kennisbank)
- Combineer gevonden oplossingen en vermeld de bron (ticket ID of Confluence URL)
- Als niets gevonden in beide bronnen: stel voor om een nieuw Jira ticket aan te maken
- Vraag altijd bevestiging vóór je het ticket aanmaakt"""

WRITE_TOOLS = {"assign_ticket", "add_comment", "update_status", "create_confluence_page", "create_ticket"}


def requires_confirmation(tool_use: dict) -> bool:
    return (
        tool_use.get("name") in WRITE_TOOLS
        and tool_use.get("input", {}).get("requires_confirmation") is True
    )


class ClaudeClient:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            http_client=httpx.Client(verify=False)
        )
        self.model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")

    def chat(self, messages: list) -> dict:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"}
                }
            ],
            tools=TOOLS,
            messages=messages,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )

        if response.stop_reason == "tool_use":
            tool_blocks = [b for b in response.content if b.type == "tool_use"]
            assistant_content = [
                {"type": "tool_use", "id": b.id, "name": b.name, "input": b.input}
                if b.type == "tool_use" else {"type": "text", "text": b.text}
                for b in response.content
            ]

            confirm_block = next(
                (b for b in tool_blocks if requires_confirmation({"name": b.name, "input": b.input})), None
            )
            if confirm_block:
                return {
                    "type": "confirmation_required",
                    "tool_name": confirm_block.name,
                    "tool_id": confirm_block.id,
                    "tool_input": confirm_block.input,
                    "assistant_content": assistant_content,
                    "messages_at_confirmation": messages,
                    "message": f"Wil je dat ik **{confirm_block.name}** uitvoer met: {confirm_block.input}?"
                }

            tool_results = [
                {"type": "tool_result", "tool_use_id": b.id, "content": str(dispatch_tool(b.name, b.input))}
                for b in tool_blocks
            ]
            follow_up = messages + [
                {"role": "assistant", "content": assistant_content},
                {"role": "user", "content": tool_results}
            ]
            return self.chat(follow_up)

        text = next((b.text for b in response.content if b.type == "text"), "")
        return {"type": "text", "text": text}

    def execute_confirmed_tool(self, tool_name: str, tool_id: str, tool_input: dict, messages_at_confirmation: list, assistant_content: list) -> dict:
        confirmed_result = dispatch_tool(tool_name, tool_input)
        tool_results = []
        for block in assistant_content:
            if block["type"] != "tool_use":
                continue
            if block["id"] == tool_id:
                tool_results.append({"type": "tool_result", "tool_use_id": tool_id, "content": str(confirmed_result)})
            else:
                other = dispatch_tool(block["name"], block["input"])
                tool_results.append({"type": "tool_result", "tool_use_id": block["id"], "content": str(other)})
        follow_up = messages_at_confirmation + [
            {"role": "assistant", "content": assistant_content},
            {"role": "user", "content": tool_results}
        ]
        return self.chat(follow_up)
