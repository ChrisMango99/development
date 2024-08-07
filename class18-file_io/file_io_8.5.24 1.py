import csv
import os
import pandas as pd


# Set our cwd as same folder of our python file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Lets try to create a file, see what happens

# f = open("my_file.txt")
'''
  File "c:\summer-2024-programming-concepts\class18_file_io\file_io 8.5.24.py", line 13, in <module>
    f = open("my_file.txt")
        ^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
'''

# Now lets try with the optional parameter to write
# f = open('my_file.txt', 'w')

''' 
Fun fact: Why is file closing important?

When you write to a file, Python may use a buffer to temporarily store the data before actually writing it to the disk. Closing a file forces the buffer to flush, meaning all data is physically written to the file, ensuring data integrity.

'''


'''
.read() Reads the entire file into a multi-line string
.readline() Reads one line of the file into a string
.readlines() Reads the entire file into a list, where each element in the list is a string representing one line.
'''


# Read
# with open('monday.txt', 'r') as monday:
#     output = monday.read()
#     print(output)


# Readline
# with open('monday.txt', 'r') as monday:
#     output = monday.readline()
#     print(output)


# Readlines
# with open('monday.txt', 'r') as monday:
#     output = monday.readlines()
#     print(output)


'''
Exercise
Create a program that reads a text file named "example.txt" and outputs the number of lines in the file.
(Assume your text file is in the same directory as your Python file)
Hint: Open the file in read-only mode, and use the .readlines() function.
'''

# Great work Akia
# with open('example.txt', 'r') as mon_day:
#     output = len(mon_day.readlines())
#     print(output)


'''Exercise
You are a data analyst who must analyze a company's sales data to determine which products are selling the best.
The data is stored in a CSV file named "sales_data.csv". The file contains the following columns: Product Name, Date Sold, Units Sold, Price per Unit, Total Sale
Write a Python script that reads the data from the CSV file and provides the product name and total sale
Make sure to ignore the first line, since that's the header.
You can go through the file line by line, and split each line into strings based on commas to get the individual column values.
You can keep track of each product and its total sale in a dictionary.
The only two relevant columns are Product Name and Total Sale.

https://docs.python.org/3/library/csv.html
'''

# # Dictionary to hold my data
# sales_dict = {}

# # Read the file in
# with open('sales_data.csv', 'r') as data:
#     output = next(data) # this nifty line of code, will remove our header
#     output = data.readlines()
# #     print(output)

# # Extract the data
# for o in output:
#     product_name, date, quantity, price, total = o.split(',')
#     sales_dict.update({product_name:total.strip()})

# print('With Python:',sales_dict)


# # With Pandas

# import pandas as pd

# df = pd.read_csv('sales_data.csv')
# result = df.set_index('Product Name')['Total Sale'].to_dict()
# print('With Pandas',result)



# '''
# .write(S) Insert the string S in a single line in the file.
# .writelines(L) For a list L containing strings, insert each string as a new line in the file.

# '''

# sales_data = ['Jibbers,12/1/2023,11, 5.67\n', 'Jabbers,11/30/2023,14, 6.75\n', 'Willers,10/12/2023,10, 4.50\n', 'Wonkers,12/3/2023,12, 8.00\n']

# Writelines
# with open('new_sales_data.csv', 'w') as file:
#     file.writelines(sales_data)

# Write
# with open('my_color.txt', 'w') as color:
#     userin = input("Please enter your favorite color: ")
#     color.write(userin)




'''
Exercise 
Create a program that asks the user for their name and favorite color, then writes this information to a new text file named "user_info.txt".
Write the name on the first line of the file, and the age on the second line of the file.
'''
# with open('user_info.txt', 'w') as file:
#     name = input("What is your name: ")
#     color = input("What is your favorite color: ")
#     file.write(name + '\n')
#     file.write(color)


'''
Append the animals in this list to a file called animals.txt

animals = ['dog', 'cat', 'bird', 'sheep', 'giraffe', 'gorilla']

How can we make sure that each animal is on a new line?
'''

# animals = ['dog', 'cat', 'bird', 'sheep', 'giraffe', 'gorilla']

# # with open('animals.txt', 'w') as file:
# #     file.writelines(animals)

# with open('animals.txt', 'a') as file:
#     file.writelines([a + '\n' for a in animals])



'''
Exercise - Tracking employee data

You work for a company that needs to keep track of employee data, such as name, age, and salary. Write a Python program that prompts the user to input data for each employee, and writes the data to a CSV file named "employee_data.csv".
The CSV file has the following columns: Name, Age, Salary
Until the user inputs "quit", keep prompting the user for employee data, and write it to the CSV file.
Remember to follow a CSV file format: Each line should be separated by commas and end in a newline.
'''
# columns = ['Name', 'Age', 'Salary'] # will be used to write our column headers

# with open('employee_data.csv', 'w') as file:
#     for c in columns:
#         file.write(c + ',')
#     file.write('\n')

# with open('employee_data.csv', 'a') as f:
#     writer = csv.writer(f)
#     while True:
#         name = input("What is your name?")
#         if name == 'quit':
#             break
#         age = input("What is your age?")
#         if age == 'quit':
#             break
#         salary = input("Please enter your salary?")
#         if salary == 'quit':
#             break
#         writer.writerow([name, age, salary])

''' Lets solve some problems with Pandas '''

# Create a dataframe out of the dictionary below and output a csv or excel file


 
data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
        {'area': 'cape-town',  'rainfall': 70, 'temperature': 25},
        {'area': 'mumbai',  'rainfall': 200,  'temperature': 39}]

df = pd.DataFrame.from_dict(data)

#df.to_csv('output.csv', index=False)
 


''' Create a dataframe from the above dictionary that does not include rainfall and output a csv or excel file with a timedatestamp on the filename'''


from datetime import datetime 
   
myts = datetime.today().strftime('%Y-%m-%d')

new_df = df[['area', 'temperature']]

new_df.to_csv(f'{myts}.csv', index=False)