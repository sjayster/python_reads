"""
https://youtu.be/FsAPt_9Bf3U
Corey Schafer decorators tutorial
"""
"""
Case 1: Basic decorator function
"""
"""
def outer_fun():
    msg = "Defined in outer function"

    def inner_fun():
        print "Printing msg var defined in outer function -> ", msg

    return inner_fun()

outer_fun()
outer_fun()

"""
"""
Calling outer_fun() will initialize msg and runs inner_fun()
Inner_fun prints out the print statement defined in it.
Calling outer_fun() again and again would make it

Output:
Printing msg var defined in outer function ->  Defined in outer function
Printing msg var defined in outer function ->  Defined in outer function
"""

##########################################################################

"""
Case 2: Returning function object instead of executing it
Passing arguments to inner function
"""

"""
def outer_fun():
    def inner_fun(*args):
        print "Object o sent me the following message \t", args

    print "Outer function here. I am returning an object to the inner function"
    return inner_fun

o = outer_fun()
o("Calling inner function once")
o(2, "Calling inner function twice")
o("Cheerio", "Adios", "Arrivederci")

"""
"""
Here, outer_fun() just returns an object to the inner function. The function is stored in variable o
So, o == inner_fun(). You can send the arguments to o, just the way you to inner_fun() if you were to invoke it separately.

Output:
Outer function here. I am returning an object to the inner function
Object o sent me the following message 	  ('Calling inner function once',)
Object o sent me the following message 	  (2, 'Calling inner function twice')
Object o sent me the following message 	  ('Cheerio', 'Adios', 'Arrivederci')
"""

##########################################################################
"""
"""
"""
Case 3: Decorators
"""

"""


def decorator_fun(original_fun):
    def wrapper_fun():
        print "Executing wrapper code before running %s" % original_fun.__name__
        return original_fun()

    return wrapper_fun


def displayfun():
    print "I am in display function"

dec_obj = decorator_fun(displayfun)
dec_obj()

# The above code can be represented as follows


def decorator_fun(original_fun):
    def wrapper_fun():
        print "Executing wrapper code before running %s" % original_fun.__name__
        return original_fun()

    return wrapper_fun


@decorator_fun
def displayfun():
    print "I am in display function"

displayfun()

"""
"""
Output:

Executing wrapper code before running displayfun
I am in display function
Executing wrapper code before running displayfun
I am in display function

"""

"""
Case 4: Decorators with arguments
As we can see, we are using the decorator with displayfun() and displayinfo().
However, displayinfo takes 2 args whereas displayfun() takes None
If we run the code with wrapper_fun(), we will get an argument error.
In order to overcome this, we always define the wrapper function with *args and **kwargs as its variables.
"""

"""


def decorator_fun(original_fun):
    def wrapper_fun(*args, **kwargs):
        print "Executing wrapper code before running %s" % original_fun.__name__
        return original_fun(*args, **kwargs)

    return wrapper_fun


@decorator_fun
def displayfun():
    print "I am in display function"


@decorator_fun
def displayinfo(name, age):
    print "The user %s is %s years old" % (name, age)


displayinfo("Bruno", 28)
displayfun()

"""
"""
Output:

Executing wrapper code before running displayinfo
The user Bruno is 28 years old
Executing wrapper code before running displayfun
I am in display function
"""


"""
Case 5: Using classes as decorators
"""


class decorator_class(object):

    def __init__(self, original_fun):
        self.original_fun = original_fun

    def __call__(self, *args, **kwargs):
        print "Executing call method before running %s" % self.original_fun.__name__
        return self.original_fun(*args, **kwargs)


@decorator_class
def displayfun():
    print "I am in display function"


@decorator_class
def displayinfo(name, age):
    print "The user %s is %s years old" % (name, age)


displayinfo("Louis", 18)
displayfun()

"""
Output:

Executing call method before running displayinfo
The user Louis is 18 years old
Executing call method before running displayfun
I am in display function
"""
