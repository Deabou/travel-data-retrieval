import requests
from bs4 import BeautifulSoup
import json


class WikipediaAirportScraper:
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_{letter}"

    def scrape_data_from_wikipedia(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table")
        if tables:
            first_table = tables[0]
            table_data = []
            rows = first_table.find_all("tr")
            for row in rows:
                columns = row.find_all("td")
                row_data = []
                for column in columns:
                    row_data.append(column.text.strip())
                if row_data:
                    table_data.append(row_data)
            return table_data
        else:
            return None

    def scrape_and_convert_to_json(self):
        scraped_data = {}
        for letter in range(65, 91):  # ASCII values for A to Z
            url = self.base_url.format(letter=chr(letter))
            print(f"Scraping data from {url}...")
            data = self.scrape_data_from_wikipedia(url)
            if data:
                scraped_data[chr(letter)] = data
            else:
                print(f"No tables found on the page for letter {chr(letter)}.")
        return json.dumps(scraped_data)


scraper = WikipediaAirportScraper()
json_data = scraper.scrape_and_convert_to_json()
print(json_data)
