cases = int(input())
for i in range(cases):
    kAndM = input().split(' ')
    k = int(kAndM[0])
    m = int(kAndM[1])
    if k == 1:
        print(int((m * (m + 1)) / 2))
    else:
        print()
