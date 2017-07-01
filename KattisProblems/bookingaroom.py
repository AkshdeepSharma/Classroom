RN = input().split(' ')
r = int(RN[0])
n = int(RN[1])
br = []
roomsArray = []

for i in range(n):
    b = int(input())
    br.append(b)

for j in range(1, r + 1):
    roomsArray.append(j)

for k in br:
    if k in roomsArray:
        roomsArray.remove(k)

if n == r:
    print('too late')
else:
    print(roomsArray[0])
