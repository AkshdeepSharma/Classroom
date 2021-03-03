class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []
        for i in range(min(len(word1), len(word2))):
            word3.append(word1[i])
            word3.append(word2[i])
        return "".join(word3) + word1[i+1:] + word2[i+1:]
