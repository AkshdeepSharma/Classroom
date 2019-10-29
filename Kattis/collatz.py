while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    A, B = [A], [B]
    i, j = 0, 0
    while A[i] != 1:
        if A[i] % 2 == 0:
            A.append(A[i] // 2)
        else:
            A.append(A[i] * 3 + 1)
        i += 1
    while B[j] != 1:
        if B[j] % 2 == 0:
            B.append(B[j] // 2)
        else:
            B.append(B[j] * 3 + 1)
        if B[j] in A:
            break
        j += 1
    print(str(A[0]) + " needs " + str(A.index(B[j])) + " steps, " + str(B[0]) + " needs " + str(j) + " steps, they meet at " + str(B[j]))