class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        res = 0
        for c in text:
            if c in balloon:
                balloon[c] += 1
        return min(balloon['b'], balloon['a'], balloon['n'], balloon['l'] // 2, balloon['o'] // 2)