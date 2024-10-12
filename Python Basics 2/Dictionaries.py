# Creating a dictionary
person = {
    'name': 'Dilpreet',
    'age': 20,
    'city': 'Ludhiana'
}

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding and updating items
person['email'] = 'kdilpreet1313@gmail.com'  # Add new item
person['age'] = 22                    # Update existing item

# Removing an item
del person['city']                      # Remove 'city'

# Iterating through the dictionary
print("\nKey-Value Pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# Using some dictionary methods
print("\nKeys:", person.keys())
print("Values:", person.values())
print("Name (using get):", person.get('name'))
print("Gender (default):", person.get('gender', 'Not specified'))

# Nested dictionary
person['address'] = {
    'street': '1855 White Quarter Dhuri Line',
    'zipcode': '141003'
}

print("\nNested Address:")
print(f"Street: {person['address']['street']}")
print(f"Zipcode: {person['address']['zipcode']}")

# Clear the dictionary
person.clear()
print("\nCleared Dictionary:", person)
