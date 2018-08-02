# Book Solution


def rearrange(A):
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
    return A


# My Solution


def alteration(A):
    sign =  1
    for i in range(len(A) - 1):
        if sign == 1:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
            sign = -1
        else:
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
            sign = 1
    return A


A = [3, 2, 8, 7, 1, 4, 6]
print(rearrange(A))
print(alteration(A))
