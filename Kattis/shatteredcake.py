def main():
    W = int(input())
    area = 0
    for _ in range(int(input())):
        cake_slice = input().split()
        area += int(cake_slice[0]) * int(cake_slice[1])
    print(area // W)


if __name__ == "__main__":
    main()
