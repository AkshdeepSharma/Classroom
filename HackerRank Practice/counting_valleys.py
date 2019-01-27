#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    in_valley = False
    valley_tracker = 0
    num_valleys = 0
    for c in s:
        if c == "U":
            valley_tracker += 1
            if valley_tracker == 0 and in_valley == True:
                in_valley = False
        else:
            valley_tracker -= 1
            if valley_tracker == -1 and in_valley == False:
                in_valley = True
                num_valleys += 1
    return num_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
