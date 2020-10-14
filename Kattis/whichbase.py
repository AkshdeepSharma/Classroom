def printBases(data_set_number, num):
    try:
        octal = int(num, 8)
    except ValueError:
        octal = 0
    try:
        deca = int(num)
    except ValueError:
        deca = 0
    try:
        hexa = int(num, 16)
    except ValueError:
        hexa = 0
    return f'{data_set_number} {octal} {deca} {hexa}'


def main():
    P = int(input())
    for _ in range(P):
        data_set_number, num = input().split()
        print(printBases(data_set_number, num))


if __name__ == "__main__":
    main()
