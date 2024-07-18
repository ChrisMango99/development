
''' Print statement outlining rules for your application'''
msg_1 = input('hello user, please read the username and password requirements to log in. Press OK to continue:')
msg_2 = input('The username must start with a lowercase letter, It must only contain letters, numbers and underscores, It must not have any spaces. Type OK to continue:')
msg_3 = input('The password must contain at least one digit, contain at least one special character, and not have any spaces. Type OK to continue:')

print(msg_1, msg_2,msg_3)


''' Initialize your variables, declaring variables 

We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
system_username , system_password = 'chris99','mango_man'
username , password = '',''



''' A List to handle error messages '''
errors = ['Please check username format', 'please check password format']

username_format_error = errors[0]

username = 56

if username != 55:
    print(username_format_error)


''' Start your while loop '''





''' Get your username and password'''


''' Test your username and enforce logic'''


''' Test your password and enforce logic'''



''' If we pass, congratulate the user and immediately ask them to register'''




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



