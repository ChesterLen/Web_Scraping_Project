from scraper import scrape_population_data
from scraper import read_existing_data
from scraper import format_data
from scraper import write_data

filepath = 'countries_population'
new_data = format_data(scrape_population_data())
existing_data = read_existing_data(filepath)

if new_data != existing_data:
    write_data(filepath, new_data)
    print("New data written to the file.")
else:
    print("Data is already up-to-date.")

with open(filepath, 'r') as file:
    print(file.read())
