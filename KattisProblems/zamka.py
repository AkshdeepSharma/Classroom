L = int(input())
D = int(input())
X = int(input())

for i in range(L, D + 1):
    value = list(str(i))
    value = [int(x) for x in value]
    sumI = sum(value)
    if sumI == X:
        print(i)
        break

for j in range(D, L - 1, -1):
    value1 = list(str(j))
    value1 = [int(x) for x in value1]
    sumJ = sum(value1)
    if sumJ == X:
        print(j)
        break