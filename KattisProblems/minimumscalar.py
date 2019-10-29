T = int(input())

for i in range(1, T + 1):
    res = 0
    n = int(input())
    scalar1 = list(map(int, input().split()))
    scalar2 = list(map(int, input().split()))
    scalar1 = sorted(scalar1)
    scalar2 = sorted(scalar2, reverse=True)
    for j in range(len(scalar1)):
        res += (scalar1[j] * scalar2[j])
    print("Case #{}: {}".format(str(i), str(res)))
