def check(board):
    for i in range(len(board)):
        if "WWW" in board[i] or "BBB" in board[i] or board[i].count("W") != board[i].count("B"):
            return False
    return True


def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(input())
    transposed_board = ["".join([row[i] for row in board]) for i in range(N)]
    if check(board) and check(transposed_board):
        print("1")
    else:
        print("0")


if __name__ == '__main__':
    main()
