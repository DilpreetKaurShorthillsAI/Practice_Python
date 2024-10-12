# 1. Basic while loop
count = 0
print("Basic while loop:")
while count < 5:
    print(count)
    count += 1

# 2. While loop with a condition
print("\nWhile loop with a condition:")
number = 10
while number > 0:
    print(number)
    number -= 1

# 3. Using a break statement
print("\nUsing break statement:")
x = 0
while True:
    if x == 3:
        break
    print(x)
    x += 1

# 4. Using a continue statement
print("\nUsing continue statement:")
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print(y)

# 5. While loop for user input
print("\nUser input loop (type 'exit' to stop):")
user_input = ""
while user_input.lower() != 'exit':
    user_input = input("Enter something (or type 'exit' to quit): ")
    print(f"You entered: {user_input}")

# 6. Using a flag variable
print("\nUsing a flag variable:")
flag = True
while flag:
    response = input("Do you want to continue? (yes/no): ")
    if response.lower() == 'no':
        flag = False
    print(f"You chose to {response}.")
