import requests
import os

API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "tblSHn0HHUGnWqJhx"  # Airtable Table ID

def upload_to_airtable(trend_data):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    fields = {
        "Title": trend_data.get("title", ""),
        "Summary": trend_data.get("summary", ""),
        "Source": trend_data.get("source", ""),
        "URL": trend_data.get("url", ""),
        "Tags": trend_data.get("tags", []),
        "Category": trend_data.get("category", ""),
        "Published Date": trend_data.get("published_date", ""),
        "Scraped Date": trend_data.get("scraped_date", "")
    }

    response = requests.post(
        f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}",
        headers=headers,
        json={"fields": fields}
    )

    if response.status_code not in [200, 201]:
        print("Error uploading:", response.json())
    else:
        print("Uploaded:", response.json())
