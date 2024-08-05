# import requests
# from bs4 import BeautifulSoup
# import pandas
#
# url = 'https://www.worldometers.info/world-population/population-by-country/'
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, 'html.parser')
#
# rows = soup.find('table', attrs={'id': 'example2'}).find('tbody').find_all('tr')
#
# countries_list = []
#
# for row in rows:
#     countries_dict = {}
#
#     country_name = row.find_all('td')[1].text
#     country_population = row.find_all('td')[2].text.replace(',', '.')
#
#     countries_dict[country_name] = country_population
#
#     countries_list.append(countries_dict)
#
# countries_population = None
#
# try:
#     countries_population_read = open('countries_population', 'r')
#     print(countries_population_read.read())
#     countries_population.close()
# except:
#     position = 1
#     countries_population = open('countries_population', 'a')
#     for country in countries_list:
#         for name, population in country.items():
#             countries_population.write(f'Position {position}: Country name: {name}: Population: {population}\n')
#         position += 1
#     countries_population.close()
