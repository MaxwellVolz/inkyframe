# Scraping 101 - BarrelVision

- [Scraping 101 - BarrelVision](#scraping-101---barrelvision)
  - [Magic Seaweed](#magic-seaweed)
  - [Surfline](#surfline)
  - [Scrape like a...person.](#scrape-like-aperson)
    - [User-Agent Switching](#user-agent-switching)
    - [Referrer Spoofing](#referrer-spoofing)
    - [Cookies](#cookies)

## Magic Seaweed

## Surfline

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


