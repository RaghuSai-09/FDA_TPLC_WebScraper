from fastapi import FastAPI, Query
from scraper import get_device_links
from parser import parse_device_page

app = FastAPI(title="FDA Device & Patient Problem Extraction API")


@app.get("/scrape")
def scrape(
    device_name: str = Query(..., description="Device name to search"),
    product_code: str = Query(None, description="Optional product code"),
    min_year: int = Query(2020, description="Minimum report year")
):
    try:
        # Step 1: search device links
        links = get_device_links(device_name, product_code, min_year)
        if not links:
            return {"device_name": device_name, "results": [], "message": "No devices found"}

        # Step 2: parse each device detail page
        results = []
        for link in links:
            device_data = parse_device_page(link)
            results.append(device_data)

        return {"device_name": device_name, "results": results}

    except Exception as e:
        return {"error": str(e)}
