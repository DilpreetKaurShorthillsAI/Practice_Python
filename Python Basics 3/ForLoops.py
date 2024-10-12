# List of fruits
fruits = ['apple', 'banana', 'cherry']

# 1. Iterate over a list
print("Fruits:")
for fruit in fruits:
    print(fruit)

# 2. Iterate using range()
print("\nNumbers from 0 to 4:")
for i in range(5):
    print(i)

# 3. Iterate over a string
print("\nCharacters in 'hello':")
for char in "hello":
    print(char)

# 4. Use enumerate() to get index and value
print("\nEnumerate fruits:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 5. List comprehension to create a list of squares
squares = [x**2 for x in range(10)]
print("\nSquares from 0 to 9:", squares)

# 6. Nested loops
print("\nNested loops:")
for i in range(2):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# 7. Loop through a dictionary
student_scores = {'Dilpreet': 90, 'Manya': 85}
print("\nStudent Scores:")
for student, score in student_scores.items():
    print(f"{student}: {score}")
