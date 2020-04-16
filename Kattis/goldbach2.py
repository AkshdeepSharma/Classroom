def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def getSumOfPrimes(num):
    ans = []
    for i in range(2, (num // 2) + 1):
        if isPrime(i) and isPrime(num - i):
            ans.append(str(i) + "+" + str(num - i))
    ans.insert(0, f"{num} has {len(ans)} representation(s)")
    return ans + [""]


def main():
    for _ in range(int(input())):
        num = int(input())
        ans = getSumOfPrimes(num)
        for line in ans:
            print(line)


if __name__ == "__main__":
    main()
