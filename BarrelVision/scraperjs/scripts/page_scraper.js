const scraperObject = {
    url: 'https://www.surf-forecast.com/breaks/Blackies/forecasts/latest',
    async scraper(browser) {
        let page = await browser.newPage();
        console.log(`Navigating to ${this.url}...`);
        await page.goto(this.url);

        // Wait for the required DOM to be rendered
        await page.waitForSelector('.forecast-table-sunset');

        // Find first index
        const tdSelector = '.forecast-table-time td';
        const indexOfFirstElement = await page.$$eval(tdSelector, elements => {
            return Array.from(elements).findIndex(element => element.classList.contains('is-day-end'));
        });




        // Temperature: temp_water
        const tempElement = '#contdiv > section > div > .break-header__content > div.break-header__temperature > b > span.temp';
        const temp_water = await page.$eval(tempElement, element => parseInt(element.textContent) || 0);

        // Temperature: temp_air
        const temp_data = await page.$$eval('#forecast-table > div > table > tfoot > tr:nth-child(6) td', elements => {
            return elements.map(element => {
                const tempElement = element.querySelector('span.temp');

                const temp_air = parseInt(tempElement.textContent);

                return {
                    temp_air
                };
            });
        });

        // Get Day and Day Number
        const day_data = await page.$$eval('.forecast-table-days__cell', elements => {
            return elements.map(element => {
                const dayNameElement = element.querySelector('.forecast-table__value:first-child');
                const dayNumberElement = element.querySelector('.forecast-table__value:last-child');

                const dayName = dayNameElement.textContent.trim();
                const dayNumber = parseInt(dayNumberElement.textContent);

                return {
                    dayName,
                    dayNumber
                };
            });
        });


        // Wave Stars: stars
        const star_data = await page.$$eval('.forecast-table__cell--has-image', elements => {
            return elements.map(element => {
                const starElement = element.querySelector('.star-rating__rating');

                const star_rating = parseInt(starElement.textContent);

                return {
                    star_rating
                };
            });
        });

        // Wave: wave_height, wave_direction, wave_angle
        const wave_data = await page.$$eval('.forecast-table-wave-height__cell', elements => {
            return elements.map(element => {
                const waveHeightElement = element.querySelector('.swell-icon__val');
                const waveDirectionElement = element.querySelector('.swell-icon__letters');
                const transformValue = element.querySelector('.swell-icon__arrow')?.getAttribute('transform');

                const wave_height = waveHeightElement ? parseFloat(waveHeightElement.textContent) || 0 : 0;
                const wave_direction = waveDirectionElement.textContent;
                const wave_angle = transformValue ? parseInt(transformValue.match(/rotate\((\d+)/)?.[1]) || 0.0 : 0.0;

                return {
                    wave_height,
                    wave_direction,
                    wave_angle
                };
            });
        });

        // Wind: wind_speed, wind_direction, wind_angle
        const wind_data = await page.$$eval('.forecast-table-wind__cell', elements => {
            return elements.map(element => {
                const windSpeedElement = element.querySelector('.wind-icon');
                const windDirectionElement = element.querySelector('.wind-icon__letters');
                const transformValue = element.querySelector('.wind-icon__arrow')?.getAttribute('transform');

                const wind_speed = windSpeedElement ? parseFloat(windSpeedElement.getAttribute('data-speed')) || 0.0 : 0.0;
                const wind_direction = windDirectionElement.textContent;
                const wind_angle = transformValue ? parseInt(transformValue.match(/rotate\((\d+)/)?.[1]) || 0.0 : 0.0;

                return {
                    wind_speed,
                    wind_direction,
                    wind_angle
                };

            });
        });

        console.log(wave_data);
        console.log(wind_data);
        console.log(star_data);
        console.log(temp_data);
        console.log(`Water temperature is ${temp_water}°F`);
        console.log(indexOfFirstElement)


        const mergedArray = wave_data.map((waveObj, index) => ({
            ...waveObj,
            ...(wind_data[index] || {}),
            ...(star_data[index] || {}),
            ...(temp_data[index] || {}),
            temp_water: temp_water
        }));
        // console.log(mergedArray);

        // trim from start of next day forward
        const trimmedArray = mergedArray.slice(indexOfFirstElement + 1);
        // console.log(trimmedArray);

        const startOf_trimmedArray = trimmedArray.slice(0, 3);
        console.log(startOf_trimmedArray);

        // 


    }
}

module.exports = scraperObject;