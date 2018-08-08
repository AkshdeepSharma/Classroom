import random


def subarray(A, k):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:k]


print(subarray([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
