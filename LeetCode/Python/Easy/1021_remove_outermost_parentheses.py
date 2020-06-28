class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        def checkVal(ans, val, paren):
            if val != 0:
                ans.append(paren)
            return ans
        ans = []
        val = 0
        for paren in S:
            if paren == '(':
                checkVal(ans, val, paren)
                val += 1
            else:
                val -= 1
                checkVal(ans, val, paren)
        return "".join(ans)
