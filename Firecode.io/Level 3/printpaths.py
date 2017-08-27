board = [
  ['A', 'B', 'C']
]


def print_paths(board):
    paths = []
    temp_str_list = []

    def search(i, j, board, temp_str_list, paths):
        rows = len(board)
        cols = len(board[0])
        if i > rows - 1 or j > cols - 1:
            return
        temp_str_list.append(board[i][j])
        if i == rows - 1 and j == cols - 1:
            paths.append("".join(temp_str_list))
            temp_str_list.pop()
            return
        search(i + 1, j, board, temp_str_list, paths)
        search(i, j + 1, board, temp_str_list, paths)
        temp_str_list.pop()

    search(0, 0, board, temp_str_list, paths)
    return paths

print(print_paths(board))
