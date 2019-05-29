from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common_chars = Counter(A[0])
        for word in A[1:]:
            common_chars &= Counter(word)
        return list(common_chars.elements())