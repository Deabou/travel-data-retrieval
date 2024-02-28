import json
from enum import Enum

import requests
from bs4 import BeautifulSoup
from string import ascii_uppercase


class WikipediaAirportScraper:
    BASE_URL = (
        "https://en.wikipedia.org/wiki/List_of_airports_by_IATA_airport_code:_{letter}"
    )


@staticmethod
def scrape_table_data(table):
    table_data = []
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        row_data = [column.text.strip() for column in columns]
        if row_data:
            table_data.append(row_data)
    return table_data


@staticmethod
def scrape_data_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")
    if tables:
        return tables[0]
    else:
        return None


@classmethod
def scrape_data_for_letter(cls, letter):
    url = cls.BASE_URL.format(letter=letter)
    table = cls.scrape_data_from_url(url)
    if table:
        return cls.scrape_table_data(table)
    else:
        print(f"No tables found on the page for letter {letter}.")
        return []


@classmethod
def convert_to_json(cls):
    scraped_data = {}
    for letter in ascii_uppercase:
        data = cls.scrape_data_for_letter(letter)
        scraped_data[letter] = data
    return json.dumps(scraped_data)


scrapper = WikipediaAirportScraper()
json_data = scrapper.convert_to_json()
print(json_data)
