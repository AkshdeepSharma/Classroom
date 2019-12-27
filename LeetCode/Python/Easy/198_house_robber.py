class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for house in nums:
            a, b = max(a, b), max(a, a + house)
        return max(a, b)