# Exercises: Level 1

# 1. Create an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ("Alice", "Eve", "Mary")
brothers = ("John", "Paul", "Mark")
print("Sisters:", sisters)
print("Brothers:", brothers)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. How many siblings do you have?
num_siblings = len(siblings)
print("Number of Siblings:", num_siblings)

# 5. Modify the siblings tuple and add the name of your father and mother, assign it to family_members
family_members = siblings + ("Father", "Mother")
print("Family Members:", family_members)

# Tuple Exercises: Level 2

# 6. Unpack siblings and parents from family_members
*siblings_unpacked, father, mother = family_members
print("Siblings Unpacked:", siblings_unpacked)
print("Father:", father)
print("Mother:", mother)

# 7. Create fruits, vegetables and animal products tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Broccoli", "Spinach")
animal_products = ("Milk", "Eggs", "Cheese")

# Join the three tuples and assign to food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)

# 8. Change food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)

# 9. Slice out the middle item or items from food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1: middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print("Middle Item(s):", middle_items)

# 10. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First Three Items:", first_three)
print("Last Three Items:", last_three)

# 11. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 12. Check if an item exists in a tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is Estonia a Nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a Nordic country?", is_iceland_nordic)
