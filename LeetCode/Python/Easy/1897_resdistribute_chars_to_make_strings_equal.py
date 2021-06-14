class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        words = "".join(words)
        d = {}
        for c in words:
            if c not in d:
                d[c] = 0
            d[c] += 1
        for key, val in d.items():
            if val % length != 0:
                return False
        return True
