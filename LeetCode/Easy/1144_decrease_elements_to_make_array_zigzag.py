import copy
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return 0
        count = 0
        temp = copy.copy(nums)
        for i in range(1, len(nums), 2):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1
            if i + 1 < len(nums) and nums[i] <= nums[i + 1]:
                count += nums[i + 1] - nums[i] + 1
                nums[i + 1] = nums[i] - 1
        res, count = count, 0
        nums = temp
        for i in range(1, len(nums), 2):
            if nums[i] >= nums[i - 1]:
                count += nums[i] - nums[i - 1] + 1
                nums[i] = nums[i - 1] - 1
            if i + 1 < len(nums) and nums[i] >= nums[i + 1]:
                count += nums[i] - nums[i + 1] + 1
                nums[i] = nums[i + 1] - 1
        return min(res, count)