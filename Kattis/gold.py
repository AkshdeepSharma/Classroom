def bfs(grid, x, y):
    gold = 0
    direction = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    while direction:
        x, y = direction.pop(0)
        if grid[x][y] == "G":
            gold += 1
        if grid[x][y] != "#" and grid[x + 1][y] != "T" and grid[x - 1][y] != "T" and grid[x][y + 1] != "T" and grid[x][y - 1] != "T":
            direction.extend([
                (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
            ])
        grid[x][y] = "#"
    return gold


def main():
    width, height = map(int, input().split())
    grid = []
    gold = 0
    for _ in range(height):
        grid.append(list(input()))
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "P":
                x, y = i, j
                break
    if grid[x + 1][y] != "T" and grid[x - 1][y] != "T" and grid[x][y + 1] != "T" and grid[x][y - 1] != "T":
        gold = bfs(grid, x, y)
    print(gold)


if __name__ == '__main__':
    main()
