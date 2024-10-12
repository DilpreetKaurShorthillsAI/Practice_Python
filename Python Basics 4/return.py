# 1. Basic return
def square(x):
    return x ** 2

print("Square of 4:", square(4))  # Output: 16

# 2. Returning multiple values
def min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = min_max([3, 1, 4, 1, 5])
print("Min:", min_val, "Max:", max_val)  # Output: Min: 1 Max: 5

# 3. Returning a boolean
def is_even(n):
    return n % 2 == 0

print("Is 10 even?", is_even(10))  # Output: True

# 4. Returning from a lambda function
double = lambda x: x * 2
print("Double of 5:", double(5))  # Output: 10

# 5. Returning from a recursive function
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120

# 6. Returning with conditions
def describe_number(num):
    return "Positive" if num > 0 else "Negative or Zero"

print(describe_number(-3))  # Output: Negative or Zero

# 7. Returning a list
def get_even_numbers(limit):
    return [num for num in range(limit) if num % 2 == 0]

print("Even numbers up to 10:", get_even_numbers(10))  # Output: [0, 2, 4, 6, 8]
