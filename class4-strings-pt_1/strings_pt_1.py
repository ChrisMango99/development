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

# capitalize() Converts the first character to upper case

color = 'blue'
color = color.capitalize()
#print(color)

# casefold() Converts string into lower case

name_one = 'sIMoN'
name_two = 'SimON'
#print(name_one == name_two) # False, becasue of the different casing
#print(name_one.casefold() == name_two.casefold()) #True 
#print(name_one.casefold()) #simon
#print(name_two.casefold()) #simon

#center() Returns a centered string
#print('hello' .center(100))

#count() Returns the number of times a specified value occurs in a string, basically shows the number of times a number is being shown in a string 
my_string = 'abracadabra'
letter_count = my_string.count('b')
#print(letter_count)

# start end parameter
letter_count_with_start_stop = my_string.count('a',0, 2)
#print(letter_count_with_start_stop)

tree = 'Malep'
find_letter_p = tree.count('p')
#print(find_letter_p)

# expandtabs() Sets the tab size of the string

testing_tabs = 'Happy\tWednesday\tEveryone!'

ten_characters = testing_tabs.expandtabs(10)
fifteen_characters = testing_tabs.expandtabs(15)
twenty_characters = testing_tabs.expandtabs(20)
#print(ten_characters)
#print(fifteen_characters)
#print(twenty_characters)

# find() Searches the string for a specified value and returns the position of where it was found
day = 'Tuesday'
month = 'June'
movie = 'Lord of The Rings'

# Find position of e in day
letter_e = day.find('e')
# print(f'The letter e appears at the number {letter_e} position in {day}')

# Find position of J in month
letter_j = month.find('J')
# print(f'The letter J appears at the number {letter_j} position in {month}')


# Find the position of R in movie
letter_r = movie.find('R')
# print(f'The letter R appears at the number {letter_r} position in {movie}')


# Note: Find returns -1 if the character is not in the string


# Find the position of b in movie
letter_b = movie.find('b')
# print(letter_b)

# index() Searches the string for a specified value and returns the position of where it was found

fav_sport = 'football'

# Error if letter doesnt exist
# letter_b = fav_sport.index('k')
# print(letter_b)




'''
Create a variable called index_of_y and apply the index string method to locate the index position of the letter y.  What happens if we try to locate a letter that does not exist in our string?
'''
fav_car = 'toyota'
# index_of_y = fav_car.index('y')
# print(index_of_y)


''' More string methods '''

# isalnum() Returns True if all characters in the string are alphanumeric (Letters and Numbers)
word_one = '%^&*'
word_two = 'hello'
word_three = 'abc123'

word_four = 'sdfsfdf'
test_user_input_for_alphanumeric = word_four.isalnum()
# print(test_user_input_for_alphanumeric)


# print(word_one.isalnum())
# print(word_two.isalnum())
# print(word_three.isalnum())



# isalpha() Returns True if all characters in the string are in the alphabet (Letters only)
word_four = 'abc123'
word_five = 'abcdef'
word_six = 'abc$%*()'

# print(word_four.isalpha())
# print(word_five.isalpha())
# print(word_six.isalpha())


# isdecimal() Returns True if all characters in the string are decimals
num_one = '12345' # True
num_two = '4.123' # False
num_three = 'abcde' # False

# print(num_one.isdecimal())
# print(num_two.isdecimal())
# print(num_three.isdecimal())


# isdigit() Returns True if all characters in the string are digits
num_four = '12345'
num_five = '4.53'
num_six = 'five'

# print(num_four.isdigit())
# print(num_five.isdigit())
# print(num_six.isdigit())


'''
isdigit & isnumeric & isdecimal

https://miguendes.me/python-isdigit-isnumeric-isdecimal

'''
# Isdigit
# all characters in the string are digits
# print('102030'.isdigit())

# 'a' is not a digit
# print('102030a'.isdigit())

# isdigit fails if there's whitespace
# print(' 102030'.isdigit())

# it must be at least one char long
# print(''.isdigit())


