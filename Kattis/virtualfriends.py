def find(set_data, count, i):
    if i not in set_data:
        set_data[i] = i
        count[i] = 1
    if i == set_data[i]:
        return i
    else:
        set_data[i] = find(set_data, count, set_data[i])
        return set_data[i]


def union(set_data, count, i, j):
    pi, pj = find(set_data, count, i), find(set_data, count, j)
    if pi != pj:
        set_data[pi] = pj
        count[pi] += count[pj]
        count[pj] = count[pi]
    return count[pi]


N = int(input())
for _ in range(N):
    F = int(input())
    set_data, count = {}, {}
    for _ in range(F):
        name1, name2 = map(str, input().split())
        print(union(set_data, count, name1, name2))
