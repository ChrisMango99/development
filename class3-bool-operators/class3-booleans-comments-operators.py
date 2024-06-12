#Operators, Boolean Expressions and Comments

# I am a comment
temperature = 95 # I am an inline comment

# I am a standard single line comment
first_name = 'Thomas' ''' Multi line comment - inline'''
last_name = 'the Train' """inline comment with double quotes"""


'''
Everything between these quotes will be commented out
'''

# Comment me
# Below are the length and width of a rectangle
# Dimensions

length = 5
width = 7

# Below is the perimeter of a rectangle
perimeter = 2 * (length + width)


# This is the calculation of that formula
# print(perimeter)

''' Script to convert temperature'''

fahrenheit = 89 # our temp to convert

celsius = (fahrenheit - 32) * 5/9 # algorithm to convert f to c



# print(celsius) #our output
# Add 5 to me





age = 25
age += 5 # adding 5 via shortcut operators
# print(age)

# Add 10 years
year = 2024
year += 10
# print(year)

# Subtract 20
num_one = 55
num_one -= 20
# print(num_one)

# Subtract 15
num_two = 11
num_two -= 15
# print(num_two)


# Multipy by 3
my_Value = 9
my_Value *=3
# print(my_Value)

# Multiply by 10
mileage = 15
mileage *= 10
# print(mileage)

# Divide by 2 /
pizza_slices = 8
pizza_slices /= 2
# print(pizza_slices)


# Divide by 7 /
fees = 8.90
fees /= 7
# print(fees)


# Raise to the 3rd power **
num_three = 6
num_three **=3
# print(num_three)


# Raise to the 2nd Power **
data = 16
# data = **=2
# print(data)

# Integer division, how many times does 3 go into 16?
val_one = 16
val_one //=3
# print(val_one)

# Integer divide by 4 //
# val_two = 9
# val_two = //=4
# print(val_two)

# Modulus we use often to find a value is odd or even
# Find the remainder if divided by 3 %
val_three = 10
val_three %= 3
# print(val_three)


#Find the remainder if divided by 5 %
val_four = 14
val_four %= 5
# print(val_four)

# Refactor me !
fahrenheit = 89 # our temp to convert
celsius = (fahrenheit -32) * 5/9
#print(celsius)


fahrenheit -= 32 # parenthesis
fahrenheit *= 5/9
celsius = fahrenheit
# print(celsius)


''' Boolean Operators'''

# Is 7 less than 5? <
print(7 < 5)
result = (7 < 5)
# print("Is 7 less than 5?",result)

# Is 4 less than or equal to 4? <=
print(4 <= 4)
result = (4 <= 4)
# print("Is 4 less than or equal to 4?",result)

# Is 6 greater than 2? >
print(6 > 2)
result = (6 > 2)
# print("Is 6 greater than 2?",result)


# Is 5 greater than or equal to 6? >=
print(5 >= 6)
result = (5 >= 6)
# print("Is 5 greater than or equal to 6?",result)


# Is 5 equal to 5? ==
print(5 == 5)
result = (5 == 5)
# print("Is 5 equal to 5",result)


# Is 100 not equal to 75? !=
print(100 != 75)
result = (100 != 75)
# print("Is 100 not equal to 75",result)

# and
# print(2 == 2 and 3 == 1) #False
# Print

log_1 = (5 == 3)
log_2 = (4 == 7)
# print('log 1', log_1)
# print('log 2', log_2)
# print('log 1 and log 2',log_1 and log_2)

#or 
# print(5 == 5 or 5 == 3) # True if at least 1 is true

# not
is_it_autumn = True
# print(not is_it_autumn)

x = 5
y = 10

# Is x less than y? <
# print(x < y)

# Are We the same object. Is keyword
fname = 'Taylor'
first_name = 'Taylor'
# print(fname is first_name)
#print(fname == first_name)

# in
# print('J' in 'January')
# print('F' in 'March')

# Formatted string
pet = 'dog' # my variable to be used in my formatted string 
# print(f'I own a {pet}

# Homework Assignment below
'''
Write a program '''