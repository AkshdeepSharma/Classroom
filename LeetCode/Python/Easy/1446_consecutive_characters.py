class Solution:
    def maxPower(self, s: str) -> int:
        best = curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1
            best = max(curr, best)
        return best
