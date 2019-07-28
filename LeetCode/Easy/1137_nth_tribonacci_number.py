class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        elif n <= 2:
            return b
        for i in range(n - 2):
            a, b, c = b, c, a + b + c
        return c