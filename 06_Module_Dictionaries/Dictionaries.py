# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

print("Dog Dictionary:", dog)

# 3. Create a student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Type of skills:", type(skills))  # Should print <class 'list'>

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['Java', 'Machine Learning'])
print("Updated skills:", student['skills'])

# 7. Get the dictionary keys as a list
keys = list(student.keys())
print("Dictionary keys:", keys)

# 8. Get the dictionary values as a list
values = list(student.values())
print("Dictionary values:", values)

# 9. Change the dictionary to a list of tuples using items() method
tuples = list(student.items())
print("List of tuples:", tuples)

# 10. Delete one of the items in the dictionary
del student['address']
print("Dictionary after deleting 'address':", student)

# 11. Delete one of the dictionaries
del dog
# print(dog)  # Uncommenting this line will raise an error since 'dog' is deleted
print("Dog dictionary has been deleted.")
