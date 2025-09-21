# FDA_SCRAPPER

FDA_SCRAPPER is a FastAPI-based web service that automates the process of gathering and refining data from FDA device databases. Instead of manual searches and tedious data extraction, this Python tool provides a REST API to fetch, clean, and return FDA device information with just HTTP requests.

## What It Does

- Connects to FDA device databases and extracts data automatically
- Searches for medical devices by name and optional product code
- Filters results by minimum report year
- Returns structured JSON data for easy integration
- Provides interactive API documentation

## Setup Instructions

### Prerequisites

- Python 3.8 or newer
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone https://github.com/raghusai-09/FDA_TPLC_WebScraper.git
   cd FDA_SCRAPPER
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the App Locally

1. **Start the FastAPI server**:
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Alternative way to start**:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## How to Test Using Interactive Documentation

FastAPI automatically generates interactive API documentation:

1. **Open your browser** and navigate to:
   ```
   http://localhost:8000/docs
   ```

2. **Use the Swagger UI** to test the API:
   - Click on the `/scrape` endpoint
   - Click "Try it out"
   - Fill in the parameters (see examples below)
   - Click "Execute" to see the results

3. **Alternative documentation** (ReDoc format):
   ```
   http://localhost:8000/redoc
   ```

## Example Usage

### Example 1: Basic Device Search
Search for syringes with default parameters:
```
device_name: syringe
```

### Example 2: Device Search with Product Code
Search for syringes with a specific product code:
```
device_name: syringe
product_code: LZH
min_year: 2020
```

### Example 3: Using cURL
```bash
curl -X GET "http://localhost:8000/scrape?device_name=syringe&min_year=2020"
```

### Example 4: Using Python requests
```python
import requests

response = requests.get(
    "http://localhost:8000/scrape",
    params={
        "device_name": "syringe",
        "min_year": 2020
    }
)
data = response.json()
print(data)
```

## API Parameters

- **device_name** (required): The name of the medical device to search for
- **product_code** (optional): FDA product code for more specific searches
- **min_year** (optional): Minimum report year to filter results (default: 2020)

## License & Contributions

FDA_SCRAPPER is MIT licensed. Contributions are welcome—just open an issue or submit a pull request.

## Questions?

Reach out at [your.email@example.com](mailto:your.email@example.com).

