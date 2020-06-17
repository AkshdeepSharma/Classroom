from math import factorial


def main():
    list_length, divisor = map(int, input().split())
    integers = list(map(int, input().split()))
    counts = getDivisorCounts(integers, divisor)
    print(getNumberOfPairs(counts))


def getDivisorCounts(integers, divisor):
    counts = {}
    for num in integers:
        quotient = num // divisor
        if quotient not in counts:
            counts[quotient] = 0
        counts[quotient] += 1
    return counts


def getNumberOfPairs(counts):
    number_of_pairs = 0
    for key, val in counts.items():
        if val == 1:
            continue
        number_of_pairs += factorial(val) / (factorial(2) * factorial(val - 2))
    return int(number_of_pairs)


if __name__ == "__main__":
    main()
