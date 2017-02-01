#!/usr/bin/python

# http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/


def args_pass(single, *args, **kwargs):
        # single takes in one argument. *args takes up multiple arguments
        # indefinitely and kwargs takes up key value pairs

    print "The first argument is %s" % single
    i = 2
    for arg in args:
        print "Argument # %s is %s" % (i, arg)
        i += 1

    for k, v in kwargs.items():
        print "Printing arguments passed in as dictionary"
        print "Key is %s, value is %s " % (k, v)

    print "the end"

args_pass("one", "two", "three", "four", key1='val1', key2='val2')

"""

python argument_passing.py 
The first argument is one
Argument # 2 is two
Argument # 3 is three
Argument # 4 is four
Printing arguments passed in as dictionary
Key is key2, value is val2 
Printing arguments passed in as dictionary
Key is key1, value is val1 
the end

"""
