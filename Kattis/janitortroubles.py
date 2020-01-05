from math import sqrt


def max_area(a, b, c, d):
    SP = (a + b + c + d) / 2
    return sqrt((SP - a) * (SP - b) * (SP - c) * (SP - d))


def main():
    a, b, c, d = map(int, input().split())
    print(max_area(a, b, c, d))


if __name__ == "__main__":
    main()
