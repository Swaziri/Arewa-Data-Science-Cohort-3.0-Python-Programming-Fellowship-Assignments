# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [n for n in numbers if n <= 0]
print("Negative and Zero:", negative_and_zero)

# 2. Flatten the list of lists of lists to a one-dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]
print("Flattened List:", flattened)

# 3. Create the specified list of tuples
tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of Tuples:", tuples)

# 4. Flatten the countries list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
print("Flattened Countries:", flattened_countries)

# 5. Change the countries list to a list of dictionaries
countries_dict = [{'country': country[0].upper(), 'city': country[1].upper()} for sublist in countries for country in sublist]
print("Countries as Dictionaries:", countries_dict)

# 6. Change the names list to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [' '.join(name) for sublist in names for name in sublist]
print("Concatenated Names:", concatenated_names)

# 7. Lambda function to solve slope or y-intercept of linear functions
find_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x1 != x2 else 'Undefined'
find_y_intercept = lambda m, x, y: y - m * x

# Example usage for slope and y-intercept
slope = find_slope(1, 2, 3, 6)
y_intercept = find_y_intercept(slope, 1, 2)
print("Slope:", slope)
print("Y-Intercept:", y_intercept)
