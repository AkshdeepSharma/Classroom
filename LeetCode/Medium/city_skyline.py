class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_increased = 0
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum_increased += min(rows_max[i], cols_max[j]) - grid[i][j]
        return sum_increased