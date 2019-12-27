class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split(' ')
        list_s = list(reversed(list_s))
        s = " ".join(list_s)
        return " ".join(s.split())