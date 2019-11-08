class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i, c in enumerate(s):
            if c in d:
                if d[c] != t[i]:
                    return False
            else:
                d[c] = t[i]
        return True if len(set(s)) == len(set(t)) else False

        """
        1 liner
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        """
