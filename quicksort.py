#!/usr/bin/python

"""
Quicksort:

1. Set the pivotelement as the last element, a[e]
2. Set the pindex to s
3. Iterate over range s, e-1
4. if element at pindex is less than the pivotelement, swap elements at pindex and i and increment pindex
5. finally, swap the elements at a[pindex] and a[e]
6. return pindex

Example:
a = [21, 74, 7, 64, 53]
pivotindex calculation
s = 0 => a[0] = 21 and e = 4 a[4] = 53
set pivotelt to 53
set pindex to s. pindex =0
i in range(0,4),
if a[i] <= pivotelt
21 < 53 True, swap 21 with a[pindex]. array = [21,74,7,64,53], pindex = 1
74 < 53 False
7 < 53 True, swap 7 with a[1]. array = [21,7,74,64,53], pindex = 2
64 < 53 False

The loop ends. Swap a[e] with a[pindex]
array = [21,7,53,64,74]. Return pindex value = 2

"""

import random


def partition(a, s, e):
    pivotelt = a[e]
    pindex = s
    for i in range(s, e - 1):
        if a[i] <= pivotelt:
            a[i], a[pindex] = a[pindex], a[i]
            pindex += 1

    a[pindex], a[e] = a[e], a[pindex]
    return pindex


def quicksort(a, s, e):
    if s < e:
        pivotindex = partition(a, s, e)
        quicksort(a, s, pivotindex - 1)
        quicksort(a, pivotindex + 1, e)


a = random.sample(range(100), 10)
print a
s = 0
e = len(a) - 1
quicksort(a, s, e)
print a
