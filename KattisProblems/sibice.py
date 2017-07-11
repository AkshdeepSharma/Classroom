NWH = input().split(' ')
N, W, H = int(NWH[0]), int(NWH[1]), int(NWH[2])
maxLength = (W ** 2 + H ** 2) ** 0.5

for i in range(N):
    match = float(input())
    if match <= maxLength:
        print('DA')
    else:
        print('NE')
