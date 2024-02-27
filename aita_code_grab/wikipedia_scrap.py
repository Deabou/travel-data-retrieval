import requests
from bs4 import BeautifulSoup
import json


class WikipediaAirportScraper:
    BASE_URL = (
        "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_{letter}"
    )

    @staticmethod
    def _scrape_table_data(table):
        table_data = []
        rows = table.find_all("tr")
        for row in rows:
            columns = row.find_all("td")
            row_data = [column.text.strip() for column in columns]
            if row_data:
                table_data.append(row_data)
        return table_data

    @classmethod
    def scrape_data_from_wikipedia(cls, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("table")
        if tables:
            return cls._scrape_table_data(tables[0])
        else:
            return None

    @classmethod
    def scrape_and_convert_to_json(cls):
        scraped_data = {}
        for letter in range(65, 90):  # ASCII values for A to Z
            url = cls.BASE_URL.format(letter=chr(letter))
            print(f"Scraping data from {url}...")
            data = cls.scrape_data_from_wikipedia(url)
            if data:
                scraped_data[chr(letter)] = data
            else:
                print(f"No tables found on the page for letter {chr(letter)}.")
        return json.dumps(scraped_data)
