x = int(input())
n = int(input())
totalMB = x * (n + 1)
used = []

for i in range(n):
    used.append(int(input()))

sumUsed = sum(used)
print(totalMB - sumUsed)
