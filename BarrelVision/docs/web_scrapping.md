# Serverless Web Scraping with Python using AWS

## How it works

**Cloudwatch** triggers **Lambda** which executes **Python**


## Lets Brk it deeern

1. Cloudwatch event trigger aka cronjob
2. Lambda function
    1. Lambda Layers
        - loads dependencies from S3
    2. Web scraping
        - Python with Beautiful Soup
    3. Save to S3

## To Figure Out

- AWS CDK
  - Used for deploying cloud infra as a service
  - how to integrate
    - install AWS CDK
    - install docker
- AWS SAM (Serveless Application Model)
  - Test and debug serverless code locally
  - Enables CI/CD


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


