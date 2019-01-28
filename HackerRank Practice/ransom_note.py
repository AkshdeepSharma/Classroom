#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words_dict = {}
    for word in magazine:
        if word in words_dict:
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    for word in note:
        if word in words_dict:
            words_dict[word] -= 1
            if words_dict[word] < 0:
                print('No')
                return
        else:
            print('No')
            return 0
    print('Yes')
    return 1

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
