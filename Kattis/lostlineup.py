def main():
    N = int(input())
    lineup = ['1'] * N
    positions = list(map(int, input().split()))
    for i in range(len(positions)):
        lineup[positions[i] + 1] = str(i + 2)
    print(" ".join(lineup))


if __name__ == '__main__':
    main()
