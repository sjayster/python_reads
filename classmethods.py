class Employee:

    # Class variables. Should be accessed as classname.var
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        # Setting the class variable - Will be the same across multiple objects
        Employee.num_of_emps += 1

    @classmethod
    def converter(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @classmethod
    def setraise(cls, new_raise_amt):
        cls.raise_amt = new_raise_amt

    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    """
    Let us say we have a function that computes whether the day is a weekday or not.
    This function does not use any of the class variables. So we will define it as a static method.
    """
    @staticmethod
    def is_workday(day):
        # Using datetime module: 0 -> Monday, 6-> Sunday
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

print "Creating new_emp_1 object the traditional way"
new_emp_1 = Employee(first, last, pay)
print "Number of employees = ", Employee.num_of_emps

print "Creating new_emp_2 object using the converter class method that we had written"
# This takes in emp-str-2 and splits it as first, last and pay and passes
# it to the parent class and returns the object
new_emp_2 = Employee.converter(emp_str_2)
print "Number of employees = ", Employee.num_of_emps

print "\nPrinting raise amount on all objects and across the class\n"
print "raise_amount accessed as class variable = ", Employee.raise_amt
print "raise_amount accessed from new_emp_1 object = ", new_emp_1.raise_amt
print "\nSetting the raise_amount to 1.5"
Employee.setraise(1.5)
print "\nraise_amount accessed from new_emp_2 object = ", new_emp_2.raise_amt

print "\n\nPrinting new_emp_1 details"
print new_emp_1.email
print new_emp_1.pay
print new_emp_1.fullname()

print "\n\nPrinting new_emp_2 details"
print new_emp_2.email
print new_emp_2.pay
print new_emp_2.fullname()

import datetime
mydate = datetime.date(2016, 10, 10)
print "Is the given day a weekday? ", Employee.is_workday(mydate)
"""

Output:

Creating new_emp_1 object the traditional way
Number of employees =  1
Creating new_emp_2 object using the converter class method that we had written
Number of employees =  2



Printing raise amount on all objects and across the class
raise_amount accessed as class variable =  1.04
raise_amount accessed from new_emp_1 object =  1.04


Setting the raise_amount to 1.5
raise_amount accessed from new_emp_2 object =  1.5



Printing new_emp_1 details
John.Doe@email.com
70000
John Doe



Printing new_emp_2 details
Steve.Smith@email.com
30000
Steve Smith
"""
