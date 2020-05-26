def main():
    L, H = map(int, input().split())
    possibleCombos = 0
    for i in range(L, H + 1):
        if i % 2 != 0 or not doesNumContainUniqueDigits(i):
            continue
        if isNumDivisibleByDigits(i):
            possibleCombos += 1
    print(possibleCombos)


def doesNumContainUniqueDigits(num):
    return len(set(list(str(num)))) == 6


def isNumDivisibleByDigits(num):
    for i in range(6):
        if int(str(num)[i]) == 0 or num % int(str(num)[i]) != 0:
            return False
    return True


if __name__ == "__main__":
    main()
