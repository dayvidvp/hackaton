import os, pytest
from unittest.mock import patch, MagicMock

os.environ.setdefault("CONFLUENCE_BASE_URL", "https://test.atlassian.net/wiki")
os.environ.setdefault("JIRA_EMAIL", "test@test.com")
os.environ.setdefault("JIRA_API_TOKEN", "fake-token")
os.environ.setdefault("CONFLUENCE_SPACE_KEY", "PROJ")
os.environ.setdefault("USE_MOCK_DATA", "false")

from tools.confluence_tools import search_confluence, create_confluence_page


def mock_resp(data, status=200):
    m = MagicMock()
    m.status_code = status
    m.json.return_value = data
    m.raise_for_status = MagicMock()
    return m


def test_search_confluence_returns_list():
    fake = {"results": [{"id": "1", "title": "Test", "body": {"storage": {"value": "inhoud"}}, "_links": {"webui": "/page/1"}}]}
    with patch("tools.confluence_tools.requests.get", return_value=mock_resp(fake)):
        result = search_confluence(query="login")
    assert isinstance(result, list)
    assert result[0]["title"] == "Test"


def test_create_confluence_page_returns_url():
    fake = {"id": "999", "_links": {"webui": "/page/999"}}
    with patch("tools.confluence_tools.requests.post", return_value=mock_resp(fake)):
        result = create_confluence_page(title="Test", content="<p>test</p>", space_key="PROJ")
    assert "url" in result


def test_search_confluence_mock_fallback(monkeypatch):
    monkeypatch.setenv("USE_MOCK_DATA", "true")
    result = search_confluence(query="login")
    assert isinstance(result, list)
    assert len(result) > 0
