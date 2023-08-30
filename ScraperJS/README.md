
# Tide Scraping with Javascript

## Tech

- Headless Browser: Puppeteer
- Scraping Library: Scrapy.
- AWS Service: Amazon API Gateway to define the endpoint and AWS Lambda to process the data.


## Scripts Breakdown

### Setup
- scraper.js: Main script where the browser is initiated and the control is passed to page_controller.
- browser.js: Manages the initialization of the Puppeteer browser instance. Here, browser settings like "headless" mode can be configured.
- page_controller.js: Accepts the browser instance and delegates the scraping task to page_scraper.

### Meat
- page_scraper.js: Does the actual web scraping. It navigates to the website, waits for certain elements to load, and then extracts the required data.
- aws_handler.js: A placeholder for AWS integration. This will be responsible for sending scraped data to AWS, but currently, it only logs the data.

## Data to Scrap

### Frequency

1. 

### Active


| Category    | Value             | Status   | Description |
| ----------- | ----------------- | -------- | ----------- |
| Temperature | Water             | complete | daily       |
|             | Air               | complete |             |
| Wave        | Height            | complete |             |
|             | Stars             | complete |             |
| Wind        | Speed             | complete |             |
|             | Direction         | complete |             |
| Tide        | High Low High Low |          |             |
|             | Plot              |          |             |
| Sun         | First Light       |          |             |
|             | Sunrise           |          |             |
|             | Sunset            |          |             |
|             | Last Light        |          |             |
