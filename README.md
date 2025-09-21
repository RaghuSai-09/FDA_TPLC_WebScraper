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
   cd FDA_TPLC_WebScraper
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

## Example API Response

When you search for `device_name=injector and syringe, angiographic`, the API returns structured data including device information, device problems, and patient problems with their respective counts and links to detailed FDA MAUDE reports:

```json
{
  "device_name": "injector and syringe, angiographic",
  "results": [
    {
      "detail_page": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm?id=957&min_report_year=2020",
      "device_name": "injector and syringe, angiographic, balloon inflation, reprocessed",
      "device_problems": [],
      "patient_problems": []
    },
    {
      "detail_page": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm?id=2719&min_report_year=2020",
      "device_name": "injector and syringe, angiographic, reprocessed",
      "device_problems": [],
      "patient_problems": []
    },
    {
      "detail_page": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm?id=2716&min_report_year=2020",
      "device_name": "injector and syringe, angiographic",
      "device_problems": [
        {
          "problem_name": "Adverse Event Without Identified Device or Use Problem",
          "count": 220,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&productproblem=2993&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Insufficient Information",
          "count": 44,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&productproblem=3190&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Manufacturing, Packaging or Shipping Problem",
          "count": 33,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&productproblem=2975&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Break",
          "count": 29,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&productproblem=1069&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        }
      ],
      "patient_problems": [
        {
          "problem_name": "No Clinical Signs, Symptoms or Conditions",
          "count": 272,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&patientproblem=4582&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Air Embolism",
          "count": 168,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&patientproblem=1697&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Insufficient Information",
          "count": 61,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&patientproblem=4580&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        },
        {
          "problem_name": "Cardiac Arrest",
          "count": 33,
          "maude_link": "https://www.accessdata.fda.gov/cfmaude/results.cfm?start_search=1&searchyear=&productcode=DXT&patientproblem=1762&devicename=&knumber=k&pmanumber=p&manufacturer=&brandname=&eventtype=&reportdatefrom=01/1/2020&reportdateto=&pagenum=10"
        }
      ]
    }
  ]
}
```

### Response Structure

- **device_name**: The search term used
- **results**: Array of matching devices, each containing:
  - **detail_page**: Direct link to the FDA device detail page
  - **device_name**: Specific device name found
  - **device_problems**: Array of reported device malfunctions with:
    - **problem_name**: Type of device problem
    - **count**: Number of reported incidents
    - **maude_link**: Link to detailed FDA MAUDE database reports
  - **patient_problems**: Array of reported patient impacts with:
    - **problem_name**: Type of patient problem/symptom
    - **count**: Number of reported incidents
    - **maude_link**: Link to detailed FDA MAUDE database reports

The API provides comprehensive safety data including both technical device issues and their potential impact on patients, with direct links to official FDA databases for further investigation.

## License & Contributions

FDA_SCRAPPER is MIT licensed. Contributions are welcome—just open an issue or submit a pull request.

## Questions?

Reach out at [your.email@example.com](mailto:your.email@example.com).
