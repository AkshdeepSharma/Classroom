class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0
        for p in S:
            if p == '(':
                stack.append(p)
            elif p == ')' and stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(p)
                    res += 1
            else:
                res += 1
        res += len(stack)
        return res