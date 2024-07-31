import math


''' Functions pt 2 completed '''

# Lambda with sort

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]



# Let's look at reduce
from functools import reduce


my_list = [1, 2, 3, 4, 5]


''' More fun with functions'''


''' 
Write a lambda function that makes a string a title case and apply the function to the list below with a map function
words = ['make', 'us', 'title', 'case']

'''
words = ['make', 'us', 'title', 'case']

result = map(lambda w : w.title(), words)
# print(list(result))



''' Write a lambda function that will add ten to a list item if that list item is greater than or equal to 50, otherwise it will subtract five

my_numbers = [50, 12, 19, 80, 5, 75]
'''

my_numbers = [50, 12, 19, 80, 5, 75]


    
''' Lambda version of add_if 

lambda n:  n + 10 if n >= 50 else n - 5
'''






''' Write a lambda function and utilize reduce to add all the numbers in this list

add_me_up = [50, 12, 9, 100, 56, 70]

'''


add_me_up = [50, 12, 9, 100, 56, 70.11]





''' Compile time errors / static errors'''
# SyntaxError: unterminated string literal 
# print('Wed) 

# SyntaxError: unterminated string literal
# name = 'John  

# SyntaxError: '(' was never closed
# print("I hope you have a great day" 

# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# if x = 10: 

# SyntaxError: expected ':'
# if x == 10 


''' Exceptions / Runtime errors'''

''' ValueError '''
# ValueError: could not convert string to float: 'testing'
# print(float("testing")) 

# ValueError: math domain error
# print(math.sqrt(-5)) 

# ValueError: not enough values to unpack (expected 3, got 2)
# fname, lname, middlename = 'fritz', 'lewis' 

''' AttributeError '''
# AttributeError: 'int' object has no attribute 'append'
# num = 10
# num.append(5) 


# AttributeError: 'str' object has no attribute 'append'
# str1 = 'hello'
# str1.append('buddy')  

''' NameError '''
# NameError: name 'x' is not defined
# print(x) 

# Name error: name 'c' is not define
# for i in range(c): 
#     print(i)  

''' TypeError '''
#TypeError: can only concatenate str (not "int") to str
# color = 'blue'
# age = 25
# result = color + age 


# TypeError: 'str' object is not callable
car = 'chevy'
# car() 

# TypeError: list indices must be integers or slices, not str
fav_animals = ['dog', 'cat', 'bird']
index_value = '1'
# print(fav_animals[index_value]) 


# TypeError: 'int' object is not iterable
# for i in 155:
#     print(i) 

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
def add_two(num1, num2):
    return num1 + num2 
# add_two(5, 'hello')


# Keyboard interruption exception

# i = 2
# while i > 0:
#     i += 1
#     print(i)  # KeyboardInterrupt


# Dividing by zero



# Let's prevent this




# Lets implement a try, except, than test







'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customer's age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

'''




# With Except / Else



# With Except / Else / Finally



''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

'''





''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''


# Propogating exceptions (functions)






