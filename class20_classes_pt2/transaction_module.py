import datetime

''' Bank Account Class Requirements

Attributes:

owner: a string representing the name of the account owner
balance: a float representing the current balance of the account
transactions: a list representing the history of transactions made on the account

Methods:

deposit(amount): adds the specified amount to the account's balance and records the transaction in the transactions list

withdraw(amount): subtracts the specified amount from the account's balance (if there are sufficient funds) and records the transaction in the transactions list

__str__(): returns a string representation of the bank account. What information do you want to display in this string? What might be okay to leave out? How do you want to format it?

get_balance(): returns the current balance of the account

get_transactions(): returns a list of all the transactions made on the account

get_transaction_count(): returns the total number of transactions made on the account

get_transaction_history(): returns a string representation of the transaction history, including the type (deposit or withdrawal) and amount for each transaction

Let's expand our BankAccount class so each transaction has a date. Make sure to keep track of transactions in chronological order.

When we make classes in Python, each class should be its own Python file.
The Python file is considered a module.
If you write code in a different file that uses the class, you must import the class.
Let's say your class is called BankAccount, your class is in the file module.py, and your code using your class is in the same folder.
To import the entire module, use this line of code:
import module
To import just the class, use this line of code:
from module import BankAccount

'''
