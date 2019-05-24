from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dictA = defaultdict(int)
        dictB = defaultdict(int)
        res = []
        A, B = A.split(), B.split()
        for word in A:
            dictA[word] += 1
        for word in B:
            dictB[word] += 1
        for word, val in dictA.items():
            if val == 1 and word not in dictB:
                res.append(word)
        for word, val in dictB.items():
            if val == 1 and word not in dictA:
                res.append(word)
        return res