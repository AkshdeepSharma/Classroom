def main():
    word = set(list(input()))
    alphabet = input()
    guesses = 0
    for letter in alphabet:
        if letter in word:
            word.discard(letter)
        else:
            guesses += 1
        if guesses == 10:
            print("LOSE")
            break
        if len(word) == 0:
            print("WIN")
            break


if __name__ == "__main__":
    main()
