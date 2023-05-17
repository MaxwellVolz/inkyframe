import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def parse_tide_table(tide_soup):
    forecast_table = tide_soup.select_one('#contdiv > div.tide-table > div.has-inertia.tide-table__container > div > div > table > tbody')



    # Define selectors
    selectors = {
        'date': 'tr:nth-child(1) > th:nth-child(1) > div',
        'sun_rise': 'tr:nth-child(6) > td.tide-table__part.tide-table__part--sun.tide-table__part--first-shadow > div',
        'sun_set': 'tr:nth-child(6) > td.tide-table__part.tide-table__part--sun.tide-table__part--sunset.tide-table__part--last-shadow > div',
    }

    # Define the time points
    time_points = {'8am': 2, '11am': 3, '2pm': 4, '5pm': 5, '8pm': 6, '11pm': 7}

    # Initialize table
    t = PrettyTable(['Date', 'Day', 'Time', 'Wave Height', 'Wave Rating', 'Wind MPH', 'Wind Dir'])

    # Get the date
    name_of_date = forecast_table.select_one(selectors['date']).get_text()
    sunrise = forecast_table.select_one(selectors['sun_rise']).get_text().strip()

    # high_tides = forecast_table.select_one('#contdiv > div.tide-table > div.has-inertia.tide-table__container > div > div > table > tbody > tr:nth-child(4)')
    # high_tides = forecast_table.find_all('span',{"class":"tide-table__value-high"})
    # high_tides = forecast_table.find_all('td',{"class":"tide-table__value-high"})
    high_tides = forecast_table.find_all('td', class_='tide-table__part tide-table__part--high tide-table__part--tide')[:4]
    low_tides = forecast_table.find_all('td', class_='tide-table__part tide-table__part--low tide-table__part--tide')[:4]

    results = []
    print(high_tides)
    print(low_tides)

    for td in high_tides:
    # Check if element is not of class "tide-table__tide-time-filler"
        if not td.find('div', class_='tide-table__tide-time-filler'):
            # Extract text from the spans for time, height, and units
            time = td.find('span', class_='tide-table__value-high').text.strip()
            height = td.find('span', class_='tide-table__height').text.strip()
            units = td.find('span', class_='tide-table__units').text.strip()

            # Add result to list
            results.append((time, height, units))

    # Print results
    for result in results:
        print(f'Time: {result[0]}, Height: {result[1]}, Units: {result[2]}')


    # number_of_date = forecast_table.select_one(selectors['date']['number']).get_text()

    # Loop over each time point
    # for time, tp in time_points.items():
    #     wave_rating = forecast_table.select_one(selectors['wave_rating'].format(tp)).get('alt')
    #     wave_height = forecast_table.select_one(selectors['wave_height'].format(tp)).get_text()
    #     wind_mph = forecast_table.select_one(selectors['wind_mph'].format(tp+25)).get_text()
    #     wind_dir = forecast_table.select_one(selectors['wind_dir'].format(tp)).get_text()

    #     # Add row to table
    #     t.add_row([number_of_date, name_of_date, time, wave_height, wave_rating, wind_mph, wind_dir])

    

    return [name_of_date, sunrise]
