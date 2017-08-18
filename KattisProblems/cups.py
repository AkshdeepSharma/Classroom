N = int(input())
cups = []
copycups = []
for i in range(N):
    a, b = input().split()
    try:
        cups.append([int(b), a])
    except:
        cups.append([int(a) // 2, b])

cups = sorted(cups, key=lambda x: x[0])

for k in range(len(cups)):
    print(cups[k][1])
