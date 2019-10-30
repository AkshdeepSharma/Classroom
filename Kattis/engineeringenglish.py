duplicate_words = {}

try:
    while True:
        sentence = input().split()
        for i, word in enumerate(sentence):
            if word.lower() in duplicate_words:
                sentence[i] = "."
            else:
                duplicate_words[word.lower()] = 1
        print(" ".join(sentence))
except EOFError:
    pass
