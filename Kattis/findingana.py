def main():
    word = input()
    for i in range(len(word)):
        if word[i] == "a":
            print(word[i:])
            break


if __name__ == "__main__":
    main()
