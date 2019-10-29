from collections import defaultdict
try:
    while True:
        n, l, w = map(int, input().split())
        sprinklers = defaultdict(list)
        for _ in range(n):
            location, radius = map(int, input().split())
            sprinklers[location].append(radius)

except EOFError:
    pass
