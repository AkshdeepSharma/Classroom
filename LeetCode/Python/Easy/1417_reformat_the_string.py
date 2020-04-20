class Solution:
    def reformat(self, s: str) -> str:
        a = []
        b = []
        ans = []
        for c in s:
            if c.isalpha():
                a.append(c)
            else:
                b.append(c)
        if len(a) < len(b):
            a, b = b, a
        if len(a) - len(b) > 1:
            return ""
        for i in range(len(a) + len(b)):
            if i % 2 == 0:
                ans.append(a[i // 2])
            else:
                ans.append(b[i // 2])
        return "".join(ans)