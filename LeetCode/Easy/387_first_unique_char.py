class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letters = []
        for l in alphabet:
            if s.count(l) == 1:
                letters.append(s.index(l))
        if len(letters) > 0:
            return min(letters)
        return -1