from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1
        for c in t:
            if c in chars and chars[c] > 0:
                chars[c] -= 1
            else:
                return False
        for count in chars.values():
            if count != 0:
                return False
        return True