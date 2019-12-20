def main():
    N = int(input())
    for _ in range(N):
        equation = input()
        if equation == "P=NP":
            print("skipped")
            continue
        a, b = map(int, equation.split("+"))
        print(a + b)


if __name__ == "__main__":
    main()
