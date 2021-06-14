class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[len(nums) - i - 1])
        return ans
