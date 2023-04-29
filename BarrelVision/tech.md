# Tech

1. AWS Infrastructure
   - Set up an Amazon RDS (Relational Database Service) instance to store the scraped data. 
       - Choose a database engine that suits your needs (e.g., MySQL, PostgreSQL, etc.).
   - Create an AWS Lambda function that will run your web scraping script.

2. Develop the [Web Scraping Script](scraping.md):
    - Write a web scraping script using a language and library of your choice (e.g., Python with BeautifulSoup or Scrapy).
    - Define the URLs you want to scrape and the data you want to extract from your website.
    - Implement error handling and logging to handle potential issues during scraping.
    - Test the script locally to ensure that it works as expected.
  
3. Parse and Store Data:
    - Parse the HTML content to extract the relevant data.
    - Define the schema for the database table(s) where you will store the scraped data.
    - Use a database library (e.g., SQLAlchemy for Python) to connect to the Amazon RDS instance and insert the parsed data into the database.

4. Deploy the Script to AWS Lambda:
    - Package the scraping script and its dependencies into a ZIP file.
    - Upload the ZIP file to the AWS Lambda function you created earlier.
    - Configure the Lambda function's runtime environment, memory, and timeout settings as needed.

5. Schedule the Lambda Function:
    - Use Amazon EventBridge (formerly known as CloudWatch Events) to create a rule that triggers the Lambda function to run at regular intervals (e.g., every six hours).  
    - Specify the schedule expression for the rule based on your desired frequency (e.g., "rate(6 hours)").