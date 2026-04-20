import json, os, requests
from pathlib import Path

CONF_BASE = os.getenv("CONFLUENCE_BASE_URL", "")
AUTH = (os.getenv("JIRA_EMAIL", ""), os.getenv("JIRA_API_TOKEN", ""))
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}
USE_MOCK = os.getenv("USE_MOCK_DATA", "false").lower() == "true"

def _mock_data():
    path = Path(__file__).parent.parent / "fixtures" / "confluence_mock.json"
    return json.loads(path.read_text())

def search_confluence(query: str) -> list:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        pages = _mock_data()["pages"]
        q = query.lower()
        return [p for p in pages if q in p["title"].lower() or q in p["body"].lower()] or pages[:2]
    resp = requests.get(
        f"{CONF_BASE}/rest/api/content/search",
        headers=HEADERS, auth=AUTH,
        params={"cql": f'text ~ "{query}" AND type=page', "limit": 5, "expand": "body.storage"}
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return [
        {
            "id": r["id"],
            "title": r["title"],
            "body": r.get("body", {}).get("storage", {}).get("value", "")[:500],
            "url": CONF_BASE + r.get("_links", {}).get("webui", "")
        }
        for r in results
    ]

def create_confluence_page(title: str, content: str, space_key: str, requires_confirmation: bool = True) -> dict:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        return {"success": True, "title": title, "url": f"{CONF_BASE}/spaces/{space_key}/pages/mock-new"}
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": content, "representation": "storage"}}
    }
    resp = requests.post(f"{CONF_BASE}/rest/api/content", headers=HEADERS, auth=AUTH, json=payload)
    resp.raise_for_status()
    data = resp.json()
    return {
        "success": True,
        "title": title,
        "url": CONF_BASE + data.get("_links", {}).get("webui", "")
    }
