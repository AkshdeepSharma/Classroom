from math import factorial


def findNumCombinations(chars):
    num_combinations = 0
    for i in range(2, chars + 1):
        num_combinations += factorial(chars) / \
            (factorial(i) * factorial(chars - i))
    return int(num_combinations)


def main():
    chars = int(input())
    print(findNumCombinations(chars))


if __name__ == "__main__":
    main()
