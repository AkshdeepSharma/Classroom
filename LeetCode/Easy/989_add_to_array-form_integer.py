class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        for i in reversed(range(len(A))):
            A[i], K = (A[i] + K) % 10, (A[i] + K) // 10
        return list(map(int, str(K)) + A) if K else A