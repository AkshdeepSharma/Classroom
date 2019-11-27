def SSD(K, base, num):
    final_num = 0
    while num > 0:
        final_num += (num % base) ** 2
        num //= base
    return str(K) + " " + str(final_num)


def main():
    cases = int(input())
    for _ in range(cases):
        K, base, num = map(int, input().split())
        print(SSD(K, base, num))


if __name__ == '__main__':
    main()
