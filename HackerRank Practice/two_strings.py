#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    comparison = {}
    for c in s1:
        if c in comparison:
            comparison[c] += 1
        else:
            comparison[c] = 1
    for c in s2:
        if c in comparison:
            result = 'YES'
            return result
    result = 'NO'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
