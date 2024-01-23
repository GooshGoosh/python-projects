'''
weather_report.py - Automatically checks weather.gov for the specified
area and sends an SMS message to the specified phone number of the weather
forecast for that day.
'''


import requests
import bs4
import text_myself


WEATHER_SITE = ''
res = requests.get(WEATHER_SITE, timeout=10)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
weather_forecast = soup.select('div.row-odd:nth-child(1) > div:nth-child(2)')

text_myself.text_myself(weather_forecast[0].getText())
