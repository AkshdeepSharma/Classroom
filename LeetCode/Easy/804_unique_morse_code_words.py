class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {
            'a': ".-",
            'b': "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--.."
        }
        for i in range(len(words)):
            temp = ""
            for c in words[i]:
                temp += morse[c]
            words[i] = temp
        return len(set(words))