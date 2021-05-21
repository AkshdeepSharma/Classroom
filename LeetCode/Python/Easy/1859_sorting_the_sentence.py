class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        ans = [0] * len(s)
        for word in s:
            ans[int(word[-1]) - 1] = word[:-1]
        return " ".join(ans)