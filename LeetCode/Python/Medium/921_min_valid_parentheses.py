class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0
        for c in S:
            if c == "(":
                stack.append(c)
            elif c == ")" and stack:
                stack.pop()
            else:
                res += 1
        return res + len(stack)
