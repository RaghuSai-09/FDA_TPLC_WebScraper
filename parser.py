# parser.py
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://www.accessdata.fda.gov"

def parse_device_html(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    result = {
        "detail_page": None,
        "device_name": None,
        "device_problems": [],
        "patient_problems": []
    }

    #  "Device" label is a <th> followed by a <td>
    dev_th = soup.find(lambda t: t.name == "th" and t.get_text(strip=True).lower() == "device")
    if dev_th:
        td = dev_th.find_next_sibling("td")
        if td:
            result["device_name"] = td.get_text(strip=True)

    # try h1/h3 if present
    if not result["device_name"]:
        h = soup.find(["h1", "h3"])
        if h:
            result["device_name"] = h.get_text(strip=True)

    def extract_table_by_header(header_text):
        
        out = []
        header_th = soup.find(lambda t: t.name == "th" and t.get_text(strip=True).strip().lower() == header_text.lower())
        if not header_th:
            return out
        table = header_th.find_parent("table")
        if not table:
            return out

        # iterating rows, looking for rows with first <td> containing an <a>
        for row in table.find_all("tr"):
            tds = row.find_all("td")
            if len(tds) < 1:
                continue
            first_td = tds[0]
            a = first_td.find("a", href=True)
            if not a:
                continue

            name = a.get_text(strip=True)
            if name.lower() == "total":
                continue 

            count_text = tds[1].get_text(strip=True) if len(tds) > 1 else None
            count = None
            if count_text:
                try:
                    count = int(count_text.replace(",", ""))
                except ValueError:
                    count = count_text

            href = a["href"]
            maude_link = urljoin(BASE, href)

            out.append({
                "problem_name": name,
                "count": count,
                "maude_link": maude_link
            })
        return out

    result["device_problems"] = extract_table_by_header("Device Problems")
    result["patient_problems"] = extract_table_by_header("Patient Problems")
    return result


def parse_device_page(path_or_url):
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    resp = requests.get(path_or_url, headers=headers, timeout=20)
    resp.raise_for_status()

    data = parse_device_html(resp.text)
    data["detail_page"] = path_or_url
    return data

