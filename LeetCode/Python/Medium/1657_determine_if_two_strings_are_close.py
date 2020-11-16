class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dict1, dict2 = {}, {}
        for c in word1:
            if c not in dict1:
                dict1[c] = 0
            dict1[c] += 1
        for c in word2:
            if c not in dict1:
                return False
            if c not in dict2:
                dict2[c] = 0
            dict2[c] += 1
        return sorted(dict1.values()) == sorted(dict2.values())
