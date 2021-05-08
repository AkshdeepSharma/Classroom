class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        for coin in sorted(coins):
            if coin > ans:
                return ans
            ans += coin
        return ans
