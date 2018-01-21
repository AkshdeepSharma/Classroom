from collections import deque
def matrix_max_sum_dfs(grid):
    class TravelNode:
        def __init__(self, row, col, node_sum, grid):
            self.row = row
            self.col = col
            node_sum += grid[row][col]
            self.node_sum = node_sum

    max_sum = -sys.maxint - 1
    rows = len(grid)
    cols = len(grid[0])

    if rows < 2 and cols < 2:
        return grid[0][0]
    else:
        stack = deque()
        stack.appendleft(TravelNode(0, 0, 0, grid))

        while len(stack) > 0:
            t = stack.popleft()
            if t.row == rows - 1 and t.col == cols - 1:
                if t.node_sum > max_sum:
                    max_sum = t.node_sum
            else:
                if t.col < cols - 1:
                    stack.appendleft(TravelNode(t.row, t.col + 1, t.node_sum, grid))
                if t.row < rows - 1:
                    stack.appendleft(TravelNode(t.row + 1, t.col, t.node_sum, grid))
    return max_sum

answer = []
answer.append(tuple(1, 2, 3))
