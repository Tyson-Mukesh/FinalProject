import pandas as pd
import pycountry
import json

def map_country_name(name):
    country_mapping = {
        'United States of America': 'USA',
        'German Democratic Republic (Germany)' : 'Germany',
        'People\'s Republic of China': 'China',
        'Republic of Korea': 'South Korea',
        'ROC': 'Russia',
        'Great Britain': 'England',
        'Democratic People\'s Republic of Korea': 'North Korea',
        'Olympic Athletes from Russia' : 'Russia',
        'Russian Federation' : 'Russia',
        'German Democratic Republic': 'Germany',
        'North Macedonia': 'North Macedonia',
        'Soviet Union': 'Russia',
        'Singapore': 'Singapore',
        'MIX': 'MIX',
        'Barbados': 'Barbados',
        'Serbia and Montenegro': 'Serbia',
        'Bahrain': 'Bahrain',
        'Bohemia': 'Czech Republic',
        'Vietnam': 'Vietnam',
        'Liechtenstein': 'Liechtenstein',
        'Chinese Taipei': 'Taiwan',
        'Unified Team': 'Russia',
        'San Marino': 'San Marino',
        'Netherlands Antilles': 'Netherlands',
        'Independent Olympic Athletes': 'IOA',
        'Virgin Islands, US': 'USA',
        'Islamic Republic of Iran': 'Iran',
        'Samoa': 'Samoa',
        'Tonga': 'Tonga',
        'Czechoslovakia': 'Czech Republic',
        'Mauritius': 'Mauritius',
        'Republic of Moldova': 'Moldova',
        'West Indies Federation': 'Caribbean',
        'Bermuda': 'Bermuda',
        'Yugoslavia': 'Serbia',
        'Grenada': 'Grenada',
        'Australasia': 'Australia',
        'United Arab Republic': 'Egypt',
        'United Arab Emirates':'Saudi Arabia',
        'Hong Kong, China': 'China',
        'Dominican Republic': 'Dominican Republic',
        'Venezuela': 'Venezuela',
        'Syrian Arab Republic': 'Syria',
        'United Republic of Tanzania': 'United Republic of Tanzania',
        'Niger' : 'Niger',
    
    }
    
    if name in country_mapping:
        return country_mapping[name]
    
    try:
        country = pycountry.countries.search_fuzzy(name)[0]
        return country.name
    except:
        return name

# Read the CSV file
df = pd.read_csv('olympic_medals.csv')

# Extract year from slug_game column
df['year'] = df['slug_game'].str.extract('(\d{4})')

# Add map_country_name column
df['map_country_name'] = df['country_name'].apply(map_country_name)


print(df)

df.to_csv('/Users/tysonmukesh/Desktop/Masters/Semesters/Fall 2024/Data Visualization/Project2/olympics_data_with_country_names.csv', index=False)

