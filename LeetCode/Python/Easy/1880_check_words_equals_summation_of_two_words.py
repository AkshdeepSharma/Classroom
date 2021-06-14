class Solution:
    def isSumEqual(self, first_word: str, second_word: str, target_word: str) -> bool:
        def convertWordToNum(word):
            word_num = []
            for c in word:
                word_num.append(str(ord(c) - 97))
            return int("".join(word_num))
        return convertWordToNum(first_word) + convertWordToNum(second_word) == convertWordToNum(target_word)
