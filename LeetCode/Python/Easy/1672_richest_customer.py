class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for banks in accounts:
            richest = max(richest, sum(banks))
        return richest
