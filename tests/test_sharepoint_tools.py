import os, pytest
from unittest.mock import patch, MagicMock

os.environ.setdefault("AZURE_TENANT_ID", "fake-tenant")
os.environ.setdefault("AZURE_CLIENT_ID", "fake-client")
os.environ.setdefault("AZURE_CLIENT_SECRET", "fake-secret")
os.environ.setdefault("SHAREPOINT_SITE_ID", "fake-site")
os.environ.setdefault("USE_MOCK_DATA", "false")

from tools.sharepoint_tools import search_sharepoint, _get_graph_token


def mock_resp(data, status=200):
    m = MagicMock()
    m.status_code = status
    m.json.return_value = data
    m.raise_for_status = MagicMock()
    return m


def test_search_sharepoint_returns_list():
    token_resp = {"access_token": "fake-token"}
    search_resp = {"value": [{"name": "Test.docx", "id": "1", "webUrl": "https://sp.com/test", "lastModifiedDateTime": "2026-01-01"}]}
    with patch("tools.sharepoint_tools.requests.post", return_value=mock_resp(token_resp)):
        with patch("tools.sharepoint_tools.requests.get", return_value=mock_resp(search_resp)):
            result = search_sharepoint(query="API")
    assert isinstance(result, list)


def test_search_sharepoint_mock_fallback(monkeypatch):
    monkeypatch.setenv("USE_MOCK_DATA", "true")
    result = search_sharepoint(query="handleiding")
    assert isinstance(result, list)
    assert len(result) > 0
