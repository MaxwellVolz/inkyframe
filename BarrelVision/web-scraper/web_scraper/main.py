import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

from wave_parser import parse_wave_table
from tide_parser import parse_tide_table

import os
# print(os.getcwd())

DEV_MODE = True

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

if DEV_MODE:
    # Psuedo Scraping
    with open('tests/surf-forecasts/forecast.html', 'r') as f:
        wave_site_contents = f.read()
    wave_soup = BeautifulSoup(wave_site_contents, 'html.parser')

    with open('tests/surf-forecasts/tides.html', 'r') as f:
        tide_site_contents = f.read()
    tide_soup = BeautifulSoup(tide_site_contents, 'html.parser')
    
else:
    print("[WARNING] Scrapping actual websites....please rate limit.")
    # Real Scraping
    # url = 'https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581'

    # url = 'https://www.surf-forecast.com/breaks/Blackies/forecasts/latest'
    # response = requests.get(url, headers)
    # soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())
wave_table_data = parse_wave_table(wave_soup)
print(wave_table_data)

tide_table_data = parse_tide_table(tide_soup)
print(tide_table_data)
