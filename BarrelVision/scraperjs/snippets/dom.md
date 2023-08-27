## Template

- Selector: data-row-name="temperature-high"
- Targets: .temp
  
```html
<tr class="forecast-table__row" data-row-name="temperature-high">
    <th class="forecast-table__header">Temp. °<span class="tempu">F</span></th>
    <td class="forecast-table__cell temp-range-7"><span class="temp">64</span></td>
    <td class="forecast-table__cell temp-range-7"><span class="temp">66</span></td>
    <td class="forecast-table__cell temp-range-8"><span class="temp">70</span></td>
    <td class="forecast-table__cell temp-range-8"><span class="temp">70</span></td>
    <td class="forecas
```
## Temperature

- Selector: #contdiv > section > div > .break-header__content > div.break-header__temperature > b > span.temp



- Targets: water temperature
  
```html
<div class="break-header__temperature break-header__temperature--tablet"><b>Today's <span>Blackies </span>sea temperature is <span class="temp">67</span> °<span class="tempu">F</span></b> <span class="break-header__statistic">(<i>Statistics for 24 Aug 1981-2005 - mean: <span class="temp">67</span> max: <span class="temp">71</span> min: <span class="temp">64</span> </i>°<span class="tempu">F</span>)</span></div>
```

## Stars

- Selector:
- Targets: 
  
```html
<td class="forecast-table__cell forecast-table__cell--has-image"><div class="star-rating" style="width: 38px; height: 38px"><svg class="star-rating__star" height="38" viewBox="0
0
16.5
16.5" width="38"><use fill="hsl(57.1, 100%, 79.4%)" stroke="hsl(0, 0%, 0%)" stroke-linecap="miter" stroke-linejoin="miter" stroke-width="0.5" transform="translate(1.6, 1.6) scale(0.8)" vector-effect="non-scaling-stroke" xlink:href="#star"></use></svg><div class="star-rating__rating star-rating__rating--1" style="font-size: 14px; font-weight: 400">1</div></div></td>
```
## Wave Height

- Selector: .forecast-table-wave-height__cell
- Targets:
  - Wave Height (ft): .swell-icon__val
  - Wave Direction (Cardinal): .swell-icon__letters
  - Wave Angle (degrees): .swell-icon__arrow
```html
<td class="forecast-table__cell forecast-table-wave-height__cell" data-date="Thursday 24 8AM"
    data-swell-state="[{&quot;period&quot;:13,&quot;angle&quot;:27.0,&quot;letters&quot;:&quot;SSW&quot;,&quot;height&quot;:0.7},{&quot;period&quot;:5,&quot;angle&quot;:90.0,&quot;letters&quot;:&quot;W&quot;,&quot;height&quot;:0.4},{&quot;period&quot;:16,&quot;angle&quot;:63.0,&quot;letters&quot;:&quot;WSW&quot;,&quot;height&quot;:0.2},null]"
    data-wind="{&quot;direction&quot;:{&quot;angle&quot;:75.0,&quot;letters&quot;:&quot;WSW&quot;},&quot;speed&quot;:5.0}"
    data-wind-state="{&quot;text&quot;:&quot;cross-on&quot;,&quot;color&quot;:&quot;#AAAAAA&quot;}">
    <div class="swell-icon" data-height="0.7"><svg class="swell-icon__svg" fill="rgb(0,0,228)" viewBox="-19 -19 38 38"
            xmlns="http://www.w3.org/2000/svg">
            <circle cx="0" cy="0" r="11.44"></circle>
            <g class="swell-icon__arrow" fill="rgb(0,0,228)" transform="rotate(27.0)">
                <polygon points="-11 -12.44 0 -18.439999999999998 11 -12.44"></polygon>
                <rect height="2" width="6" x="-3" y="-12.44"></rect>
            </g><text class="swell-icon__val" fill="rgb(254,254,254)" text-anchor="middle" textLength="17" x="0"
                y="5">2.5</text>
        </svg>
        <div class="swell-icon__letters">SSW</div>
    </div>
</td>
```
## Wind

- Selector: .forecast-table-wind__cell
- Targets: 
  - Wind Speed (mph): data-speed
  - Wind Direction (Cardinal): text from the <text> element that says "WSW"
  - Wind Direction (degrees): int value 75 from transform="rotate(75)" 

```html
<td class="forecast-table__cell forecast-table-wind__cell">
    <div class="wind-icon" data-precision="5" data-speed="5.0">
        <svg class="wind-icon__svg" fill="rgb(0, 0, 0)" viewBox="-19 -19 38 38" xmlns="http://www.w3.org/2000/svg">
            <circle cx="0" cy="0" r="10.5"></circle>
            <g class="wind-icon__arrow" transform="rotate(75)">
                <polygon points="-7 -13.5 0 -19.5 7 -13.5"></polygon>
                <rect height="4" width="4" x="-2" y="-13.5"></rect>
            </g>
            <text class="wind-icon__val" fill="rgb(255, 255, 255)" text-anchor="middle" x="0" y="5">5</text>
        </svg>
        <div class="wind-icon__letters">WSW</div>
    </div>
</td>

```
