s, h, v = map(int, input().split())
print(max(v * h, (s - v) * h, v * (s - h), (s - v) * (s - h)) * 4)
