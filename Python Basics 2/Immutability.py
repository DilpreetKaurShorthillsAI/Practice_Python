# Initial string
original_string = "Hello, World!"

# Attempting to modify the string
try:
    original_string[0] = 'h'  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# Creating a new string instead
new_string = 'h' + original_string[1:]  # Creates a new string
print(f"Original string: {original_string}")
print(f"New string: {new_string}")

# Other examples of string operations
# Concatenation
concatenated_string = original_string + " How are you?"
print(f"Concatenated string: {concatenated_string}")

# Replacing part of the string
replaced_string = original_string.replace("World", "Python")
print(f"Replaced string: {replaced_string}")

# Original string remains unchanged
print(f"Original string after replacements: {original_string}")
