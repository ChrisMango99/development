'''
Name: Chris Kayembe 
Assignment 3: Valid Email


'''

# Get input 
email = input("Hello, please enter your email: ") # Email is our variable and we are asking the user to input our email, which is chriskayembe@gmail.com
  


# Clean data 
email = email.strip() # We must sanitize the data using the strip method, the result is 22 so step is completed 

 

# Test 1: It has a "." at the third-to-last index

test_1 = (email[-4] == '.')
#print(f'Test 1:Does{email}has a "." at the third-to-last index?',test_1)


# Test 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier
test_2 = ('@' in email[-5::-1])
#print(f'test_2: {email} has exactly one "@" symbol, at the fifth-to-last-index?',test_2)


# Test 3: There is at least one character before the "@" symbol
test_3 = (email[0] != '@')
#print(f'Test 3: There is at least one character before the @ symbol in {email}',test_3)

# Test 4: It doesn’t have any spaces (doesn’t contain " ")
test_4 = (' ' not in email)
#print(test_4)


# Final Test with AND Keyword

all_tests = test_1 and test_2 and test_3 and test_4
#print(all_tests)

#This comes out as true. Therfore, we have a valid email address