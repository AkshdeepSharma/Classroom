def findSquares(distance):
    a, b = 0, 0
    if (distance - 2) % 4 == 0:
        return "impossible", ""
    while b**2 - a**2 != distance:
        if b**2 - a**2 < distance:
            b += 1
        else:
            a += 1
    return a, b


def main():
    distance = int(input())
    a, b = findSquares(distance)
    print(str(a), str(b))


if __name__ == "__main__":
    main()
