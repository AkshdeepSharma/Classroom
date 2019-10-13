def cross(board, num):
    rows = {x for x in range(9)}
    cols = {x for x in range(9)}
    cells = {x for x in range(9)}
    for i in range(9):
        for j in range(9):
            if board[i][j] == num:
                rows.discard(i)
                cols.discard(j)
                cells.discard((i // 3) * 3 + j // 3)
    if len(rows) == 0:
        return None
    for cell in cells:
        cell_rows = {x for x in range((cell // 3) * 3, (cell // 3 + 1) * 3) if x in rows}
        cell_cols = {x for x in range((cell % 3) * 3, (cell % 3 + 1) * 3) if x in cols}
        if len(cell_rows) == 0 or len(cell_cols) == 0:
            raise Exception()
        curr_position = [(i, j) for i in cell_rows for j in cell_cols if board[i][j] == "."]
        if len(curr_position) == 0:
            raise Exception()
        if len(curr_position) == 1:
            return curr_position[0]
    return None

if __name__ == "__main__":
    board = []
    for _ in range(9):
        temp = input()
        board.append(list(temp))
    while True:
        sudoku_complete = True
        error = False
        for num in range(1, 10):
            try:
                res = cross(board, str(num))
                if res is not None:
                    sudoku_complete = False
                    i, j = res[0], res[1]
                    board[i][j] = str(num)
            except:
                error = True
                break
        if sudoku_complete:
            if error:
                print("ERROR")
            else:
                for i in range(9):
                    temp = "".join(board[i])
                    print(temp)
            break


"""
..9......
.....4...
.......4.
.........
.4.......
.........
.........
.........
.........

...1...6.
18...9...
..7.642..
2.9..6.5.
.43...72.
.6.3..9.1
..265.1..
...2...97
.5...3...
"""
