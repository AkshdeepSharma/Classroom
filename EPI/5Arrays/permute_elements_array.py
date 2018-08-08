# Book Solution


def permute_nums(A, p):
    for i in range(len(A)):
        next = i

        while p[next] >= 0:
            A[i], A[p[next]] = A[p[next]], A[i]
            temp = p[next]
            p[next] -= len(p)
            next = temp
    return A


# My Solution


def permute(A, p):
    if len(A) <= 1:
        return A
    r = [0] * len(p)

    for i in range(len(p)):
        r[p[i]] = A[i]
    return r


A = ['a','b','c','d','e']
p = [4,2,1,0,3]

print(permute(A,p))

