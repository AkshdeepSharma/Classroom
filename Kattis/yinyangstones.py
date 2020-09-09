def canStonesBeBalanced(stones):
    return 1 if stones.count("W") == stones.count("B") else 0


def main():
    stones = input()
    print(canStonesBeBalanced(stones))


if __name__ == "__main__":
    main()
