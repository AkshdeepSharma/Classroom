from math import ceil
from sys import stdin

while True:
    N, B = map(int, stdin.readline().split())
    if N == B == -1:
        break
    city_populations = [int(stdin.readline()) for _ in range(N)]
    lo, hi = 1, max(city_populations)

    while hi - lo > 0.1:
        res = 0
        mid = lo + (hi - lo) / 2
        for population in city_populations:
            res += ceil(population / mid)
        if res <= B:
            hi = mid
        else:
            lo = mid
    print(ceil(lo))
    stdin.readline()
