def main():
    N = int(input())
    if N % 2 == 1:
        print("Either")
    else:
        M = N // 2
        if M % 2 == 0:
            print("Even")
        else:
            print("Odd")


if __name__ == "__main__":
    main()
