from api_handler import APIHandler
from public_holiday_handler import PublicHolidayHandler


def main():
    BASE_URL = "https://data.gov.au/data/api/action"
    RESOURCE_ID = "d256f989-8f49-46eb-9770-1c6ee9bd2661"

    api_handler = APIHandler(BASE_URL)

    holiday_handler = PublicHolidayHandler(
        api_handler=api_handler,
        resource_id=RESOURCE_ID,
        limit=1000,
    )

    df = holiday_handler.to_dataframe()

    # Print first 5 rows
    print(df.head())

    # Save full table as CSV
    holiday_handler.save_to_csv(
        "australian_public_holidays.csv"
    )


if __name__ == "__main__":
    main()
