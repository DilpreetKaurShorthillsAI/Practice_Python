def add_complex(c1, c2):
    """Returns the sum of two complex numbers."""
    return c1 + c2

def subtract_complex(c1, c2):
    """Returns the difference between two complex numbers."""
    return c1 - c2

def multiply_complex(c1, c2):
    """Returns the product of two complex numbers."""
    return c1 * c2

def divide_complex(c1, c2):
    """Returns the quotient of two complex numbers. Raises an error for division by zero."""
    return c1 / c2

def main():
    # Sample complex numbers
    c1 = complex(3, 4)  # 3 + 4j
    c2 = complex(1, 2)  # 1 + 2j

    # Perform operations
    print("Addition:", add_complex(c1, c2))
    print("Subtraction:", subtract_complex(c1, c2))
    print("Multiplication:", multiply_complex(c1, c2))
    print("Division:", divide_complex(c1, c2))

if __name__ == "__main__":
    main()
