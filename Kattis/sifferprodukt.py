def digitProduct(num):
    while num > 9:
        product = 1
        num = list(map(int, list(str(num))))
        for digit in num:
            if digit != 0:
                product *= digit
        num = product
    return num


def main():
    num = int(input())
    print(digitProduct(num))


if __name__ == '__main__':
    main()
