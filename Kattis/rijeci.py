def rijeci(K):
    a, b = 1, 0
    for _ in range(K):
        a, b = b, a + b
    return a, b


def main():
    K = int(input())
    a, b = rijeci(K)
    print(a, b)


if __name__ == '__main__':
    main()
