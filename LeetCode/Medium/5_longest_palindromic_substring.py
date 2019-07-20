class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(len(s)):
            odd = self.checkPalindrome(s, i, i)
            even = self.checkPalindrome(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res
        
    def checkPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]