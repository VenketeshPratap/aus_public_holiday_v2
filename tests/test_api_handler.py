import pytest
import requests
from api_handler import APIHandler


def test_api_handler_invalid_url():
    api_handler = APIHandler("https://invalid-url")

    with pytest.raises(Exception):
        api_handler.fetch_data(
            resource_id="dummy",
            limit=5,
        )


def test_api_handler_success(monkeypatch):
    """
    Test that APIHandler returns JSON data on successful API call.
    """

    class MockResponse:
        status_code = 200

        def json(self):
            return {"success": True, "result": {"records": []}}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    api_handler = APIHandler("https://fake-url")
    data = api_handler.fetch_data("dummy", limit=5)

    assert data["success"] is True

