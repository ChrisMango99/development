from module import BankAccount

taras_acct = BankAccount('Tara Jones', [{"type": "deposit", "amount": 500, 'transaction date':'2010-05-09'},
{"type": "withdrawal", "amount": 200, 'transaction date':'2023-05-09'},
{"type": "withdrawal", "amount": 100, 'transaction date':'2020-05-09'},
{"type": "deposit", "amount": 50, 'transaction date':'2024-05-09'},
{"type": "deposit", "amount": 75, 'transaction date':'1999-05-09'},
{"type": "withdrawal", "amount": 60,'transaction date':'2010-05-09'}], 1000)





'''
When a script is run, and the script imports py files, different __name__ values are assigned to the script and the imported py files.

where "__main__" is assigned to the running script, and different __name__ values are assigned to the imported files.

Also, importing py files will automatically execute their contents. If you put the "if __name__" statement in each of the imported py file, the file will check its own __name__ value first. Since the "__main__" is only assigned to the running script, that means the imported py files will stop executing after the if-statement.

'''









