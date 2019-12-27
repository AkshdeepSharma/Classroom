class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            max_sum = max(max_sum, nums[i])
        return max_sum