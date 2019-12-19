def main():
    P, N = map(int, input().split())
    new_parts = set()
    day = None
    for i in range(N):
        part = input()
        new_parts.add(part)
        if len(new_parts) == P and day is None:
            day = i + 1
    if day is not None:
        print(day)
    else:
        print("paradox avoided")


if __name__ == '__main__':
    main()
