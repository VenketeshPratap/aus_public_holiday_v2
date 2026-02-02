import requests
from typing import Dict, Any


class APIHandler:
    """
    Handles communication with the Australian Government CKAN API.
    """

    def __init__(self, base_url: str):
        """
        Initialize APIHandler with base API URL.

        :param base_url: Base CKAN API URL
        """
        self.base_url = base_url.rstrip("/")

    def fetch_data(
        self, resource_id: str, limit: int
    ) -> Dict[str, Any]:
        """
        Fetch data from CKAN datastore_search endpoint.

        :param resource_id: CKAN resource ID
        :param limit: Number of rows to retrieve
        :return: JSON response
        """
        url = f"{self.base_url}/datastore_search"
        params = {
            "resource_id": resource_id,
            "limit": limit,
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            raise RuntimeError("Failed to fetch data from API")

        data = response.json()

        if not data.get("success"):
            raise RuntimeError("API returned unsuccessful response")

        return data
