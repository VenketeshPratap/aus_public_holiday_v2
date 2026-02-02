import pandas as pd
from api_handler import APIHandler


class PublicHolidayHandler:
    """
    Prepares public holiday data for analysis.
    """

    def __init__(
        self,
        api_handler: APIHandler,
        resource_id: str,
        limit: int = 1000,
    ):
        """
        Initialize handler and retrieve public holiday data.

        :param api_handler: APIHandler instance
        :param resource_id: CKAN resource ID
        :param limit: Number of rows to fetch
        """
        try:
            self.raw_data = api_handler.fetch_data(
                resource_id=resource_id,
                limit=limit,
            )
        except Exception as exc:
            raise RuntimeError(
                "Failed to retrieve public holiday data"
            ) from exc

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert public holiday JSON data to Pandas DataFrame.

        :return: Pandas DataFrame
        """
        records = self.raw_data["result"]["records"]
        return pd.DataFrame(records)

    def save_to_csv(self, file_path: str) -> None:
        """
        Save public holiday data as CSV.

        :param file_path: Output CSV file path
        """
        df = self.to_dataframe()
        df.to_csv(file_path, index=False)
