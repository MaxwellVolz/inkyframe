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
print(soup.prettify())

forecast_table = soup.select_one('#forecast-table')


# Date
today_selector = 'div > table > tbody > tr.forecast-table__row.forecast-table-days > td:nth-child(2) > div'
name_of_date = forecast_table.select_one(f'{today_selector} > div:nth-child(1)').get_text()
number_of_date = forecast_table.select_one(f'{today_selector} > div:nth-child(2)').get_text()

# Rating
wave_rating_selector = '#forecast-table > div > table > tbody > tr.forecast-table__row.forecast-table-rating'
# wave_rating_8am = '> td:nth-child(11) > img'
wave_rating_8am = forecast_table.select_one(f'{wave_rating_selector} > td:nth-child(1) > img').get('alt')

wave_rating_8am = forecast_table.select_one(f'{wave_rating_selector}')
# wave_rating_11am = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(2) > img').get_text()
# wave_rating_2pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(3) > img').get_text()
# wave_rating_5pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(4) > img').get_text()
# wave_rating_8pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(5) > img').get_text()
# wave_rating_11pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(6) > img').get_text()

# Wave Height
wave_height_selector = 'div > table > tbody > tr:nth-child(5)'
wave_height_8am = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(2) > div > svg > text').get_text()
wave_height_11am = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(3) > div > svg > text').get_text()
wave_height_2pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(4) > div > svg > text').get_text()
wave_height_5pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(5) > div > svg > text').get_text()
wave_height_8pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(6) > div > svg > text').get_text()
wave_height_11pm = forecast_table.select_one(f'{wave_height_selector} > td:nth-child(7) > div > svg > text').get_text()


t = PrettyTable(['Date', 'Day', 'Time', 'Wave Height', 'Wave Rating'])

# Add rows
t.add_row([number_of_date, name_of_date, '8am', wave_height_8am, wave_rating_8am])
# t.add_row([number_of_date, name_of_date, '11am', wave_height_11am, wave_rating_11am])
# t.add_row([number_of_date, name_of_date, '2pm', wave_height_2pm, wave_rating_2pm])
# t.add_row([number_of_date, name_of_date, '5pm', wave_height_5pm, wave_rating_5pm])
# t.add_row([number_of_date, name_of_date, '8pm', wave_height_8pm, wave_rating_8pm])
# t.add_row([number_of_date, name_of_date, '11pm', wave_height_11pm, wave_rating_11pm])


print(t)
# Print the text
# print(text.get_text())


# print(forecast_table)


# Print the extracted data
# print(data)
