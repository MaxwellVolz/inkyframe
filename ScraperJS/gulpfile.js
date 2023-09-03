const gulp = require('gulp');
const scraper = require('./scraper');

function isTimeToRun() {
    const currentTime = new Date();
    const startHour = 9;  // 9 AM
    const endHour = 17;  // 5 PM

    return currentTime.getHours() >= startHour && currentTime.getHours() <= endHour;
}

function keyIndicatorExists(content) {
    // Replace with actual logic to check if the key indicator exists in the scraped content
    return content.includes("key-indicator");
}

gulp.task('watch', async function () {
    // Run once immediately
    if (isTimeToRun()) {
        const content = await scraper();  // Assuming scraper.js returns the scraped content
        if (keyIndicatorExists(content)) {
            console.log("Key indicator found. Site is ready to scrape.");
            // Do something (e.g., send data to AWS)
        }
    }

    // Then check every 30 minutes
    setInterval(async () => {
        if (isTimeToRun()) {
            const content = await scraper();  // Assuming scraper.js returns the scraped content
            if (keyIndicatorExists(content)) {
                console.log("Key indicator found. Site is ready to scrape.");
                // Do something (e.g., send data to AWS)
            }
        }
    }, 1800000);  // 1800000 milliseconds = 30 minutes
});
