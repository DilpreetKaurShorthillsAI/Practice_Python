def process_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ValueError("Negative value not allowed!")  # Breaks flow with an exception
        if num % 2 == 0:
            continue  # Skip even numbers
        if num == 5:
            print("Breaking the loop at", num)
            break  # Exit the loop when num is 5
        print("Processing:", num)

try:
    process_numbers([1, 2, 3, 4, 5, -1, 7])
except ValueError as e:
    print(e)
