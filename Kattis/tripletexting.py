def main():
    d = set()
    text = input()
    length = len(text)
    w1 = text[0:length // 3]
    w2 = text[length // 3:2 * (length // 3)]
    w3 = text[2 * (length // 3):]
    d.add(w1)
    if w2 in d:
        print(w2)
    else:
        print(w3)


if __name__ == "__main__":
    main()
