rAndC = input().split(' ')

r = int(rAndC[0])
c = int(rAndC[1])
pi = 3.141592654


if r == c:
    print('0.0')
else:
    print(round(((pi * (r - c) ** 2) / (pi * r ** 2)) * 100, 8))
