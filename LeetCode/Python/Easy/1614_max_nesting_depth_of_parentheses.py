class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = curr_depth = 0
        for c in s:
            if c == '(':
                stack.append(c)
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif c == ')':
                stack.pop()
                curr_depth -= 1
        return max_depth
