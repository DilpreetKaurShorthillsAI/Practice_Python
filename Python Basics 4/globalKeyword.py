# Global variable
counter = 0

def increment():
    """Increment the global counter variable by 1."""
    global counter  # Declare counter as global to modify it
    counter += 1
    print("Counter inside increment:", counter)

def reset():
    """Reset the global counter variable to 0."""
    global counter  # Declare counter as global to modify it
    counter = 0
    print("Counter reset to:", counter)

# Initial value of the global variable
print("Initial counter:", counter)

# Increment the counter
increment()  # Output: 1
increment()  # Output: 2

# Reset the counter
reset()  # Output: 0

# Check the counter value after reset
print("Final counter:", counter)  # Output: 0
