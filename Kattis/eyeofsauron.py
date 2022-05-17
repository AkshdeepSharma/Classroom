def main():
    sauron = input()
    if len(sauron) % 2 == 1 or sauron[len(sauron) // 2 - 1] != "(":
        print("fix")
    else:
        print("correct")


if __name__ == "__main__":
    main()
