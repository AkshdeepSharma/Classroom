def minimumGuess(number, questions):
    if 2 ** questions >= number:
        return "Your wish is granted!"
    return "You will become a flying monkey!"


def main():
    number, questions = map(int, input().split())
    print(minimumGuess(number, questions))


if __name__ == "__main__":
    main()
