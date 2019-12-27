class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        RLRRLLRLRL
        """
        res = 0
        balance = 0
        for c in s:
            if c == "R":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res += 1
        return res