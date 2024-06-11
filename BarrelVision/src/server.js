/**
 * server.js
 * Author: Maxwell
 * 
 * This script handles incoming requests with a "spot" parameter, e.g., "Linda Mar".
 * It checks if an image has been made in the last hour for the given spot.
 * If such an image exists, it returns the image.
 * If not, it kicks off a scraper with the "spot" parameter, renders a new image,
 * saves the image, and then returns the new image.
 */

const express = require('express');
const path = require('path');
const { checkImageStorage, storeImage } = require('./imageStorage');
const { scrapeData } = require('./dataScraper');
const { renderImage } = require('./imageRenderer');

const app = express();
const port = process.env.PORT || 3000;

app.get('/render-image/:spot', async (req, res) => {
    const spot = req.params.spot;

    // Check if image has been made in the last hour
    const imagePath = await checkImageStorage(spot);

    if (imagePath) {
        // If image is available, return the image
        res.sendFile(path.resolve(imagePath));
    } else {
        // If image is not available, kick off scraper with "spot" param
        const data = await scrapeData(spot);


        // Render new image
        const newImagePath = await renderImage(data);

        // Save image
        storeImage(newImagePath, spot);

        // Return the new image
        res.sendFile(path.resolve(newImagePath));
    }
});

app.listen(port, () => {
    console.log(`Image Handler listening at http://localhost:${port}`);
});