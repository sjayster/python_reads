#!/usr/bin/python

import random


def merge(l, r, a):
    nl = len(l)
    nr = len(r)
    i, j, k = 0, 0, 0

    while i < nl and j < nr:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1

        else:
            a[k] = r[j]
            j += 1

        k += 1

    while i < nl:
        a[k] = l[i]
        i += 1
        k += 1

    while j < nr:
        a[k] = r[j]
        j += 1
        k += 1


def mergesort(a):
    length = len(a)
    if length < 2:
        return

    m = length / 2
    l = a[:m]
    r = a[m:length]
    mergesort(l)
    mergesort(r)
    merge(l, r, a)

a = random.sample(range(100), 10)
print a
mergesort(a)
print a
