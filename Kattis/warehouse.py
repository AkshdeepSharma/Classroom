def warehouse(toys):
    toys = sorted(toys.items(), key=lambda x: (-x[1], x[0]))
    return toys


def main():
    for _ in range(int(input())):
        toys = {}
        for _ in range(int(input())):
            toy, amount = input().split()
            if toy in toys:
                toys[toy] += int(amount)
            else:
                toys[toy] = int(amount)
        ans = warehouse(toys)
        print(len(ans))
        for toy, amount in ans:
            print(toy, amount)


if __name__ == "__main__":
    main()
