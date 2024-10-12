# Create an initial list
my_list = [1, 2, 3]

# Append an item
my_list.append(4)
print("After append:", my_list)  # Output: [1, 2, 3, 4]

# Extend the list with another list
my_list.extend([5, 6])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Insert an item at index 2
my_list.insert(2, 'a')
print("After insert:", my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]

# Remove the first occurrence of 'a'
my_list.remove('a')
print("After remove:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Pop the last item
item = my_list.pop()
print("Popped item:", item)       # Output: 6
print("After pop:", my_list)      # Output: [1, 2, 3, 4, 5]

# Clear the list
my_list.clear()
print("After clear:", my_list)    # Output: []

# Re-create the list for further operations
my_list = [1, 2, 3, 2]

# Get the index of the first occurrence of 2
index_of_2 = my_list.index(2)
print("Index of first occurrence of 2:", index_of_2)  # Output: 1

# Count occurrences of 2
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)  # Output: 2

# Sort the list
my_list.sort()
print("After sort:", my_list)      # Output: [1, 2, 2, 3]

# Reverse the list
my_list.reverse()
print("After reverse:", my_list)    # Output: [3, 2, 2, 1]

# Create a copy of the list
my_list_copy = my_list.copy()
print("Copied list:", my_list_copy)  # Output: [3, 2, 2, 1]
