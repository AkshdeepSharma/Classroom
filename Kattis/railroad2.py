def isPossible(y):
    if y % 2 == 0:
        return "possible"
    return "impossible"


def main():
    x, y = map(int, input().split())
    print(isPossible(y))


if __name__ == "__main__":
    main()
