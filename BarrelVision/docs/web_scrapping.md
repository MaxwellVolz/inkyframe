# Scraping 101 - BarrelVision

- [Scraping 101 - BarrelVision](#scraping-101---barrelvision)
  - [Surf-Forecast](#surf-forecast)
  - [Magic Seaweed](#magic-seaweed)
  - [Surfline](#surfline)
  - [Scrape like a...person.](#scrape-like-aperson)
    - [User-Agent Switching](#user-agent-switching)
    - [Referrer Spoofing](#referrer-spoofing)
    - [Cookies](#cookies)

## [Surf-Forecast](https://www.surf-forecast.com/breaks/Blackies/forecasts/latest)

Wave Height(8am):

Selector:
#forecast-table > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > svg > text

XPath:
//*[@id="forecast-table"]/div/table/tbody/tr[5]/td[1]/div/svg/text

Full XPath:
/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[5]/div[2]/div/div[3]/div/table/tbody/tr[5]/td[1]/div/svg/text

## Magic Seaweed

## [Surfline](https://www.surfline.com/surf-report/river-jetties/5842041f4e65fad6a77088ee?camId=5834a0223421b20545c4b581')

## Scrape like a...person. 

### User-Agent Switching

Using *requests*, specify different user agent profiles to spoof browser type

```py
import random
import requests

user_agents = [
    # valid user agent strings aka 'Mozilla/5.0 (Windows)...
]

headers = {
    'User-Agent': random.choice(user_agents),
}

response = requests.get('http://scrapetown.com', headers=headers)
```

### Referrer Spoofing

Set referer so it seems like you came from a link


```py
headers = {
    'User-Agent': random.choice(user_agents),
    'Referer': 'http://hot-links.com',
}

response = requests.get('http://scrapetown.com', headers=headers)
```

### Cookies

Get remembered when hitting same domain using Sessions

```py
session = requests.Session()

response = session.get('http://favoritesite.com')
# handles cookies

response = session.get('http://favoritesite.com/other_page')
# reuse cookies
```


