import json, os, requests
from pathlib import Path

def _base(): return os.getenv("CONFLUENCE_BASE_URL", "")
def _auth(): return (os.getenv("JIRA_EMAIL", ""), os.getenv("JIRA_API_TOKEN", ""))
def _headers(): return {"Accept": "application/json", "Content-Type": "application/json"}

def _mock_data():
    path = Path(__file__).parent.parent / "fixtures" / "confluence_mock.json"
    return json.loads(path.read_text())

def search_confluence(query: str) -> list:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        pages = _mock_data()["pages"]
        q = query.lower()
        return [p for p in pages if q in p["title"].lower() or q in p["body"].lower()] or pages[:2]
    base = _base()
    resp = requests.get(
        f"{base}/rest/api/content/search",
        headers=_headers(), auth=_auth(),
        params={"cql": f'text ~ "{query}" AND type=page', "limit": 5, "expand": "body.storage"}
    )
    resp.raise_for_status()
    results = resp.json().get("results", [])
    return [
        {
            "id": r["id"],
            "title": r["title"],
            "body": r.get("body", {}).get("storage", {}).get("value", "")[:500],
            "url": base + r.get("_links", {}).get("webui", "")
        }
        for r in results
    ]

def create_confluence_page(title: str, content: str, space_key: str, requires_confirmation: bool = True) -> dict:
    base = _base()
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        return {"success": True, "title": title, "url": f"{base}/spaces/{space_key}/pages/mock-new"}
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": content, "representation": "storage"}}
    }
    resp = requests.post(f"{base}/rest/api/content", headers=_headers(), auth=_auth(), json=payload)
    resp.raise_for_status()
    data = resp.json()
    return {
        "success": True,
        "title": title,
        "url": base + data.get("_links", {}).get("webui", "")
    }
