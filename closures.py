"""
Got the example and an undestanding of closures from Corey Schafer's video:
https://youtu.be/swU3c34d2NQ
https://github.com/CoreyMSchafer/code_snippets/blob/master/Closures/closure.py

Decorators:
When a function takes a function as an argument and it returns a function, it is called as a decorator.
Typically, we use decorators for recording log messages
In order to understand decorators, we need to get a hang of closures.

Here, logger is our outer function that takes func as its argument and log_func is the inner function that takes multiple arguments.

It accepts a function as an argument -> say logger(addition)
Within logger we define another function (inner function), log_func(*args), which takes the arguments passed to addition()

In this example, we pass a function as an arg to the outer function and returns log_func, which is also a function.
We then pass the variables to the returned log_func object, which is nothing but the inner function, where we evaluate the answer to the values that we are passing.

Confusing, right?
"""

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

"""
logger is our outer function, it takes func as an argument. We pass addition (a function) as our arg
"""


def logger(func):
    """
    log_func is our inner function, it takes multiple arguments and we pass 3,3, etc as our arguments.
    """
    print "Step 2 - addition() is passed to the logger function and the object is stored in the func variable"

    def log_func(*args):
        print "Step 5 - log_func gets 3, 3 as its arguments and we log it out in our log file"
        logging.info(
            'Running %s with arguments %s' % (func.__name__, args))
        print "Step 6 - We pass 3, 3 to func, which is addition(*args) = addition(3,3)"
        print "Result: The output is ", (func(*args))

    print "Step 3 - Outer function returns the object of log_func, which is the inner function. Now, addition_logger will contain the object of log_func"
    """
    if we print log_func and addition_logger, we will get the same object value.
    print log_func -> <function log_func at 0x1023211b8>
    """
    return log_func


def addition(x, y):
    return x + y


def subt(x, y):
    return x - y

# The program starts its execution here.
if __name__ == '__main__':
    print "Step 1 - Passing addition() to logger() - outer function"
    addition_logger = logger(addition)
    # print addition_logger -> <function log_func at 0x1023211b8>
    print "Step 4 - We now pass 3, 3 to the addition_logger function. The inner function will now be called as addition_logger = log_func"
    addition_logger(3, 3)

    """
    # Sample for subtraction
    subt_logger = logger(subt)
    subt_logger(7,3)
    """

"""
Sample Output:
Step 1 - Passing addition() to logger() - outer function
Step 2 - addition() is passed to the logger function and the object is stored in the func variable
Step 3 - Outer function returns the object of log_func, which is the inner function. Now, addition_logger will contain the object of log_func
Step 4 - We now pass 3, 3 to the addition_logger function. The inner function will now be called as addition_logger = log_func
Step 5 - log_func gets 3, 3 as its arguments and we log it out in our log file
Step 6 - We pass 3, 3 to func, which is addition(*args) = addition(3,3)
Result: The output is  6


Log file: cat example.log

INFO:root:Running addition with arguments (3, 3)
"""
