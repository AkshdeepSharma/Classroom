class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = max_sum = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum