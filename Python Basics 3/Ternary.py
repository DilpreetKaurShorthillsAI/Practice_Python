def get_status(age):
    return "Adult" if age >= 18 else "Minor"

# Test the function with different ages
ages = [15, 22, 18, 12]
for age in ages:
    status = get_status(age)
    print(f"Age {age} is categorized as: {status}")
