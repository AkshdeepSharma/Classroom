setNum = 0
while True:
    count = 0
    names = []
    rilNames = []
    n = int(input())
    setNum += 1
    if n == 0:
        break
    for i in range(n):
        names.append(input())
    for j in range(0, n, 2):
        rilNames.append(names[j])
    for k in range(1, n, 2):
        rilNames.insert(len(rilNames) - count, names[k])
        count += 1

    print("SET", str(setNum))
    print("\n".join(rilNames))
