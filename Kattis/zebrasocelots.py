def main():
    num_animals = int(input())
    bell_count = 0
    for i in range(num_animals):
        if input() == "O":
            bell_count += 2 ** (num_animals - i - 1)
    print(bell_count)


if __name__ == "__main__":
    main()
