T = int(input())

for i in range(T):
    n = 0
    p = 0.5
    k = int(input())
    for j in range(k):
        p *= 2
        n += 0.5
        n += p
        if n % 2 == 0:
            n -= 1
    print(int(n))
