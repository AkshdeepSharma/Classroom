class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for c in s:
            if c in d.keys():
                stack.append(c)
            elif not stack and c in d.values():
                return False
            elif c == d[stack.pop()]:
                pass
            else:
                return False
        return not stack