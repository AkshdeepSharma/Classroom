def main():
    candies = int(input())
    friends = {0}
    for i in range(1, int(candies ** 0.5) + 1):
        if candies % (i + 1) == 0:
            friends.add(i)
            friends.add(candies // (i + 1) - 1)
    friends.add(candies - 1)
    print(" ".join(map(str, sorted(list(friends)))))


if __name__ == "__main__":
    main()
