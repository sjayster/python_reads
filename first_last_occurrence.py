def occur(a, s, e, n, f):
    first = -1
    last = -1
    while s <= e:
        m = (s + e) / 2
        if a[m] < n:
            s = m + 1

        elif a[m] > n:
            e = m - 1

        else:
            if not f:
                last = m
                s = m + 1
            else:
                first = m
                e = m - 1

    if f:
        return first
    return last


a = [1, 2, 3, 4, 5, 5, 6, 7, 7, 7]
s = 0
e = len(a) - 1
print occur(a, s, e, 7, f=True)
print occur(a, s, e, 7, f=False)
