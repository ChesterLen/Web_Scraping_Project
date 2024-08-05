import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.worldometers.info/world-population/population-by-country/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table', attrs={'id': 'example2'}).find('tbody').find_all('tr')

countries_list = []

for row in rows:
    countries_dict = {}

    country_name = row.find_all('td')[1].text
    country_population = row.find_all('td')[2].text.replace(',', '.')

    countries_dict[country_name] = country_population

    countries_list.append(countries_dict)

print(countries_list[0])