from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        chars = Counter(chars)
        ans = 0
        for word in words:
            if not Counter(word) - chars:
                ans += len(word)
        return ans