class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for key, val in d.items():
            res += (val // 2) * 2
            d[key] = val % 2
            if d[key] == 0:
                d.pop(key)
        if d:
            return res + 1
        return res