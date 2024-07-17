

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {'user_id': 400,
            'fname':'Fritz'}

# print(user_data)
# print(type(user_data))


# Bracket notation - we can grab the value by referencing the key
# print(user_data["fname"])
# print(user_data["user_id"])

#  Add new key/value pair
user_data['address'] = 'elm street'
# print(user_data)

# lets look at all the methods available to us
# print(dir(user_data))

# lets try one
#print(user_data. __contains__('user_id')) # Basically looks if a certain variable is in a list or dictionary 

# Dict constructor
new_dict = dict()
# print(new_dict)
# print(type(new_dict))

# Let's update our name key
user_data = dict(user_id = 400, fname = 'Daisy')
# print(user_data)


# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Let's look at our keys
print(f' The keys for this dog dictionary are {dog.keys()}')

# or set it as a variable?



# Lets use the values methods to get the values from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets look at our values


# or set to a variable

# Lets use clear method to remove all elements

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets use get method to get a key value

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}



# lets look at one of the parameters to show an error if the key doesnt exist



# Lets create a copy

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}





# Lets remove a specified key with pop
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}


# Lets remove a last inserted key-value pair with popitem
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}


# Get a list with each key-value pair with items
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}




# we can loop through
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}



# Update dictionary
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}



# Update can also update current key value pairs, as well as adding



# Dictionaries vs Lists
# list1 = ['a', 'b', 'c', 'd', 'e']
# dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}





'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]




''' Zip Solution

When you use the zip() function in Python, it takes two or more data sets and "zips" them together. This returns an object containing pairs of items derived from the data sets. 
'''

my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]





'''
Exercise

Write a dictionary that five countries and their languages Then have your code print the languages of each country one at a time.
Hint: Use the items() method


'''

languages = { 'USA': 'English', 'Mexico': 'Spanish', 'France': 'French', 'Portugal':'Portugese', 'Belgium':'Dutch' }
    



# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}



# Lets make a dataframe out of this


# Lets rename the columns




'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list




# What about the count method for Lists?? 


# from statistics import mode



'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},
           {'name': 'David', 'title': 'developer', 'salary': 65000}]




# import pandas as pd













 



