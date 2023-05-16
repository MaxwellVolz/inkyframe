import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def parse_tide_table(tide_soup):
    forecast_table = tide_soup.select_one('#contdiv > div.tide-table > div.has-inertia.tide-table__container > div > div > table > tbody')

    sunrise = 'tr:nth-child(6) > td.tide-table__part.tide-table__part--sun.tide-table__part--first-shadow > div'


    # Define selectors
    selectors = {
        'date': 'tr:nth-child(1) > th:nth-child(1) > div',
        'sun_rise': 'tr.forecast-table__row.forecast-table-rating > td:nth-child({}) > img',
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
    name_of_date = forecast_table.select_one(selectors['date']).get_text()
    # number_of_date = forecast_table.select_one(selectors['date']['number']).get_text()

    # Loop over each time point
    # for time, tp in time_points.items():
    #     wave_rating = forecast_table.select_one(selectors['wave_rating'].format(tp)).get('alt')
    #     wave_height = forecast_table.select_one(selectors['wave_height'].format(tp)).get_text()
    #     wind_mph = forecast_table.select_one(selectors['wind_mph'].format(tp+25)).get_text()
    #     wind_dir = forecast_table.select_one(selectors['wind_dir'].format(tp)).get_text()

    #     # Add row to table
    #     t.add_row([number_of_date, name_of_date, time, wave_height, wave_rating, wind_mph, wind_dir])

    

    return name_of_date
