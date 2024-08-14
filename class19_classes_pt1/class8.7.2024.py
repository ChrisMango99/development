import datetime
from datetime import datetime

''' Classes''' 


class Point2d():
    # This first method, is your constructor it builds your object
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # This is our string method, it delivers a string representation
    def __str__(self):
        return f'({self.x},{self.y})'
    
    # This will control the == operator
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # Mutator method
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    # Accessor methods
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    
point1 = Point2d(3, 5) # created an object of the class
point2 = Point2d(4, 11)

# print(point1)
# print(point2)

# __eq__
# print(point1 == point2)

#__add__
point3 = point1 + point2
# print(point3)

#__sub__
point4 = Point2d(10, 11)
point5 = point4 - point3
# print(point5)

#__lt__
# print(point1 < point2)

# Mutator method - set x
jeans_point = Point2d(5, 11)
jeans_point.set_x(25)
jeans_point.set_y(15)

# print(jeans_point)

my_x_value = jeans_point.get_x()
my_y_value = jeans_point.get_y()

# print(my_x_value, my_y_value)


''' Date Class'''

class Date:

    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.month:02d}/{self.day:02d}/{self.year}'
    
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
    
    def __lt__(self, other):
        selfdate = datetime(self.year, self.month, self.day)
        otherdate = datetime(other.year, other.month, other.day)
        if selfdate < otherdate:
            return True
        return False
    
    def is_leap_year(self):
        return True if self.year % 4 == 0 and (self.year % 100 !=0 or self.year % 400 == 0) else False
        


first_date = Date(2000, 10, 5)
second_date = Date(1999, 10, 5)

print(second_date.is_leap_year())

# print(first_date < second_date)
# second_date.is_leap_year()


