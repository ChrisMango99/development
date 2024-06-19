''' Strings

Strings are how we store text in python
Strings are actually a sequence of characters.
Strings are immutable - this means that if we want to change a string we have to completely remake the string . (More on this next class)

'''

''' Printing Exercise

You have a variable called hours which equals 24, the number of hours in a day.
Print there are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember to cast hours to a string and manually add the spaces !
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!
'''
hours = 24
day_of_the_week = 'Wednesday'
# Commas
#print("There are", hours, "hours in a day. ")

# Concatenating
hours = str(hours) # we are casting int to string
#print('There are ' + hours + ' hours in a day.')

# Formatted Strings
#print(f'There are {hours} hours in a day')


''' Concatenation and Multiplication '''


# Concatenation
first_name = 'Joe'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
#print(full_name)


# Multiplication

greeting = 'hip hip hooray '
three_cheers = greeting * 3
#print(three_cheers)


'''
Create a variable called fav_food, and assign a string value of your favorite food. Create a second variable, called result, which multiplies your fav_food variable by 10
'''

fav_food = 'broccoli '
result = fav_food * 10
#print(result)

'''
Using the 'in' keyword solve the following

Is 'a' in giraffe?
Is 'z' in birthday?
Is 'w' in wrapper?

'''
#print('A' in 'giraffe')
#print('B' in 'birthday')
#print('W' in 'wrapper')

'''
Using the len function find the numbers of characters in the following strings

Pardon
Halloween
Ice Cream
Tank
Laptop
'''

pardon = len('Pardon')
halloween = len('Halloween')
ice_cream = len('Ice Cream')
tank = len('Tank')
laptop = len('Laptop')
#print(pardon, halloween, ice_cream, tank, laptop) # result should be 6,9,9,4,6. 

''' Let's try some string methods '''







