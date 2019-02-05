class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        S = 0
        res = []
        for val in A:
            if val % 2 == 0:
                S += val

        for x, y in queries:
            if A[y] % 2 == 0:
                S -= A[y]
            A[y] += x
            if A[y] % 2 == 0:
                S += A[y]
            res.append(S)
        return res