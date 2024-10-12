def check_truthiness(value):
    if value:
        print(f"{value} is truthy.")
    else:
        print(f"{value} is falsy.")

# Examples of truthy and falsy values
values = [0, "", [], {}, None, 
          1, "Hello", [1, 2, 3], {"key": "value"}, True]

for val in values:
    check_truthiness(val)
