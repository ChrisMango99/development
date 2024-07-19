'''
Chris Kayembe
Project 1: Website Sign in

'''


''' Print statement outlining rules for application'''
msg_1 = ('hello user, To sign up enter a username and password')
msg_2 = ('username must start with a lowercase letter, must only contain letters, numbers and underscores, and not have any spaces.')
msg_3 = ('The password must contain at least one digit, contain at least one special character, and not have any spaces.')

print(msg_1 ,msg_2, msg_3) 



''' 

Initialize your variables, declaring variables 

Below are the two variables for this program 
'''
system_username = 'chris99'
system_password = 'Mango_man'

username = ''
password = ''



''' While Loop'''
while system_username == username and system_password == password:
   print('Type Username and Password')
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

#print statements after inputing correct information

if system_username == username and system_password == password:
    print("Sign in Complete")
if system_username!= username and system_password != password:
    print("Unable to Login try again")







