def main():
    N = int(input())
    while N:
        names = [input() for _ in range(N)]
        sorted_names = sorted(names, key=lambda x: x[:2])
        for name in sorted_names:
            print(name)
        N = int(input())
        if N:
            print(" ")


if __name__ == "__main__":
    main()
