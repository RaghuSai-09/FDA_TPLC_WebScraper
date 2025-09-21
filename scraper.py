import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm"

def get_device_links(device_name: str, product_code: str = None, min_year: int = 2020):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/114.0.0.0 Safari/537.36",
        "Referer": BASE_URL,
        "Origin": "https://www.accessdata.fda.gov"
    }
    session.headers.update(headers)

    form_data = {}
    form_data["DeviceName"] = device_name
    form_data["min_report_year"] = str(min_year)
    form_data["search"] = "search"
    if product_code:
        form_data["ProductCode"] = product_code

    #  POST search
    resp = session.post(BASE_URL, data=form_data) 
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    # Parse search results for links
    links = []
    for a in soup.find_all("a", href=True):
        if "tplc.cfm?id=" in a["href"]:
            href = a["href"]
            if not href.startswith("http"):
                href = "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/" + href
            if "min_report_year" not in href:
                href += f"&min_report_year={min_year}"
            links.append(href)

    print(f"Found {len(links)} device links:")
    for link in links:
        print(link)

    # Optional: save HTML for inspection
    with open("debug_search.html", "w", encoding="utf-8") as f:
        f.write(resp.text)

    resp = session.get(links[0]) 
    resp.raise_for_status()
    with open("debug_detail.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
    return list(set(links))
