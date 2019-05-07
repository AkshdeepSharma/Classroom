class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        to_remove = []
        for i in range(len(S)):
            if count == 0:
                to_remove.append(i)
            if S[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                to_remove.append(i)
        curr = len(to_remove) - 1
        S = list(S)
        for i in reversed(range(len(S))):
            if i == to_remove[curr]:
                del S[i]
                curr -=1
        S = ''.join(S)
        return S