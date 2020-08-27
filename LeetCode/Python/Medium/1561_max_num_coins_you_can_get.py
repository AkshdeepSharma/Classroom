class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        max_coins = 0
        piles = sorted(piles)
        for i in range(len(piles) // 3, len(piles), 2):
            max_coins += piles[i]
        return max_coins
