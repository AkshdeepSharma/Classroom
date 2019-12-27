class Solution:
    def dfs(self, i, j, grid):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[i]) - 1 or grid[i][j] == 0:
            return 0

        grid[i][j] = 0

        left = self.dfs(i - 1, j, grid)
        right = self.dfs(i + 1, j, grid)
        down = self.dfs(i, j - 1, grid)
        up = self.dfs(i, j + 1, grid)

        return up + down + left + right + 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = max(count, self.dfs(i, j, grid))
        return count