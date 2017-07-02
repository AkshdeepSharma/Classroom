NPQ = input().split(' ')
N = int(NPQ[0])
P = int(NPQ[1])
Q = int(NPQ[2])

roundsDone = P + Q

if (roundsDone // N) % 2 == 0:
    print('paul')
else:
    print('opponent')

