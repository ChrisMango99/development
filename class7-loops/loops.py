

''' While Loops

While loops run as long as the given condition returns a True boolean.
'''



''' Example
Create a while loop that prints every integer from 1 to 10.
'''

# i = 0 # initilization

# while i <= 10: # condition
#     print(i) # output for the user
#     i += 1  # increment or decrement




# We can also assign it to a variable
# end = int(input('Enter your number: '))
# counter = 0


# while counter <= end:
#     print(counter)
#     counter += 1




# we can choose our end point. our starting point is 0. We will count up by one and display it to the user as long as start is less than end.

# end = 10
# start = 0


# while start < end:
#     print(start)
#     start -= 1



# Let's create and infinite loop, a condition we will never see fulfilled, kill your terminal with ctrl + c






''' While loops and user input 

This will keep asking us to input a word until we input "stop" Let's follow it line by line

'''

# userin = '' # initialize your variable

# while userin != 'stop':
#     userin = input('Enter something: ').lower()
#     print(userin)


# print('Done collecting user input')

'''
Improve the login system we wrote last class to allow multiple attempts. You’re developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''


# Initialize all of our variables
# system_username, system_password = 'admin', 'password'
# username, password = '', ''




# # While Loop with conditional to handle user input
# while system_username != username and system_password != password:
#     print("Incorrect username or password")
#     username = input('Please enter your username')
#     password = input('Please enter your password')

#print('Login Successful')

''' For Loops
For loops are used to iterate through something.
For loops perform an action on a group of objects
For loops can be performed on iterables: 

Strings
Lists
Tuples
Dictionaries
Sets

# The Temporary Variable (item, goes out of scope after for loop ends)
for item in collection:
	print(item)

'''

'''
Lets loop through the string "Hello World"

'''

# my_string = 'Hello World how is everyone doing today'

# for m in my_string:
#     print(m)

'''
Lets loop through a list of colors

'''
# colors = ['red', 'green', 'orange', 'yellow']

# for c in colors:
#     print(f'My favorite color is {c}')



'''Lets loop through a tuple

'''
# fav_food = ('pizza', 'subs', 'chicken')

# for f in fav_food:
#     print(f)



'''
Example
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.

'''

# season = 'summer'
# counter = 0

# for s in season:
#     counter += 1
#     print(s, counter)

# print(f'{season} has {counter} letter(s)') # formatted string

    



'''
Exercise - Lets try to add conditionals to the mix

Take a string from the user. Verify that it’s a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop

'''

# initialize variables and get user input3
# userin = input('Please enter your data:')

# total = 0 # This variable, will capture the values as we loop through



# # # Verify Decimal, if it is, lets do our fun for loop, else we will send the user home with a nice message

# if userin.isnumeric(): #if the string value is actually numeric
#     for u in userin: # we can loop through
#         total += u
# else:
#     print('Sorry this is not a valid number')

# print(total)


''' More conditionals in loops'''

# word = 'hello'

# vowels = ['a','e','i','o','u']

# for word in word: # this will loop through the words variable 
#     if word in vowels: # if the letters in words, is in vowels
#         print(f'{word} is a vowel')
#     else:
#         print(f'{word} is a consonant')


''' Cleaning Strings

You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

test_string = 'a56b32ra87ca++d#@a*&b21r23a'

'''

test_string = 'a56b32ra87ca++d#@a*&b21r23a' # we only want (A-Z, a-z)
output = '' # we will add the letters that pass testing to this last

for t in test_string: # we are looping through t
    if t.isalpha(): 


# word_1 = 'move me to another variable'

# word_2 = ''
# for w in word_1:
#     word_2 += w
#    # print(w)

# print(word_2)
