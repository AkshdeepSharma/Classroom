def isValid(grid):
    if any(row.count("*") != 1 for row in grid):
        return False
    if any(col.count("*") != 1 for col in [*zip(*grid)]):
        return False

    starts = [(x, 0) for x in range(8)] + [(0, y) for y in range(8)]

    for start in starts:
        i, j = start
        i2, j2 = i, 7 - j
        count = count2 = 0
        while i < 8 and j < 8:
            count += grid[j][i] == "*"
            count2 += grid[j2][i2] == "*"
            i, j = i + 1, j + 1
            i2, j2 = i2 + 1, j2 - 1
        if count > 1 or count2 > 1:
            return False
    return True


input_grid = []
for i in range(8):
    temp = input()
    input_grid.append(temp)

print("valid" if isValid(input_grid) else "invalid")
