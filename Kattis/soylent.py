from math import ceil


def count_bottles(calories):
    SOYLENT = 400
    return int(ceil(calories / SOYLENT))


def main():
    T = int(input())
    for _ in range(T):
        calories = int(input())
        print(count_bottles(calories))


if __name__ == "__main__":
    main()
