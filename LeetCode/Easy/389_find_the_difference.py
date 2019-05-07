class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for c in t:
            if c in dict:
                dict[c] -= 1
                if dict[c] == -1:
                    return c
            else:
                return c