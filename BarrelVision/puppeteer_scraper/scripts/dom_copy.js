const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

(async () => {
    // Launch the browser
    const browser = await puppeteer.launch({
        headless: false, // Run in headless mode for debugging
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });
    const page = await browser.newPage();

    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');

    // Function to navigate and follow redirects
    const navigateWithRedirects = async (url) => {
        let response = await page.goto(url, { waitUntil: 'networkidle2' });

        // Follow redirects until final URL is reached
        while (response.status() === 302 || response.status() === 301) {
            const redirectUrl = response.headers()['location'];
            console.log(`Redirecting to: ${redirectUrl}`);
            response = await page.goto(redirectUrl, { waitUntil: 'networkidle2' });
        }
    };

    // Go to the desired website and handle redirects
    await navigateWithRedirects('https://www.surfline.com/surf-report/river-jetties/');


    const xpath_to_click = [
        '/*[@id="forecast-day-1"]/div/div[1]',
        '/*[@id="forecast-day-2"]/div/div[1]',
        '/*[@id="forecast-day-3"]/div/div[1]',
    ]

    // Click each xpath with 1s delay
    for (const xpath of xpath_to_click) {
        console.log(`Attempting to click: ${xpath}`)

        await page.click('xpath/' + xpath)
        await page.waitForTimeout(1000); // 1-second delay

    }

    const content = await page.content();

    // Define the output file path
    const outputPath = path.join(__dirname, 'output.html');

    // Save the content to a file
    await fs.writeFile(outputPath, content);

    console.log('DOM content saved to output.html');

    // Close the browser
    await browser.close();
})();
