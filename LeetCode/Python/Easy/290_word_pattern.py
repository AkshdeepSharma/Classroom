class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        d_word, d_pattern = {}, {}
        
        for i, char in enumerate(pattern):
            if d_pattern.get(char, -1) != d_word.get(words[i], -1):
                return False
            d_pattern[char] = d_word[words[i]] = i
        return True