
# 1. Declare variables
age = 25  # Integer
height = 5.9  # Float
complex_number = 2 + 3j  # Complex number

# 2. Calculate area of a triangle
base = float(input("Enter base of the triangle: "))
height_triangle = float(input("Enter height of the triangle: "))
area_triangle = 0.5 * base * height_triangle
print(f"The area of the triangle is {area_triangle}")

# 3. Calculate perimeter of a triangle
side_a = float(input("\nEnter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter_triangle = side_a + side_b + side_c
print(f"The perimeter of the triangle is {perimeter_triangle}")

# 4. Calculate area and perimeter of a rectangle
length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print(f"The area of the rectangle is {area_rectangle}")
print(f"The perimeter of the rectangle is {perimeter_rectangle}")

# 5. Calculate area and circumference of a circle
radius = float(input("\nEnter the radius of the circle: "))
pi = 3.14
area_circle = pi * radius**2
circum_circle = 2 * pi * radius
print(f"The area of the circle is {area_circle}")
print(f"The circumference of the circle is {circum_circle}")

# 6. Slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2  # Coefficient of x in y = 2x - 2
x_intercept = -(-2 / 2)  # Solve 2x - 2 = 0
y_intercept = -2  # Constant term
print("\nSlope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# 7. Slope and Euclidean distance between two points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"\nSlope between points: {slope_points}")
print(f"Euclidean distance between points: {distance}")

# 8. Compare slopes
print(f"\nSlope from y = 2x - 2: {slope}, Slope from points: {slope_points}")
print("Are slopes equal?", slope == slope_points)

# 9. Solve y = x^2 + 6x + 9
print("\nSolving y = x^2 + 6x + 9")
for x in range(-10, 5):  # Testing a range of x values
    y = x**2 + 6*x + 9
    print(f"x={x}, y={y}")
print("y is zero when x =", -3)  # (x + 3)^2 = 0 => x = -3

# 10. Falsy comparison of string lengths
len_python = len("python")
len_dragon = len("dragon")
print("\nFalsy comparison (lengths):", len_python != len_dragon)

# 11. Check 'on' in both strings
print("'on' in 'python' and 'dragon':", 'on' in "python" and 'on' in "dragon")

# 12. Check 'jargon' in a sentence
sentence = "I hope this course is not full of jargon."
print("Is 'jargon' in the sentence?", 'jargon' in sentence)

# 13. Check absence of 'on' in both words
print("No 'on' in 'python' and 'dragon':", not ('on' in "python" and 'on' in "dragon"))

# 14. Convert length to float and string
length_python = float(len("python"))
length_python_str = str(length_python)
print(f"Length of 'python' as float: {length_python}, as string: {length_python_str}")

# 15. Check if a number is even
num = int(input("\nEnter a number to check if it is even: "))
print("Is the number even?", num % 2 == 0)

# 16. Floor division comparison
print("\nFloor division comparison:", 7 // 3 == int(2.7))

# 17. Type comparison
print("Type of '10' == Type of 10:", type("10") == type(10))
print("int('9.8') == 10:", int(float('9.8')) == 10)

# 18. Calculate pay
hours = float(input("\nEnter hours worked: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")

# 19. Calculate seconds lived
years_lived = int(input("\nEnter the number of years you have lived: "))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print(f"You have lived for {seconds_lived} seconds.")

# 20. Display table
print("\nTable:")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
