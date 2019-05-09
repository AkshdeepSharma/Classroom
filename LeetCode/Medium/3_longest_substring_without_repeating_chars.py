class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        s = list(s)
        print(s)
        dict = {}
        i = j = 0
        while j < len(s):
            if s[j] in dict:
                longest_substring = max(longest_substring, len(dict))
                dict = {}
                i += 1
                j = i
            dict[s[j]] = 1
            j += 1
        return max(longest_substring, len(dict))