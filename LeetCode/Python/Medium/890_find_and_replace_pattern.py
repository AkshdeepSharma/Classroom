from collections import OrderedDict


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        pattern_dict = OrderedDict()
        for i, char in enumerate(pattern):
            if char in pattern_dict:
                pattern_dict[char].append(i)
            else:
                pattern_dict[char] = [i]
        for k in range(len(words)):
            word_dict = OrderedDict()
            temp_pattern = []
            temp_word = []
            for i, char in enumerate(words[k]):
                if char in word_dict:
                    word_dict[char].append(i)
                else:
                    word_dict[char] = [i]
            for val in pattern_dict.values():
                temp_pattern.append(val)
            for val in word_dict.values():
                temp_word.append(val)
            if temp_word == temp_pattern:
                res.append(words[k])
        return res
