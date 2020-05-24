class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        searchWordLen = len(searchWord)
        for i in range(len(sentence)):
            if sentence[i][:searchWordLen] == searchWord:
                return i + 1
        return -1