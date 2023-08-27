// https://www.surf-forecast.com/breaks/Blackies/forecasts/latest

const browserObject = require('./browser');
const scraperController = require('./page_controller');

//Start the browser and create a browser instance
let browserInstance = browserObject.startBrowser();

// Pass the browser instance to the scraper controller
scraperController(browserInstance)