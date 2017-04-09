"""
To use multiple decorators on top of the same function, we need to use the functools module and import wraps
Then on top of every wrapper, we need to include @wraps(argument_present_in_the_decorator_function)
"""

from functools import wraps
import time
import logging


def deco_logger(original_fun):
    # original_fun here is our display_info()
    logging.basicConfig(filename="%s.log" %
                        (original_fun.__name__), level=logging.INFO)
    logging.info("Logging %s()" % (original_fun.__name__))

    @wraps(original_fun)
    def wrapper(*args, **kwargs):
        print "Step 3 - The wrapper in deco_logger is to be executed and the details are logged to the logfile."
        logging.info("The args are %s and the kwargs are %s" % (args, kwargs))
        # The below return statement would send the control to the wrapper
        # defined in deco_timer
        return original_fun(*args, **kwargs)

    print "Step 2 - Calls the wrapper function defined above, with the args passed to display_info()"
    return wrapper


def deco_timer(original_fun):

    @wraps(original_fun)
    def wrapper(*args, **kwargs):
        print "Step 4 - Wrapper in deco timer is to be executed."
        t1 = time.time()
        result = original_fun(*args, **kwargs)
        t2 = time.time() - t1
        print "Function %s ran for %s seconds" % (original_fun.__name__, t2)
        # The below line will send the control back to the main()
        return result
    print "Step 1 - Passes the wrapper function (display_info) to deco_logger"
    return wrapper

# Works as logger(timer(display_info))


@deco_logger
@deco_timer
def display_info(name, age):
    time.sleep(1)
    print "Step 5 - Called by the wrapper in deco_timer()"
    print "User %s is %s years old" % (name, age)

display_info("Messi", 11)
print "Step 6 - Finish"

"""
Output:

Step 1 - Passes the wrapper function (display_info) to deco_logger
Step 2 - Calls the wrapper function defined above, with the args passed to display_info()
Step 3 - The wrapper in deco_logger is to be executed and the details are logged to the logfile.
Step 4 - Wrapper in deco timer is to be executed.
Step 5 - Called by the wrapper in deco_timer()
User Messi is 11 years old
Function display_info ran for 1.00046300888 seconds
Step 6 - Finish

cat display_info.log

INFO:root:Logging display_info()
INFO:root:The args are ('Messi', 11) and the kwargs are {}

"""
