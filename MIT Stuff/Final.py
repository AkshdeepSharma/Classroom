'''
1-1: False
1-2: True
1-3: True
1-4: True
1-5: False

2-1: When a = A()
2-2: O(n)
2-3: False because a dictionary is mutable
2-4: Worst case foo_two is worse than foo_one
2-5: Polynomial

-------------------------


def sum_digits(s):
    digits = '1234567890'
    sums = []
    for i in s:
        if i in digits:
            sums.append(int(i))
    if len(sums) == 0:
        return ValueError
    else:
        return sum(sums)
-------------------------

import collections


def max_val(t):
    def flatten(t):
        if isinstance(t, collections.Iterable):
            return [a for i in t for a in flatten(i)]
        else:
            return [t]
    flat = flatten(t)
    return max(flat)
-------------------------


def cipher(map_from, map_to, code):
    key_code = {}
    decoded = ''
    for letter in range(len(map_from)):
        key_code[map_from[letter]] = map_to[letter]
    for i in code:
        decoded += key_code.get(i)
    return key_code, decoded

'''

