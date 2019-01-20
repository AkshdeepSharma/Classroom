def maxTurbulenceSize(A):
    """
    :type A: List[int]
    :rtype: int
    """
    lts = 0
    for i in range(len(A) - 1):
        j = i
        sign = 0
        temp = 0
        while True and j < len(A) - 1:
            print(i, j, lts)
            if j == i and A[j] > A[j + 1]:
                sign = -1
                j += 1
                temp += 1
            elif j == i and A[j] < A[j + 1]:
                sign = 1
                j += 1
                temp += 1
            elif j != i and sign == -1:
                if A[j] < A[j + 1]:
                    j += 1
                    sign = 1
                    temp += 1
                else:
                    break
            elif j != i and sign == 1:
                if A[j] > A[j + 1]:
                    j += 1
                    sign = -1
                    temp += 1
                else:
                    break
            elif A[j] == A[j + 1]:
                break
            if temp > lts:
                lts = temp
    return lts

print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))