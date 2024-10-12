# 1. Using break
print("Using break:")
for num in range(10):
    if num == 5:
        print("Breaking at number 5")
        break
    print(num)

# 2. Using continue
print("\nUsing continue:")
for num in range(10):
    if num % 2 == 0:  # Skip even numbers
        continue
    print(num)

# 3. Using pass
print("\nUsing pass:")
for num in range(5):
    if num == 2:
        pass  # Do nothing for number 2
    print(num)

# 4. Combining break and continue
print("\nCombining break and continue:")
for num in range(10):
    if num == 8:
        print("Breaking at number 8")
        break
    if num % 3 == 0:
        continue
    print(num)
# 1. Basic function
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Call the basic function
print(greet("Alice"))

# 2. Function with default argument
def add(a, b=5):
    """Function to add two numbers, with a default value for b."""
    return a + b

# Call the function with and without the default argument
print(add(3))     # Uses default value for b
print(add(3, 4))  # Overrides default value

# 3. Function with variable number of arguments
def multiply(*args):
    """Function to multiply any number of arguments."""
    result = 1
    for num in args:
        result *= num
    return result

# Call the function with varying numbers of arguments
print(multiply(2, 3))          # 6
print(multiply(2, 3, 4, 5))    # 120

# 4. Function with keyword arguments
def person_info(name, age):
    """Function to display person information."""
    return f"{name} is {age} years old."

# Call the function with keyword arguments
print(person_info(age=30, name="Bob"))

# 5. Lambda function
square = lambda x: x ** 2
print("Square of 4:", square(4))

# 6. Higher-order function
def apply_function(func, value):
    """Function that takes another function and applies it."""
    return func(value)

# Using the higher-order function
print(apply_function(square, 5))  # 25

# 7. Function with a return statement
def find_max(a, b):
    """Function to find the maximum of two numbers."""
    return a if a > b else b

# Call the function
print("Max of 10 and 20:", find_max(10, 20))

# 8. Recursive function
def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Call the recursive function
print("Factorial of 5:", factorial(5))
