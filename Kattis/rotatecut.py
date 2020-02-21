def getSlicedSentence(rotates, sentence):
    length_sentence = len(sentence)
    amount_cut_from_front = amount_cut_from_back = 0
    for i in range(rotates):
        if length_sentence <= 3:
            break
        amount_to_cut = length_sentence // 4
        if i % 2 == 0:
            amount_cut_from_front += amount_to_cut
        else:
            amount_cut_from_back += amount_to_cut
        length_sentence -= amount_to_cut
    return sentence[amount_cut_from_front:len(sentence) - amount_cut_from_back]


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        number_of_rotates, sentence = input().split()
        print(getSlicedSentence(int(number_of_rotates), sentence))


if __name__ == "__main__":
    main()
