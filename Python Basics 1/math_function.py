import math

def calculate_square_root(x):
    """Returns the square root of x."""
    return math.sqrt(x)

def calculate_factorial(n):
    """Returns the factorial of n."""
    return math.factorial(n)

def calculate_sine(angle):
    """Returns the sine of the angle (in degrees)."""
    radians = math.radians(angle)  # Convert angle to radians
    return math.sin(radians)

def calculate_cosine(angle):
    """Returns the cosine of the angle (in degrees)."""
    radians = math.radians(angle)  # Convert angle to radians
    return math.cos(radians)

def calculate_logarithm(value, base=10):
    """Returns the logarithm of value with the specified base."""
    return math.log(value, base)

def main():
    # Example calculations
        print("Square root of 16:", calculate_square_root(16))
        print("Factorial of 5:", calculate_factorial(5))
        print("Sine of 30 degrees:", calculate_sine(30))
        print("Cosine of 60 degrees:", calculate_cosine(60))
        print("Logarithm of 1000 (base 10):", calculate_logarithm(1000, 10))

if __name__ == "__main__":
    main()
