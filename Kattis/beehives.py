while True:
    dN = input().split(' ')
    xy = []
    d = float(dN[0])
    N = int(dN[1])
    magnitude = []
    sour, sweet = 0, 0
    if dN == ['0.0', '0']:
        break

    for i in range(N):
        xyCoordinates = input().split(' ')
        xy.append(xyCoordinates)

    xy = sorted(xy)

    for j in range(len(xy) - 1):
        magnitude.append((float(xy[j][0]) - float(xy[j + 1][0])) **
                         2 + ((float(xy[j][1]) - float(xy[j + 1][1])) ** 2) ** 0.5)

    for k in magnitude:
        print(k)
        if k <= d:
            sour += 1
        else:
            sweet += 1

    print(str(sour), 'sour', str(sweet), 'sweet')
