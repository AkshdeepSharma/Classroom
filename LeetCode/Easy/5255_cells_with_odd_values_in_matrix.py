class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        grid = [[0] * m for _ in range(n)]
        res = 0
        for i in range(len(indices)):
            for j in range(len(indices[i])):
                num = indices[i][j]
                if j == 0:
                    for x in range(len(grid[num])):
                        grid[num][x] += 1
                else:
                    for x in range(len(grid)):
                        grid[x][num] += 1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] % 2 == 1:
                    res += 1
        return res
