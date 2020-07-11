class Solution:
    def validPalindrome(self, word: str) -> bool:
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                fromLeft, fromRight = word[i+1:j+1], word[i:j]
                return fromLeft == fromLeft[::-1] or fromRight == fromRight[::-1]
            i, j = i + 1, j - 1
        return True
