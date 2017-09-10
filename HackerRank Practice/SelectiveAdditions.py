#!/bin/python3

import sys

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    A = list(map(int, input().strip().split(' ')))
    S = list(map(int, input().strip().split(' ')))
    for a0 in range(m):
        l, r, x = input().strip().split(' ')
        l, r, x = [int(l), int(r), int(x)]
        for i in range(l - 1, r):
            if A[i] not in S:
                A[i] += x
        print(sum(A))
