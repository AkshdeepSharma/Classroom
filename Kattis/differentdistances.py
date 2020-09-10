def calculatePNormDistance(x1, y1, x2, y2, p):
    return (abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1 / p)


def main():
    inp = list(map(float, input().split()))
    while inp != [0]:
        x1, y1, x2, y2, p = inp
        print(calculatePNormDistance(x1, y1, x2, y2, p))
        inp = list(map(float, input().split()))


if __name__ == "__main__":
    main()
