class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decreasing_count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i -1]:
                if decreasing_count > 0:
                    return False
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                decreasing_count += 1
        return True


"""
THIS PROBLEM IS NOT EASY. IT SHOULD BE A MEDIUM >:(
"""