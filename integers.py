def add(a, b):
    """Returns the sum of two integers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two integers."""
    return a - b

def multiply(a, b):
    """Returns the product of two integers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two integers"""
    return a / b

def main():
    # Sample integers
    num1 = 10
    num2 = 5

    # Perform operations
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

if __name__ == "__main__":
    main()
