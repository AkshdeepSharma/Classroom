def main():
    N = int(input())
    for i in range(N):
        word = input()
        if i % 2 == 0:
            print(word)

if __name__ == "__main__":
    main()