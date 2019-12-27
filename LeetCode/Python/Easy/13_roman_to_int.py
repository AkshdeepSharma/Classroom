class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        translate = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num += translate.get(s[-1])
        for char in reversed(range(len(s) - 1)):
            if translate.get(s[char + 1]) > translate.get(s[char]):
                num -= translate[s[char]]
            else:
                num += translate[s[char]]
        return num