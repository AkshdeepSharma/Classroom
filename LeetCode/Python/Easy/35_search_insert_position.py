class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            if nums[mid] < target:
                lower = mid + 1
            elif nums[mid] >= target:
                upper = mid - 1
        return lower