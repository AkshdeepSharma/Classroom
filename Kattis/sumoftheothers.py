def findSumFromList(numbers):
    total = sum(numbers)
    for num in numbers:
        if num == total - num:
            return num


def main():
    try:
        while True:
            numbers = list(map(int, input().split()))
            print(findSumFromList(numbers))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
