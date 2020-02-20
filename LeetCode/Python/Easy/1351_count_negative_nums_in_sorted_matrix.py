class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[i]))):
                if grid[i][j] >= 0:
                    break
                count += 1
        return count
