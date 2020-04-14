def main():
    count = 0
    for i in range(int(input())):
        button_colour = input().lower()
        if 'pink' in button_colour or 'rose' in button_colour:
            count += 1
    if count == 0:
        print("I must watch Star Wars with my daughter")
    else:
        print(count)


if __name__ == "__main__":
    main()
