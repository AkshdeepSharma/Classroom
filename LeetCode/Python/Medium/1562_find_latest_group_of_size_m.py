class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        dp = [0] * (len(arr) + 2)
        ans = -1
        for i, val in enumerate(arr):
            left, right = dp[val - 1], dp[val + 1]
            if left == m or right == m:
                ans = i
            dp[val - left] = dp[val + right] = left + right + 1
        return ans
