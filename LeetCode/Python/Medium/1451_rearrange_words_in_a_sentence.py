class Solution:
    def arrangeWords(self, text: str) -> str:
        curr_max_length = 0
        lexicon = {}
        new_sentence_list = []
        for word in text.split():
            if len(word) not in lexicon:
                curr_max_length = max(curr_max_length, len(word))
                lexicon[len(word)] = [word.lower()]
            else:
                lexicon[len(word)].append(word.lower())
        for i in range(1, curr_max_length + 1):
            if i in lexicon:
                new_sentence_list.extend(lexicon[i])
        new_sentence_list[0] = new_sentence_list[0].capitalize()
        return " ".join(new_sentence_list)
