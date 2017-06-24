rAndN = input().split(' ')
r = int(rAndN[0])
n = int(rAndN[1])
br = []
roomsArray = []
for i in range(n):
    b = int(input())
    br.append(b)

for j in range(r):
    roomsArray.append(j)
roomsArray1 = roomsArray

for k in range(len(br)):
    roomsArray1.remove(k)

if n == r:
    print('too late')
else:
    print(roomsArray1[0])

'''
Refine logic for printing out booked rooms. Something is fucky.
'''