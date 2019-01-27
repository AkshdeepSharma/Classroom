#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    letter_counts = {'a': 0}
    result = 0

    for c in s:
        if c == 'a':
            letter_counts[c] += 1
    result += letter_counts.get('a') * (n // len(s))
    for i in range(n - ((n // len(s)) * len(s))):
        if s[i] == 'a':
            result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
