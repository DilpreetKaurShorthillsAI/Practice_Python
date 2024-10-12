# Implicit type conversion in arithmetic operations
int_num = 5
float_num = 2.0

result = int_num + float_num  # int is converted to float
print(result)          # Output: 7.0
print(type(result))   # Output: <class 'float'>

# Implicit conversion in concatenation
str_num = "10"
result2 = str_num + str(int_num)  # int is converted to str
print(result2)       # Output: 101
print(type(result2)) # Output: <class 'str'>
