

''' I scoured the interwebs and found some fun problems for us to solve! Lets work through these and have fun learning along the way '''


'''
You have 2 lists, extract and remove the data from one list and place the items in the other. Print your result
'''

first_list = [1,2,3,4,5,6,7,8,9,10]

second_list = []




'''
Write a  Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes', 'pop', 'racecar', 'bob', 'lol']
Output:
[False, True, True, False, False]

'''

palindrome_test_list = ['palindrome', 'madamimadam', '', 'foo', 'eyes', 'pop', 'racecar', 'bob', 'lol']




'''

Write a Python program to find the length of a given list of non-empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
'''

my_list = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']


'''
 Write a  Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
Input: 123456789
Output:
945
Input: 2468
Output:
0
Input: 13579
Output:
945

'''

test_string = '123456789'

# Put string into a list
make_list = [int(t) for t in test_string]
#print(make_list)
 

# Pull out odd numbers
odd_nums = [n for n in make_list if n % 2 != 0]
print(odd_nums)

# Detrimine product
import numpy as np
result = np.prod(odd_nums)
print(result)



'''
Write a  Python program to find the largest k numbers from a given list of numbers.
Input: [1, 2, 3, 4, 5, 5, 3, 6, 2]

Try it with a for loop!
Is there a function in Python that will do this for us??

'''

test_list = [1, 2, 3, 4, 5, 5, 3, 6, 2]





'''
Please turn this:
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

into this:
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
'''

convert_me = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




