from math import pi


def gnaw(D, V):
    return round((D ** 3 - 6 * (V / pi)) ** (1.0 / 3), 9)


def main():
    D, V = map(int, input().split())
    while D != 0:
        print(gnaw(D, V))
        D, V = map(int, input().split())


if __name__ == "__main__":
    main()
