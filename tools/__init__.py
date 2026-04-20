from tools.jira_tools import (
    get_open_tickets, get_resolved_tickets, create_ticket,
    assign_ticket, add_comment, update_status
)
from tools.confluence_tools import search_confluence, create_confluence_page
from tools.sharepoint_tools import search_sharepoint, get_document, list_site_pages

TOOL_FUNCTIONS = {
    "get_open_tickets": get_open_tickets,
    "get_resolved_tickets": get_resolved_tickets,
    "create_ticket": create_ticket,
    "assign_ticket": assign_ticket,
    "add_comment": add_comment,
    "update_status": update_status,
    "search_confluence": search_confluence,
    "create_confluence_page": create_confluence_page,
    "search_sharepoint": search_sharepoint,
}

def dispatch_tool(name: str, inputs: dict) -> dict:
    fn = TOOL_FUNCTIONS.get(name)
    if not fn:
        return {"error": f"Onbekende tool: {name}"}
    return fn(**inputs)
