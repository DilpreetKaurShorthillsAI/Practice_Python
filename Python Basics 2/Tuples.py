# Creating a tuple
fruits = ('apple', 'banana', 'cherry', 'date')

# Accessing values
print("First fruit:", fruits[0])          # Accessing first element
print("Last fruit:", fruits[-1])           # Accessing last element

# Tuple unpacking
fruit1, fruit2, fruit3, fruit4 = fruits
print(f"\nUnpacked fruits: {fruit1}, {fruit2}, {fruit3}, {fruit4}")

# Slicing a tuple
sliced_fruits = fruits[1:3]               # Slicing from index 1 to 2
print("\nSliced fruits:", sliced_fruits)

# Checking membership
is_banana = 'banana' in fruits
print("\nIs 'banana' in fruits?", is_banana)

# Concatenating tuples
more_fruits = ('elderberry', 'fig')
all_fruits = fruits + more_fruits
print("\nAll fruits:", all_fruits)

# Repeating tuples
repeated_fruits = fruits * 2
print("\nRepeated fruits:", repeated_fruits)

# Finding the length of a tuple
print("\nNumber of fruits:", len(fruits))

# Creating a single-element tuple
single_fruit = ('grape',)  # Note the comma
print("\nSingle-element tuple:", single_fruit)

# Tuples are immutable: Attempting to change an element (commented out to avoid error)
# fruits[0] = 'kiwi'  # This will raise a TypeError

# Iterating through a tuple
print("\nIterating through fruits:")
for fruit in fruits:
    print(fruit)

# Nested tuples
nested_tuple = (fruits, more_fruits)
print("\nNested tuple:", nested_tuple)
