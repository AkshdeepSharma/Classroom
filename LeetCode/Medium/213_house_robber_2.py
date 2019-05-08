class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def _rob(nums):
            a, b = 0, 0
            for i in range(len(nums)):
                a, b = b, max(b, a + nums[i])
            return b
        a, b = _rob(nums[1:]), _rob(nums[:-1])
        return max(a, b)