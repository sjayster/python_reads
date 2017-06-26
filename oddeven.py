l = [12, 34, 45, 9, 8, 90, 3]
s, e = 0, len(l) - 1
while s < e:
    if s < e:
        if l[s] % 2 == 1 and l[e] % 2 == 1:
            e -= 1
        if l[s] % 2 == 0 and l[e] % 2 == 0:
            s += 1
        if l[s] % 2 == 1 and l[e] % 2 == 0:
            l[s], l[e] = l[e], l[s]
        s += 1
        e -= 1

print l
