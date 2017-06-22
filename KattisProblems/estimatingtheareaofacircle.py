while True:
    pi = 3.141592654
    inp1 = input().split(' ')
    radius = float(inp1[0])
    outside = int(inp1[1])
    inside = int(inp1[2])
    areaCircle = pi * radius ** 2
    areaSquare = (radius * 2) ** 2

    if inp1 == ['0', '0', '0']:
        break
    print(areaCircle, (inside/outside * areaSquare))
