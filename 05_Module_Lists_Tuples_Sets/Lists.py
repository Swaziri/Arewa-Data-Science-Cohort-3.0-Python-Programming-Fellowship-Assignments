# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6]

# Find the length of your list
print(len(items_list))

# Get the first item, the middle item and the last item of the list
print(items_list[0])  # First item
print(items_list[len(items_list) // 2])  # Middle item
print(items_list[-1])  # Last item

# Declare a list called mixed_data_types
mixed_data_types = ["John Doe", 25, 5.9, "Single", "123 Main Street"]

# Declare a list named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])  # First
print(it_companies[len(it_companies) // 2])  # Middle
print(it_companies[-1])  # Last

# Modify one of the companies in the list
it_companies[0] = "Meta"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("SAP")
print(it_companies)

# Insert an IT company in the middle of the list
it_companies.insert(len(it_companies) // 2, "Adobe")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_companies = "#;  ".join(it_companies)
print(joined_companies)

# Check if a certain company exists in the list
print("Google" in it_companies)
print("Twitter" in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print(it_companies[middle_index - 1: middle_index + 1])
else:
    print(it_companies[middle_index])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1: middle_index + 1]
else:
    del it_companies[middle_index]
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# Insert Python and SQL after Redux
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print(full_stack)

# List Exercise Level 2
# Given list of student ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted Ages:", ages)
print("Min Age:", min_age)
print("Max Age:", max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Updated Ages:", ages)

# Find the median age (one middle item or two middle items divided by two)
middle = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[middle - 1] + ages[middle]) / 2
else:
    median_age = ages[middle]
print("Median Age:", median_age)

# Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print("Average Age:", average_age)

# Find the range of the ages (max minus min)
age_range = max_age - min_age
print("Range of Ages:", age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min - Average Difference:", min_diff)
print("Max - Average Difference:", max_diff)

# List of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Find the middle country(ies) in the countries list
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1: middle_index + 1]
else:
    middle_countries = countries[middle_index]
print("Middle Country(ies):", middle_countries)

# Divide the countries list into two equal lists if it is even, if not, one more country for the first half
half = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:half]
    second_half = countries[half:]
else:
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]
print("First Half of Countries:", first_half)
print("Second Half of Countries:", second_half)

# Unpack the first three countries and the rest as scandic countries
first_three, *scandic_countries = countries
print("First Three Countries:", first_three)
print("Scandic Countries:", scandic_countries)
