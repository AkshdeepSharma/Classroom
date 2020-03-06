def h(n, s):
    s += n
    if n == 1:
        return s
    if n % 2 == 0:
        return h(n // 2, s)
    if n % 2 == 1:
        return h((3 * n) + 1, s)


def main():
    n = int(input())
    s = 0
    print(h(n, s))


if __name__ == "__main__":
    main()
