def main():
    for _ in range(int(input())):
        outlets = list(map(int, input().split()))
        print(sum(outlets) - outlets[0] - (len(outlets) - 2))


if __name__ == "__main__":
    main()
