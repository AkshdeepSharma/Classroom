class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and c.isupper() and ord(c) == ord(stack[-1]) - 32:
                stack.pop()
            elif stack and c.islower() and ord(c) == ord(stack[-1]) + 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
