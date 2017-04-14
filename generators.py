#! /usr/bin/python

# Generate fib sequence


def sample_gen(num):
    a, b = 0, 1
    while num:
        yield a
        a, b = b, a + b
        num -= 1

print "Calling generator"
x = sample_gen(5)
print "Using next() to print the next value"
print x.next()
print x.next()

print "Calling generator function in a for loop"
for i in sample_gen(12):
    print i
