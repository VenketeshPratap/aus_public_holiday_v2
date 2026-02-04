import pandas as pd
from public_holiday_handler import PublicHolidayHandler


class MockAPIHandler:
    def fetch_data(self, resource_id, limit):
        return {
            "success": True,
            "result": {
                "records": [
                    {"date": "2024-01-01", "name": "New Year"},
                    {"date": "2024-01-26", "name": "Australia Day"},
                ]
            },
        }


def test_dataframe_creation():
    handler = PublicHolidayHandler(
        api_handler=MockAPIHandler(),
        resource_id="dummy",
        limit=2,
    )

    df = handler.to_dataframe()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2


def test_save_to_csv(tmp_path):
    """
    Test that CSV file is created successfully.
    """

    class MockAPIHandler:
        def fetch_data(self, resource_id, limit):
            return {
                "success": True,
                "result": {
                    "records": [
                        {"date": "2024-01-01", "name": "New Year"}
                    ]
                },
            }

    handler = PublicHolidayHandler(
        api_handler=MockAPIHandler(),
        resource_id="dummy",
        limit=1,
    )

    file_path = tmp_path / "holidays.csv"
    handler.save_to_csv(str(file_path))

    assert file_path.exists()


def test_dataframe_columns():
    """
    Test that expected columns exist in DataFrame.
    """

    class MockAPIHandler:
        def fetch_data(self, resource_id, limit):
            return {
                "success": True,
                "result": {
                    "records": [
                        {"date": "2024-01-01", "name": "New Year"}
                    ]
                },
            }

    handler = PublicHolidayHandler(
        api_handler=MockAPIHandler(),
        resource_id="dummy",
        limit=1,
    )

    df = handler.to_dataframe()

    assert "date" in df.columns
    assert "name" in df.columns
