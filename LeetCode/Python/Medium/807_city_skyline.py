class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height_increase = 0
        row_maxes = list(map(max, grid))
        column_maxes = list(map(max, zip(*grid)))
        for i in range(len(grid)):
            for j in range(len(grid)):
                curr_num = grid[i][j]
                height_increase -= curr_num - \
                    min(row_maxes[i], column_maxes[j])
        return height_increase
