import pytest
from api_handler import APIHandler


def test_api_handler_invalid_url():
    api_handler = APIHandler("https://invalid-url")

    with pytest.raises(Exception):
        api_handler.fetch_data(
            resource_id="dummy",
            limit=5,
        )
