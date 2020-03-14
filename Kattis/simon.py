def simonSays(sentence):
    if " ".join(sentence[:2]) == "simon says":
        return(" ".join(sentence[2:]))
    return " "


def main():
    T = int(input())
    for _ in range(T):
        sentence = input().split()
        print(simonSays(sentence))


if __name__ == "__main__":
    main()
