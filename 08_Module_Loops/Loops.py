# 1. Iterate 0 to 10 using for and while loop
print("Iterate 0 to 10:")
for i in range(11):
    print(i, end=" ")
print()

i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# 2. Iterate 10 to 0 using for and while loop
print("Iterate 10 to 0:")
for i in range(10, -1, -1):
    print(i, end=" ")
print()

i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1
print("\n")

# 3. Print a triangle pattern
print("Triangle Pattern:")
for i in range(1, 8):
    print("#" * i)
print()

# 4. Nested square pattern
print("Square Pattern:")
for _ in range(8):
    print("# " * 8)
print()

# 5. Multiplication pattern
print("Multiplication Pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")
print()

# 6. Iterate through a list and print items
print("List Iteration:")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)
print()

# 7. Print even numbers from 0 to 100
print("Even Numbers:")
for i in range(0, 101, 2):
    print(i, end=" ")
print("\n")

# 8. Print odd numbers from 0 to 100
print("Odd Numbers:")
for i in range(1, 101, 2):
    print(i, end=" ")
print("\n")


# 1. Sum of all numbers from 0 to 100
print("Sum of all numbers from 0 to 100:")
total = sum(range(101))
print("The sum of all numbers is", total)
print()

# 2. Sum of all even and odd numbers
print("Sum of evens and odds:")
evens = sum(i for i in range(101) if i % 2 == 0)
odds = sum(i for i in range(101) if i % 2 != 0)
print("The sum of all evens is", evens)
print("The sum of all odds is", odds)
print()



# 2. Reverse a fruit list
print("Reverse a fruit list:")
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruit in reversed(fruits):
    reversed_fruits.append(fruit)
print(reversed_fruits)
print()

