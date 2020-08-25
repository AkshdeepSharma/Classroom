class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        for key, val in d.items():
            ans += (val * (val - 1)) // 2
        return ans
