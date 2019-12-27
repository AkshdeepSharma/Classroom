from collections import defaultdict


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        letters = defaultdict(int)
        res = []
        for c in T:
            letters[c] += 1
        for char in S:
            if char in letters:
                res += [char] * letters[char]
                letters.pop(char)
        for key, val in letters.items():
            res += [key] * val
        return "".join(res)
