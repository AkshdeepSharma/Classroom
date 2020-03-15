def main():
    n = int(input())
    i = 2
    meowfactor = 1
    while i ** 9 <= n:
        if n % i ** 9 == 0:
            meowfactor = i
        i += 1
    print(meowfactor)


if __name__ == "__main__":
    main()
