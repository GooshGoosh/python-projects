#!/usr/bin/env python3
# weatherReport.py - Automatically checks weather.gov for the Rochester, MN
# area and sends an SMS message to the specified phone number of the weather
# forecast for that day.


import requests
import bs4
import textMyself

weatherSite = 'https://forecast.weather.gov/MapClick.php?lat=44.03101000000004&lon=-92.47095999999999'
res = requests.get(weatherSite)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
weatherForecast = soup.select('div.row-odd:nth-child(1) > div:nth-child(2)')

textMyself.textmyself(weatherForecast[0].getText())
