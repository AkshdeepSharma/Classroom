class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        row_maxes = [max(row) for row in grid]
        col_maxes = list(map(max, zip(*grid)))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans += min(row_maxes[i], col_maxes[j]) - grid[i][j]
        return ans
