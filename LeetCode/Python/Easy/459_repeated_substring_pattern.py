class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = (s + s)[1:-1]
        return True if s in ss else False
