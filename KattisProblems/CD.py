NM = input().split(' ')
N, M = int(NM[0]), int(NM[1])
CD = {}
count = 0
for i in range(N):
    jill = int(input())
    CD.update({jill: 1})

for j in range(M):
    jack = int(input())
    if jack in CD:
        count += 1
wtf = input()
print(count)