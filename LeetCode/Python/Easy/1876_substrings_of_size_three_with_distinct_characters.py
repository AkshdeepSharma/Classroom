class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_substrings = 0
        for i in range(len(s) - 2):
            if len(set(list(s[i:i+3]))) == 3:
                good_substrings += 1
        return good_substrings
