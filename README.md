# 1. Project Structure

venketesh_aus-public-holiday/
│
├── api_handler.py                    
├── public_holiday_handler.py         
├── main.py                           
│
├── tests/
│   ├── __init__.py
│   ├── test_api_handler.py        
│   └── test_public_holiday_handler.py 
│
├── requirements.txt               
├── README.md                         
├── .gitignore                       
└── australian_public_holidays.csv    

# 2. Setup Instructions

## Prerequisites:
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps:

1. Clone the repository:
   git clone https://github.com/VenketeshPratap/venketesh_aus-public-holiday.git
   cd venketesh_aus-public-holiday

2. Create virtual environment (recommended):
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

## Dependencies (requirements.txt):
requests==2.31.0
pandas==2.2.0
pytest==8.0.0

# 4. How to Run the Application

## Running the Main Script:

python main.py

## Expected Output:
- Console output showing first 5 rows of data
- CSV file created: australian_public_holidays.csv

## Running Unit Tests:

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_api_handler.py -v

## Expected Test Results:
- All tests should pass
- Coverage: 95%+
