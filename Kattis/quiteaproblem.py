def checkIfStatementHasProblem(string):
    for word in string:
        if 'problem' in word.lower():
            return 'yes'
    return 'no'


def main():
    try:
        while True:
            string = input().split()
            print(checkIfStatementHasProblem(string))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
