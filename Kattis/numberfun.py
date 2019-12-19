def main():
    N = int(input())
    for _ in range(N):
        a, b, c = map(int, input().split())
        if a + b == c or abs(a - b) == c or (a // b == c and a % b == 0) or (b // a == c and b % a == 0) or a * b == c:
            print("Possible")
        else:
            print("Impossible")


if __name__ == '__main__':
    main()