# dots '.' are also not digit
# print('12.5'.isdigit())


''' Is decimal'''
# isdecimal
# print('5'.isdecimal())

# superscripts are not decimal
# print('⁵'.isdecimal())

# superscripts, false
# print('5⁵'.isdecimal())

# negative sign, false
# print('-4'.isdecimal())

# decimal point, false
# print('4.5'.isdecimal())


# islower() Returns True if all characters in the string are lower case
house_type = 'MULTI-FAMILY'
house_type_lower = house_type.islower()
# print(f'Are the letters in this house type lower case? {house_type_lower}')


''' Try the islower method to test if the following strings are upper and lower case'''
animal = 'GIRAFFE'
car = 'truck'
season = 'SUMMERTIME'

# print(animal.islower())
# print(car.islower())
# print(season.islower())



# isupper() Returns True if all characters in the string are upper case


# isnumeric() Returns True if all characters in the string are numeric


val = '5005'


val = '10534875'


val = '5⁵'


val = '⁵'


val = '⅕'




# isspace() Returns True if all characters in the string are whitespaces
my_word = '    '

my_new_word = '   hello'



# istitle() Returns True if the string follows the rules of a title

song_one = 'Time To Say Goodbye'
song_two = 'eye of the tiger'
song_three = 'Sing for the moment'





# join() Joins the elements of an iterable to the end of the string
my_colors = ['blue', 'yellow', 'red']
result = ' '.join(my_colors)
# print(result)


# lower() Converts a string into lower case
weather = 'RAINY'



# Partition - looks for the match and separates into a tuple with before match, match, after match

string = "Let's see if this really works!"



# replace() Returns a string where a specified value is replaced with a specified value
test_name = 'abraham'



# split() Splits the string at the specified separator, and returns a list

string = 'I would like to split up this string'


# # splitlines splits at new line
txt = "Thank you for the music\nWelcome to the jungle"


# startswith() Returns true if the string starts with the specified value
str = 'zootopia'



# strip() Returns a trimmed version of the string

# txt = "     banana     "



# reference vs value equality: == vs is

x = 'hello'
str2 = "HELLO".lower()



# What is your name
# print("What is your name? ")
# first_name = input()
# print(f'You typed in {first_name}.')

# Let's shorten our code

# first_name = input('What is your name? ')


# Let's sanitize our string!
# first_name = first_name.strip()
# length_of_name = len(first_name)
# print(f'Hello, {first_name}. I am counting {length_of_name} characters')


'''
Example

Write some code that will take a string from the user and print if it is a number or not.
Examples:
apple
False

4
True

# Get User Input, sanitize user input

# Test Value, which test are we using??

# Provide Output

'''
# Get User Input
# user_input = input('What is your magic word? ')
# user_input = user_input.strip()

# # Test Value, which test are we using??
# number_or_not = user_input.isdigit()

# # Provide Output
# print(number_or_not)

'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True

Hint: use len() to find the length of the string, and don’t forget to cast to int()

'''

# Get our inputs 
# user_word = input("Hello, what is your word? ")
# user_num = int(input("Hello, what is your number? "))

# # Find whether the word is longer than the number 
# length_of_word = len(user_word)
# word_vs_num = (length_of_word > user_num)
# print(f'Does {user_word} have more than {user_num} letters? {word_vs_num}')


'''
Write some code that takes a string from the user, and prints how many vowels are in the string. (Vowels are a, e, i, o, u)
How will you count both uppercase and lowercase vowels?
What string method can you use to count the number of vowels?

'''

# Get input from the user
user_input = input("Please enter your word: ")
user_input = user_input.strip()

# Test vowel count

total_count = user_input.lower().count('a') + user_input.lower().count('e') + user_input.lower().count('i')+ user_input.lower().count('o') + user_input.lower().count('u')

print(f'{user_input} has {total_count} vowel(s).')


''' Exercise - Challenge

Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
Hint: You will have to use the len() function, string concatenation (+), and string multiplication (*)

'''







