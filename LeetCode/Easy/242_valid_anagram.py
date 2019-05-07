class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        chars = {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        for ch in t:
            if ch in chars:
                chars[ch] -= 1
            else:
                return False

        for count in chars.itervalues():
            if count != 0:
                return False
        return True