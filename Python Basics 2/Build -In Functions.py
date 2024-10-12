# Sample string
my_string = "  Hello, World!  "

# Using built-in functions
length = len(my_string)
print(f"Length of the string: {length}")

# String methods
lower_string = my_string.lower()
upper_string = my_string.upper()
title_string = my_string.title()
stripped_string = my_string.strip()

# Replacing and finding substrings
replaced_string = my_string.replace("World", "Python")
index_of_world = my_string.find("World")

# Splitting and joining strings
words = my_string.split(", ")
joined_string = " | ".join(words)

# Output results
print(f"Original string: '{my_string}'")
print(f"Lowercase: '{lower_string}'")
print(f"Uppercase: '{upper_string}'")
print(f"Title case: '{title_string}'")
print(f"Stripped: '{stripped_string}'")
print(f"Replaced: '{replaced_string}'")
print(f"Index of 'World': {index_of_world}")
print(f"Words: {words}")
print(f"Joined string: '{joined_string}'")
    