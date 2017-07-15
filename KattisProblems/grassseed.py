C = float(input())
L = int(input())
lawns = []
costs = 0

for i in range(L):
    lawns.append(input().split(' '))
lawns = [[float(y) for y in x] for x in lawns]

for j in range(L):
    costs += lawns[j][0] * lawns[j][1] * C

print(costs)
