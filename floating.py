def add(a, b):
    """Returns the sum of two floating-point numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two floating-point numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two floating-point numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two floating-point numbers. Raises an error for division by zero."""
    return a / b

def main():
    # Sample floating-point numbers
    num1 = 10.5
    num2 = 5.2

    # Perform operations
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

if __name__ == "__main__":
    main()
