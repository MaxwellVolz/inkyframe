/**
 * imageHandler.js
 * Author: Maxwell
 * 
 * This script handles the image rendering and storage process.
 * It checks if the requested "spot" image is already available in the Image Storage,
 * renders the required image with the sharp library if it's not available,
 * and then stores the rendered image in the Image Storage for future requests.
 */

const sharp = require('sharp');

async function checkImageStorage(spot, time = 30) {
    // Check if the image is already available in the Image Storage
    const imagePath = `${imageStoragePath}/${spot}.jpg`;
    const fs = require('fs');
    if (fs.existsSync(imagePath)) {
        const fileStats = fs.statSync(imagePath);
        const fileTime = fileStats.mtimeMs; // modification time 
        if (Date.now() - fileTime < time * 60 * 1000) {
            return imagePath;
        } else {
            return null;
        }
    } else {
        return null;
    }
}

async function renderImage(data) {
    // Render the required image with the sharp library
    // Replace 'outputPath' with the actual path where you want to save the output image
    const outputPath = `${outputPath}/${data.spot}.jpg`;
    const image = sharp(data.image);
    await image.resize({ width: data.width, height: data.height }).toFile(outputPath);
    return outputPath;
}

async function storeImage(imagePath, spot) {
    // Store the rendered image in the Image Storage for future requests
    // Replace 'imageStoragePath' with the actual path to your Image Storage
    const newImagePath = `${imageStoragePath}/${spot}.jpg`;
    const fs = require('fs');
    fs.copyFileSync(imagePath, newImagePath);
}

module.exports = {
    checkImageStorage,
    renderImage,
    storeImage
};