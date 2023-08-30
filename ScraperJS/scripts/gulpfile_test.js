const gulp = require('gulp');
// const scraper = require('./scraper');

// [MOCK] scraper
const scraper = async () => 'some text key-indicator some more text';

let hasRunToday = false;

function resetHasRun() {
    hasRunToday = false;
}

function performOncePerDay() {
    console.log("Function executed for today.");
    // Your code here (e.g., send data to AWS)
    hasRunToday = true;
}
function isTimeToRun() {
    const currentTime = new Date();
    const targetHour = 13;  // 9 AM
    const targetMinuteStart = 58;  // 9:30
    const targetMinuteEnd = 59;  // 9:32

    return currentTime.getHours() === targetHour &&
        currentTime.getMinutes() >= targetMinuteStart &&
        currentTime.getMinutes() < targetMinuteEnd;
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

    // Then check every 10 seconds
    setInterval(async () => {

        const currentTime = new Date();
        if (currentTime.getHours() === 0 && currentTime.getMinutes() === 0) {
            resetHasRun();
        }

        if (isTimeToRun()) {
            const content = await scraper();
            if (keyIndicatorExists(content) && !hasRunToday) {
                performOncePerDay();
            }
        }
    }, 10000);  // 10000 milliseconds = 10 seconds
});
