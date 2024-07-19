
''' Print statement outlining rules for your application'''
msg_1 = ('hello user, To sign up enter a username and password')
msg_2 = ('username must start with a lowercase letter, must only contain letters, numbers and underscores, and not have any spaces.')
msg_3 = ('The password must contain at least one digit, contain at least one special character, and not have any spaces.')

print(msg_1 ,msg_2, msg_3)



''' Initialize your variables, declaring variables 

We will need 2 variables to capture the username and password. Another 2 variables to use as the system username and password to authenticate against when we register
'''
system_username = 'chris99'
system_password = 'Mango_man'

username = ''
password = ''





''' Start your while loop '''
while system_username != username and system_password != password:
   username = input("Enter a username: ")
   password = input("Enter a password: ")  




if system_username == username and system_password == password:
    print("login successful")


elif system_username != username and system_password != password:
    print("incorrect info")
    
elif system_username == username and system_password != password:
    print('check password')
    
elif system_username != username and system_password == password:
    print('check username')



    




''' A List to handle error messages '''
error = ['Invalid Username', 'Invalid Password']

if username[0].isupper():
    print(error[0])

if password[1].isspace():
    print(error[1])






''' If we pass, congratulate the user and immediately ask them to register'''
if system_username == username and system_password == password:
    print("Sign in Complete")
if system_username!= username and system_password != password:
    print("Unable to Login try again")




''' If they input the correct matching info, program complete. If incorrect, send the user all the way back to the beginning of the loop to start from scratch. '''



