from collections import defaultdict
from heapq import heappop, heappush

N, T = map(int, input().split())
bank_queue = defaultdict(list)
total_money = 0
priority_queue = []

for _ in range(N):
    money, time = map(int, input().split())
    bank_queue[time].append(money)

for i in reversed(range(T)):
    for money in bank_queue[i]:
        heappush(priority_queue, -money)
    if priority_queue:
        total_money += heappop(priority_queue) * -1
print(total_money)
