def main():
    numer, denom = map(int, input().split("/"))
    numer = (numer - (32 * denom)) * 5
    denom *= 9
    gcdNum = gcd(numer, denom)
    print(str(numer // gcdNum) + "/" + str(denom // gcdNum))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    main()
