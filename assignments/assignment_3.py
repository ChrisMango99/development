'''
Exercise - Valid email
Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()
An email address is valid if:
It has a "." at the third-to-last index
It has exactly one "@" symbol, at the fifth-to-last index or earlier
There is at least one character before the "@" symbol
It doesn't have any spaces (doesn't contain " ")
If all these conditions are met, print True. Otherwise, print False.
To do this, use boolean statements on your string.
Test your code on a few inputs to make sure it works!

'''

# Get input 
email = input("Hello, please enter your email: ") # Email is our variable and we are asking the user to input our email, which is chriskayembe@gmail.com

print(email) 

# Clean data

# Test 1: It has a "." at the third-to-last index

# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier

# Test 3: There is at least one character before the "@" symbol

# Test 4: It doesn’t have any spaces (doesn’t contain " ")

# Final Test with AND Keyword