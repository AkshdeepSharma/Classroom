class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = set()
        for c in sentence:
            alpha.add(c)
        return True if len(alpha) == 26 else False
