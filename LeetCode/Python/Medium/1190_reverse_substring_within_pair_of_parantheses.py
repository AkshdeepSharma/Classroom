class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else:
                stack[-1] += c
        return stack[-1]