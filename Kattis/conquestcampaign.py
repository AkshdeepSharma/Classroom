from collections import deque


def createGrid(rows, cols, weak_cells):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x, y in weak_cells:
        grid[x - 1][y - 1] = 1
    return grid


def timeToConquer(grid, rows, cols, weak_cells):
    q = deque()
    days_to_conquer = 0
    for x, y in weak_cells:
        q.append((x - 1, y - 1))
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0:
                    grid[i][j] = 1
                    q.append((i, j))
        days_to_conquer += 1
    return days_to_conquer


def main():
    rows, cols, n = map(int, input().split())
    weak_cells = list(set([tuple(map(int, input().split()))
                           for _ in range(n)]))
    grid = createGrid(rows, cols, weak_cells)
    print(timeToConquer(grid, rows, cols, weak_cells))


if __name__ == "__main__":
    main()
