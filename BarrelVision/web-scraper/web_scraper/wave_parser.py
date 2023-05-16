import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def parse_wave_table(wave_soup):
    forecast_table = wave_soup.select_one('#forecast-table > div > table > tbody')

    # Define selectors
    selectors = {
        'date': {
            'name': 'tr.forecast-table__row.forecast-table-days > td:nth-child(2) > div > div:nth-child(1)',
            'number': 'tr.forecast-table__row.forecast-table-days > td:nth-child(2) > div > div:nth-child(2)'
        },
        'wave_rating': 'tr.forecast-table__row.forecast-table-rating > td:nth-child({}) > img',
        'wave_height': 'tr:nth-child(5) > td:nth-child({}) > div > svg > text',
        'wind_mph': 'tr:nth-child(9) > td:nth-child({}) > div > svg > text',
        'wind_dir': 'tr:nth-child(9) > td:nth-child({}) > div > div'
        # TODO: More selectors!
    }

    # Define the time points
    time_points = {'8am': 2, '11am': 3, '2pm': 4, '5pm': 5, '8pm': 6, '11pm': 7}

    # Initialize table
    t = PrettyTable(['Date', 'Day', 'Time', 'Wave Height', 'Wave Rating', 'Wind MPH', 'Wind Dir'])

    # Get the date
    name_of_date = forecast_table.select_one(selectors['date']['name']).get_text()
    number_of_date = forecast_table.select_one(selectors['date']['number']).get_text()

    # Loop over each time point
    for time, tp in time_points.items():
        wave_rating = forecast_table.select_one(selectors['wave_rating'].format(tp)).get('alt')
        wave_height = forecast_table.select_one(selectors['wave_height'].format(tp)).get_text()
        wind_mph = forecast_table.select_one(selectors['wind_mph'].format(tp+25)).get_text()
        wind_dir = forecast_table.select_one(selectors['wind_dir'].format(tp)).get_text()

        # Add row to table
        t.add_row([number_of_date, name_of_date, time, wave_height, wave_rating, wind_mph, wind_dir])

    return t
