while True:
    dN = input().split(' ')

    sour = 0
    sweet = 0
    xy = []
    d = float(dN[0])
    N = int(dN[1])

    if dN == ['0.0', '0']:
        break

    for i in range(N):
        xyCoordinates = input().split(' ')
        xy.append(xyCoordinates)

    for j in range(len(xy)-1):
        magnitude = ((float(xy[j + 1][0]) - float(xy[j][0])) ** 2 + (float(xy[j + 1][1]) - float(xy[j][1])) ** 2) ** 0.5
        if magnitude <= d:
            sour += 1
        else:
            sweet += 1

    print(str(sour + 1), "sour,", str(sweet), "sweet")
