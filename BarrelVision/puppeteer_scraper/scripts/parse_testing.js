const fs = require('fs').promises;
const path = require('path');
const cheerio = require('cheerio');

(async () => {
    // Define the path to the output file
    const outputPath = path.join(__dirname, 'output.html');

    // Read the content of the file
    const content = await fs.readFile(outputPath, 'utf-8');

    // Load the content into cheerio
    const $ = cheerio.load(content);

    // Example: Get the title of the page
    const title = $('title').text();
    console.log('Title:', title);

    // Example: Get the text of the first <h1> element
    const h1Text = $('h1').first().text();
    console.log('First <h1> text:', h1Text);

    // Example: Get an element with a specific class
    const exampleClassElement = $('.example-class');
    console.log('.example-class HTML:', exampleClassElement.html());

    // Example: Get an element with a specific ID
    const exampleIdElement = $('#forecast-day1');
    console.log('#example-id HTML:', exampleIdElement.html());

    // Add more selectors and logging as needed
})();
