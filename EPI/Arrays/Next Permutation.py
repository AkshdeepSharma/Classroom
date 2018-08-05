def next_permutation(A):
    invert = len(A) - 2
    while invert >= 0 and A[invert] >= A[invert + 1]:
        invert -= 1
    if invert < 0:
        return []
    for i in reversed(range(invert, len(A))):
        if A[i] > A[invert]:
            A[i], A[invert] = A[invert], A[i]
            break
    A[invert + 1:] = reversed(A[invert + 1:])
    return A


arr = [6, 8, 9, 7, 1, 2, 6, 4, 3, 0]
print(next_permutation(arr))
