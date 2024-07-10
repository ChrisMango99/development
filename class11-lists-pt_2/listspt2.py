import statistics

''' Lists Containing Other Lists '''

# Exercise - Months of the year

first_quarter = ['january', 'february', 'march'] 
second_quarter = ['april', 'may', 'june'] 
third_quarter = ['july', 'august', 'september'] 
fourth_quarter = ['october', 'november', 'december'] 

year = [first_quarter, second_quarter, third_quarter, fourth_quarter]
# print(year)


# Access february with indexing
february = year[0][1]



# # Access june with indexing


# # Access july with indexing


# # Access october with indexing



''' *** '''
''' *** '''

# Lets loop through rows and columns

year = [
    ['january', 'february', 'march'], 
    ['april', 'may', 'june'], 
    ['july', 'august', 'september'], 
    ['october', 'november', 'december']
    ]

# Accessing rows


# Accessing columns



''' *** '''
''' *** '''

# Lets practice some more indexing

my_super_list = [
    ['superman', 'wonderwoman','batman'],
    ['spiderman','captain america','ironman'],
    ['aquaman']]

# # Create a variable and assign it to wonderwoman via indexing


# # Create a variable and assign it to spiderman via indexing


# # Create a variable and assign it to aquaman via indexing


'''
How do you access each element in this list by index?
my_list = ["hello", 1, ["dog", 3], "cat", [True, ["frog", 5]]]
For example, "hello" is my_list[0]. How do you access all the other elements?
'''
my_list = ["hello", 1, ["dog", 3], "cat", [True, ["frog", 5]]]

# Access each of these elements in the above list by index









mdList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 8]
]

# let's loop through once and review our output


# Lets do a nested for loop and review our output


'''
Write a 2D list that is a 3x3 grid of numbers.
Write some code that prints out that grid nicely with proper formatting.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 2 3
4 5 6
7 8 9
'''

lis = [[1,2,3],[4,5,6],[7,8,9]]




'''


Write some code that goes through a 2D list and prints the columns.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 4 7
2 5 8
3 6 9
Hint: First create a new 2D list with swapped rows and columns. (You will need 2 nested for loops.) Then it's the same as the last problem.

Solution Courtesy of 

https://www.geeksforgeeks.org/python-transpose-elements-of-two-dimensional-list/
'''

lis = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

final_list = [] # this will hold our swapped rows and columns 

for i in range(len(lis[0])): # this will set the length for the loop of our 2d lists 
    temp_list = [] # this list will hold our coulmn items
    for item in lis:
        # appending list values and indexes
        temp_list.append(item[i])
    final_list.append(temp_list) #appending swapped rows and columns to final list 
# 

for row in final_list:
    for columns in row:
        print(columns, end= '')
    print()
print(final_list)




# Let's transpose with Pandas!
# import pandas as pd

# df = pd.DataFrame(lis)
# df = df.transpose()
# df_to_excel = df.to_excel('my_output.xlsx', index=False, header=None)
# print(df)


'''
You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
For example, if this is your list:
data = [[45,56,89],[67,34,78],[23,67,34]]
This would be your output:
Column 1: Sum = 135, Average = 45.0
Column 2: Sum = 157, Average = 52.33
Column 3: Sum = 201, Average = 67.0
Hint: Make a list to store the sums, and a list to store the averages.

'''


data = [[45,56,89],[67,34,78],[23,67,34]]






# Lets make our dataframe


# our sum and average functions


# our output


# Lets put it all together

# Lets add columns

# Lets send it to excel


'''
Creating a list via for loop vs List comprehension

Let's say you have a list of vegetables, and you want a new list containing only the vegetables that are less than 6 letters long.


'''

# For Loop

vegetables = ['broccoli', 'kale', 'onion', 'garlic', 'kale']

# List comprehension



# Lets add a range to a list comprehension




'''
You are given a list of integers. Write a Python program to create a new list that only includes the even numbers from the original list.
You can do this in one line with a list comprehension.
Example:
original_list = [34, 57, 81, 92, 2, 13]
new_list = [34, 92, 2]


'''
original_list = [34, 57, 81, 92, 2, 13]



''' More complex variation, lets see what is happening '''

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# For Loop

animals = ['giraffe', 'zebra', 'dog', 'cat', 'camel']
animals_no_letter_c = list()
for s in animals:
    if 'c' not in s:
        animals_no_letter_c.append(s)
# print(animals_no_letter_c)


# Do this with list comprehension




# Using List comprehension, lets double the list items

original_list = [1, 2, 3, 4, 5]




''' Exercise


You work for a sales company and must generate a list of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a list of customers over 60, and a list of customers who have made at least 5 purchases. Use a list comprehension to output a list of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']
Output: ['Dominic', 'Simone']

'''

over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']

customer_discount = []

# For Loop


# # with list comprehension
