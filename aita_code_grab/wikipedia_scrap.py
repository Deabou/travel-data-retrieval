import json
from enum import Enum

import requests
from bs4 import BeautifulSoup


class Alphabet(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"


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
        for letter in Alphabet:
            url = cls.BASE_URL.format(letter=letter.value)
            print(f"Scraping data from {url}...")
            data = cls.scrape_data_from_wikipedia(url)
            if data:
                scraped_data[letter.value] = data
            else:
                print(f"No tables found on the page for letter {letter.value}.")
        return json.dumps(scraped_data)


scrapper = WikipediaAirportScraper()
json_data = scrapper.scrape_and_convert_to_json()
print(json_data)
