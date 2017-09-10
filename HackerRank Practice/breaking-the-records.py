#!/bin/python3
import sys


def getRecord(s):
    low, high = s[0], s[0]
    break_low, break_high = 0, 0
    for i in s:
        if i > high:
            high = i
            break_high += 1
        if i < low:
            low = i
            break_low += 1
    return break_high, break_low


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print(" ".join(map(str, result)))
