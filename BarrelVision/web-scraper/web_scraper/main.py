import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# import os
# print(os.getcwd())

# Define the URL of the webpage you want to scrape

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Real Scraping
#url = 'https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581'

# url = 'https://www.surf-forecast.com/breaks/Blackies/forecasts/latest'
# response = requests.get(url, headers)
# soup = BeautifulSoup(response.content, 'html.parser')



# Psuedo Scraping
with open('tests/surf-forecasts/forecast.html', 'r') as f:
    contents = f.read()


soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())
from prettytable import PrettyTable

forecast_table = soup.select_one('#forecast-table')

# Define selectors
selectors = {
    'date': {
        'name': 'div > table > tbody > tr.forecast-table__row.forecast-table-days > td:nth-child(2) > div > div:nth-child(1)',
        'number': 'div > table > tbody > tr.forecast-table__row.forecast-table-days > td:nth-child(2) > div > div:nth-child(2)'
    },
    'wave_rating': 'div > table > tbody > tr.forecast-table__row.forecast-table-rating > td:nth-child({}) > img',
    'wave_height': 'div > table > tbody > tr:nth-child(5) > td:nth-child({}) > div > svg > text'
    # TODO: Add more selectors here as needed
}

# Define the time points
time_points = {'8am': 2, '11am': 3, '2pm': 4, '5pm': 5, '8pm': 6, '11pm': 7}

# Initialize table
t = PrettyTable(['Date', 'Day', 'Time', 'Wave Height', 'Wave Rating'])

# Get the date
name_of_date = forecast_table.select_one(selectors['date']['name']).get_text()
number_of_date = forecast_table.select_one(selectors['date']['number']).get_text()

# Loop over each time point
for time, tp in time_points.items():
    wave_rating = forecast_table.select_one(selectors['wave_rating'].format(tp)).get('alt')
    wave_height = forecast_table.select_one(selectors['wave_height'].format(tp)).get_text()

    # Add row to table
    t.add_row([number_of_date, name_of_date, time, wave_height, wave_rating])

print(t)
