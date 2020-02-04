class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        count = len(s)
        for c in s:
            while j < len(t):
                if t[j] == c:
                    count -= 1
                    j += 1
                    break
                j += 1
        return count == 0
