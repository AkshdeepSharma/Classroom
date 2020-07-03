class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word in (word.upper(), word.lower(), word.capitalize()) else False
