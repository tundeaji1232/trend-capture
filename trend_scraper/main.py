from scrapers.producthunt import scrape_producthunt
from scrapers.trendhunter import scrape_trendhunter
from scrapers.springwise import scrape_springwise
from scrapers.nichehunt import scrape_nichehunt
from airtable_connector import upload_to_airtable
from datetime import datetime

def main():
    all_data = []
    all_data += scrape_producthunt()
    all_data += scrape_trendhunter()
    all_data += scrape_springwise()
    all_data += scrape_nichehunt()

    today = datetime.utcnow().date().isoformat()
    for entry in all_data:
        entry["scraped_date"] = today
        upload_to_airtable(entry)

if __name__ == "__main__":
    main()