# Concatenate strings
string1 = 'Thirty'
string2 = 'Days'
string3 = 'Of'
string4 = 'Python'
concatenated_string = string1 + ' ' + string2 + ' ' + string3 + ' ' + string4
print(concatenated_string)  # Thirty Days Of Python

string5 = 'Coding'
string6 = 'For'
string7 = 'All'
concatenated_string2 = string5 + ' ' + string6 + ' ' + string7
print(concatenated_string2)  # Coding For All

# Declare variable company and assign "Coding For All"
company = "Coding For All"
print(company)

# Length of the company string
print(len(company))

# String methods: upper(), lower(), capitalize(), title(), swapcase()
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Slicing the first word
first_word = company[:company.index(' ')]
print(first_word)

# Check if the string contains the word "Coding"
print('Coding' in company)

# Replace the word "Coding" with "Python"
print(company.replace('Coding', 'Python'))

# Replace "Python for Everyone" with "Python for All"
phrase = "Python for Everyone"
print(phrase.replace('Everyone', 'All'))

# Split the string 'Coding For All'
print(company.split())

# Split "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))

# Character at index 0
print(company[0])

# Last index
print(company[-1])

# Character at index 10
print(company[10])

# Create acronyms
phrase1 = "Python For Everyone"
phrase2 = "Coding For All"
acronym1 = ''.join([word[0] for word in phrase1.split()])
acronym2 = ''.join([word[0] for word in phrase2.split()])
print(acronym1)  # PFE
print(acronym2)  # CFA

# Find positions using index and rfind
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

# Find positions of "because"
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find('because'))
print(sentence.rindex('because'))

# Slice out "because because because"
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

# Does "Coding For All" start/end with "Coding"?
print(company.startswith('Coding'))
print(company.endswith('coding'))

# Remove trailing spaces
trimmed_string = '   Coding For All      '.strip()
print(trimmed_string)

# Check valid identifiers
print("30DaysOfPython".isidentifier())  # False
print("thirty_days_of_python".isidentifier())  # True

# Join list of libraries with a hash
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# New line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# Tab escape sequence
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# String formatting for area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Arithmetic operations using string formatting
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
