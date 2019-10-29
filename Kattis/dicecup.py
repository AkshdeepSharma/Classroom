nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
probabilities = []
array = []

for i in range(1, n+1):
    for j in range(1, m+1):
        array.append(i + j)

for k in range(len(array)):
    probabilities.append(array.count(k) / (n + m))

counts = probabilities.count(max(probabilities))

for l in range(counts):
    print(probabilities.index(max(probabilities)) + l)
