import requests
from bs4 import BeautifulSoup
import os


def scrape_population_data():
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

    return countries_list


def read_existing_data(file_path):
    if not os.path.exists(file_path):
        return None
    else:
        with open(file_path, 'r') as file_read:
            return file_read.read()


def write_data(file_path, data):
    with open(file_path, 'w') as file_write:
        file_write.write(data)


def format_data(countries_list):
    formatted_data = ''

    position = 1

    for country in countries_list:
        for name, population in country.items():
            formatted_data += f'Position {position}: Country name: {name}: Population: {population}\n'
        position += 1

    return formatted_data