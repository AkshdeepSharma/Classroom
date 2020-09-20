class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        num_spaces = len(text) - len("".join(words))
        if len(words) == 1:
            return words[0] + " " * num_spaces
        spaces_between_words = num_spaces // (len(words) - 1)
        extra_spaces = num_spaces % (len(words) - 1)
        return (" " * spaces_between_words).join(words) + " " * extra_spaces
