import requests
from tide_parser import parse_tide_table
import os
from datetime import datetime

from bs4 import BeautifulSoup

# from prettytable import PrettyTable
from wave_parser import parse_wave_table

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
DEV_MODE = False 

directory = "soup"
if not os.path.exists(directory):
    os.makedirs(directory)

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}

print(DEV_MODE)

if DEV_MODE:
    # Psuedo Scraping
    with open("tests/surf-forecasts/forecast.html", "r") as f:
        wave_site_contents = f.read()
    wave_soup = BeautifulSoup(wave_site_contents, "html.parser")

    with open("tests/surf-forecasts/tides_5_17.html", "r") as f:
        tide_site_contents = f.read()
    tide_soup = BeautifulSoup(tide_site_contents, "html.parser")
    # with open('soup/tid)
else:
    print("[WARNING] Scrapping actual websites....please rate limit.")
    # Real Scraping
    # url = 'https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581'

    url = "https://www.surf-forecast.com/breaks/Blackies/forecasts/latest"
    response = requests.get(url, headers)
    wave_soup = BeautifulSoup(response.content, "html.parser")

    file_path = os.path.join(directory, f"wavesoup_{timestamp}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(wave_soup))

    url = "https://www.surf-forecast.com/breaks/Blackies/tides/latest"
    response = requests.get(url, headers)
    tide_soup = BeautifulSoup(response.content, "html.parser")

    file_path = os.path.join(directory, f"tidesoup_{timestamp}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(tide_soup))


# print(soup.prettify())
# wave_table_data = parse_wave_table(wave_soup)
# print(wave_table_data)

tide_table_data = parse_tide_table(tide_soup)
print(tide_table_data)
