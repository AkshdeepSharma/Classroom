from math import pi


def main():
    area, perimeter = map(float, input().split())
    if area > pi * (perimeter / (2 * pi)) ** 2:
        print("Need more materials!")
    else:
        print("Diablo is happy!")


if __name__ == "__main__":
    main()
