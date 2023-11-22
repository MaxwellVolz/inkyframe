# Store selectors for BeautifulSoup4 as strings

# General Scraping
HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}

# Tide Scrapping
TIDE_TABLE = "#contdiv > div.tide-table > div.has-inertia.tide-table__container > div > div > table > tbody"
TIDE_DATE = "tr:nth-child(1) > th:nth-child(1) > div"
TIDE_SUNRISE = "tr:nth-child(6) > td.tide-table__part.tide-table__part--sun.tide-table__part--first-shadow > div"
TIDE_SUNSET = "tr:nth-child(6) > td.tide-table__part.tide-table__part--sun.tide-table__part--sunset.tide-table__part--last-shadow > div"


# Wave Scrapping
