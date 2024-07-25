''' Focus on the structure of your functions, let's have fun and learn how they work! :) '''


'''
1. Write as function that converts celsius to fahrenheit
''' 
# snake case for function names

# fahrenheit = (celsius * 9/5) + 32

def find_fahrenheit(temperature_in_celsius):
    fahrenheit = (temperature_in_celsius * 9/5) + 32
    print(fahrenheit)
   
# find_fahrenheit(float(input("Enter the temperature in celsius: ")))  # function call


def convert_c():
    celsius = float(input("Enter the temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in fahrenheit is: {fahrenheit}" )
 
# convert_c()
    
    



''' 2. write a function that generates a filename of lastname, firstname, and todays date'''

from datetime import date

firstname = 'bill'
lastname = 'smith'

def filename_gen(fname, lname):
    return f'{lname}_{fname}_{date.today()}.txt'

final_file_name = filename_gen(firstname, lastname)


# df.to_csv(final_file_name, index=False)




'''  3. Function to add two different numbers '''

num1 = 5
num2 = 17

num3 = 100
num4 = 55

def add_two(val1, val2):
    return val1 + val2

# print(add_two(num1, num2)) # one use
# print(add_two(num3, num4)) # two uses

result = add_two(1000, 500)
# print(result) # 1500 in terminal


'''   4. Function to reverse a word for example 'team' becomes 'maet' '''

newword = 'hollywood'
 
# print(string[::-1]) # reverse string
 
def reverse(string):
     return string[::-1]
 
# print(reverse(newword))




'''  5. Function that will deliver the average of 2 values '''
from statistics import mean

num1 = 55
num2 = 70

def average(a, b):
    average = mean([a, b])
    return average

# print(average(num1, num2))




''' 
 6. Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
word = 'hooray'

def vowel_check(word):
    
    vowels = 'aeiou'
    for w in word:
        if w in vowels:
            print(f'{w} is a vowel')
        else:
            print(f'{w} is not a vowel')
     

# vowel_check(word)


# calling function within a function

def is_vowel(letter):
  vowels = ['a','e','i','o','u']
  if letter in vowels:
    return "vowel"
  else:
    return "not a vowel"

# def check_word_for_vowels(word):
#   for letter in word:
#     print(f"{letter}: {is_vowel(letter)}")

# check_word_for_vowels("expialidocious")



'''  7. Write a function that takes a list of these dictionary items. Return the first names from the list of dictionaries in a single list

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 21}]'''

students = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 22},
            {'name': 'Charlie', 'age': 21}]


def first_name(students): # this function accepts a list of dictionaries
   output = [] # this will hold our first names
   for s in students:
      name = s['name']
      output.append(name)
   return output
      
students_first_names = first_name(students)

# print(students_first_names)
# print(type(students_first_names))







''' Let's print from our functions'''

''' 8.  Create a function that asks the user for their name and greets them back with a hello'''

def say_hello(fname, lname):
    print(f'Hello {fname} {lname}')

# say_hello(input("What is your first name"), input("What is your last name"))



''' If we print we return none'''
def show_none(word):
    print(word)

# print(show_none('hello')) # the print statement will display the return value


''' 9.  Write a function that takes a list of students grades, return a dictionary with the students names and grade averages

students = [{'name': 'Alice', 'science':75, 'math':80, 'world history': 90},\
            {'name': 'Bob', 'science':50, 'math':65, 'world history': 88},\
            {'name': 'Charlie', 'science':100, 'math':75, 'world history': 70}]

'''

students = [{'name': 'Alice', 'science': 75, 'math': 80, 'world history': 90},
            {'name': 'Bob', 'science': 50, 'math': 65, 'world history': 88},
            {'name': 'Charlie', 'science': 100, 'math': 75, 'world history': 70}]


def gpa(students):
    grade_averages = {}
    
    for s in students:
        name = s['name']
        science = s['science']
        math = s['math']
        world_history  = s['world history']
        gpa = (science + math + world_history) / 3
        grade_averages.update({name:gpa})
    return grade_averages

# report_card = gpa(students)
# print(report_card)



# gpa(students)


'''
10.
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'withdrawal'},
                {'id': 'b', 'amount': 1350, 'type': 'deposit'},
                {'id': 'c', 'amount': 1000, 'type': 'deposit'},
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'},
                {'id': 'a', 'amount': 1000, 'type': 'deposit'},
                {'id': 'a', 'amount': 75, 'type': 'deposit'},
                {'id': 'a', 'amount': 60, 'type': 'deposit'},
                {'id': 'b', 'amount': 13, 'type': 'withdrawal'}]

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]


def account_balances(transactions):
    
    balances = {} # this dictionary will have our final balances

    for t in transactions:
        transaction_type = t['type']
        amount = t['amount']
        transaction_id = t['id']
        # if the dictionary does not contain the id, add it and update the amount initially
        if transaction_id not in balances:
            balances.update({transaction_id: amount})
        # otherwise it means the id exists, we can now check fo rtype and add or subtraction
        else:
            if transaction_type == 'deposit':
                balances[transaction_id] = balances.get(transaction_id) + amount
            else:
                balances[transaction_id] = balances.get(transaction_id) + amount
         
    return balances
                

result = account_balances(transactions)
print(result)





