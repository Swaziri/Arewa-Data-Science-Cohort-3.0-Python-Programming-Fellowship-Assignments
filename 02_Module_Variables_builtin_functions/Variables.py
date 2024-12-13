# Day 2: 30 Days of Python programming

# Declaring variables
first_name = "Muhammad"
last_name = "Waziri"
full_name = f"{first_name} {last_name}"
country = "Nigeria"
city = "Katsina"
age = 25
year = 2024
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables on one line
a, b, c = 10, 20, 30

# Output to verify variables
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Multiple Variables:", a, b, c)
# Day 2: Extended Assignment - 30 Days of Python programming

# Checking data types of variables
print("Data Types:")
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool

# Using len() to find the length of first name
first_name_length = len(first_name)
print("\nLength of first name:", first_name_length)

# Comparing the length of first name and last name
last_name_length = len(last_name)
print("Length of last name:", last_name_length)

if first_name_length > last_name_length:
    print("First name is longer.")
elif first_name_length < last_name_length:
    print("Last name is longer.")
else:
    print("First name and last name are of the same length.")

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nArithmetic Operations:")
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponential:", exp)
print("Floor Division:", floor_division)

# Calculating area and circumference of a circle
radius = 30
pi = 3.14159

area_of_circle = pi * radius**2
circum_of_circle = 2 * pi * radius

print("\nCircle Calculations:")
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# Taking user input for radius and calculating area
user_radius = float(input("\nEnter the radius of a circle: "))
user_area_of_circle = pi * user_radius**2
print("Area of Circle with user radius:", user_area_of_circle)

# Taking user input for personal details
user_first_name = input("\nEnter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = input("Enter your age: ")

print("\nUser Details:")
print("First Name:", user_first_name)
print("Last Name:", user_last_name)
print("Country:", user_country)
print("Age:", user_age)

# Python keywords
print("\nPython Reserved Words:")
help("keywords")

