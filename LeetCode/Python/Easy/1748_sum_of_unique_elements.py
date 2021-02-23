class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        seen = [0] * 101
        for num in nums:
            if seen[num] == 0:
                seen[num] += 1
                ans += num
            elif seen[num] == 1:
                seen[num] += 1
                ans -= num
        return ans
