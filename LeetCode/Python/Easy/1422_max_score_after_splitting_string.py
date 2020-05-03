class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = ones = 0
        score = float("-inf")
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1
            score = max(score, zeroes + ones)
        return score - ones + (1 if s[-1] == '1' else 0)
