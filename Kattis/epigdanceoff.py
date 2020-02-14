def calculateDanceMoves(dance):
    moves = 0
    for i in range(len(dance)):
        if '$' not in dance[i]:
            moves += 1
    return moves + 1


def rotateMatrix(dance, N, M):
    return [[dance[j][i] for j in range(N)] for i in range(M - 1, -1, -1)]


def main():
    N, M = map(int, input().split())
    dance = []
    for _ in range(N):
        dance.append(list(input()))
    dance = rotateMatrix(dance, N, M)
    print(calculateDanceMoves(dance))


if __name__ == "__main__":
    main()
