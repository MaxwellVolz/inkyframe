import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage you want to scrape

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = 'https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581'

response = requests.get(url, headers)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())


# Send an HTTP GET request to the URL and get the content
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract data from the parsed HTML (e.g., the text of an element with a specific class)
# Note: You'll need to customize this part based on the structure of your webpage and the data you want to extract
# data = soup.find(class_='sl-current-conditions').get_text()

print(soup)

# Print the extracted data
# print(data)
