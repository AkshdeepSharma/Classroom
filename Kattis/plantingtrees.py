def main():
    max_day = 0
    num_trees = input()
    trees = sorted(list(map(int, input().split())), reverse=True)
    for i, tree in enumerate(trees):
        max_day = max(max_day, i + 1 + tree)
    print(max_day + 1)


if __name__ == "__main__":
    main()
