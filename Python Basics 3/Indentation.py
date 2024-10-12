def check_numbers(numbers):
    for num in numbers:
        if num > 0:
            print(f"{num} is positive.")
        elif num < 0:
            print(f"{num} is negative.")
        else:
            print(f"{num} is zero.")

# Example list of numbers
number_list = [10, -5, 0, 3, -2]

# Call the function
check_numbers(number_list)
