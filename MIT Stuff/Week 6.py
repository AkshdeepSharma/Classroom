L = [2, 2, 2, [3, 2, 1, 2]]
def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])

    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

print(genSubsets(L))