#!/usr/bin/python


class parent(object):
    count = 100

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def printnums(self):
        print "PARENT: 1st number is ", self.num1
        print "PARENT: 2nd number is ", self.num2
        print "PARENT: Count is ", parent.count

    def changenums(self, newnum1, newnum2):
        self.num1 = newnum1
        self.num2 = newnum2

    @classmethod
    def setcount(cls, count):
        cls.count = count


class child(parent):

    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

        # If you want the child to have its own instance of num1 and num2, we
        # use super. By doing that, the child can also have num1 and num2 with
        # same or different values
        print "CHILD: I am going to alter num1 and num2 for the child class using super"
        super(child, self).__init__(1, 2)

    def printwords(self):
        print "CHILD: 1st word is ", self.word1
        print "CHILD: 2nd word is ", self.word2

    def getparentnums(self):
        print "CHILD: Num1 of parent is ", self.num1
        print "CHILD: Num2 of parent is ", self.num2
        print "CHILD: Count value is  ", child.count

if __name__ == "__main__":
    parentobj = parent(10, 20)
    parentobj.printnums()
    # If this line is not included, the count value will be 100
    print "#" * 25
    print "Changing the numbers and count to 100,200 and 250 respectively."
    parentobj.changenums(100, 200)
    parent.count = 250
    parentobj.printnums()

    print "#" * 25
    print "Creating a child object with count = 50"
    childobj = child("child", "class")
    childobj.printwords()
    childobj.setcount(50)
    childobj.getparentnums()

    print "#" * 25
    print "The parent instance still has its original values"
    parentobj.printnums()

"""
Output:

PARENT: 1st number is  10
PARENT: 2nd number is  20
PARENT: Count is  100
#########################
Changing the numbers and count to 100,200 and 250 respectively.
PARENT: 1st number is  100
PARENT: 2nd number is  200
PARENT: Count is  250
#########################
Creating a child object
CHILD: I am going to alter num1 and num2 for the child class using super
CHILD: 1st word is  child
CHILD: 2nd word is  class
CHILD: Num1 of parent is  1
CHILD: Num2 of parent is  2
CHILD: Count value is   50
#########################
The parent instance still has its original values
PARENT: 1st number is  100
PARENT: 2nd number is  200
PARENT: Count is  250
"""
