# Tech

**Cloudwatch** triggers a **Lambda** which executes **Python** to scrape data, saves to **MySQL**, consumed by **website**.

## Overview
1. Cloudwatch event trigger aka cronjob
2. Lambda function
3. Scrape data with Beautiful Soup
4. Upload to RDS
5. Website consumes data for display

## AWS Infrastructure
   - Set up an Amazon RDS (Relational Database Service) instance to store the scraped data. 
       - Choose a database engine that suits your needs (e.g., MySQL, PostgreSQL, etc.).

## Cloudwatch

## Lambda Functions


### Deploy the Script to AWS Lambda:
    - Package the scraping script and its dependencies into a ZIP file.
    - Upload the ZIP file to the AWS Lambda function you created earlier.
    - Configure the Lambda function's runtime environment, memory, and timeout settings as needed.

  - Lambda Layers loads dependencies from S3

### Schedule the Lambda Function:
    - Use Amazon EventBridge (formerly known as CloudWatch Events) to create a rule that triggers the Lambda function to run at regular intervals (e.g., every six hours).  
    - Specify the schedule expression for the rule based on your desired frequency (e.g., "rate(6 hours)").

## Upload to RDS
    - Parse the HTML content to extract the relevant data.
    - Define the schema for the database table(s) where you will store the scraped data.
    - Use a database library (e.g., SQLAlchemy for Python) to connect to the Amazon RDS instance and insert the parsed data into the database.

## To Figure Out
- AWS CDK
  - Used for deploying cloud infra as a service
  - how to integrate
    - install AWS CDK
    - install docker
- AWS SAM (Serveless Application Model)
  - Test and debug serverless code locally
  - Enables CI/CD