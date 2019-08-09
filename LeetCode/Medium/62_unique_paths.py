class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dpMatrix = [[1 for col in range(m)] for row in range(n)]
        print(dpMatrix)
        for col in range(1, m):
            for row in range(1, n):
                dpMatrix[row][col] = dpMatrix[row - 1][col] + dpMatrix[row][col - 1]
        return dpMatrix[-1][-1]