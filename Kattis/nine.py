def main():
    cases = int(input())
    for _ in range(cases):
        digits = int(input())
        print(getNumsThatDontContainNine(digits))


def getNumsThatDontContainNine(digits):
    MOD = 1000000007
    return 8 * 9 ** (digits - 1) % MOD


if __name__ == "__main__":
    main()

# runs but times out :[ not sure how to make it better
