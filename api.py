import requests
from config import APP_ID, APP_KEY, COUNTRY, BASE_URL

def fetch_jobs(role="intern", location="india", results=10):
    """
    Fetch job/internship data from Adzuna API
    """
    url = f"{BASE_URL}/{COUNTRY}/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": results,
        "what": role,
        "where": location,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for item in data.get("results", []):
        jobs.append({
            "company": item.get("company", {}).get("display_name"),
            "role": item.get("title"),
            "location": item.get("location", {}).get("display_name"),
            "apply_link": item.get("redirect_url")
        })

    return jobs
