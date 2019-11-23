class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        partition_index = 0
        val = A[partition_index]
        curr_max = val
        for i in range(len(A)):
            curr_max = max(curr_max, A[i])
            if A[i] < val:
                partition_index = i
                val = curr_max
        return partition_index + 1
