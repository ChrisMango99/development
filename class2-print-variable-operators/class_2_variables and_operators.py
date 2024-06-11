# Let's talk about the print statement
# I am a comment
 
 
# print('Hello World') # Print Built in Function
# print('Hello World')
 
 
# Addition
 
# print(4 + 2)
# print(7 + 10)
# print(100 + 200)
 
# Subtraction
 
# print(10 - 7)
# print(4 - 3)
# print(9 - 8)
 
# Multiplication
 
# print(4 * 8)
# print(3 * 9)
# print(11 * 9)
 
# Division
 
# print(10 / 2)
# print(5 / 3)
# print(5 / 0)
 
# Try Except
# try:
#     print(5 / 0)
# except ZeroDivisionError as e:
#     print("You cannot divide by 0")
 
 
# Exponents
 
# print(5 ** 5)
# print(2 ** 5)
# print(3 ** 6)
 
# Integer Division
 
# print(10 // 3)
# print(4 // 3)
# print(5 // 2)
 
# Modulo / Mod / Remainder
# print(5 % 2)
# print(10 % 4)
# print(6 % 2)
 
# Using variables as placeholders
# This is assigning integer value 1 to variable num_one
num_one = 1
num_two = 20
# print(num_one + num_two)
 
 
# Program to find the perimeter of a rectangle
# perimeter = 2 * (length + width)
 
# declaring your variables
length = 10
width = 7
perimeter = 2 * (length + width)
 
# print('The perimeter of my rectangle is',perimeter)
 
 
# Data Types
 
# Integer
num_3 = 5 # declare variable
# print(num_3) # print variable value
# print(type(num_3)) # we can check data type
 
 
# String
fav_color = 'blue'
# print(fav_color)
# print(type(fav_color))
 
 
# Boolean
technical_errors = False
# print(technical_errors)
# print(type(technical_errors))
 
 
# Float
num_4 = 4.05
# print(num_4)
# print(type(num_4))
 
# Lists
students_grades = [100, 95, 70, 85, 40]
# print(students_grades)
# print(type(students_grades))
 
# For loop
# for s in students_grades:
#     print(s)
 
# Dictionaries
demographic_info = {"First name":'first_name',
                    "Last name": 'last_name',
                    "State": 'state'}
 
# print(demographic_info)
# print(type(demographic_info))
 
# When you get input from a user, Python will make it a string
 
 
my_string = '5' # variable is a string of number 5
# print(my_string)
# print(type(my_string))
 
# changing the data type from string to int
new_number = int(my_string) # casting our string '5' to a integer
# print(new_number)
# print(type(new_number))
 
# casting an integer to a string
second_num = 10
# print(type(second_num))
 
new_string = str(second_num)
# print(type(new_string))
 
 
# Colors
my_fav_colors = ['blue', 'black', 'red', 'purple', 'yellow']
len_counts_the_items = len(my_fav_colors) # we are passing the argument my_fav_colors into the len function
# print(len_counts_the_items)
 
one_color = 'orange'
# my_count = len(one_color)
# print(my_count)
 
# for o in one_color:
#     print(o)
 
# Eval
cold_weather = 'True'
# print(eval(cold_weather))
 
# Find the perimeter of a Triangle
# perimeter = side_one + base + side_two
# User has a triangle with one side (6), one side (7), base (4)
 
 
'''
I am a multi line comment
I can go on another line if I want
 
 
 
 
We are still in the multi line comment
print('hello world') this code will not run
'''
 
 
"""
I am a multi line comment
 
 
 
Look at me everyone
"""
 
import math # this import should be at the top
 
radius = 5
height = 10
 
volume_of_right_cylinder = math.pi * (radius * radius) * height
print(volume_of_right_cylinder)