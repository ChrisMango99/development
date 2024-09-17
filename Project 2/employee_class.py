'''Chris Kayembe     
 8-22-24
Employee Class
'''
from datetime import datetime
import math

class Employee:
    ''' Documentation for our Employee Class'''
    def __init__(self, name: str, job_title: str,department: str,salary: float,hire_year: str):
        self.name = name 
        self.job_title = job_title 
        self.department = department 
        self.salary = salary 
        self.hire_year = hire_year

    def __str__(self) -> str:  
        return (f"Employee(name={self.name}, job_title={self.job_title}, "  
                f"department={self.department}, salary={self.salary}, "
                f"hire_year={self.hire_year})")
    
# Step 3: Years Worked

    def years_worked(self):
        return datetime.now().year - self.hire_year
    
    
    def total_expense(self):                        # Total Expense Method 
        return self.salary * self.years_worked()
    


    def print_employee_information(self):
        print(f"Name: {self.name}")
        print(f"Job Title: {self.job_title}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Hire Year: {self.hire_year}")
        print(f"Years Worked: {self.years_worked()}")
        print(f"Total Expense to Company: ${self.total_expense():,.2f}")



    def get_name(self):                # Accessor methods
        return self._name

    def get_years_worked(self):
        return self._years_worked

    def get_total_expense(self):
        return self._total_expense
    

    def set_name(self, name):              # Mutator methods
        self._name = name

    def set_years_worked(self, years_worked):
        self._years_worked = years_worked

    def set_total_expense(self, total_expense):
        self._total_expense = total_expense






employee1 = Employee('Chris Kayembe' , 'Cyber Janitor' , 'IT' , 100000 , 2023) 
#print(employee1)
employee1.print_employee_information()