from math import factorial
from itertools import combinations

N = int(input())
fruits = list(map(int, input().split()))
total_weight = 0

i = 1
while i < 4 and i <= N:
    for fruit_weight in combinations(fruits, i):
        if sum(fruit_weight) >= 200:
            total_weight += sum(fruit_weight)
    i += 1

for j in range(4, N + 1):
    fruit_weight = factorial(
        N - 1) // (factorial(j - 1) * factorial(N - j))
    for fruit in fruits:
        total_weight += (fruit * fruit_weight)
print(total_weight)
