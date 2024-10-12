# Module-level docstring
"""This module demonstrates the use of docstrings in Python."""

def add(a, b):
    """Return the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def factorial(n):
    """Return the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Negative values are not allowed.")
    return 1 if n == 0 else n * factorial(n - 1)

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""
    
    def multiply(self, a, b):
        """Return the product of two numbers.

        Args:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers.

        Args:
            a (int or float): The numerator.
            b (int or float): The denominator.

        Returns:
            float: The result of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

# Example usage
if __name__ == "__main__":
    print("Add 5 and 3:", add(5, 3))
    print("Factorial of 5:", factorial(5))

    calc = Calculator()
    print("Multiply 4 and 5:", calc.multiply(4, 5))
    print("Divide 10 by 2:", calc.divide(10, 2))
