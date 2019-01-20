class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for num in A:
            result.append(num ** 2)
        return sorted(result)
    