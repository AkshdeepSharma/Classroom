# My solution


def add_one(D):
    length = len(D)
    if D[length-1] != 9:
        D[length-1] += 1
        return D
    if D[length - 1] == 9:
        for x in reversed(range(length)):
            if D[x] == 9:
                D[x] = 0
            else:
                D[x] = D[x] + 1
                break
    count_zeros = 0
    for z in range(length):
        if D[z] == 0:
            count_zeros += 1
    if count_zeros == length:
        D.append(0)
        D[0] = 1
    return D


print(add_one([3,0]))
print(add_one([3,9]))
print(add_one([3,9,2,9]))
print(add_one([9,9]))

# Book's solution


def plus_one(D):
    D[-1] += 1
    for i in reversed(range(1, len(D))):
        if D[i] != 10:
            break
        D[i] = 0
        D[i - 1] += 1
    if D[0] == 10:
        D[0] = 1
        D.append(0)
    return D
