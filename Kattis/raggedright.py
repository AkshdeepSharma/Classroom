def calculateRaggednessScore(max_sentence_length, lines):
    raggedness_score = 0
    for i in range(len(lines) - 1):
        raggedness_score += (max_sentence_length - len(lines[i])) ** 2
    return raggedness_score


def main():
    lines = []
    max_sentence_length = 0
    try:
        while True:
            sentence = input()
            lines.append(sentence)
            max_sentence_length = max(max_sentence_length, len(sentence))
    except EOFError:
        pass
    print(calculateRaggednessScore(max_sentence_length, lines))


if __name__ == "__main__":
    main()
