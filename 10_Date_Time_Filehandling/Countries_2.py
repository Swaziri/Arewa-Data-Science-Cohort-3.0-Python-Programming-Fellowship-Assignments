import json
filename =  r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\countries_data.json'
def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    population_data = [{'country': country['name'], 'population': country['population']} for country in data]
    # Sort by population in descending order
    sorted_population = sorted(population_data, key=lambda x: x['population'], reverse=True)
    # Return the top n most populated countries
    return sorted_population[:n]
print(most_populated_countries(filename='./data/countries_data.json', n=10))
