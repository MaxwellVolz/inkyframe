const puppeteer = require('puppeteer');
// const sendDataToAWS = require('./aws_handler');

async function startBrowser() {
	let browser;
	try {
		console.log("Opening the browser......");
		browser = await puppeteer.launch({
			headless: false,
			args: ["--disable-setuid-sandbox"],
			'ignoreHTTPSErrors': true
		});
	} catch (err) {
		console.log("Could not create a browser instance => : ", err);
	}
	return browser;
}

module.exports = {
	startBrowser
};