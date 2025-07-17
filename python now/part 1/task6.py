import wbdata
import datetime

# Fetch population data for Chile from 2010 to 2020
data = wbdata.get_data(
    indicator='SP.POP.TOTL',
    country='CHL',
    date=(
        datetime.datetime(2010, 1, 1),
        datetime.datetime(2020, 12, 31),
    )
)

# Print results
for entry in data:
    country    = entry['country']['value']
    year       = entry['date']
    population = entry['value']
    print(f"Country: {country}, Year: {year}, Population: {population:,}")