def dfs(grid, N, M):
    edges = 0
    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]
    stack = [(0, 0)]
    while stack:
        row, col = stack.pop()
        for i in range(4):
            new_row = row + delta_x[i]
            new_col = col + delta_y[i]
            if new_row >= 0 and new_row < N and new_col >= 0 and new_col < M:
                if grid[new_row][new_col] == "1":
                    edges += 1
                if grid[new_row][new_col] == "0":
                    grid[new_row][new_col] = "#"
                    stack.append((new_row, new_col))
    return edges


def main():
    N, M = map(int, input().split())
    grid = [['0'] + list(input()) + ['0'] for x in range(N)]
    grid.insert(0, ['0'] * (M + 2))
    grid.append(['0'] * (M + 2))
    print(dfs(grid, N + 2, M + 2))


if __name__ == '__main__':
    main()
