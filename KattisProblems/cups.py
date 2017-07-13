N = int(input())
cups = []
cupsColours = []

for i in range(N):
    cups.append(int(input().split(' ')))


'''for k in range(N):
    if type(cups[k][0]) == float:
        cups[k][0] = cups[k][0] / 2
'''


print(cups)

print("\n".join(cupsColours))