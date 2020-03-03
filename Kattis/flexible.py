width = int(input().split()[0])
arr = [0] + list(map(int, input().split())) + [width]
res = set()

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        else:
            length_of_wall = abs(arr[i] - arr[j])
            res.add(length_of_wall)

res = sorted(res)
res = list(map(str, res))
print(" ".join(res))
