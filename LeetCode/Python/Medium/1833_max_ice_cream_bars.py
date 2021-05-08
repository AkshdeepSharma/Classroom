class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total_bars = 0
        for bar in sorted(costs):
            if bar > coins:
                return total_bars
            total_bars += 1
            coins -= bar
        return total_bars
