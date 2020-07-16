class Solution:
    def printVertically(self, s: str) -> List[str]:
        max_len = -1
        ans = []
        s = s.split()
        for i in range(len(s)):
            max_len = max(max_len, len(s[i]))
            s[i] = list(s[i])
        for i in range(len(s)):
            if len(s[i]) < max_len:
                s[i].extend([" "] * (max_len - len(s[i])))
        ans = list(zip(*s))
        for i in range(len(ans)):
            ans[i] = "".join(list(ans[i])).rstrip()
        return ans
