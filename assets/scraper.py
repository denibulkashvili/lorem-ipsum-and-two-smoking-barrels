"""Quotes Scraper Module"""
import json
from bs4 import BeautifulSoup
import requests

# get the source
MOVIES = [
    {
        'name': 'LOCK',
        'url': 'https://www.rottentomatoes.com/m/snatch/quotes/'
    },
    {
        'name': 'SNATCH',
        'url': 'https://www.rottentomatoes.com/m/lock_stock_and_two_smoking_barrels/quotes/'
    }
]

class Scraper:
    """Creates a scraper"""

    def __init__(self, website_url, movie_name):
        self.website_url = website_url
        self.source = requests.get(self.website_url).text
        self.soup = BeautifulSoup(self.source, 'lxml')
        self.movie_name = movie_name

    def find_quotes(self):
        """get all quotes as a list of <li> elements"""
        quotes = self.soup.find_all('div', class_="quoteBody")
        return quotes

    def save_quotes_list(self):
        """Get the quotes form the soup"""
        quotes_list = []
        quotes = self.find_quotes()

        for quote in quotes:
            content = quote.get_text()
            quotes_list.append({
                "model": "quotes.Quote",
                "fields": {
                    "movie" : self.movie_name,
                    "text" : content,
                    "quote_len": len(content)
                }
            })

        return quotes_list


if __name__ == "__main__":
    for movie in MOVIES:

        s = Scraper(movie["url"], movie["name"])
        data = s.save_quotes_list()

        with open(f'quotes/fixtures/{movie["name"]}.json', 'w') as outfile:
            json.dump(data, outfile)
