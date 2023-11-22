
# Redesign

describe a modern software architecture design for an ad-hoc server renderer that does the following:

a low powered device will wake up periodically, request an image from the last hour from a set of locations, if not already available the server gather relevant data from scraping websites, then will render then image, store it for future requests. the low powered device will wait X seconds then request the image again.


lets the image handler express server more specific, KPIs:

requests comes in with a param called "spot", ex: "Linda Mar"
check storage if image has been made in the last hour, 
    if so
        return the image
kick off scrapper with "spot" param
render new image
save image





# Modern Software Architecture Design for an Ad-Hoc Server Renderer

## Overview
The proposed architecture is a combination of microservices and serverless architecture. It is designed to be scalable, reliable, and efficient in handling requests from low-powered devices. 

## The architecture includes the following components:
Low-Powered Device: This is the client that sends requests to the server for images from the last hour from a set of locations.

- API Gateway: This is the entry point for all requests from the low-powered device. It routes the requests to the appropriate microservice.
- Image Request Handler Microservice: This service handles the incoming requests. It checks if the requested image is already available. If not, it triggers the Data Scraper and Image Renderer microservices.
- Data Scraper Microservice: This service scrapes relevant data from websites when a new image request comes in.
- Image Renderer Microservice: This service renders the image using the data provided by the Data Scraper.
- Image Storage: This is where the rendered images are stored for future requests.
- Cache: This is used to store the most recently requested images for faster retrieval.
- 
## Workflow
1. The low-powered device wakes up periodically and sends a request to the API Gateway for an image from the last hour from a set of locations.
2. The API Gateway routes the request to the Image Request Handler.
3. The Image Request Handler checks the Cache for the requested image. If the image is available, it is returned to the low-powered device. If not, the Image Request Handler triggers the Data Scraper and Image Renderer microservices.
4. The Data Scraper scrapes the relevant data from websites and sends it to the Image Renderer.
5. The Image Renderer renders the image and stores it in the Image Storage and Cache.
6. The Image Request Handler retrieves the rendered image from the Cache and sends it to the low-powered device.
7. The low-powered device waits X seconds and then sends another request.

## Technologies

- API Gateway: Amazon API Gateway or Google Cloud Endpoints
- Microservices: Node.js with Express.js or Python with Flask
- Data Scraper: Node.js with puppeteer
- Image Renderer: Python with Pillow or Node.js with sharp
- Image Storage: Amazon S3 or Google Cloud Storage
- Cache: Redis or Memcached
  
This architecture ensures that the system is scalable and can handle a large number of requests efficiently. It also ensures that the low-powered device does not have to wait for the image to be rendered if it has already been requested in the last hour.


## Image Handler
The Image Handler is a Node.js microservice that is responsible for managing image requests and responses. It interacts with the Data Scraper and Image Storage to ensure that the requested images are available and delivered to the client.
### WORKFLOW
2. Check Image Storage: The Image Handler checks the Image Storage to see if the requested "spot" image is already available (generated within an hour)
3. Render Image: The Image Handler takes in data to render the required image with the library sharp.
4. Store Image: The rendered image is then stored in the Image Storage for future requests.

## Data Scraper
The Data Scraper is another Node.js microservice that is responsible for gathering the necessary data to render the images. It does this by scraping relevant websites.

### WORKFLOW
1. Receive Request: The Data Scraper receives a request from server.js with the "spot"
2. Scrape Data: The Data Scraper uses puppeteer to scrape the necessary data from relevant websites.
3. Send Data: Once the data has been gathered, the Data Scraper sends this data back

### Technologies
- Node.js: The runtime environment for both the Image Handler and Data Scraper microservices.
- Express.js: The web application framework used to build the microservices.
- sharp: A Node.js module for high-performance image processing.
- Puppeteer or Axios: Node.js libraries used for web scraping.
- Local File System or MongoDB: For storing the images locally.
  
This architecture ensures that the system is efficient and scalable, and can handle a large number of requests. It also ensures that the low-powered device does not have to wait for the image to be rendered if it has already been requested in the last hour.

## Image Generation

### SVG

1. Swap Text / Values
2. Rotate Elements
3. Images? Test render path