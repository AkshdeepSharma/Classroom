def isRightAngle(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return 'right'
    return 'wrong'


def main():
    a, b, c = sorted(map(int, input().split()))
    while a + b + c != 0:
        print(isRightAngle(a, b, c))
        a, b, c = sorted(map(int, input().split()))


if __name__ == "__main__":
    main()
