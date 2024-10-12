def evaluate_number(num):
    if num > 0:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"

# Test the function with different values
for value in [10, -5, 0]:
    result = evaluate_number(value)
    print(f"The number {value} is: {result}")

