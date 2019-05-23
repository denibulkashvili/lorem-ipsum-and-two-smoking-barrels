"""Quotes Scraper Module"""
import json
from bs4 import BeautifulSoup
import requests

#pylint:disable=invalid-name
# get the source
website_url = 'https://www.rottentomatoes.com/m/lock_stock_and_two_smoking_barrels/quotes/'
source = requests.get(website_url).text
soup = BeautifulSoup(source, 'lxml')

# get all quotes as a list of <li> elements
quotes = soup.find_all('div', class_="quoteBody")

# create an empty dictionary of quotes
data = []

for quote in quotes:
    movie = "LOCK"
    # get the two parts (actor and text) and combine
    content = quote.find_all("span")
    text = f"{content[0].text} {content[1].text}"

    # append quote text to the dictionary
    data.append({
        "movie" : movie,
        "text" : text
    })

with open('assets/lock_quotes.json', 'w') as outfile:
    json.dump(data, outfile)
