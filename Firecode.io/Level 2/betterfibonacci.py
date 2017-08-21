def better_fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, y+x
    return x

print(better_fibonacci(8))