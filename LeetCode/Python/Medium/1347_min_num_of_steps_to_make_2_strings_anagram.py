class Solution:
    def minSteps(self, s: str, t: str) -> int:
        word_count = {}
        count = 0
        for c in s:
            if c in word_count:
                word_count[c] += 1
            else:
                word_count[c] = 1
        for c in t:
            if c in word_count and word_count[c] > 0:
                word_count[c] -= 1
            else:
                count += 1
        return count
