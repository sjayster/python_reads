def count(s):
    l = len(s)
    r = ""
    c = 1
    for i in range(1, l):
        if s[i - 1] != s[i]:
            r = r + s[i - 1] + str(c)
            c = 0
        c += 1

    r = r + s[i] + str(c)

    return r


s = "aabcceeeeeff"
print count(s)
