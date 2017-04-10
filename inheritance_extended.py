"""
https://youtu.be/jCzT9XFZ5bw?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

Inheritance
Super
Property decorator

"""

#! /usr/bin/python


class Employee(object):

    # Class variables
    raise_percent = 10
    ouremployees = []

    def __init__(self, fname, lname, pay, title):
        self.fname = fname
        self.lname = lname
        self.name = self.fname + ' ' + self.lname
        self.pay = pay
        self.title = title
        Employee.ouremployees.append(self.name)
        """
        Above line is pertinent to the entire class, so it makes sense to have it common across the class.
        If it is given as self.num_employees, then for each object/instance of a class, the value will be set to 1
        """

    @property
    def email(self):
        """
        This function is setup as a property decorator so that if anyone changes their name, the change can be reflected on their email ID
        """
        return "%s_%s@company.com" % (self.fname, self.lname)

    def getname(self):
        return self.name

    def setpay(self):
        self.pay += (self.pay * self.raise_percent) / 100

    def getpay(self):
        return self.pay

    """
    Use str to depict the object to the end user - readable. Cannot be passed to eval()
    
    Use repr to return a printable representation the object to the developers - unambiguous.
    repr returns a lot more info - like module, etc

    functions starting with __ are special functions - These methods can be overridden
    """

    def __str__(self):
        return "The employee name and pay is %s %s" % (self.name, self.pay)

    def __repr__(self):
        return "Employee(%s, %s, %s)" % (self.name, self.pay, self.title)


class Developer(Employee):
    """
    If the dev needs to get a 20% hike, just set the raise_percent to whatever you want.
    If nothing is specified, the raise_percent defined in the parent class would be used.
    """
    raise_percent = 20

    def __init__(self, fname, lname, pay, title, language):
        """
        We don't want to mess with the name and pay.
        We want the Employee class to take care of it. So we put that in the super function.
        We only care about the language.
        """
        super(Developer, self).__init__(fname, lname, pay, title)
        self.language = language

    """
    Get the combined salary of 2 developers. 
    If we do not define a __add__ method and just do dev1 + dev2, we will get a type error.
    self is obj1, say dev1 and other is obj2 is dev2
    """

    def __add__(self, other):
        return self.pay + other.pay


class Manager(Employee):

    def __init__(self, fname, lname, pay, title, directreports=None):
        super(Manager, self).__init__(fname, lname, pay, title)

        if directreports is None:
            self.directreports = []
        else:
            self.directreports = directreports

    def addrep(self, rep):
        if rep not in self.directreports:
            self.directreports.append(rep)

    def removerep(self, rep):
        if rep in self.directreports:
            self.directreports.remove(rep)

    def printreports(self):
        print "%s manages" % (self.name)
        for rep in self.directreports:
            print "-->", rep.name

emp1 = Employee("Frank", "Lampard", 100000, "CEO")

print "\nRepr and str representation"
print repr(emp1)
print str(emp1)

print "#" * 25
dev1 = Developer("Great", "Gatsby", 30000, "Sw Engg 2", "Java")
dev2 = Developer("Harry", "Styles", 20000, "Sw Engg 1", "Ruby")
mgr1 = Manager("Stan", "Smith", 50000, "Manager", [dev1])
mgr1.addrep(dev2)
mgr1.printreports()

print "#" * 25
print "\nSetting email using property decorator"
print dev1.email
dev1.fname = "John"
print dev1.email


print "#" * 25
print "\nThe combined salary of all the devs in the company is ", dev1 + dev2
print "Employees in this is company are"
for emps in Employee.ouremployees:
    print emps

print "#" * 25
print "\nIs instance or subclass"
print isinstance(mgr1, Employee)
print isinstance(mgr1, Developer)
print issubclass(Manager, Developer)
print issubclass(Manager, Employee)

"""
Output:

Repr and str representation
Employee(Frank Lampard, 100000, CEO)
The employee name and pay is Frank Lampard 100000
#########################
Stan Smith manages
--> Great Gatsby
--> Harry Styles
#########################

Setting email using property decorator
Great_Gatsby@company.com
John_Gatsby@company.com
#########################

The combined salary of all the devs in the company is  50000
Employees in this is company are
Frank Lampard
Great Gatsby
Harry Styles
Stan Smith
#########################

Is instance or subclass
True
False
False
True
"""
