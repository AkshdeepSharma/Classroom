def harshad(num):
    MAX_RANGE = 1000000001
    for i in range(num, MAX_RANGE):
        sum_num = sum(map(int, list(str(i))))
        if i % sum_num == 0:
            return i


def main():
    num = int(input())
    print(harshad(num))


if __name__ == '__main__':
    main()
