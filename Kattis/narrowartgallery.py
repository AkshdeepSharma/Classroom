memo = {}


def rooms_to_close(N, grid, row, open_rooms, k):
    value = 0
    if (row, open_rooms, k) in memo:
        return memo[(row, open_rooms, k)]
    if k < N - row and row < N:
        if open_rooms == -1:
            option_one = grid[row][0] + \
                rooms_to_close(N, grid, row + 1, 0, k - 1)
            option_two = grid[row][1] + \
                rooms_to_close(N, grid, row + 1, 1, k - 1)
            option_three = grid[row][0] + grid[row][1] + \
                rooms_to_close(N, grid, row + 1, -1, k)
            value = max(option_one, option_two, option_three)
        elif open_rooms == 0:
            option_one = grid[row][0] + \
                rooms_to_close(N, grid, row + 1, 0, k - 1)
            option_three = grid[row][0] + grid[row][1] + \
                rooms_to_close(N, grid, row + 1, -1, k)
            value = max(option_one, option_three)
        elif open_rooms == 1:
            option_two = grid[row][1] + \
                rooms_to_close(N, grid, row + 1, 1, k - 1)
            option_three = grid[row][0] + grid[row][1] + \
                rooms_to_close(N, grid, row + 1, -1, k)
            value = max(option_two, option_three)
    elif k == N - row and row < N:
        if open_rooms == -1:
            option_one = grid[row][0] + \
                rooms_to_close(N, grid, row + 1, 0, k - 1)
            option_two = grid[row][1] + \
                rooms_to_close(N, grid, row + 1, 1, k - 1)
            value = max(option_one, option_two)
        elif open_rooms == 0:
            value = grid[row][0] + rooms_to_close(N, grid, row + 1, 0, k - 1)
        elif open_rooms == 1:
            value = grid[row][1] + rooms_to_close(N, grid, row + 1, 1, k - 1)
    memo[(row, open_rooms, k)] = value
    return value


def main():
    while True:
        grid = []
        N, k = map(int, input().split())
        if N == k == 0:
            break
        for _ in range(N):
            gallery_row = list(map(int, input().split()))
            grid.append(gallery_row)
        print(rooms_to_close(N, grid, 0, -1, k))


if __name__ == "__main__":
    main()
