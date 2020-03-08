def makeNumberWord(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    if num == 0:
        return 'zero'
    if num < 20:
        return ones[num]
    ten, one = num // 10, num % 10
    if one > 0:
        return tens[ten] + "-" + ones[one]
    return tens[ten]


def main():
    try:
        while True:
            sentence = input().split()
            for i in range(len(sentence)):
                if sentence[i].isdigit():
                    word = makeNumberWord(int(sentence[i]))
                    sentence[i] = word
            print(" ".join(sentence))
    except EOFError:
        pass


if __name__ == "__main__":
    main()
