class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curr = 0
        for i, val in enumerate(nums):
            if curr < i:
                return False
            curr = max(i + val, curr)
        return True