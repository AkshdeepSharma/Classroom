class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        val = 0
        for c in t:
            val += ord(c)
        for c in s:
            val -= ord(c)
        return chr(val)
