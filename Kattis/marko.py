def findAllWords(words, phone_input):
    duplicate_words = 0
    numbers_to_letters = {
        '2': {'a', 'b', 'c'},
        '3': {'d', 'e', 'f'},
        '4': {'g', 'h', 'i'},
        '5': {'j', 'k', 'l'},
        '6': {'m', 'n', 'o'},
        '7': {'p', 'q', 'r', 's'},
        '8': {'t', 'u', 'v'},
        '9': {'w', 'x', 'y', 'z'}
    }
    phone_input_characters = [numbers_to_letters[num] for num in phone_input]
    for word in words:
        good_word = True
        if len(word) != len(phone_input):
            continue
        for i in range(len(word)):
            if word[i] not in phone_input_characters[i]:
                good_word = False
                break
        if good_word:
            duplicate_words += 1
    return duplicate_words


def main():
    N = int(input())
    words = set([input() for _ in range(N)])
    phone_input = input()
    print(findAllWords(words, phone_input))


if __name__ == "__main__":
    main()
