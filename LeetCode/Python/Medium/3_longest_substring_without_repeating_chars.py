class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start = 0
        longest_substring_length = 0
        for i, char in enumerate(s):
            if char in dic and start < dic[char] + 1:
                start = dic[char] + 1
            dic[char] = i
            longest_substring_length = max(longest_substring_length, i - start + 1)
        return longest_substring_length