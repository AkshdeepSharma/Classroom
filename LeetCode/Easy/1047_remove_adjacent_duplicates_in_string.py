class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            stack.append(char)
            if len(stack) > 1:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
        return "".join(stack)