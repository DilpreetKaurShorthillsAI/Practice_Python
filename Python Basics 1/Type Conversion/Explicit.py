# Explicit type conversion
float_num = 3.14
int_num = int(float_num)  # Converting float to int
print(int_num)            # Output: 3
print(type(int_num))      # Output: <class 'int'>

# Converting string to int
str_num = "42"
int_num2 = int(str_num)  # Converting str to int
print(int_num2)          # Output: 42
print(type(int_num2))    # Output: <class 'int'>

# Converting int to string
int_num3 = 100
str_num2 = str(int_num3)  # Converting int to str
print(str_num2)          # Output: '100'
print(type(str_num2))    # Output: <class 'str'>
    