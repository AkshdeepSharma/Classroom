class Solution:
    def maximumWealth(self, accounts):
        richest = 0
        for banks in accounts:
            richest = max(richest, sum(banks))
        return richest
