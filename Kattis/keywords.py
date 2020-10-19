def main():
    keywords = []
    for _ in range(int(input())):
        keywords.append(input().lower().replace('-', ' '))
    print(len(set(keywords)))


if __name__ == "__main__":
    main()
