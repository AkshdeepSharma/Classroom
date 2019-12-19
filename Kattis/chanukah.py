def main():
    N = int(input())
    for _ in range(N):
        case, days = map(int, input().split())
        candles = (days * (days + 1)) / 2 + days
        print(case, int(candles))


if __name__ == '__main__':
    main()
