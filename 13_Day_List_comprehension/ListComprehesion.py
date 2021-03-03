# List Comprehension
# syntax
[i for i in iterable if expression]


# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']
# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)] 


# Lambda Function
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
# Named function
def add_two_nums(a, b):
    return a + b
print(2, 3)     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5
# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console
square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27
# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))


# Lambda Function Inside Another Function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
