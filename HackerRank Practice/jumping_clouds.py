#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    current_cloud = 0
    c.append(3)  # SUPER HACKY SOLUTION
    while current_cloud <= len(c) - 3:
        if c[current_cloud + 2] == 0:
            jumps += 1
            current_cloud += 2
        elif c[current_cloud + 1] == 0:
            jumps += 1
            current_cloud += 1
        else:
            break
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()