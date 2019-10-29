while True:
    pairs = []
    distance = 0
    n = int(input())
    if n == -1:
        break
    for i in range(n):
        pairs.append(input().split(' '))
    for j in range(n):
        if j == 0:
            distance += int(pairs[j][0]) * int(pairs[j][1])
        else:
            distance += int(pairs[j][0]) * (int(pairs[j][1]) - int(pairs[j - 1][1]))
    print(str(distance), 'miles')