class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')' and stack:
                stack.pop()
            elif char == ')':
                s[i] = ""
        for index in stack:
            s[index] = ""
        return "".join(s)
