# Exercises: Level 1

# 1. Driving eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare my_age and your_age
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    diff = your_age - my_age
    print(f"You are {diff} {'year' if diff == 1 else 'years'} older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    print(f"I am {diff} {'year' if diff == 1 else 'years'} older than you.")
else:
    print("We are the same age!")

# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2

# 1. Grading students
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
else:
    print("F")

# 2. Check the season
month = input("Enter the month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
elif month in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month.")

# 3. Fruit check
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Updated fruit list:", fruits)

# Exercises: Level 3

person = {
    'first_name': 'Muhammad',
    'last_name': 'Waziri',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check for 'skills' key and print middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2. Check for 'Python' skill
if 'skills' in person:
    print("Has Python skill:", 'Python' in person['skills'])

# 3. Determine the developer type
if 'skills' in person:
    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print("He is a front-end developer.")
    elif {'Node', 'MongoDB', 'Python'}.issubset(skills):
        print("He is a backend developer.")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a full-stack developer.")
    else:
        print("Unknown title.")

# 4. Married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")
