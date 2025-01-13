import json
from collections import Counter
filename =  r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\countries_data.json'
def most_spoken_languages(filename, n):
    # Read the JSON file
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Extract all languages from the data
    languages = []
    for country in data:
        languages.extend(country.get('languages', []))

    # Count occurrences of each language
    language_counts = Counter(languages)

    # Get the n most common languages
    most_common_languages = language_counts.most_common(n)

    return most_common_languages

print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print(most_spoken_languages(filename='./data/countries_data.json', n=3))
