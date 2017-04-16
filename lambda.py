#!/usr/bin/python

# Lambda, map, filter and reduce

"""
http://www.python-course.eu/lambda.php
Lambda is an instant, anonymous and throwaway function
A sequence can be applied to the lambda function using the map function
Example: Sum of elements in two list
"""

list1 = [1, 3, -4, 15, -8, 0, 12]
list2 = [0, -4, -3, -14, 9, 34, -19]

"""
Define lambda as a function that takes x and y and returns its sum
variables on the left, function on the right
The current lambda function takes 2 arguments, we can pass list1 and list2 to it. 
When we pass it in the map function, it automatically iterates through both the list and returns the sum of list1[i] + list2[i]
"""
answer = map(lambda x, y: x + y, list1, list2)
print answer
"""
If we want to filter out the answers that are lesser than 0, we can use the filter operation with the lambda function
We can do the same using map, but it will return only True or False and not the number
"""

print filter(lambda x: x < 0, answer)

# filter vs map
print "Difference between filter and map"
print filter(lambda x: x % 2 == 0, list1)
print map(lambda x: x % 2 == 0, list1)

"""
Reduce is used to apply a function to a sequence.
function will be applied on l[0], l[1] and return say temp
Now function will be applied on temp and l[2] and so on
"""
# To get the sum of the list
print reduce(lambda x, y: x + y, list1)

"""
[1, -1, -7, 1, 1, 34, -7]
[-1, -7, -7]
Difference between filter and map
[-4, -8, 0, 12]
[False, False, True, False, True, True, True]
19
"""
