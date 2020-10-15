def getHighestUniqueOutcome(rolls):
    d = {}
    best = 0
    for roll in rolls:
        if roll not in d:
            d[roll] = 0
        d[roll] += 1
    for key, val in d.items():
        if val == 1:
            best = max(key, best)
    return rolls.index(best) + 1 if best != 0 else 'none'


def main():
    group_size = int(input())
    rolls = list(map(int, input().split()))
    print(getHighestUniqueOutcome(rolls))


if __name__ == "__main__":
    main()
