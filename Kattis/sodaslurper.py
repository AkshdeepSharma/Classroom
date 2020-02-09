def soda(e, c):
    sodas = 0
    while e >= c:
        temp = e % c
        sodas += e // c
        e = e // c + temp
    return sodas


def main():
    e, f, c = map(int, input().split())
    print(soda(e + f, c))


if __name__ == "__main__":
    main()
