import json, os, requests
from pathlib import Path

TENANT_ID = os.getenv("AZURE_TENANT_ID", "")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET", "")
SITE_ID = os.getenv("SHAREPOINT_SITE_ID", "")
USE_MOCK = os.getenv("USE_MOCK_DATA", "false").lower() == "true"

def _mock_data():
    path = Path(__file__).parent.parent / "fixtures" / "sharepoint_mock.json"
    return json.loads(path.read_text())

def _get_graph_token() -> str:
    resp = requests.post(
        f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token",
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "scope": "https://graph.microsoft.com/.default"
        }
    )
    resp.raise_for_status()
    return resp.json()["access_token"]

def search_sharepoint(query: str) -> list:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        docs = _mock_data()["documents"]
        q = query.lower()
        return [d for d in docs if q in d["name"].lower() or q in d["summary"].lower()] or docs[:2]
    token = _get_graph_token()
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    resp = requests.get(
        f"https://graph.microsoft.com/v1.0/sites/{SITE_ID}/drive/root/search(q='{query}')",
        headers=headers, params={"$select": "name,id,webUrl,lastModifiedDateTime", "$top": 5}
    )
    resp.raise_for_status()
    items = resp.json().get("value", [])
    return [
        {
            "id": i["id"],
            "name": i["name"],
            "url": i.get("webUrl", ""),
            "last_modified": i.get("lastModifiedDateTime", "")
        }
        for i in items
    ]

def get_document(document_id: str) -> dict:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        docs = _mock_data()["documents"]
        return next((d for d in docs if d["id"] == document_id), {})
    token = _get_graph_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"https://graph.microsoft.com/v1.0/sites/{SITE_ID}/drive/items/{document_id}", headers=headers)
    resp.raise_for_status()
    return resp.json()

def list_site_pages() -> list:
    if os.getenv("USE_MOCK_DATA", "false").lower() == "true":
        return _mock_data()["documents"]
    token = _get_graph_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"https://graph.microsoft.com/v1.0/sites/{SITE_ID}/pages", headers=headers)
    resp.raise_for_status()
    return resp.json().get("value", [])
