#!/usr/bin/python


def hash_it(chars):
    d = dict()
    for c in chars:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


if __name__ == "__main__":
    max_len = 0
    l = []
    chars = ['a', 'a', 'n', 'c', 'b']
    d = hash_it(chars)

    print d
    wrds = ["abc", "baa", "caan", "an", "banc"]
    for word in wrds:
        hashed = hash_it(word)
        print hashed
        if len(hashed) > len(d) or len(word) < max_len:
            continue
        good = True
        for k, v in hashed.iteritems():
            if k not in d or v > d[k]:
                good = False
                break

        if not good:
            continue

        if max_len < len(word):
            max_len = len(word)
            l = []
        l.append(word)

    print l
