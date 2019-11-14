def check_duplicates(sentence_list):
    if len(sentence_list) == len(set(sentence_list)):
        return "yes"
    return "no"


def main():
    sentence_list = input().split()
    print(check_duplicates(sentence_list))


if __name__ == "__main__":
    main()
